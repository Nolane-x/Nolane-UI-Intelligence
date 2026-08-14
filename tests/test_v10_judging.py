import unittest
import nolane_ui


class V10JudgingTests(unittest.TestCase):
    def _blind(self):
        fn = getattr(nolane_ui, "blind_run_for_judge", None)
        self.assertIsNotNone(fn, "V10 blind-run helper must be exported")
        return fn

    def _orientation(self):
        fn = getattr(nolane_ui, "pair_orientation", None)
        self.assertIsNotNone(fn, "V10 pair orientation helper must be exported")
        return fn

    def _leak(self):
        fn = getattr(nolane_ui, "detect_leakage", None)
        self.assertIsNotNone(fn, "V10 leakage detector must be exported")
        return fn

    def test_judge_payload_strips_treatment_and_generation_identity(self):
        fn = self._blind()
        payload = fn({
            "run_id": "r1", "treatment": "nui_ablation:taste-court", "provider": "p",
            "model_family": "family-a", "model_name": "model-a", "model_snapshot": "s",
            "nui_revision": "deadbeef", "route": ["exploring-aesthetic-directions"],
            "artifact_refs": ["shot-1"], "task_id": "taste-01", "output_text": "candidate result"
        })
        rendered = repr(payload).lower()
        for forbidden in ("ablation", "nui_revision", "provider", "model-a", "exploring-aesthetic-directions"):
            self.assertNotIn(forbidden, rendered)

    def test_pair_orientation_is_deterministic_and_not_constant(self):
        fn = self._orientation()
        a1 = fn("exp-1", "task-1", 0)
        a2 = fn("exp-1", "task-1", 0)
        self.assertEqual(a1, a2)
        orientations = {fn("exp-1", f"task-{i}", i) for i in range(10)}
        self.assertGreater(len(orientations), 1)

    def test_hidden_phrase_leakage_is_detected(self):
        fn = self._leak()
        hits = fn("The answer is HIDDEN_RECOVERY_TRAP and we should include it.", {
            "leakage_sensitive_phrases": ["HIDDEN_RECOVERY_TRAP", "PRIVATE_RUBRIC_TERM"]
        })
        self.assertIn("HIDDEN_RECOVERY_TRAP", hits)


if __name__ == "__main__":
    unittest.main()
