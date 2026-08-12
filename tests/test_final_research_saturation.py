import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui import validators

SATURATION = json.loads((ROOT / "knowledge/research-saturation.json").read_text(encoding="utf-8"))
FINAL = json.loads((ROOT / "knowledge/final-saturation-evidence.json").read_text(encoding="utf-8"))
GRAPH = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))


class FinalResearchSaturationTests(unittest.TestCase):
    def test_saturation_is_bounded_and_evidence_complete(self):
        record = SATURATION
        self.assertEqual(record["decision"], "SATURATED")
        self.assertIn("as_of", record)
        self.assertGreaterEqual(len(record.get("reopen_conditions", [])), 5)
        for dimension in ("breadth", "depth", "contradictions", "novelty", "freshness"):
            evidence = record["evidence"][dimension]
            self.assertEqual(evidence["status"], "PASS", dimension)
            self.assertTrue(evidence["criterion"].strip())
            self.assertTrue(evidence["observed"].strip())

    def test_final_sweep_records_decomposition_instead_of_false_new_skills(self):
        evidence = FINAL
        self.assertEqual(evidence["decision"], "NO_NEW_NONDECOMPOSABLE_OWNER")
        self.assertGreaterEqual(len(evidence.get("sweeps", [])), 5)
        final = evidence["sweeps"][-1]
        self.assertEqual(final["new_owner_count"], 0)
        self.assertGreaterEqual(len(final.get("decomposition_checks", [])), 6)
        for check in final["decomposition_checks"]:
            self.assertTrue(check.get("source_id"))
            self.assertTrue(check.get("mapped_skills"))
            self.assertTrue(check.get("reason"))

    def test_validator_rejects_saturated_claim_without_final_zero_novelty_evidence(self):
        self.assertTrue(hasattr(validators, "validate_bounded_saturation"), "bounded saturation validator is missing")
        evidence = copy.deepcopy(FINAL)
        evidence["sweeps"][-1]["new_owner_count"] = 1
        result = validators.validate_bounded_saturation(SATURATION, evidence)
        self.assertFalse(result["valid"])
        self.assertTrue(any("new_owner_count" in error or "novel" in error.lower() for error in result["errors"]))

    def test_validator_rejects_saturated_claim_with_nonpass_dimension_or_weak_reopen_policy(self):
        self.assertTrue(hasattr(validators, "validate_bounded_saturation"), "bounded saturation validator is missing")
        record = copy.deepcopy(SATURATION)
        record["evidence"]["depth"]["status"] = "IN_PROGRESS"
        record["reopen_conditions"] = ["something changes"]
        result = validators.validate_bounded_saturation(record, FINAL)
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("depth", joined)
        self.assertIn("reopen", joined)

    def test_final_sweep_source_and_skill_references_are_real(self):
        final_ledger_path = ROOT / "knowledge/source-ledger-final-sweep.json"
        self.assertTrue(final_ledger_path.is_file(), "final sweep source ledger is missing")
        ledger_paths = [
            ROOT / "knowledge/source-ledger.json",
            ROOT / "knowledge/source-ledger-emerging.json",
            ROOT / "knowledge/source-ledger-emerging-2.json",
            ROOT / "knowledge/source-ledger-emerging-3.json",
            ROOT / "knowledge/source-ledger-emerging-4.json",
            final_ledger_path,
        ]
        source_ids = {
            source["id"]
            for path in ledger_paths
            for source in json.loads(path.read_text(encoding="utf-8"))["sources"]
        }
        skill_names = set(GRAPH["skills"])
        result = validators.validate_bounded_saturation(
            SATURATION, FINAL, source_ids=source_ids, skill_names=skill_names
        )
        self.assertTrue(result["valid"], result)

        fake_source = copy.deepcopy(FINAL)
        fake_source["sweeps"][-1]["decomposition_checks"][0]["source_id"] = "invented-source"
        result = validators.validate_bounded_saturation(
            SATURATION, fake_source, source_ids=source_ids, skill_names=skill_names
        )
        self.assertFalse(result["valid"])
        self.assertTrue(any("source" in error.lower() for error in result["errors"]))

        fake_skill = copy.deepcopy(FINAL)
        fake_skill["sweeps"][-1]["decomposition_checks"][0]["mapped_skills"] = ["invented-skill"]
        result = validators.validate_bounded_saturation(
            SATURATION, fake_skill, source_ids=source_ids, skill_names=skill_names
        )
        self.assertFalse(result["valid"])
        self.assertTrue(any("skill" in error.lower() for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
