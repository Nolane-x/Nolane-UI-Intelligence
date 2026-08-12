import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui import validators

RADAR = json.loads((ROOT / "knowledge/research-radar.json").read_text(encoding="utf-8"))
LEDGERS = [
    json.loads((ROOT / "knowledge/source-ledger.json").read_text(encoding="utf-8")),
    json.loads((ROOT / "knowledge/source-ledger-emerging.json").read_text(encoding="utf-8")),
    json.loads((ROOT / "knowledge/source-ledger-emerging-2.json").read_text(encoding="utf-8")),
    json.loads((ROOT / "knowledge/source-ledger-emerging-3.json").read_text(encoding="utf-8")),
    json.loads((ROOT / "knowledge/source-ledger-emerging-4.json").read_text(encoding="utf-8")),
    json.loads((ROOT / "knowledge/source-ledger-final-sweep.json").read_text(encoding="utf-8")),
]


class ResearchRadarTests(unittest.TestCase):
    def test_radar_covers_every_high_and_very_high_source_without_current_warnings(self):
        self.assertTrue(hasattr(validators, "validate_research_radar"), "research radar validator is missing")
        result = validators.validate_research_radar(RADAR, LEDGERS)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["missing_very_high_drift"], [])
        self.assertEqual(result["warnings"], [], result)

    def test_radar_rejects_missing_high_drift_watch_and_unknown_source(self):
        self.assertTrue(hasattr(validators, "validate_research_radar"), "research radar validator is missing")
        very_high = [
            source["id"]
            for ledger in LEDGERS
            for source in ledger["sources"]
            if source.get("drift") == "very-high"
        ]
        self.assertTrue(very_high, "fixture requires at least one very-high-drift source")
        radar = copy.deepcopy(RADAR)
        radar["watch"] = [item for item in radar["watch"] if item.get("source_id") != very_high[0]]
        radar["watch"].append({"source_id":"invented-source","cadence":"monthly","trigger":"anything","reason":"test"})
        result = validators.validate_research_radar(radar, LEDGERS)
        self.assertFalse(result["valid"])
        self.assertIn(very_high[0], result["missing_very_high_drift"])
        self.assertTrue(any("unknown source" in error.lower() for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
