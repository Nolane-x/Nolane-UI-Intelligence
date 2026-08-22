import importlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.external_ui_intelligence import load_external_ui_network


class ExternalUIExecutionV12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.network = load_external_ui_network(ROOT)
        cls.packs = json.loads((ROOT / "knowledge" / "external-ui-reference-packs-v12.json").read_text(encoding="utf-8"))

    def execution(self):
        spec = importlib.util.find_spec("nolane_ui.external_ui_execution")
        self.assertIsNotNone(spec, "V12.1 execution module is required")
        module = importlib.import_module("nolane_ui.external_ui_execution")
        for name in (
            "infer_reference_pack_ids",
            "compile_reference_execution_contract",
            "record_reference_checkpoint",
            "validate_reference_execution_contract",
            "validate_reference_stage_checkpoint",
            "validate_reference_completion",
        ):
            self.assertTrue(callable(getattr(module, name, None)), f"missing execution API {name}")
        return module

    def routing(self):
        path = ROOT / "knowledge" / "external-ui-generation-routing-v12.json"
        self.assertTrue(path.exists(), "V12.1 generation routing artifact is required")
        return json.loads(path.read_text(encoding="utf-8"))

    def profile(self):
        return {
            "material_ui": True,
            "task": "Build a React AI chat with animated send button, streaming tool calls and human approval",
            "domain": "ai-collaboration",
            "platform": "web",
            "stack": "react",
            "requirements": ["keyboard accessible", "loading success error states", "reduced motion"],
            "visual_ambition": "exceptional",
        }

    def test_material_ui_inference_routes_baseline_and_task_specific_packs(self):
        execution = self.execution(); routing = self.routing()
        pack_ids = execution.infer_reference_pack_ids(self.profile(), routing)
        self.assertIn("accessibility-verification", pack_ids)
        self.assertIn("performance-quality", pack_ids)
        self.assertIn("ai-chat", pack_ids)
        self.assertTrue({"button-feedback", "microinteraction"} & set(pack_ids))
        self.assertTrue({"agent-tool-ui", "agent-approval-human-loop"} & set(pack_ids))
        self.assertLessEqual(len(pack_ids), routing["policy"]["max_active_packs"])

    def test_generation_contract_is_compact_active_and_bound_to_task(self):
        execution = self.execution(); routing = self.routing(); profile = self.profile()
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        self.assertEqual(contract["posture"], "ACTIVE")
        self.assertTrue(contract["task_fingerprint"])
        self.assertTrue(contract["required_pack_ids"])
        self.assertEqual(set(contract["required_pack_ids"]), {p["pack_id"] for p in contract["resolved_packs"]})
        self.assertGreaterEqual(len(contract["must_preserve_source_ids"]), 3)
        self.assertLessEqual(len(contract["must_preserve_source_ids"]), routing["policy"]["max_active_source_ids"])
        self.assertTrue(contract["routing_evaluated"])
        self.assertFalse(contract["license_gate"]["requires_user_consent"])

    def test_missing_required_pack_invalidates_generation_contract(self):
        execution = self.execution(); routing = self.routing(); profile = self.profile()
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        removed = contract["resolved_packs"].pop()
        result = execution.validate_reference_execution_contract(contract, profile, routing)
        self.assertFalse(result["valid"])
        self.assertTrue(any(removed["pack_id"] in error for error in result["errors"]))

    def test_task_profile_drift_invalidates_bound_contract(self):
        execution = self.execution(); routing = self.routing(); profile = self.profile()
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        changed = dict(profile); changed["task"] = "Build a medical imaging annotation canvas"
        result = execution.validate_reference_execution_contract(contract, changed, routing)
        self.assertFalse(result["valid"])
        self.assertTrue(any("fingerprint" in error.lower() for error in result["errors"]))

    def test_checkpoint_cannot_drop_persistent_reference_ids(self):
        execution = self.execution(); routing = self.routing(); profile = self.profile()
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        checkpoint = execution.record_reference_checkpoint(contract, "intent", "evidence:intent")
        self.assertTrue(execution.validate_reference_stage_checkpoint(contract, checkpoint)["valid"])
        checkpoint["active_source_ids"] = checkpoint["active_source_ids"][1:]
        result = execution.validate_reference_stage_checkpoint(contract, checkpoint)
        self.assertFalse(result["valid"])
        self.assertTrue(any("source" in error.lower() and "drop" in error.lower() for error in result["errors"]))

    def test_implementable_phase_requires_design_selection_and_license_checkpoints(self):
        execution = self.execution(); routing = self.routing(); profile = self.profile()
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        for stage in ("intent", "design"):
            execution.record_reference_checkpoint(contract, stage, f"evidence:{stage}", mutate=True)
        incomplete = execution.validate_reference_completion(contract, "IMPLEMENTABLE")
        self.assertFalse(incomplete["valid"])
        self.assertIn("implementation-selection", incomplete["missing_stages"])
        self.assertIn("license-gate", incomplete["missing_stages"])
        for stage in ("implementation-selection", "license-gate"):
            execution.record_reference_checkpoint(contract, stage, f"evidence:{stage}", mutate=True)
        complete = execution.validate_reference_completion(contract, "IMPLEMENTABLE")
        self.assertTrue(complete["valid"], complete["errors"])

    def test_release_requires_every_reference_stage_and_provenance(self):
        execution = self.execution(); routing = self.routing(); profile = self.profile()
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        for stage in ("intent", "design", "implementation-selection", "license-gate", "critique", "runtime-verification"):
            execution.record_reference_checkpoint(contract, stage, f"evidence:{stage}", mutate=True)
        result = execution.validate_reference_completion(contract, "RELEASED")
        self.assertFalse(result["valid"])
        self.assertEqual(result["missing_stages"], ["provenance"])
        provenance = {source_id: "influenced" for source_id in contract["must_preserve_source_ids"]}
        execution.record_reference_checkpoint(
            contract,
            "provenance",
            "evidence:provenance",
            provenance=provenance,
            mutate=True,
        )
        result = execution.validate_reference_completion(contract, "RELEASED")
        self.assertTrue(result["valid"], result["errors"])

    def test_restrictive_research_fallback_does_not_trigger_consent(self):
        execution = self.execution(); routing = self.routing()
        profile = {
            "material_ui": True,
            "task": "Design a polished animated CTA button",
            "platform": "web",
            "stack": "react",
            "visual_ambition": "exceptional",
        }
        contract = execution.compile_reference_execution_contract(profile, self.network, self.packs, routing, stack="react")
        self.assertIn("button-feedback", contract["required_pack_ids"])
        self.assertFalse(contract["license_gate"]["requires_user_consent"])
        self.assertEqual(contract["license_gate"]["consent_source_ids"], [])


if __name__ == "__main__":
    unittest.main()
