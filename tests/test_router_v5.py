import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_mandatory_routes

class RouterV5Tests(unittest.TestCase):
    def test_exceptional_visual_freedom_cannot_save_context_by_skipping_visual_spine(self):
        profile={
            'platform_surfaces':['web'],'input_modalities':['pointer','keyboard'],'ai_role':'none','risk_class':'routine','temporal_behaviors':[],
            'visual_ambition':'exceptional','visual_freedom':'high','material_data_visualization':True,
            'aspirational_identity':True,'magnitude_language':True,'product_wide':True,
        }
        result=validate_mandatory_routes(profile,[])
        for skill in ('preserving-experiential-intent','directing-visual-ambition','exploring-aesthetic-directions','researching-visual-references','engineering-visual-legibility','critiquing-aesthetic-adequacy','escaping-aesthetic-basins','proving-visual-encoding-semantics','modeling-aspirational-identity','composing-spatial-dramaturgy','evaluating-perceptual-diversity'):
            self.assertIn(skill,result['missing_routes'],(skill,result))

    def test_utilitarian_task_does_not_route_entire_aesthetic_spine(self):
        profile={'platform_surfaces':['web'],'input_modalities':['pointer'],'ai_role':'none','risk_class':'routine','temporal_behaviors':[],'visual_ambition':'utilitarian'}
        result=validate_mandatory_routes(profile,[])
        self.assertNotIn('critiquing-aesthetic-adequacy',result['required_routes'])
        self.assertNotIn('escaping-aesthetic-basins',result['required_routes'])

if __name__=='__main__': unittest.main()
