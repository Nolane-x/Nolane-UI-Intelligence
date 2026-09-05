import json
import tempfile
import unittest
from pathlib import Path

from nolane_ui.reality_catalog_v12 import REALITY_RULES_V12
from nolane_ui.rules_v13.catalog import get_rule_v13, load_rule_catalog_v13, query_rules_v13
from nolane_ui.rules_v13.compat_v12 import normalize_v12_rule
from nolane_ui.rules_v13.contracts import validate_catalog_v13, validate_rule_v13
from nolane_ui.rules_v13.provenance import validate_provenance_ledger_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity
from nolane_ui.rules_v13.shards.foundation import FOUNDATION_RULES_V13


class RuleV13CompatibilityTests(unittest.TestCase):
    def test_v12_blocking_authority_is_not_weakened(self):
        source = next(rule for rule in REALITY_RULES_V12 if rule["rule_id"] == "ui.forms.submit-idempotency")
        normalized = normalize_v12_rule(source)
        self.assertEqual(normalized["rule_id"], source["rule_id"])
        self.assertEqual(normalized["class"], source["class"])
        self.assertEqual(normalized["severity"], source["severity"])
        self.assertEqual(normalized["enforcement"], source["enforcement"])
        self.assertTrue(validate_rule_v13(normalized)["valid"], validate_rule_v13(normalized)["errors"])
        self.assertIn("nui-v12-reality-catalog", normalized["provenance_ids"])
        self.assertEqual(normalized["legacy_contract_version"], 12)

    def test_v12_contextual_warning_remains_non_blocking(self):
        source = next(rule for rule in REALITY_RULES_V12 if rule["rule_id"] == "ui.state.disabled-control-reason")
        normalized = normalize_v12_rule(source)
        self.assertEqual(normalized["class"], "contextual")
        self.assertEqual(normalized["enforcement"], "warn")
        self.assertTrue(validate_rule_v13(normalized)["valid"])

    def test_all_v12_reality_rules_normalize_to_v13_contract(self):
        failures = []
        for source in REALITY_RULES_V12:
            result = validate_rule_v13(normalize_v12_rule(source))
            if not result["valid"]:
                failures.append((source["rule_id"], result["errors"]))
        self.assertFalse(failures, failures)


class RuleV13FoundationTests(unittest.TestCase):
    def test_foundation_shard_is_independently_valid(self):
        self.assertGreaterEqual(len(FOUNDATION_RULES_V13), 12)
        result = validate_catalog_v13({"version": 13, "rules": FOUNDATION_RULES_V13})
        self.assertTrue(result["valid"], result["errors"])

    def test_convergence_rules_are_never_blocking(self):
        convergence = [rule for rule in FOUNDATION_RULES_V13 if rule["class"] == "convergence"]
        self.assertGreaterEqual(len(convergence), 8)
        for rule in convergence:
            self.assertIn(rule["enforcement"], {"warn", "review"}, rule["rule_id"])
            self.assertNotEqual(rule["severity"], "critical", rule["rule_id"])
            self.assertIn("semantic-product", rule["capabilities"])
            self.assertIn("human-review", rule["capabilities"])
            self.assertTrue(rule["falsifiers"], rule["rule_id"])

    def test_foundation_shard_has_no_similarity_duplicates(self):
        result = audit_catalog_similarity(FOUNDATION_RULES_V13)
        self.assertTrue(result["valid"], result)


class RuleV13CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)

    def test_catalog_composes_v12_and_v13_shards(self):
        self.assertEqual(self.catalog["version"], 13)
        self.assertGreaterEqual(len(self.catalog["rules"]), len(REALITY_RULES_V12) + len(FOUNDATION_RULES_V13))
        self.assertEqual(len(self.catalog["rules"]), len({rule["rule_id"] for rule in self.catalog["rules"]}))
        validation = validate_catalog_v13(self.catalog)
        self.assertTrue(validation["valid"], validation["errors"])
        similarity = audit_catalog_similarity(self.catalog["rules"])
        self.assertTrue(similarity["valid"], similarity)

    def test_every_catalog_rule_resolves_provenance(self):
        ledger = self.catalog["provenance"]
        ledger_result = validate_provenance_ledger_v13(ledger)
        self.assertTrue(ledger_result["valid"], ledger_result["errors"])
        known = {record["provenance_id"] for record in ledger["records"]}
        missing = {
            provenance_id
            for rule in self.catalog["rules"]
            for provenance_id in rule["provenance_ids"]
            if provenance_id not in known
        }
        self.assertFalse(missing, missing)

    def test_query_and_exact_lookup_are_bounded_and_deterministic(self):
        exact = get_rule_v13("ui.forms.submit-idempotency", root=self.root)
        self.assertIsNotNone(exact)
        self.assertEqual(exact["rule_id"], "ui.forms.submit-idempotency")

        first = query_rules_v13(root=self.root, domain="convergence", limit=3)
        second = query_rules_v13(root=self.root, domain="convergence", limit=3)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 3)
        self.assertTrue(all(rule["domain"] == "convergence" for rule in first))

        with self.assertRaises(ValueError):
            query_rules_v13(root=self.root, limit=0)
        with self.assertRaises(ValueError):
            query_rules_v13(root=self.root, limit=101)

    def test_catalog_load_rejects_missing_provenance_ledger(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "knowledge").mkdir()
            with self.assertRaises(FileNotFoundError):
                load_rule_catalog_v13(root)


if __name__ == "__main__":
    unittest.main()
