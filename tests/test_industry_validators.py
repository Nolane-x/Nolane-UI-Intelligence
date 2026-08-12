import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "nolane_ui" / "validators.py"
ATLAS = json.loads((ROOT / "knowledge/ui-domain-atlas.json").read_text(encoding="utf-8"))
LEDGER = json.loads((ROOT / "knowledge/source-ledger.json").read_text(encoding="utf-8"))
SATURATION = json.loads((ROOT / "knowledge/research-saturation.json").read_text(encoding="utf-8"))
GRAPH = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))


def load_validators():
    spec = importlib.util.spec_from_file_location("nui_validators_v2_tests", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class IndustryValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validators = load_validators()

    def require(self, name):
        self.assertTrue(hasattr(self.validators, name), f"validators.{name} is not implemented")
        return getattr(self.validators, name)

    def test_atlas_rejects_unowned_or_unverified_mandatory_cell(self):
        fn = self.require("validate_industry_atlas")
        atlas = copy.deepcopy(ATLAS)
        atlas["coverage_cells"][0]["owner_skills"] = []
        result = fn(atlas, GRAPH)
        self.assertFalse(result["valid"])
        self.assertTrue(any("owner" in error.lower() for error in result["errors"]))

    def test_source_ledger_rejects_unknown_authority_and_stale_high_drift(self):
        fn = self.require("validate_source_ledger")
        ledger = copy.deepcopy(LEDGER)
        ledger["sources"][0]["authority"] = "influencer-opinion"
        ledger["sources"][1]["drift"] = "very-high"
        ledger["sources"][1]["reviewed_at"] = "2025-01-01"
        result = fn(ledger, as_of="2026-08-12")
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("authority", joined)
        self.assertIn("stale", joined)

    def test_research_saturation_rejects_false_saturated_claim(self):
        fn = self.require("validate_research_saturation")
        record = copy.deepcopy(SATURATION)
        record["decision"] = "SATURATED"
        record["evidence"]["novelty"]["status"] = "IN_PROGRESS"
        result = fn(record, LEDGER, ATLAS, as_of="2026-08-12")
        self.assertFalse(result["valid"])
        self.assertTrue(any("saturat" in error.lower() or "novelty" in error.lower() for error in result["errors"]))

    def test_mandatory_routes_reject_omission_for_automotive_agentic_and_medical(self):
        fn = self.require("validate_mandatory_routes")
        profiles = [
            ({"platform_surfaces":["automotive"], "driving_context":"driving", "input_modalities":["voice"], "ai_role":"none", "risk_class":"safety-critical", "temporal_behaviors":[]},
             {"designing-automotive-interfaces", "engineering-human-factors", "critiquing-human-factors-and-safety"}),
            ({"platform_surfaces":["web"], "input_modalities":["keyboard"], "ai_role":"agentic", "risk_class":"security-sensitive", "temporal_behaviors":["streaming"]},
             {"designing-human-ai-interaction", "designing-agent-autonomy-and-control", "designing-ai-uncertainty-and-provenance", "critiquing-ai-trust-and-agency"}),
            ({"platform_surfaces":["desktop"], "input_modalities":["pointer"], "ai_role":"none", "risk_class":"medical", "temporal_behaviors":["realtime"]},
             {"designing-medical-safety-critical-ui", "engineering-human-factors", "designing-high-stakes-decisions", "critiquing-human-factors-and-safety"}),
        ]
        for profile, expected in profiles:
            result = fn(profile, selected_skills=[])
            self.assertFalse(result["valid"])
            self.assertTrue(expected.issubset(set(result["missing_routes"])), (profile, result))

    def test_mandatory_routes_accept_complete_spatial_profile(self):
        fn = self.require("validate_mandatory_routes")
        profile = {"platform_surfaces":["spatial-xr"], "input_modalities":["gaze","hand-gesture"], "ai_role":"none", "risk_class":"routine", "temporal_behaviors":[]}
        selected = ["designing-spatial-xr-interfaces", "designing-gaze-hand-spatial-input", "critiquing-platform-fit", "critiquing-input-modality"]
        result = fn(profile, selected)
        self.assertTrue(result["valid"], result)


if __name__ == "__main__":
    unittest.main()
