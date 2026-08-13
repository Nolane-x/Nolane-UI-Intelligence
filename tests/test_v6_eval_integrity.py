import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.source_intelligence import validate_source_research_dossier, validate_source_mix, validate_cross_source_synthesis
from nolane_ui.depth import validate_industry_ontology

class V6EvalIntegrityTests(unittest.TestCase):
    def test_manifest_registers_four_planes_and_all_cases(self):
        m=json.loads((ROOT/'evals/v6/manifest.json').read_text())
        self.assertEqual(m['version'],6)
        self.assertEqual(len(m['assets']),4)
        cases=[]
        for rel in m['assets']:
            data=json.loads((ROOT/rel).read_text())
            self.assertEqual(data['version'],6)
            cases += data['cases']
        self.assertEqual(m['case_count'],len(cases))
        self.assertGreaterEqual(len(cases),32)
        self.assertEqual(len({c['id'] for c in cases}),len(cases))
        for c in cases:
            for field in ('id','required_skills','setup','pressure','expected_decision','evidence_requirements','evaluator_owner'):
                self.assertIn(field,c,c.get('id'))
            self.assertTrue(c['required_skills'])
            self.assertTrue(c['evidence_requirements'])

    def test_readme_only_eval_is_executable_against_source_validator(self):
        d={'source_id':'x','source_role':'animated-component-gallery','usage':'adapt','snapshot':{'canonical_url':'https://example.com/x','ref':'main','commit_sha':'abcdef1','retrieved_at':'2026-08-13'},'task_fit':{'need':'motion','why_this_source':'demo','source_role_fit':True},'inspected_artifacts':[{'kind':'readme','path':'README.md','finding':'claims','evidence_ref':'r'},{'kind':'license','path':'LICENSE','finding':'terms','evidence_ref':'l'}],'mechanisms':[],'license':{'evidence_refs':['l']},'accessibility':{'evidence_refs':['r']},'performance':{'evidence_refs':['r']},'unread_material':[],'stop_reason':'read docs'}
        r=validate_source_research_dossier(d,{'role':'animated-component-gallery','drift':'high','verify_live_before_use':True})
        self.assertFalse(r['valid']); self.assertTrue(any('README-only' in e for e in r['errors']))

    def test_gallery_monoculture_eval_is_executable(self):
        r=validate_source_mix({'visual_ambition':'exceptional','sources':[{'role':'animated-component-gallery'},{'role':'animated-component-gallery'},{'role':'animated-component-gallery'}]})
        self.assertFalse(r['valid'])

    def test_collage_eval_is_executable(self):
        r=validate_cross_source_synthesis({'sources':['a','b'],'layers':{'visual':{'owner':'a'}},'conflicts':[],'local_system':{}})
        self.assertFalse(r['valid'])

    def test_ontology_interaction_eval_is_executable(self):
        o=json.loads((ROOT/'knowledge/ui-industry-ontology-v6.json').read_text()); o['interaction_cells'][0]['verifier_skills']=[]
        skills=set(json.loads((ROOT/'skills/skill-graph.json').read_text())['skills'])
        r=validate_industry_ontology(o,skills)
        self.assertFalse(r['valid'])

if __name__=='__main__': unittest.main()
