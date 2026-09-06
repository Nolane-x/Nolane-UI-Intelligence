from __future__ import annotations

from copy import deepcopy
import unittest
from unittest.mock import patch

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
from nolane_ui.ux_intelligence import catalog as ux_catalog


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
    "ux.convergence.product-architecture-not-generic-template",
    "ux.flow.interruption-preserves-resumable-context",
    "ux.flow.no-cross-step-contradiction",
    "ux.flow.stale-task-context-revalidated",
    "ux.friction.no-semantically-redundant-reentry",
    "ux.ia.navigation-preserves-object-identity",
    "ux.mental-model.product-terms-match-user-concepts",
    "ux.recovery.dead-end-has-recovery-path",
    "ux.recovery.progress-not-silently-destroyed",
    "ux.recovery.recovery-path-is-reachable",
    "ux.task.hidden-dependency-before-commit",
    "ux.task.no-premature-commitment",
    "ux.task.same-goal-navigation-preserves-context",
}


def _ids(records, key):
    return [record[key] for record in records]


class UXIntelligenceV1Tests(unittest.TestCase):
    def test_first_wave_inventory_is_explicit_and_sorted(self):
        self.assertEqual(set(_ids(UX_MECHANISMS, "mechanism_id")), EXPECTED_MECHANISMS)
        self.assertEqual(set(_ids(UX_SKILLS, "skill_id")), EXPECTED_SKILLS)
        self.assertEqual(set(_ids(UX_RULES, "rule_id")), EXPECTED_RULES)
        self.assertEqual(_ids(UX_MECHANISMS, "mechanism_id"), sorted(EXPECTED_MECHANISMS))
        self.assertEqual(_ids(UX_SKILLS, "skill_id"), sorted(EXPECTED_SKILLS))
        self.assertEqual(_ids(UX_RULES, "rule_id"), sorted(EXPECTED_RULES))

    def test_ids_are_unique_and_references_resolve(self):
        mechanism_ids = set(_ids(UX_MECHANISMS, "mechanism_id"))
        skill_ids = set(_ids(UX_SKILLS, "skill_id"))
        skill_index = {skill["skill_id"]: skill for skill in UX_SKILLS}
        self.assertEqual(len(mechanism_ids), len(UX_MECHANISMS))
        self.assertEqual(len(skill_ids), len(UX_SKILLS))
        self.assertEqual(len(set(_ids(UX_RULES, "rule_id"))), len(UX_RULES))

        for skill in UX_SKILLS:
            self.assertTrue(skill["related_mechanisms"])
            self.assertLessEqual(set(skill["related_mechanisms"]), mechanism_ids)
        for rule in UX_RULES:
            self.assertIn(rule["mechanism_id"], mechanism_ids)
            self.assertTrue(rule["owner_skill_ids"])
            self.assertLessEqual(set(rule["owner_skill_ids"]), skill_ids)
            self.assertTrue(
                any(
                    rule["mechanism_id"] in skill_index[skill_id]["related_mechanisms"]
                    for skill_id in rule["owner_skill_ids"]
                ),
                msg=f"{rule['rule_id']} has no owner skill covering {rule['mechanism_id']}",
            )

    def test_rule_owner_skill_must_semantically_cover_mechanism(self):
        rules = deepcopy(UX_RULES)
        target = deepcopy(rules[0])
        unrelated_skill = next(
            skill["skill_id"]
            for skill in UX_SKILLS
            if target["mechanism_id"] not in skill["related_mechanisms"]
        )
        target["owner_skill_ids"] = (unrelated_skill,)
        mutated = tuple(
            sorted(
                (target if rule["rule_id"] == target["rule_id"] else deepcopy(rule) for rule in rules),
                key=lambda rule: rule["rule_id"],
            )
        )
        mechanism_ids = set(_ids(UX_MECHANISMS, "mechanism_id"))
        skill_ids = set(_ids(UX_SKILLS, "skill_id"))
        with patch.object(ux_catalog, "UX_RULES", mutated):
            with self.assertRaisesRegex(ValueError, "mechanism-compatible owner skill"):
                ux_catalog._validate_rules(mechanism_ids, skill_ids)

    def test_duplicate_operational_signature_is_rejected(self):
        duplicate = deepcopy(UX_RULES[0])
        duplicate["rule_id"] = "ux.zzz.synthetic-duplicate-signature"
        mutated = tuple(sorted((*deepcopy(UX_RULES), duplicate), key=lambda rule: rule["rule_id"]))
        mechanism_ids = set(_ids(UX_MECHANISMS, "mechanism_id"))
        skill_ids = set(_ids(UX_SKILLS, "skill_id"))
        with patch.object(ux_catalog, "UX_RULES", mutated):
            with self.assertRaisesRegex(ValueError, "duplicate operational signature"):
                ux_catalog._validate_rules(mechanism_ids, skill_ids)

    def test_rules_have_operational_planes_and_no_quota_fields(self):
        required = {
            "applies_when",
            "failure_modes",
            "user_impacts",
            "observables",
            "falsifiers",
            "repairs",
            "verification",
        }
        forbidden = {
            "minimum_rule_count",
            "target_rule_count",
            "rule_quota",
            "minimum_skill_count",
            "target_skill_count",
        }
        for rule in UX_RULES:
            self.assertFalse(set(rule) & forbidden)
            for field in required:
                self.assertIsInstance(rule[field], tuple)
                self.assertTrue(rule[field])
                self.assertTrue(
                    all(isinstance(item, str) and len(item.strip()) >= 24 for item in rule[field]),
                    msg=f"{rule['rule_id']} has weak {field}",
                )

    def test_contextual_and_convergence_rules_never_block(self):
        for rule in UX_RULES:
            if rule["class"] in {"contextual", "convergence"}:
                self.assertIn(rule["enforcement"], {"warn", "review"})

    def test_exact_lookup_returns_copy_and_missing_returns_none(self):
        mechanism = get_ux_mechanism("context-loss")
        self.assertIsNotNone(mechanism)
        self.assertEqual(mechanism["mechanism_id"], "context-loss")
        mechanism["title"] = "mutated"
        self.assertNotEqual(get_ux_mechanism("context-loss")["title"], "mutated")

        skill = get_ux_skill("identifying-user-goals")
        self.assertIsNotNone(skill)
        self.assertEqual(skill["skill_id"], "identifying-user-goals")
        rule = get_ux_rule("ux.recovery.progress-not-silently-destroyed")
        self.assertIsNotNone(rule)
        self.assertEqual(rule["mechanism_id"], "unrecoverable-progress-loss")
        self.assertIsNone(get_ux_rule("ux.missing.rule"))

    def test_queries_are_deterministic_filterable_and_bounded(self):
        first = query_ux_skills(domain="recovery", limit=100)
        second = query_ux_skills(domain="recovery", limit=100)
        self.assertEqual(first, second)
        self.assertTrue(all(item["domain"] == "recovery" for item in first))

        context_rules = query_ux_rules(mechanism_id="context-loss", limit=100)
        self.assertTrue(context_rules)
        self.assertTrue(all(item["mechanism_id"] == "context-loss" for item in context_rules))

        found = query_ux_mechanisms(text="navigation", limit=100)
        self.assertTrue(any(item["mechanism_id"] == "navigation-disorientation" for item in found))

        for query in (query_ux_mechanisms, query_ux_skills, query_ux_rules):
            with self.assertRaises(ValueError):
                query(limit=0)
            with self.assertRaises(ValueError):
                query(limit=101)
            with self.assertRaises(TypeError):
                query(limit=True)

    def test_status_exposes_coverage_without_quality_quota(self):
        status = ux_intelligence_status()
        self.assertIs(status["valid"], True)
        self.assertEqual(status["version"], 1)
        self.assertEqual(status["mechanism_count"], 14)
        self.assertEqual(status["skill_count"], 32)
        self.assertEqual(status["rule_count"], 16)
        self.assertIs(status["rule_count_is_quality_target"], False)
        self.assertIs(status["skill_count_is_quality_target"], False)
        self.assertEqual(status["orphan_mechanisms"], [])
        self.assertEqual(status["domain_counts"]["evaluation"], 4)
        self.assertEqual(status["domain_counts"]["recovery"], 4)


if __name__ == "__main__":
    unittest.main()
