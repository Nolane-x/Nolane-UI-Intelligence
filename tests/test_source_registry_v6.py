import copy, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.source_intelligence import validate_source_intelligence_registry

REGISTRY=json.loads((ROOT/'knowledge/ui-source-intelligence-v6.json').read_text()) if (ROOT/'knowledge/ui-source-intelligence-v6.json').exists() else None

class SourceRegistryV6Tests(unittest.TestCase):
    def test_registry_covers_missing_industry_source_classes(self):
        self.assertIsNotNone(REGISTRY, 'v6 registry must exist')
        result=validate_source_intelligence_registry(REGISTRY)
        self.assertTrue(result['valid'], result['errors'])
        self.assertGreaterEqual(result['source_count'], 75)
        required={'motion','component-semantics','design-systems','data-visualization','rich-editing','canvas','3d-spatial','mobile','icons','typography','design-tokens','visual-testing','accessibility-testing','graph-diagram','geospatial','code-editor','terminal-ui','ai-native-ui','creative-rendering','animation-assets'}
        self.assertTrue(required.issubset(set(result['domains'])), required-set(result['domains']))

    def test_source_requires_research_map_and_adaptation_boundary(self):
        bad={'version':6,'sources':[{'id':'x','name':'x','url':'https://example.com','role':'icon-system','tier':'specialist','domains':['icons'],'capabilities':['icons'],'stacks':['web'],'drift':'high','license':{'status':'unknown'},'mechanism_families':['symbol grammar'],'provenance':{}}]}
        result=validate_source_intelligence_registry(bad)
        self.assertFalse(result['valid'])
        self.assertTrue(any('research_map' in e for e in result['errors']))
        self.assertTrue(any('adaptation_boundary' in e for e in result['errors']))

    def test_anchor_requires_artifact_level_provenance(self):
        source=copy.deepcopy(REGISTRY['sources'][0])
        source['tier']='anchor'; source['provenance']={'verified_at':'2026-08-13','inspected':['repository','readme','license']}
        result=validate_source_intelligence_registry({'version':6,'sources':[source]})
        self.assertFalse(result['valid'])
        self.assertTrue(any('anchor' in e.lower() and 'artifact' in e.lower() for e in result['errors']))

    def test_invalid_tier_and_duplicate_id_are_rejected(self):
        source=copy.deepcopy(REGISTRY['sources'][0]); source['tier']='best'
        result=validate_source_intelligence_registry({'version':6,'sources':[source,copy.deepcopy(source)]})
        self.assertFalse(result['valid'])
        self.assertTrue(any('tier' in e for e in result['errors']))
        self.assertTrue(any('duplicate source id' in e for e in result['errors']))

    def test_react_bits_is_not_authorized_by_readme_alone(self):
        rb=next(s for s in REGISTRY['sources'] if s['id']=='react-bits')
        self.assertIn('component-source', rb['research_map']['required_for_adapt'])
        self.assertIn('motion-behavior', rb['research_map']['required_for_adapt'])
        self.assertTrue(rb['live_verification_required'])
        self.assertNotEqual(rb['tier'],'discovery')

if __name__=='__main__': unittest.main()
