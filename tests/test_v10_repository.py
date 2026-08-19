import json
import unittest
from pathlib import Path

from nolane_ui.validators import validate_repository

ROOT = Path(__file__).resolve().parents[1]


class V10RepositoryTests(unittest.TestCase):
    def test_repository_reports_v10_behavioral_metrics_and_structural_claim_ceiling(self):
        result = validate_repository(ROOT)
        self.assertTrue(result["valid"], result["errors"])
        metrics = result["metrics"]
        self.assertEqual(metrics["nui_major"], 10)
        self.assertGreaterEqual(metrics["v10_hypotheses"], 12)
        self.assertEqual(metrics["v10_benchmark_tasks"], 48)
        self.assertEqual(metrics["v10_holdout_tasks"], 12)
        self.assertGreaterEqual(metrics["v10_mutations"], 16)
        self.assertEqual(metrics["v10_claim_ceiling"], "STRUCTURAL_ONLY")

    def test_v10_reports_current_graph_without_erasing_historical_baseline(self):
        result = validate_repository(ROOT)
        graph = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))["skills"]
        self.assertGreaterEqual(len(graph), 174)
        self.assertEqual(result["metrics"]["skill_count"], len(graph))

    def test_required_v10_protocol_files_exist(self):
        required = [
            "src/nolane_ui/v10_repository.py", "knowledge/v10-behavioral-hypotheses.json",
            "knowledge/v10-empirical-evaluation-sources.json", "benchmarks/v10/tasks-public.json",
            "benchmarks/v10/tasks-hidden.json", "benchmarks/v10/mutations.json",
            "docs/V10-EMPIRICAL-RUN-PROTOCOL.md", "evals/v10-behavioral-empirical-adversarial.json",
            "schemas/v10-experiment.schema.json", "schemas/v10-run-record.schema.json", "schemas/v10-claim.schema.json",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).is_file(), rel)


if __name__ == "__main__":
    unittest.main()
