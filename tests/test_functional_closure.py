import copy
import unittest


BASE = {
    'status': 'PASS',
    'capabilities': [
        {'id': 'cap-dashboard', 'required': True, 'roles': ['member'], 'surface_ids': ['dashboard'], 'action_ids': ['act-open-settings']},
        {'id': 'cap-settings', 'required': True, 'roles': ['member'], 'surface_ids': ['settings'], 'action_ids': ['act-save-settings']},
    ],
    'surfaces': [
        {'id': 'dashboard', 'entry': True, 'kind': 'page'},
        {'id': 'settings', 'entry': False, 'kind': 'page'},
    ],
    'actions': [
        {'id': 'act-open-settings', 'capability_id': 'cap-dashboard', 'destination_id': 'settings', 'risk': 'routine'},
        {'id': 'act-save-settings', 'capability_id': 'cap-settings', 'destination_id': 'settings', 'risk': 'async', 'recovery': 'keep edits and allow retry'},
    ],
    'bindings': [
        {'id': 'bind-settings', 'action_id': 'act-open-settings', 'surface_id': 'dashboard', 'label': 'Settings', 'modalities': ['pointer', 'keyboard'], 'discoverability': 'visible', 'roles': ['member']},
        {'id': 'bind-save', 'action_id': 'act-save-settings', 'surface_id': 'settings', 'label': 'Save changes', 'modalities': ['pointer', 'keyboard'], 'discoverability': 'visible', 'roles': ['member']},
    ],
    'routes': [
        {'from': 'dashboard', 'to': 'settings', 'action_id': 'act-open-settings', 'intentional': True},
    ],
    'scenarios': [
        {'id': 'sc-settings', 'role': 'member', 'start_surface': 'dashboard', 'capability_ids': ['cap-dashboard', 'cap-settings'], 'path_actions': ['act-open-settings', 'act-save-settings']},
    ],
}


class FunctionalClosureTests(unittest.TestCase):
    def validate(self, record):
        from nolane_ui.closure import validate_functional_closure
        return validate_functional_closure(record)

    def test_complete_graph_passes(self):
        result = self.validate(BASE)
        self.assertTrue(result['valid'], result)

    def test_required_capability_without_surface_fails(self):
        record = copy.deepcopy(BASE)
        record['capabilities'][1]['surface_ids'] = []
        result = self.validate(record)
        self.assertFalse(result['valid'])
        self.assertTrue(any('cap-settings' in e and 'surface' in e for e in result['errors']))

    def test_action_without_binding_fails(self):
        record = copy.deepcopy(BASE)
        record['bindings'] = [record['bindings'][0]]
        result = self.validate(record)
        self.assertFalse(result['valid'])
        self.assertTrue(any('act-save-settings' in e and 'binding' in e for e in result['errors']))

    def test_secret_url_does_not_rescue_orphan_destination(self):
        record = copy.deepcopy(BASE)
        record['routes'] = []
        record['surfaces'][1]['deep_link'] = '/settings'
        record['surfaces'][1]['intentional_hidden'] = False
        result = self.validate(record)
        self.assertFalse(result['valid'])
        self.assertTrue(any('settings' in e and 'unreachable' in e for e in result['errors']))

    def test_semantic_label_collision_fails(self):
        record = copy.deepcopy(BASE)
        record['actions'].append({'id': 'act-delete', 'capability_id': 'cap-dashboard', 'destination_id': 'dashboard', 'risk': 'destructive', 'recovery': 'undo toast'})
        record['bindings'].append({'id': 'bind-delete', 'action_id': 'act-delete', 'surface_id': 'dashboard', 'label': 'Settings', 'modalities': ['pointer'], 'discoverability': 'visible', 'roles': ['member']})
        result = self.validate(record)
        self.assertFalse(result['valid'])
        self.assertTrue(any('collision' in e.lower() for e in result['errors']))

    def test_async_or_destructive_action_requires_recovery(self):
        record = copy.deepcopy(BASE)
        record['actions'][1].pop('recovery')
        result = self.validate(record)
        self.assertFalse(result['valid'])
        self.assertTrue(any('recovery' in e.lower() for e in result['errors']))

    def test_every_required_capability_needs_scenario_coverage(self):
        record = copy.deepcopy(BASE)
        record['scenarios'][0]['capability_ids'] = ['cap-dashboard']
        result = self.validate(record)
        self.assertFalse(result['valid'])
        self.assertTrue(any('cap-settings' in e and 'scenario' in e for e in result['errors']))

    def test_ui_specification_rejects_missing_control_for_action(self):
        from nolane_ui.closure import validate_ui_specification
        spec = {
            'screens': [
                {'id': 'dashboard', 'states': ['default'], 'responsive_behavior': 'preserve access', 'controls': [
                    {'id': 'settings-button', 'action_id': 'act-open-settings', 'label': 'Settings', 'semantic_role': 'button', 'focus_behavior': 'normal', 'accessibility_name': 'Settings'}
                ]},
                {'id': 'settings', 'states': ['default', 'saving', 'error'], 'responsive_behavior': 'stack fields', 'controls': []},
            ],
            'required_action_ids': ['act-open-settings', 'act-save-settings'],
        }
        result = validate_ui_specification(spec)
        self.assertFalse(result['valid'])
        self.assertIn('act-save-settings', result['missing_actions'])

    def test_runtime_ledger_requires_pass_for_required_actions(self):
        from nolane_ui.closure import validate_runtime_behavior_ledger
        ledger = {
            'required_action_ids': ['act-open-settings', 'act-save-settings'],
            'probes': [
                {'action_id': 'act-open-settings', 'status': 'PASS', 'modalities': ['pointer', 'keyboard'], 'evidence': 'browser trace'},
                {'action_id': 'act-save-settings', 'status': 'FAIL', 'modalities': ['pointer'], 'evidence': 'network failure path broken'},
            ],
        }
        result = validate_runtime_behavior_ledger(ledger)
        self.assertFalse(result['valid'])
        self.assertIn('act-save-settings', result['failed_actions'])


if __name__ == '__main__':
    unittest.main()
