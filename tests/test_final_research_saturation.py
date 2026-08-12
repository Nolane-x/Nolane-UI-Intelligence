import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FinalResearchSaturationTests(unittest.TestCase):
    def test_saturation_is_bounded_and_evidence_complete(self):
        record = json.loads((ROOT / "knowledge/research-saturation.json").read_text(encoding="utf-8"))
        self.assertEqual(record["decision"], "SATURATED")
        self.assertIn("as_of", record)
        self.assertGreaterEqual(len(record.get("reopen_conditions", [])), 5)
        for dimension in ("breadth", "depth", "contradictions", "novelty", "freshness"):
            evidence = record["evidence"][dimension]
            self.assertEqual(evidence["status"], "PASS", dimension)
            self.assertTrue(evidence["criterion"].strip())
            self.assertTrue(evidence["observed"].strip())

    def test_final_sweep_records_decomposition_instead_of_false_new_skills(self):
        path = ROOT / "knowledge/final-saturation-evidence.json"
        self.assertTrue(path.is_file(), "final saturation evidence is missing")
        evidence = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(evidence["decision"], "NO_NEW_NONDECOMPOSABLE_OWNER")
        self.assertGreaterEqual(len(evidence.get("sweeps", [])), 5)
        final = evidence["sweeps"][-1]
        self.assertEqual(final["new_owner_count"], 0)
        self.assertGreaterEqual(len(final.get("decomposition_checks", [])), 6)
        for check in final["decomposition_checks"]:
            self.assertTrue(check.get("source_id"))
            self.assertTrue(check.get("mapped_skills"))
            self.assertTrue(check.get("reason"))


if __name__ == "__main__":
    unittest.main()
