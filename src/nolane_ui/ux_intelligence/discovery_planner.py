"""Bounded observation planning for UX Intelligence v3.

The planner emits evidence requests only. It never claims execution, observation,
or user-goal truth, and it does not own browser/runtime authority.
"""
from __future__ import annotations

import hashlib
from typing import Any, Iterable


def _validate_limit(limit: Any) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    return limit


def _string_tuple(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, (tuple, list)):
        raise TypeError(f"{label} must be a sequence")
    out = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{label}[{index}] must be a non-empty string")
        out.append(item.strip())
    return tuple(out)


def _available_capabilities(values: Iterable[str]) -> frozenset[str]:
    if isinstance(values, (str, bytes)):
        raise TypeError("available_capabilities must be an iterable of strings")
    out: set[str] = set()
    for index, item in enumerate(tuple(values)):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"available_capabilities[{index}] must be a non-empty string")
        out.add(item.strip())
    return frozenset(out)


def _request_id(candidate_id: str, step_id: str, fields: tuple[str, ...]) -> str:
    raw = "|".join((candidate_id, step_id, *fields)).encode("utf-8")
    return "uxr:" + hashlib.sha256(raw).hexdigest()[:24]


def _request(
    *,
    candidate_id: str,
    step_id: str,
    kind: str,
    fields: tuple[str, ...],
    requested_capabilities: tuple[str, ...],
    available_capabilities: frozenset[str],
    reason: str,
) -> dict[str, Any]:
    normalized_fields = tuple(sorted(set(fields)))
    return {
        "request_id": _request_id(candidate_id, step_id, normalized_fields),
        "candidate_id": candidate_id,
        "step_id": step_id,
        "request_kind": kind,
        "required_evidence_fields": normalized_fields,
        "preferred_v11_capabilities": tuple(sorted(set(requested_capabilities) & available_capabilities)),
        "reason": reason,
        "claim_boundary": "evidence-request-only",
    }


def plan_ux_discovery(
    subject: dict[str, Any],
    available_capabilities: Iterable[str],
    *,
    limit: int = 25,
) -> tuple[dict[str, Any], ...]:
    """Return deterministic observation requests without claiming they ran."""
    bounded_limit = _validate_limit(limit)
    if not isinstance(subject, dict):
        raise TypeError("subject must be an object")
    candidate_id = subject.get("candidate_id")
    if not isinstance(candidate_id, str) or not candidate_id.strip():
        raise ValueError("subject.candidate_id must be a non-empty string")
    available = _available_capabilities(available_capabilities)

    steps = subject.get("step_hypotheses")
    if not isinstance(steps, (tuple, list)):
        raise TypeError("subject.step_hypotheses must be a sequence")

    requests: list[dict[str, Any]] = []
    for index, step in enumerate(steps):
        if not isinstance(step, dict):
            raise TypeError(f"subject.step_hypotheses[{index}] must be an object")
        step_id = step.get("candidate_step_id")
        if not isinstance(step_id, str) or not step_id.strip():
            raise ValueError(f"subject.step_hypotheses[{index}].candidate_step_id must be non-empty")
        required_context = _string_tuple(step.get("required_context_hypotheses", ()), f"{step_id}.required_context_hypotheses")
        preserved_context = _string_tuple(step.get("preserved_context_hypotheses", ()), f"{step_id}.preserved_context_hypotheses")

        transition_fields = tuple(sorted(set(("route",) + required_context + preserved_context)))
        requests.append(_request(
            candidate_id=candidate_id,
            step_id=step_id,
            kind="transition-and-context",
            fields=transition_fields,
            requested_capabilities=("browser-runtime", "interaction"),
            available_capabilities=available,
            reason="Verify target transition and product-local context fields for this candidate step.",
        ))

        requests.append(_request(
            candidate_id=candidate_id,
            step_id=step_id,
            kind="recovery",
            fields=("recoverable_failure", "recovery_path_exists", "recovery_path_reachable"),
            requested_capabilities=("browser-runtime", "interaction"),
            available_capabilities=available,
            reason="Collect recovery evidence without assuming a failure or a recovery path exists.",
        ))

    success_hypotheses = subject.get("success_hypotheses", ())
    if not isinstance(success_hypotheses, (tuple, list)):
        raise TypeError("subject.success_hypotheses must be a sequence")
    for index, item in enumerate(success_hypotheses):
        if not isinstance(item, dict):
            raise TypeError(f"subject.success_hypotheses[{index}] must be an object")
        outcome_id = item.get("outcome_id")
        if not isinstance(outcome_id, str) or not outcome_id.strip():
            raise ValueError(f"subject.success_hypotheses[{index}].outcome_id must be non-empty")
        requests.append(_request(
            candidate_id=candidate_id,
            step_id="journey-outcome",
            kind="outcome",
            fields=(outcome_id.strip(),),
            requested_capabilities=("browser-runtime", "interaction"),
            available_capabilities=available,
            reason="Collect evidence for the candidate outcome without asserting completion.",
        ))

    deduplicated = {item["request_id"]: item for item in requests}
    ordered = tuple(deduplicated[key] for key in sorted(deduplicated))
    return ordered[:bounded_limit]


__all__ = ["plan_ux_discovery"]
