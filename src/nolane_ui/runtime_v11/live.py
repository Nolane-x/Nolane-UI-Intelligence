"""Transactional, recoverable protocol core for NUI V11 Live Lab."""
from __future__ import annotations

import copy
import os
import re
import tempfile
from pathlib import Path
from typing import Any

from .evidence import sha256_file

_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
_STATES = frozenset({
    "SELECTED", "CONTEXT_BOUND", "VARIANTS_READY", "PREVIEWING",
    "ACCEPTED", "DISCARDED", "APPLIED", "REOBSERVED", "RECOVERY",
    "FAILED", "CLOSED",
})
_TERMINAL = frozenset({"FAILED", "CLOSED"})
_TRANSITIONS: dict[tuple[str, str], str] = {
    ("SELECTED", "bind_context"): "CONTEXT_BOUND",
    ("CONTEXT_BOUND", "variants_ready"): "VARIANTS_READY",
    ("VARIANTS_READY", "preview_started"): "PREVIEWING",
    ("PREVIEWING", "accept"): "ACCEPTED",
    ("PREVIEWING", "discard"): "DISCARDED",
    ("ACCEPTED", "apply"): "APPLIED",
    ("APPLIED", "reobserve"): "REOBSERVED",
    ("REOBSERVED", "close"): "CLOSED",
    ("DISCARDED", "close"): "CLOSED",
    ("RECOVERY", "resume_preview"): "PREVIEWING",
}


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _next_state(state: str, event_type: str) -> str:
    if event_type == "interrupt":
        # Recovery is a preview-transport concern. Once a variant has been
        # accepted/applied, rewinding into PREVIEWING would make the journal
        # claim a state that no longer matches the mutated source tree.
        if state != "PREVIEWING":
            raise ValueError(f"live event interrupt is invalid from {state}")
        return "RECOVERY"
    if event_type == "fail":
        if state in _TERMINAL:
            raise ValueError(f"live event fail is invalid from terminal state {state}")
        return "FAILED"
    target = _TRANSITIONS.get((state, event_type))
    if target is None:
        raise ValueError(f"live event {event_type} is invalid from {state}")
    return target


def create_live_session(
    *,
    session_id: str,
    target: str,
    selected_source_digest: str,
) -> dict[str, Any]:
    if not _text(session_id):
        raise ValueError("live session requires session_id")
    if not _text(target):
        raise ValueError("live session requires target")
    if not isinstance(selected_source_digest, str) or not _SHA256.match(selected_source_digest):
        raise ValueError("live session selected_source_digest must be sha256:<64 hex>")
    return {
        "version": 11,
        "session_id": session_id.strip(),
        "target": target.strip(),
        "selected_source_digest": selected_source_digest,
        "state": "SELECTED",
        "events": [],
    }


def append_live_event(
    session: dict[str, Any],
    event_type: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    validation = validate_live_session(session)
    if not validation["valid"]:
        raise ValueError("invalid live session: " + "; ".join(validation["errors"]))
    if not _text(event_type):
        raise ValueError("live event requires event_type")
    if payload is not None and not isinstance(payload, dict):
        raise ValueError("live event payload must be an object")

    current_state = str(session["state"])
    target_state = _next_state(current_state, event_type)
    updated = copy.deepcopy(session)
    seq = len(updated["events"]) + 1
    updated["events"].append({
        "seq": seq,
        "type": event_type,
        "from_state": current_state,
        "to_state": target_state,
        "payload": dict(payload or {}),
    })
    updated["state"] = target_state
    return updated


def validate_live_session(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["live session must be an object"]}
    if record.get("version") != 11:
        errors.append("live session must declare version 11")
    for field in ("session_id", "target"):
        if not _text(record.get(field)):
            errors.append(f"live session requires {field}")
    digest = record.get("selected_source_digest")
    if not isinstance(digest, str) or not _SHA256.match(digest):
        errors.append("live session selected_source_digest must be sha256:<64 hex>")
    state = record.get("state")
    if state not in _STATES:
        errors.append(f"live session has invalid state {state}")
    events = record.get("events")
    if not isinstance(events, list):
        return {"valid": False, "errors": errors + ["live session events must be a list"]}

    replay = "SELECTED"
    for index, event in enumerate(events, start=1):
        if not isinstance(event, dict):
            errors.append(f"live event[{index}] must be an object")
            continue
        if event.get("seq") != index:
            errors.append(f"live event[{index}] must have contiguous seq {index}")
        event_type = event.get("type")
        if not _text(event_type):
            errors.append(f"live event[{index}] requires type")
            continue
        if event.get("from_state") != replay:
            errors.append(f"live event[{index}] from_state does not match replay state {replay}")
        try:
            expected = _next_state(replay, str(event_type))
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if event.get("to_state") != expected:
            errors.append(f"live event[{index}] to_state must be {expected}")
        payload = event.get("payload")
        if not isinstance(payload, dict):
            errors.append(f"live event[{index}] payload must be an object")
        replay = expected
    if state in _STATES and replay != state:
        errors.append(f"live session state {state} does not match replay state {replay}")
    return {"valid": not errors, "errors": errors, "event_count": len(events), "replayed_state": replay}


def _conflict_result(
    target: Path,
    expected_digest: str,
    *,
    current_digest: str | None,
    phase: str,
) -> dict[str, Any]:
    return {
        "applied": False,
        "status": "CONFLICT",
        "phase": phase,
        "path": target.as_posix(),
        "expected_digest": expected_digest,
        "current_digest": current_digest,
    }


def transactional_replace(
    path: Path | str,
    expected_digest: str,
    start: int,
    end: int,
    replacement: str,
) -> dict[str, Any]:
    """Replace a character range with optimistic pre-commit source guards.

    The operation performs an initial digest check, prepares the replacement in
    a sibling temporary file, then rechecks source existence and digest
    immediately before the atomic filesystem replace. This deliberately
    refuses known concurrent edits/deletes. It is not a lock-free compare-and-
    swap against an uncooperative writer that races after the final guard.
    """
    target = Path(path)
    if not target.exists() or not target.is_file():
        raise ValueError(f"live transactional target is not a file: {target}")
    if not isinstance(expected_digest, str) or not _SHA256.match(expected_digest):
        raise ValueError("expected_digest must be sha256:<64 hex>")
    if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end < start:
        raise ValueError("transactional replace range must satisfy 0 <= start <= end")
    if not isinstance(replacement, str):
        raise TypeError("transactional replacement must be text")

    current_digest = sha256_file(target)
    if current_digest != expected_digest:
        return _conflict_result(
            target,
            expected_digest,
            current_digest=current_digest,
            phase="initial",
        )

    text = target.read_text(encoding="utf-8")
    if end > len(text):
        raise ValueError(f"transactional replace end {end} exceeds source length {len(text)}")
    updated = text[:start] + replacement + text[end:]

    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=target.parent,
            prefix=f".{target.name}.nui-live-",
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            handle.write(updated)
            handle.flush()
            os.fsync(handle.fileno())

        # The initial digest protects against stale selections. This second
        # guard protects the preparation window itself: if another participant
        # edited or deleted the source while the variant was being staged, do
        # not overwrite/resurrect that state.
        if not target.exists() or not target.is_file():
            return _conflict_result(
                target,
                expected_digest,
                current_digest=None,
                phase="pre-commit",
            )
        precommit_digest = sha256_file(target)
        if precommit_digest != expected_digest:
            return _conflict_result(
                target,
                expected_digest,
                current_digest=precommit_digest,
                phase="pre-commit",
            )

        os.replace(temp_path, target)
        temp_path = None
    finally:
        if temp_path is not None and temp_path.exists():
            temp_path.unlink()

    new_digest = sha256_file(target)
    return {
        "applied": True,
        "status": "APPLIED",
        "path": target.as_posix(),
        "old_digest": current_digest,
        "new_digest": new_digest,
        "range": {"start": start, "end": end},
    }


__all__ = [
    "append_live_event",
    "create_live_session",
    "transactional_replace",
    "validate_live_session",
]
