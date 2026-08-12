import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "nolane_ui" / "validators.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("nui_validators_gate", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_completion_packet


class AdversarialGateTests(unittest.TestCase):
    def test_adversarial_packets_are_rejected_as_expected(self):
        validate = load_validator()
        cases_path = ROOT / "evals" / "adversarial" / "completion-packets.json"
        data = json.loads(cases_path.read_text(encoding="utf-8"))
        failures = []
        for case in data["cases"]:
            result = validate(case["packet"], ROOT)
            if result["decision"] != case["expected_decision"]:
                failures.append(
                    f"{case['id']}: expected {case['expected_decision']}, got {result['decision']} ({result['errors']})"
                )
        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
