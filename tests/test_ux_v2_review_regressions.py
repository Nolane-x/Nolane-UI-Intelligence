import unittest
from tests.test_ux_intelligence_v2_journeys import VALID_JOURNEY
from nolane_ui.ux_intelligence.evaluators import UX_JOURNEY_EVALUATORS, evaluate_ux_journey_rule
from nolane_ui.ux_intelligence import verify_ux_journey


class ReviewRegressions(unittest.TestCase):
    def test_false_boolean_activation_does_not_require_irrelevant_evidence(self):
        evaluator = next(
            item
            for item in UX_JOURNEY_EVALUATORS
            if item["evaluator_id"] == "false-completion"
        )
        result = evaluate_ux_journey_rule(
            evaluator,
            VALID_JOURNEY["steps"][0],
            {"completion_claimed": False},
        )
        self.assertEqual(result["status"], "not-executed")

    def test_same_rule_same_step_finding_id_is_unique(self):
        report = verify_ux_journey(
            VALID_JOURNEY,
            {
                "steps": {
                    "review-cart": {
                        "route": "/checkout",
                        "object_id": "cart-2",
                        "same_goal_navigation": True,
                        "context_preserved": False,
                    }
                },
                "success": {"completion_confirmed": True},
            },
        )
        ids = [finding["finding_id"] for finding in report["findings"]]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
