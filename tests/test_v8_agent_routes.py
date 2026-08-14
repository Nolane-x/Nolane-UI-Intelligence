import json
import unittest
from pathlib import Path

from nolane_ui.interop import build_agent_install_plan, validate_agent_interop_registry
from nolane_ui.media import mandatory_v8_routes

ROOT = Path(__file__).resolve().parents[1]


class V8AgentRouteTests(unittest.TestCase):
    def test_registry_is_valid(self):
        data = json.loads((ROOT / "knowledge/agent-interop-v8.json").read_text())
        self.assertTrue(validate_agent_interop_registry(data)["valid"])

    def test_registry_has_nine_adapters(self):
        data = json.loads((ROOT / "knowledge/agent-interop-v8.json").read_text())
        self.assertEqual(validate_agent_interop_registry(data)["adapter_count"], 9)

    def test_codex_plan_points_to_canonical_bridge(self):
        plan = build_agent_install_plan("openai-codex", ROOT)
        self.assertIn(".agents/skills/nolane-ui/SKILL.md", plan["project_files"])
        self.assertEqual(plan["canonical_skill"], "skills/using-nolane-ui/SKILL.md")

    def test_unknown_host_is_not_guessed(self):
        with self.assertRaises(ValueError):
            build_agent_install_plan("unknown-host", ROOT)

    def test_subject_native_media_routes_media_owners(self):
        routes = mandatory_v8_routes({"subject_native_media": True})
        self.assertIn("mapping-visual-media-opportunities", routes)
        self.assertIn("replacing-shape-substitution", routes)

    def test_custom_media_routes_authoring(self):
        routes = mandatory_v8_routes({"custom_visual_asset": True})
        self.assertIn("authoring-domain-native-visual-assets", routes)
        self.assertIn("orchestrating-creative-toolchains", routes)

    def test_agent_harness_routes_export_owner(self):
        routes = mandatory_v8_routes({"agent_harness": True})
        self.assertIn("exporting-nui-to-agent-harnesses", routes)


if __name__ == "__main__":
    unittest.main()
