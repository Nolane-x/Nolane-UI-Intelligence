import json
import tempfile
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.registry import load_rule_registry, validate_rule_registry


VALID_RULE = {
    "rule_id": "runtime.integrity.broken-image-src",
    "domain": "runtime-integrity",
    "class": "mechanical",
    "tier": "edit",
    "severity": "major",
    "engines": ["markup", "text"],
    "description": "Image source is empty or a placeholder value.",
    "falsifier": "The source resolves to an intentional runtime-provided asset before render.",
    "owner_hints": ["designing-visual-media"],
    "source_provenance": {
        "kind": "independent-nui-rule",
        "research_inspiration": ["deterministic UI observation"],
        "implementation": "independently-authored",
    },
}


class RuntimeV11RegistryTests(unittest.TestCase):
    def test_valid_registry_passes(self):
        result = validate_rule_registry({"version": 11, "rules": [VALID_RULE]})
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["rule_count"], 1)

    def test_duplicate_rule_ids_fail(self):
        result = validate_rule_registry({"version": 11, "rules": [VALID_RULE, dict(VALID_RULE)]})
        self.assertFalse(result["valid"])
        self.assertTrue(any("duplicate" in error.lower() for error in result["errors"]))

    def test_missing_falsifier_and_provenance_fail(self):
        rule = dict(VALID_RULE)
        rule.pop("falsifier")
        rule.pop("source_provenance")
        result = validate_rule_registry({"version": 11, "rules": [rule]})
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("falsifier", joined)
        self.assertIn("provenance", joined)

    def test_invalid_class_tier_and_engine_fail(self):
        rule = dict(VALID_RULE)
        rule.update({"class": "taste-score", "tier": "always", "engines": ["llm"]})
        result = validate_rule_registry({"version": 11, "rules": [rule]})
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("class", joined)
        self.assertIn("tier", joined)
        self.assertIn("engine", joined)

    def test_genericness_and_advisory_cannot_be_edit_blockers(self):
        for rule_class in ("genericness", "advisory"):
            with self.subTest(rule_class=rule_class):
                rule = dict(VALID_RULE)
                rule.update({"rule_id": f"runtime.genericness.{rule_class}", "class": rule_class, "tier": "edit"})
                result = validate_rule_registry({"version": 11, "rules": [rule]})
                self.assertFalse(result["valid"])
                self.assertTrue(any("edit" in error.lower() for error in result["errors"]))

    def test_legacy_mechanism_sources_are_rejected(self):
        rule = dict(VALID_RULE)
        rule["source_provenance"] = {
            "kind": "independent-nui-rule",
            "mechanism_sources": ["external-repository:pattern"],
            "implementation": "independently-authored",
        }
        result = validate_rule_registry({"version": 11, "rules": [rule]})
        self.assertFalse(result["valid"])
        self.assertTrue(any("mechanism_sources" in error for error in result["errors"]))

    def test_research_inspiration_must_be_nonempty_strings_when_present(self):
        for inspiration in ("external-reference", ["valid", ""], [1]):
            with self.subTest(inspiration=inspiration):
                rule = dict(VALID_RULE)
                rule["source_provenance"] = {
                    "kind": "independent-nui-rule",
                    "research_inspiration": inspiration,
                    "implementation": "independently-authored",
                }
                result = validate_rule_registry({"version": 11, "rules": [rule]})
                self.assertFalse(result["valid"])
                self.assertTrue(any("research_inspiration" in error for error in result["errors"]))

    def test_external_inspiration_is_optional_for_independent_rule(self):
        rule = dict(VALID_RULE)
        rule["source_provenance"] = {
            "kind": "independent-nui-rule",
            "implementation": "independently-authored",
        }
        result = validate_rule_registry({"version": 11, "rules": [rule]})
        self.assertTrue(result["valid"], result["errors"])

    def test_load_registry_reads_and_validates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            knowledge = root / "knowledge"
            knowledge.mkdir()
            payload = {"version": 11, "rules": [VALID_RULE]}
            (knowledge / "runtime-detector-rules-v11.json").write_text(json.dumps(payload), encoding="utf-8")
            loaded = load_rule_registry(root)
            self.assertEqual(loaded["version"], 11)
            self.assertEqual(loaded["rules"][0]["rule_id"], VALID_RULE["rule_id"])


if __name__ == "__main__":
    unittest.main()
