"""Empirical claim promotion gates for NUI V10."""
from __future__ import annotations

from typing import Any

STATUSES = {"STRUCTURAL_ONLY", "EMPIRICAL_LOCAL", "EMPIRICAL_TRANSFER", "REJECTED"}


def _positive_aggregate(aggregate: dict[str, Any], errors: list[str]) -> bool:
    delta = aggregate.get("paired_delta")
    ci = aggregate.get("ci")
    ok = True
    if not isinstance(delta, (int, float)) or float(delta) <= 0:
        errors.append("empirical claim requires positive paired_delta")
        ok = False
    if not isinstance(ci, (list, tuple)) or len(ci) != 2 or not all(isinstance(x, (int, float)) for x in ci):
        errors.append("empirical claim requires a two-sided confidence interval")
        ok = False
    elif float(ci[0]) <= 0:
        errors.append("confidence interval must exclude zero in the claimed positive direction")
        ok = False
    return ok


def promote_claim(claim: dict[str, Any], aggregate: dict[str, Any], provenance: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    requested = str(claim.get("requested_status", "STRUCTURAL_ONLY")) if isinstance(claim, dict) else "STRUCTURAL_ONLY"
    if requested not in STATUSES:
        errors.append("requested_status is invalid")
        requested = "STRUCTURAL_ONLY"

    if not provenance.get("real_model_runs"):
        errors.append("structural or synthetic fixtures cannot be promoted to empirical evidence")
        return {"status": "STRUCTURAL_ONLY", "errors": errors, "bounded_claim": claim.get("bounded_claim") if isinstance(claim, dict) else None}

    blockers = aggregate.get("hard_blocker_regressions", []) if isinstance(aggregate, dict) else []
    if blockers:
        errors.append(f"hard-blocker regression prevents positive efficacy claim: {blockers}")
        return {"status": "REJECTED", "errors": errors, "bounded_claim": claim.get("bounded_claim") if isinstance(claim, dict) else None}

    empirical_ok = _positive_aggregate(aggregate, errors)
    if provenance.get("ablation_identified") is not True:
        errors.append("attributed efficacy requires targeted ablation identification")
        empirical_ok = False
    if not empirical_ok:
        return {"status": "REJECTED", "errors": errors, "bounded_claim": claim.get("bounded_claim") if isinstance(claim, dict) else None}

    if requested == "EMPIRICAL_TRANSFER":
        families = sorted({str(x) for x in provenance.get("model_families", []) if str(x).strip()})
        if len(families) < 2:
            errors.append("EMPIRICAL_TRANSFER requires at least two model families")
        if provenance.get("holdout") is not True:
            errors.append("EMPIRICAL_TRANSFER requires holdout task evidence")
        directions = aggregate.get("per_model_direction", {})
        if not isinstance(directions, dict) or len(directions) < 2:
            errors.append("EMPIRICAL_TRANSFER requires per-model direction evidence")
        elif any(not isinstance(v, (int, float)) or float(v) <= 0 for v in directions.values()):
            errors.append("EMPIRICAL_TRANSFER cannot hide a contradictory model-family effect in pooled averaging")
        if not errors:
            return {"status": "EMPIRICAL_TRANSFER", "errors": [], "bounded_claim": claim.get("bounded_claim"), "model_families": families}
        return {"status": "EMPIRICAL_LOCAL", "errors": errors, "bounded_claim": claim.get("bounded_claim"), "model_families": families}

    if requested == "REJECTED":
        return {"status": "REJECTED", "errors": ["claim explicitly requested rejection"], "bounded_claim": claim.get("bounded_claim")}
    if requested in {"EMPIRICAL_LOCAL", "STRUCTURAL_ONLY"}:
        return {"status": "EMPIRICAL_LOCAL" if requested == "EMPIRICAL_LOCAL" else "STRUCTURAL_ONLY", "errors": errors, "bounded_claim": claim.get("bounded_claim")}
    return {"status": "STRUCTURAL_ONLY", "errors": errors, "bounded_claim": claim.get("bounded_claim")}


def validate_claim(record: dict[str, Any], aggregate: dict[str, Any], provenance: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["claim must be an object"]}
    for field in ("claim_id", "dimension", "bounded_claim"):
        if not isinstance(record.get(field), str) or not record.get(field).strip():
            errors.append(f"claim requires {field}")
    promoted = promote_claim(record, aggregate, provenance)
    return {"valid": not errors and promoted["status"] != "REJECTED", "errors": errors + promoted["errors"], "status": promoted["status"]}


__all__ = ["promote_claim", "validate_claim", "STATUSES"]
