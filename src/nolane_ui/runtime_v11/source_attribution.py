"""Fail-closed rendered-element to source attribution for NUI V11 Phase 5."""
from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any

from .evidence import sha256_file

_ATTRIBUTION_STATES = ("EXACT", "CANDIDATE", "AMBIGUOUS", "UNKNOWN")
_CONFIDENCE = ("LOW", "MEDIUM", "HIGH")
_CONFIDENCE_RANK = {name: index for index, name in enumerate(_CONFIDENCE)}
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_text(item) for item in value)


def _inside_root(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _normalize_range(value: Any) -> dict[str, int] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        return None
    start = value.get("start")
    end = value.get("end")
    if isinstance(start, bool) or isinstance(end, bool):
        return None
    if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end < start:
        return None
    return {"start": start, "end": end}


def _base_record(rendered_identity: dict[str, Any]) -> dict[str, Any]:
    return {
        "version": 11,
        "status": "UNKNOWN",
        "rendered_identity": copy.deepcopy(rendered_identity),
        "candidates": [],
        "failures": [],
        "mutation_authorized": False,
        "selected_candidate_id": None,
        "selection_authority": None,
        "claim_boundary": "source-attribution-only",
    }


def validate_source_attribution(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["source attribution must be an object"], "candidate_count": 0}
    if record.get("version") != 11:
        errors.append("source attribution must declare version 11")
    if record.get("status") not in _ATTRIBUTION_STATES:
        errors.append("source attribution status must be EXACT, CANDIDATE, AMBIGUOUS, or UNKNOWN")
    identity = record.get("rendered_identity")
    if not isinstance(identity, dict) or not _text(identity.get("locator")):
        errors.append("source attribution requires rendered_identity.locator")
    candidates = record.get("candidates")
    if not isinstance(candidates, list):
        errors.append("source attribution candidates must be a list")
        candidates = []
    else:
        seen: set[str] = set()
        for index, candidate in enumerate(candidates):
            if not isinstance(candidate, dict):
                errors.append(f"source attribution candidate[{index}] must be an object")
                continue
            candidate_id = candidate.get("candidate_id")
            if not _text(candidate_id):
                errors.append(f"source attribution candidate[{index}] requires candidate_id")
            elif candidate_id in seen:
                errors.append(f"source attribution duplicate candidate_id {candidate_id}")
            else:
                seen.add(str(candidate_id))
            if not _text(candidate.get("source_path")):
                errors.append(f"source attribution candidate[{index}] requires source_path")
            digest = candidate.get("source_digest")
            if not isinstance(digest, str) or not _SHA256.match(digest):
                errors.append(f"source attribution candidate[{index}] source_digest must be sha256:<64 hex>")
            if candidate.get("confidence") not in _CONFIDENCE:
                errors.append(f"source attribution candidate[{index}] confidence must be LOW, MEDIUM, or HIGH")
            if not _string_list(candidate.get("attribution_mechanisms")) or not candidate.get("attribution_mechanisms"):
                errors.append(f"source attribution candidate[{index}] requires attribution_mechanisms")
            if not _string_list(candidate.get("evidence_refs")) or not candidate.get("evidence_refs"):
                errors.append(f"source attribution candidate[{index}] requires evidence_refs")
            if candidate.get("range") is not None and _normalize_range(candidate.get("range")) is None:
                errors.append(f"source attribution candidate[{index}] has invalid range")
    failures = record.get("failures")
    if not _string_list(failures):
        errors.append("source attribution failures must be a list of non-empty strings")
    if not isinstance(record.get("mutation_authorized"), bool):
        errors.append("source attribution mutation_authorized must be boolean")
    selected = record.get("selected_candidate_id")
    if selected is not None and not _text(selected):
        errors.append("source attribution selected_candidate_id must be null or non-empty string")
    if record.get("claim_boundary") != "source-attribution-only":
        errors.append("source attribution claim_boundary must be source-attribution-only")
    if record.get("status") == "UNKNOWN" and record.get("mutation_authorized") is True:
        errors.append("UNKNOWN source attribution cannot authorize mutation")
    if record.get("status") == "AMBIGUOUS" and record.get("mutation_authorized") is True:
        errors.append("AMBIGUOUS source attribution cannot authorize mutation")
    if record.get("status") == "CANDIDATE" and record.get("mutation_authorized") is True:
        errors.append("CANDIDATE source attribution requires explicit selection before mutation")
    if record.get("mutation_authorized") is True and not _text(selected):
        errors.append("authorized source attribution requires selected_candidate_id")
    return {"valid": not errors, "errors": errors, "candidate_count": len(candidates)}


def _normalize_candidate(candidate: dict[str, Any], root: Path) -> tuple[dict[str, Any] | None, list[str]]:
    failures: list[str] = []
    if not isinstance(candidate, dict):
        return None, ["ATTRIBUTION_CANDIDATE_INVALID"]
    candidate_id = candidate.get("candidate_id")
    source_path = candidate.get("source_path")
    source_digest = candidate.get("source_digest")
    confidence = candidate.get("confidence")
    mechanisms = candidate.get("attribution_mechanisms")
    evidence_refs = candidate.get("evidence_refs")
    if not _text(candidate_id) or not _text(source_path):
        return None, ["ATTRIBUTION_CANDIDATE_INVALID"]
    if not isinstance(source_digest, str) or not _SHA256.match(source_digest):
        return None, ["ATTRIBUTION_CANDIDATE_INVALID"]
    if confidence not in _CONFIDENCE:
        return None, ["ATTRIBUTION_CANDIDATE_INVALID"]
    if not _string_list(mechanisms) or not mechanisms or not _string_list(evidence_refs) or not evidence_refs:
        return None, ["ATTRIBUTION_CANDIDATE_INVALID"]
    normalized_range = _normalize_range(candidate.get("range"))
    if candidate.get("range") is not None and normalized_range is None:
        return None, ["ATTRIBUTION_CANDIDATE_INVALID"]

    raw = Path(str(source_path))
    target = raw if raw.is_absolute() else root / raw
    try:
        resolved = target.resolve(strict=True)
    except (OSError, RuntimeError):
        return None, ["SOURCE_MISSING"]
    if not resolved.is_file() or not _inside_root(resolved, root):
        return None, ["SOURCE_OUTSIDE_ROOT"]
    current_digest = sha256_file(resolved)
    if current_digest != source_digest:
        return None, ["SOURCE_STALE"]

    relative = resolved.relative_to(root).as_posix()
    normalized: dict[str, Any] = {
        "candidate_id": str(candidate_id).strip(),
        "source_path": relative,
        "source_digest": current_digest,
        "range": normalized_range,
        "attribution_mechanisms": [str(item).strip() for item in mechanisms],
        "evidence_refs": [str(item).strip() for item in evidence_refs],
        "confidence": str(confidence),
    }
    if isinstance(candidate.get("provider_metadata"), dict):
        normalized["provider_metadata"] = copy.deepcopy(candidate["provider_metadata"])
    return normalized, failures


def resolve_source_attribution(
    rendered_identity: dict[str, Any],
    candidates: list[dict[str, Any]],
    *,
    repository_root: str | Path,
) -> dict[str, Any]:
    if not isinstance(rendered_identity, dict) or not _text(rendered_identity.get("locator")):
        raise ValueError("rendered_identity requires a non-empty locator")
    if not isinstance(candidates, list):
        raise TypeError("source attribution candidates must be a list")
    root = Path(repository_root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("repository_root must be a directory")

    record = _base_record(rendered_identity)
    normalized: list[dict[str, Any]] = []
    failures: list[str] = []
    for candidate in candidates:
        item, item_failures = _normalize_candidate(candidate, root)
        failures.extend(item_failures)
        if item is not None:
            normalized.append(item)
    normalized.sort(key=lambda item: (str(item["candidate_id"]), str(item["source_path"])))
    record["candidates"] = normalized
    record["failures"] = sorted(set(failures))

    if not normalized:
        validation = validate_source_attribution(record)
        if not validation["valid"]:
            raise AssertionError("internal source attribution record invalid: " + "; ".join(validation["errors"]))
        return record

    top_rank = max(_CONFIDENCE_RANK[str(item["confidence"])] for item in normalized)
    top = [item for item in normalized if _CONFIDENCE_RANK[str(item["confidence"])] == top_rank]
    if len(top) > 1:
        record["status"] = "AMBIGUOUS"
    elif top_rank == _CONFIDENCE_RANK["HIGH"]:
        record["status"] = "EXACT"
        record["selected_candidate_id"] = top[0]["candidate_id"]
        record["mutation_authorized"] = True
        record["selection_authority"] = "evidence-exact"
    else:
        record["status"] = "CANDIDATE"

    validation = validate_source_attribution(record)
    if not validation["valid"]:
        raise AssertionError("internal source attribution record invalid: " + "; ".join(validation["errors"]))
    return record


def select_source_candidate(attribution: dict[str, Any], candidate_id: str) -> dict[str, Any]:
    validation = validate_source_attribution(attribution)
    if not validation["valid"]:
        raise ValueError("invalid source attribution: " + "; ".join(validation["errors"]))
    if attribution["status"] == "UNKNOWN":
        raise ValueError("UNKNOWN source attribution has no selectable mutation target")
    if not _text(candidate_id):
        raise ValueError("candidate_id must be a non-empty string")
    matches = [item for item in attribution["candidates"] if item.get("candidate_id") == candidate_id]
    if len(matches) != 1:
        raise ValueError(f"source attribution candidate not found: {candidate_id}")
    updated = copy.deepcopy(attribution)
    updated["status"] = "EXACT"
    updated["selected_candidate_id"] = candidate_id
    updated["mutation_authorized"] = True
    updated["selection_authority"] = "explicit-candidate-selection"
    validation = validate_source_attribution(updated)
    if not validation["valid"]:
        raise AssertionError("selected source attribution invalid: " + "; ".join(validation["errors"]))
    return updated


__all__ = [
    "resolve_source_attribution",
    "select_source_candidate",
    "validate_source_attribution",
]
