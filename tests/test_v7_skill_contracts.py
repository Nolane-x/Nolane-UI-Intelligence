import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
V7={
'routing-to-ui-authorities':('routing-ui-work','ui-authority-route-plan'),
'compiling-concrete-design-packets':('routing-to-ui-authorities','concrete-design-packet'),
'adapting-institutional-design-knowledge':('synthesizing-cross-source-ui-language','institutional-knowledge-synthesis'),
'orchestrating-implementation-authorities':('selecting-ui-building-blocks','implementation-authority-plan'),
'validating-rendered-perception':('iterating-rendered-visual-design','rendered-perception-evidence'),
'designing-domain-native-signatures':('deepening-signature-mechanisms','domain-signature-brief'),
'building-agent-readable-ui-context':('performing-ui-repository-archaeology','agent-readable-ui-context'),
'compressing-ui-decisions-for-execution':('compiling-ui-implementation-specifications','ui-execution-brief')}
class V7SkillContractsTests(unittest.TestCase):
 def test_manifest(self):
  m=json.loads((ROOT/'knowledge/v7-skill-manifest.json').read_text()); self.assertEqual(m['version'],7); self.assertEqual({x['name'] for x in m['skills']},set(V7))
 def test_graph_preserves_v7(self):
  g=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']; self.assertGreaterEqual(len(g),166)
  for n,(p,o) in V7.items(): self.assertEqual((g[n]['parent'],g[n]['output']),(p,o))
 def test_v7_documents_keep_behavior(self):
  for n in V7:
   t=(ROOT/'skills'/n/'SKILL.md').read_text().lower(); self.assertIn('falsif',t); self.assertIn('recovery',t); self.assertIn('output contract',t)
 def test_outputs_unique(self): self.assertEqual(len(V7),len({x[1] for x in V7.values()}))
 def test_depth_subset(self):
  d=json.loads((ROOT/'knowledge/v6-depth-focus-obligations.json').read_text())['skills']; g=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']
  self.assertEqual(len(d),166); self.assertTrue(set(d).issubset(g)); self.assertTrue(all(len(x)==5 for x in d.values()))
if __name__=='__main__': unittest.main()
