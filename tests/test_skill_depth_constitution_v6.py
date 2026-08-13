import json,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.depth import audit_skill_depth, validate_skill_depth_record

class SkillDepthConstitutionV6Tests(unittest.TestCase):
    def complete_record(self, name='x'):
        dims={
          'ownership':{'evidence':'owns the source transfer decision','decision':'distinguish research discovery from transfer authorization'},
          'inputs_inherited_obligations':{'evidence':'receives task profile and parent obligations','decision':'preserve non-waivable parent constraints'},
          'observation_protocol':{'evidence':'inspect implementation, demos, tests and computed behavior','decision':'observe mechanism-bearing evidence before inference'},
          'branch_logic_tradeoffs':{'evidence':'if semantics conflict, prefer local authority; otherwise compare cost','decision':'branch by conflict and materiality'},
          'counterfactual_falsification':{'evidence':'remove the mechanism and test whether the product goal changes','decision':'reject causal stories that survive removal unchanged'},
          'evidence':{'evidence':'bind claims to artifact paths and runtime traces','decision':'no material claim without traceable evidence'},
          'output_semantics':{'evidence':'emit a typed decision record with unresolved conflicts','decision':'downstream agents receive explicit state rather than prose confidence'},
          'failure_topology':{'evidence':'detect README-only research, source monoculture and foreign defaults','decision':'name distinct failure classes rather than generic quality'},
          'escalation_recovery':{'evidence':'reopen research or re-diverge when evidence contradicts the chosen path','decision':'do not locally polish a structurally wrong decision'},
          'downstream_verification':{'evidence':'require integration, accessibility, visual and runtime verification','decision':'generator cannot self-certify completion'}
        }
        return {'skill':name,'dimensions':dims,'unresolved':[],'evaluator':'auditing-ui-research-depth'}

    def test_long_shallow_prose_record_fails_without_behavior_dimensions(self):
        rec={'skill':'shallow','prose':'beautiful modern thoughtful '+('quality '*5000),'dimensions':{'ownership':{'evidence':'make it good','decision':'make it good'}}}
        result=validate_skill_depth_record(rec)
        self.assertFalse(result['valid'])
        self.assertGreaterEqual(len(result['missing_dimensions']),8)

    def test_short_behaviorally_complete_record_passes_without_word_threshold(self):
        result=validate_skill_depth_record(self.complete_record())
        self.assertTrue(result['valid'],result['errors'])
        self.assertEqual(result['dimension_count'],10)

    def test_dimension_requires_distinct_evidence_and_decision(self):
        rec=self.complete_record(); rec['dimensions']['counterfactual_falsification']={'evidence':'', 'decision':''}
        result=validate_skill_depth_record(rec)
        self.assertFalse(result['valid']); self.assertTrue(any('counterfactual_falsification' in e for e in result['errors']))

    def test_repeated_identical_evidence_across_many_skills_is_suspicious_not_automatic_failure(self):
        records=[self.complete_record(f'skill-{i}') for i in range(8)]
        result=audit_skill_depth(records)
        self.assertTrue(result['valid'])
        self.assertTrue(result['warnings'])
        self.assertTrue(any('repeated' in w.lower() for w in result['warnings']))

    def test_constitution_defines_behavioral_dimensions_and_forbids_word_count(self):
        c=json.loads((ROOT/'knowledge/skill-depth-constitution-v6.json').read_text())
        self.assertEqual(c['version'],6)
        self.assertEqual(len(c['dimensions']),10)
        self.assertIn('word_count',c['forbidden_proxies'])
        self.assertIn('token_count',c['forbidden_proxies'])

if __name__=='__main__': unittest.main()
