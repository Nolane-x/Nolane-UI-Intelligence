import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_v5_completion_evidence


def evidence():
    return {
      'visual_ambition':'exceptional','visual_freedom':'high','product_wide':True,'material_data_visualization':True,
      'functional_closure':{'status':'PASS'},'ui_specification':{'status':'IMPLEMENTABLE'},
      'experiential_intent':{'status':'PASS'},'visual_ambition_contract':{'status':'PASS'},
      'divergence_evidence':{'status':'PASS','candidate_count':3,'materially_distinct':True,'rendered_evidence':True},
      'reference_frontier':{'status':'PASS'},'visual_legibility_evidence':{'status':'PASS'},
      'aesthetic_attractor_audit':{'status':'PASS'},'signature_depth_contract':{'status':'PASS'},
      'visual_energy_evidence':{'status':'PASS'},'aesthetic_adequacy':{'status':'PASS'},
      'aesthetic_basin_decision':{'decision':'REFINE'},'encoding_provenance':{'status':'PASS'},
      'perceptual_diversity':{'status':'PASS'},
    }

class CompletionV5Tests(unittest.TestCase):
    def test_render_health_alone_cannot_pass_exceptional_objective(self):
        r=validate_v5_completion_evidence({'visual_ambition':'exceptional','visual_freedom':'high','code_tests':{'status':'PASS'},'render_checks':{'status':'PASS'},'browser_errors':0})
        self.assertEqual(r['decision'],'BLOCKED')
        self.assertTrue(any('experiential intent' in x.lower() for x in r['errors']),r)

    def test_high_freedom_requires_three_materially_distinct_candidates(self):
        x=evidence(); x['divergence_evidence']={'status':'PASS','candidate_count':2,'materially_distinct':True,'rendered_evidence':True}
        r=validate_v5_completion_evidence(x); self.assertEqual(r['decision'],'BLOCKED'); self.assertTrue(any('three' in e.lower() for e in r['errors']),r)

    def test_rediverge_blocks_release_even_if_other_evidence_passes(self):
        x=evidence(); x['aesthetic_basin_decision']={'decision':'RE_DIVERGE'}
        r=validate_v5_completion_evidence(x); self.assertEqual(r['decision'],'BLOCKED'); self.assertTrue(any('re-divergence' in e.lower() for e in r['errors']),r)

    def test_complete_high_ambition_evidence_passes_v5_gate(self):
        r=validate_v5_completion_evidence(evidence()); self.assertEqual(r['decision'],'PASS',r)

if __name__=='__main__': unittest.main()
