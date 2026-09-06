import unittest


class UXV2PublicApiMcpTests(unittest.TestCase):
    def test_top_level_exports_exist(self):
        import nolane_ui

        for name in (
            "UX_CANONICAL_SKILL_BRIDGE",
            "UX_PROVENANCE",
            "UX_JOURNEY_EVALUATORS",
            "get_ux_provenance",
            "query_ux_provenance",
            "get_ux_canonical_skill_bridge",
            "query_ux_canonical_skill_bridge",
            "validate_ux_journey_spec",
            "verify_ux_journey",
            "ux_v2_status",
        ):
            self.assertTrue(hasattr(nolane_ui, name), name)

    def test_mcp_tool_catalog_contains_v2_tools(self):
        from nolane_ui import mcp_server

        names = {item["name"] for item in mcp_server.tool_catalog()}
        expected = {
            "nui_ux_v2_status",
            "nui_get_ux_provenance",
            "nui_query_ux_provenance",
            "nui_get_ux_canonical_skill_bridge",
            "nui_query_ux_canonical_skill_bridge",
            "nui_verify_ux_journey",
        }
        self.assertTrue(expected <= names)

    def test_exact_mcp_lookup_raises_for_missing_id(self):
        from nolane_ui import mcp_server

        with self.assertRaises(ValueError):
            mcp_server.get_ux_provenance_record("missing")
        with self.assertRaises(ValueError):
            mcp_server.get_ux_canonical_skill_bridge_record("missing")

    def test_v2_status_reports_integrity_without_quotas(self):
        import nolane_ui

        status = nolane_ui.ux_v2_status()
        self.assertTrue(status["valid"])
        self.assertFalse(status["uses_rule_count_quota"])
        self.assertFalse(status["uses_skill_count_quota"])
        self.assertGreater(status["canonical_skill_bridge_count"], 0)
        self.assertGreater(status["provenance_count"], 0)
        self.assertGreater(status["evaluator_count"], 0)


if __name__ == "__main__":
    unittest.main()
