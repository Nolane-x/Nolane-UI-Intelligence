import unittest

from tests.test_ux_intelligence_v2_journeys import VALID_JOURNEY


class UXJourneyVerifierTests(unittest.TestCase):
    def test_missing_required_evidence_is_not_a_failure(self):
        from nolane_ui.ux_intelligence import verify_ux_journey

        report = verify_ux_journey(
            VALID_JOURNEY,
            {"steps": {"review-cart": {"route": "/checkout"}}},
        )
        self.assertEqual(report["status"], "insufficient-evidence")
        self.assertFalse(report["findings"])
        self.assertTrue(report["evidence_gaps"])

    def test_false_completion_produces_rule_derived_finding(self):
        from nolane_ui.ux_intelligence import verify_ux_journey

        journey = dict(VALID_JOURNEY)
        journey["steps"] = (
            dict(
                VALID_JOURNEY["steps"][0],
                evidence_requirements=("route", "object_id", "completion_claimed", "completion_confirmed"),
            ),
        )
        report = verify_ux_journey(
            journey,
            {
                "steps": {
                    "review-cart": {
                        "route": "/checkout",
                        "object_id": "cart-1",
                        "completion_claimed": True,
                        "completion_confirmed": False,
                    }
                }
            },
        )
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["findings"][0]["rule_id"], "ux.comprehension.no-false-completion")
        self.assertTrue(report["findings"][0]["mechanism_id"])
        self.assertTrue(report["findings"][0]["verification_mode"])

    def test_complete_journey_passes(self):
        from nolane_ui.ux_intelligence import verify_ux_journey

        report = verify_ux_journey(
            VALID_JOURNEY,
            {
                "steps": {
                    "review-cart": {
                        "route": "/checkout",
                        "object_id": "cart-1",
                        "completion_confirmed": True,
                    }
                },
                "success": {"completion_confirmed": True},
            },
        )
        self.assertEqual(report["status"], "passed")
        self.assertFalse(report["findings"])


if __name__ == "__main__":
    unittest.main()
