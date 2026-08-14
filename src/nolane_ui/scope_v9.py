"""Independent scope-adequacy checks for NUI v9.

Functional closure can prove that a declared capability set is internally closed.
This critic challenges whether the declared set is adequate for the product class
and ambition before a broad completion claim is accepted.
"""
from __future__ import annotations

from typing import Any


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_scope_adequacy(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["scope adequacy must be an object"]}

    if record.get("status") != "PASS":
        errors.append("scope adequacy requires explicit PASS status after independent challenge")

    challenges = record.get("challenges")
    if not isinstance(challenges, list) or not challenges:
        errors.append("scope adequacy requires independent challenge/falsification cases")
        challenges = []
    for index, challenge in enumerate(challenges):
        if not isinstance(challenge, dict):
            errors.append(f"scope challenge[{index}] must be an object")
            continue
        for field in ("assumption", "attack", "evidence", "verdict"):
            if not _text(challenge.get(field)):
                errors.append(f"scope challenge[{index}] requires {field}")

    omitted_probe = record.get("omitted_capability_probe")
    if not isinstance(omitted_probe, dict):
        errors.append("scope adequacy requires omitted-capability falsification probe")
    else:
        if not isinstance(omitted_probe.get("families_tested"), list) or not omitted_probe.get("families_tested"):
            errors.append("omitted-capability probe requires families_tested")
        if not _text(omitted_probe.get("result")):
            errors.append("omitted-capability probe requires result")

    compression = record.get("compression_check")
    if not isinstance(compression, dict):
        errors.append("scope adequacy requires compression check against an artificially tiny product model")
    else:
        if compression.get("tiny_model_rejected") is not True:
            errors.append("scope adequacy must reject an artificially tiny but internally coherent product model")
        if not _text(compression.get("reason")):
            errors.append("scope compression check requires reason")

    independent = record.get("independent_from_generator")
    if independent is not True:
        errors.append("scope adequacy critic must be independent from the generator/self-certifier")

    return {
        "valid": not errors,
        "errors": errors,
        "challenge_count": len(challenges),
    }


__all__ = ["validate_scope_adequacy"]
