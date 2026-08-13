import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))

class UIEcosystemTests(unittest.TestCase):
    def setUp(self):
        from nolane_ui.ecosystem import validate_ui_ecosystem_registry, query_ui_ecosystem, validate_reference_ledger, validate_source_selection, validate_rich_interaction_contract
        self.validate_registry=validate_ui_ecosystem_registry; self.query=query_ui_ecosystem; self.validate_ledger=validate_reference_ledger; self.validate_selection=validate_source_selection; self.validate_rich=validate_rich_interaction_contract
        self.registry=json.loads((ROOT/'knowledge/ui-ecosystem-registry.json').read_text())
    def test_registry_is_typed_and_has_broad_category_coverage(self):
        r=self.validate_registry(self.registry)
        self.assertTrue(r['valid'],r)
        self.assertGreaterEqual(r['source_count'],40)
        self.assertGreaterEqual(r['category_count'],12)
    def test_react_animated_adapt_query_surfaces_react_bits_without_popularity_authority(self):
        r=self.query(self.registry,{'capabilities':['animated-components'],'stacks':['react'],'intent':'adapt'})
        ids=[x['id'] for x in r['matches']]
        self.assertIn('react-bits',ids)
        self.assertNotIn('stars', r['ranking_factors'])
    def test_adopt_or_adapt_blocks_unresolved_license_or_missing_inspection(self):
        bad={'decision':'adapt','source_id':'x','license_posture':'unresolved','inspected':['readme'],'citations':['https://example.test']}
        r=self.validate_selection(bad)
        self.assertFalse(r['valid']); self.assertTrue(any('license' in e.lower() for e in r['errors']))
        bad['license_posture']='verified-compatible'; bad['inspected']=['readme','license']
        r=self.validate_selection(bad); self.assertFalse(r['valid']); self.assertTrue(any('implementation' in e.lower() for e in r['errors']))
    def test_popularity_only_selection_is_rejected(self):
        r=self.validate_selection({'decision':'adapt','source_id':'react-bits','license_posture':'verified-compatible','inspected':['readme','license','implementation'],'citations':['https://github.com/DavidHDev/react-bits'],'rationale':['stars']})
        self.assertFalse(r['valid']); self.assertTrue(any('popularity' in e.lower() for e in r['errors']))
    def test_material_reference_ledger_requires_citation_and_mechanism_boundary(self):
        r=self.validate_ledger({'references':[{'source_id':'react-bits','url':'https://github.com/DavidHDev/react-bits','mechanism':'shared layout morph','usage':'adapt','inspected':['README.md']} ]})
        self.assertFalse(r['valid']); self.assertTrue(any('adaptation boundary' in e.lower() for e in r['errors']))
    def test_rich_interaction_requires_reduced_motion_keyboard_and_exit_strategy(self):
        base={'states':['idle','active','interrupted','complete'],'modalities':['pointer','keyboard'],'reduced_motion':'preserve information without transform motion','interruptible':True,'retargetable':True,'focus_behavior':'stable','performance_budget':'60fps target with measured fallback','ssr_strategy':'stable server markup; measure after hydration','exit_strategy':'remove enhancement without losing task'}
        self.assertTrue(self.validate_rich(base)['valid'])
        for key in ('reduced_motion','exit_strategy'):
            bad=copy.deepcopy(base); bad.pop(key); self.assertFalse(self.validate_rich(bad)['valid'])

if __name__=='__main__': unittest.main()
