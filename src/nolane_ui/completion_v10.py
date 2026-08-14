"""V10 empirical completion evidence.

This validator is deliberately separate from ordinary UI/product completion. It
answers only how far a claim about NUI efficacy may be promoted.
"""
from __future__ import annotations

from typing import Any

STATUSES = {"STRUCTURAL_ONLY", "EMPIRICAL_LOCAL", "EMPIRICAL_TRANSFER", "REJECTED"}


def _sha(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
        return True
    except ValueError:
        return False


def validate_v10_completion_evidence(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["v10 completion evidence must be an object"], "claim_ceiling": "REJECTED"}
    if record.get("version") != 10:
        errors.append("v10 completion evidence requires version 10")
    requested = record.get("claim_ceiling")
    if requested not in STATUSES:
        errors.append(f"claim_ceiling must be one of {sorted(STATUSES)}")
        requested = "REJECTED"

    if requested == "STRUCTURAL_ONLY":
        if record.get("empirical_runs_executed") is not False:
            errors.append("STRUCTURAL_ONLY repository packet must state empirical_runs_executed=false unless importing a separate empirical evidence bundle")
        digests = record.get("imported_empirical_bundle_digests", [])
        if not isinstance(digests, list) or digests:
            errors.append("STRUCTURAL_ONLY repository packet must not imply imported empirical bundles")
        unresolved = record.get("unresolved_empirical_claims")
        if not isinstance(unresolved, list) or not unresolved:
            errors.append("STRUCTURAL_ONLY packet must state unresolved empirical work explicitly")
        return {"valid": not errors, "errors": errors, "claim_ceiling": "STRUCTURAL_ONLY"}

    if requested == "REJECTED":
        return {"valid": not errors, "errors": errors, "claim_ceiling": "REJECTED"}

    # Any empirical status needs evidence that cannot be manufactured by a flag
    # alone: a validated immutable bundle, nonzero real runs and matched units.
    if record.get("empirical_runs_executed") is not True:
        errors.append("empirical claim requires real empirical runs")
    if record.get("validated_bundle") is not True:
        errors.append("empirical claim requires validated_bundle=true after run-bundle validation")
    digests = record.get("imported_empirical_bundle_digests")
    if not isinstance(digests, list) or not digests or any(not _sha(x) for x in digests):
        errors.append("empirical claim requires one or more validated 64-hex bundle digests")
    if not isinstance(record.get("real_run_count"), int) or record.get("real_run_count", 0) <= 0:
        errors.append("empirical claim requires positive real_run_count")
    if not isinstance(record.get("matched_pair_count"), int) or record.get("matched_pair_count", 0) <= 0:
        errors.append("empirical claim requires positive matched_pair_count")
    if record.get("ablation_identified") is not True:
        errors.append("empirical claim requires targeted ablation identification")
    if record.get("judge_blind") is not True:
        errors.append("empirical qualitative claim requires treatment-blind judging")

    blockers = record.get("hard_blocker_regressions", [])
    if blockers:
        errors.append(f"hard blocker regressions reject empirical promotion: {blockers}")
        return {"valid": False, "errors": errors, "claim_ceiling": "REJECTED"}

    if requested == "EMPIRICAL_TRANSFER":
        if record.get("holdout_evidence") is not True:
            errors.append("EMPIRICAL_TRANSFER requires genuine holdout evidence")
        families = record.get("model_families")
        if not isinstance(families, list) or len({str(x) for x in families if str(x).strip()}) < 2:
            errors.append("EMPIRICAL_TRANSFER requires at least two materially distinct model families")
        directions = record.get("per_family_positive_direction")
        if not isinstance(directions, dict) or len(directions) < 2 or any(v is not True for v in directions.values()):
            errors.append("EMPIRICAL_TRANSFER requires positive direction in every declared model family")

    effective = requested if not errors else "REJECTED"
    return {"valid": not errors, "errors": errors, "claim_ceiling": effective}


__all__ = ["validate_v10_completion_evidence"]
