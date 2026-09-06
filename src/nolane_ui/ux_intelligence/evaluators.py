"""Deterministic UX rule evaluators for structured journey evidence.

Evaluators are deliberately narrow. They activate only when a rule-specific
condition is materially present, distinguish absent evidence from a proven
failure, and never perform fuzzy text matching.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Callable, Iterable

from .provenance import UX_PROVENANCE
from .rules import UX_RULES


Evaluator = Callable[[dict[str, Any], dict[str, Any]], tuple[bool, str, str]]


def _hidden_dependency(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["dependency_required"]
        and observation["commit_available"]
        and not observation["dependency_visible"]
    )
    return (
        not failed,
        "required dependency is visible before commit",
        "commit exposed while a required dependency remained hidden",
    )


def _premature_commitment(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["commit_available"]
        and not observation["required_decisions_complete"]
    )
    return (
        not failed,
        "commit is unavailable until required decisions are complete",
        "commit became available before required decisions were complete",
    )


def _same_goal_context(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["same_goal_navigation"]
        and not observation["context_preserved"]
    )
    return (
        not failed,
        "same-goal navigation preserves task context",
        "same-goal navigation lost task context",
    )


def _cross_step_consistency(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = observation["shared_state_consistent"] is False
    return (
        not failed,
        "shared workflow state remains coherent across steps",
        "shared workflow state contradicted an earlier actionable state",
    )


def _interruption_context(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["interrupted"]
        and not observation["resumable_context_preserved"]
    )
    return (
        not failed,
        "predictable interruption preserves resumable context",
        "predictable interruption lost context required for safe resumption",
    )


def _stale_context(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["context_may_be_stale"]
        and not observation["context_revalidated"]
    )
    return (
        not failed,
        "stale-capable context is revalidated before consequential continuation",
        "stale-capable context remained actionable without revalidation",
    )


def _false_completion(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["completion_claimed"]
        and not observation["completion_confirmed"]
    )
    return (
        not failed,
        "success language follows authoritative completion",
        "completion was claimed before authoritative completion was confirmed",
    )


def _dead_end(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["recoverable_failure"]
        and not observation["recovery_path_exists"]
    )
    return (
        not failed,
        "recoverable failure exposes a viable next path",
        "recoverable failure exposed no retry, revise, return, or continuation path",
    )


def _recovery_reachable(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["recoverable_failure"]
        and observation["recovery_path_exists"]
        and not observation["recovery_path_reachable"]
    )
    return (
        not failed,
        "the affected user can reach the declared recovery path",
        "a recovery path existed but was unreachable from the affected failure state",
    )


def _progress_destroyed(step: dict[str, Any], observation: dict[str, Any]) -> tuple[bool, str, str]:
    failed = bool(
        observation["progress_was_valuable"]
        and observation["progress_destroyed"]
        and not (
            observation["discard_authorized"]
            and observation["discard_explained"]
        )
    )
    return (
        not failed,
        "valuable progress is preserved or explicitly authorized and explained before discard",
        "valuable progress was destroyed without both discard authority and visible explanation",
    )


def _is_activated(evaluator_id: str, observation: dict[str, Any]) -> bool:
    """Return whether the rule-specific condition is materially applicable.

    Presence of a boolean field is not enough. A false signal such as
    ``completion_claimed=False`` means the false-completion rule is not active
    and therefore must not manufacture an evidence requirement.
    """
    if evaluator_id == "cross-step-consistency":
        return "shared_state_consistent" in observation
    if evaluator_id == "dead-end-recovery":
        return observation.get("recoverable_failure") is True
    if evaluator_id == "false-completion":
        return observation.get("completion_claimed") is True
    if evaluator_id == "hidden-dependency":
        return observation.get("dependency_required") is True
    if evaluator_id == "interruption-context":
        return observation.get("interrupted") is True
    if evaluator_id == "premature-commitment":
        return observation.get("required_decisions_complete") is False
    if evaluator_id == "progress-destruction":
        return observation.get("progress_destroyed") is True
    if evaluator_id == "recovery-reachability":
        return (
            observation.get("recoverable_failure") is True
            and observation.get("recovery_path_exists") is True
        )
    if evaluator_id == "same-goal-context":
        return observation.get("same_goal_navigation") is True
    if evaluator_id == "stale-context":
        return observation.get("context_may_be_stale") is True
    raise ValueError(f"unknown UX evaluator activation contract: {evaluator_id}")


_EVALUATOR_FUNCTIONS: dict[str, Evaluator] = {
    "cross-step-consistency": _cross_step_consistency,
    "dead-end-recovery": _dead_end,
    "false-completion": _false_completion,
    "hidden-dependency": _hidden_dependency,
    "interruption-context": _interruption_context,
    "premature-commitment": _premature_commitment,
    "progress-destruction": _progress_destroyed,
    "recovery-reachability": _recovery_reachable,
    "same-goal-context": _same_goal_context,
    "stale-context": _stale_context,
}


UX_JOURNEY_EVALUATORS = tuple(sorted((
    {
        "evaluator_id": "cross-step-consistency",
        "rule_id": "ux.flow.no-cross-step-contradiction",
        "activation_evidence": ("shared_state_consistent",),
        "required_evidence": ("shared_state_consistent",),
        "verification_mode": "runtime-observation",
        "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "dead-end-recovery",
        "rule_id": "ux.recovery.dead-end-has-recovery-path",
        "activation_evidence": ("recoverable_failure",),
        "required_evidence": ("recoverable_failure", "recovery_path_exists"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "false-completion",
        "rule_id": "ux.comprehension.no-false-completion",
        "activation_evidence": ("completion_claimed",),
        "required_evidence": ("completion_claimed", "completion_confirmed"),
        "verification_mode": "runtime-observation",
        "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "hidden-dependency",
        "rule_id": "ux.task.hidden-dependency-before-commit",
        "activation_evidence": ("dependency_required",),
        "required_evidence": ("dependency_required", "dependency_visible", "commit_available"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.product-journey-contract", "uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "interruption-context",
        "rule_id": "ux.flow.interruption-preserves-resumable-context",
        "activation_evidence": ("interrupted",),
        "required_evidence": ("interrupted", "resumable_context_preserved"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.product-journey-contract", "uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "premature-commitment",
        "rule_id": "ux.task.no-premature-commitment",
        "activation_evidence": ("required_decisions_complete",),
        "required_evidence": ("required_decisions_complete", "commit_available"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.product-journey-contract", "uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "progress-destruction",
        "rule_id": "ux.recovery.progress-not-silently-destroyed",
        "activation_evidence": ("progress_destroyed",),
        "required_evidence": ("progress_was_valuable", "progress_destroyed", "discard_authorized", "discard_explained"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "recovery-reachability",
        "rule_id": "ux.recovery.recovery-path-is-reachable",
        "activation_evidence": ("recovery_path_reachable",),
        "required_evidence": ("recoverable_failure", "recovery_path_exists", "recovery_path_reachable"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "same-goal-context",
        "rule_id": "ux.task.same-goal-navigation-preserves-context",
        "activation_evidence": ("same_goal_navigation",),
        "required_evidence": ("same_goal_navigation", "context_preserved"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.product-journey-contract", "uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
    {
        "evaluator_id": "stale-context",
        "rule_id": "ux.flow.stale-task-context-revalidated",
        "activation_evidence": ("context_may_be_stale",),
        "required_evidence": ("context_may_be_stale", "context_revalidated"),
        "verification_mode": "interaction",
        "provenance_ids": ("uxp.product-journey-contract", "uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
    },
), key=lambda item: item["evaluator_id"]))


def validate_ux_journey_evaluators(
    records: Iterable[dict[str, Any]],
    *,
    rule_catalog: Iterable[dict[str, Any]] = UX_RULES,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    records = list(records)
    rules = {item["rule_id"]: item for item in rule_catalog}
    provenance_ids = {item["provenance_id"] for item in provenance_catalog}
    seen_evaluators: set[str] = set()
    seen_rules: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise TypeError(f"UX evaluator record {index} must be an object")
        evaluator_id = record.get("evaluator_id")
        rule_id = record.get("rule_id")
        if not isinstance(evaluator_id, str) or evaluator_id not in _EVALUATOR_FUNCTIONS:
            raise ValueError(f"UX evaluator record {index}: unknown evaluator_id {evaluator_id!r}")
        if evaluator_id in seen_evaluators:
            raise ValueError(f"UX evaluators: duplicate evaluator_id {evaluator_id}")
        seen_evaluators.add(evaluator_id)
        if not isinstance(rule_id, str) or rule_id not in rules:
            raise ValueError(f"{evaluator_id}: unknown UX rule {rule_id!r}")
        if rule_id in seen_rules:
            raise ValueError(f"UX evaluators: duplicate rule evaluator for {rule_id}")
        seen_rules.add(rule_id)
        rule = rules[rule_id]
        if rule.get("class") in {"contextual", "convergence"} and rule.get("enforcement") == "block":
            raise ValueError(f"{evaluator_id}: contextual/convergence rules cannot gain blocking authority")
        for field in ("activation_evidence", "required_evidence", "provenance_ids"):
            value = record.get(field)
            if not isinstance(value, (tuple, list)) or not value:
                raise ValueError(f"{evaluator_id}: {field} must be a non-empty sequence")
            if not all(isinstance(item, str) and item.strip() for item in value):
                raise ValueError(f"{evaluator_id}: {field} must contain non-empty strings")
        if not set(record["activation_evidence"]) <= set(record["required_evidence"]):
            raise ValueError(f"{evaluator_id}: activation evidence must be a subset of required evidence")
        unknown_provenance = set(record["provenance_ids"]) - provenance_ids
        if unknown_provenance:
            raise ValueError(f"{evaluator_id}: unknown provenance ids {sorted(unknown_provenance)}")
        mode = record.get("verification_mode")
        if not isinstance(mode, str) or not mode.strip():
            raise ValueError(f"{evaluator_id}: verification_mode must be non-empty")
    identifiers = [record["evaluator_id"] for record in records]
    if identifiers != sorted(identifiers):
        raise ValueError("UX evaluators must be canonically sorted by evaluator_id")
    return {"valid": True, "record_count": len(records), "errors": []}


validate_ux_journey_evaluators(UX_JOURNEY_EVALUATORS)


def evaluate_ux_journey_rule(
    evaluator: dict[str, Any],
    step: dict[str, Any],
    observation: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate one explicit rule without interpreting non-applicability as missing evidence."""
    if not isinstance(observation, dict):
        raise TypeError("UX step observation must be an object")
    if not _is_activated(evaluator["evaluator_id"], observation):
        return {"status": "not-executed", "missing_evidence": (), "expected": None, "observed": None}
    missing = tuple(key for key in evaluator["required_evidence"] if key not in observation)
    if missing:
        return {
            "status": "insufficient-evidence",
            "missing_evidence": missing,
            "expected": None,
            "observed": "rule activation observed but required evidence is incomplete",
        }
    passed, expected, failed_observation = _EVALUATOR_FUNCTIONS[evaluator["evaluator_id"]](step, observation)
    return {
        "status": "pass" if passed else "fail",
        "missing_evidence": (),
        "expected": expected,
        "observed": expected if passed else failed_observation,
    }


def get_ux_journey_evaluators() -> list[dict[str, Any]]:
    return deepcopy(list(UX_JOURNEY_EVALUATORS))


__all__ = [
    "UX_JOURNEY_EVALUATORS",
    "evaluate_ux_journey_rule",
    "get_ux_journey_evaluators",
    "validate_ux_journey_evaluators",
]
