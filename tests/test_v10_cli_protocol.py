import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V10CLIProtocolTests(unittest.TestCase):
    def test_build_matrix_is_deterministic_and_contains_required_conditions(self):
        script = ROOT / "scripts/nui-v10-build-run-matrix"
        experiment = ROOT / "examples/v10/experiment.example.json"
        first = subprocess.run([sys.executable, str(script), str(experiment)], cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run([sys.executable, str(script), str(experiment)], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        rows = [json.loads(x) for x in first.stdout.splitlines() if x.strip()]
        treatments = {x["treatment"] for x in rows}
        self.assertIn("baseline", treatments)
        self.assertIn("nui_full", treatments)
        self.assertTrue(any(x.startswith("nui_ablation:") for x in treatments))

    def test_aggregate_without_real_runs_stays_structural_only(self):
        script = ROOT / "scripts/nui-v10-aggregate"
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "runs.jsonl"
            path.write_text("", encoding="utf-8")
            proc = subprocess.run([sys.executable, str(script), str(path)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual(payload["claim_ceiling"], "STRUCTURAL_ONLY")
            self.assertFalse(payload["real_model_runs"])

    def test_example_run_record_is_not_misrepresented_as_real_empirical_proof(self):
        example = (ROOT / "examples/v10/run-record.example.jsonl").read_text(encoding="utf-8")
        row = json.loads(example.splitlines()[0])
        self.assertTrue(row["synthetic_example"])


if __name__ == "__main__":
    unittest.main()
