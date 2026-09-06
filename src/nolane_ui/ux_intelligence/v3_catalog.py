"""Versioned selection metadata for UX Intelligence v3."""
from __future__ import annotations

import math


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


def _validate_weight_map(weights, required, label):
    if set(weights) != set(required):
        raise ValueError(f"{label} weights must expose the complete closed component set")
    for key, value in weights.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{key} weight must be numeric")
        numeric = float(value)
        if not math.isfinite(numeric) or not 0.0 <= numeric <= 1.0:
            raise ValueError(f"{key} weight must be finite and within [0, 1]")
    total = sum(float(value) for value in weights.values())
    if abs(total - 1.0) > 1e-12:
        raise ValueError(f"{label} weights must sum to 1.0")
    return total


def validate_discovery_score_weights(weights=UX_DISCOVERY_SCORE_WEIGHTS):
    total = _validate_weight_map(weights, UX_DISCOVERY_SCORE_WEIGHTS, "UX v3 discovery score")
    return {"valid": True, "version": VERSION, "component_count": len(weights), "weight_sum": total, "errors": []}


def validate_impact_score_weights(weights=UX_IMPACT_SCORE_WEIGHTS):
    total = _validate_weight_map(weights, UX_IMPACT_SCORE_WEIGHTS, "UX v3 impact score")
    return {"valid": True, "version": VERSION, "component_count": len(weights), "weight_sum": total, "errors": []}


def ux_v3_status():
    discovery = validate_discovery_score_weights()
    impact = validate_impact_score_weights()
    thresholds = tuple(threshold for threshold, _ in UX_PRIORITY_BANDS)
    bands_valid = bool(UX_PRIORITY_BANDS) and thresholds[-1] == 0.0 and all(
        left > right for left, right in zip(thresholds, thresholds[1:])
    )
    return {
        "version": VERSION,
        "catalog_valid": bool(discovery["valid"] and impact["valid"] and bands_valid),
        "product_model_valid": True,
        "goal_graph_valid": True,
        "discovery_score_weight_sum": round(discovery["weight_sum"], 12),
        "impact_score_weight_sum": round(impact["weight_sum"], 12),
        "priority_bands_valid": bands_valid,
        "discovery_can_create_blocking_findings": False,
        "owns_browser_runtime": False,
        "uses_v2_verification_authority": True,
        "uses_rule_count_quota": False,
        "uses_skill_count_quota": False,
        "uses_journey_count_quota": False,
    }


validate_discovery_score_weights()
validate_impact_score_weights()


__all__ = [
    "CANDIDATE_STATUSES",
    "UX_DISCOVERY_SCORE_WEIGHTS",
    "UX_IMPACT_SCORE_WEIGHTS",
    "UX_PRIORITY_BANDS",
    "UX_REQUIRED_IMPACT_COMPONENTS",
    "UX_RULE_REGRESSION_CLASSES",
    "VERSION",
    "ux_v3_status",
    "validate_discovery_score_weights",
    "validate_impact_score_weights",
]
