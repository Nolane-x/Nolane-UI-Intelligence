import copy
import unittest

from nolane_ui.ux_intelligence.regression import compare_ux_snapshots
from nolane_ui.ux_intelligence.temporal_evidence import create_ux_evidence_snapshot


class UXRegressionV3Tests(unittest.TestCase):
    def journey(self):
        return {
            "journey_id": "uxj:checkout",
            "title": "Checkout",
            "user_goal": "Submit an order",
            "entry_state": {"route": "/cart", "object_id": "cart-42"},
            "steps": ({
                "step_id": "step-1",
                "intent": "Checkout",
                "action": "checkout",
                "expected_transition": {"route": "/confirmation"},
                "required_context": ("object_id",),
                "preserved_context": ("object_id",),
                "allowed_detours": (),
                "recovery_expectation": "return-to-cart",
                "evidence_requirements": ("object_id", "route"),
            },),
            "success_criteria": ("order-submitted",),
            "critical_state": ("checkout",),
            "provenance_ids": ("uxp.product-journey-contract",),
            "status": "experimental",
        }

    def finding(self, *, rule_id="ux.task.same-goal-navigation-preserves-context", enforcement="block"):
        return {
            "finding_id": f"uxf:uxj:checkout:step-1:{rule_id}",
            "journey_id": "uxj:checkout",
            "step_id": "step-1",
            "rule_id": rule_id,
            "mechanism_id": "context-loss",
            "summary": "Context failure",
            "observed": {"object_id": "cart-9"},
            "expected": {"object_id": "cart-42"},
            "evidence_refs": ("capture:A",),
            "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
            "severity": "major",
            "enforcement": enforcement,
            "verification_mode": "runtime-observation",
        }

    def verification(self, status="passed", findings=(), gaps=()):
        return {
            "journey_id": "uxj:checkout",
            "status": status,
            "step_results": (),
            "findings": tuple(findings),
            "evidence_gaps": tuple(gaps),
            "success_criteria_results": ({"criterion": "order-submitted", "status": "pass" if status == "passed" else "insufficient-evidence", "observed": True if status == "passed" else None},),
            "provenance_ids": ("uxp.product-journey-contract", "uxp.v11-runtime-observation"),
            "runtime_evidence": None,
        }

    def snapshot(self, *, product_id="shop", revision="r1", status="passed", findings=(), gaps=()):
        return create_ux_evidence_snapshot(product_id, revision, self.journey(), self.verification(status, findings, gaps), created_from=f"ci:{revision}")

    def test_cross_product_comparison_is_rejected(self):
        with self.assertRaises(ValueError):
            compare_ux_snapshots(self.snapshot(product_id="shop"), self.snapshot(product_id="mail"))

    def test_pass_to_missing_evidence_is_not_proven_failure(self):
        result = compare_ux_snapshots(
            self.snapshot(revision="a", status="passed"),
            self.snapshot(revision="b", status="insufficient-evidence", gaps=({"field": "route"},)),
        )
        self.assertEqual(result["status"], "insufficient-evidence")
        regression = next(r for r in result["regressions"] if r["class"] == "journey-pass-to-insufficient-evidence")
        self.assertFalse(regression["proven_failure"])

    def test_new_context_finding_maps_to_specific_regression_without_authority_escalation(self):
        finding = self.finding()
        before = copy.deepcopy(finding)
        result = compare_ux_snapshots(
            self.snapshot(revision="a", status="passed"),
            self.snapshot(revision="b", status="failed", findings=(finding,)),
        )
        regression = next(r for r in result["regressions"] if r["class"] == "preserved-context-regressed")
        self.assertEqual(regression["enforcement"], "block")
        self.assertEqual(regression["rule_id"], "ux.task.same-goal-navigation-preserves-context")
        self.assertTrue(regression["proven_failure"])
        self.assertEqual(finding, before)

    def test_reintroduced_requires_history(self):
        failure = self.finding(rule_id="ux.comprehension.no-false-completion", enforcement="warn")
        result = compare_ux_snapshots(
            self.snapshot(revision="b", status="passed"),
            self.snapshot(revision="c", status="failed", findings=(failure,)),
            history=(self.snapshot(revision="a", status="failed", findings=(failure,)),),
        )
        regression = next(r for r in result["regressions"] if r["class"] == "reintroduced-rule-finding")
        self.assertEqual(regression["enforcement"], "warn")

    def test_same_existing_finding_is_not_new_regression(self):
        finding = self.finding()
        result = compare_ux_snapshots(
            self.snapshot(revision="a", status="failed", findings=(finding,)),
            self.snapshot(revision="b", status="failed", findings=(finding,)),
        )
        self.assertEqual(result["status"], "no-regression")
        self.assertEqual(result["regressions"], ())


if __name__ == "__main__":
    unittest.main()
