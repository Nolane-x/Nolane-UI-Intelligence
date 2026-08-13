import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V7ReleaseTests(unittest.TestCase):
    def test_current_version_is_not_older_than_v7(self):
        config = json.loads((ROOT / "nui.config.json").read_text(encoding="utf-8"))
        major, minor, patch = (int(x) for x in config["version"].split("."))
        self.assertGreaterEqual((major, minor, patch), (0, 7, 0))

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

    def test_v7_release_artifact_remains_available_after_later_versions(self):
        self.assertTrue((ROOT / "artifacts/v7-completion-packet.example.json").is_file())
        self.assertTrue((ROOT / "docs/V7-CONCRETE-KNOWLEDGE-CLOSURE.md").is_file())

    def test_release_docs_explain_v7_execution_contract(self):
        docs = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in ("README.md", "docs/USAGE.md", "AGENTS.md"))
        for phrase in (
            "decision-dimensional authority",
            "access protocol is not authority",
            "concrete design packet",
            "rendered perception",
            "mechanism, not trade dress",
        ):
            self.assertIn(phrase, docs.lower())


if __name__ == "__main__":
    unittest.main()
