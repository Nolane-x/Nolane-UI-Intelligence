import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src/nolane_ui/validators.py"
MANIFEST = json.loads((ROOT / "knowledge/emerging-skill-manifest.json").read_text(encoding="utf-8"))
CASES = json.loads((ROOT / "evals/v2/coverage/emerging-domains.json").read_text(encoding="utf-8"))["cases"]
GRAPH = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))["skills"]


def load_validators():
    spec = importlib.util.spec_from_file_location("nui_emerging_validators", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class EmergingUICoverageTests(unittest.TestCase):
    def test_emerging_skills_are_declared_and_deep(self):
        for item in MANIFEST["skills"]:
            self.assertIn(item["name"], GRAPH, f"emerging skill {item['name']} missing from graph")
            path = ROOT / "skills" / item["name"] / "SKILL.md"
            self.assertTrue(path.is_file(), f"missing emerging skill {item['name']}")
            text = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(re.findall(r"\b[\w'-]+\b", text)), 260)
            for heading in ("## Parent Contract", "## Decision Model", "## Evidence", "## Output Contract", "## Failure Traps"):
                self.assertIn(heading, text)
            self.assertIn(item["output"], text)

    def test_emerging_profiles_have_mandatory_routes(self):
        module = load_validators()
        for case in CASES:
            result = module.validate_mandatory_routes(case["profile"], [])
            self.assertFalse(result["valid"])
            self.assertTrue(set(case["required_skills"]).issubset(set(result["missing_routes"])), (case, result))


if __name__ == "__main__":
    unittest.main()
