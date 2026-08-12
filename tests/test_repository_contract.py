import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_required_contract_files_exist(self):
        required = [
            "README.md",
            "AGENTS.md",
            "nui.config.json",
            "skills/skill-graph.json",
            "schemas/ui-task-profile.schema.json",
            "schemas/finding.schema.json",
            "schemas/evidence.schema.json",
            "schemas/completion-packet.schema.json",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual([], missing, f"missing repository contracts: {missing}")

    def test_skill_graph_declares_canonical_lifecycle(self):
        graph_path = ROOT / "skills/skill-graph.json"
        self.assertTrue(graph_path.is_file(), "skill graph must exist before lifecycle can be verified")
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        expected = [
            "INTAKE", "CONTRACTED", "ROUTED", "DISCOVERED", "ARCHITECTED",
            "DIVERGED", "DESIGN_SELECTED", "SYSTEMIZED", "SPECIFIED",
            "IMPLEMENTABLE", "RENDERED", "CRITIQUED", "VERIFIED", "RELEASED",
        ]
        self.assertEqual(expected, graph.get("lifecycle"))
        self.assertIn("RECOVERY", graph.get("exception_states", []))

    def test_skill_graph_contains_mandatory_kernel(self):
        graph_path = ROOT / "skills/skill-graph.json"
        self.assertTrue(graph_path.is_file(), "skill graph must exist before kernel can be verified")
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        required = {
            "using-nolane-ui", "nolane-ui", "ui-contracting", "routing-ui-work",
            "compiling-ui-obligations", "binding-ui-evidence", "challenging-ui-designs",
            "gating-ui-completion", "recovering-ui-work",
        }
        declared = set(graph.get("skills", {}).keys())
        self.assertEqual(set(), required - declared)


if __name__ == "__main__":
    unittest.main()
