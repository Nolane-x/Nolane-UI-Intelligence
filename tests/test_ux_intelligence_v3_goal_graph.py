import unittest

from nolane_ui.ux_intelligence.goal_graph import (
    build_ux_goal_graph,
    validate_ux_goal_graph,
)


class UXGoalGraphV3Tests(unittest.TestCase):
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
                    "evidence_refs": ("capture:cart",),
                },
                {
                    "surface_id": "checkout",
                    "kind": "route",
                    "locator": "/checkout",
                    "labels": ("Checkout",),
                    "available_action_ids": (),
                    "visible_object_ids": ("cart-42",),
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("capture:checkout",),
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
                    "observed_target_surface_ids": ("checkout",),
                    "observed_state_changes": {"checkout_started": True},
                    "commitment_level": "state-changing",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("action:checkout",),
                },
            ),
            "states": (
                {
                    "state_id": "cart-open",
                    "object_id": "cart-42",
                    "attributes": {"checkout_started": False},
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("state:cart-open",),
                },
            ),
            "relationships": (
                {
                    "relationship_id": "cart-to-checkout",
                    "source_id": "cart",
                    "relation": "navigates-to",
                    "target_id": "checkout",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("transition:cart-to-checkout",),
                },
            ),
            "outcomes": (
                {
                    "outcome_id": "order-submitted",
                    "label": "Order submitted",
                    "surface_id": "checkout",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ("outcome:order-submitted",),
                },
            ),
            "evidence_refs": ("capture:cart", "capture:checkout"),
            "provenance_ids": ("uxp.v11-runtime-observation",),
            "status": "active",
        }

    def valid_graph(self):
        return {
            "product_id": "shop",
            "revision": "r1",
            "nodes": [
                {
                    "node_id": "action:checkout",
                    "kind": "action",
                    "label": "Checkout",
                    "description": "Product action checkout",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["action:checkout"],
                },
                {
                    "node_id": "goal:submit-order",
                    "kind": "goal",
                    "label": "Submit an order",
                    "description": "Complete checkout for the current cart",
                    "origin": "declared",
                    "confidence": 1.0,
                    "evidence_refs": [],
                },
                {
                    "node_id": "object:cart-42",
                    "kind": "object",
                    "label": "Current cart",
                    "description": "Product object cart",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["object:cart-42"],
                },
                {
                    "node_id": "outcome:order-submitted",
                    "kind": "outcome",
                    "label": "Order submitted",
                    "description": "Observed product outcome",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["outcome:order-submitted"],
                },
                {
                    "node_id": "state:cart-open",
                    "kind": "state",
                    "label": "cart-open",
                    "description": "Observed product state",
                    "origin": "observed",
                    "confidence": 1.0,
                    "evidence_refs": ["state:cart-open"],
                },
                {
                    "node_id": "task:checkout-cart",
                    "kind": "task",
                    "label": "Checkout cart",
                    "description": "Complete checkout for the current cart",
                    "origin": "declared",
                    "confidence": 1.0,
                    "evidence_refs": [],
                },
            ],
            "edges": [
                {
                    "edge_id": "goal:submit-order->task:checkout-cart",
                    "source_id": "goal:submit-order",
                    "relation": "decomposes-to",
                    "target_id": "task:checkout-cart",
                    "origin": "declared",
                    "confidence": 1.0,
                    "evidence_refs": [],
                },
                {
                    "edge_id": "task:checkout-cart->action:checkout",
                    "source_id": "task:checkout-cart",
                    "relation": "acts-on",
                    "target_id": "action:checkout",
                    "origin": "declared",
                    "confidence": 1.0,
                    "evidence_refs": [],
                },
                {
                    "edge_id": "goal:submit-order->outcome:order-submitted",
                    "source_id": "goal:submit-order",
                    "relation": "succeeds-when",
                    "target_id": "outcome:order-submitted",
                    "origin": "declared",
                    "confidence": 1.0,
                    "evidence_refs": [],
                },
            ],
            "evidence_refs": ["action:checkout", "outcome:order-submitted"],
            "provenance_ids": ["uxp.product-journey-contract", "uxp.v11-runtime-observation"],
            "status": "active",
        }

    def test_goal_and_task_cannot_be_observed(self):
        for node_id in ("goal:submit-order", "task:checkout-cart"):
            graph = self.valid_graph()
            node = next(item for item in graph["nodes"] if item["node_id"] == node_id)
            node["origin"] = "observed"
            node["evidence_refs"] = ["runtime:click-path"]
            with self.assertRaises(ValueError):
                validate_ux_goal_graph(graph)

    def test_browser_traversal_does_not_promote_inferred_goal(self):
        graph = build_ux_goal_graph(
            self.product_model(),
            inferred_goals=[
                {
                    "goal_id": "checkout",
                    "label": "Checkout",
                    "description": "Inferred from product structure",
                    "task_ids": [],
                    "outcome_ids": ["order-submitted"],
                    "evidence_refs": ["runtime-v11:url-path:/checkout"],
                    "confidence": 0.8,
                }
            ],
        )
        goal = next(node for node in graph["nodes"] if node["node_id"] == "goal:checkout")
        self.assertEqual(goal["origin"], "inferred")
        self.assertNotEqual(goal["origin"], "declared")

    def test_invalid_self_decomposition_is_rejected(self):
        graph = self.valid_graph()
        graph["edges"].append(
            {
                "edge_id": "bad",
                "source_id": "goal:submit-order",
                "relation": "decomposes-to",
                "target_id": "goal:submit-order",
                "origin": "declared",
                "confidence": 1.0,
                "evidence_refs": [],
            }
        )
        graph["edges"] = sorted(graph["edges"], key=lambda item: item["edge_id"])
        with self.assertRaises(ValueError):
            validate_ux_goal_graph(graph)

    def test_declared_goal_stays_declared_and_connects_outcome(self):
        graph = build_ux_goal_graph(
            self.product_model(),
            declared_goals=[
                {
                    "goal_id": "submit-order",
                    "label": "Submit an order",
                    "description": "Complete checkout for the current cart",
                    "task_ids": ["checkout-cart"],
                    "outcome_ids": ["order-submitted"],
                    "provenance_ids": ["uxp.product-journey-contract"],
                }
            ],
        )
        self.assertTrue(validate_ux_goal_graph(graph)["valid"])
        goal = next(node for node in graph["nodes"] if node["node_id"] == "goal:submit-order")
        self.assertEqual(goal["origin"], "declared")
        self.assertIn(
            ("goal:submit-order", "succeeds-when", "outcome:order-submitted"),
            {(edge["source_id"], edge["relation"], edge["target_id"]) for edge in graph["edges"]},
        )


if __name__ == "__main__":
    unittest.main()
