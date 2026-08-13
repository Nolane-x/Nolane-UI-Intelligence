import json
import unittest
from pathlib import Path

from src.nolane_ui.authority import validate_agent_adapters

ROOT = Path(__file__).resolve().parents[1]


class AgentAdapterV7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = ROOT / "knowledge" / "agent-readable-ui-sources-v7.json"

    def test_registry_exists_and_is_valid(self):
        data = json.loads(self.path.read_text(encoding="utf-8"))
        result = validate_agent_adapters(data)
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["adapter_count"], 8)

    def test_access_protocol_never_escalates_authority(self):
        data = json.loads(self.path.read_text(encoding="utf-8"))
        for item in data["adapters"]:
            self.assertIs(item["authority_escalation"], False, item["id"])
            self.assertTrue(item["live_verification_required"], item["id"])
            self.assertTrue(item["underlying_authority"], item["id"])

    def test_expected_access_modes_are_present(self):
        data = json.loads(self.path.read_text(encoding="utf-8"))
        modes = {item["access_mode"] for item in data["adapters"]}
        self.assertTrue({"mcp", "llms-txt", "agent-skill", "open-code", "ai-toolkit"}.issubset(modes))

    def test_registry_has_primer_mantine_shadcn_carbon_shopify_and_gsap(self):
        data = json.loads(self.path.read_text(encoding="utf-8"))
        ids = {item["id"] for item in data["adapters"]}
        expected = {
            "primer-mcp", "mantine-llms", "mantine-mcp", "shadcn-open-code",
            "carbon-mcp", "shopify-ai-toolkit", "gsap-official-skills"
        }
        self.assertTrue(expected.issubset(ids), expected - ids)

    def test_each_adapter_preserves_transfer_and_license_boundary(self):
        data = json.loads(self.path.read_text(encoding="utf-8"))
        for item in data["adapters"]:
            self.assertIsInstance(item.get("license_boundary"), str, item["id"])
            self.assertTrue(item["license_boundary"].strip(), item["id"])
            self.assertIsInstance(item.get("transfer_boundary"), str, item["id"])
            self.assertTrue(item["transfer_boundary"].strip(), item["id"])
            self.assertIsInstance(item.get("verified_at"), str, item["id"])

    def test_schema_artifacts_exist(self):
        for name in ("ui-authority-route.schema.json", "concrete-design-packet.schema.json"):
            data = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
            self.assertEqual(data["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_validator_rejects_mcp_as_authority_boost(self):
        data = json.loads(self.path.read_text(encoding="utf-8"))
        data["adapters"][0]["authority_escalation"] = True
        result = validate_agent_adapters(data)
        self.assertFalse(result["valid"])
        self.assertTrue(any("authority escalation" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
