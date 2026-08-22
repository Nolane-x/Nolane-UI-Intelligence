import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.external_ui_intelligence import (
    PERMISSIVE_LICENSES,
    RECONSULT_STAGES,
    load_external_ui_network,
    rank_reference_candidates,
    resolve_reference_pack,
    validate_external_ui_network,
)


class ExternalUIIntelligenceV12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.network = load_external_ui_network(ROOT)
        cls.packs = json.loads((ROOT / "knowledge" / "external-ui-reference-packs-v12.json").read_text(encoding="utf-8"))
        cls.license_policy = json.loads((ROOT / "knowledge" / "external-ui-license-policy-v12.json").read_text(encoding="utf-8"))
        cls.sources = {item["id"]: item for item in cls.network["sources"]}

    def test_network_is_large_but_typed(self):
        self.assertGreaterEqual(len(self.network["sources"]), 140)
        self.assertGreaterEqual(len(self.packs["packs"]), 30)
        required = {
            "id", "name", "url", "family", "role", "mechanisms", "adoption_mode",
            "license", "health", "drift", "fallbacks", "reconsult_at",
        }
        for source in self.network["sources"]:
            self.assertTrue(required.issubset(source), source.get("id"))
            self.assertTrue(source["mechanisms"], source["id"])
            self.assertEqual(source["reconsult_at"], list(RECONSULT_STAGES), source["id"])

    def test_restrictive_or_mixed_sources_require_consent_for_direct_adoption(self):
        for source in self.network["sources"]:
            status = source["license"]["status"]
            if status in {"consent", "restricted", "mixed"}:
                self.assertTrue(source["requires_user_consent"], source["id"])
                self.assertNotEqual(source["adoption_mode"], "direct-preferred", source["id"])

    def test_reference_only_and_discovery_sources_cannot_direct_adopt(self):
        for source in self.network["sources"]:
            if source["adoption_mode"] in {"reference-only", "discovery-only"}:
                self.assertFalse(source.get("direct_adoption_allowed", False), source["id"])

    def test_permissive_alternative_outranks_restricted_equivalent(self):
        candidates = [
            {"id": "heavy", "capability_fit": 1.0, "license": {"status": "consent", "id": "Custom"}, "health": "active"},
            {"id": "green", "capability_fit": 0.96, "license": {"status": "green", "id": "MIT"}, "health": "active"},
        ]
        self.assertEqual(rank_reference_candidates(candidates)[0]["id"], "green")

    def test_restricted_source_can_win_only_when_materially_better(self):
        candidates = [
            {"id": "heavy", "capability_fit": 1.0, "unique_requirement_fit": 1.0, "license": {"status": "consent", "id": "Custom"}, "health": "active"},
            {"id": "green", "capability_fit": 0.35, "unique_requirement_fit": 0.0, "license": {"status": "green", "id": "MIT"}, "health": "active"},
        ]
        ranked = rank_reference_candidates(candidates)
        self.assertEqual(ranked[0]["id"], "heavy")
        self.assertTrue(ranked[0]["requires_user_consent"])

    def test_every_pack_keeps_permissive_route_or_declares_exception(self):
        for pack in self.packs["packs"]:
            preferred = [self.sources[source_id] for source_id in pack["preferred_sources"]]
            has_green = any(
                source["license"]["status"] == "green" and source["license"]["id"] in PERMISSIVE_LICENSES
                for source in preferred
            )
            self.assertTrue(has_green or pack.get("restricted_only_reason"), pack["id"])
            self.assertEqual(pack["reconsult_at"], list(RECONSULT_STAGES), pack["id"])

    def test_resolver_returns_small_persistent_reference_packet(self):
        result = resolve_reference_pack("button-feedback", self.network, self.packs, stack="react", max_sources=8)
        self.assertGreaterEqual(len(result["sources"]), 3)
        self.assertLessEqual(len(result["sources"]), 8)
        self.assertEqual(result["reconsult_at"], list(RECONSULT_STAGES))
        self.assertIn("license_gate", result)
        self.assertTrue(any(source["license"]["status"] == "green" for source in result["sources"]))

    def test_full_network_contract(self):
        result = validate_external_ui_network(self.network, self.packs, self.license_policy)
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["source_count"], 140)
        self.assertGreaterEqual(result["pack_count"], 30)


if __name__ == "__main__":
    unittest.main()
