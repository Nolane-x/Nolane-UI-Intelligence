import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'knowledge/v3-skill-manifest.json').read_text(encoding='utf-8'))
GRAPH = json.loads((ROOT / 'skills/skill-graph.json').read_text(encoding='utf-8'))['skills']

REQUIRED_HEADINGS = (
    '## Decision Boundary', '## Product Truth', '## Decision Model',
    '## Evidence', '## Output Contract', '## Failure Traps',
)

class V3SkillDepthTests(unittest.TestCase):
    def test_manifest_has_ten_unique_decision_owners(self):
        items = MANIFEST['skills']
        self.assertEqual(len(items), 10)
        self.assertEqual(len({x['name'] for x in items}), 10)
        self.assertEqual(len({x['ownership'].strip().lower() for x in items}), 10)

    def test_every_v3_skill_is_deep_and_graph_canonical(self):
        for item in MANIFEST['skills']:
            path = ROOT / 'skills' / item['name'] / 'SKILL.md'
            self.assertTrue(path.is_file(), f"missing v3 skill {item['name']}")
            text = path.read_text(encoding='utf-8')
            words = re.findall(r"\b[\w'-]+\b", text)
            self.assertGreaterEqual(len(words), 700, f"{item['name']} too shallow: {len(words)} words")
            for heading in REQUIRED_HEADINGS:
                self.assertIn(heading, text, f"{item['name']} missing {heading}")
            self.assertIn(f"`{item['output']}`", text)
            self.assertIn(f"`{item['parent']}`", text)
            self.assertIn(item['name'], GRAPH)
            node = GRAPH[item['name']]
            self.assertEqual(node['parent'], item['parent'])
            self.assertEqual(node['output'], item['output'])
            self.assertEqual(node['family'], item['family'])

if __name__ == '__main__':
    unittest.main()
