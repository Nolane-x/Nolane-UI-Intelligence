import json,shutil,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.validators import validate_repository

class V6RepositoryGateTests(unittest.TestCase):
 def _copy(self):
  t=tempfile.TemporaryDirectory(); d=Path(t.name)/'repo'; shutil.copytree(ROOT,d,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc','milestone-artifacts')); return t,d
 def test_current_repository_passes_v6_gate_and_reports_deep_metrics(self):
  r=validate_repository(ROOT); self.assertTrue(r['valid'],r)
  m=r['metrics']; self.assertEqual(m['v6_skill_count'],4); self.assertEqual(m['skill_count'],158)
  self.assertGreaterEqual(m['v6_source_count'],75); self.assertGreaterEqual(m['v6_source_domain_count'],20)
  self.assertGreaterEqual(m['v6_ontology_axes'],15); self.assertGreaterEqual(m['v6_ontology_values'],100); self.assertGreaterEqual(m['v6_interaction_cells'],18)
  self.assertGreaterEqual(m['v6_adversarial_cases'],32); self.assertEqual(m['v6_depth_dimensions'],10)
 def test_removing_v6_plane_fails(self):
  for rel in ('knowledge/ui-source-intelligence-v6.json','knowledge/ui-industry-ontology-v6.json','knowledge/skill-depth-constitution-v6.json','evals/v6/manifest.json','knowledge/v6-skill-manifest.json'):
   t,d=self._copy()
   try:
    (d/rel).unlink(); r=validate_repository(d); self.assertFalse(r['valid'],rel); self.assertTrue(any(rel in e for e in r['errors']),r)
   finally:t.cleanup()
 def test_v6_graph_drift_fails(self):
  t,d=self._copy()
  try:
   p=d/'skills/skill-graph.json'; g=json.loads(p.read_text()); g['skills']['performing-ui-repository-archaeology']['output']='wrong'; p.write_text(json.dumps(g,indent=2)+'\n')
   r=validate_repository(d); self.assertFalse(r['valid']); self.assertTrue(any('performing-ui-repository-archaeology' in e for e in r['errors']),r)
  finally:t.cleanup()
 def test_depth_lock_must_exactly_cover_graph_and_use_five_unique_anchors(self):
  t,d=self._copy()
  try:
   p=d/'knowledge/v6-depth-focus-obligations.json'; x=json.loads(p.read_text()); x['skills'].pop('designing-navigation'); p.write_text(json.dumps(x,indent=2)+'\n')
   r=validate_repository(d); self.assertFalse(r['valid']); self.assertTrue(any('depth focus' in e.lower() and 'cover' in e.lower() for e in r['errors']),r)
  finally:t.cleanup()
if __name__=='__main__':unittest.main()
