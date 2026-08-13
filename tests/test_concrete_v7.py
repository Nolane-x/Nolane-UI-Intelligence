import json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.authority import resolve_authorities

class ConcreteV7Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  from nolane_ui.concrete import compile_concrete_design_packet, validate_pattern_kb, validate_concrete_design_packet
  cls.compile=staticmethod(compile_concrete_design_packet); cls.validate_kb=staticmethod(validate_pattern_kb); cls.validate_packet=staticmethod(validate_concrete_design_packet)
  cls.mesh=json.loads((ROOT/'knowledge/ui-authority-mesh-v7.json').read_text())
  cls.kb=json.loads((ROOT/'knowledge/concrete-design-patterns-v7.json').read_text())
  cls.grammar=json.loads((ROOT/'knowledge/immediate-synthesis-grammar-v7.json').read_text())

 def packet(self, profile):
  dims=profile.setdefault('decision_dimensions', self.grammar['dimension_defaults'].get(profile.get('domain','generic'), self.grammar['dimension_defaults']['generic']))
  auth=resolve_authorities(profile,self.mesh)
  return self.compile(profile,auth,self.kb,self.grammar)

 def test_pattern_kb_is_concrete_and_source_bound(self):
  r=self.validate_kb(self.kb); self.assertTrue(r['valid'],r)
  self.assertGreaterEqual(r['pattern_count'],30)
  self.assertGreaterEqual(r['domain_count'],10)

 def test_public_service_packet_returns_service_evidence_patterns(self):
  p=self.packet({'domain':'public-service','jurisdiction':'uk','task':'benefit eligibility application','user_needs':['low vision','error recovery']})
  ids={d['pattern_id'] for d in p['decisions']}
  self.assertIn('service-eligibility-before-application',ids)
  self.assertTrue(any('research' in x.lower() or 'assistive' in x.lower() for x in p['validation_obligations']))

 def test_ios_packet_contains_platform_harmony_not_generic_web_defaults(self):
  p=self.packet({'domain':'consumer-productivity','platform':'ios','task':'document scanner','visual_ambition':'flagship'})
  ids={d['pattern_id'] for d in p['decisions']}
  self.assertIn('platform-hardware-software-harmony',ids)
  self.assertFalse(any(d.get('source_id')=='ui-ux-pro-max' and d.get('decision_type')=='visual-style-default' for d in p['decisions']))

 def test_enterprise_packet_is_role_task_and_state_aware(self):
  p=self.packet({'domain':'enterprise-operations','task':'approve purchase orders','roles':['requester','approver'],'risk_class':'financial'})
  ids={d['pattern_id'] for d in p['decisions']}
  self.assertTrue({'enterprise-role-task-slice','enterprise-draft-message-state'} & ids)
  self.assertTrue(any('state' in x.lower() for x in p['validation_obligations']))

 def test_shopify_pattern_does_not_leak_to_generic_commerce(self):
  shop=self.packet({'domain':'commerce','platform':'shopify-admin','task':'manage orders'})
  generic=self.packet({'domain':'commerce','task':'manage orders'})
  self.assertTrue(any(d['pattern_id'].startswith('shopify-') for d in shop['decisions']))
  self.assertFalse(any(d['pattern_id'].startswith('shopify-') for d in generic['decisions']))

 def test_fast_packet_is_bounded_but_not_empty(self):
  p=self.packet({'domain':'ai-collaboration','task':'review AI generated project plan','ai_experience':True,'visual_ambition':'polished'})
  self.assertGreaterEqual(len(p['decisions']),5)
  self.assertLessEqual(len(p['decisions']),9)
  self.assertTrue(p['task_thesis'])
  self.assertTrue(p['authority_stack'])
  self.assertTrue(p['implementation_shortcuts'])

 def test_unresolved_authority_survives_as_blocker_not_guess(self):
  profile={'domain':'unknown-exotic','decision_dimensions':['nonexistent-decision-axis'],'task':'novel interface'}
  auth=resolve_authorities(profile,self.mesh)
  p=self.compile(profile,auth,self.kb,self.grammar)
  self.assertIn('nonexistent-decision-axis',p['unresolved_blockers'][0])
  self.assertNotEqual(p['status'],'READY')

 def test_packet_validator_rejects_decision_without_provenance_or_contraindication(self):
  p={'status':'READY','task_thesis':'x','authority_stack':[{'dimension':'visual-craft','source_id':'x'}],
     'decisions':[{'pattern_id':'bad','decision':'use blue cards','rationale':'nice'}],
     'implementation_shortcuts':['x'],'validation_obligations':['x'],'unresolved_blockers':[]}
  r=self.validate_packet(p); self.assertFalse(r['valid'])
  self.assertTrue(any('provenance' in e.lower() or 'contraind' in e.lower() for e in r['errors']))

if __name__=='__main__': unittest.main()
