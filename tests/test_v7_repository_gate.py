import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from nolane_ui.validators import validate_repository


class V7RepositoryGateTests(unittest.TestCase):
    def _copy(self):
        t = tempfile.TemporaryDirectory()
        d = Path(t.name) / "repo"
        shutil.copytree(ROOT, d, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", "milestone-artifacts"))
        return t, d

    def test_current_repository_passes_v7_kernel_gate(self):
        r = validate_repository(ROOT)
        self.assertTrue(r["valid"], r)
        m = r["metrics"]
        self.assertEqual(m["skill_count"], 166)
        self.assertEqual(m["v7_skill_count"], 8)
        self.assertGreaterEqual(m["v7_authority_count"], 20)
        self.assertGreaterEqual(m["v7_authority_dimension_count"], 10)
        self.assertGreaterEqual(m["v7_pattern_count"], 35)
        self.assertGreaterEqual(m["v7_pattern_domain_count"], 8)
        self.assertGreaterEqual(m["v7_agent_adapter_count"], 8)
        self.assertGreaterEqual(m["v7_perception_planes"], 8)
        self.assertEqual(m["v7_adversarial_cases"], 32)
        self.assertEqual(m["v7_authority_conflicts"], 8)
        self.assertEqual(m["v7_concrete_knowledge_cases"], 8)
        self.assertEqual(m["v7_rendered_perception_cases"], 8)
        self.assertEqual(m["v7_fast_path_cases"], 8)

    def test_removing_v7_kernel_plane_fails(self):
        for rel in (
            "knowledge/ui-authority-mesh-v7.json",
            "knowledge/concrete-design-patterns-v7.json",
            "knowledge/agent-readable-ui-sources-v7.json",
            "knowledge/rendered-perception-rubric-v7.json",
            "knowledge/v7-skill-manifest.json",
            "src/nolane_ui/perceptual.py",
            "evals/v7/manifest.json",
            "docs/V7-CONCRETE-KNOWLEDGE-CLOSURE.md",
            "artifacts/v7-completion-packet.example.json",
        ):
            t, d = self._copy()
            try:
                (d / rel).unlink()
                r = validate_repository(d)
                self.assertFalse(r["valid"], rel)
                self.assertTrue(any(rel in e for e in r["errors"]), (rel, r["errors"][:8]))
            finally:
                t.cleanup()

    def test_authority_mesh_corruption_fails_repository(self):
        t, d = self._copy()
        try:
            p = d / "knowledge/ui-authority-mesh-v7.json"
            data = json.loads(p.read_text())
            data["authorities"][0]["authority_dimensions"] = []
            p.write_text(json.dumps(data, indent=2) + "\n")
            r = validate_repository(d)
            self.assertFalse(r["valid"])
            self.assertTrue(any("v7 authority" in e.lower() for e in r["errors"]), r)
        finally:
            t.cleanup()


if __name__ == "__main__":
    unittest.main()
