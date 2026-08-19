import unittest
from pathlib import Path

from nolane_ui.v9_repository import extend
from nolane_ui.validators import validate_repository

ROOT = Path(__file__).resolve().parents[1]


class V9RepositoryTests(unittest.TestCase):
    def test_v9_extension_accepts_repository(self):
        result = extend(ROOT, {"valid": True, "errors": [], "warnings": [], "metrics": {}})
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["metrics"]["skill_count"], 174)
        self.assertGreaterEqual(result["metrics"]["v9_benchmark_references"], 12)
        self.assertGreaterEqual(result["metrics"]["v9_domain_signatures"], 8)
        self.assertGreaterEqual(result["metrics"]["v9_adversarial_cases"], 24)

    def test_public_repository_validator_includes_v9_gate(self):
        result = validate_repository(ROOT)
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["metrics"]["nui_major"], 9)
        self.assertGreaterEqual(result["metrics"]["v9_benchmark_references"], 12)
        self.assertGreaterEqual(result["metrics"]["v9_domain_signatures"], 8)
        self.assertGreaterEqual(result["metrics"]["v9_adversarial_cases"], 24)


if __name__ == "__main__":
    unittest.main()
