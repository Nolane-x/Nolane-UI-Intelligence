import json
import shutil
import tempfile
import unittest
from pathlib import Path

from nolane_ui.validators import validate_repository


class RuleV13RepositoryIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def test_current_repository_reports_unified_v11_v12_v13_metrics(self):
        result = validate_repository(self.root)
        self.assertTrue(result["valid"], result["errors"])
        metrics = result["metrics"]
        self.assertEqual(metrics["package_version"], "0.13.0")
        self.assertEqual(metrics["config_version"], "0.13.0")
        self.assertGreater(metrics["v11_runtime_artifact_count"], 20)
        self.assertEqual(metrics["v12_reality_rule_count"], 75)
        self.assertGreaterEqual(metrics["v13_rule_count"], 89)
        self.assertEqual(metrics["v13_duplicate_pair_count"], 0)
        self.assertEqual(metrics["v13_boilerplate_cluster_count"], 0)
        self.assertEqual(metrics["v10_claim_ceiling"], "STRUCTURAL_ONLY")

    def test_version_mismatch_blocks_current_head_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "repo"
            shutil.copytree(self.root, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            config_path = target / "nui.config.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["version"] = "0.12.9"
            config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
            result = validate_repository(target)
            self.assertFalse(result["valid"])
            self.assertTrue(any("version coherence" in error.lower() for error in result["errors"]), result["errors"])

    def test_invalid_v13_provenance_blocks_current_head_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "repo"
            shutil.copytree(self.root, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            path = target / "knowledge" / "rule-provenance-v13.json"
            ledger = json.loads(path.read_text(encoding="utf-8"))
            ledger["records"][0]["evidence_class"] = "invented-authority"
            path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
            result = validate_repository(target)
            self.assertFalse(result["valid"])
            self.assertTrue(any("v13" in error.lower() and "provenance" in error.lower() for error in result["errors"]), result["errors"])

    def test_missing_v11_runtime_artifact_blocks_current_head_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "repo"
            shutil.copytree(self.root, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            (target / "knowledge" / "runtime-detector-rules-v11.json").unlink()
            result = validate_repository(target)
            self.assertFalse(result["valid"])
            self.assertTrue(any("v11 runtime" in error.lower() for error in result["errors"]), result["errors"])


if __name__ == "__main__":
    unittest.main()
