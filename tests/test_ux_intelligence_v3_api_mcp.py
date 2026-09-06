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


if __name__ == '__main__':
    unittest.main()
