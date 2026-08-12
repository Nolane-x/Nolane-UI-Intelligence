import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIMES = ["generic", "codex", "claude-code", "gemini-cli", "cursor", "opencode"]
REQUIRED_CAPABILITIES = {
    "file-read", "file-write", "test-execution", "browser-inspection",
    "screenshot-capture", "semantic-tree", "subagent-review", "component-retrieval"
}


class AdapterTests(unittest.TestCase):
    def test_all_runtime_adapters_exist(self):
        missing = [name for name in RUNTIMES if not (ROOT / "adapters" / name / "README.md").is_file()]
        self.assertEqual([], missing)

    def test_capability_map_covers_runtime_and_fallbacks(self):
        path = ROOT / "adapters" / "capabilities.json"
        self.assertTrue(path.is_file(), "capability map missing")
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(REQUIRED_CAPABILITIES, set(data.get("capabilities", {})))
        for capability, record in data["capabilities"].items():
            self.assertIn("fallback", record, capability)
            self.assertEqual(set(RUNTIMES), set(record.get("runtimes", {})), capability)


if __name__ == "__main__":
    unittest.main()
