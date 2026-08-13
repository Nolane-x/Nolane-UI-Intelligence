import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from nolane_ui.source_intelligence import validate_source_intelligence_registry


class V6AnchorSourceProvenanceTests(unittest.TestCase):
    def test_registry_has_diverse_sha_pinned_artifact_level_anchors(self):
        registry = json.loads((ROOT / 'knowledge/ui-source-intelligence-v6.json').read_text())
        anchors = [s for s in registry['sources'] if s.get('tier') == 'anchor']
        roles = {s.get('role') for s in anchors}
        required_roles = {
            'animated-component-gallery',
            'icon-system',
            'design-token-tool',
            'design-system',
            'accessibility-testing-tool',
            'diagram-graph-ui',
            'visual-testing-tool',
            'typography-source',
        }
        self.assertTrue(required_roles <= roles, (required_roles - roles, roles))
        self.assertGreaterEqual(len(anchors), 8)
        for source in anchors:
            provenance = source.get('provenance', {})
            snapshot = str(provenance.get('snapshot_ref', ''))
            self.assertRegex(snapshot, r'^[0-9a-f]{40}$', source['id'])
            artifacts = provenance.get('inspected_artifacts', [])
            self.assertGreaterEqual(len(artifacts), 4, source['id'])
            classes = {a.get('class') for a in artifacts}
            self.assertIn('implementation', classes, source['id'])
            self.assertTrue({'test', 'runtime-evidence', 'example'} & classes, source['id'])
            self.assertTrue(all(str(a.get('finding', '')).strip() for a in artifacts), source['id'])

    def test_registry_validator_rejects_missing_required_anchor_role(self):
        registry = json.loads((ROOT / 'knowledge/ui-source-intelligence-v6.json').read_text())
        candidate = deepcopy(registry)
        required_ids = {
            'react-bits', 'lucide', 'style-dictionary', 'spectrum-web-components',
            'axe-core', 'xyflow', 'storybook', 'fontsource',
        }
        for source in candidate['sources']:
            if source.get('id') in required_ids:
                source['tier'] = 'anchor'
                source.pop('live_verification_required', None)
                source['provenance'] = {
                    'verified_at': '2026-08-13',
                    'snapshot_ref': 'a' * 40,
                    'inspected_artifacts': [
                        {'path': 'src/core', 'class': 'implementation', 'finding': 'mechanism'},
                        {'path': 'tests/core', 'class': 'test', 'finding': 'behavior'},
                        {'path': 'docs/core', 'class': 'guidance', 'finding': 'contract'},
                        {'path': 'package.json', 'class': 'dependency-config', 'finding': 'delivery'},
                    ],
                }
        self.assertTrue(validate_source_intelligence_registry(candidate)['valid'])
        for source in candidate['sources']:
            if source.get('id') == 'lucide':
                source['tier'] = 'specialist'
                source['live_verification_required'] = True
                break
        result = validate_source_intelligence_registry(candidate)
        self.assertFalse(result['valid'], result)
        self.assertTrue(any('anchor role' in e.lower() for e in result['errors']), result)


if __name__ == '__main__':
    unittest.main()
