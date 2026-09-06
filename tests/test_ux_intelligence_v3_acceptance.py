import copy
import unittest

from nolane_ui import (
    build_ux_goal_graph,
    build_ux_product_model,
    compare_ux_snapshots,
    create_ux_evidence_snapshot,
    discover_ux_journeys,
    plan_ux_discovery,
    promote_ux_journey_candidate,
    rank_ux_impacts,
    verify_ux_journey,
)


class UXV3AcceptanceTests(unittest.TestCase):
    def packet(self):
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
                            "commitment_level": "external-effect",
                            "target_surface_ids": ["confirmation"],
                            "state_changes": {"submitted": True},
                            "evidence_refs": ["runtime:checkout"],
                        }
                    ],
                    "transition_evidence": [
                        {
                            "transition_id": "cart-to-confirmation",
                            "source_id": "cart",
                            "relation": "navigates-to",
                            "target_id": "confirmation",
                            "evidence_refs": ["runtime:route-confirmation"],
                        },
                        {
                            "transition_id": "checkout-preserves-cart",
                            "source_id": "checkout",
                            "relation": "preserves",
                            "target_id": "cart-42",
                            "evidence_refs": ["contract:preserve-cart-id"],
                        },
                        {
                            "transition_id": "checkout-recovers-cart",
                            "source_id": "checkout",
                            "relation": "recovers-via",
                            "target_id": "cart",
                            "evidence_refs": ["contract:return-to-cart"],
                        },
                    ],
                    "object_evidence": [
                        {
                            "object_id": "cart-42",
                            "object_type": "cart",
                            "labels": ["Current cart"],
                            "identity_fields": ["object_id"],
                            "state_ids": ["cart-open"],
                            "evidence_refs": ["runtime:cart-id"],
                        }
                    ],
                    "state_evidence": [
                        {
                            "state_id": "cart-open",
                            "object_id": "cart-42",
                            "attributes": {"object_id": "cart-42", "submitted": False},
                            "evidence_refs": ["runtime:cart-state"],
                        }
                    ],
                    "success_evidence": [],
                    "evidence_refs": ["capture:cart"],
                },
                {
                    "capture_id": "confirmation-capture",
                    "surface_id": "confirmation",
                    "surface_kind": "route",
                    "surface_locator": "/confirmation",
                    "surface_labels": ["Confirmation"],
                    "action_evidence": [],
                    "transition_evidence": [],
                    "object_evidence": [],
                    "state_evidence": [],
                    "success_evidence": [
                        {
                            "outcome_id": "order-submitted",
                            "label": "Order submitted",
                            "surface_id": "confirmation",
                            "evidence_refs": ["runtime:success"],
                        }
                    ],
                    "evidence_refs": ["capture:confirmation"],
                },
            ],
            "declared_goals": [],
            "declared_success_signals": [],
            "declared_object_hints": [],
            "provenance_ids": ["uxp.v11-runtime-observation"],
        }

    def declared_goal(self):
        return {
            "goal_id": "submit-order",
            "label": "Submit an order",
            "description": "Submit the current cart and reach confirmation",
            "task_ids": ["checkout-cart"],
            "outcome_ids": ["order-submitted"],
            "provenance_ids": ["uxp.product-journey-contract"],
        }

    def inferred_goal(self):
        return {
            "goal_id": "checkout",
            "label": "Checkout",
            "description": "Inferred from navigation structure only",
            "task_ids": [],
            "outcome_ids": ["order-submitted"],
            "evidence_refs": ["runtime:path:/confirmation"],
            "confidence": 0.8,
        }

    def pipeline(self):
        model = build_ux_product_model(self.packet())
        graph = build_ux_goal_graph(model, declared_goals=[self.declared_goal()])
        candidate = discover_ux_journeys(model, graph)[0]
        promoted = promote_ux_journey_candidate(candidate, model, graph)
        return model, graph, candidate, promoted

    def passing_observations(self, journey):
        step = journey["steps"][0]
        return {
            "steps": {
                step["step_id"]: {
                    "route": "/confirmation",
                    "object_id": "cart-42",
                    "_evidence_refs": {
                        "route": "runtime:route-confirmation",
                        "object_id": "runtime:cart-id-after",
                    },
                }
            },
            "success": {"order-submitted": True},
        }

    def test_declared_goal_observed_path_promotes_and_verifies(self):
        _, _, _, promoted = self.pipeline()
        self.assertEqual(promoted["status"], "promoted")
        report = verify_ux_journey(promoted["journey"], self.passing_observations(promoted["journey"]))
        self.assertEqual(report["status"], "passed")

    def test_inferred_goal_stays_non_authoritative(self):
        model = build_ux_product_model(self.packet())
        graph = build_ux_goal_graph(model, inferred_goals=[self.inferred_goal()])
        candidate = discover_ux_journeys(model, graph)[0]
        promoted = promote_ux_journey_candidate(candidate, model, graph)
        self.assertEqual(promoted["status"], "promotion-gaps")
        self.assertIn("goal-not-declared", {gap["code"] for gap in promoted["promotion_gaps"]})

    def test_relationship_evidence_survives_discovery_for_context_and_recovery(self):
        _, _, candidate, _ = self.pipeline()
        step = candidate["step_hypotheses"][0]
        self.assertIn("object_id", step["preserved_context_hypotheses"])
        self.assertTrue(step["recovery_hypotheses"])
        self.assertIn("contract:preserve-cart-id", step["evidence_refs"])
        self.assertIn("contract:return-to-cart", step["evidence_refs"])
        self.assertEqual(candidate["entry_state"]["object_id"], "cart-42")

    def test_duplicate_semantic_actions_with_different_ids_collapse(self):
        model = build_ux_product_model(self.packet())
        alias = copy.deepcopy(next(item for item in model["actions"] if item["action_id"] == "checkout"))
        alias["action_id"] = "checkout-alias"
        alias["evidence_refs"] = ("runtime:checkout-alias",)
        model["actions"] = tuple(sorted(model["actions"] + (alias,), key=lambda item: item["action_id"]))
        surfaces = []
        for surface in model["surfaces"]:
            item = copy.deepcopy(surface)
            if item["surface_id"] == "cart":
                item["available_action_ids"] = tuple(sorted(set(item["available_action_ids"]) | {"checkout-alias"}))
            surfaces.append(item)
        model["surfaces"] = tuple(surfaces)
        graph = build_ux_goal_graph(model, declared_goals=[self.declared_goal()])
        candidates = discover_ux_journeys(model, graph)
        self.assertEqual(len(candidates), 1)

    def test_label_only_success_cannot_be_promoted_to_outcome_truth(self):
        packet = self.packet()
        packet["captures"][1]["success_evidence"] = []
        model = build_ux_product_model(packet)
        with self.assertRaises(ValueError):
            build_ux_goal_graph(model, declared_goals=[self.declared_goal()])

    def test_missing_object_identity_is_rejected_before_discovery(self):
        packet = self.packet()
        packet["captures"][0]["object_evidence"] = []
        packet["captures"][0]["state_evidence"] = []
        with self.assertRaises(ValueError):
            build_ux_product_model(packet)

    def test_context_regression_inherits_existing_v2_rule_authority(self):
        _, _, _, promoted = self.pipeline()
        journey = promoted["journey"]
        baseline_report = verify_ux_journey(journey, self.passing_observations(journey))
        failing = self.passing_observations(journey)
        failing["steps"][journey["steps"][0]["step_id"]]["object_id"] = "cart-other"
        candidate_report = verify_ux_journey(journey, failing)
        baseline = create_ux_evidence_snapshot("shop", "r1", journey, baseline_report, created_from="ci:base")
        candidate = create_ux_evidence_snapshot("shop", "r2", journey, candidate_report, created_from="ci:candidate")
        comparison = compare_ux_snapshots(baseline, candidate)
        regression = next(item for item in comparison["regressions"] if item["class"] == "preserved-context-regressed")
        self.assertEqual(regression["rule_id"], "ux.task.same-goal-navigation-preserves-context")
        source = next(item for item in candidate_report["findings"] if item["rule_id"] == regression["rule_id"])
        self.assertEqual(regression["enforcement"], source["enforcement"])
        self.assertEqual(regression["severity"], source["severity"])

    def test_evidence_loss_is_not_proven_failure(self):
        _, _, _, promoted = self.pipeline()
        journey = promoted["journey"]
        baseline_report = verify_ux_journey(journey, self.passing_observations(journey))
        missing_report = verify_ux_journey(journey, {"steps": {}, "success": {}})
        baseline = create_ux_evidence_snapshot("shop", "r1", journey, baseline_report, created_from="ci:base")
        candidate = create_ux_evidence_snapshot("shop", "r2", journey, missing_report, created_from="ci:candidate")
        comparison = compare_ux_snapshots(baseline, candidate)
        self.assertEqual(comparison["status"], "insufficient-evidence")
        self.assertFalse(any(item["proven_failure"] for item in comparison["regressions"]))

    def test_p0_warning_stays_warn(self):
        finding = {
            "finding_id": "uxf:warning",
            "rule_id": "ux.example.warning",
            "severity": "major",
            "enforcement": "warn",
        }
        evidence = {
            "uxf:warning": {
                "goal_criticality": {"value": 1.0, "origin": "declared", "evidence_refs": ("contract:goal",)},
                "task_frequency": {"value": 1.0, "origin": "observed", "evidence_refs": ("analytics:freq",)},
                "completion_blockage": {"value": 1.0, "origin": "observed", "evidence_refs": ("runtime:block",)},
                "recoverability_cost": {"value": 1.0, "origin": "observed", "evidence_refs": ("runtime:recovery",)},
                "affected_scope": {"value": 1.0, "origin": "declared", "evidence_refs": ("contract:scope",)},
                "regression_confidence": {"value": 1.0, "origin": "observed", "evidence_refs": ("compare:1",)},
                "evidence_completeness": {"value": 1.0, "origin": "observed", "evidence_refs": ("evidence:full",)},
            }
        }
        before = copy.deepcopy(finding)
        assessment = rank_ux_impacts([finding], evidence)[0]
        self.assertEqual(assessment["priority_band"], "p0")
        self.assertEqual(assessment["source_enforcement"], "warn")
        self.assertEqual(finding, before)

    def test_planner_request_does_not_claim_execution_or_observation(self):
        _, _, candidate, _ = self.pipeline()
        requests = plan_ux_discovery(candidate, ["browser-runtime", "interaction"])
        self.assertTrue(requests)
        for request in requests:
            self.assertEqual(request["claim_boundary"], "evidence-request-only")
            self.assertNotIn("executed", request)
            self.assertNotIn("observed", request)
            self.assertNotIn("success", request)

    def test_cross_product_snapshot_comparison_is_rejected(self):
        _, _, _, promoted = self.pipeline()
        journey = promoted["journey"]
        report = verify_ux_journey(journey, self.passing_observations(journey))
        shop = create_ux_evidence_snapshot("shop", "r1", journey, report, created_from="ci:shop")
        mail = create_ux_evidence_snapshot("mail", "r2", journey, report, created_from="ci:mail")
        with self.assertRaises(ValueError):
            compare_ux_snapshots(shop, mail)

    def test_impact_evidence_cannot_smuggle_enforcement_override(self):
        finding = {"finding_id": "uxf:x", "rule_id": "ux.x", "severity": "major", "enforcement": "warn"}
        evidence = {
            "uxf:x": {
                "goal_criticality": {"value": 1.0, "origin": "declared", "evidence_refs": ("contract:goal",)},
                "completion_blockage": {"value": 1.0, "origin": "observed", "evidence_refs": ("runtime:block",)},
                "regression_confidence": {"value": 1.0, "origin": "observed", "evidence_refs": ("compare:1",)},
                "evidence_completeness": {"value": 1.0, "origin": "observed", "evidence_refs": ("evidence:full",)},
                "enforcement": {"value": 1.0, "origin": "declared", "evidence_refs": ("attack:block",)},
            }
        }
        with self.assertRaises(ValueError):
            rank_ux_impacts([finding], evidence)


if __name__ == "__main__":
    unittest.main()
