"""Blinded comparative taste court for V11 Phase 4."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

VERDICTS = {"LEFT", "RIGHT", "TIE", "UNJUDGABLE"}
_FORBIDDEN_JUDGE_KEYS = {
    "generator_preference", "self_score", "beauty_score", "ai_score",
    "reference_brand", "preferred_candidate", "generator_label",
}


def _sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _sanitize(item) for key, item in value.items() if key not in _FORBIDDEN_JUDGE_KEYS}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    return deepcopy(value)


def prepare_blinded_candidates(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(candidates, list) or len(candidates) < 2:
        raise ValueError("taste court requires at least two candidates")
    blinded = []
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            raise ValueError("candidate must be an object")
        clean = _sanitize(candidate)
        original_id = candidate.get("direction_id", f"candidate-{index + 1}")
        clean.pop("direction_id", None)
        clean["court_label"] = "LEFT" if index == 0 else ("RIGHT" if index == 1 else f"ALT_{index + 1}")
        clean["candidate_ref"] = str(original_id)
        blinded.append(clean)
    return {
        "version": 11,
        "candidates": blinded,
        "excluded_fields": sorted(_FORBIDDEN_JUDGE_KEYS),
        "claim_boundary": "blinded-comparison-input-only",
    }


def _contains_forbidden_key(value: Any) -> bool:
    if isinstance(value, dict):
        if any(key in _FORBIDDEN_JUDGE_KEYS for key in value):
            return True
        return any(_contains_forbidden_key(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_forbidden_key(item) for item in value)
    return False


def validate_taste_judgment(judgment: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(judgment, dict):
        return {"valid": False, "errors": ["judgment must be an object"]}
    if _contains_forbidden_key(judgment):
        errors.append("judgment contains forbidden generator/prestige/scalar fields")
    if not isinstance(judgment.get("dimension"), str) or not judgment["dimension"].strip():
        errors.append("dimension must be non-empty")
    if judgment.get("verdict") not in VERDICTS:
        errors.append("verdict is invalid")
    refs = judgment.get("evidence_refs")
    if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or not ref.strip() for ref in refs):
        errors.append("evidence_refs must contain evidence")
    if not isinstance(judgment.get("observable_cause"), str) or not judgment["observable_cause"].strip():
        errors.append("observable_cause must be non-empty")
    preserve = judgment.get("preserve", [])
    if not isinstance(preserve, list):
        errors.append("preserve must be a list when present")
    return {"valid": not errors, "errors": errors}


def aggregate_taste_court(
    judgments: list[dict[str, Any]],
    *,
    hard_blockers: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    if not isinstance(judgments, list) or not judgments:
        raise ValueError("taste court requires judgments")
    for judgment in judgments:
        validation = validate_taste_judgment(judgment)
        if not validation["valid"]:
            raise ValueError("invalid taste judgment: " + "; ".join(validation["errors"]))
    blockers = deepcopy(hard_blockers or [])
    blocked_candidates = {item.get("candidate") for item in blockers if isinstance(item, dict) and item.get("candidate") in {"LEFT", "RIGHT"}}
    if blockers:
        return {
            "status": "BLOCKED",
            "winner": None,
            "hard_blockers": blockers,
            "judgments": deepcopy(judgments),
            "blocked_candidates": sorted(blocked_candidates),
            "claim_boundary": "taste-comparison-only",
        }
    counts = {"LEFT": 0, "RIGHT": 0, "TIE": 0, "UNJUDGABLE": 0}
    for judgment in judgments:
        counts[judgment["verdict"]] += 1
    if counts["LEFT"] > counts["RIGHT"]:
        status, winner = "PREFERENCE", "LEFT"
    elif counts["RIGHT"] > counts["LEFT"]:
        status, winner = "PREFERENCE", "RIGHT"
    elif counts["UNJUDGABLE"]:
        status, winner = "RE_DIVERGE", None
    else:
        status, winner = "TIE", None
    return {
        "status": status,
        "winner": winner,
        "dimension_counts": counts,
        "judgments": deepcopy(judgments),
        "hard_blockers": [],
        "claim_boundary": "taste-comparison-only",
    }


__all__ = ["VERDICTS", "aggregate_taste_court", "prepare_blinded_candidates", "validate_taste_judgment"]
