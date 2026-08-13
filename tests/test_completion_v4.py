import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_v4_completion_evidence
class CompletionV4Tests(unittest.TestCase):
 def test_external_adaptation_blocks_without_integration_audit_and_reference_ledger(self):
  r=validate_v4_completion_evidence({'external_ui_used':True,'adoption_intent':'adapt','source_selection':{'status':'PASS'}}); self.assertEqual(r['decision'],'BLOCKED')
 def test_rich_interaction_blocks_without_local_runtime_evidence(self):
  r=validate_v4_completion_evidence({'rich_interaction':True,'rich_interaction_contract':{'status':'PASS'}}); self.assertEqual(r['decision'],'BLOCKED')
 def test_complete_evidence_passes(self):
  r=validate_v4_completion_evidence({'external_ui_used':True,'adoption_intent':'adapt','source_selection':{'status':'PASS'},'reference_ledger':{'status':'PASS'},'adaptation_contract':{'status':'PASS'},'integration_audit':{'status':'PASS'},'rich_interaction':True,'rich_interaction_contract':{'status':'PASS'},'behavior_verification':{'status':'PASS'}}); self.assertEqual(r['decision'],'PASS')
if __name__=='__main__':unittest.main()
