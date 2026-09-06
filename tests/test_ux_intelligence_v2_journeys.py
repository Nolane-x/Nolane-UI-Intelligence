import unittest


VALID_JOURNEY = {
    "journey_id": "checkout-primary",
    "title": "Complete primary checkout",
    "user_goal": "Buy the selected item without losing cart context",
    "entry_state": {"route": "/cart", "object_id": "cart-1"},
    "steps": (
        {
            "step_id": "review-cart",
            "intent": "Review selected item",
            "action": "continue",
            "expected_transition": {"route": "/checkout"},
            "required_context": ("object_id",),
            "preserved_context": ("object_id",),
            "allowed_detours": (),
            "recovery_expectation": "return-to-cart",
            "evidence_requirements": ("route", "object_id"),
        },
    ),
    "success_criteria": ("completion_confirmed",),
    "critical_state": ("object_id",),
    "provenance_ids": ("uxp.product-journey-contract",),
    "status": "active",
}


class UXJourneyTests(unittest.TestCase):
    def test_valid_journey_normalizes_without_inference(self):
        from nolane_ui.ux_intelligence import normalize_ux_journey_spec, validate_ux_journey_spec

        self.assertTrue(validate_ux_journey_spec(VALID_JOURNEY)["valid"])
        normalized = normalize_ux_journey_spec(VALID_JOURNEY)
        self.assertEqual(normalized["steps"][0]["expected_transition"], {"route": "/checkout"})

    def test_duplicate_step_ids_are_rejected(self):
        from nolane_ui.ux_intelligence import validate_ux_journey_spec

        bad = dict(VALID_JOURNEY)
        bad["steps"] = VALID_JOURNEY["steps"] + VALID_JOURNEY["steps"]
        with self.assertRaises(ValueError):
            validate_ux_journey_spec(bad)

    def test_missing_success_criteria_is_rejected(self):
        from nolane_ui.ux_intelligence import validate_ux_journey_spec

        bad = dict(VALID_JOURNEY)
        bad["success_criteria"] = ()
        with self.assertRaises(ValueError):
            validate_ux_journey_spec(bad)

    def test_unresolved_provenance_is_rejected(self):
        from nolane_ui.ux_intelligence import validate_ux_journey_spec

        bad = dict(VALID_JOURNEY)
        bad["provenance_ids"] = ("missing",)
        with self.assertRaises(ValueError):
            validate_ux_journey_spec(bad)


if __name__ == "__main__":
    unittest.main()
