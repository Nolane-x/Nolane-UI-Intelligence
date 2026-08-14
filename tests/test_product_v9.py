import unittest

from nolane_ui.product_v9 import (
    validate_account_workspace_lifecycle,
    validate_capability_envelope,
    validate_domain_audience_fit,
    validate_interface_residue_audit,
    validate_render_critique,
    validate_render_fidelity,
    validate_settings_architecture,
    validate_taste_comparison,
    validate_v9_product_system,
)


class ProductV9Tests(unittest.TestCase):
    def test_complete_sales_platform_rejects_tiny_envelope(self):
        record = {
            "product_class": "sales-management-platform",
            "ambition": "full-platform",
            "actors": ["owner", "staff"],
            "capabilities": [
                {"id": "dashboard", "disposition": "REQUIRED", "evidence": "brief"},
                {"id": "products", "disposition": "REQUIRED", "evidence": "brief"},
                {"id": "orders", "disposition": "REQUIRED", "evidence": "brief"},
            ],
            "expected_capability_families": [
                "identity-account", "workspace-organization", "catalog", "inventory",
                "orders-fulfillment", "customers", "payments-refunds", "reporting",
                "search", "notifications", "import-export", "integrations", "settings",
                "roles-permissions", "audit-history", "help-recovery",
            ],
            "coverage": ["catalog", "orders-fulfillment"],
        }
        result = validate_capability_envelope(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("undispositioned" in e or "coverage" in e for e in result["errors"]))

    def test_expected_capability_requires_disposition(self):
        result = validate_capability_envelope({
            "product_class": "commerce-admin",
            "ambition": "production",
            "actors": ["owner"],
            "expected_capability_families": ["catalog", "settings"],
            "capabilities": [
                {"id": "catalog", "family": "catalog", "disposition": "REQUIRED", "evidence": "brief"},
                {"id": "settings", "family": "settings", "evidence": "domain expectation"},
            ],
            "coverage": ["catalog", "settings"],
        })
        self.assertFalse(result["valid"])
        self.assertTrue(any("disposition" in e for e in result["errors"]))

    def test_settings_architecture_requires_scope_and_recovery(self):
        result = validate_settings_architecture({
            "settings": [{"id": "theme", "scope": "user"}],
            "scopes": ["user"],
            "search": False,
        })
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("inherit", joined)
        self.assertIn("recovery", joined)

    def test_account_lifecycle_goes_beyond_login(self):
        result = validate_account_workspace_lifecycle({
            "states": ["sign-up", "sign-in", "signed-in"],
            "workspace_model": "organization",
        })
        self.assertFalse(result["valid"])
        self.assertTrue(any("membership" in e or "recovery" in e or "deactivation" in e for e in result["errors"]))

    def test_default_scrollbar_requires_intentional_treatment(self):
        result = validate_interface_residue_audit({
            "surfaces": [{
                "id": "main-scroll",
                "kind": "scrollbar",
                "appearance": "browser-default",
                "intentional": False,
                "platform_fit": "mismatch",
                "operable_alternative": True,
            }]
        })
        self.assertFalse(result["valid"])
        self.assertTrue(any("residue" in e.lower() or "intentional" in e.lower() for e in result["errors"]))

    def test_taste_is_comparative_not_single_score(self):
        result = validate_taste_comparison({
            "candidates": [{"id": "a", "render_ref": "shot-a"}],
            "dimensions": ["hierarchy", "rhythm", "material-coherence"],
            "verdict": "A",
        })
        self.assertFalse(result["valid"])
        self.assertTrue(any("two" in e.lower() or "compar" in e.lower() for e in result["errors"]))

    def test_render_critique_requires_actual_render_evidence(self):
        result = validate_render_critique({
            "render_refs": [],
            "viewports": ["desktop"],
            "observations": [{"dimension": "hierarchy", "finding": "good"}],
            "revision_decisions": ["keep"],
        })
        self.assertFalse(result["valid"])
        self.assertTrue(any("render" in e.lower() for e in result["errors"]))

    def test_domain_audience_fit_requires_both_axes(self):
        result = validate_domain_audience_fit({
            "domain": "fintech",
            "domain_signature": {"trust": "high", "density": "medium"},
        })
        self.assertFalse(result["valid"])
        self.assertTrue(any("audience" in e.lower() for e in result["errors"]))

    def test_render_fidelity_requires_token_component_runtime_chain(self):
        result = validate_render_fidelity({
            "token_contract": {"spacing": True, "type": True},
            "component_constraints": {},
            "runtime_evidence": [],
        })
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("component", joined)
        self.assertIn("runtime", joined)

    def test_v9_product_system_aggregates_independent_gates(self):
        result = validate_v9_product_system({
            "capability_envelope": {},
            "settings_architecture": {},
            "account_workspace_lifecycle": {},
            "interface_residue_audit": {},
            "taste_comparison": {},
            "render_critique": {},
            "domain_audience_fit": {},
            "render_fidelity": {},
        })
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertGreaterEqual(len(result["errors"]), 6)


if __name__ == "__main__":
    unittest.main()
