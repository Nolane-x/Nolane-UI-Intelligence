import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import nolane_ui
from nolane_ui.external_ui_intelligence import load_external_ui_network


class ExternalUICompletionGateV12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.network = load_external_ui_network(ROOT)
        cls.packs = json.loads((ROOT / "knowledge" / "external-ui-reference-packs-v12.json").read_text())
        cls.routing = json.loads((ROOT / "knowledge" / "external-ui-generation-routing-v12.json").read_text())

    def profile(self):
        return {
            "material_ui": True,
            "task": "Build a React AI chat interface with tool-call approval and animated send feedback",
            "domain": "ai-collaboration",
            "platform": "web",
            "stack": "react",
            "ai_experience": True,
            "visual_ambition": "polished",
        }

    def reference_contract(self, profile=None):
        profile = profile or self.profile()
        contract = nolane_ui.compile_reference_execution_contract(
            profile, self.network, self.packs, self.routing, stack="react"
        )
        for stage in (
            "intent",
            "design",
            "implementation-selection",
            "license-gate",
            "critique",
            "runtime-verification",
        ):
            nolane_ui.record_reference_checkpoint(
                contract, stage, f"evidence:{stage}", mutate=True
            )
        return contract

    def packet(self):
        profile = self.profile()
        return {
            "packet_id": "v12-material",
            "artifact_revision": "revision-v12",
            "phase": "VERIFIED",
            "task_profile": profile,
            "obligations": [{"id": "O1", "status": "PASS", "evidence_refs": ["E1"]}],
            "evidence": [{
                "evidence_id": "E1",
                "method": "test-run",
                "source": "runtime-verification",
                "scope": "material-ui",
                "claim": "bounded material UI verification",
                "observed_at": "2026-08-22T00:00:00Z",
                "result": "PASS",
            }],
            "findings": [],
            "checks": {"repository": "PASS"},
            "claim": "bounded material UI claim",
            "bounds": ["tested React web flow only"],
            "unknowns": [],
            "decision": "PASS",
            "reference_execution": self.reference_contract(profile),
        }

    def test_package_completion_validator_accepts_closed_material_reference_lineage(self):
        packet = self.packet()
        result = nolane_ui.validate_completion_packet(packet, ROOT)
        self.assertEqual("PASS", result["decision"], result["errors"])

    def test_package_completion_validator_blocks_missing_reference_execution(self):
        packet = self.packet()
        packet.pop("reference_execution")
        result = nolane_ui.validate_completion_packet(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("reference execution" in error.lower() for error in result["errors"]))

    def test_package_completion_validator_blocks_reference_source_dropout(self):
        packet = self.packet()
        checkpoint = packet["reference_execution"]["stage_checkpoints"]["critique"]
        checkpoint["active_source_ids"] = checkpoint["active_source_ids"][1:]
        result = nolane_ui.validate_completion_packet(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("dropped persistent source" in error.lower() for error in result["errors"]))

    def test_package_completion_validator_blocks_task_fingerprint_drift(self):
        packet = self.packet()
        packet["task_profile"] = dict(packet["task_profile"])
        packet["task_profile"]["task"] = "Build a medical image annotation workstation"
        result = nolane_ui.validate_completion_packet(packet, ROOT)
        self.assertEqual("BLOCKED", result["decision"])
        self.assertTrue(any("fingerprint" in error.lower() for error in result["errors"]))

    def test_non_material_completion_keeps_historical_semantics(self):
        packet = self.packet()
        packet["task_profile"] = "legacy-profile-ref"
        packet.pop("reference_execution")
        result = nolane_ui.validate_completion_packet(packet, ROOT)
        self.assertEqual("PASS", result["decision"], result["errors"])


if __name__ == "__main__":
    unittest.main()
