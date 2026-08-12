import unittest
from nolane_ui.validators import validate_v3_completion_evidence

class CompletionV3Tests(unittest.TestCase):
    def test_beauty_cannot_compensate_for_failed_closure(self):
        r=validate_v3_completion_evidence({'product_wide':True,'visual_score':100,'functional_closure':{'status':'FAIL'},'ui_specification':{'status':'IMPLEMENTABLE'}})
        self.assertEqual(r['decision'],'BLOCKED')
        self.assertTrue(any('closure' in e.lower() for e in r['errors']))

    def test_complete_product_wide_runtime_and_visual_evidence_passes(self):
        r=validate_v3_completion_evidence({'product_wide':True,'claims_runtime_behavior':True,'visual_evidence_iteration':True,'functional_closure':{'status':'PASS'},'ui_specification':{'status':'IMPLEMENTABLE'},'behavior_verification':{'status':'PASS'},'visual_iteration_evidence':{'status':'PASS'}})
        self.assertEqual(r['decision'],'PASS')

if __name__=='__main__': unittest.main()
