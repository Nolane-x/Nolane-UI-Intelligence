import copy
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = json.loads((ROOT / 'skills/skill-graph.json').read_text(encoding='utf-8'))


class ContractIntegrityTests(unittest.TestCase):
    def test_validator_exists_and_current_repository_contracts_are_canonical(self):
        from nolane_ui.contracts import validate_skill_contract_integrity
        result = validate_skill_contract_integrity(ROOT, GRAPH)
        self.assertTrue(result['valid'], result)
        self.assertEqual(result['checked'], len(GRAPH['skills']))

    def test_mutated_output_is_rejected(self):
        from nolane_ui.contracts import validate_skill_contract_integrity
        graph = copy.deepcopy(GRAPH)
        graph['skills']['designing-navigation']['output'] = 'invented-navigation-output'
        result = validate_skill_contract_integrity(ROOT, graph)
        self.assertFalse(result['valid'])
        self.assertTrue(any('designing-navigation' in e and 'output' in e.lower() for e in result['errors']))

    def test_mutated_parent_is_rejected(self):
        from nolane_ui.contracts import validate_skill_contract_integrity
        graph = copy.deepcopy(GRAPH)
        graph['skills']['designing-navigation']['parent'] = 'invented-parent'
        result = validate_skill_contract_integrity(ROOT, graph)
        self.assertFalse(result['valid'])
        self.assertTrue(any('designing-navigation' in e and 'parent' in e.lower() for e in result['errors']))


if __name__ == '__main__':
    unittest.main()
