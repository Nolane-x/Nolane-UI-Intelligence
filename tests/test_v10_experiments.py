import unittest
import nolane_ui


class V10ExperimentTests(unittest.TestCase):
    def _manifest_validator(self):
        fn = getattr(nolane_ui, "validate_experiment_manifest", None)
        self.assertIsNotNone(fn, "V10 experiment validator must be exported")
        return fn

    def _run_validator(self):
        fn = getattr(nolane_ui, "validate_run_record", None)
        self.assertIsNotNone(fn, "V10 run validator must be exported")
        return fn

    def test_manifest_requires_matched_baseline_full_and_ablation_conditions(self):
        fn = self._manifest_validator()
        manifest = {
            "version": 10, "experiment_id": "exp-1", "nui_revision": "abc123",
            "tasks": ["scope-01"], "models": [{"family": "family-a", "name": "model-a", "snapshot": "2026-08"}],
            "treatments": ["nui_full"], "replicates": 2,
            "tool_budget": {"browser": True, "max_steps": 40}
        }
        result = fn(manifest, {"task_ids": ["scope-01"]}, {"mutation_ids": [], "ablation_ids": ["product-envelope"]})
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("baseline", joined)
        self.assertIn("ablation", joined)

    def test_run_record_requires_exact_provenance_and_failure_visibility(self):
        fn = self._run_validator()
        run = {
            "run_id": "r1", "experiment_id": "exp-1", "task_id": "scope-01", "treatment": "nui_full",
            "provider": "provider-x", "model_family": "family-a", "model_name": "model-a",
            "status": "success", "seed": 1, "temperature": 0.2,
            "prompt_sha256": "a" * 64, "context_sha256": "b" * 64,
            "artifact_digests": ["c" * 64]
        }
        result = fn(run, {"experiment_id": "exp-1", "nui_revision": "abc123"})
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("snapshot", joined)
        self.assertIn("runtime", joined)
        self.assertIn("nui", joined)

    def test_exclusion_reason_is_closed_enum(self):
        fn = self._run_validator()
        run = {
            "run_id": "r1", "experiment_id": "exp-1", "task_id": "scope-01", "treatment": "baseline",
            "provider": "p", "model_family": "f", "model_name": "m", "model_snapshot": "s", "runtime": "runner-1",
            "nui_revision": "abc123", "status": "excluded", "exclusion_reason": "looked bad",
            "seed": 1, "temperature": 0, "prompt_sha256": "a"*64, "context_sha256": "b"*64,
            "artifact_digests": [], "tool_budget_hash": "c"*64
        }
        result = fn(run, {"experiment_id": "exp-1", "nui_revision": "abc123"})
        self.assertFalse(result["valid"])
        self.assertIn("exclusion", " ".join(result["errors"]).lower())


if __name__ == "__main__":
    unittest.main()
