import copy
import unittest
from pathlib import Path

from nolane_ui.reality_rules import load_reality_rule_catalog, validate_reality_rule_catalog


ROOT = Path(__file__).resolve().parents[1]


def sample_rule():
    return {
        "rule_id": "ui.accessibility.keyboard-reachability",
        "domain": "accessibility",
        "class": "mechanical",
        "severity": "major",
        "enforcement": "block",
        "title": "Interactive functionality must be keyboard reachable",
        "statement": "Any interactive function exposed to pointer users must have an operable keyboard path unless the function intrinsically depends on free-form pointer movement.",
        "applies_when": "The interface exposes an interactive control or action that a user can operate with a pointer.",
        "failure_mode": "Keyboard-only users cannot reach or operate functionality that pointer users can use.",
        "observables": ["A pointer-operable action has no focusable or keyboard-operable equivalent."],
        "repair": ["Expose the action through a semantic focusable control or an equivalent keyboard command."],
        "exceptions": ["Free-form drawing or other input whose meaning intrinsically depends on a continuous pointer path."],
        "verification": ["Traverse and operate the affected workflow using keyboard input only."],
    }


class RealityRuleCatalogV12Tests(unittest.TestCase):
    def test_minimum_catalog_is_large_and_domain_diverse(self):
        catalog = load_reality_rule_catalog(ROOT)
        result = validate_reality_rule_catalog(catalog)
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["rule_count"], 60)
        self.assertGreaterEqual(len(result["domains"]), 10)

    def test_source_provenance_is_optional(self):
        result = validate_reality_rule_catalog({"version": 12, "rules": [sample_rule()]})
        self.assertTrue(result["valid"], result["errors"])

    def test_reality_contract_fields_are_required(self):
        for field in ("applies_when", "failure_mode", "observables", "repair", "verification"):
            with self.subTest(field=field):
                rule = sample_rule()
                rule.pop(field)
                result = validate_reality_rule_catalog({"version": 12, "rules": [rule]})
                self.assertFalse(result["valid"])
                self.assertTrue(any(field in error for error in result["errors"]), result["errors"])

    def test_empty_operational_lists_fail(self):
        for field in ("observables", "repair", "verification"):
            with self.subTest(field=field):
                rule = sample_rule()
                rule[field] = []
                result = validate_reality_rule_catalog({"version": 12, "rules": [rule]})
                self.assertFalse(result["valid"])

    def test_placeholder_strength_operational_fields_fail(self):
        replacements = {
            "title": "Looks good",
            "statement": "Make it nice",
            "applies_when": "When needed",
            "failure_mode": "Looks bad",
            "observables": ["Seems wrong"],
            "repair": ["Fix it"],
            "verification": ["Check it"],
        }
        for field, value in replacements.items():
            with self.subTest(field=field):
                rule = sample_rule()
                rule[field] = value
                result = validate_reality_rule_catalog({"version": 12, "rules": [rule]})
                self.assertFalse(result["valid"])
                self.assertTrue(any(field in error for error in result["errors"]), result["errors"])

    def test_duplicate_ids_fail(self):
        rule = sample_rule()
        result = validate_reality_rule_catalog({"version": 12, "rules": [rule, copy.deepcopy(rule)]})
        self.assertFalse(result["valid"])
        self.assertTrue(any("duplicate" in error.lower() for error in result["errors"]))

    def test_advisory_or_aesthetic_rule_cannot_be_a_hard_blocker(self):
        for rule_class in ("advisory", "aesthetic"):
            with self.subTest(rule_class=rule_class):
                rule = sample_rule()
                rule["class"] = rule_class
                rule["enforcement"] = "block"
                result = validate_reality_rule_catalog({"version": 12, "rules": [rule]})
                self.assertFalse(result["valid"])
                self.assertTrue(any("block" in error.lower() for error in result["errors"]))

    def test_catalog_contains_high_consequence_reality_rules(self):
        catalog = load_reality_rule_catalog(ROOT)
        ids = {rule["rule_id"] for rule in catalog["rules"]}
        required = {
            "ui.accessibility.keyboard-reachability",
            "ui.accessibility.focus-not-obscured",
            "ui.pointer.minimum-target-separation",
            "ui.forms.error-identification",
            "ui.forms.preserve-input-on-validation-error",
            "ui.navigation.back-preserves-context",
            "ui.state.async-action-feedback",
            "ui.recovery.retry-preserves-user-work",
            "ui.performance.no-input-blocking-work",
            "ui.motion.respect-reduced-motion",
            "ui.layout.no-document-horizontal-overflow",
            "ui.content.no-shipping-placeholders",
            "ui.data.no-fake-precision",
            "ui.modal.restore-focus-on-close",
            "ui.drag.provide-non-drag-alternative",
        }
        self.assertTrue(required.issubset(ids), sorted(required - ids))


if __name__ == "__main__":
    unittest.main()
