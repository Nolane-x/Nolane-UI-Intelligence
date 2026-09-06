import copy
import unittest

from nolane_ui.ux_intelligence.temporal_evidence import (
    create_ux_evidence_snapshot,
    ux_semantic_fingerprint,
    validate_ux_evidence_snapshot,
)


class UXTemporalV3Tests(unittest.TestCase):
    def journey(self):
        return {
            "journey_id": "uxj:checkout",
            "title": "Checkout",
            "user_goal": "Submit an order",
            "entry_state": {"route": "/cart", "object_id": "cart-42"},
            "steps": (
                {
                    "step_id": "step-1",
                    "intent": "Checkout",
                    "action": "checkout",
                    "expected_transition": {"route": "/confirmation"},
                    "required_context": ("object_id",),
                    "preserved_context": ("object_id",),
                    "allowed_detours": (),
                    "recovery_expectation": "return-to-cart",
                    "evidence_requirements": ("object_id", "route"),
                },
            ),
            "success_criteria": ("order-submitted",),
            "critical_state": ("checkout",),
            "provenance_ids": ("uxp.product-journey-contract",),
            "status": "experimental",
        }

    def finding(self, *, evidence_refs=("capture:A",), expected=None):
        return {
            "finding_id": "uxf:uxj:checkout:step-1:ux.task.same-goal-navigation-preserves-context",
            "journey_id": "uxj:checkout",
            "step_id": "step-1",
            "rule_id": "ux.task.same-goal-navigation-preserves-context",
            "mechanism_id": "context-loss",
            "summary": "Context is not preserved",
            "observed": {"object_id": "cart-9"},
            "expected": expected or {"object_id": "cart-42"},
            "evidence_refs": evidence_refs,
            "provenance_ids": ("uxp.rule-authority-inheritance", "uxp.v11-runtime-observation"),
            "severity": "major",
            "enforcement": "block",
            "verification_mode": "runtime-observation",
        }

    def verification(self, *, evidence_refs=("capture:A",)):
        return {
            "journey_id": "uxj:checkout",
            "status": "failed",
            "step_results": ({"step_id": "step-1", "status": "fail", "contract_failures": (), "finding_ids": (self.finding()["finding_id"],), "evaluator_results": ()},),
            "findings": (self.finding(evidence_refs=evidence_refs),),
            "evidence_gaps": (),
            "success_criteria_results": ({"criterion": "order-submitted", "status": "pass", "observed": True},),
            "provenance_ids": ("uxp.product-journey-contract", "uxp.v11-runtime-observation"),
            "runtime_evidence": {"capture_ref": evidence_refs[0], "timestamp": "2026-09-06T10:00:00Z"},
        }

    def test_fingerprint_ignores_transient_evidence_refs_but_not_semantics(self):
        a = self.finding(evidence_refs=("capture:A",))
        b = self.finding(evidence_refs=("capture:B",))
        self.assertEqual(ux_semantic_fingerprint(a), ux_semantic_fingerprint(b))
        b["expected"] = {"object_id": "cart-2"}
        self.assertNotEqual(ux_semantic_fingerprint(a), ux_semantic_fingerprint(b))

    def test_snapshot_creation_does_not_mutate_verification_input(self):
        verification = self.verification()
        before = copy.deepcopy(verification)
        create_ux_evidence_snapshot("shop", "rev-a", self.journey(), verification, created_from="ci:1")
        self.assertEqual(verification, before)

    def test_same_semantics_same_fingerprint_across_revisions_and_capture_refs(self):
        a = create_ux_evidence_snapshot("shop", "rev-a", self.journey(), self.verification(evidence_refs=("capture:A",)), created_from="ci:1")
        b = create_ux_evidence_snapshot("shop", "rev-b", self.journey(), self.verification(evidence_refs=("capture:B",)), created_from="ci:2")
        self.assertEqual(a["journey_fingerprint"], b["journey_fingerprint"])
        self.assertEqual(a["finding_fingerprints"], b["finding_fingerprints"])
        self.assertEqual(a["verification_fingerprint"], b["verification_fingerprint"])

    def test_snapshot_validation_rejects_identity_mismatch(self):
        snapshot = create_ux_evidence_snapshot("shop", "rev-a", self.journey(), self.verification(), created_from="ci:1")
        snapshot["journey_id"] = "uxj:other"
        with self.assertRaises(ValueError):
            validate_ux_evidence_snapshot(snapshot)

    def test_semantic_change_changes_verification_fingerprint(self):
        a = create_ux_evidence_snapshot("shop", "rev-a", self.journey(), self.verification(), created_from="ci:1")
        changed = self.verification()
        changed["findings"][0]["expected"] = {"object_id": "cart-2"}
        b = create_ux_evidence_snapshot("shop", "rev-b", self.journey(), changed, created_from="ci:2")
        self.assertNotEqual(a["verification_fingerprint"], b["verification_fingerprint"])


if __name__ == "__main__":
    unittest.main()
