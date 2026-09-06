import unittest

from nolane_ui.ux_intelligence.discovery_planner import plan_ux_discovery


class UXPlannerV3Tests(unittest.TestCase):
    def candidate(self, *, inferred=False):
        return {
            "candidate_id": "uxc:planner-test",
            "goal_node_id": "goal:submit-order",
            "origin_summary": {"goal_origin": "inferred" if inferred else "declared"},
            "entry_state": {"surface_id": "cart", "route": "/cart"},
            "step_hypotheses": (
                {
                    "candidate_step_id": "step-1:checkout",
                    "action_id": "checkout",
                    "source_surface_id": "cart",
                    "expected_target_surface_ids": ("checkout",),
                    "required_context_hypotheses": ("object_id",),
                    "preserved_context_hypotheses": ("object_id",),
                    "recovery_hypotheses": (),
                },
                {
                    "candidate_step_id": "step-2:submit-order",
                    "action_id": "submit-order",
                    "source_surface_id": "checkout",
                    "expected_target_surface_ids": ("confirmation",),
                    "required_context_hypotheses": (),
                    "preserved_context_hypotheses": ("object_id",),
                    "recovery_hypotheses": (),
                },
            ),
            "success_hypotheses": (
                {"outcome_id": "order-submitted", "surface_id": "confirmation"},
            ),
        }

    def test_planner_returns_requests_not_execution_claims(self):
        requests = plan_ux_discovery(self.candidate(), {"browser-runtime", "interaction"})
        self.assertTrue(requests)
        for request in requests:
            self.assertNotIn("executed", request)
            self.assertNotIn("observed", request)
            self.assertNotIn("success", request)
            self.assertIn("required_evidence_fields", request)
            self.assertTrue(request["request_id"].startswith("uxr:"))

    def test_goal_acceptance_is_not_faked_as_runtime_observation(self):
        requests = plan_ux_discovery(self.candidate(inferred=True), {"browser-runtime", "interaction"})
        self.assertNotIn("goal_origin", {field for item in requests for field in item["required_evidence_fields"]})

    def test_capabilities_are_intersected_not_invented(self):
        requests = plan_ux_discovery(self.candidate(), {"browser-runtime"})
        self.assertTrue(requests)
        self.assertTrue(all(set(item["preferred_v11_capabilities"]) <= {"browser-runtime"} for item in requests))

    def test_requests_are_deterministic_and_bounded(self):
        first = plan_ux_discovery(self.candidate(), {"browser-runtime", "interaction"}, limit=2)
        second = plan_ux_discovery(self.candidate(), {"interaction", "browser-runtime"}, limit=2)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 2)

    def test_limit_rejects_bool_and_out_of_range(self):
        with self.assertRaises(TypeError):
            plan_ux_discovery(self.candidate(), {"browser-runtime"}, limit=True)
        for value in (0, 101):
            with self.assertRaises(ValueError):
                plan_ux_discovery(self.candidate(), {"browser-runtime"}, limit=value)


if __name__ == "__main__":
    unittest.main()
