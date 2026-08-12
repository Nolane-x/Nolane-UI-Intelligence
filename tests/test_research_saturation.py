import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ResearchSaturationContractTests(unittest.TestCase):
    def test_research_ledgers_exist(self):
        for relative in (
            "knowledge/source-ledger.json",
            "knowledge/research-radar.json",
            "knowledge/research-saturation.json",
        ):
            self.assertTrue((ROOT / relative).is_file(), f"missing {relative}")

    def test_saturation_record_contains_falsifiable_dimensions(self):
        path = ROOT / "knowledge/research-saturation.json"
        self.assertTrue(path.is_file(), "research saturation record is missing")
        record = json.loads(path.read_text(encoding="utf-8"))
        evidence = record.get("evidence", {})
        for key in ("breadth", "depth", "contradictions", "novelty", "freshness"):
            self.assertIn(key, evidence, f"saturation record missing {key} evidence")
        self.assertIn(record.get("decision"), {"OPEN", "SATURATED"})
        self.assertTrue(record.get("as_of"), "saturation decision must be timestamp-bounded")


if __name__ == "__main__":
    unittest.main()
