import unittest

from nolane_ui.validators import validate_v9_completion_evidence


class V9CompletionTests(unittest.TestCase):
    def test_full_platform_claim_requires_scope_evidence(self):
        result = validate_v9_completion_evidence({"product_ambition": "full-platform"})
        self.assertEqual(result["decision"], "BLOCKED")
        text = " ".join(result["errors"]).lower()
        self.assertIn("capability envelope", text)
        self.assertIn("scope adequacy", text)

    def test_material_settings_require_settings_architecture(self):
        result = validate_v9_completion_evidence({"settings_material": True})
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertTrue(any("settings architecture" in e.lower() for e in result["errors"]))

    def test_material_account_workspace_requires_full_lifecycle(self):
        result = validate_v9_completion_evidence({"account_workspace_material": True})
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertTrue(any("account/workspace lifecycle" in e.lower() for e in result["errors"]))

    def test_exceptional_visual_claim_requires_v9_perceptual_chain(self):
        result = validate_v9_completion_evidence({"visual_ambition": "exceptional"})
        self.assertEqual(result["decision"], "BLOCKED")
        text = " ".join(result["errors"]).lower()
        # V8 flagship evidence remains mandatory, while V9 adds discrimination,
        # real-render critique, audience/domain fit and implementation fidelity.
        self.assertIn("flagship visual synthesis", text)
        self.assertIn("taste comparison", text)
        self.assertIn("render critique", text)
        self.assertIn("domain/audience fit", text)
        self.assertIn("render fidelity", text)

    def test_rendered_product_claim_requires_residue_audit(self):
        result = validate_v9_completion_evidence({"material_rendered_ui": True})
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertTrue(any("interface residue audit" in e.lower() for e in result["errors"]))

    def test_scope_adequacy_cannot_self_certify_without_challenge(self):
        result = validate_v9_completion_evidence({
            "product_ambition": "full-platform",
            "capability_envelope": {
                "product_class": "commerce-admin",
                "ambition": "full-platform",
                "actors": ["owner"],
                "expected_capability_families": [
                    "identity", "catalog", "orders", "customers", "payments", "settings"
                ],
                "capabilities": [
                    {"id": name, "family": name, "disposition": "EXPECTED", "evidence": "domain discovery"}
                    for name in ["identity", "catalog", "orders", "customers", "payments", "settings"]
                ],
                "coverage": ["identity", "catalog", "orders", "customers", "payments", "settings"],
            },
            "scope_adequacy": {"status": "PASS"},
        })
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertTrue(any("challenge" in e.lower() or "falsif" in e.lower() for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
