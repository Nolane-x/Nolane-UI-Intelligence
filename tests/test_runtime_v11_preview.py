from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

try:
    from nolane_ui.runtime_v11.preview import (
        assess_preview_freshness,
        build_preview_candidate,
        prepare_preview_application,
        record_preview_observation,
        validate_preview_candidate,
    )
except ModuleNotFoundError:
    def _missing(*args, **kwargs):
        raise AssertionError("Phase 5 preview API is missing")
    assess_preview_freshness = build_preview_candidate = prepare_preview_application = record_preview_observation = validate_preview_candidate = _missing


class RuntimeV11PreviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / "src").mkdir()
        self.source = self.root / "src" / "App.tsx"
        self.source.write_text("hello world", encoding="utf-8")
        self.digest = "sha256:" + hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.source_candidate = {
            "candidate_id": "app",
            "source_path": "src/App.tsx",
            "source_digest": self.digest,
            "range": {"start": 0, "end": 5},
            "attribution_mechanisms": ["development-instrumentation"],
            "evidence_refs": ["browser:target"],
            "confidence": "HIGH",
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    def preview(self) -> dict:
        return build_preview_candidate(
            preview_id="preview-a",
            session_id="session-a",
            source_candidate=self.source_candidate,
            replacement="HELLO",
            preserve_constraints=["keep interaction semantics"],
            direction_id="direction-a",
            provenance={"generator": "nui", "revision": "rev-a"},
        )

    def browser_packet(self, *, capture_ref: str = "capture:preview-a") -> dict:
        return {
            "version": 11,
            "collector": "test",
            "url": "http://localhost/",
            "viewport": {"width": 1280, "height": 720, "dpr": 1},
            "capabilities": {
                "geometry": True,
                "computed_style": True,
                "runtime_errors": True,
                "capture": True,
                "document_metrics": True,
                "occlusion": False,
            },
            "capture_ref": capture_ref,
            "document_metrics": {"scroll_width": 1280, "client_width": 1280, "scroll_height": 720, "client_height": 720},
            "observations": [{
                "locator": "#target",
                "visible_text": "HELLO world",
                "bounding_box": {"x": 10, "y": 10, "width": 100, "height": 40},
                "computed_style": {"display": "block"},
            }],
            "runtime_errors": [],
        }

    def transport(self, *, preview_injection: bool = True, reload: bool = True) -> dict:
        return {
            "version": 11,
            "provider": "test",
            "capabilities": {
                "navigation": True, "geometry": True, "computed_style": True,
                "runtime_errors": True, "capture": True, "document_metrics": True,
                "occlusion": False, "rendered_metadata": True,
                "preview_injection": preview_injection, "hot_reload": False, "reload": reload,
            },
            "claim_boundary": "browser-transport-only",
        }

    def test_build_preview_does_not_write_canonical_source(self) -> None:
        before = self.source.read_text(encoding="utf-8")
        preview = self.preview()
        self.assertEqual(self.source.read_text(encoding="utf-8"), before)
        self.assertEqual(preview["state"], "PREPARED")
        self.assertEqual(preview["claim_boundary"], "preview-transport-only")

    def test_preview_transition_returns_new_record_without_mutating_input(self) -> None:
        preview = self.preview()
        plan = prepare_preview_application(preview, self.transport())
        self.assertEqual(preview["state"], "PREPARED")
        self.assertEqual(plan["preview"]["state"], "INJECTED")
        self.assertIsNot(plan["preview"], preview)

    def test_changed_base_digest_marks_preview_stale(self) -> None:
        preview = self.preview()
        self.source.write_text("changed", encoding="utf-8")
        freshness = assess_preview_freshness(preview, self.root)
        self.assertEqual(freshness["status"], "STALE")
        self.assertEqual(freshness["failure"], "PREVIEW_STALE")

    def test_preview_application_requires_injection_and_refresh_capability(self) -> None:
        preview = self.preview()
        result = prepare_preview_application(preview, self.transport(preview_injection=False, reload=False))
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertIn("preview_injection", result["missing_capabilities"])
        self.assertIn("refresh", result["missing_capabilities"])
        self.assertEqual(preview["state"], "PREPARED")

    def test_observed_requires_successful_refresh(self) -> None:
        preview = prepare_preview_application(self.preview(), self.transport())["preview"]
        with self.assertRaises(ValueError):
            record_preview_observation(
                preview,
                refresh_evidence={"status": "RELOAD_FAILED", "candidate_id": "preview-a"},
                browser_observation=self.browser_packet(),
            )

    def test_successful_refresh_plus_valid_packet_records_observation_immutably(self) -> None:
        injected = prepare_preview_application(self.preview(), self.transport())["preview"]
        observed = record_preview_observation(
            injected,
            refresh_evidence={"status": "RELOAD_OK", "candidate_id": "preview-a", "revision": "rev-a"},
            browser_observation=self.browser_packet(),
        )
        self.assertEqual(injected["state"], "INJECTED")
        self.assertEqual(observed["state"], "OBSERVED")
        self.assertEqual(observed["capture_refs"], ["capture:preview-a"])
        self.assertEqual(observed["observation"]["refresh_status"], "RELOAD_OK")

    def test_validator_rejects_release_authority(self) -> None:
        bad = self.preview()
        bad["released"] = True
        self.assertFalse(validate_preview_candidate(bad)["valid"])

    def test_schema_exists_with_closed_preview_states(self) -> None:
        path = Path(__file__).resolve().parents[1] / "schemas" / "runtime-live-preview-v11.schema.json"
        self.assertTrue(path.exists(), "Phase 5 preview schema is missing")
        schema = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["state"]["enum"], ["PREPARED", "INJECTED", "OBSERVED", "STALE", "CONFLICT", "REJECTED", "ACCEPTED"])


if __name__ == "__main__":
    unittest.main()
