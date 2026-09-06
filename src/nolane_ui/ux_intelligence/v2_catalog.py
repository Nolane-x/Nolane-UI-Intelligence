"""Composed integrity status for UX Intelligence v2."""
from __future__ import annotations

from typing import Any

from .canonical_bridge import UX_CANONICAL_SKILL_BRIDGE, validate_ux_canonical_skill_bridge
from .evaluators import UX_JOURNEY_EVALUATORS, validate_ux_journey_evaluators
from .provenance import UX_PROVENANCE, validate_ux_provenance
from .rules import UX_RULES
from .skills import UX_SKILLS


VERSION = 2


def ux_v2_status() -> dict[str, Any]:
    skill_ids = {item["skill_id"] for item in UX_SKILLS}
    rule_ids = {item["rule_id"] for item in UX_RULES}
    unresolved_bridge_skills = sorted(
        item["skill_id"] for item in UX_CANONICAL_SKILL_BRIDGE if item["skill_id"] not in skill_ids
    )
    unresolved_evaluator_rules = sorted(
        item["rule_id"] for item in UX_JOURNEY_EVALUATORS if item["rule_id"] not in rule_ids
    )
    bridge_result = validate_ux_canonical_skill_bridge(UX_CANONICAL_SKILL_BRIDGE)
    provenance_result = validate_ux_provenance(UX_PROVENANCE)
    evaluator_result = validate_ux_journey_evaluators(UX_JOURNEY_EVALUATORS)
    valid = bool(
        bridge_result["valid"]
        and provenance_result["valid"]
        and evaluator_result["valid"]
        and not unresolved_bridge_skills
        and not unresolved_evaluator_rules
    )
    return {
        "valid": valid,
        "version": VERSION,
        "canonical_skill_bridge_count": len(UX_CANONICAL_SKILL_BRIDGE),
        "provenance_count": len(UX_PROVENANCE),
        "evaluator_count": len(UX_JOURNEY_EVALUATORS),
        "bridge_valid": bool(bridge_result["valid"]),
        "provenance_valid": bool(provenance_result["valid"]),
        "evaluator_valid": bool(evaluator_result["valid"]),
        "unresolved_bridge_skills": unresolved_bridge_skills,
        "unresolved_evaluator_rules": unresolved_evaluator_rules,
        "uses_rule_count_quota": False,
        "uses_skill_count_quota": False,
        "fuzzy_similarity_is_blocking": False,
        "v13_authority_inherited": False,
    }


__all__ = ["ux_v2_status"]
