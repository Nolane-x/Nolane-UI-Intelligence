import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from nolane_ui.validators import validate_repository


class V4RepositoryGateTests(unittest.TestCase):
    def _copy_repo(self):
        temp = tempfile.TemporaryDirectory()
        dest = Path(temp.name) / "repo"
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", "milestone-artifacts"))
        return temp, dest

    def test_current_repository_passes_v4_gate(self):
        result = validate_repository(ROOT)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["metrics"]["v4_skill_count"], 6)
        self.assertGreaterEqual(result["metrics"]["ecosystem_source_count"], 40)
        self.assertEqual(result["metrics"]["v4_adversarial_cases"], 14)
        self.assertEqual(result["metrics"]["skill_contracts_checked"], 141)

    def test_removing_registry_or_v4_manifest_fails_repository(self):
        for relative in ("knowledge/ui-ecosystem-registry.json", "knowledge/v4-skill-manifest.json"):
            temp, dest = self._copy_repo()
            try:
                (dest / relative).unlink()
                result = validate_repository(dest)
                self.assertFalse(result["valid"], relative)
                self.assertTrue(any(relative in error for error in result["errors"]), result)
            finally:
                temp.cleanup()

    def test_v4_graph_contract_drift_fails_repository(self):
        temp, dest = self._copy_repo()
        try:
            graph_path = dest / "skills/skill-graph.json"
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
            graph["skills"]["selecting-ui-building-blocks"]["output"] = "wrong-output"
            graph_path.write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")
            result = validate_repository(dest)
            self.assertFalse(result["valid"])
            self.assertTrue(any("selecting-ui-building-blocks" in error for error in result["errors"]), result)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
