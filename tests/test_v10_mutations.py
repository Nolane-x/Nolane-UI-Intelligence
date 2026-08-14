import unittest
import nolane_ui


class V10MutationTests(unittest.TestCase):
    def _validator(self):
        fn = getattr(nolane_ui, "validate_mutation_registry", None)
        self.assertIsNotNone(fn, "V10 mutation validator must be exported")
        return fn

    def test_mutation_without_targeted_degradation_is_invalid(self):
        fn = self._validator()
        record = {"version": 10, "mutations": [{
            "id": "scalar-beauty", "kind": "semantic", "target_hypothesis": "taste-compare",
            "target_owner": "exploring-aesthetic-directions", "target_dimensions": ["genericness-resistance"],
            "exposed_tasks": ["taste-01"], "operation": "replace comparison with scalar score"
        }]}
        result = fn(record, {"hypothesis_ids": ["taste-compare"]}, {"task_ids": ["taste-01"]})
        self.assertFalse(result["valid"])
        self.assertIn("degrad", " ".join(result["errors"]).lower())

    def test_placebo_must_declare_dimensions_expected_to_remain_stable(self):
        fn = self._validator()
        record = {"version": 10, "mutations": [{
            "id": "placebo-copy-tone", "kind": "placebo", "target_hypothesis": "scope-breadth",
            "target_owner": "modeling-product-intent", "target_dimensions": ["capability-recall"],
            "exposed_tasks": ["scope-01"], "operation": "alter irrelevant prose tone",
            "expected_effect": {"direction": "no-material-change"}
        }]}
        result = fn(record, {"hypothesis_ids": ["scope-breadth"]}, {"task_ids": ["scope-01"]})
        self.assertFalse(result["valid"])
        self.assertIn("stable", " ".join(result["errors"]).lower())


if __name__ == "__main__":
    unittest.main()
