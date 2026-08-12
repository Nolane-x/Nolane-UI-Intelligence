import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "nolane_ui" / "validators.py"


class KernelTests(unittest.TestCase):
    def validator(self, name):
        self.assertTrue(MODULE_PATH.is_file(), "validator implementation must exist")
        spec = importlib.util.spec_from_file_location("nui_validators", MODULE_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertTrue(hasattr(module, name), f"missing validator: {name}")
        return getattr(module, name)

    def test_skill_graph_rejects_missing_skill_and_unknown_parent(self):
        validate = self.validator("validate_skill_graph")
        graph = {
            "lifecycle": ["INTAKE", "RELEASED"],
            "skills": {
                "root": {"parent": None},
                "child": {"parent": "ghost"},
            },
        }
        errors = validate(graph, {"root"})
        self.assertTrue(any("child" in e and "missing" in e.lower() for e in errors))
        self.assertTrue(any("ghost" in e for e in errors))

    def test_state_matrix_requires_each_required_state_to_be_accounted_for(self):
        validate = self.validator("validate_state_matrix")
        matrix = {
            "required_states": ["default", "focus", "loading", "error"],
            "applicable_states": ["default", "focus", "loading"],
            "explicitly_inapplicable": [],
            "transitions": [{"from": "default", "to": "loading"}],
        }
        result = validate(matrix)
        self.assertFalse(result["valid"])
        self.assertIn("error", result["unaccounted_states"])

    def test_token_model_rejects_invalid_tier_and_alias_cycle(self):
        validate = self.validator("validate_tokens")
        model = {
            "tokens": {
                "a": {"tier": "semantic", "alias": "b"},
                "b": {"tier": "semantic", "alias": "a"},
                "x": {"tier": "page-hack", "value": "17px"},
            }
        }
        result = validate(model)
        self.assertFalse(result["valid"])
        self.assertTrue(result["cycles"])
        self.assertIn("x", result["invalid_tiers"])

    def test_completion_gate_blocks_unknown_evidence_and_open_major(self):
        validate = self.validator("validate_completion_packet")
        packet = {
            "packet_id": "p1",
            "phase": "VERIFIED",
            "task_profile": "profile-1",
            "obligations": [{"id": "O1", "status": "PASS"}],
            "evidence": [{"evidence_id": "E1", "result": "UNKNOWN"}],
            "findings": [{"finding_id": "F1", "severity": "major", "status": "open"}],
            "checks": {"repository": "PASS"},
            "claim": "UI verified",
            "bounds": ["desktop only"],
            "unknowns": ["screen reader not checked"],
        }
        result = validate(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("UNKNOWN" in e for e in result["errors"]))
        self.assertTrue(any("major" in e.lower() for e in result["errors"]))

    def test_completion_gate_accepts_bounded_resolved_packet(self):
        validate = self.validator("validate_completion_packet")
        packet = {
            "packet_id": "p2",
            "phase": "VERIFIED",
            "task_profile": "profile-1",
            "obligations": [{"id": "O1", "status": "PASS"}],
            "evidence": [{"evidence_id": "E1", "result": "PASS"}],
            "findings": [{"finding_id": "F1", "severity": "minor", "status": "repaired"}],
            "checks": {"repository": "PASS"},
            "claim": "Structural NUI repository verification passed",
            "bounds": ["does not prove future UI aesthetic quality"],
            "unknowns": [],
        }
        result = validate(packet, ROOT)
        self.assertEqual("PASS", result["decision"])
        self.assertEqual([], result["errors"])


if __name__ == "__main__":
    unittest.main()
