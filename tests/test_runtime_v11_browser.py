import unittest

from nolane_ui.runtime_v11.browser import normalize_browser_observation, validate_browser_observation


VALID = {
    "version": 11,
    "collector": "test-browser-driver",
    "url": "http://localhost:3000/settings",
    "viewport": {"width": 1440, "height": 900, "dpr": 2},
    "capabilities": {
        "geometry": True,
        "computed_style": True,
        "runtime_errors": True,
        "capture": True,
    },
    "capture_ref": "artifacts/settings-desktop.png",
    "observations": [{
        "locator": "#save-button",
        "bounding_box": {"x": 1200, "y": 820, "width": 120, "height": 44},
        "computed_style": {"display": "inline-flex", "outline": "rgb(0, 0, 0) none 0px"},
        "visible_text": "Save changes",
        "attributes": {"type": "submit"},
    }],
    "runtime_errors": [{"kind": "console-error", "message": "Failed to load preference state"}],
}


class RuntimeV11BrowserTests(unittest.TestCase):
    def test_valid_observation_packet_passes(self):
        result = validate_browser_observation(VALID)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["observation_count"], 1)
        self.assertEqual(result["runtime_error_count"], 1)

    def test_malformed_geometry_is_rejected(self):
        record = {**VALID, "observations": [{**VALID["observations"][0], "bounding_box": {"x": 0, "y": 0, "width": -1, "height": 44}}]}
        result = validate_browser_observation(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("width" in error.lower() for error in result["errors"]))

    def test_capture_capability_requires_capture_ref(self):
        record = dict(VALID)
        record.pop("capture_ref")
        result = validate_browser_observation(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("capture_ref" in error for error in result["errors"]))

    def test_capability_limited_packet_does_not_invent_missing_evidence(self):
        record = {
            "version": 11,
            "collector": "read-only-host",
            "url": "http://localhost:3000",
            "viewport": {"width": 390, "height": 844, "dpr": 3},
            "capabilities": {"geometry": False, "computed_style": False, "runtime_errors": False, "capture": False},
            "observations": [{"locator": "main", "visible_text": "Hello"}],
            "runtime_errors": [],
        }
        result = validate_browser_observation(record)
        self.assertTrue(result["valid"], result["errors"])
        normalized = normalize_browser_observation(record)
        self.assertNotIn("capture_ref", normalized)
        self.assertNotIn("bounding_box", normalized["observations"][0])
        self.assertFalse(normalized["capabilities"]["computed_style"])

    def test_runtime_error_requires_kind_and_message(self):
        record = {**VALID, "runtime_errors": [{"kind": "console-error"}]}
        result = validate_browser_observation(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("message" in error.lower() for error in result["errors"]))

    def test_normalization_has_stable_observation_order(self):
        record = {**VALID, "observations": [
            {**VALID["observations"][0], "locator": "#z"},
            {**VALID["observations"][0], "locator": "#a"},
        ]}
        normalized = normalize_browser_observation(record)
        self.assertEqual([item["locator"] for item in normalized["observations"]], ["#a", "#z"])


if __name__ == "__main__":
    unittest.main()
