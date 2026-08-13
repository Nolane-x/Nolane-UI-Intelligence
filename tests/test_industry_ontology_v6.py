import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.depth import validate_industry_ontology

ONTO=json.loads((ROOT/'knowledge/ui-industry-ontology-v6.json').read_text()) if (ROOT/'knowledge/ui-industry-ontology-v6.json').exists() else None
GRAPH=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']

class IndustryOntologyV6Tests(unittest.TestCase):
    def test_full_ontology_has_mandatory_axes_and_interactions(self):
        self.assertIsNotNone(ONTO)
        result=validate_industry_ontology(ONTO,set(GRAPH))
        self.assertTrue(result['valid'],result['errors'])
        self.assertGreaterEqual(result['axis_count'],15)
        self.assertGreaterEqual(result['interaction_cell_count'],18)
        self.assertGreaterEqual(result['axis_value_count'],100)

    def test_missing_axis_fails(self):
        bad=copy.deepcopy(ONTO); bad['axes'].pop('aesthetic_art_direction_regimes')
        result=validate_industry_ontology(bad,set(GRAPH))
        self.assertFalse(result['valid']); self.assertTrue(any('aesthetic_art_direction_regimes' in e for e in result['errors']))

    def test_unknown_skill_fails(self):
        bad=copy.deepcopy(ONTO); bad['axis_obligations']['surfaces_platforms']['owner_skills']=['imaginary-skill']
        result=validate_industry_ontology(bad,set(GRAPH))
        self.assertFalse(result['valid']); self.assertTrue(any('imaginary-skill' in e for e in result['errors']))

    def test_owner_verifier_collision_fails(self):
        bad=copy.deepcopy(ONTO); owner=bad['axis_obligations']['surfaces_platforms']['owner_skills'][0]; bad['axis_obligations']['surfaces_platforms']['verifier_skills']=[owner]
        result=validate_industry_ontology(bad,set(GRAPH))
        self.assertFalse(result['valid']); self.assertTrue(any('independent' in e for e in result['errors']))

    def test_unowned_high_risk_interaction_fails(self):
        bad=copy.deepcopy(ONTO); bad['interaction_cells'][0]['owner_skills']=[]
        result=validate_industry_ontology(bad,set(GRAPH))
        self.assertFalse(result['valid']); self.assertTrue(any('interaction' in e and 'owner' in e for e in result['errors']))

if __name__=='__main__': unittest.main()
