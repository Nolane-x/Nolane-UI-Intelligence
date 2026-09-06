from __future__ import annotations

import unittest
from pathlib import Path

import nolane_ui
from nolane_ui import mcp_server


class UXIntelligenceV1PublicApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def test_top_level_api_exposes_ux_intelligence(self):
        expected = (
            "UX_MECHANISMS",
            "UX_SKILLS",
            "UX_RULES",
            "get_ux_mechanism",
            "query_ux_mechanisms",
            "get_ux_skill",
            "query_ux_skills",
            "get_ux_rule",
            "query_ux_rules",
            "ux_intelligence_status",
        )
        for name in expected:
            self.assertTrue(hasattr(nolane_ui, name), name)

        status = nolane_ui.ux_intelligence_status()
        self.assertTrue(status["valid"], status)
        self.assertEqual(status["version"], 1)
        self.assertIs(status["rule_count_is_quality_target"], False)
        self.assertIs(status["skill_count_is_quality_target"], False)

    def test_top_level_queries_remain_bounded(self):
        rules = nolane_ui.query_ux_rules(mechanism_id="context-loss", limit=2)
        self.assertGreaterEqual(len(rules), 1)
        self.assertLessEqual(len(rules), 2)
        with self.assertRaises(ValueError):
            nolane_ui.query_ux_rules(limit=101)


class UXIntelligenceV1McpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def test_tool_catalog_exposes_bounded_ux_tools(self):
        names = {item["name"] for item in mcp_server.tool_catalog(self.root)}
        self.assertTrue(
            {
                "nui_ux_status",
                "nui_get_ux_mechanism",
                "nui_query_ux_mechanisms",
                "nui_get_ux_skill",
                "nui_query_ux_skills",
                "nui_get_ux_rule",
                "nui_query_ux_rules",
            }.issubset(names),
            names,
        )

    def test_mcp_exact_lookup_uses_distinct_ux_namespace(self):
        mechanism = mcp_server.get_ux_mechanism_record(self.root, "context-loss")
        self.assertEqual(mechanism["mechanism_id"], "context-loss")
        skill = mcp_server.get_ux_skill_record(self.root, "identifying-user-goals")
        self.assertEqual(skill["skill_id"], "identifying-user-goals")
        rule = mcp_server.get_ux_rule_record(
            self.root, "ux.recovery.progress-not-silently-destroyed"
        )
        self.assertEqual(rule["rule_id"], "ux.recovery.progress-not-silently-destroyed")

        with self.assertRaises(ValueError):
            mcp_server.get_ux_mechanism_record(self.root, "missing")
        with self.assertRaises(ValueError):
            mcp_server.get_ux_skill_record(self.root, "missing")
        with self.assertRaises(ValueError):
            mcp_server.get_ux_rule_record(self.root, "missing")

    def test_mcp_ux_queries_are_bounded_and_filterable(self):
        mechanisms = mcp_server.query_ux_mechanism_records(
            self.root, text="navigation", limit=2
        )
        self.assertGreaterEqual(mechanisms["count"], 1)
        self.assertLessEqual(len(mechanisms["mechanisms"]), 2)

        skills = mcp_server.query_ux_skill_records(
            self.root, domain="recovery", limit=2
        )
        self.assertEqual(skills["count"], 2)
        self.assertTrue(all(item["domain"] == "recovery" for item in skills["skills"]))

        rules = mcp_server.query_ux_rule_records(
            self.root, mechanism_id="context-loss", limit=2
        )
        self.assertGreaterEqual(rules["count"], 1)
        self.assertTrue(
            all(item["mechanism_id"] == "context-loss" for item in rules["rules"])
        )

        with self.assertRaises(ValueError):
            mcp_server.query_ux_rule_records(self.root, limit=101)

    def test_mcp_ux_status_preserves_no_quota_boundary(self):
        status = mcp_server.get_ux_status(self.root)
        self.assertTrue(status["valid"], status)
        self.assertIs(status["rule_count_is_quality_target"], False)
        self.assertIs(status["skill_count_is_quality_target"], False)


if __name__ == "__main__":
    unittest.main()
