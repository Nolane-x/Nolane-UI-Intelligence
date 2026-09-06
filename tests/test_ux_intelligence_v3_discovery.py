import copy
import unittest

from nolane_ui.ux_intelligence.discovery import (
    discover_ux_journeys,
    query_ux_journey_candidates,
)
from nolane_ui.ux_intelligence.v3_catalog import UX_DISCOVERY_SCORE_WEIGHTS


class UXDiscoveryV3Tests(unittest.TestCase):
    def product_model(self, *, cyclic=False):
        actions = [
            {
                "action_id": "checkout",
                "label": "Checkout",
                "action_kind": "activate",
                "source_surface_id": "cart",
                "object_id": "cart-42",
                "observed_target_surface_ids": ("checkout",),
                "observed_state_changes": {"checkout_started": True},
                "commitment_level": "state-changing",
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": ("action:checkout",),
            },
            {
                "action_id": "submit-order",
                "label": "Submit order",
                "action_kind": "activate",
                "source_surface_id": "checkout",
                "object_id": "cart-42",
                "observed_target_surface_ids": ("confirmation",),
                "observed_state_changes": {"submitted": True},
                "commitment_level": "external-effect",
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": ("action:submit-order",),
            },
        ]
        if cyclic:
            actions.append(
                {
                    "action_id": "edit-cart",
                    "label": "Edit cart",
                    "action_kind": "activate",
                    "source_surface_id": "checkout",
                    "object_id": "cart-42",
                    "observed_target_surface_ids": ("cart",),
                    "observed_state_changes": {},
                    "commitment_level": "reversible",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("action:edit-cart",),
                }
            )
        surfaces = []
        for sid, locator, available in (
            ("cart", "/cart", ("checkout",)),
            ("checkout", "/checkout", ("edit-cart", "submit-order") if cyclic else ("submit-order",)),
            ("confirmation", "/confirmation", ()),
        ):
            surfaces.append(
                {
                    "surface_id": sid,
                    "kind": "route",
                    "locator": locator,
                    "labels": (sid.title(),),
                    "available_action_ids": tuple(a for a in available if a in {item["action_id"] for item in actions}),
                    "visible_object_ids": ("cart-42",),
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": (f"surface:{sid}",),
                }
            )
        return {
            "product_id": "shop",
            "revision": "r1",
            "surfaces": tuple(sorted(surfaces, key=lambda item: item["surface_id"])),
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
            "actions": tuple(sorted(actions, key=lambda item: item["action_id"])),
            "states": (
                {
                    "state_id": "cart-open",
                    "object_id": "cart-42",
                    "attributes": {},
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
            "evidence_refs": ("surface:cart", "surface:checkout", "surface:confirmation"),
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

    def test_score_weights_are_explicit_and_sum_to_one(self):
        self.assertEqual(
            set(UX_DISCOVERY_SCORE_WEIGHTS),
            {
                "goal_confidence",
                "success_evidence_strength",
                "path_evidence_coverage",
                "critical_action_presence",
                "recovery_relevance",
                "novelty_against_verified_journeys",
            },
        )
        self.assertAlmostEqual(sum(UX_DISCOVERY_SCORE_WEIGHTS.values()), 1.0)

    def test_candidates_are_deterministic_and_semantic_ids_are_unique(self):
        first = discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=8)
        second = discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=8)
        self.assertEqual(first, second)
        self.assertTrue(first)
        self.assertEqual(len({item["candidate_id"] for item in first}), len(first))
        self.assertEqual(first[0]["step_hypotheses"][0]["action_id"], "checkout")
        self.assertEqual(first[0]["step_hypotheses"][-1]["action_id"], "submit-order")

    def test_cycle_terminates_at_bounded_repeated_semantic_state(self):
        candidates = discover_ux_journeys(self.product_model(cyclic=True), self.goal_graph(), max_depth=8)
        self.assertTrue(candidates)
        self.assertLessEqual(max(len(item["step_hypotheses"]) for item in candidates), 8)
        for candidate in candidates:
            transitions = [
                (step["source_surface_id"], step["action_id"], tuple(step["expected_target_surface_ids"]))
                for step in candidate["step_hypotheses"]
            ]
            self.assertEqual(len(transitions), len(set(transitions)))

    def test_depth_rejects_bool_and_out_of_range(self):
        with self.assertRaises(TypeError):
            discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=True)
        for value in (0, 33):
            with self.assertRaises(ValueError):
                discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=value)

    def test_inferred_goal_candidate_remains_hypothesis(self):
        candidates = discover_ux_journeys(self.product_model(), self.goal_graph(inferred=True))
        self.assertTrue(candidates)
        self.assertTrue(all(item["status"] == "hypothesis" for item in candidates))
        self.assertTrue(all(item["origin_summary"]["goal_origin"] == "inferred" for item in candidates))

    def test_query_is_bounded_sorted_and_defensive(self):
        candidates = discover_ux_journeys(self.product_model(), self.goal_graph())
        queried = query_ux_journey_candidates(candidates, goal_node_id="goal:submit-order", limit=10)
        self.assertEqual(queried, sorted(queried, key=lambda item: (-item["discovery_score"], item["candidate_id"])))
        before = copy.deepcopy(candidates)
        queried[0]["title"] = "mutated"
        self.assertEqual(candidates, before)
        with self.assertRaises(TypeError):
            query_ux_journey_candidates(candidates, limit=True)


if __name__ == "__main__":
    unittest.main()
