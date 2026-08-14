import unittest
from pathlib import Path
from nolane_ui.validators import validate_repository

ROOT=Path(__file__).resolve().parents[1]

class V7RepositoryGateTests(unittest.TestCase):
    def test_current_repository_preserves_v7_metrics(self):
        r=validate_repository(ROOT)
        self.assertTrue(r['valid'],r)
        m=r['metrics']
        self.assertGreaterEqual(m.get('skill_count',0),166)
        self.assertEqual(m['v7_skill_count'],8)
        self.assertEqual(m['v7_adversarial_cases'],32)
        self.assertGreaterEqual(m['v7_authority_count'],20)
        self.assertGreaterEqual(m['v7_pattern_count'],35)
        self.assertGreaterEqual(m['v7_perception_planes'],8)

    def test_v7_artifacts_remain_present(self):
        for rel in (
            'knowledge/ui-authority-mesh-v7.json',
            'knowledge/concrete-design-patterns-v7.json',
            'knowledge/v7-skill-manifest.json',
            'src/nolane_ui/perceptual.py',
            'evals/v7/manifest.json',
            'artifacts/v7-completion-packet.example.json',
        ):
            self.assertTrue((ROOT/rel).is_file(),rel)

    def test_v7_validator_snapshot_remains_present(self):
        self.assertTrue((ROOT/'src/nolane_ui/validators_v7.py').is_file())

if __name__=='__main__':
    unittest.main()
