from __future__ import annotations

import json
import unittest
from pathlib import Path

import nolane_ui
from nolane_ui import runtime_v11
from nolane_ui.runtime_v11.doctor import REQUIRED_RUNTIME_ARTIFACTS

ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11Phase5IntegrationTests(unittest.TestCase):
    def test_doctor_inventory_covers_live_visual_runtime(self) -> None:
        required = {
            "schemas/runtime-source-attribution-v11.schema.json",
            "schemas/runtime-browser-transport-v11.schema.json",
            "schemas/runtime-live-preview-v11.schema.json",
            "schemas/runtime-live-overlay-v11.schema.json",
            "src/nolane_ui/runtime_v11/source_attribution.py",
            "src/nolane_ui/runtime_v11/browser_transport.py",
            "src/nolane_ui/runtime_v11/playwright_adapter.py",
            "src/nolane_ui/runtime_v11/preview.py",
            "src/nolane_ui/runtime_v11/overlay.py",
            "src/nolane_ui/runtime_v11/live_visual.py",
        }
        self.assertTrue(required.issubset(set(REQUIRED_RUNTIME_ARTIFACTS)))

    def test_runtime_v11_exports_phase5_contract(self) -> None:
        expected = {
            "validate_source_attribution", "resolve_source_attribution", "select_source_candidate",
            "validate_browser_transport_capability", "build_browser_transport_capability", "require_transport_capabilities",
            "validate_preview_candidate", "build_preview_candidate", "assess_preview_freshness",
            "prepare_preview_application", "record_preview_observation",
            "validate_overlay_packet", "build_overlay_packet",
            "playwright_available", "playwright_capability", "refresh_playwright_preview",
            "inject_playwright_preview", "collect_playwright_observation",
            "prepare_live_visual_selection", "prepare_live_visual_preview", "accept_live_visual_preview",
            "assess_visual_observation_capabilities",
        }
        missing = sorted(name for name in expected if not callable(getattr(runtime_v11, name, None)))
        self.assertEqual(missing, [])

    def test_top_level_phase5_aliases_are_explicit_and_callable(self) -> None:
        expected = {
            "validate_runtime_source_attribution", "resolve_runtime_source_attribution", "select_runtime_source_candidate",
            "validate_runtime_browser_transport", "build_runtime_browser_transport", "require_runtime_transport_capabilities",
            "validate_runtime_preview_candidate", "build_runtime_preview_candidate", "assess_runtime_preview_freshness",
            "prepare_runtime_preview_application", "record_runtime_preview_observation",
            "validate_runtime_overlay_packet", "build_runtime_overlay_packet",
            "runtime_playwright_available", "runtime_playwright_capability", "refresh_runtime_playwright_preview",
            "inject_runtime_playwright_preview", "collect_runtime_playwright_observation",
            "prepare_runtime_live_visual_selection", "prepare_runtime_live_visual_preview",
            "accept_runtime_live_visual_preview", "assess_runtime_visual_observation_capabilities",
        }
        missing = sorted(name for name in expected if not callable(getattr(nolane_ui, name, None)))
        self.assertEqual(missing, [])
        self.assertTrue(expected.issubset(set(nolane_ui.__all__)))

    def test_phase5_remains_outside_canonical_skill_graph(self) -> None:
        graph = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))
        self.assertEqual(len(graph["skills"]), 874)
        serialized = json.dumps(graph, sort_keys=True)
        for runtime_only_name in (
            "runtime-source-attribution-v11", "runtime-browser-transport-v11",
            "runtime-live-preview-v11", "runtime-live-overlay-v11",
            "playwright_adapter", "live_visual",
        ):
            self.assertNotIn(runtime_only_name, serialized)


if __name__ == "__main__":
    unittest.main()
