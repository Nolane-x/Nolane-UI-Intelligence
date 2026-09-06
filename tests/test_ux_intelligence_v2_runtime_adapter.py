import unittest

from tests.test_ux_intelligence_v2_journeys import VALID_JOURNEY


V11_PACKET = {
    "version": 11,
    "collector": "test-runtime",
    "url": "https://example.test/checkout",
    "viewport": {"width": 1280, "height": 720, "dpr": 1},
    "capabilities": {
        "geometry": False,
        "computed_style": False,
        "runtime_errors": False,
        "capture": False,
    },
    "observations": [
        {
            "locator": "#cart-context",
            "visible_text": "Cart 1",
            "attributes": {"data-object-id": "cart-1"},
        },
        {
            "locator": "#completion",
            "visible_text": "Complete",
            "attributes": {"data-completion-confirmed": "true"},
        },
    ],
    "runtime_errors": [],
}

BINDINGS = {
    "steps": {
        "review-cart": {
            "route": {"source": "url_path"},
            "object_id": {
                "source": "attribute",
                "locator": "#cart-context",
                "name": "data-object-id",
            },
        },
    },
    "success": {
        "completion_confirmed": {
            "source": "attribute",
            "locator": "#completion",
            "name": "data-completion-confirmed",
            "coerce": "bool",
        },
    },
}


class UXV2RuntimeAdapterTests(unittest.TestCase):
    def test_adapter_extracts_bound_fields_from_real_v11_shape(self):
        from nolane_ui.ux_intelligence import adapt_v11_browser_observation

        evidence = adapt_v11_browser_observation(V11_PACKET, BINDINGS)
        self.assertEqual(evidence["steps"]["review-cart"]["route"], "/checkout")
        self.assertEqual(evidence["steps"]["review-cart"]["object_id"], "cart-1")
        self.assertIs(evidence["success"]["completion_confirmed"], True)
        refs = evidence["steps"]["review-cart"]["_evidence_refs"]
        self.assertIn("#cart-context", refs["object_id"])

    def test_verifier_accepts_v11_packet_with_explicit_bindings(self):
        from nolane_ui.ux_intelligence import verify_ux_journey

        report = verify_ux_journey(
            VALID_JOURNEY,
            {"runtime_v11": V11_PACKET, "bindings": BINDINGS},
        )
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["runtime_evidence"]["version"], 11)
        self.assertEqual(report["runtime_evidence"]["collector"], "test-runtime")

    def test_missing_bound_locator_becomes_missing_evidence_not_failure(self):
        from nolane_ui.ux_intelligence import verify_ux_journey

        bindings = {
            "steps": {
                "review-cart": {
                    "route": {"source": "url_path"},
                    "object_id": {
                        "source": "attribute",
                        "locator": "#missing",
                        "name": "data-object-id",
                    },
                },
            },
            "success": BINDINGS["success"],
        }
        report = verify_ux_journey(
            VALID_JOURNEY,
            {"runtime_v11": V11_PACKET, "bindings": bindings},
        )
        self.assertEqual(report["status"], "insufficient-evidence")
        self.assertFalse(report["findings"])
        self.assertTrue(any(gap["field"] == "object_id" for gap in report["evidence_gaps"]))

    def test_invalid_v11_packet_is_rejected_by_v11_contract(self):
        from nolane_ui.ux_intelligence import adapt_v11_browser_observation

        bad = dict(V11_PACKET)
        bad["version"] = 10
        with self.assertRaises(ValueError):
            adapt_v11_browser_observation(bad, BINDINGS)


if __name__ == "__main__":
    unittest.main()
