import unittest
from pathlib import Path

from nolane_ui.interop import SUPPORTED_AGENT_IDS, build_agent_install_plan
from nolane_ui.runtime_v11.hooks import build_hook_capability


ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11HookTests(unittest.TestCase):
    def test_every_supported_agent_uses_same_canonical_detector(self):
        for agent_id in SUPPORTED_AGENT_IDS:
            with self.subTest(agent_id=agent_id):
                capability = build_hook_capability(agent_id)
                self.assertEqual(capability["detector_command"], "python scripts/nui-detect")
                self.assertEqual(capability["authority"], "evidence-only")
                self.assertFalse(capability["permission_escalation"])

    def test_cursor_can_preflight_and_block_but_does_not_claim_stop(self):
        capability = build_hook_capability("cursor-compatible")
        self.assertTrue(capability["events"]["pre_write"])
        self.assertTrue(capability["can_block_write"])
        self.assertFalse(capability["events"]["session_stop"])

    def test_codex_and_claude_are_post_write_stop_advisors_not_blockers(self):
        for agent_id in ("openai-codex", "claude-code"):
            with self.subTest(agent_id=agent_id):
                capability = build_hook_capability(agent_id)
                self.assertFalse(capability["events"]["pre_write"])
                self.assertTrue(capability["events"]["post_write"])
                self.assertTrue(capability["events"]["session_stop"])
                self.assertFalse(capability["can_block_write"])
                self.assertTrue(capability["returns_findings_to_agent"])

    def test_unknown_or_generic_hosts_do_not_invent_native_hooks(self):
        for agent_id in ("generic-cli", "generic-mcp", "gemini-cli", "opencode"):
            with self.subTest(agent_id=agent_id):
                capability = build_hook_capability(agent_id)
                self.assertEqual(capability["integration"], "manual")
                self.assertFalse(any(capability["events"].values()))
                self.assertFalse(capability["can_block_write"])

    def test_agent_install_plan_exposes_runtime_detection_without_new_authority(self):
        for agent_id in SUPPORTED_AGENT_IDS:
            with self.subTest(agent_id=agent_id):
                plan = build_agent_install_plan(agent_id, ROOT)
                runtime = plan["runtime_detection"]
                self.assertEqual(runtime["command"], "python scripts/nui-detect")
                self.assertEqual(runtime["claim_boundary"], "evidence-only")
                self.assertEqual(runtime["hook_capabilities"], build_hook_capability(agent_id))
                self.assertIn("scripts/nui-detect", runtime["project_files"])


if __name__ == "__main__":
    unittest.main()
