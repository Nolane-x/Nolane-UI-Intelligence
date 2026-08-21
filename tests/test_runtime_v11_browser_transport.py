from __future__ import annotations

import json
import unittest
from pathlib import Path

try:
    from nolane_ui.runtime_v11.browser_transport import (
        build_browser_transport_capability,
        require_transport_capabilities,
        validate_browser_transport_capability,
    )
except ModuleNotFoundError:
    def _missing(*args, **kwargs):
        raise AssertionError("Phase 5 browser transport API is missing")

    build_browser_transport_capability = _missing
    require_transport_capabilities = _missing
    validate_browser_transport_capability = _missing


CAPS = {
    "navigation": True,
    "geometry": True,
    "computed_style": True,
    "runtime_errors": True,
    "capture": True,
    "document_metrics": True,
    "occlusion": False,
    "rendered_metadata": True,
    "preview_injection": True,
    "hot_reload": False,
    "reload": True,
}


class RuntimeV11BrowserTransportTests(unittest.TestCase):
    def test_missing_required_capability_is_unknown_not_false_clean(self) -> None:
        record = build_browser_transport_capability("fake", CAPS)
        result = require_transport_capabilities(record, ["occlusion"])
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertEqual(result["missing"], ["occlusion"])
        self.assertEqual(result["claim_boundary"], "browser-transport-only")

    def test_ready_requires_every_named_capability(self) -> None:
        record = build_browser_transport_capability("fake", CAPS)
        result = require_transport_capabilities(record, ["geometry", "capture", "reload"])
        self.assertEqual(result["status"], "READY")
        self.assertEqual(result["missing"], [])

    def test_provider_name_never_changes_authority(self) -> None:
        record = build_browser_transport_capability("playwright", CAPS)
        self.assertEqual(record["provider"], "playwright")
        self.assertEqual(record["claim_boundary"], "browser-transport-only")
        text = json.dumps(record).lower()
        self.assertNotIn("verified", text)
        self.assertNotIn("released", text)
        self.assertNotIn("design_authority", text)

    def test_unknown_capability_name_is_rejected(self) -> None:
        bad = dict(CAPS)
        bad["magic_source_truth"] = True
        with self.assertRaises(ValueError):
            build_browser_transport_capability("fake", bad)

    def test_validator_rejects_missing_boolean_or_extra_authority_field(self) -> None:
        record = build_browser_transport_capability("fake", CAPS)
        broken = dict(record)
        broken["capabilities"] = dict(record["capabilities"])
        broken["capabilities"]["geometry"] = "yes"
        broken["release_authority"] = True
        validation = validate_browser_transport_capability(broken)
        self.assertFalse(validation["valid"])

    def test_required_unknown_name_is_rejected(self) -> None:
        record = build_browser_transport_capability("fake", CAPS)
        with self.assertRaises(ValueError):
            require_transport_capabilities(record, ["telepathy"])

    def test_schema_exists_and_lists_closed_capability_vocabulary(self) -> None:
        schema_path = Path(__file__).resolve().parents[1] / "schemas" / "runtime-browser-transport-v11.schema.json"
        self.assertTrue(schema_path.exists(), "Phase 5 browser transport schema is missing")
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        properties = schema["properties"]["capabilities"]["properties"]
        self.assertEqual(set(properties), set(CAPS))
        self.assertFalse(schema["properties"]["capabilities"]["additionalProperties"])


if __name__ == "__main__":
    unittest.main()
