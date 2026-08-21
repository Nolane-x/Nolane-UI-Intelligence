"""Immutable, non-destructive preview contracts for NUI V11 Phase 5."""
from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any

from .browser import normalize_browser_observation, validate_browser_observation
from .browser_transport import validate_browser_transport_capability
from .evidence import sha256_file

_PREVIEW_STATES = ("PREPARED", "INJECTED", "OBSERVED", "STALE", "CONFLICT", "REJECTED", "ACCEPTED")
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
_ALLOWED_FIELDS = frozenset({
    "version", "preview_id", "session_id", "source_candidate", "base_source_digest",
    "replacement", "preserve_constraints", "direction_id", "provenance",
    "transport_requirements", "state", "capture_refs", "observation", "claim_boundary",
})


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: Any) -> bool:
    return isinstance(value, list) and all(_text(item) for item in value)


def _valid_source_candidate(candidate: Any) -> bool:
    if not isinstance(candidate, dict):
        return False
    if not _text(candidate.get("candidate_id")) or not _text(candidate.get("source_path")):
        return False
    digest = candidate.get("source_digest")
    if not isinstance(digest, str) or not _SHA256.match(digest):
        return False
    source_range = candidate.get("range")
    if source_range is not None:
        if not isinstance(source_range, dict):
            return False
        start, end = source_range.get("start"), source_range.get("end")
        if isinstance(start, bool) or isinstance(end, bool) or not isinstance(start, int) or not isinstance(end, int) or start < 0 or end < start:
            return False
    return True


def validate_preview_candidate(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["preview candidate must be an object"]}
    extra = sorted(set(record) - _ALLOWED_FIELDS)
    if extra:
        errors.append("preview candidate has unsupported fields: " + ", ".join(extra))
    if record.get("version") != 11:
        errors.append("preview candidate must declare version 11")
    for field in ("preview_id", "session_id"):
        if not _text(record.get(field)):
            errors.append(f"preview candidate requires {field}")
    if not _valid_source_candidate(record.get("source_candidate")):
        errors.append("preview candidate requires a valid source_candidate")
    digest = record.get("base_source_digest")
    if not isinstance(digest, str) or not _SHA256.match(digest):
        errors.append("preview candidate base_source_digest must be sha256:<64 hex>")
    elif isinstance(record.get("source_candidate"), dict) and record["source_candidate"].get("source_digest") != digest:
        errors.append("preview candidate base_source_digest must match source_candidate.source_digest")
    if not isinstance(record.get("replacement"), str):
        errors.append("preview candidate replacement must be text")
    if not _strings(record.get("preserve_constraints")):
        errors.append("preview candidate preserve_constraints must be a list of strings")
    direction_id = record.get("direction_id")
    if direction_id is not None and not _text(direction_id):
        errors.append("preview candidate direction_id must be null or non-empty string")
    if not isinstance(record.get("provenance"), dict):
        errors.append("preview candidate provenance must be an object")
    if record.get("transport_requirements") != ["preview_injection", "refresh"]:
        errors.append("preview candidate transport_requirements must be preview_injection + refresh")
    if record.get("state") not in _PREVIEW_STATES:
        errors.append("preview candidate has invalid state")
    if not _strings(record.get("capture_refs")):
        errors.append("preview candidate capture_refs must be a list of strings")
    observation = record.get("observation")
    if observation is not None and not isinstance(observation, dict):
        errors.append("preview candidate observation must be null or object")
    if record.get("state") == "OBSERVED":
        if not isinstance(observation, dict) or observation.get("refresh_status") not in {"HMR_OK", "RELOAD_OK"}:
            errors.append("OBSERVED preview requires successful refresh observation")
    if record.get("claim_boundary") != "preview-transport-only":
        errors.append("preview candidate claim_boundary must be preview-transport-only")
    return {"valid": not errors, "errors": errors}


def build_preview_candidate(
    *,
    preview_id: str,
    session_id: str,
    source_candidate: dict[str, Any],
    replacement: str,
    preserve_constraints: list[str] | None = None,
    direction_id: str | None = None,
    provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not _text(preview_id) or not _text(session_id):
        raise ValueError("preview_id and session_id must be non-empty strings")
    if not _valid_source_candidate(source_candidate):
        raise ValueError("source_candidate is invalid")
    if not isinstance(replacement, str):
        raise TypeError("preview replacement must be text")
    preserve = list(preserve_constraints or [])
    if not _strings(preserve):
        raise ValueError("preserve_constraints must contain non-empty strings")
    if direction_id is not None and not _text(direction_id):
        raise ValueError("direction_id must be null or non-empty string")
    if provenance is not None and not isinstance(provenance, dict):
        raise TypeError("provenance must be an object")
    record = {
        "version": 11,
        "preview_id": preview_id.strip(),
        "session_id": session_id.strip(),
        "source_candidate": copy.deepcopy(source_candidate),
        "base_source_digest": source_candidate["source_digest"],
        "replacement": replacement,
        "preserve_constraints": preserve,
        "direction_id": direction_id.strip() if isinstance(direction_id, str) else None,
        "provenance": copy.deepcopy(provenance or {}),
        "transport_requirements": ["preview_injection", "refresh"],
        "state": "PREPARED",
        "capture_refs": [],
        "observation": None,
        "claim_boundary": "preview-transport-only",
    }
    validation = validate_preview_candidate(record)
    if not validation["valid"]:
        raise AssertionError("internal preview candidate invalid: " + "; ".join(validation["errors"]))
    return record


def assess_preview_freshness(record: dict[str, Any], repository_root: str | Path) -> dict[str, Any]:
    validation = validate_preview_candidate(record)
    if not validation["valid"]:
        raise ValueError("invalid preview candidate: " + "; ".join(validation["errors"]))
    root = Path(repository_root).resolve(strict=True)
    candidate = record["source_candidate"]
    target = (root / candidate["source_path"]).resolve(strict=False)
    try:
        target.relative_to(root)
    except ValueError:
        return {"status": "CONFLICT", "failure": "SOURCE_OUTSIDE_ROOT", "claim_boundary": "preview-transport-only"}
    if not target.exists() or not target.is_file():
        return {"status": "CONFLICT", "failure": "PREVIEW_CONFLICT", "claim_boundary": "preview-transport-only"}
    current = sha256_file(target)
    if current != record["base_source_digest"]:
        return {
            "status": "STALE", "failure": "PREVIEW_STALE",
            "expected_digest": record["base_source_digest"], "current_digest": current,
            "claim_boundary": "preview-transport-only",
        }
    return {"status": "CURRENT", "failure": None, "current_digest": current, "claim_boundary": "preview-transport-only"}


def prepare_preview_application(record: dict[str, Any], transport_capability: dict[str, Any]) -> dict[str, Any]:
    validation = validate_preview_candidate(record)
    if not validation["valid"]:
        raise ValueError("invalid preview candidate: " + "; ".join(validation["errors"]))
    transport_validation = validate_browser_transport_capability(transport_capability)
    if not transport_validation["valid"]:
        raise ValueError("invalid browser transport: " + "; ".join(transport_validation["errors"]))
    if record["state"] != "PREPARED":
        raise ValueError("only PREPARED preview candidates can be injected")
    caps = transport_capability["capabilities"]
    missing: list[str] = []
    if not caps["preview_injection"]:
        missing.append("preview_injection")
    if not (caps["hot_reload"] or caps["reload"]):
        missing.append("refresh")
    if missing:
        return {
            "status": "UNKNOWN",
            "missing_capabilities": missing,
            "preview": copy.deepcopy(record),
            "claim_boundary": "preview-transport-only",
        }
    updated = copy.deepcopy(record)
    updated["state"] = "INJECTED"
    return {
        "status": "READY",
        "missing_capabilities": [],
        "preview": updated,
        "provider": transport_capability["provider"],
        "claim_boundary": "preview-transport-only",
    }


def record_preview_observation(
    record: dict[str, Any],
    *,
    refresh_evidence: dict[str, Any],
    browser_observation: dict[str, Any],
) -> dict[str, Any]:
    validation = validate_preview_candidate(record)
    if not validation["valid"]:
        raise ValueError("invalid preview candidate: " + "; ".join(validation["errors"]))
    if record["state"] != "INJECTED":
        raise ValueError("preview observation requires INJECTED state")
    if not isinstance(refresh_evidence, dict) or refresh_evidence.get("status") not in {"HMR_OK", "RELOAD_OK"}:
        raise ValueError("preview observation requires successful HMR_OK or RELOAD_OK refresh evidence")
    if refresh_evidence.get("candidate_id") != record["preview_id"]:
        raise ValueError("refresh evidence candidate_id does not match preview")
    browser_validation = validate_browser_observation(browser_observation)
    if not browser_validation["valid"]:
        raise ValueError("invalid browser observation: " + "; ".join(browser_validation["errors"]))
    normalized = normalize_browser_observation(browser_observation)
    updated = copy.deepcopy(record)
    updated["state"] = "OBSERVED"
    updated["capture_refs"] = [normalized["capture_ref"]] if normalized.get("capture_ref") else []
    updated["observation"] = {
        "refresh_status": refresh_evidence["status"],
        "revision": refresh_evidence.get("revision"),
        "collector": normalized["collector"],
        "url": normalized["url"],
        "viewport": copy.deepcopy(normalized["viewport"]),
    }
    final_validation = validate_preview_candidate(updated)
    if not final_validation["valid"]:
        raise AssertionError("observed preview candidate invalid: " + "; ".join(final_validation["errors"]))
    return updated


__all__ = [
    "assess_preview_freshness",
    "build_preview_candidate",
    "prepare_preview_application",
    "record_preview_observation",
    "validate_preview_candidate",
]
