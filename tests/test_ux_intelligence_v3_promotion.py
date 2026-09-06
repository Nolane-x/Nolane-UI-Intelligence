import copy
import unittest

from nolane_ui.ux_intelligence.promotion import promote_ux_journey_candidate
from nolane_ui.ux_intelligence.journeys import validate_ux_journey_spec


class UXPromotionV3Tests(unittest.TestCase):
    def product_model(self):
        return {
            "product_id": "shop",
            "revision": "r1",
            "surfaces": (
                {
                    "surface_id": "cart",
                    "kind": "route",
                    "locator": "/cart",
                    "labels": ("Cart",),
                    "available_action_ids": ("checkout",),
                    "visible_object_ids": ("cart-42",),
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("surface:cart",),
                },
                {
                    "surface_id": "confirmation",
                    "kind": "route",
                    "locator": "/confirmation",
                    "labels": ("Confirmation",),
                    "available_action_ids": (),
                    "visible_object_ids": ("cart-42",),
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("surface:confirmation",),
                },
            ),
            "objects": (
                {
                    "object_id": "cart-42",
                    "object_type": "cart",
                    "labels": ("Current cart",),
                    "identity_fields": ("object_id",),
                    "state_ids": ("cart-open",),
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("object:cart-42",),
                },
            ),
            "actions": (
                {
                    "action_id": "checkout",
                    "label": "Checkout",
                    "action_kind": "activate",
                    "source_surface_id": "cart",
                    "object_id": "cart-42",
                    "observed_target_surface_ids": ("confirmation",),
                    "observed_state_changes": {"submitted": True},
                    "commitment_level": "external-effect",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("action:checkout",),
                },
            ),
            "states": (
                {
                    "state_id": "cart-open",
                    "object_id": "cart-42",
                    "attributes": {"object_id": "cart-42"},
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("state:cart-open",),
                },
            ),
            "relationships": (),
            "outcomes": (
                {
                    "outcome_id": "order-submitted",
                    "label": "Order submitted",
                    "surface_id": "confirmation",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("outcome:order-submitted",),
                },
            ),
            "evidence_refs": ("surface:cart", "surface:confirmation"),
            "provenance_ids": ("uxp.v11-runtime-observation",),
            "status": "active",
        }

    def goal_graph(self, *, inferred=False):
        origin = "inferred" if inferred else "declared"
        evidence = ("inference:checkout",) if inferred else ()
        return {
            "product_id": "shop",
            "revision": "r1",
            "nodes": (
                {
                    "node_id": "goal:submit-order",
                    "kind": "goal",
                    "label": "Submit an order",
                    "description": "Complete checkout",
                    "origin": origin,
                    "confidence": 0.8 if inferred else 1.0,
                    "evidence_refs": evidence,
                },
                {
                    "node_id": "outcome:order-submitted",
                    "kind": "outcome",
                    "label": "Order submitted",
                    "description": "Observed outcome",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("outcome:order-submitted",),
                },
            ),
            "edges": (
                {
                    "edge_id": "goal-outcome",
                    "source_id": "goal:submit-order",
                    "relation": "succeeds-when",
                    "target_id": "outcome:order-submitted",
                    "origin": origin,
                    "confidence": 0.8 if inferred else 1.0,
                    "evidence_refs": evidence,
                },
            ),
            "evidence_refs": ("outcome:order-submitted",) + evidence,
            "provenance_ids": (
                ("uxp.v11-runtime-observation",)
                if inferred
                else ("uxp.product-journey-contract", "uxp.v11-runtime-observation")
            ),
            "status": "active",
        }

    def candidate(self, *, inferred=False, recovery=True):
        return {
            "candidate_id": "uxc:promotion-test",
            "candidate_fingerprint": "promotion-test",
            "product_id": "shop",
            "revision": "r1",
            "goal_node_id": "goal:submit-order",
            "title": "Submit an order via /cart",
            "entry_state": {"surface_id": "cart", "route": "/cart", "object_id": "cart-42"},
            "step_hypotheses": (
                {
                    "candidate_step_id": "step-1:checkout",
                    "intent_hypothesis": "Use Checkout",
                    "action_id": "checkout",
                    "source_surface_id": "cart",
                    "expected_target_surface_ids": ("confirmation",),
                    "required_context_hypotheses": ("object_id",),
                    "preserved_context_hypotheses": ("object_id",),
                    "recovery_hypotheses": (("return-to-cart",) if recovery else ()),
                    "evidence_refs": ("action:checkout",),
                    "origin": "observed",
                    "confidence": 1.0,
                },
            ),
            "success_hypotheses": (
                {
                    "outcome_id": "order-submitted",
                    "label": "Order submitted",
                    "surface_id": "confirmation",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("outcome:order-submitted",),
                },
            ),
            "critical_state_hypotheses": ("checkout",),
            "discovery_score": 0.95,
            "score_components": {},
            "origin_summary": {
                "goal_origin": "inferred" if inferred else "declared",
                "path_origins": ("observed",),
                "success_origins": ("observed",),
            },
            "evidence_refs": ("action:checkout", "outcome:order-submitted"),
            "provenance_ids": ("uxp.product-journey-contract", "uxp.v11-runtime-observation"),
            "status": "hypothesis",
        }

    def test_inferred_goal_cannot_promote(self):
        result = promote_ux_journey_candidate(
            self.candidate(inferred=True), self.product_model(), self.goal_graph(inferred=True)
        )
        self.assertEqual(result["status"], "promotion-gaps")
        self.assertIn("goal-not-declared", {gap["code"] for gap in result["promotion_gaps"]})
        self.assertIsNone(result["journey"])

    def test_missing_recovery_semantics_cannot_be_filled_with_not_applicable(self):
        result = promote_ux_journey_candidate(
            self.candidate(recovery=False), self.product_model(), self.goal_graph()
        )
        self.assertIn("recovery-expectation-unproven", {gap["code"] for gap in result["promotion_gaps"]})
        self.assertIsNone(result["journey"])

    def test_promoted_mapping_passes_existing_v2_validator_unchanged(self):
        result = promote_ux_journey_candidate(
            self.candidate(), self.product_model(), self.goal_graph()
        )
        self.assertEqual(result["status"], "promoted")
        self.assertTrue(validate_ux_journey_spec(result["journey"])["valid"])
        self.assertEqual(result["journey"]["steps"][0]["expected_transition"], {"route": "/confirmation"})
        self.assertEqual(result["journey"]["steps"][0]["recovery_expectation"], "return-to-cart")

    def test_promotion_is_deterministic_and_does_not_mutate_inputs(self):
        candidate = self.candidate()
        model = self.product_model()
        graph = self.goal_graph()
        before = copy.deepcopy((candidate, model, graph))
        first = promote_ux_journey_candidate(candidate, model, graph)
        second = promote_ux_journey_candidate(candidate, model, graph)
        self.assertEqual(first, second)
        self.assertEqual((candidate, model, graph), before)

    def test_ambiguous_target_surface_blocks_promotion_instead_of_guessing(self):
        candidate = self.candidate()
        candidate["step_hypotheses"][0]["expected_target_surface_ids"] = ("cart", "confirmation")
        result = promote_ux_journey_candidate(candidate, self.product_model(), self.goal_graph())
        self.assertIn("expected-transition-ambiguous", {gap["code"] for gap in result["promotion_gaps"]})
        self.assertIsNone(result["journey"])


if __name__ == "__main__":
    unittest.main()
