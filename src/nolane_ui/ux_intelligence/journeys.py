"""Structured user-journey contracts for UX Intelligence v2.

Journey validation is intentionally independent of browser execution.  It
validates what the product claims should happen; runtime evidence is bound later
by :mod:`verifier`.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable

from .provenance import UX_PROVENANCE


JOURNEY_STATUSES = {"active", "deprecated", "experimental"}
_REQUIRED_JOURNEY_FIELDS = (
    "journey_id",
    "title",
    "user_goal",
    "entry_state",
    "steps",
    "success_criteria",
    "critical_state",
    "provenance_ids",
    "status",
)
_REQUIRED_STEP_FIELDS = (
    "step_id",
    "intent",
    "action",
    "expected_transition",
    "required_context",
    "preserved_context",
    "allowed_detours",
    "recovery_expectation",
    "evidence_requirements",
)


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value


def _require_string_sequence(value: Any, label: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(value, (tuple, list)):
        raise TypeError(f"{label} must be a sequence")
    if not allow_empty and not value:
        raise ValueError(f"{label} must not be empty")
    if not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{label} must contain only non-empty strings")
    return tuple(value)


def _validate_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{label} must be an object")
    return value


def validate_ux_journey_spec(
    journey: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    if not isinstance(journey, dict):
        raise TypeError("UX journey must be an object")
    missing_fields = [field for field in _REQUIRED_JOURNEY_FIELDS if field not in journey]
    if missing_fields:
        raise ValueError(f"UX journey missing required fields: {missing_fields}")

    journey_id = _require_string(journey.get("journey_id"), "journey_id")
    _require_string(journey.get("title"), f"{journey_id}.title")
    _require_string(journey.get("user_goal"), f"{journey_id}.user_goal")
    _validate_mapping(journey.get("entry_state"), f"{journey_id}.entry_state")
    if journey.get("status") not in JOURNEY_STATUSES:
        raise ValueError(f"{journey_id}: unknown status {journey.get('status')!r}")

    success_criteria = _require_string_sequence(
        journey.get("success_criteria"), f"{journey_id}.success_criteria"
    )
    critical_state = _require_string_sequence(
        journey.get("critical_state"), f"{journey_id}.critical_state"
    )
    provenance_ids = _require_string_sequence(
        journey.get("provenance_ids"), f"{journey_id}.provenance_ids"
    )
    known_provenance = {record["provenance_id"] for record in provenance_catalog}
    unknown_provenance = set(provenance_ids) - known_provenance
    if unknown_provenance:
        raise ValueError(f"{journey_id}: unknown provenance ids {sorted(unknown_provenance)}")

    steps = journey.get("steps")
    if not isinstance(steps, (tuple, list)):
        raise TypeError(f"{journey_id}.steps must be a sequence")
    if not steps:
        raise ValueError(f"{journey_id}.steps must not be empty")

    step_ids: set[str] = set()
    for index, step in enumerate(steps):
        if not isinstance(step, dict):
            raise TypeError(f"{journey_id}.steps[{index}] must be an object")
        missing_step_fields = [field for field in _REQUIRED_STEP_FIELDS if field not in step]
        if missing_step_fields:
            raise ValueError(
                f"{journey_id}.steps[{index}] missing required fields: {missing_step_fields}"
            )
        step_id = _require_string(step.get("step_id"), f"{journey_id}.steps[{index}].step_id")
        if step_id in step_ids:
            raise ValueError(f"{journey_id}: duplicate step_id {step_id}")
        step_ids.add(step_id)
        _require_string(step.get("intent"), f"{journey_id}.{step_id}.intent")
        _require_string(step.get("action"), f"{journey_id}.{step_id}.action")
        expected = _validate_mapping(
            step.get("expected_transition"), f"{journey_id}.{step_id}.expected_transition"
        )
        if not expected:
            raise ValueError(f"{journey_id}.{step_id}.expected_transition must not be empty")
        _require_string_sequence(
            step.get("required_context"), f"{journey_id}.{step_id}.required_context", allow_empty=True
        )
        _require_string_sequence(
            step.get("preserved_context"), f"{journey_id}.{step_id}.preserved_context", allow_empty=True
        )
        _require_string_sequence(
            step.get("allowed_detours"), f"{journey_id}.{step_id}.allowed_detours", allow_empty=True
        )
        _require_string(step.get("recovery_expectation"), f"{journey_id}.{step_id}.recovery_expectation")
        _require_string_sequence(
            step.get("evidence_requirements"), f"{journey_id}.{step_id}.evidence_requirements"
        )

    return {
        "valid": True,
        "journey_id": journey_id,
        "step_count": len(steps),
        "success_criterion_count": len(success_criteria),
        "critical_state_count": len(critical_state),
        "errors": [],
    }


def normalize_ux_journey_spec(
    journey: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    """Validate and defensively normalize sequence fields without inventing semantics."""
    validate_ux_journey_spec(journey, provenance_catalog=provenance_catalog)
    normalized = deepcopy(journey)
    normalized["success_criteria"] = tuple(normalized["success_criteria"])
    normalized["critical_state"] = tuple(normalized["critical_state"])
    normalized["provenance_ids"] = tuple(normalized["provenance_ids"])
    normalized_steps: list[dict[str, Any]] = []
    for step in normalized["steps"]:
        item = deepcopy(step)
        for field in (
            "required_context",
            "preserved_context",
            "allowed_detours",
            "evidence_requirements",
        ):
            item[field] = tuple(item[field])
        normalized_steps.append(item)
    normalized["steps"] = tuple(normalized_steps)
    return normalized


__all__ = [
    "JOURNEY_STATUSES",
    "normalize_ux_journey_spec",
    "validate_ux_journey_spec",
]
