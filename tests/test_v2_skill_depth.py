import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "knowledge/v2-skill-manifest.json").read_text(encoding="utf-8"))


class V2SkillDepthTests(unittest.TestCase):
    def test_manifest_ownership_is_unique_and_specific(self):
        ownership = [item["ownership"].strip().lower() for item in MANIFEST["skills"]]
        self.assertEqual(len(ownership), len(set(ownership)), "v2 skills may not share duplicated ownership text")
        for item in MANIFEST["skills"]:
            self.assertGreaterEqual(len(item["ownership"].split()), 7, f"{item['name']} ownership is too vague")

    def test_every_v2_skill_is_substantive(self):
        required_sections = ("## Parent Contract", "## Decision Model", "## Evidence", "## Output Contract", "## Failure Traps")
        for item in MANIFEST["skills"]:
            path = ROOT / "skills" / item["name"] / "SKILL.md"
            self.assertTrue(path.is_file(), f"missing v2 skill {item['name']}")
            text = path.read_text(encoding="utf-8")
            words = re.findall(r"\b[\w'-]+\b", text)
            self.assertGreaterEqual(len(words), 260, f"{item['name']} is too shallow: {len(words)} words")
            for section in required_sections:
                self.assertIn(section, text, f"{item['name']} missing {section}")
            self.assertIn(item["parent"], text, f"{item['name']} does not bind its declared parent")
            self.assertIn(item["output"], text, f"{item['name']} does not name its typed output")


if __name__ == "__main__":
    unittest.main()
