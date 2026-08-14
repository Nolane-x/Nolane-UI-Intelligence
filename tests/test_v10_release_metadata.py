import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V10ReleaseMetadataTests(unittest.TestCase):
    def test_workflow_packages_v10_artifacts(self):
        workflow = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("nui-v10-completion-packet", workflow)
        self.assertIn("Nolane-UI-Intelligence-v10-complete.zip", workflow)
        self.assertIn("nui-v10-complete-project", workflow)
        self.assertNotIn("nui-v9-completion-packet", workflow)
        self.assertNotIn("Nolane-UI-Intelligence-v9-complete.zip", workflow)

    def test_release_packet_is_v10_and_keeps_empirical_claim_bounded(self):
        script = (ROOT / "scripts/nui-release-packet").read_text(encoding="utf-8")
        self.assertIn("NUI-V10-STRUCTURAL", script)
        self.assertIn("validate_v10_completion_evidence", script)
        self.assertIn('"claim_ceiling":"STRUCTURAL_ONLY"', script.replace(" ", ""))
        self.assertIn('"empirical_runs_executed":False', script.replace(" ", ""))


if __name__ == "__main__":
    unittest.main()
