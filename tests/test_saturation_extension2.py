import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "knowledge/emerging-skill-manifest-2.json").read_text(encoding="utf-8"))
GRAPH = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))["skills"]


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


if __name__ == "__main__":
    unittest.main()
