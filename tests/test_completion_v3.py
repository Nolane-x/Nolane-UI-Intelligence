import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.validators import validate_v3_completion_evidence


class CompletionV3Tests(unittest.TestCase):
    def test_beauty_cannot_compensate_for_failed_closure(self):
        result = validate_v3_completion_evidence({
            "product_wide": True,
            "visual_score": 100,
            "functional_closure": {"status": "FAIL"},
            "ui_specification": {"status": "IMPLEMENTABLE"},
        })
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertTrue(any("closure" in error.lower() for error in result["errors"]))

    def test_complete_product_wide_runtime_and_visual_evidence_passes(self):
        result = validate_v3_completion_evidence({
            "product_wide": True,
            "claims_runtime_behavior": True,
            "visual_evidence_iteration": True,
            "functional_closure": {"status": "PASS"},
            "ui_specification": {"status": "IMPLEMENTABLE"},
            "behavior_verification": {"status": "PASS"},
            "visual_iteration_evidence": {"status": "PASS"},
        })
        self.assertEqual(result["decision"], "PASS")


if __name__ == "__main__":
    unittest.main()
