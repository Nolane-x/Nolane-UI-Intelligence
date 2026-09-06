import copy
import math
import unittest

from nolane_ui.ux_intelligence.impact import rank_ux_impacts


class UXImpactV3Tests(unittest.TestCase):
    def finding(self, *, finding_id='uxf:context', enforcement='warn'):
        return {
            'finding_id': finding_id,
            'journey_id': 'uxj:checkout',
            'rule_id': 'ux.task.same-goal-navigation-preserves-context',
            'severity': 'major',
            'enforcement': enforcement,
        }

    def component(self, value, *, origin='observed', ref='runtime:impact'):
        return {'value': value, 'origin': origin, 'evidence_refs': (ref,)}

    def complete_evidence(self):
        return {
            'goal_criticality': self.component(0.9, origin='declared', ref='contract:critical-flow'),
            'task_frequency': self.component(0.8),
            'completion_blockage': self.component(0.9),
            'recoverability_cost': self.component(0.8),
            'affected_scope': self.component(0.8),
            'regression_confidence': self.component(0.95),
            'evidence_completeness': self.component(1.0),
        }

    def incomplete_evidence(self):
        value = self.complete_evidence()
        value.pop('completion_blockage')
        return value

    def p0_evidence(self):
        return {name: self.component(1.0, origin='declared') for name in self.complete_evidence()}

    def test_missing_required_component_returns_unknown_not_default(self):
        assessment = rank_ux_impacts([self.finding()], self.incomplete_evidence())[0]
        self.assertEqual(assessment['status'], 'insufficient-evidence')
        self.assertEqual(assessment['priority_band'], 'unknown')
        self.assertIsNone(assessment['priority_score'])
        self.assertIn('completion_blockage', assessment['missing_required_components'])

    def test_inferred_component_makes_ranking_provisional(self):
        evidence = self.complete_evidence()
        evidence['task_frequency']['origin'] = 'inferred'
        assessment = rank_ux_impacts([self.finding()], evidence)[0]
        self.assertEqual(assessment['status'], 'provisional')
        self.assertIsNotNone(assessment['priority_score'])

    def test_priority_does_not_mutate_warning_authority(self):
        finding = self.finding(enforcement='warn')
        before = copy.deepcopy(finding)
        assessment = rank_ux_impacts([finding], self.p0_evidence())[0]
        self.assertEqual(assessment['priority_band'], 'p0')
        self.assertEqual(assessment['source_enforcement'], 'warn')
        self.assertEqual(finding, before)
        self.assertEqual(finding['enforcement'], 'warn')

    def test_invalid_component_values_reject_bool_nonfinite_and_out_of_range(self):
        for value in (True, math.nan, math.inf, -0.1, 1.1):
            evidence = self.complete_evidence()
            evidence['goal_criticality']['value'] = value
            with self.assertRaises((TypeError, ValueError)):
                rank_ux_impacts([self.finding()], evidence)

    def test_known_scores_sort_descending_then_source_identity(self):
        high = self.finding(finding_id='uxf:z')
        low = self.finding(finding_id='uxf:a')
        high_evidence = self.complete_evidence()
        low_evidence = {name: self.component(0.5) for name in self.complete_evidence()}
        assessments = rank_ux_impacts([low, high], {'uxf:z': high_evidence, 'uxf:a': low_evidence})
        self.assertEqual([item['source_id'] for item in assessments], ['uxf:z', 'uxf:a'])

    def test_same_score_sorts_by_stable_source_identity(self):
        evidence = self.complete_evidence()
        assessments = rank_ux_impacts(
            [self.finding(finding_id='uxf:z'), self.finding(finding_id='uxf:a')],
            {'uxf:z': evidence, 'uxf:a': evidence},
        )
        self.assertEqual([item['source_id'] for item in assessments], ['uxf:a', 'uxf:z'])


if __name__ == '__main__':
    unittest.main()
