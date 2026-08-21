import json
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.browser import browser_observation_findings
from nolane_ui.runtime_v11.contracts import NUI_FINDING_REQUIRED_FIELDS


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT / "knowledge" / "runtime-detector-rules-v11.json").read_text(encoding="utf-8"))


def packet(*, overflow=True, runtime_error=True, occlusion=True):
    return {
        "version": 11,
        "collector": "test-driver",
        "url": "http://localhost:3000/dashboard",
        "viewport": {"width": 390, "height": 844, "dpr": 3},
        "capabilities": {
            "geometry": True,
            "computed_style": True,
            "runtime_errors": True,
            "capture": True,
            "document_metrics": True,
            "occlusion": True,
        },
        "capture_ref": "artifacts/mobile-dashboard.png",
        "document_metrics": {
            "scroll_width": 520 if overflow else 390,
            "client_width": 390,
            "scroll_height": 1200,
            "client_height": 844,
        },
        "observations": [{
            "locator": "#balance-label",
            "bounding_box": {"x": 16, "y": 120, "width": 180, "height": 30},
            "computed_style": {"display": "block", "opacity": "1"},
            "visible_text": "Current balance",
            "attributes": {},
            "occluded_by": ["#floating-toolbar"] if occlusion else [],
            "essential_text": True,
        }],
        "runtime_errors": (
            [{"kind": "uncaught-exception", "message": "Cannot read properties of undefined"}]
            if runtime_error else []
        ),
    }


class RuntimeV11BrowserFindingTests(unittest.TestCase):
    def test_browser_packet_emits_runtime_overflow_and_occlusion_rules(self):
        findings = browser_observation_findings(packet(), REGISTRY)
        ids = {item["runtime"]["rule_id"] for item in findings}
        self.assertIn("runtime.browser.script-error", ids)
        self.assertIn("runtime.browser.document-horizontal-overflow", ids)
        self.assertIn("runtime.browser.text-occlusion", ids)

    def test_clean_browser_packet_avoids_three_findings(self):
        findings = browser_observation_findings(
            packet(overflow=False, runtime_error=False, occlusion=False),
            REGISTRY,
        )
        ids = {item["runtime"]["rule_id"] for item in findings}
        self.assertFalse(ids & {
            "runtime.browser.script-error",
            "runtime.browser.document-horizontal-overflow",
            "runtime.browser.text-occlusion",
        })

    def test_browser_findings_satisfy_nui_finding_vocabulary(self):
        findings = browser_observation_findings(packet(), REGISTRY)
        self.assertGreaterEqual(len(findings), 3)
        for finding in findings:
            for field in NUI_FINDING_REQUIRED_FIELDS:
                self.assertIn(field, finding)
            self.assertTrue(finding["evidence"])
            self.assertEqual(finding["runtime"]["engine"], "browser")
            self.assertEqual(finding["runtime"]["capture_ref"], "artifacts/mobile-dashboard.png")

    def test_occlusion_capability_is_required_to_claim_occlusion(self):
        record = packet(overflow=False, runtime_error=False, occlusion=False)
        record["capabilities"]["occlusion"] = False
        record["observations"][0]["occluded_by"] = ["#toolbar"]
        with self.assertRaises(ValueError):
            browser_observation_findings(record, REGISTRY)


if __name__ == "__main__":
    unittest.main()
