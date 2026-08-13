import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

class AuthorityV7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from nolane_ui.authority import resolve_authorities, validate_authority_mesh, validate_authority_route_plan
        cls.resolve = staticmethod(resolve_authorities)
        cls.validate_mesh = staticmethod(validate_authority_mesh)
        cls.validate_plan = staticmethod(validate_authority_route_plan)
        cls.mesh = json.loads((ROOT / 'knowledge/ui-authority-mesh-v7.json').read_text())

    def test_mesh_is_valid_and_decision_dimensional(self):
        r = self.validate_mesh(self.mesh)
        self.assertTrue(r['valid'], r)
        self.assertGreaterEqual(r['authority_count'], 16)
        self.assertGreaterEqual(r['dimension_count'], 10)
        self.assertTrue(all('authority_dimensions' in a for a in self.mesh['authorities']))

    def test_apple_native_platform_outranks_generic_visual_preference(self):
        r = self.resolve({'platform':'ios','decision_dimensions':['platform-convention','visual-craft']}, self.mesh)
        self.assertEqual(r['primary']['platform-convention']['source_id'], 'apple-hig')
        self.assertNotEqual(r['primary']['platform-convention']['source_id'], 'nui-internal-aesthetic')

    def test_public_service_routes_service_and_accessibility_authorities(self):
        r = self.resolve({'domain':'public-service','decision_dimensions':['service-journey','accessibility-testing']}, self.mesh)
        self.assertIn(r['primary']['service-journey']['source_id'], {'govuk-design-system','uswds'})
        self.assertIn(r['primary']['accessibility-testing']['source_id'], {'uswds','react-aria'})

    def test_component_semantics_never_routes_visual_gallery_as_primary(self):
        r = self.resolve({'decision_dimensions':['component-semantics'], 'stack':'react'}, self.mesh)
        self.assertIn(r['primary']['component-semantics']['source_id'], {'react-aria','radix-primitives'})
        self.assertNotIn(r['primary']['component-semantics']['source_id'], {'react-bits','magic-ui','aceternity'})

    def test_enterprise_workflow_prefers_lived_enterprise_authority(self):
        r = self.resolve({'domain':'enterprise-operations','decision_dimensions':['enterprise-workflow']}, self.mesh)
        self.assertIn(r['primary']['enterprise-workflow']['source_id'], {'sap-fiori','ant-design','carbon'})

    def test_shopify_authority_is_scoped_to_shopify_context(self):
        shopify = self.resolve({'domain':'commerce','platform':'shopify-admin','decision_dimensions':['commerce-workflow']}, self.mesh)
        generic = self.resolve({'domain':'commerce','decision_dimensions':['commerce-workflow']}, self.mesh)
        self.assertEqual(shopify['primary']['commerce-workflow']['source_id'], 'shopify-polaris')
        self.assertNotEqual(generic['primary']['commerce-workflow']['source_id'], 'shopify-polaris')

    def test_visual_frontier_is_inspiration_not_semantic_authority(self):
        r = self.resolve({'visual_ambition':'exceptional','decision_dimensions':['visual-frontier','component-semantics']}, self.mesh)
        self.assertIn(r['primary']['visual-frontier']['source_id'], {'react-bits','magic-ui','aceternity'})
        self.assertIn(r['primary']['component-semantics']['source_id'], {'react-aria','radix-primitives'})

    def test_agent_adapter_access_does_not_raise_authority(self):
        r = self.resolve({'decision_dimensions':['agent-readable-access','component-semantics'], 'stack':'react'}, self.mesh)
        self.assertIn(r['primary']['agent-readable-access']['source_id'], {'primer-mcp','mantine-agent-docs','carbon-mcp','shadcn-open-code'})
        self.assertIn(r['primary']['component-semantics']['source_id'], {'react-aria','radix-primitives'})

    def test_route_plan_validator_rejects_authority_smear(self):
        plan = {
            'status':'PASS',
            'decisions':[
                {'dimension':'component-semantics','source_id':'magic-ui','role':'visual-inspiration','reason':'looks good'}
            ],
            'conflicts':[],
            'live_verification':[]
        }
        r = self.validate_plan(plan, mesh=self.mesh)
        self.assertFalse(r['valid'])
        self.assertTrue(any('semantic' in e.lower() or 'authority' in e.lower() for e in r['errors']))

if __name__ == '__main__':
    unittest.main()
