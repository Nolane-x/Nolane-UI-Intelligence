import json
import unittest
from pathlib import Path

from nolane_ui import (
    build_runtime_hook_capability,
    load_runtime_rule_registry,
    scan_runtime_text,
    validate_runtime_browser_observation,
    validate_runtime_rule_registry,
)
from nolane_ui.interop import build_agent_install_plan


ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11IntegrationTests(unittest.TestCase):
    def test_public_runtime_api_is_available(self):
        registry = load_runtime_rule_registry(ROOT)
        result = validate_runtime_rule_registry(registry)
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["rule_count"], 10)
        self.assertTrue(callable(scan_runtime_text))
        self.assertTrue(callable(validate_runtime_browser_observation))
        self.assertEqual(build_runtime_hook_capability("generic-cli")["authority"], "evidence-only")

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

    def test_browser_schema_and_mechanism_provenance_exist(self):
        schema = json.loads((ROOT / "schemas" / "runtime-browser-observation-v11.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        provenance_path = ROOT / "docs" / "research" / "impeccable-runtime-mechanism-transfer-v11.md"
        self.assertTrue(provenance_path.exists())
        provenance = provenance_path.read_text(encoding="utf-8").lower()
        self.assertIn("apache-2.0", provenance)
        self.assertIn("independently authored", provenance)
        self.assertIn("no canonical skills", provenance)


if __name__ == "__main__":
    unittest.main()
