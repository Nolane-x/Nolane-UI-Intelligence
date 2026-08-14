import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V9AdversarialTests(unittest.TestCase):
    def test_v9_corpus_has_breadth_unique_ids_and_two_sided_traps(self):
        data = json.loads((ROOT / "evals" / "v9-product-completeness-adversarial.json").read_text(encoding="utf-8"))
        self.assertEqual(data["version"], 9)
        cases = data["cases"]
        self.assertGreaterEqual(len(cases), 24)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        categories = {case["category"] for case in cases}
        self.assertGreaterEqual(len(categories), 8)
        verdicts = {case["expected_verdict"] for case in cases}
        self.assertIn("BLOCK", verdicts)
        self.assertIn("ALLOW", verdicts)
        for case in cases:
            self.assertTrue(case["scenario"])
            self.assertTrue(case["protected_invariant"])
            self.assertGreaterEqual(len(case["must_detect"]), 1)
            self.assertIn(case["expected_verdict"], {"BLOCK", "ALLOW", "RE_DIVERGE"})

    def test_corpus_attacks_all_v9_planes(self):
        data = json.loads((ROOT / "evals" / "v9-product-completeness-adversarial.json").read_text(encoding="utf-8"))
        categories = {case["category"] for case in data["cases"]}
        required = {
            "scope", "settings", "account-lifecycle", "workspace", "residue",
            "taste", "render-critique", "reference", "domain-audience",
            "render-fidelity", "motion"
        }
        self.assertTrue(required.issubset(categories))


if __name__ == "__main__":
    unittest.main()
