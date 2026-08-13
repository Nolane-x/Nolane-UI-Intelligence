import json, shutil, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_repository

class V5RepositoryGateTests(unittest.TestCase):
 def _copy(self):
  t=tempfile.TemporaryDirectory(); d=Path(t.name)/'repo'; shutil.copytree(ROOT,d,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc','milestone-artifacts')); return t,d
 def test_current_repository_passes_v5_gate_and_reports_behavioral_metrics(self):
  r=validate_repository(ROOT); self.assertTrue(r['valid'],r)
  self.assertEqual(r['metrics']['v5_skill_count'],13)
  self.assertGreaterEqual(r['metrics']['v5_adversarial_cases'],28)
  self.assertGreaterEqual(r['metrics']['skill_contracts_checked'],154)
  self.assertEqual(r['metrics']['v5_semantic_mutations'],5)
  self.assertGreaterEqual(r['metrics']['v5_skill_interactions'],5)
 def test_removing_v5_manifest_or_eval_fails_repository(self):
  for rel in ('knowledge/v5-skill-manifest.json','evals/v5/manifest.json','schemas/experiential-intent.schema.json'):
   t,d=self._copy()
   try:
    (d/rel).unlink(); r=validate_repository(d); self.assertFalse(r['valid'],rel); self.assertTrue(any(rel in e for e in r['errors']),r)
   finally:t.cleanup()
 def test_v5_graph_contract_drift_fails_repository(self):
  t,d=self._copy()
  try:
   p=d/'skills/skill-graph.json'; g=json.loads(p.read_text()); g['skills']['critiquing-aesthetic-adequacy']['output']='wrong-output'; p.write_text(json.dumps(g,indent=2)+'\n')
   r=validate_repository(d); self.assertFalse(r['valid']); self.assertTrue(any('critiquing-aesthetic-adequacy' in e for e in r['errors']),r)
  finally:t.cleanup()
if __name__=='__main__': unittest.main()
