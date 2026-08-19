import json
import unittest
from pathlib import Path
from nolane_ui.validators import validate_repository

ROOT=Path(__file__).resolve().parents[1]

class V8RepositoryTests(unittest.TestCase):
    def test_graph_retains_historical_v8_baseline(self):
        g=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']; self.assertGreaterEqual(len(g),174)
    def test_manifest_has_eight_owners(self):
        m=json.loads((ROOT/'knowledge/v8-skill-manifest.json').read_text()); self.assertEqual(len(m['skills']),8)
    def test_depth_union_is_174(self):
        a=json.loads((ROOT/'knowledge/v6-depth-focus-obligations.json').read_text())['skills']; b=json.loads((ROOT/'knowledge/v8-depth-obligations.json').read_text())['skills']; self.assertEqual(len(set(a)|set(b)),174)
    def test_tool_sources_are_14(self):
        a=json.loads((ROOT/'knowledge/tool-learning-sources-v8.json').read_text())['sources']; b=json.loads((ROOT/'knowledge/tool-learning-sources-v8-extension.json').read_text())['sources']; self.assertGreaterEqual(len(a)+len(b),14)
    def test_media_sources_are_14(self):
        a=json.loads((ROOT/'knowledge/visual-media-sources-v8.json').read_text())['sources']; b=json.loads((ROOT/'knowledge/visual-media-sources-v8-extension.json').read_text())['sources']; self.assertGreaterEqual(len(a)+len(b),14)
    def test_creative_tools_are_14(self):
        a=json.loads((ROOT/'knowledge/creative-toolchain-v8.json').read_text())['tools']; b=json.loads((ROOT/'knowledge/creative-toolchain-v8-extension.json').read_text())['tools']; self.assertGreaterEqual(len(a)+len(b),14)
    def test_flagship_synthesis_is_deep_without_adding_duplicate_owner(self):
        k=json.loads((ROOT/'knowledge/flagship-visual-synthesis-v8.json').read_text())
        self.assertEqual(len(k['planes']),12)
        self.assertGreaterEqual(len(k['anti_generic_attractors']),6)
        self.assertGreaterEqual(len(k['perceptual_tests']),7)
        m=json.loads((ROOT/'knowledge/v8-skill-manifest.json').read_text())
        self.assertEqual(len(m['skills']),8)
    def test_repository_gate_passes(self):
        r=validate_repository(ROOT); self.assertTrue(r['valid'],r)

if __name__=='__main__': unittest.main()
