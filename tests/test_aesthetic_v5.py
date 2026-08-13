import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.aesthetic import (
    decide_aesthetic_basin,
    mandatory_aesthetic_routes,
    validate_aesthetic_attractor_audit,
    validate_encoding_provenance_table,
    validate_experiential_intent,
    validate_signature_depth_contract,
    validate_skill_interaction_evidence,
    validate_visual_legibility_evidence,
    validate_workspace_visual_matrix,
)


class AestheticKernelV5Tests(unittest.TestCase):
    def test_exceptional_ambition_hard_routes_full_visual_spine(self):
        required = mandatory_aesthetic_routes({
            "visual_ambition": "exceptional",
            "visual_freedom": "high",
            "material_data_visualization": True,
            "aspirational_identity": True,
            "magnitude_language": True,
            "product_wide": True,
        })
        expected = {
            "preserving-experiential-intent", "directing-visual-ambition",
            "exploring-aesthetic-directions", "researching-visual-references",
            "directing-visual-hierarchy", "crafting-typography", "crafting-color",
            "crafting-spacing-and-rhythm", "crafting-depth-and-surfaces",
            "directing-iconography-and-imagery", "designing-motion", "preventing-generic-ui",
            "detecting-aesthetic-attractors", "engineering-visual-legibility",
            "directing-visual-energy", "deepening-signature-mechanisms",
            "critiquing-visual-design", "critiquing-aesthetic-adequacy",
            "iterating-rendered-visual-design", "escaping-aesthetic-basins",
            "proving-visual-encoding-semantics", "modeling-aspirational-identity",
            "composing-spatial-dramaturgy", "evaluating-perceptual-diversity",
        }
        self.assertTrue(expected.issubset(required), sorted(expected - required))

    def test_experiential_intent_cannot_be_replaced_by_operational_proxies(self):
        result = validate_experiential_intent({
            "desired_feelings": ["awe", "mastery"],
            "forbidden_feelings": ["ordinary SaaS"],
            "identity_projection": "principal scientist",
            "emotional_intensity": 0.92,
            "memorability_target": 0.90,
            "magnitude_target": {k: "extreme" for k in ("scope", "data", "spatial", "institutional", "temporal", "network", "visual")},
            "source_language": ["extremely beautiful", "feel like the highest-level scientist"],
            "operational_proxies": ["hierarchy", "density"],
        })
        self.assertTrue(result["valid"], result)
        collapsed = validate_experiential_intent({"operational_proxies": ["hierarchy", "density", "restrained chroma"]})
        self.assertFalse(collapsed["valid"])
        self.assertTrue(any("desired_feelings" in e for e in collapsed["errors"]), collapsed)

    def test_attractor_audit_escalates_repeated_low_specificity_mechanisms(self):
        result = validate_aesthetic_attractor_audit({
            "mechanisms": [{
                "name": "tiny-uppercase-metadata",
                "semantic_necessity": 0.1,
                "subject_specificity": 0.1,
                "frequency": 80,
                "information_gain": 0.1,
                "emotional_contribution": 0.1,
                "removal_cost": 0.1,
            }],
            "global_metrics": {
                "boundary_density": 0.8, "edge_density": 0.8, "surface_entropy": 0.1,
                "boundary_repetition": 0.9, "material_variety": 0.1, "quiet_region_ratio": 0.05,
            },
        })
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertIn("tiny-uppercase-metadata", result["probable_tropes"])

    def test_legibility_blocks_required_microtext_and_compound_risk(self):
        result = validate_visual_legibility_evidence({
            "samples": [
                {"id": "required-label", "computed_px": 8.0, "required_information": True, "semantic_reason": "dense table", "low_contrast": True, "uppercase": True, "tracked": True},
            ],
            "resolved_fonts": [{"role": "body", "intended": "Inter", "resolved": "Arial", "loading": "fallback", "fallback_delta_reviewed": False}],
        })
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertTrue(any("required information" in e for e in result["errors"]), result)
        self.assertTrue(any("fallback" in e.lower() for e in result["errors"]), result)

    def test_encoding_provenance_requires_meaning_or_decorative_declaration(self):
        bad = validate_encoding_provenance_table({"channels": [
            {"channel": "position_x", "meaning": "capability family", "decorative": False},
            {"channel": "radius", "decorative": False},
        ]})
        self.assertFalse(bad["valid"])
        good = validate_encoding_provenance_table({"channels": [
            {"channel": "position_x", "meaning": "capability family", "decorative": False},
            {"channel": "orbit_angle", "meaning": "", "decorative": True},
        ]})
        self.assertTrue(good["valid"], good)

    def test_signature_depth_rejects_decorative_signature(self):
        result = validate_signature_depth_contract({
            "semantic_depth": 0.1, "interaction_depth": 0.1, "visual_depth": 0.9,
            "information_gain": 0.1, "product_specificity": 0.1, "reusability": 0.9,
            "memorability": 0.7, "failure_if_removed": 0.0,
            "required_level": "high",
        })
        self.assertEqual(result["decision"], "BLOCKED")

    def test_workspace_matrix_detects_template_repetition(self):
        screens = []
        for i in range(6):
            screens.append({
                "screen": f"s{i}", "signature": "same", "dominant_geometry": "three-pane",
                "density": "dense", "main_visualization": "radial", "surface_pattern": "hairline panes",
                "typographic_gesture": "micro uppercase mono", "color_mass": "near-black cyan",
                "interaction_signature": "inspector",
            })
        result = validate_workspace_visual_matrix({"screens": screens})
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertIn("template repetition", " ".join(result["errors"]).lower())

    def test_basin_escape_rediverges_instead_of_polishing_wrong_basin(self):
        result = decide_aesthetic_basin({
            "affective_fit": 0.55, "affective_target": 0.9,
            "distinctiveness": 0.5, "distinctiveness_target": 0.8,
            "reference_losses": 2, "signature_depth_pass": False,
            "adequacy_status": "FAIL",
        })
        self.assertEqual(result["decision"], "RE_DIVERGE")

    def test_skill_interaction_evidence_requires_factorial_and_mutation_detection(self):
        bad = validate_skill_interaction_evidence({"factorial_cases": [], "semantic_mutations": []})
        self.assertFalse(bad["valid"])
        good = validate_skill_interaction_evidence({
            "factorial_cases": [{"id": "dense-science", "skills": ["crafting-spacing-and-rhythm", "crafting-color", "preventing-generic-ui"], "baseline": "A", "combined": "B", "objective_delta_reviewed": True}],
            "semantic_mutations": [{"id": "preserve-discard", "mutation": "preserve→discard", "target_skill": "preserving-experiential-intent", "detected_by": ["AA-01"], "expected": "FAIL"}],
        })
        self.assertTrue(good["valid"], good)


if __name__ == "__main__":
    unittest.main()
