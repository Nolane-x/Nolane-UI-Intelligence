"""Versioned selection metadata for UX Intelligence v3."""
from __future__ import annotations


VERSION = 3

UX_DISCOVERY_SCORE_WEIGHTS = {
    "goal_confidence": 0.25,
    "success_evidence_strength": 0.20,
    "path_evidence_coverage": 0.20,
    "critical_action_presence": 0.15,
    "recovery_relevance": 0.10,
    "novelty_against_verified_journeys": 0.10,
}

UX_IMPACT_SCORE_WEIGHTS = {
    "goal_criticality": 0.22,
    "task_frequency": 0.12,
    "completion_blockage": 0.22,
    "recoverability_cost": 0.14,
    "affected_scope": 0.12,
    "regression_confidence": 0.10,
    "evidence_completeness": 0.08,
}

UX_REQUIRED_IMPACT_COMPONENTS = frozenset({
    "goal_criticality",
    "completion_blockage",
    "regression_confidence",
    "evidence_completeness",
})

UX_PRIORITY_BANDS = ((0.85, "p0"), (0.70, "p1"), (0.50, "p2"), (0.0, "p3"))

CANDIDATE_STATUSES = {"hypothesis", "promotable", "promoted", "rejected"}


UX_RULE_REGRESSION_CLASSES = {
    "ux.recovery.dead-end-has-recovery-path": "recovery-path-lost",
    "ux.recovery.recovery-path-is-reachable": "recovery-path-lost",
    "ux.task.same-goal-navigation-preserves-context": "preserved-context-regressed",
    "ux.task.no-premature-commitment": "new-premature-commitment",
    "ux.task.hidden-dependency-before-commit": "new-hidden-dependency",
    "ux.comprehension.no-false-completion": "new-false-completion",
}


def validate_discovery_score_weights(weights=UX_DISCOVERY_SCORE_WEIGHTS):
    required = {
        "goal_confidence",
        "success_evidence_strength",
        "path_evidence_coverage",
        "critical_action_presence",
        "recovery_relevance",
        "novelty_against_verified_journeys",
    }
    if set(weights) != required:
        raise ValueError("UX v3 discovery score weights must expose the complete closed component set")
    for key, value in weights.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{key} weight must be numeric")
        if not 0.0 <= float(value) <= 1.0:
            raise ValueError(f"{key} weight must be within [0, 1]")
    if abs(sum(float(value) for value in weights.values()) - 1.0) > 1e-12:
        raise ValueError("UX v3 discovery score weights must sum to 1.0")
    return {"valid": True, "version": VERSION, "component_count": len(weights), "errors": []}


validate_discovery_score_weights()


__all__ = [
    "CANDIDATE_STATUSES",
    "UX_DISCOVERY_SCORE_WEIGHTS",
    "UX_IMPACT_SCORE_WEIGHTS",
    "UX_PRIORITY_BANDS",
    "UX_REQUIRED_IMPACT_COMPONENTS",
    "UX_RULE_REGRESSION_CLASSES",
    "VERSION",
    "validate_discovery_score_weights",
]
