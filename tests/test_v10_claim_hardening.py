import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from nolane_ui.claims_v10 import promote_claim
from nolane_ui.experiment_v10 import stable_hash_jsonish, validate_experiment_manifest

ROOT = Path(__file__).resolve().parents[1]


class V10ClaimHardeningTests(unittest.TestCase):
    def _positive_aggregate(self):
        return {
            "paired_delta": 0.16,
            "ci": [0.04, 0.27],
            "hard_blocker_regressions": [],
            "per_model_direction": {"family-a": 0.13, "family-b": 0.09},
        }

    def test_real_model_boolean_without_validated_bundle_stays_non_empirical(self):
        result = promote_claim(
            {
                "claim_id": "scope-local",
                "requested_status": "EMPIRICAL_LOCAL",
                "dimension": "capability-recall",
                "bounded_claim": "NUI improves capability recall on the declared matrix.",
            },
            aggregate=self._positive_aggregate(),
            provenance={
                "real_model_runs": True,
                "model_families": ["family-a"],
                "holdout": False,
                "ablation_identified": True,
                "judge_blind": True,
            },
        )
        self.assertNotEqual(result["status"], "EMPIRICAL_LOCAL")
        self.assertIn("bundle", " ".join(result["errors"]).lower())

    def test_local_empirical_claim_requires_nonzero_matched_pairs_and_real_runs(self):
        result = promote_claim(
            {
                "claim_id": "scope-local",
                "requested_status": "EMPIRICAL_LOCAL",
                "dimension": "capability-recall",
                "bounded_claim": "NUI improves capability recall on the declared matrix.",
            },
            aggregate=self._positive_aggregate(),
            provenance={
                "real_model_runs": True,
                "validated_bundle": True,
                "bundle_digests": ["a" * 64],
                "real_run_count": 0,
                "matched_pair_count": 0,
                "model_families": ["family-a"],
                "holdout": False,
                "ablation_identified": True,
                "judge_blind": True,
            },
        )
        self.assertNotEqual(result["status"], "EMPIRICAL_LOCAL")
        joined = " ".join(result["errors"]).lower()
        self.assertIn("run", joined)
        self.assertIn("pair", joined)

    def test_valid_local_claim_needs_exact_bundle_provenance(self):
        result = promote_claim(
            {
                "claim_id": "scope-local",
                "requested_status": "EMPIRICAL_LOCAL",
                "dimension": "capability-recall",
                "bounded_claim": "NUI improves capability recall on this exact task/model/runtime matrix.",
            },
            aggregate=self._positive_aggregate(),
            provenance={
                "real_model_runs": True,
                "validated_bundle": True,
                "bundle_digests": ["a" * 64],
                "real_run_count": 24,
                "matched_pair_count": 12,
                "model_families": ["family-a"],
                "holdout": False,
                "ablation_identified": True,
                "judge_blind": True,
            },
        )
        self.assertEqual(result["status"], "EMPIRICAL_LOCAL", result["errors"])

    def test_experiment_models_require_provider_and_runtime_not_only_name(self):
        result = validate_experiment_manifest(
            {
                "version": 10,
                "experiment_id": "exp",
                "nui_revision": "abcdef123456",
                "tasks": ["scope-01"],
                "models": [{"family": "family-a", "name": "m", "snapshot": "s"}],
                "treatments": ["baseline", "nui_full", "nui_ablation:product-envelope"],
                "replicates": 1,
                "tool_budget": {"browser": True},
            },
            {"task_ids": ["scope-01"]},
            {"ablation_ids": ["product-envelope"], "mutation_ids": []},
        )
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("provider", joined)
        self.assertIn("runtime", joined)

    def test_hash_of_mapping_is_canonical_not_insertion_order_sensitive(self):
        self.assertEqual(
            stable_hash_jsonish({"b": 2, "a": 1, "nested": {"z": 9, "x": 7}}),
            stable_hash_jsonish({"nested": {"x": 7, "z": 9}, "a": 1, "b": 2}),
        )

    def test_aggregate_does_not_treat_incomplete_non_synthetic_row_as_real_run(self):
        script = ROOT / "scripts" / "nui-v10-aggregate"
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "runs.jsonl"
            path.write_text(json.dumps({
                "run_id": "fake-real",
                "synthetic_example": False,
                "status": "success",
                "model_family": "family-a"
            }) + "\n", encoding="utf-8")
            proc = subprocess.run([sys.executable, str(script), str(path)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertFalse(payload["real_model_runs"])
            self.assertEqual(payload["claim_ceiling"], "STRUCTURAL_ONLY")
            self.assertGreater(payload["invalid_run_count"], 0)


if __name__ == "__main__":
    unittest.main()
