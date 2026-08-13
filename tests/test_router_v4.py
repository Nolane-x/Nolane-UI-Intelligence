import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_mandatory_routes
class RouterV4Tests(unittest.TestCase):
 def test_external_rich_react_ui_routes_ecosystem_and_integration(self):
  p={'platform_surfaces':['web'],'input_modalities':['pointer','keyboard'],'ai_role':'none','risk_class':'routine','temporal_behaviors':[],'external_ui_sources':True,'rich_interaction':True,'stack':'react','adoption_intent':'adapt'}
  r=validate_mandatory_routes(p,[]); req={'researching-ui-implementation-ecosystems','selecting-ui-building-blocks','adapting-external-ui-patterns','engineering-rich-interactive-components','auditing-ui-library-integration'}; self.assertTrue(req.issubset(set(r['missing_routes'])),r)
 def test_named_repo_reference_still_requires_research_and_audit(self):
  p={'platform_surfaces':['web'],'input_modalities':['pointer'],'ai_role':'none','risk_class':'routine','temporal_behaviors':[],'named_ui_source':'react-bits','adoption_intent':'inspire'}
  r=validate_mandatory_routes(p,[]); self.assertIn('researching-ui-implementation-ecosystems',r['missing_routes']); self.assertIn('selecting-ui-building-blocks',r['missing_routes'])
if __name__=='__main__':unittest.main()
