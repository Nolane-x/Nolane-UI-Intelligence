import json
import unittest
from pathlib import Path

from nolane_ui.interop import build_agent_install_plan

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_AGENTS = {
    "openai-codex",
    "claude-code",
    "google-antigravity",
    "gemini-cli",
    "opencode",
    "generic-mcp",
    "generic-cli",
    "cursor-compatible",
    "vscode-agent-compatible",
}


class V10AgentOnboardingTests(unittest.TestCase):
    def test_every_declared_adapter_has_an_executable_export_plan(self):
        registry = json.loads((ROOT / "knowledge/agent-interop-v8.json").read_text(encoding="utf-8"))
        declared = {item["id"] for item in registry["adapters"]}
        self.assertEqual(declared, EXPECTED_AGENTS)
        for agent_id in sorted(declared):
            try:
                plan = build_agent_install_plan(agent_id, ROOT)
            except ValueError as exc:
                self.fail(f"declared adapter {agent_id} has no export plan: {exc}")
            self.assertEqual(plan["agent_id"], agent_id)
            self.assertEqual(plan["canonical_skill"], "skills/using-nolane-ui/SKILL.md")
            self.assertTrue(plan["project_files"], agent_id)
            self.assertIn("command", plan["cli"])
            self.assertIn("permission_boundary", plan)

    def test_export_cli_exposes_every_registry_adapter(self):
        script = (ROOT / "scripts/nui-agent-export").read_text(encoding="utf-8")
        for agent_id in EXPECTED_AGENTS:
            self.assertIn(agent_id, script, agent_id)

    def test_readmes_make_agent_installation_a_first_class_entry_point(self):
        expectations = {
            "README.md": ("Use NUI with your AI agent", "Codex", "Claude Code", "Gemini CLI", "OpenCode", "Cursor", "VS Code", "nui-agent-export"),
            "README-VN.md": ("Dùng NUI với AI agent của bạn", "Codex", "Claude Code", "Gemini CLI", "OpenCode", "Cursor", "VS Code", "nui-agent-export"),
            "README-CN.md": ("在你的 AI Agent 中使用 NUI", "Codex", "Claude Code", "Gemini CLI", "OpenCode", "Cursor", "VS Code", "nui-agent-export"),
        }
        for rel, markers in expectations.items():
            text = (ROOT / rel).read_text(encoding="utf-8")
            for marker in markers:
                self.assertIn(marker, text, f"{rel}: {marker}")

    def test_deep_agent_integration_guide_covers_thin_bridges_and_generic_paths(self):
        path = ROOT / "docs/AGENT-INTEGRATION.md"
        self.assertTrue(path.is_file(), "docs/AGENT-INTEGRATION.md")
        text = path.read_text(encoding="utf-8")
        for marker in (
            ".agents/skills/nolane-ui/SKILL.md",
            ".claude/skills/nolane-ui/SKILL.md",
            "scripts/nui-mcp-server",
            "scripts/nui-agent-export",
            "skills/using-nolane-ui/SKILL.md",
            "host permissions remain authoritative",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
