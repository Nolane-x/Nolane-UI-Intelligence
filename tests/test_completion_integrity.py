import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "nolane_ui" / "validators.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("nui_validators_integrity", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_completion_packet


def base_packet():
    return {
        "packet_id": "integrity",
        "artifact_revision": "revision-1",
        "phase": "VERIFIED",
        "task_profile": "profile",
        "obligations": [{"id": "O1", "status": "PASS", "evidence_refs": ["E1"]}],
        "evidence": [{
            "evidence_id": "E1", "method": "test-run", "source": "unit-test",
            "scope": "repository", "claim": "contract holds",
            "observed_at": "2026-08-12T00:00:00Z", "result": "PASS"
        }],
        "findings": [],
        "checks": {"repository": "PASS"},
        "claim": "bounded structural claim",
        "bounds": ["repository only"],
        "unknowns": [],
        "decision": "PASS",
    }


class CompletionIntegrityTests(unittest.TestCase):
    def test_missing_artifact_revision_and_declared_decision_block(self):
        validate = load_validator()
        packet = base_packet()
        del packet["artifact_revision"]
        del packet["decision"]
        result = validate(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        joined = " ".join(result["errors"])
        self.assertIn("artifact_revision", joined)
        self.assertIn("decision", joined)

    def test_pass_obligation_must_reference_existing_passing_evidence(self):
        validate = load_validator()
        packet = base_packet()
        packet["obligations"][0]["evidence_refs"] = []
        result = validate(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("evidence" in e.lower() for e in result["errors"]))

        packet = base_packet()
        packet["evidence"][0]["result"] = "UNKNOWN"
        result = validate(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("UNKNOWN" in e for e in result["errors"]))

    def test_accepted_risk_requires_authority_but_can_preserve_failing_evidence(self):
        validate = load_validator()
        packet = base_packet()
        packet["obligations"][0] = {
            "id": "O-risk", "status": "ACCEPTED_RISK", "evidence_refs": ["E1"]
        }
        packet["evidence"][0]["result"] = "FAIL"
        packet["decision"] = "PASS_WITH_ACCEPTED_RISK"
        result = validate(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("accept" in e.lower() for e in result["errors"]))

        packet["obligations"][0]["acceptance"] = {
            "accepted_by": "product-owner",
            "authority": "user-product-requirements",
            "scope": "known visual polish defect"
        }
        result = validate(packet, ROOT)
        self.assertEqual("PASS_WITH_ACCEPTED_RISK", result["decision"])
        self.assertEqual([], result["errors"])

    def test_declared_decision_must_match_computed_decision(self):
        validate = load_validator()
        packet = base_packet()
        packet["decision"] = "BLOCKED"
        result = validate(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("declared decision" in e.lower() for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
