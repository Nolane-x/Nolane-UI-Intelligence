import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V10AdversarialTests(unittest.TestCase):
    def test_corpus_has_48_two_sided_cases_across_empirical_failure_planes(self):
        data = json.loads((ROOT / "evals/v10-behavioral-empirical-adversarial.json").read_text(encoding="utf-8"))
        self.assertEqual(data["version"], 10)
        cases = data["cases"]
        self.assertGreaterEqual(len(cases), 48)
        ids = [x["id"] for x in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual({"BLOCK", "ALLOW"}, {x["expected_verdict"] for x in cases})
        planes = {x["plane"] for x in cases}
        for required in ("provenance", "blindness", "pairing", "statistics", "ablation", "holdout", "missingness", "cost", "claims", "contamination"):
            self.assertIn(required, planes)

    def test_each_adversary_names_failure_and_detector(self):
        data = json.loads((ROOT / "evals/v10-behavioral-empirical-adversarial.json").read_text(encoding="utf-8"))
        for case in data["cases"]:
            self.assertTrue(case["stimulus"])
            self.assertTrue(case["expected_failure"])
            self.assertTrue(case["detector"])
            self.assertTrue(case["rationale"])


if __name__ == "__main__":
    unittest.main()
