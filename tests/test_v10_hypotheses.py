import unittest
import nolane_ui


class V10HypothesisTests(unittest.TestCase):
    def _validator(self):
        fn = getattr(nolane_ui, "validate_hypothesis_registry", None)
        self.assertIsNotNone(fn, "V10 hypothesis validator must be exported")
        return fn

    def test_descriptive_rule_without_falsifier_is_not_behavioral_evidence(self):
        fn = self._validator()
        result = fn({"version": 10, "hypotheses": [{
            "hypothesis_id": "scope-breadth",
            "owners": ["modeling-product-intent"],
            "decision_boundary": "scope discovery",
            "observable_behavior": "recalls implied capability families",
            "baseline_failure": "prompt-literal compression",
            "positive_controls": ["ambiguous full platform"],
            "negative_controls": ["single-purpose utility"],
            "evidence_channels": ["capability-ledger"],
            "dimensions": ["capability-recall"],
            "tasks": ["scope-01"],
            "mutations": ["scope-compress"],
            "ablations": ["product-envelope"],
            "prohibited_overclaims": ["proves universal completeness"]
        }]})
        self.assertFalse(result["valid"])
        self.assertTrue(any("falsif" in e.lower() for e in result["errors"]))

    def test_hypothesis_requires_positive_and_negative_controls(self):
        fn = self._validator()
        base = {
            "hypothesis_id": "taste-compare", "owners": ["exploring-aesthetic-directions"],
            "decision_boundary": "comparative aesthetic selection",
            "observable_behavior": "prefers evidence-backed candidate",
            "baseline_failure": "scalar self-score", "evidence_channels": ["render-pair"],
            "falsifiers": ["ablation does not reduce pairwise preference"],
            "dimensions": ["genericness-resistance"], "tasks": ["taste-01"],
            "mutations": ["scalar-beauty"], "ablations": ["taste-court"],
            "prohibited_overclaims": ["objective beauty"]
        }
        result = fn({"version": 10, "hypotheses": [base]})
        self.assertFalse(result["valid"])
        self.assertIn("control", " ".join(result["errors"]).lower())

    def test_duplicate_observable_behavior_requires_interaction_declaration(self):
        fn = self._validator()
        def h(i, owner):
            return {
                "hypothesis_id": i, "owners": [owner], "decision_boundary": i,
                "observable_behavior": "detects omitted recovery paths",
                "baseline_failure": "recovery omission", "positive_controls": ["complex"],
                "negative_controls": ["not applicable"], "evidence_channels": ["ledger"],
                "falsifiers": ["no degradation under ablation"], "dimensions": ["state-recovery-completeness"],
                "tasks": ["recovery-01"], "mutations": ["remove-recovery"], "ablations": [i],
                "prohibited_overclaims": ["universal"]
            }
        result = fn({"version": 10, "hypotheses": [h("a", "modeling-product-intent"), h("b", "architecting-information")]})
        self.assertFalse(result["valid"])
        self.assertIn("overlap", " ".join(result["errors"]).lower())


if __name__ == "__main__":
    unittest.main()
