import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.validators import validate_industry_atlas, validate_mandatory_routes, validate_source_ledger

MANIFEST = json.loads((ROOT / "knowledge/emerging-skill-manifest-3.json").read_text(encoding="utf-8"))
GRAPH_DOC = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))
GRAPH = GRAPH_DOC["skills"]


class SaturationExtensionThreeTests(unittest.TestCase):
    def test_third_extension_has_deep_owner_skills(self):
        for item in MANIFEST["skills"]:
            self.assertIn(item["name"], GRAPH, f"graph missing {item['name']}")
            path = ROOT / "skills" / item["name"] / "SKILL.md"
            self.assertTrue(path.is_file(), f"missing {item['name']}")
            text = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(re.findall(r"\b[\w'-]+\b", text)), 260)
            for heading in ("## Parent Contract", "## Decision Model", "## Evidence", "## Output Contract", "## Failure Traps"):
                self.assertIn(heading, text)
            self.assertIn(item["output"], text)

    def test_third_extension_atlas_and_ledger_validate(self):
        atlas_path = ROOT / "knowledge/ui-domain-atlas-emerging-3.json"
        ledger_path = ROOT / "knowledge/source-ledger-emerging-3.json"
        self.assertTrue(atlas_path.is_file(), "extension-three atlas missing")
        self.assertTrue(ledger_path.is_file(), "extension-three source ledger missing")
        atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertTrue(validate_industry_atlas(atlas, GRAPH_DOC)["valid"])
        self.assertTrue(validate_source_ledger(ledger, as_of="2026-08-12")["valid"])

    def test_third_extension_profiles_are_hard_routed(self):
        cases = [
            ({"specialized_ui_domains":["cross-device-action-equivalence"],"platform_surfaces":["web","mobile"],"input_modalities":["pointer","touch"],"ai_role":"none","risk_class":"routine","temporal_behaviors":[]},{"designing-cross-device-action-equivalence","adapting-platform-conventions","critiquing-input-modality"}),
            ({"specialized_ui_domains":["accessibility-settings"],"platform_surfaces":["desktop"],"input_modalities":["keyboard","alternative-input"],"ai_role":"none","risk_class":"routine","temporal_behaviors":[]},{"designing-accessible-interfaces","designing-accessibility-settings-and-profiles","critiquing-accessibility"}),
            ({"specialized_ui_domains":["accessible-media"],"platform_surfaces":["web"],"input_modalities":["keyboard"],"ai_role":"none","risk_class":"routine","temporal_behaviors":["streaming"]},{"designing-accessible-media-alternatives","critiquing-accessibility"}),
            ({"specialized_ui_domains":["sign-language-presentation"],"platform_surfaces":["tv-ten-foot"],"input_modalities":["remote"],"ai_role":"none","risk_class":"routine","temporal_behaviors":["streaming"]},{"designing-accessible-media-alternatives","designing-sign-language-presentation","critiquing-accessibility"}),
        ]
        for profile, required in cases:
            result = validate_mandatory_routes(profile, selected_skills=[])
            self.assertFalse(result["valid"])
            self.assertTrue(required.issubset(set(result["missing_routes"])), (profile, result))


if __name__ == "__main__":
    unittest.main()
