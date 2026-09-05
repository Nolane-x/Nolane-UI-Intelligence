import unittest
from pathlib import Path

import nolane_ui
from nolane_ui import mcp_server


class RuleV13PublicApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def test_top_level_api_exposes_v13_rule_intelligence(self):
        expected = (
            "get_rule_v13",
            "query_rules_v13",
            "rule_catalog_status_v13",
            "get_rule_provenance_v13",
            "explain_rule_capabilities_v13",
        )
        for name in expected:
            self.assertTrue(hasattr(nolane_ui, name), name)

        status = nolane_ui.rule_catalog_status_v13(self.root)
        self.assertTrue(status["valid"], status)
        self.assertGreaterEqual(status["rule_count"], 89)

    def test_capability_explanation_preserves_unknown_boundaries(self):
        result = nolane_ui.explain_rule_capabilities_v13(
            "ui.convergence.product-substitution-plausibility", root=self.root
        )
        self.assertEqual(result["rule_id"], "ui.convergence.product-substitution-plausibility")
        self.assertIn("semantic-product", result["required"])
        self.assertIn("human-review", result["required"])
        self.assertIn("accessibility-tree", result["unsupported"])
        self.assertNotIn("accessibility-tree", result["supported"])

    def test_provenance_lookup_is_exact_and_bounded(self):
        record = nolane_ui.get_rule_provenance_v13("nui-anti-convergence-corpus-2026-09-01", root=self.root)
        self.assertEqual(record["evidence_class"], "corroborated")
        self.assertIsNone(nolane_ui.get_rule_provenance_v13("missing", root=self.root))


class RuleV13McpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def test_tool_catalog_exposes_bounded_v13_tools(self):
        names = {item["name"] for item in mcp_server.tool_catalog(self.root)}
        self.assertTrue({
            "nui_rule_status",
            "nui_get_rule",
            "nui_query_rules",
            "nui_rule_provenance",
            "nui_runtime_doctor",
        }.issubset(names), names)

    def test_mcp_rule_lookup_and_query_are_bounded(self):
        rule = mcp_server.get_rule_record(self.root, "ui.forms.submit-idempotency")
        self.assertEqual(rule["rule_id"], "ui.forms.submit-idempotency")
        with self.assertRaises(ValueError):
            mcp_server.get_rule_record(self.root, "ui.missing.rule")

        result = mcp_server.query_rule_records(self.root, domain="convergence", limit=2)
        self.assertEqual(result["count"], 2)
        self.assertEqual(len(result["rules"]), 2)
        with self.assertRaises(ValueError):
            mcp_server.query_rule_records(self.root, limit=101)

    def test_runtime_doctor_tool_is_read_only_and_valid(self):
        result = mcp_server.get_runtime_doctor(self.root)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["mutation_policy"], "Doctor is read-only; repairs require an explicit follow-up command/owner.")


if __name__ == "__main__":
    unittest.main()
