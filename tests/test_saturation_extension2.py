import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.validators import validate_industry_atlas, validate_mandatory_routes, validate_source_ledger

MANIFEST = json.loads((ROOT / "knowledge/emerging-skill-manifest-2.json").read_text(encoding="utf-8"))
GRAPH_DOC = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))
GRAPH = GRAPH_DOC["skills"]


class SaturationExtensionTwoTests(unittest.TestCase):
    def test_new_standardized_ui_domains_have_deep_owner_skills(self):
        for item in MANIFEST["skills"]:
            self.assertIn(item["name"], GRAPH, f"graph missing {item['name']}")
            path = ROOT / "skills" / item["name"] / "SKILL.md"
            self.assertTrue(path.is_file(), f"missing {item['name']}")
            text = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(re.findall(r"\b[\w'-]+\b", text)), 260)
            for heading in ("## Parent Contract", "## Decision Model", "## Evidence", "## Output Contract", "## Failure Traps"):
                self.assertIn(heading, text)
            self.assertIn(item["output"], text)

    def test_extension_two_atlas_and_sources_are_machine_validated(self):
        atlas_path = ROOT / "knowledge/ui-domain-atlas-emerging-2.json"
        ledger_path = ROOT / "knowledge/source-ledger-emerging-2.json"
        self.assertTrue(atlas_path.is_file(), "extension-two atlas missing")
        self.assertTrue(ledger_path.is_file(), "extension-two source ledger missing")
        atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertTrue(validate_industry_atlas(atlas, GRAPH_DOC)["valid"])
        self.assertTrue(validate_source_ledger(ledger, as_of="2026-08-12")["valid"])

    def test_specialized_domain_profiles_have_non_optional_routes(self):
        cases = [
            (
                {"specialized_ui_domains": ["affective-adaptive"], "platform_surfaces": ["web"], "input_modalities": ["pointer"], "ai_role": "none", "risk_class": "privacy-sensitive", "temporal_behaviors": []},
                {"designing-affective-adaptive-interfaces", "designing-permissions-and-consent", "designing-privacy-sensitive-interfaces", "critiquing-security-and-privacy"},
            ),
            (
                {"specialized_ui_domains": ["avatar-embodied"], "platform_surfaces": ["spatial-xr"], "input_modalities": ["gaze", "hand-gesture"], "ai_role": "none", "risk_class": "routine", "temporal_behaviors": []},
                {"designing-avatar-embodied-representation", "critiquing-security-and-privacy", "critiquing-accessibility"},
            ),
            (
                {"specialized_ui_domains": ["aac-communication"], "platform_surfaces": ["mobile"], "input_modalities": ["alternative-input"], "ai_role": "none", "risk_class": "routine", "temporal_behaviors": []},
                {"designing-accessible-interfaces", "designing-aac-communication-interfaces", "critiquing-accessibility"},
            ),
        ]
        for profile, required in cases:
            result = validate_mandatory_routes(profile, selected_skills=[])
            self.assertFalse(result["valid"])
            self.assertTrue(required.issubset(set(result["missing_routes"])), (profile, result))


if __name__ == "__main__":
    unittest.main()
