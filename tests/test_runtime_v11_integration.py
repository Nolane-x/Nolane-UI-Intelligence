import json
import unittest
from pathlib import Path

from nolane_ui import (
    append_runtime_live_event,
    assess_runtime_evidence_staleness,
    browser_runtime_findings,
    build_runtime_hook_capability,
    create_runtime_live_session,
    diagnose_runtime_state,
    load_runtime_rule_registry,
    route_runtime_finding,
    route_runtime_findings,
    scan_runtime_text,
    validate_runtime_browser_observation,
    validate_runtime_rule_registry,
)
from nolane_ui.interop import build_agent_install_plan
from nolane_ui.runtime_v11.evidence import build_evidence_binding, sha256_text


ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11IntegrationTests(unittest.TestCase):
    def test_public_runtime_api_is_available(self):
        registry = load_runtime_rule_registry(ROOT)
        result = validate_runtime_rule_registry(registry)
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["rule_count"], 13)
        self.assertTrue(callable(scan_runtime_text))
        self.assertTrue(callable(validate_runtime_browser_observation))
        self.assertTrue(callable(browser_runtime_findings))
        self.assertTrue(callable(diagnose_runtime_state))
        self.assertTrue(callable(create_runtime_live_session))
        self.assertTrue(callable(append_runtime_live_event))
        self.assertTrue(callable(route_runtime_finding))
        self.assertTrue(callable(route_runtime_findings))
        self.assertEqual(build_runtime_hook_capability("generic-cli")["authority"], "evidence-only")

    def test_runtime_evidence_api_detects_overlapping_staleness(self):
        binding = build_evidence_binding(
            evidence_id="render:integration",
            revision="rev-a",
            source_digests={"src/app.tsx": sha256_text("before")},
            artifacts=["artifacts/app.png"],
        )
        status = assess_runtime_evidence_staleness(
            binding,
            {"src/app.tsx": sha256_text("after")},
        )
        self.assertEqual(status["status"], "STALE")

    def test_runtime_rules_are_not_canonical_skills(self):
        graph_text = (ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8")
        registry = load_runtime_rule_registry(ROOT)
        for rule in registry["rules"]:
            self.assertNotIn(rule["rule_id"], graph_text)
        self.assertFalse((ROOT / "skills" / "runtime-v11").exists())

    def test_agent_plan_exposes_detector_as_evidence_only(self):
        plan = build_agent_install_plan("generic-cli", ROOT)
        runtime = plan["runtime_detection"]
        self.assertEqual(runtime["command"], "python scripts/nui-detect")
        self.assertEqual(runtime["claim_boundary"], "evidence-only")
        self.assertTrue((ROOT / "scripts" / "nui-detect").exists())

    def test_runtime_schemas_and_research_provenance_exist(self):
        for name in (
            "runtime-browser-observation-v11.schema.json",
            "runtime-evidence-binding-v11.schema.json",
            "runtime-live-session-v11.schema.json",
        ):
            schema = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        provenance_path = ROOT / "docs" / "research" / "impeccable-runtime-mechanism-transfer-v11.md"
        self.assertTrue(provenance_path.exists())
        provenance = provenance_path.read_text(encoding="utf-8").lower()
        self.assertIn("apache-2.0", provenance)
        self.assertIn("research inspiration", provenance)
        self.assertIn("independently designed and authored", provenance)
        self.assertIn("does not incorporate impeccable source code", provenance)
        self.assertIn("no canonical skills", provenance)
        self.assertTrue((ROOT / "docs" / "RUNTIME-DESIGN-INTELLIGENCE.md").exists())


if __name__ == "__main__":
    unittest.main()
