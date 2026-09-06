import math
import unittest

from nolane_ui.ux_intelligence.product_model import (
    build_ux_product_model,
    normalize_ux_discovery_packet,
    validate_ux_product_model,
)


class UXProductModelV3Tests(unittest.TestCase):
    def valid_model(self):
        return {
            "product_id": "shop",
            "revision": "r1",
            "surfaces": [
                {
                    "surface_id": "cart",
                    "kind": "route",
                    "locator": "/cart",
                    "labels": ["Cart"],
                    "available_action_ids": ["checkout"],
                    "visible_object_ids": ["cart-42"],
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["capture:cart"],
                },
                {
                    "surface_id": "checkout",
                    "kind": "route",
                    "locator": "/checkout",
                    "labels": ["Checkout"],
                    "available_action_ids": [],
                    "visible_object_ids": ["cart-42"],
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["capture:checkout"],
                },
            ],
            "objects": [
                {
                    "object_id": "cart-42",
                    "object_type": "cart",
                    "labels": ["Current cart"],
                    "identity_fields": ["object_id"],
                    "state_ids": ["cart-open"],
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["runtime-v11:locator:#cart:attribute:data-object-id"],
                }
            ],
            "actions": [
                {
                    "action_id": "checkout",
                    "label": "Checkout",
                    "action_kind": "activate",
                    "source_surface_id": "cart",
                    "object_id": "cart-42",
                    "observed_target_surface_ids": ["checkout"],
                    "observed_state_changes": {"checkout_started": True},
                    "commitment_level": "state-changing",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["runtime-v11:locator:#checkout:visible_text"],
                }
            ],
            "states": [
                {
                    "state_id": "cart-open",
                    "object_id": "cart-42",
                    "attributes": {"checkout_started": False},
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["runtime-v11:locator:#cart:attribute:data-state"],
                }
            ],
            "relationships": [
                {
                    "relationship_id": "cart-to-checkout",
                    "source_id": "cart",
                    "relation": "navigates-to",
                    "target_id": "checkout",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["runtime-v11:url-path:https://example.test/checkout"],
                }
            ],
            "evidence_refs": ["capture:cart", "capture:checkout"],
            "provenance_ids": ["uxp.v11-runtime-observation"],
            "status": "active",
        }

    def raw_v11(self, url):
        return {
            "version": 11,
            "collector": "test",
            "url": url,
            "viewport": {"width": 1280, "height": 720, "dpr": 1},
            "capabilities": {
                "geometry": False,
                "computed_style": False,
                "runtime_errors": True,
                "capture": False,
            },
            "observations": [
                {
                    "locator": "#checkout",
                    "visible_text": "Checkout",
                    "attributes": {"data-object-id": "cart-42"},
                }
            ],
            "runtime_errors": [],
        }

    def discovery_packet_with_runtime_v11(self):
        return {
            "product_id": "shop",
            "revision": "r1",
            "captures": [
                {
                    "capture_id": "cart-capture",
                    "surface_id": "cart",
                    "action_evidence": [],
                    "transition_evidence": [],
                    "object_evidence": [],
                    "state_evidence": [],
                    "success_evidence": [],
                    "evidence_refs": ["capture:cart"],
                    "runtime_v11": self.raw_v11("https://example.test/cart"),
                }
            ],
            "declared_goals": [],
            "declared_success_signals": [],
            "declared_object_hints": [],
            "provenance_ids": ["uxp.v11-runtime-observation"],
        }

    def complete_discovery_packet(self):
        return {
            "product_id": "shop",
            "revision": "r1",
            "captures": [
                {
                    "capture_id": "cart-capture",
                    "surface_id": "cart",
                    "surface_kind": "route",
                    "surface_locator": "/cart",
                    "surface_labels": ["Cart"],
                    "action_evidence": [
                        {
                            "action_id": "checkout",
                            "label": "Checkout",
                            "action_kind": "activate",
                            "object_id": "cart-42",
                            "commitment_level": "state-changing",
                            "target_surface_ids": ["checkout"],
                            "state_changes": {"checkout_started": True},
                            "evidence_refs": ["runtime-v11:locator:#checkout:visible_text"],
                        }
                    ],
                    "transition_evidence": [
                        {
                            "transition_id": "cart-to-checkout",
                            "source_id": "cart",
                            "relation": "navigates-to",
                            "target_id": "checkout",
                            "evidence_refs": ["runtime-v11:url-path:https://example.test/checkout"],
                        }
                    ],
                    "object_evidence": [
                        {
                            "object_id": "cart-42",
                            "object_type": "cart",
                            "labels": ["Current cart"],
                            "identity_fields": ["object_id"],
                            "state_ids": ["cart-open"],
                            "evidence_refs": [
                                "runtime-v11:locator:#cart:attribute:data-object-id",
                                "runtime-v11:locator:#cart:attribute:data-object-id",
                            ],
                        }
                    ],
                    "state_evidence": [
                        {
                            "state_id": "cart-open",
                            "object_id": "cart-42",
                            "attributes": {"checkout_started": False},
                            "evidence_refs": ["runtime-v11:locator:#cart:attribute:data-state"],
                        }
                    ],
                    "success_evidence": [],
                    "evidence_refs": ["capture:cart"],
                },
                {
                    "capture_id": "checkout-capture",
                    "surface_id": "checkout",
                    "surface_kind": "route",
                    "surface_locator": "/checkout",
                    "surface_labels": ["Checkout"],
                    "action_evidence": [],
                    "transition_evidence": [],
                    "object_evidence": [],
                    "state_evidence": [],
                    "success_evidence": [
                        {
                            "outcome_id": "order-submitted",
                            "label": "Order submitted",
                            "surface_id": "checkout",
                            "evidence_refs": ["runtime-v11:locator:#success:visible_text"],
                        }
                    ],
                    "evidence_refs": ["capture:checkout"],
                },
            ],
            "declared_goals": [],
            "declared_success_signals": [],
            "declared_object_hints": [],
            "provenance_ids": ["uxp.v11-runtime-observation"],
        }

    def test_bool_and_nonfinite_confidence_are_rejected(self):
        model = self.valid_model()
        model["surfaces"][0]["confidence"] = True
        with self.assertRaises((TypeError, ValueError)):
            validate_ux_product_model(model)

        model = self.valid_model()
        model["surfaces"][0]["confidence"] = math.inf
        with self.assertRaises(ValueError):
            validate_ux_product_model(model)

    def test_observed_record_requires_evidence(self):
        model = self.valid_model()
        model["actions"][0]["evidence_refs"] = []
        with self.assertRaises(ValueError):
            validate_ux_product_model(model)

    def test_v11_packet_is_normalized_without_inventing_semantics(self):
        normalized = normalize_ux_discovery_packet(self.discovery_packet_with_runtime_v11())
        capture = normalized["captures"][0]
        self.assertIn("runtime_v11", capture)
        self.assertEqual(capture["action_evidence"], ())
        self.assertNotIn("inferred_goal", capture)

    def test_build_model_resolves_ids_and_deduplicates_exact_evidence(self):
        model = build_ux_product_model(self.complete_discovery_packet())
        self.assertTrue(validate_ux_product_model(model)["valid"])
        surface_ids = tuple(item["surface_id"] for item in model["surfaces"])
        self.assertEqual(surface_ids, tuple(sorted(surface_ids)))
        cart = next(item for item in model["objects"] if item["object_id"] == "cart-42")
        self.assertEqual(
            cart["evidence_refs"],
            ("runtime-v11:locator:#cart:attribute:data-object-id",),
        )


if __name__ == "__main__":
    unittest.main()
