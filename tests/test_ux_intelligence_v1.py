from __future__ import annotations

import pytest

from nolane_ui.ux_intelligence import (
    UX_MECHANISMS,
    UX_RULES,
    UX_SKILLS,
    get_ux_mechanism,
    get_ux_rule,
    get_ux_skill,
    query_ux_mechanisms,
    query_ux_rules,
    query_ux_skills,
    ux_intelligence_status,
)


EXPECTED_MECHANISMS = {
    "ambiguous-consequence",
    "context-loss",
    "cross-step-inconsistency",
    "decision-overload",
    "false-completion",
    "goal-displacement",
    "hidden-dependency",
    "mental-model-mismatch",
    "navigation-disorientation",
    "premature-commitment",
    "state-without-explanation",
    "unnecessary-recall",
    "unrecoverable-progress-loss",
    "workflow-fragmentation",
}

EXPECTED_SKILLS = {
    "aligning-conceptual-models",
    "analyzing-task-frequency-criticality",
    "architecting-goal-oriented-navigation",
    "assessing-recovery-completeness",
    "auditing-decision-friction",
    "clarifying-action-consequences",
    "conducting-cognitive-walkthroughs",
    "designing-contextual-explanations",
    "designing-cross-session-continuity",
    "designing-error-recovery-paths",
    "designing-progress-preservation",
    "designing-recognition-over-recall",
    "distinguishing-goals-from-interface-actions",
    "evaluating-first-value-paths",
    "evaluating-task-success",
    "grouping-information-by-user-intent",
    "identifying-user-goals",
    "mapping-critical-user-journeys",
    "measuring-workflow-friction",
    "minimizing-context-switching",
    "modeling-expert-novice-workflows",
    "modeling-object-continuity",
    "optimizing-critical-task-paths",
    "preserving-location-awareness",
    "reducing-redundant-input",
    "structuring-complex-decisions",
    "testing-information-findability",
    "testing-mental-model-alignment",
    "tracing-cross-step-state",
    "validating-navigation-scent",
    "verifying-interruption-recovery",
    "writing-domain-aligned-language",
}

EXPECTED_RULES = {
    "ux.comprehension.destructive-consequence-before-commit",
    "ux.comprehension.hidden-scope-change-visible",
    "ux.comprehension.no-false-completion",
    "ux.friction.no-semantically-redundant-reentry",
    "ux.flow.interruption-preserves-resumable-context",
    "ux.flow.no-cross-step-contradiction",
    "ux.flow.stale-task-context-revalidated",
    "ux.ia.navigation-preserves-object-identity",
    "ux.mental-model.product-terms-match-user-concepts",
    "ux.recovery.dead-end-has-recovery-path",
    "ux.recovery.progress-not-silently-destroyed",
    "ux.recovery.recovery-path-is-reachable",
    "ux.task.hidden-dependency-before-commit",
    "ux.task.no-premature-commitment",
    "ux.task.same-goal-navigation-preserves-context",
    "ux.convergence.product-architecture-not-generic-template",
}


def _ids(records, key):
    return [record[key] for record in records]


def test_first_wave_inventory_is_explicit_and_sorted():
    assert set(_ids(UX_MECHANISMS, "mechanism_id")) == EXPECTED_MECHANISMS
    assert set(_ids(UX_SKILLS, "skill_id")) == EXPECTED_SKILLS
    assert set(_ids(UX_RULES, "rule_id")) == EXPECTED_RULES
    assert _ids(UX_MECHANISMS, "mechanism_id") == sorted(EXPECTED_MECHANISMS)
    assert _ids(UX_SKILLS, "skill_id") == sorted(EXPECTED_SKILLS)
    assert _ids(UX_RULES, "rule_id") == sorted(EXPECTED_RULES)


def test_ids_are_unique_and_references_resolve():
    mechanism_ids = set(_ids(UX_MECHANISMS, "mechanism_id"))
    skill_ids = set(_ids(UX_SKILLS, "skill_id"))
    assert len(mechanism_ids) == len(UX_MECHANISMS)
    assert len(skill_ids) == len(UX_SKILLS)
    assert len(set(_ids(UX_RULES, "rule_id"))) == len(UX_RULES)

    for skill in UX_SKILLS:
        assert skill["related_mechanisms"]
        assert set(skill["related_mechanisms"]) <= mechanism_ids
    for rule in UX_RULES:
        assert rule["mechanism_id"] in mechanism_ids
        assert rule["owner_skill_ids"]
        assert set(rule["owner_skill_ids"]) <= skill_ids


def test_rules_have_operational_planes_and_no_quota_fields():
    required = {
        "applies_when",
        "failure_modes",
        "user_impacts",
        "observables",
        "falsifiers",
        "repairs",
        "verification",
    }
    forbidden = {"minimum_rule_count", "target_rule_count", "rule_quota", "minimum_skill_count", "target_skill_count"}
    for rule in UX_RULES:
        assert not (set(rule) & forbidden)
        for field in required:
            assert isinstance(rule[field], tuple)
            assert rule[field]
            assert all(isinstance(item, str) and len(item.strip()) >= 24 for item in rule[field])


def test_contextual_and_convergence_rules_never_block():
    for rule in UX_RULES:
        if rule["class"] in {"contextual", "convergence"}:
            assert rule["enforcement"] in {"warn", "review"}


def test_exact_lookup_returns_copy_and_missing_returns_none():
    mechanism = get_ux_mechanism("context-loss")
    assert mechanism and mechanism["mechanism_id"] == "context-loss"
    mechanism["title"] = "mutated"
    assert get_ux_mechanism("context-loss")["title"] != "mutated"

    skill = get_ux_skill("identifying-user-goals")
    assert skill and skill["skill_id"] == "identifying-user-goals"
    rule = get_ux_rule("ux.recovery.progress-not-silently-destroyed")
    assert rule and rule["mechanism_id"] == "unrecoverable-progress-loss"
    assert get_ux_rule("ux.missing.rule") is None


def test_queries_are_deterministic_filterable_and_bounded():
    first = query_ux_skills(domain="recovery", limit=100)
    second = query_ux_skills(domain="recovery", limit=100)
    assert first == second
    assert all(item["domain"] == "recovery" for item in first)

    context_rules = query_ux_rules(mechanism_id="context-loss", limit=100)
    assert context_rules
    assert all(item["mechanism_id"] == "context-loss" for item in context_rules)

    found = query_ux_mechanisms(text="navigation", limit=100)
    assert any(item["mechanism_id"] == "navigation-disorientation" for item in found)

    for query in (query_ux_mechanisms, query_ux_skills, query_ux_rules):
        with pytest.raises(ValueError):
            query(limit=0)
        with pytest.raises(ValueError):
            query(limit=101)
        with pytest.raises(TypeError):
            query(limit=True)


def test_status_exposes_coverage_without_quality_quota():
    status = ux_intelligence_status()
    assert status["valid"] is True
    assert status["version"] == 1
    assert status["mechanism_count"] == 14
    assert status["skill_count"] == 32
    assert status["rule_count"] == 16
    assert status["rule_count_is_quality_target"] is False
    assert status["skill_count_is_quality_target"] is False
    assert status["orphan_mechanisms"] == []
    assert status["domain_counts"]["evaluation"] == 4
    assert status["domain_counts"]["recovery"] == 4
