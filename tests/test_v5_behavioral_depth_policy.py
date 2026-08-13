import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class V5BehavioralDepthPolicyTests(unittest.TestCase):
 def test_historical_skill_depth_tests_no_longer_use_token_length_as_depth(self):
  for rel in ('tests/test_v2_skill_depth.py','tests/test_v3_skill_depth.py','tests/test_v4_skill_depth.py'):
   text=(ROOT/rel).read_text(encoding='utf-8')
   self.assertNotIn('len(words)',text,rel)
   self.assertNotIn('findall',text,rel)
if __name__=='__main__': unittest.main()
