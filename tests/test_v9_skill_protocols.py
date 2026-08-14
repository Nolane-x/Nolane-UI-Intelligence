import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V9SkillProtocolTests(unittest.TestCase):
    def assert_anchors(self, skill, anchors):
        text = (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8").lower()
        for anchor in anchors:
            self.assertIn(anchor.lower(), text, f"{skill} missing V9 anchor: {anchor}")

    def test_product_scope_is_discovered_before_compression(self):
        self.assert_anchors("modeling-product-intent", [
            "V9 Product Envelope Discovery", "broad-before-narrow", "scope adequacy challenge"
        ])
        self.assert_anchors("inventorying-product-capabilities", [
            "V9 Expected-Capability Disposition", "REQUIRED", "EXPECTED", "OPTIONAL", "EXCLUDED", "UNKNOWN"
        ])

    def test_settings_and_account_are_not_one_generic_item(self):
        self.assert_anchors("architecting-information", [
            "V9 Settings Architecture", "scope precedence", "settings search", "recovery/reset"
        ])
        self.assert_anchors("designing-authentication-and-passkeys", [
            "V9 Account Continuity Boundary", "account/workspace lifecycle", "session/device continuity"
        ])

    def test_taste_and_rendered_critique_are_explicit(self):
        self.assert_anchors("exploring-aesthetic-directions", [
            "V9 Comparative Taste Discrimination", "premium", "editorial", "cheap-looking"
        ])
        self.assert_anchors("critiquing-visual-design", [
            "V9 Rendered Design-Director Court", "screenshot", "A/B", "focal hierarchy", "visual rhythm"
        ])
        self.assert_anchors("verifying-design-fidelity", [
            "V9 Design-to-Render Fidelity", "default chrome", "scrollbar", "visual regression"
        ])

    def test_domain_audience_professional_workspace_and_motion_are_deepened(self):
        self.assert_anchors("modeling-users-and-tasks", [
            "V9 Audience Strategy Sensitivity", "trust-first", "delight-first"
        ])
        self.assert_anchors("designing-editor-canvas-workspaces", [
            "V9 Instrument Architecture", "context inspector", "asset/resource"
        ])
        self.assert_anchors("designing-desktop-windowed-workspaces", [
            "V9 Professional Workspace Completeness", "secondary panels", "status surface"
        ])
        self.assert_anchors("designing-motion", [
            "V9 Motion Direction", "emotional cadence", "intentional absence", "reduced motion equivalence"
        ])
        self.assert_anchors("engineering-rich-interactive-components", [
            "V9 Motion Implementation Fidelity", "semantic motion", "performance degradation"
        ])

    def test_router_activates_v9_planes(self):
        self.assert_anchors("routing-ui-work", [
            "V9 Product Completeness and Taste Routing", "capability envelope", "rendered critique", "interface residue"
        ])


if __name__ == "__main__":
    unittest.main()
