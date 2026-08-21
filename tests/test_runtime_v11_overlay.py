from __future__ import annotations

import json
import unittest
from pathlib import Path

try:
    from nolane_ui.runtime_v11.overlay import build_overlay_packet, validate_overlay_packet
except ModuleNotFoundError:
    def _missing(*args, **kwargs):
        raise AssertionError("Phase 5 overlay API is missing")
    build_overlay_packet = validate_overlay_packet = _missing


class RuntimeV11OverlayTests(unittest.TestCase):
    def identity(self) -> dict:
        return {
            "locator": "#target",
            "bounding_box": {"x": 10, "y": 20, "width": 200, "height": 80},
        }

    def attribution(self, status: str = "AMBIGUOUS") -> dict:
        return {
            "version": 11,
            "status": status,
            "rendered_identity": {"locator": "#target"},
            "candidates": [{
                "candidate_id": "app",
                "source_path": "src/App.tsx",
                "source_digest": "sha256:" + "a" * 64,
                "range": {"start": 1, "end": 5},
                "attribution_mechanisms": ["source-map"],
                "evidence_refs": ["browser:target"],
                "confidence": "HIGH",
            }],
            "failures": [],
            "mutation_authorized": False,
            "selected_candidate_id": None,
            "selection_authority": None,
            "claim_boundary": "source-attribution-only",
        }

    def preview(self) -> dict:
        return {
            "version": 11,
            "preview_id": "preview-a",
            "session_id": "session-a",
            "source_candidate": self.attribution()["candidates"][0],
            "base_source_digest": "sha256:" + "a" * 64,
            "replacement": "new",
            "preserve_constraints": [],
            "direction_id": "direction-a",
            "provenance": {"revision": "rev-a"},
            "transport_requirements": ["preview_injection", "refresh"],
            "state": "OBSERVED",
            "capture_refs": ["capture:a"],
            "observation": {"refresh_status": "RELOAD_OK", "revision": "rev-a"},
            "claim_boundary": "preview-transport-only",
        }

    def build(self, status: str = "AMBIGUOUS") -> dict:
        return build_overlay_packet(
            rendered_identity=self.identity(),
            attribution=self.attribution(status),
            preview=self.preview(),
            runtime_findings=[{"finding_id": "runtime.layout:test"}],
            capability_gaps=["occlusion"],
            reobservation={"decision": "UNKNOWN", "claim_boundary": "runtime-closure-only"},
        )

    def test_overlay_preserves_attribution_ambiguity_and_capability_gaps(self) -> None:
        packet = self.build("AMBIGUOUS")
        self.assertEqual(packet["source_attribution_status"], "AMBIGUOUS")
        self.assertEqual(packet["capability_gaps"], ["occlusion"])
        self.assertEqual(packet["claim_boundary"], "overlay-evidence-only")

    def test_overlay_carries_only_runtime_finding_ids_not_mutable_findings(self) -> None:
        packet = self.build()
        self.assertEqual(packet["runtime_finding_ids"], ["runtime.layout:test"])
        self.assertNotIn("runtime_findings", packet)

    def test_overlay_rejects_beauty_winner_or_release_authority(self) -> None:
        base = self.build()
        for key, value in (
            ("beauty_score", 10),
            ("winner", "preview-a"),
            ("verified", True),
            ("released", True),
            ("generator_self_score", 0.99),
            ("generator_preference", "A"),
        ):
            with self.subTest(key=key):
                bad = dict(base)
                bad[key] = value
                self.assertFalse(validate_overlay_packet(bad)["valid"])

    def test_overlay_does_not_upgrade_unknown_source_to_exact(self) -> None:
        packet = self.build("UNKNOWN")
        self.assertEqual(packet["source_attribution_status"], "UNKNOWN")
        self.assertIsNone(packet["selected_source"])

    def test_overlay_capture_refs_come_from_preview_evidence(self) -> None:
        packet = self.build()
        self.assertEqual(packet["capture_refs"], ["capture:a"])
        self.assertEqual(packet["preview_state"], "OBSERVED")

    def test_schema_exists_and_claim_boundary_is_evidence_only(self) -> None:
        path = Path(__file__).resolve().parents[1] / "schemas" / "runtime-live-overlay-v11.schema.json"
        self.assertTrue(path.exists(), "Phase 5 overlay schema is missing")
        schema = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["claim_boundary"]["const"], "overlay-evidence-only")
        self.assertFalse(schema["additionalProperties"])


if __name__ == "__main__":
    unittest.main()
