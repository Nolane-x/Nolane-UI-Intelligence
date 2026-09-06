import copy
import unittest


class UXV2QualityCourtTests(unittest.TestCase):
    def test_bridge_rejects_unsupported_mechanism(self):
        from nolane_ui.ux_intelligence.canonical_bridge import UX_CANONICAL_SKILL_BRIDGE, validate_ux_canonical_skill_bridge

        bad = copy.deepcopy(list(UX_CANONICAL_SKILL_BRIDGE))
        bad[0]["supported_mechanisms"] = tuple(bad[0]["supported_mechanisms"]) + ("missing-mechanism",)
        with self.assertRaises(ValueError):
            validate_ux_canonical_skill_bridge(bad)

    def test_provenance_rejects_duplicate_ids(self):
        from nolane_ui.ux_intelligence.provenance import UX_PROVENANCE, validate_ux_provenance

        bad = copy.deepcopy(list(UX_PROVENANCE))
        bad.append(copy.deepcopy(bad[0]))
        with self.assertRaises(ValueError):
            validate_ux_provenance(bad)

    def test_evaluator_registry_rejects_unknown_rule(self):
        from nolane_ui.ux_intelligence.evaluators import UX_JOURNEY_EVALUATORS, validate_ux_journey_evaluators

        bad = copy.deepcopy(list(UX_JOURNEY_EVALUATORS))
        bad[0]["rule_id"] = "ux.missing.rule"
        with self.assertRaises(ValueError):
            validate_ux_journey_evaluators(bad)


if __name__ == "__main__":
    unittest.main()
