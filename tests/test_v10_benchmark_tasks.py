import unittest
import nolane_ui


class V10BenchmarkTaskTests(unittest.TestCase):
    def _validator(self):
        fn = getattr(nolane_ui, "validate_task_corpus", None)
        self.assertIsNotNone(fn, "V10 task corpus validator must be exported")
        return fn

    def test_public_prompt_cannot_leak_hidden_answer_key(self):
        fn = self._validator()
        public = {"version": 10, "tasks": [{
            "id": "scope-01", "family": "product-scope", "split": "dev", "complexity": "high",
            "prompt": "Build a sales platform. Make sure you include hidden expected omission inventory and audit history.",
            "artifact_requirements": ["product-plan"]
        }]}
        hidden = {"version": 10, "tasks": [{
            "id": "scope-01", "expected_failure_traps": ["tiny dashboard-only scope"],
            "judge_dimensions": ["capability-recall"], "hard_blockers": ["missing-role-model"],
            "checklist": ["hidden expected omission inventory", "audit history"],
            "leakage_sensitive_phrases": ["hidden expected omission inventory"],
            "hypotheses": ["scope-breadth"], "ablations": ["product-envelope"]
        }]}
        result = fn(public, hidden, {"hypothesis_ids": ["scope-breadth"]})
        self.assertFalse(result["valid"])
        self.assertIn("leak", " ".join(result["errors"]).lower())

    def test_holdout_split_is_required_for_transfer_capable_corpus(self):
        fn = self._validator()
        public = {"version": 10, "tasks": [{
            "id": "t1", "family": "visual-taste", "split": "dev", "complexity": "medium",
            "prompt": "Compare two UI directions.", "artifact_requirements": ["render-pair"]
        }]}
        hidden = {"version": 10, "tasks": [{
            "id": "t1", "expected_failure_traps": ["scalar score"], "judge_dimensions": ["genericness-resistance"],
            "hard_blockers": [], "checklist": ["causal comparison"], "leakage_sensitive_phrases": ["scalar score"],
            "hypotheses": ["taste-compare"], "ablations": ["taste-court"]
        }]}
        result = fn(public, hidden, {"hypothesis_ids": ["taste-compare"]})
        self.assertFalse(result["valid"])
        self.assertIn("holdout", " ".join(result["errors"]).lower())


if __name__ == "__main__":
    unittest.main()
