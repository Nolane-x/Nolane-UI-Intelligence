import unittest

from nolane_ui.flagship import validate_flagship_visual_synthesis


def complete_packet():
    return {
        "ambition": "exceptional",
        "visual_thesis": "A living field notebook for coastal ecology: evidence first, salt-air tactility second, controls recede until needed.",
        "direction_candidates": [
            {
                "id": "field-notebook",
                "composition": "asymmetric specimen rail with one dominant observation canvas",
                "type_system": "editorial serif display paired with quiet grotesk utility text",
                "material_system": "paper-fiber content field with ink-like separators and restrained translucent tools",
                "signature_mechanism": "tide-line annotations connect evidence, time and location",
            },
            {
                "id": "instrument-panel",
                "composition": "dense instrument spine around a wide live transect",
                "type_system": "condensed numeric display with neutral humanist reading text",
                "material_system": "matte instrument surfaces with luminous measurement accents",
                "signature_mechanism": "measurement ticks become navigation and progress",
            },
            {
                "id": "coastal-atlas",
                "composition": "full-bleed geographic plate interrupted by editorial evidence islands",
                "type_system": "large cartographic titles with compact sans annotations",
                "material_system": "map layers, contour lines and photographic specimen windows",
                "signature_mechanism": "contour geometry expands into section boundaries",
            },
        ],
        "selected_direction_id": "field-notebook",
        "selection_rationale": "Best preserves scientific evidence while giving the product an ownable tactile memory without turning the workflow into spectacle.",
        "attention_hierarchy": [
            {"rank": 1, "role": "primary-evidence", "visual_mechanism": "scale + open field + subject media"},
            {"rank": 2, "role": "current-observation", "visual_mechanism": "type contrast + proximity"},
            {"rank": 3, "role": "controls", "visual_mechanism": "low-chroma compact utility rail"},
        ],
        "typography": {
            "roles": ["display", "reading", "utility", "numeric"],
            "measure_strategy": "reading columns stay within a deliberate comfortable measure; evidence labels stay terse",
            "optical_hierarchy": "display contrast is earned by narrative moments; utility text never competes with evidence",
            "fallback_behavior": "fallback metrics preserve wrapping and hierarchy rather than only font-family similarity",
        },
        "composition": {
            "grid_logic": "content-led asymmetric grid anchored to specimen and map geometry",
            "density_rhythm": "compressed evidence clusters alternate with quiet inspection fields",
            "edge_logic": "primary evidence may break the grid; controls align to stable rails",
            "responsive_transform": "desktop split field becomes a mobile evidence sequence; utilities move to a bottom sheet",
        },
        "color_material": {
            "semantic_palette": "mineral neutrals carry structure; algae green marks live state; warning amber is reserved for risk",
            "chroma_budget": "high chroma is localized to state and focal evidence, never spread evenly",
            "depth_model": "content is the base plane; tools float only when spatial separation improves action clarity",
            "surface_rule": "translucency is allowed only for transient controls over context that must remain visible",
            "dark_mode_behavior": "preserve evidence contrast and material hierarchy without simple palette inversion",
        },
        "motion": {
            "purpose": "maintain spatial continuity between observation, specimen and location",
            "timing_model": "short direct feedback; longer transitions only for meaningful context changes",
            "gesture_relation": "motion direction follows the initiating spatial action",
            "reduced_motion": "replace travel/morphing with immediate state change plus opacity emphasis",
        },
        "signature": {
            "mechanism": "tide-line annotation",
            "subject_link": "the mark derives from measured coastal water levels and annotation practice",
            "memory_hook": "users can describe the interface as the notebook whose tide line connects evidence",
            "restraint_rule": "use only where evidence changes through place or time",
        },
        "reference_frontier": [
            {"id": "r1", "mechanism": "editorial scale contrast", "transfer_boundary": "mechanism only; no layout cloning"},
            {"id": "r2", "mechanism": "instrument density zoning", "transfer_boundary": "density logic only; no trade dress"},
            {"id": "r3", "mechanism": "cartographic annotation rhythm", "transfer_boundary": "annotation grammar only; derive geometry from product data"},
        ],
        "generic_transfer_test": {
            "verdict": "FAILS_TRANSFER",
            "reason": "Removing coastal evidence, tide measurements and specimen relationships destroys the composition and signature rather than leaving a reusable SaaS shell.",
        },
        "rendered_states": [
            {"id": "desktop-light", "viewport": "wide", "structural_changes": ["split evidence field", "persistent specimen rail"]},
            {"id": "mobile-light", "viewport": "narrow", "structural_changes": ["sequenced evidence", "utilities become bottom sheet"]},
            {"id": "desktop-dark-loading", "viewport": "wide", "structural_changes": ["media fallback preserves focal hierarchy", "dark material mapping"]},
        ],
        "critique_cycles": [
            {"category": "perception", "finding": "utility rail competed with specimen labels", "correction": "reduced utility contrast and tightened grouping", "verified_in": "desktop-light"},
            {"category": "responsive", "finding": "mobile crop hid the specimen scale cue", "correction": "changed to a scale-preserving art-directed crop", "verified_in": "mobile-light"},
        ],
        "anti_generic_audit": {
            "rejected_attractors": ["equal-weight card grid", "decorative gradient orb", "uniform pill treatment"],
            "replacement_mechanisms": ["evidence-led field hierarchy", "subject photography", "role-specific control geometry"],
            "silhouette_observation": "blurred thumbnail still has one large observation field, a narrow specimen rail and an identifiable annotation line",
        },
        "decision": "PASS",
    }


class V8FlagshipVisualSynthesisTests(unittest.TestCase):
    def test_complete_exceptional_packet_passes(self):
        result = validate_flagship_visual_synthesis(complete_packet())
        self.assertTrue(result["valid"], result["errors"])

    def test_requires_three_meaningfully_distinct_directions(self):
        packet = complete_packet()
        packet["direction_candidates"] = packet["direction_candidates"][:2]
        result = validate_flagship_visual_synthesis(packet)
        self.assertFalse(result["valid"])
        self.assertTrue(any("three" in e.lower() for e in result["errors"]))

    def test_rejects_direction_candidates_that_only_rename_same_solution(self):
        packet = complete_packet()
        first = dict(packet["direction_candidates"][0])
        packet["direction_candidates"] = [dict(first, id=f"d{i}") for i in range(3)]
        result = validate_flagship_visual_synthesis(packet)
        self.assertFalse(result["valid"])
        self.assertTrue(any("converged" in e.lower() for e in result["errors"]))

    def test_generic_transfer_must_fail_for_exceptional_work(self):
        packet = complete_packet()
        packet["generic_transfer_test"] = {"verdict": "TRANSFERS", "reason": "works for any dashboard"}
        result = validate_flagship_visual_synthesis(packet)
        self.assertFalse(result["valid"])
        self.assertTrue(any("transfer" in e.lower() for e in result["errors"]))

    def test_responsive_evidence_requires_structural_recomposition(self):
        packet = complete_packet()
        packet["rendered_states"][1]["structural_changes"] = []
        result = validate_flagship_visual_synthesis(packet)
        self.assertFalse(result["valid"])
        self.assertTrue(any("structural" in e.lower() for e in result["errors"]))

    def test_two_closed_critique_cycles_are_required(self):
        packet = complete_packet()
        packet["critique_cycles"] = packet["critique_cycles"][:1]
        result = validate_flagship_visual_synthesis(packet)
        self.assertFalse(result["valid"])
        self.assertTrue(any("critique" in e.lower() for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
