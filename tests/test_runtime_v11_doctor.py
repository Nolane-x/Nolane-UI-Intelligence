import tempfile
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.doctor import REQUIRED_RUNTIME_ARTIFACTS, diagnose_runtime_state
from nolane_ui.runtime_v11.evidence import build_evidence_binding, sha256_text


ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11DoctorTests(unittest.TestCase):
    def test_healthy_repository_runtime_has_no_blocking_findings(self):
        report = diagnose_runtime_state(ROOT)
        self.assertTrue(report["valid"], report["findings"])
        self.assertEqual(report["blocking_count"], 0)

    def test_required_artifact_inventory_covers_phase2_foundation(self):
        required = set(REQUIRED_RUNTIME_ARTIFACTS)
        expected = {
            "scripts/nui-detect",
            "scripts/nui-runtime-doctor",
            "knowledge/runtime-detector-rules-v11.json",
            "schemas/runtime-browser-observation-v11.schema.json",
            "schemas/runtime-evidence-binding-v11.schema.json",
            "schemas/runtime-live-session-v11.schema.json",
            "src/nolane_ui/runtime_v11/__init__.py",
            "src/nolane_ui/runtime_v11/contracts.py",
            "src/nolane_ui/runtime_v11/registry.py",
            "src/nolane_ui/runtime_v11/detector.py",
            "src/nolane_ui/runtime_v11/adjudication.py",
            "src/nolane_ui/runtime_v11/cli.py",
            "src/nolane_ui/runtime_v11/browser.py",
            "src/nolane_ui/runtime_v11/hooks.py",
            "src/nolane_ui/runtime_v11/evidence.py",
            "src/nolane_ui/runtime_v11/doctor.py",
            "src/nolane_ui/runtime_v11/doctor_cli.py",
            "src/nolane_ui/runtime_v11/live.py",
        }
        self.assertTrue(expected.issubset(required), expected - required)

    def test_missing_canonical_detector_artifact_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = diagnose_runtime_state(root)
            ids = {item["id"] for item in report["findings"]}
            self.assertFalse(report["valid"])
            self.assertIn("runtime-installation.missing-artifact", ids)

    def test_stale_evidence_is_routed_not_erased(self):
        binding = build_evidence_binding(
            evidence_id="render:settings",
            revision="rev-a",
            source_digests={"src/settings.tsx": sha256_text("before")},
            artifacts=["artifacts/settings.png"],
        )
        report = diagnose_runtime_state(
            ROOT,
            evidence_bindings=[binding],
            current_digests={"src/settings.tsx": sha256_text("after")},
        )
        stale = [item for item in report["findings"] if item["id"] == "runtime-evidence.stale"]
        self.assertEqual(len(stale), 1)
        self.assertEqual(stale[0]["action"], "route")
        self.assertIn("src/settings.tsx", stale[0]["details"]["changed_paths"])

    def test_required_capability_gap_is_blocking_unknown(self):
        report = diagnose_runtime_state(
            ROOT,
            required_capabilities=["browser", "screenshot", "accessibility-tree"],
            available_capabilities=["browser"],
        )
        gaps = [item for item in report["findings"] if item["id"] == "runtime-capability.missing"]
        self.assertEqual(len(gaps), 1)
        self.assertEqual(gaps[0]["action"], "route")
        self.assertEqual(gaps[0]["details"]["missing"], ["accessibility-tree", "screenshot"])
        self.assertFalse(report["valid"])

    def test_commit_count_never_becomes_truth_drift_evidence(self):
        report = diagnose_runtime_state(ROOT, commit_count=1000000)
        ids = {item["id"] for item in report["findings"]}
        self.assertNotIn("truth-drift", " ".join(ids))
        self.assertEqual(report["commit_count_note"], "informational-only")


if __name__ == "__main__":
    unittest.main()
