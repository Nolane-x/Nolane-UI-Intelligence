import unittest


class UXV3PublicAPITests(unittest.TestCase):
    def test_top_level_exports_v3_surfaces(self):
        import nolane_ui
        for name in (
            'validate_ux_product_model', 'normalize_ux_product_model', 'build_ux_product_model',
            'validate_ux_goal_graph', 'normalize_ux_goal_graph', 'build_ux_goal_graph', 'discover_ux_journeys',
            'query_ux_journey_candidates', 'promote_ux_journey_candidate', 'plan_ux_discovery',
            'create_ux_evidence_snapshot', 'validate_ux_evidence_snapshot', 'ux_semantic_fingerprint',
            'compare_ux_snapshots', 'rank_ux_impacts', 'ux_v3_status',
        ):
            self.assertTrue(hasattr(nolane_ui, name), name)

    def test_v3_status_preserves_authority_boundaries(self):
        from nolane_ui import ux_v3_status
        status = ux_v3_status()
        self.assertEqual(status['version'], 3)
        self.assertTrue(status['catalog_valid'])
        self.assertEqual(status['discovery_score_weight_sum'], 1.0)
        self.assertEqual(status['impact_score_weight_sum'], 1.0)
        self.assertFalse(status['discovery_can_create_blocking_findings'])
        self.assertFalse(status['owns_browser_runtime'])
        self.assertTrue(status['uses_v2_verification_authority'])
        self.assertFalse(status['uses_rule_count_quota'])
        self.assertFalse(status['uses_skill_count_quota'])
        self.assertFalse(status['uses_journey_count_quota'])


class UXV3MCPTests(unittest.TestCase):
    def candidate(self):
        return {
            "candidate_id": "uxc:mcp",
            "candidate_fingerprint": "mcp",
            "product_id": "shop",
            "revision": "r1",
            "goal_node_id": "goal:submit-order",
            "title": "Submit order",
            "entry_state": {"surface_id": "cart", "route": "/cart"},
            "step_hypotheses": (
                {
                    "candidate_step_id": "step-1:checkout",
                    "intent_hypothesis": "Checkout",
                    "action_id": "checkout",
                    "source_surface_id": "cart",
                    "expected_target_surface_ids": ("confirmation",),
                    "required_context_hypotheses": ("object_id",),
                    "preserved_context_hypotheses": ("object_id",),
                    "recovery_hypotheses": ("return-to-cart",),
                    "evidence_refs": ("action:checkout",),
                    "origin": "observed",
                    "confidence": 1.0,
                },
            ),
            "success_hypotheses": ({"outcome_id": "done", "surface_id": "confirmation"},),
            "critical_state_hypotheses": ("checkout",),
            "discovery_score": 1.0,
            "score_components": {},
            "origin_summary": {"goal_origin": "declared", "path_origins": ("observed",), "success_origins": ("observed",)},
            "evidence_refs": ("action:checkout",),
            "provenance_ids": ("uxp.v11-runtime-observation",),
            "status": "hypothesis",
        }

    def test_tool_catalog_contains_complete_v3_namespace(self):
        from nolane_ui import mcp_server
        names = {item["name"] for item in mcp_server.tool_catalog()}
        self.assertTrue({
            "nui_ux_v3_status", "nui_build_ux_product_model", "nui_build_ux_goal_graph",
            "nui_discover_ux_journeys", "nui_query_ux_journey_candidates",
            "nui_promote_ux_journey_candidate", "nui_plan_ux_discovery",
            "nui_create_ux_evidence_snapshot", "nui_compare_ux_snapshots", "nui_rank_ux_impacts",
        }.issubset(names))

    def test_planner_wrapper_returns_requests_only(self):
        from nolane_ui import mcp_server
        result = mcp_server.plan_ux_discovery_record(self.candidate(), ["browser-runtime"])
        self.assertIn("requests", result)
        self.assertTrue(result["requests"])
        for item in result["requests"]:
            self.assertNotIn("executed", item)
            self.assertNotIn("observed", item)
            self.assertNotIn("success", item)
            self.assertEqual(item["claim_boundary"], "evidence-request-only")

    def test_v3_status_wrapper_is_read_only_boundary_report(self):
        from nolane_ui import mcp_server
        status = mcp_server.get_ux_v3_status()
        self.assertEqual(status["version"], 3)
        self.assertFalse(status["owns_browser_runtime"])
        self.assertFalse(status["discovery_can_create_blocking_findings"])


if __name__ == '__main__':
    unittest.main()
