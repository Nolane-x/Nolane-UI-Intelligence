import unittest
import nolane_ui


class V10StatsTests(unittest.TestCase):
    def _delta(self):
        fn = getattr(nolane_ui, "paired_delta", None)
        self.assertIsNotNone(fn, "V10 paired_delta must be exported")
        return fn

    def _ci(self):
        fn = getattr(nolane_ui, "bootstrap_ci", None)
        self.assertIsNotNone(fn, "V10 bootstrap_ci must be exported")
        return fn

    def _ablation(self):
        fn = getattr(nolane_ui, "evaluate_ablation_recovery", None)
        self.assertIsNotNone(fn, "V10 ablation recovery evaluator must be exported")
        return fn

    def test_paired_delta_rejects_unmatched_sample_keys(self):
        fn = self._delta()
        with self.assertRaises(ValueError):
            fn({"a": 0.8, "b": 0.7}, {"a": 0.5, "c": 0.2})

    def test_bootstrap_interval_is_deterministic_and_contains_observed_center(self):
        fn = self._ci()
        samples = [0.1, 0.2, 0.15, 0.18, 0.12, 0.21]
        ci1 = fn(samples, confidence=0.95, resamples=1000, seed=7)
        ci2 = fn(samples, confidence=0.95, resamples=1000, seed=7)
        self.assertEqual(ci1, ci2)
        mean = sum(samples) / len(samples)
        self.assertLessEqual(ci1[0], mean)
        self.assertGreaterEqual(ci1[1], mean)

    def test_targeted_ablation_must_degrade_owned_dimension(self):
        fn = self._ablation()
        result = fn(full={"capability-recall": [0.8, 0.82, 0.79]}, ablated={"capability-recall": [0.81, 0.83, 0.8]}, target_dimension="capability-recall")
        self.assertFalse(result["identified"])
        self.assertIn("degrad", " ".join(result["errors"]).lower())


if __name__ == "__main__":
    unittest.main()
