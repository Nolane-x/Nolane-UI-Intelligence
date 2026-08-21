"""Generation-time aesthetic governor for V11 Phase 4.

The governor spends visual freedom inside a validated NUI intent packet. It is
not a style oracle and it cannot promote its own output to verification.
"""
from __future__ import annotations

from copy import deepcopy
from itertools import combinations
from typing import Any

from .aesthetic_intent import validate_aesthetic_intent

CAUSAL_AXES = ("composition", "typography", "density", "material", "media", "motion", "signature")
MIN_CANDIDATES = {"UTILITY": 1, "STANDARD": 1, "HIGH": 2, "FLAGSHIP": 3}


def _identity_conflicts(intent: dict[str, Any], candidate: dict[str, Any]) -> list[str]:
    if intent.get("mode") != "IDENTITY_LOCKED":
        return []
    frozen = set(x for x in intent.get("frozen_axes", []) if isinstance(x, str))
    changes = set(x for x in candidate.get("identity_changes", []) if isinstance(x, str))
    return sorted(frozen & changes)


def _pair_delta(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    return [axis for axis in CAUSAL_AXES if left.get(axis) != right.get(axis)]


def evaluate_direction_candidates(
    intent: dict[str, Any],
    candidates: list[dict[str, Any]],
    capabilities: dict[str, Any] | None = None,
) -> dict[str, Any]:
    validation = validate_aesthetic_intent(intent)
    if not validation["valid"]:
        raise ValueError("invalid aesthetic intent: " + "; ".join(validation["errors"]))
    if not isinstance(candidates, list):
        raise ValueError("candidates must be a list")
    capabilities = capabilities or {}
    assessed: list[dict[str, Any]] = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise ValueError("each candidate must be an object")
        item = deepcopy(candidate)
        conflicts = _identity_conflicts(intent, item)
        item["identity_conflicts"] = conflicts
        item["valid"] = not conflicts
        assessed.append(item)

    valid = [item for item in assessed if item["valid"]]
    pairwise: list[dict[str, Any]] = []
    for left, right in combinations(valid, 2):
        axes = _pair_delta(left, right)
        pairwise.append({"left": left.get("direction_id"), "right": right.get("direction_id"), "causal_axis_deltas": axes, "material": len(axes) >= 2})

    ambition = intent["ambition"]
    required = MIN_CANDIDATES[ambition]
    count_ok = len(valid) >= required
    if len(valid) <= 1:
        divergent = ambition in {"UTILITY", "STANDARD"}
    else:
        divergent = bool(pairwise) and all(item["material"] for item in pairwise)
    render_evidence = "OBSERVED" if capabilities.get("render") is True else "UNKNOWN"

    status = "READY"
    reasons: list[str] = []
    if not count_ok:
        status = "RE_DIVERGE"
        reasons.append(f"{ambition} requires at least {required} valid candidate(s)")
    if ambition in {"HIGH", "FLAGSHIP"} and not divergent:
        status = "RE_DIVERGE"
        reasons.append("candidate set lacks material causal-axis divergence")
    # Missing render capability never becomes an invented pass. It is recorded
    # separately so mechanism-level exploration can proceed without claiming
    # rendered divergence evidence.
    return {
        "status": status,
        "candidates": assessed,
        "valid_candidate_count": len(valid),
        "required_candidate_count": required,
        "pairwise": pairwise,
        "materially_divergent": divergent,
        "render_evidence": render_evidence,
        "reasons": reasons,
        "claim_boundary": "generation-governor-only",
    }


def commit_direction(intent: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    validation = validate_aesthetic_intent(intent)
    if not validation["valid"]:
        raise ValueError("invalid aesthetic intent: " + "; ".join(validation["errors"]))
    if not isinstance(candidate, dict) or not candidate.get("direction_id"):
        raise ValueError("candidate requires direction_id")
    conflicts = _identity_conflicts(intent, candidate)
    if conflicts:
        raise ValueError("candidate violates frozen identity axes: " + ", ".join(conflicts))
    return {
        "version": 11,
        "direction_id": candidate["direction_id"],
        "intent_id": intent["intent_id"],
        "revision": intent["revision"],
        "status": "COMMITTED",
        "thesis": candidate.get("thesis", intent["product_thesis"]),
        "subject_causality": deepcopy(candidate.get("subject_causality", intent.get("subject_anchors", []))),
        "signature_mechanism": candidate.get("signature", intent["signature_mechanism"]),
        "quiet_system": deepcopy(intent["quiet_system"]),
        "frozen_axes": deepcopy(intent["frozen_axes"]),
        "flexible_axes": deepcopy(intent["flexible_axes"]),
        "preserve": deepcopy(intent["preserve"]),
        "known_risks": deepcopy(candidate.get("known_risks", [])),
        "rejection_conditions": deepcopy(intent["rejection_conditions"]),
        "claim_boundary": "committed-direction-only",
    }


__all__ = ["CAUSAL_AXES", "commit_direction", "evaluate_direction_candidates"]
