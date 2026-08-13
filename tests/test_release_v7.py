import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V7ReleaseTests(unittest.TestCase):
    def test_versions_are_070(self):
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertRegex(pyproject, r'version\s*=\s*"0\.7\.0"')
        config = json.loads((ROOT / "nui.config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["version"], "0.7.0")

    def test_concrete_packet_schema_matches_runtime_contract(self):
        schema = json.loads((ROOT / "schemas/concrete-design-packet.schema.json").read_text(encoding="utf-8"))
        required = set(schema["required"])
        self.assertTrue({
            "status", "task_thesis", "authority_stack", "decisions",
            "implementation_shortcuts", "validation_obligations", "unresolved_blockers"
        }.issubset(required))
        self.assertEqual(schema["properties"]["decisions"]["maxItems"], 9)
        self.assertIn("rationale", schema["properties"]["decisions"]["items"]["required"])
        self.assertIn("unresolved_blockers", schema["properties"])
        self.assertNotIn("blockers", schema["required"])

    def test_release_packet_is_v7_and_names_new_obligations(self):
        text = (ROOT / "scripts/nui-release-packet").read_text(encoding="utf-8")
        self.assertIn("NUI-V7-STRUCTURAL", text)
        for obligation in (
            "O-V7-AUTHORITY-MESH",
            "O-V7-CONCRETE-KNOWLEDGE",
            "O-V7-RENDERED-PERCEPTION",
            "O-V7-AGENT-READABLE-CONTEXT",
            "O-V7-ADVERSARIAL-EVAL",
        ):
            self.assertIn(obligation, text)
        self.assertIn("concrete craft", text.lower())
        self.assertIn("rendered perception", text.lower())

    def test_ci_packages_v7_exact_artifacts(self):
        text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("nui-v7-completion-packet", text)
        self.assertIn("nui-v7-complete-project", text)
        self.assertIn("Nolane-UI-Intelligence-v7-complete.zip", text)
        self.assertNotIn("nui-v6-completion-packet", text)
        self.assertNotIn("Nolane-UI-Intelligence-v6-complete.zip", text)

    def test_release_docs_explain_v7_execution_contract(self):
        docs = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in ("README.md", "docs/USAGE.md", "AGENTS.md"))
        for phrase in (
            "decision-dimensional authority",
            "access protocol is not authority",
            "concrete design packet",
            "rendered perception",
            "mechanism, not trade dress",
            "166 canonical skills",
        ):
            self.assertIn(phrase, docs.lower())


if __name__ == "__main__":
    unittest.main()
