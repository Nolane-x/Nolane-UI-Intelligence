import json
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.contracts import NUI_FINDING_REQUIRED_FIELDS
from nolane_ui.runtime_v11.detector import scan_text
from nolane_ui.runtime_v11.registry import validate_rule_registry


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "runtime_v11"
REGISTRY = json.loads((ROOT / "knowledge" / "runtime-detector-rules-v11.json").read_text(encoding="utf-8"))


class RuntimeV11DetectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        validation = validate_rule_registry(REGISTRY)
        if not validation["valid"]:
            raise AssertionError(validation["errors"])

    def test_defective_html_emits_expected_rule_families(self):
        findings = scan_text(
            (FIXTURES / "defects.html").read_text(encoding="utf-8"),
            "tests/fixtures/runtime_v11/defects.html",
            REGISTRY,
            tier="session",
        )
        ids = {finding["runtime"]["rule_id"] for finding in findings}
        self.assertIn("runtime.integrity.broken-image-src", ids)
        self.assertIn("runtime.integrity.empty-navigation-target", ids)
        self.assertIn("runtime.accessibility.image-alt-omission", ids)
        self.assertIn("runtime.accessibility.focus-visibility-suppressed", ids)
        self.assertIn("runtime.layout.viewport-minimum-width", ids)
        self.assertIn("runtime.layout.content-clipping-risk", ids)
        self.assertIn("runtime.genericness.repeated-nested-card-shell", ids)
        self.assertIn("runtime.genericness.decorative-gradient-text", ids)

    def test_clean_fixture_avoids_false_positive_families(self):
        findings = scan_text(
            (FIXTURES / "clean.html").read_text(encoding="utf-8"),
            "tests/fixtures/runtime_v11/clean.html",
            REGISTRY,
            tier="session",
        )
        ids = {finding["runtime"]["rule_id"] for finding in findings}
        forbidden = {
            "runtime.integrity.broken-image-src",
            "runtime.integrity.empty-navigation-target",
            "runtime.accessibility.image-alt-omission",
            "runtime.accessibility.focus-visibility-suppressed",
            "runtime.layout.viewport-minimum-width",
            "runtime.layout.content-clipping-risk",
            "runtime.genericness.repeated-nested-card-shell",
        }
        self.assertFalse(ids & forbidden, ids)

    def test_edit_tier_excludes_session_genericness(self):
        findings = scan_text(
            (FIXTURES / "defects.html").read_text(encoding="utf-8"),
            "defects.html",
            REGISTRY,
            tier="edit",
        )
        ids = {finding["runtime"]["rule_id"] for finding in findings}
        self.assertIn("runtime.integrity.broken-image-src", ids)
        self.assertIn("runtime.integrity.empty-navigation-target", ids)
        self.assertNotIn("runtime.genericness.repeated-nested-card-shell", ids)
        self.assertNotIn("runtime.genericness.decorative-gradient-text", ids)

    def test_hard_coded_color_requires_token_owned_context(self):
        source = ".label { color: #6f6f73; }"
        without_contract = scan_text(source, "theme.css", REGISTRY, tier="session")
        with_contract = scan_text(
            source,
            "theme.css",
            REGISTRY,
            tier="session",
            context={"design_system": {"token_owned_axes": ["color"]}},
        )
        self.assertNotIn(
            "runtime.design-system.hard-coded-color",
            {item["runtime"]["rule_id"] for item in without_contract},
        )
        self.assertIn(
            "runtime.design-system.hard-coded-color",
            {item["runtime"]["rule_id"] for item in with_contract},
        )

    def test_findings_have_complete_nui_fields_and_stable_order(self):
        source = '<a href="">A</a>\n<img src="">'
        first = scan_text(source, "sample.html", REGISTRY, tier="session")
        second = scan_text(source, "sample.html", REGISTRY, tier="session")
        self.assertEqual(first, second)
        self.assertEqual(
            [(item["runtime"]["line"], item["runtime"]["rule_id"]) for item in first],
            sorted((item["runtime"]["line"], item["runtime"]["rule_id"]) for item in first),
        )
        for finding in first:
            for field in NUI_FINDING_REQUIRED_FIELDS:
                self.assertIn(field, finding)
            self.assertTrue(finding["evidence"])
            self.assertEqual(finding["status"], "open")

    def test_same_rule_line_is_deduplicated(self):
        source = '<img src="" src="">'
        findings = scan_text(source, "duplicate.html", REGISTRY, tier="session")
        broken = [
            item for item in findings
            if item["runtime"]["rule_id"] == "runtime.integrity.broken-image-src"
        ]
        self.assertEqual(len(broken), 1)


if __name__ == "__main__":
    unittest.main()
