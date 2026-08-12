import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


class SkillMetadataTests(unittest.TestCase):
    def test_every_graph_skill_has_a_skill_file(self):
        missing = []
        for name in GRAPH["skills"]:
            path = ROOT / "skills" / name / "SKILL.md"
            if not path.is_file():
                missing.append(name)
        self.assertEqual([], missing, f"graph nodes without SKILL.md: {missing}")

    def test_skill_frontmatter_is_discoverable(self):
        failures = []
        for name in GRAPH["skills"]:
            path = ROOT / "skills" / name / "SKILL.md"
            if not path.is_file():
                continue
            meta = parse_frontmatter(path.read_text(encoding="utf-8"))
            if meta.get("name") != name:
                failures.append(f"{name}: frontmatter name mismatch")
            description = meta.get("description", "")
            if not description.startswith("Use when"):
                failures.append(f"{name}: description must start with Use when")
            if len(description) > 500:
                failures.append(f"{name}: description exceeds 500 characters")
        self.assertEqual([], failures)

    def test_non_root_skills_declare_parent_contract(self):
        failures = []
        for name, node in GRAPH["skills"].items():
            if node.get("parent") is None:
                continue
            path = ROOT / "skills" / name / "SKILL.md"
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            if "## Parent Contract" not in text:
                failures.append(f"{name}: missing Parent Contract")
            if node["parent"] not in text:
                failures.append(f"{name}: parent {node['parent']} not named")
        self.assertEqual([], failures)

    def test_no_placeholders_or_soft_completion_language(self):
        banned = re.compile(r"\b(TODO|TBD|fill this in|implement later)\b", re.I)
        failures = []
        for name in GRAPH["skills"]:
            path = ROOT / "skills" / name / "SKILL.md"
            if path.is_file() and banned.search(path.read_text(encoding="utf-8")):
                failures.append(name)
        self.assertEqual([], failures, f"placeholder language found in: {failures}")


if __name__ == "__main__":
    unittest.main()
