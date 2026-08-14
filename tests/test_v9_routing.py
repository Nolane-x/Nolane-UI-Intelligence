import unittest

from nolane_ui.validators import mandatory_routes_for_profile


class V9RoutingTests(unittest.TestCase):
    def test_full_platform_routes_product_envelope_and_independent_completion_court(self):
        routes = mandatory_routes_for_profile({"product_ambition": "full-platform"})
        self.assertTrue({
            "modeling-product-intent",
            "inventorying-product-capabilities",
            "covering-product-scenarios",
            "critiquing-functional-completeness",
        }.issubset(routes))

    def test_material_settings_route_structure_not_just_theme(self):
        routes = mandatory_routes_for_profile({"settings_material": True})
        self.assertTrue({"architecting-information", "inventorying-product-capabilities"}.issubset(routes))

    def test_account_workspace_routes_auth_and_product_capabilities(self):
        routes = mandatory_routes_for_profile({"account_workspace_material": True})
        self.assertTrue({"designing-authentication-and-passkeys", "inventorying-product-capabilities"}.issubset(routes))

    def test_professional_editor_routes_workspace_instruments_and_power_input(self):
        routes = mandatory_routes_for_profile({"professional_editor": True, "platform_surfaces": ["desktop"]})
        self.assertTrue({
            "designing-editor-canvas-workspaces",
            "designing-desktop-windowed-workspaces",
            "designing-keyboard-power-user-ux",
        }.issubset(routes))

    def test_exceptional_visual_routes_taste_render_and_audience_planes(self):
        routes = mandatory_routes_for_profile({"visual_ambition": "exceptional", "material_rendered_ui": True})
        self.assertTrue({
            "exploring-aesthetic-directions",
            "modeling-users-and-tasks",
            "critiquing-visual-design",
            "verifying-design-fidelity",
            "adapting-platform-conventions",
        }.issubset(routes))

    def test_material_motion_routes_direction_and_engineering(self):
        routes = mandatory_routes_for_profile({"motion_material": True, "rich_interaction": True})
        self.assertTrue({"designing-motion", "engineering-rich-interactive-components"}.issubset(routes))


if __name__ == "__main__":
    unittest.main()
