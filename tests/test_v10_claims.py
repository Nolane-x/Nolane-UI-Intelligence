import unittest
import nolane_ui


class V10ClaimTests(unittest.TestCase):
    def _promote(self):
        fn = getattr(nolane_ui, "promote_claim", None)
        self.assertIsNotNone(fn, "V10 promote_claim must be exported")
        return fn

    def test_structural_fixtures_cannot_be_promoted_to_empirical(self):
        fn = self._promote()
        result = fn({
            "claim_id": "scope-improves", "requested_status": "EMPIRICAL_LOCAL",
            "dimension": "capability-recall", "bounded_claim": "NUI improves capability recall on this matrix"
        }, aggregate={"paired_delta": 0.4, "ci": [0.2, 0.5], "hard_blocker_regressions": []}, provenance={
            "real_model_runs": False, "model_families": ["synthetic"], "holdout": False, "ablation_identified": True
        })
        self.assertEqual(result["status"], "STRUCTURAL_ONLY")
        self.assertTrue(result["errors"])

    def test_transfer_claim_requires_multiple_model_families_and_holdout(self):
        fn = self._promote()
        result = fn({
            "claim_id": "taste-transfer", "requested_status": "EMPIRICAL_TRANSFER",
            "dimension": "genericness-resistance", "bounded_claim": "NUI improves preference across configured models"
        }, aggregate={
            "paired_delta": 0.15, "ci": [0.04, 0.24], "hard_blocker_regressions": [],
            "per_model_direction": {"family-a": 0.12}
        }, provenance={
            "real_model_runs": True, "model_families": ["family-a"], "holdout": False, "ablation_identified": True
        })
        self.assertNotEqual(result["status"], "EMPIRICAL_TRANSFER")
        joined = " ".join(result["errors"]).lower()
        self.assertIn("model", joined)
        self.assertIn("holdout", joined)

    def test_hard_blocker_regression_prevents_positive_empirical_claim(self):
        fn = self._promote()
        result = fn({
            "claim_id": "visual-win", "requested_status": "EMPIRICAL_LOCAL",
            "dimension": "visual-craft", "bounded_claim": "visual quality improves"
        }, aggregate={
            "paired_delta": 0.2, "ci": [0.08, 0.3], "hard_blocker_regressions": ["accessibility-core"]
        }, provenance={
            "real_model_runs": True, "model_families": ["family-a"], "holdout": False, "ablation_identified": True
        })
        self.assertEqual(result["status"], "REJECTED")


if __name__ == "__main__":
    unittest.main()
