import unittest

from nolane_ui.completion_v10 import validate_v10_completion_evidence


class V10CompletionTests(unittest.TestCase):
    def test_structural_release_must_admit_no_real_model_efficacy_runs(self):
        result = validate_v10_completion_evidence({
            "version": 10,
            "claim_ceiling": "STRUCTURAL_ONLY",
            "empirical_runs_executed": False,
            "imported_empirical_bundle_digests": [],
            "unresolved_empirical_claims": ["No real cross-model treatment matrix executed in repository CI."],
        })
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["claim_ceiling"], "STRUCTURAL_ONLY")

    def test_empirical_local_cannot_be_self_declared_without_validated_bundle(self):
        result = validate_v10_completion_evidence({
            "version": 10,
            "claim_ceiling": "EMPIRICAL_LOCAL",
            "empirical_runs_executed": True,
            "imported_empirical_bundle_digests": [],
            "real_run_count": 24,
            "matched_pair_count": 12,
            "ablation_identified": True,
            "judge_blind": True,
        })
        self.assertFalse(result["valid"])
        self.assertIn("bundle", " ".join(result["errors"]).lower())

    def test_empirical_transfer_requires_holdout_and_multiple_families(self):
        result = validate_v10_completion_evidence({
            "version": 10,
            "claim_ceiling": "EMPIRICAL_TRANSFER",
            "empirical_runs_executed": True,
            "validated_bundle": True,
            "imported_empirical_bundle_digests": ["a" * 64],
            "real_run_count": 40,
            "matched_pair_count": 20,
            "ablation_identified": True,
            "judge_blind": True,
            "holdout_evidence": False,
            "model_families": ["family-a"],
            "per_family_positive_direction": {"family-a": True},
        })
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("holdout", joined)
        self.assertIn("model", joined)

    def test_hard_regression_rejects_empirical_promotion(self):
        result = validate_v10_completion_evidence({
            "version": 10,
            "claim_ceiling": "EMPIRICAL_LOCAL",
            "empirical_runs_executed": True,
            "validated_bundle": True,
            "imported_empirical_bundle_digests": ["b" * 64],
            "real_run_count": 20,
            "matched_pair_count": 10,
            "ablation_identified": True,
            "judge_blind": True,
            "hard_blocker_regressions": ["accessibility-core"],
        })
        self.assertFalse(result["valid"])
        self.assertEqual(result["claim_ceiling"], "REJECTED")


if __name__ == "__main__":
    unittest.main()
