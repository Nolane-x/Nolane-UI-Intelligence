from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.browser import validate_browser_observation

try:
    from nolane_ui.runtime_v11.playwright_adapter import (
        collect_playwright_observation,
        inject_playwright_preview,
        playwright_available,
        playwright_capability,
        refresh_playwright_preview,
    )
except ModuleNotFoundError:
    def _missing(*args, **kwargs):
        raise AssertionError("Phase 5 Playwright adapter API is missing")
    def playwright_available() -> bool:
        return False
    collect_playwright_observation = inject_playwright_preview = playwright_capability = refresh_playwright_preview = _missing


class _FakePage:
    def __init__(self, *, reload_ok: bool = True) -> None:
        self.reload_ok = reload_ok
        self.reload_calls = 0
        self.evaluations = []

    def reload(self, **kwargs):
        self.reload_calls += 1
        if not self.reload_ok:
            raise RuntimeError("reload failed")
        return None

    def evaluate(self, expression, arg=None):
        self.evaluations.append((expression, arg))
        return True


class RuntimeV11PlaywrightAdapterContractTests(unittest.TestCase):
    def test_core_runtime_import_is_not_coupled_to_playwright(self) -> None:
        import nolane_ui.runtime_v11 as runtime
        self.assertTrue(callable(runtime.validate_browser_observation))

    def test_adapter_capability_is_provider_only_not_authority(self) -> None:
        record = playwright_capability()
        self.assertEqual(record["provider"], "playwright")
        self.assertEqual(record["claim_boundary"], "browser-transport-only")
        self.assertTrue(record["capabilities"]["geometry"])
        self.assertTrue(record["capabilities"]["preview_injection"])
        self.assertTrue(record["capabilities"]["reload"])
        self.assertNotIn("verified", str(record).lower())

    def test_failed_hmr_falls_back_to_bounded_reload(self) -> None:
        page = _FakePage(reload_ok=True)
        result = refresh_playwright_preview(page, prefer_hmr=True, hmr_bridge=lambda _page: False)
        self.assertEqual(result["status"], "RELOAD_OK")
        self.assertEqual(result["hmr_status"], "HOT_RELOAD_FAILED")
        self.assertEqual(page.reload_calls, 1)

    def test_failed_hmr_and_reload_remain_failure(self) -> None:
        page = _FakePage(reload_ok=False)
        result = refresh_playwright_preview(page, prefer_hmr=True, hmr_bridge=lambda _page: False)
        self.assertEqual(result["status"], "RELOAD_FAILED")
        self.assertEqual(result["hmr_status"], "HOT_RELOAD_FAILED")

    def test_preview_injection_is_ephemeral_browser_operation(self) -> None:
        page = _FakePage()
        result = inject_playwright_preview(
            page,
            selector="#target",
            patch={"text": "Preview", "styles": {"fontWeight": "700"}},
            candidate_id="preview-a",
        )
        self.assertEqual(result["status"], "INJECTED")
        self.assertEqual(result["candidate_id"], "preview-a")
        self.assertEqual(len(page.evaluations), 1)


class RuntimeV11PlaywrightRealSmokeTests(unittest.TestCase):
    def test_real_chromium_collects_canonical_observation(self) -> None:
        required = os.environ.get("NUI_REQUIRE_REAL_PLAYWRIGHT") == "1"
        if not playwright_available():
            if required:
                self.fail("NUI_REQUIRE_REAL_PLAYWRIGHT=1 but Playwright is unavailable")
            self.skipTest("Playwright optional dependency is not installed")

        fixture = Path(__file__).resolve().parent / "fixtures" / "runtime_v11" / "live_visual_smoke.html"
        self.assertTrue(fixture.exists())
        with tempfile.TemporaryDirectory() as temp:
            capture = Path(temp) / "smoke.png"
            packet = collect_playwright_observation(
                fixture.resolve().as_uri(),
                selector="#nui-smoke-target",
                viewport={"width": 960, "height": 640, "dpr": 1},
                capture_path=capture.as_posix(),
            )
            validation = validate_browser_observation(packet)
            self.assertTrue(validation["valid"], validation["errors"])
            self.assertEqual(packet["collector"], "playwright")
            self.assertEqual(packet["observations"][0]["visible_text"], "NUI Live Visual Smoke")
            self.assertGreater(packet["observations"][0]["bounding_box"]["width"], 0)
            self.assertTrue(packet["observations"][0]["computed_style"]["display"])
            self.assertGreater(packet["document_metrics"]["client_width"], 0)
            self.assertTrue(capture.exists())
            self.assertTrue(packet["capture_ref"].startswith("file:"))


if __name__ == "__main__":
    unittest.main()
