import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_v6_completion_evidence


def base():
 return {'visual_ambition':'polished','functional_closure':{'status':'PASS'},'ui_specification':{'status':'IMPLEMENTABLE'}}

class CompletionV6Tests(unittest.TestCase):
 def test_material_external_source_requires_deep_research_and_audit(self):
  x=base(); x.update({'external_source_usage':'adapt','external_source_count':1})
  r=validate_v6_completion_evidence(x)
  self.assertEqual(r['decision'],'BLOCKED')
  self.assertTrue(any('source research' in e.lower() for e in r['errors']))
  self.assertTrue(any('research depth' in e.lower() for e in r['errors']))

 def test_multiple_sources_require_cross_source_synthesis(self):
  x=base(); x.update({'external_source_usage':'adapt','external_source_count':2,'source_research':{'status':'PASS'},'research_depth_audit':{'status':'PASS'}})
  r=validate_v6_completion_evidence(x)
  self.assertEqual(r['decision'],'BLOCKED'); self.assertTrue(any('cross-source synthesis' in e.lower() for e in r['errors']))

 def test_cross_axis_high_risk_requires_ontology_coverage(self):
  x=base(); x['high_risk_interaction_cell']=True
  r=validate_v6_completion_evidence(x)
  self.assertEqual(r['decision'],'BLOCKED'); self.assertTrue(any('ontology' in e.lower() for e in r['errors']))

 def test_skill_effect_claim_requires_bounded_benchmark(self):
  x=base(); x['claim_skill_effect']=True; x['skill_effect_benchmark']={'status':'INCONCLUSIVE'}
  r=validate_v6_completion_evidence(x)
  self.assertEqual(r['decision'],'BLOCKED')
  x['skill_effect_benchmark']={'status':'SUPPORTED','lineage_recorded':True,'controls_present':True,'falsifiers_declared':True}
  r=validate_v6_completion_evidence(x); self.assertEqual(r['decision'],'PASS',r)

 def test_complete_material_multi_source_evidence_passes(self):
  x=base(); x.update({'external_source_usage':'adapt','external_source_count':3,'source_research':{'status':'PASS'},'research_depth_audit':{'status':'PASS'},'source_mix':{'status':'PASS'},'cross_source_synthesis':{'status':'PASS'}})
  r=validate_v6_completion_evidence(x); self.assertEqual(r['decision'],'PASS',r)

if __name__=='__main__':unittest.main()
