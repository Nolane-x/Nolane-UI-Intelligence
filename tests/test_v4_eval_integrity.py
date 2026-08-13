import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class V4EvalIntegrityTests(unittest.TestCase):
 def test_v4_manifest_discovers_all_assets_and_fourteen_distinct_failures(self):
  m=json.loads((ROOT/'evals/v4/manifest.json').read_text()); self.assertEqual(m['case_count'],14); self.assertEqual(m['assets'],['evals/v4/ecosystem/cases.json'])
  data=json.loads((ROOT/m['assets'][0]).read_text()); cases=data['cases']; self.assertEqual(len(cases),14); self.assertEqual(len({x['id'] for x in cases}),14); self.assertEqual(len({x['failure'] for x in cases}),14)
  for c in cases: self.assertTrue(c['required_skills']); self.assertGreaterEqual(len(c['must_find']),2)
if __name__=='__main__':unittest.main()
