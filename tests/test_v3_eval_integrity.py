import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GRAPH=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']
class V3EvalIntegrityTests(unittest.TestCase):
    def test_v3_eval_manifest_discovers_all_assets_and_cases(self):
        root=ROOT/'evals/v3'; manifest=json.loads((root/'manifest.json').read_text())
        paths=[x['path'] for x in manifest['assets']]
        discovered={str(p.relative_to(ROOT)).replace('\\','/') for p in root.rglob('*.json') if p.name!='manifest.json'}
        self.assertEqual(set(paths),discovered)
        total=0; ids=[]
        for path in paths:
            doc=json.loads((ROOT/path).read_text()); self.assertEqual(doc.get('version'),3)
            for case in doc.get('cases',[]):
                total+=1; ids.append(case['id'])
                self.assertGreaterEqual(len(case.get('failure','').split()),6)
                required=case.get('required_skills',[]); self.assertTrue(required)
                self.assertEqual(sorted(set(required)-set(GRAPH)),[])
                self.assertGreaterEqual(len(case.get('must_find',[])),2)
        self.assertGreaterEqual(total,17)
        self.assertEqual(len(ids),len(set(ids)))
if __name__=='__main__': unittest.main()
