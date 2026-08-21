from __future__ import annotations

import inspect
import tempfile
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.evidence import sha256_file
from nolane_ui.runtime_v11.preview import build_preview_candidate
from nolane_ui.runtime_v11.reobserve import compare_runtime_observations

try:
    from nolane_ui.runtime_v11.live_visual import (
        accept_live_visual_preview,
        assess_visual_observation_capabilities,
        prepare_live_visual_selection,
    )
except ModuleNotFoundError:
    def _missing(*args, **kwargs):
        raise AssertionError("Phase 5 live visual coordinator API is missing")
    accept_live_visual_preview = _missing
    assess_visual_observation_capabilities = _missing
    prepare_live_visual_selection = _missing


def _candidate(path: str, digest: str, *, candidate_id: str, confidence: str = "HIGH", start: int = 0, end: int = 4):
    return {
        "candidate_id": candidate_id,
        "source_path": path,
        "source_digest": digest,
        "range": {"start": start, "end": end},
        "attribution_mechanisms": ["explicit-development-mapping"],
        "evidence_refs": [f"mapping:{candidate_id}"],
        "confidence": confidence,
    }


def _finding(finding_id: str, rule_id: str):
    return {
        "finding_id": finding_id,
        "runtime": {
            "rule_id": rule_id,
            "url": "https://example.test/",
            "locator": "#target",
        },
    }


class RuntimeV11LiveVisualTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "src").mkdir()
        self.a = self.root / "src" / "A.tsx"
        self.b = self.root / "src" / "B.tsx"
        self.a.write_text("AAAA source", encoding="utf-8")
        self.b.write_text("BBBB source", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_ambiguous_attribution_blocks_live_visual_selection(self) -> None:
        result = prepare_live_visual_selection(
            {"locator": "#target"},
            [
                _candidate("src/A.tsx", sha256_file(self.a), candidate_id="a"),
                _candidate("src/B.tsx", sha256_file(self.b), candidate_id="b"),
            ],
            repository_root=self.root,
        )
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["failure"], "ATTRIBUTION_AMBIGUOUS")
        self.assertEqual(result["claim_boundary"], "live-visual-closure-only")

    def test_missing_capability_only_keeps_affected_assertion_unknown(self) -> None:
        result = assess_visual_observation_capabilities(
            {
                "overflow": ["document_metrics"],
                "occlusion": ["occlusion"],
            },
            {
                "document_metrics": True,
                "occlusion": False,
            },
        )
        self.assertEqual(result["assertions"]["overflow"], "READY")
        self.assertEqual(result["assertions"]["occlusion"], "UNKNOWN")
        self.assertEqual(result["missing_by_assertion"]["occlusion"], ["occlusion"])

    def test_source_edit_during_observed_preview_returns_apply_conflict(self) -> None:
        digest = sha256_file(self.a)
        source_candidate = _candidate("src/A.tsx", digest, candidate_id="a")
        preview = build_preview_candidate(
            preview_id="preview-a",
            session_id="session-a",
            source_candidate=source_candidate,
            replacement="ZZZZ",
        )
        preview["state"] = "OBSERVED"
        preview["observation"] = {"refresh_status": "RELOAD_OK", "revision": "rev-a"}

        self.a.write_text("newer edit", encoding="utf-8")
        result = accept_live_visual_preview(preview, repository_root=self.root)

        self.assertEqual(result["status"], "APPLY_CONFLICT")
        self.assertEqual(result["failure"], "SOURCE_STALE")
        self.assertEqual(self.a.read_text(encoding="utf-8"), "newer edit")

    def test_reobserve_can_scope_capability_completeness_by_rule(self) -> None:
        signature = inspect.signature(compare_runtime_observations)
        self.assertIn("capabilities_by_rule", signature.parameters)

        result = compare_runtime_observations(
            [
                _finding("overflow-before", "runtime.browser.document-horizontal-overflow"),
                _finding("occlusion-before", "runtime.browser.text-occlusion"),
            ],
            [],
            capabilities_complete=True,
            capabilities_by_rule={
                "runtime.browser.document-horizontal-overflow": True,
                "runtime.browser.text-occlusion": False,
            },
        )
        statuses = {item["finding_id"]: item["status"] for item in result["closures"]}
        self.assertEqual(statuses["overflow-before"], "RESOLVED")
        self.assertEqual(statuses["occlusion-before"], "UNKNOWN")
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertEqual(result["claim_boundary"], "runtime-closure-only")


if __name__ == "__main__":
    unittest.main()
