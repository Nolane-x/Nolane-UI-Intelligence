import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EvalContractTests(unittest.TestCase):
    def test_required_eval_assets_exist(self):
        required = [
            "evals/README.md",
            "evals/rubric.json",
            "evals/routing/cases.json",
            "evals/adversarial/completion-packets.json",
            "evals/craft/cases.json",
            "evals/accessibility/cases.json",
            "evals/fidelity/cases.json",
        ]
        missing = [p for p in required if not (ROOT / p).is_file()]
        self.assertEqual([], missing, f"missing eval assets: {missing}")

    def test_rubric_has_hard_gates_and_quality_dimensions(self):
        path = ROOT / "evals/rubric.json"
        self.assertTrue(path.is_file(), "rubric missing")
        data = json.loads(path.read_text(encoding="utf-8"))
        hard = set(data.get("hard_gates", {}))
        expected_hard = {
            "authority-preservation", "no-self-certification", "unknown-not-pass",
            "state-coverage", "accessibility-scope", "fidelity-evidence"
        }
        self.assertTrue(expected_hard.issubset(hard))
        dimensions = set(data.get("quality_dimensions", {}))
        expected_dimensions = {
            "product-fit", "information-architecture", "interaction-quality",
            "visual-hierarchy", "aesthetic-specificity", "system-coherence",
            "responsive-durability", "inclusive-design", "content-quality"
        }
        self.assertTrue(expected_dimensions.issubset(dimensions))

    def test_eval_cases_have_falsifiable_expectations(self):
        files = [
            ROOT / "evals/routing/cases.json",
            ROOT / "evals/craft/cases.json",
            ROOT / "evals/accessibility/cases.json",
            ROOT / "evals/fidelity/cases.json",
        ]
        for path in files:
            self.assertTrue(path.is_file(), f"missing {path.relative_to(ROOT)}")
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(data.get("cases"), f"no cases in {path.name}")
            for case in data["cases"]:
                self.assertTrue(case.get("id"), path.name)
                self.assertTrue(case.get("prompt"), case.get("id"))
                self.assertTrue(case.get("must"), case.get("id"))
                self.assertTrue(case.get("must_not"), case.get("id"))
                self.assertTrue(case.get("oracle"), case.get("id"))


if __name__ == "__main__":
    unittest.main()
