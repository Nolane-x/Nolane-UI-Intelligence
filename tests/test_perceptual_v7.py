import copy
import unittest

from src.nolane_ui.perceptual import validate_rendered_perception


def base_record():
    return {
        "status": "PASS",
        "capture_matrix": [
            {
                "viewport": {"width": 1440, "height": 960, "dpr": 1},
                "state": "default",
                "artifact": "desktop-default.png",
                "renderer": "chromium",
            },
            {
                "viewport": {"width": 390, "height": 844, "dpr": 3},
                "state": "default",
                "artifact": "mobile-default.png",
                "renderer": "webkit",
            },
            {
                "viewport": {"width": 390, "height": 844, "dpr": 3},
                "state": "menu-open",
                "artifact": "mobile-menu-open.png",
                "renderer": "webkit",
            },
        ],
        "required_states": ["default", "menu-open"],
        "observations": {
            "focal_order": ["subject-native hero", "primary task", "supporting evidence"],
            "hierarchy": {
                "primary": "subject-native hero",
                "secondary": "primary task",
                "quiet_regions": ["utility rail", "footer"],
            },
            "resolved_typography": [
                {
                    "role": "display",
                    "intended": "Display Variable",
                    "resolved": "Display Variable",
                    "loaded": True,
                    "fallback_reviewed": True,
                },
                {
                    "role": "body",
                    "intended": "System Sans",
                    "resolved": "System Sans",
                    "loaded": True,
                    "fallback_reviewed": True,
                },
            ],
            "signature_mechanism": {
                "name": "live material map",
                "subject_link": "maps the product's actual spatial inventory",
                "removal_cost": 0.82,
                "observed_in": ["desktop-default.png", "mobile-default.png"],
            },
            "material_structure": {
                "surface_roles": ["canvas", "control", "evidence", "overlay"],
                "boundary_density": 0.32,
                "material_variety": 0.68,
            },
        },
        "reference_comparison": {
            "references": ["reference-a", "reference-b"],
            "dimensions": ["hierarchy", "material", "type", "signature"],
            "result": "direction is more subject-specific while preserving task clarity",
        },
        "critique_cycle": {
            "weaknesses": [
                {
                    "finding": "mobile utility rail competed with primary task",
                    "fix": "collapsed utility rail into contextual drawer",
                    "verified_in": "mobile-default.png",
                }
            ],
            "adequacy": "PASS",
        },
    }


class PerceptualV7Tests(unittest.TestCase):
    def test_high_ambition_rejects_screenshot_theater(self):
        record = {"status": "PASS", "screenshot": "hero.png"}
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("capture_matrix" in e for e in result["errors"]))

    def test_high_ambition_accepts_multi_viewport_state_observation(self):
        result = validate_rendered_perception(base_record(), high_ambition=True)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["decision"], "PASS")

    def test_responsive_work_requires_multiple_viewports(self):
        record = base_record()
        record["responsive_material"] = True
        record["capture_matrix"] = [record["capture_matrix"][0]]
        result = validate_rendered_perception(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("viewports" in e for e in result["errors"]))

    def test_required_states_must_be_captured(self):
        record = base_record()
        record["required_states"] = ["default", "menu-open", "error"]
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("error" in e for e in result["errors"]))

    def test_typography_requires_actual_resolved_font_evidence(self):
        record = base_record()
        record["observations"]["resolved_typography"][0].pop("resolved")
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("resolved" in e for e in result["errors"]))

    def test_signature_must_be_subject_linked_and_observed(self):
        record = base_record()
        record["observations"]["signature_mechanism"] = {
            "name": "glow orb",
            "subject_link": "",
            "removal_cost": 0.1,
            "observed_in": [],
        }
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("signature" in e for e in result["errors"]))

    def test_material_motion_requires_temporal_sequence_and_reduced_motion(self):
        record = base_record()
        record["motion_material"] = True
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("temporal" in e or "reduced" in e for e in result["errors"]))

        record["temporal_evidence"] = {
            "sequence": [
                {"state": "before", "artifact": "before.png", "time_ms": 0},
                {"state": "transition", "artifact": "during.png", "time_ms": 180},
                {"state": "settled", "artifact": "after.png", "time_ms": 420},
            ],
            "semantic_purpose": "preserve spatial continuity while replacing the detail panel",
            "reduced_motion_equivalent": "instant content replacement with retained focus and no spatial sweep",
        }
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertTrue(result["valid"], result["errors"])

    def test_pixel_diff_requires_renderer_environment_tolerance_and_rationale(self):
        record = base_record()
        record["pixel_diff"] = {
            "delta": 112,
            "tolerance": 150,
            "renderer": "webgl2",
            "environment": "ubuntu-24.04 chromium 140",
            "rationale": "font edge anti-aliasing variance on otherwise stable geometry",
            "baseline": "baseline.png",
            "candidate": "candidate.png",
        }
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertTrue(result["valid"], result["errors"])

        bad = copy.deepcopy(record)
        del bad["pixel_diff"]["rationale"]
        result = validate_rendered_perception(bad, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("pixel_diff" in e for e in result["errors"]))

    def test_pixel_diff_over_tolerance_blocks_even_when_prose_says_pass(self):
        record = base_record()
        record["pixel_diff"] = {
            "delta": 151,
            "tolerance": 150,
            "renderer": "canvas",
            "environment": "linux chromium",
            "rationale": "calibrated text rendering tolerance",
            "baseline": "baseline.png",
            "candidate": "candidate.png",
        }
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("exceeds calibrated tolerance" in e for e in result["errors"]))

    def test_high_ambition_requires_reference_comparison_and_actual_critique(self):
        record = base_record()
        record.pop("reference_comparison")
        record["critique_cycle"] = {"weaknesses": [], "adequacy": "PASS"}
        result = validate_rendered_perception(record, high_ambition=True)
        self.assertFalse(result["valid"])
        self.assertTrue(any("reference" in e for e in result["errors"]))
        self.assertTrue(any("critique" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
