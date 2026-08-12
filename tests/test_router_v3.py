import unittest
from nolane_ui.validators import validate_mandatory_routes

class RouterV3Tests(unittest.TestCase):
    def test_product_wide_requires_closure_plane(self):
        profile={'scope':'multi-feature-product','delivery_stage':'verify','platform_surfaces':['web'],'input_modalities':['pointer','keyboard'],'ai_role':'none','risk_class':'routine','temporal_behaviors':[]}
        r=validate_mandatory_routes(profile, [])
        required={'inventorying-product-capabilities','registering-ui-actions','proving-interface-reachability','covering-product-scenarios','compiling-ui-implementation-specifications','critiquing-functional-completeness','verifying-runtime-ui-behavior'}
        self.assertTrue(required.issubset(set(r['missing_routes'])), r)

    def test_visual_evidence_iteration_routes_learning_loop(self):
        profile={'visual_evidence_iteration':True,'platform_surfaces':['web'],'input_modalities':['pointer'],'ai_role':'none','risk_class':'routine','temporal_behaviors':[]}
        r=validate_mandatory_routes(profile, [])
        required={'researching-visual-references','iterating-rendered-visual-design','maintaining-project-design-memory'}
        self.assertTrue(required.issubset(set(r['missing_routes'])), r)

if __name__=='__main__': unittest.main()
