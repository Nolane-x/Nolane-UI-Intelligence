import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class V5EvalIntegrityTests(unittest.TestCase):
 def test_v5_eval_manifest_and_cases_cover_four_behavior_planes(self):
  manifest=json.loads((ROOT/'evals/v5/manifest.json').read_text())
  self.assertEqual(manifest['version'],5)
  self.assertEqual(len(manifest['assets']),4)
  total=0; ids=set()
  graph=set(json.loads((ROOT/'skills/skill-graph.json').read_text())['skills'])
  for rel in manifest['assets']:
   doc=json.loads((ROOT/rel).read_text()); self.assertEqual(doc['version'],5)
   for case in doc['cases']:
    total+=1; self.assertNotIn(case['id'],ids); ids.add(case['id'])
    self.assertGreaterEqual(len(case['required_skills']),1)
    self.assertFalse(set(case['required_skills'])-graph,(case['id'],set(case['required_skills'])-graph))
    self.assertGreaterEqual(len(case['must_find']),2)
  self.assertEqual(total,manifest['case_count']); self.assertGreaterEqual(total,28)
  self.assertIn('v5-atlas-green-runtime-affective-fail',ids)

 def test_semantic_mutations_are_detection_mapped(self):
  doc=json.loads((ROOT/'evals/v5/semantic-mutations/cases.json').read_text())
  mutations={c['mutation'] for c in doc['cases']}
  for x in ('DO NOT→ALWAYS','must→may','preserve→discard','independent→self','minimum→maximum'):
   self.assertIn(x,mutations)
  for c in doc['cases']:
   self.assertTrue(c.get('target_skill')); self.assertTrue(c.get('detected_by')); self.assertEqual(c.get('expected'),'FAIL')

 def test_skill_interactions_are_factorial_not_single_skill_smoke_tests(self):
  doc=json.loads((ROOT/'evals/v5/skill-interactions/cases.json').read_text())
  for c in doc['cases']:
   self.assertGreaterEqual(len(c['required_skills']),2,c['id'])
   self.assertIn('baseline',c); self.assertIn('combined',c); self.assertTrue(c.get('objective_delta_reviewed'))

 def test_craft_distribution_breaks_restraint_house_style(self):
  doc=json.loads((ROOT/'evals/v5/craft-distribution/cases.json').read_text())
  regimes={c['visual_regime'] for c in doc['cases']}
  expected={'expressive operational','luxury scientific','cinematic professional','playful expert','editorial analytical','tactile creative','organic biotech','monumental command','warm medical','bright high-tech'}
  self.assertTrue(expected.issubset(regimes),expected-regimes)

 def test_aesthetic_excellence_vector_is_separate_from_specificity(self):
  rubric=json.loads((ROOT/'evals/rubric.json').read_text())
  q=rubric['quality_dimensions']
  self.assertIn('aesthetic-specificity',q); self.assertIn('aesthetic-excellence',q)
  self.assertIn('aesthetic_excellence_vector',rubric)
  self.assertGreaterEqual(len(rubric['aesthetic_excellence_vector']),9)

 def test_v5_schemas_exist_for_evidence_boundaries(self):
  for name in ('experiential-intent','visual-ambition-contract','aesthetic-quality-evidence','encoding-provenance','workspace-visual-matrix','skill-interaction-evidence'):
   doc=json.loads((ROOT/'schemas'/f'{name}.schema.json').read_text())
   self.assertEqual(doc.get('$schema'),'https://json-schema.org/draft/2020-12/schema')
   self.assertEqual(doc.get('type'),'object')
   self.assertTrue(doc.get('required'),name)
if __name__=='__main__': unittest.main()
