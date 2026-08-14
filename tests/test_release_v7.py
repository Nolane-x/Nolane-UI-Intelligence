import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V7ReleaseTests(unittest.TestCase):
    def test_current_version_is_not_older_than_v7(self):
        config = json.loads((ROOT / "nui.config.json").read_text(encoding="utf-8"))
        version = tuple(int(x) for x in config["version"].split("."))
        self.assertGreaterEqual(version, (0, 7, 0))

    def test_concrete_packet_schema_matches_v7_contract(self):
        schema = json.loads((ROOT / "schemas/concrete-design-packet.schema.json").read_text(encoding="utf-8"))
        required = set(schema["required"])
        self.assertTrue({"status", "task_thesis", "authority_stack", "decisions", "implementation_shortcuts", "validation_obligations", "unresolved_blockers"}.issubset(required))
        self.assertEqual(schema["properties"]["decisions"]["maxItems"], 9)
        self.assertIn("rationale", schema["properties"]["decisions"]["items"]["required"])

    def test_v7_release_artifacts_remain_available(self):
        for rel in ("artifacts/v7-completion-packet.example.json", "docs/V7-CONCRETE-KNOWLEDGE-CLOSURE.md", "knowledge/v7-skill-manifest.json", "src/nolane_ui/validators_v7.py"):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_release_docs_preserve_v7_execution_language(self):
        docs = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in ("README.md", "docs/USAGE.md", "AGENTS.md"))
        for phrase in ("decision-dimensional authority", "access protocol is not authority", "concrete design packet", "rendered perception", "mechanism, not trade dress"):
            self.assertIn(phrase, docs.lower())


if __name__ == "__main__":
    unittest.main()
