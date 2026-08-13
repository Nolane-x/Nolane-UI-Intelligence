import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nolane_ui.source_intelligence import (
    plan_source_research,
    required_artifact_classes,
    validate_cross_source_synthesis,
    validate_source_mix,
    validate_source_research_dossier,
)


class SourceIntelligenceV6Tests(unittest.TestCase):
    def _animated_source(self):
        return {
            "id": "react-bits",
            "role": "animated-component-gallery",
            "drift": "very-high",
            "verify_live_before_use": True,
            "url": "https://github.com/DavidHDev/react-bits",
        }

    def _deep_dossier(self):
        return {
            "source_id": "react-bits",
            "source_role": "animated-component-gallery",
            "usage": "adapt",
            "snapshot": {
                "canonical_url": "https://github.com/DavidHDev/react-bits",
                "ref": "main",
                "commit_sha": "a" * 40,
                "retrieved_at": "2026-08-13",
            },
            "task_fit": {
                "need": "object-continuity motion for a spatial scientific explorer",
                "why_this_source": "contains multiple source-level continuity and reveal mechanisms",
                "source_role_fit": True,
            },
            "inspected_artifacts": [
                {"kind": "readme", "path": "README.md", "finding": "project scope", "evidence_ref": "repo:README"},
                {"kind": "license", "path": "LICENSE.md", "finding": "reuse boundary", "evidence_ref": "repo:LICENSE"},
                {"kind": "component-source", "path": "src/content/Animations/Example/Example.tsx", "finding": "state and animation mechanism", "evidence_ref": "repo:component"},
                {"kind": "demo-example", "path": "src/demo/ExampleDemo.jsx", "finding": "intended interaction context", "evidence_ref": "repo:demo"},
                {"kind": "dependency-config", "path": "package.json", "finding": "runtime dependencies", "evidence_ref": "repo:package"},
                {"kind": "motion-behavior", "path": "src/content/Animations/Example/Example.tsx", "finding": "interruption and transform behavior", "evidence_ref": "repo:motion"},
                {"kind": "reduced-motion", "path": "src/content/Animations/Example/Example.tsx", "finding": "reduced motion handling is absent and must be locally supplied", "evidence_ref": "repo:motion"},
                {"kind": "performance-guidance", "path": "package.json", "finding": "dependency and runtime cost must be measured locally because upstream guidance is incomplete", "evidence_ref": "repo:package"},
                {"kind": "accessibility-fallback", "path": "src/demo/ExampleDemo.jsx", "finding": "visual effect needs a local semantic and reduced-motion fallback", "evidence_ref": "repo:demo"},
            ],
            "mechanisms": [
                {
                    "name": "shared-object continuity through transform interpolation",
                    "evidence_artifact_paths": ["src/content/Animations/Example/Example.tsx", "src/demo/ExampleDemo.jsx"],
                    "transfer_boundary": "reuse the continuity relationship, not the demo styling or labels",
                    "product_fit": "supports spatial orientation during model-state transitions",
                }
            ],
            "contradictions": ["demo has no product-specific keyboard contract"],
            "integration_hazards": ["must add reduced-motion alternative and preserve semantic focus"],
            "license": {"status": "verified-compatible", "evidence_refs": ["repo:LICENSE"]},
            "accessibility": {"status": "mixed", "evidence_refs": ["repo:demo", "repo:motion"]},
            "performance": {"status": "reviewed", "evidence_refs": ["repo:package", "repo:component"]},
            "unread_material": ["unrelated background components"],
            "stop_reason": "mechanism, dependencies, license, runtime behavior, and missing a11y obligations are sufficiently characterized for this adaptation decision",
        }

    def test_role_specific_obligations_are_not_one_generic_checklist(self):
        animated = required_artifact_classes("animated-component-gallery", "adapt", "exceptional", "routine")
        primitive = required_artifact_classes("headless-primitive", "adopt", "polished", "routine")
        icons = required_artifact_classes("icon-system", "adapt", "flagship", "routine")
        self.assertIn("component-source", animated)
        self.assertIn("motion-behavior", animated)
        self.assertIn("interaction-tests", primitive)
        self.assertIn("accessibility-guidance", primitive)
        self.assertIn("icon-catalog", icons)
        self.assertIn("symbol-conventions", icons)
        self.assertNotEqual(animated, primitive)
        self.assertNotEqual(primitive, icons)

    def test_readme_only_material_research_fails(self):
        dossier = self._deep_dossier()
        dossier["inspected_artifacts"] = [
            {"kind": "readme", "path": "README.md", "finding": "looks useful", "evidence_ref": "repo:README"},
            {"kind": "license", "path": "LICENSE.md", "finding": "license", "evidence_ref": "repo:LICENSE"},
        ]
        result = validate_source_research_dossier(dossier, self._animated_source())
        self.assertFalse(result["valid"])
        self.assertTrue(any("component-source" in error for error in result["errors"]))
        self.assertTrue(any("README-only" in error for error in result["errors"]))

    def test_high_drift_material_source_requires_pinned_snapshot(self):
        dossier = self._deep_dossier()
        dossier["snapshot"]["commit_sha"] = ""
        result = validate_source_research_dossier(dossier, self._animated_source())
        self.assertFalse(result["valid"])
        self.assertTrue(any("commit_sha" in error for error in result["errors"]))

    def test_deep_role_specific_dossier_passes(self):
        result = validate_source_research_dossier(self._deep_dossier(), self._animated_source())
        self.assertTrue(result["valid"], result["errors"])
        self.assertGreaterEqual(result["artifact_class_count"], 7)
        self.assertEqual(result["mechanism_count"], 1)

    def test_research_plan_explains_each_required_artifact_class(self):
        plan = plan_source_research(
            self._animated_source(),
            {"visual_ambition": "exceptional", "risk_class": "routine"},
            "adapt",
        )
        self.assertEqual(plan["source_id"], "react-bits")
        self.assertTrue(plan["snapshot_required"])
        self.assertGreaterEqual(len(plan["obligations"]), 6)
        self.assertTrue(all(item.get("why") for item in plan["obligations"]))

    def test_gallery_monoculture_is_blocked_for_exceptional_source_mix(self):
        record = {
            "visual_ambition": "exceptional",
            "source_required": True,
            "sources": [
                {"source_id": "react-bits", "role": "animated-component-gallery", "influence": 0.5},
                {"source_id": "magic-ui", "role": "animated-component-gallery", "influence": 0.3},
                {"source_id": "motion-primitives", "role": "animated-component-gallery", "influence": 0.2},
            ],
            "monoculture_justification": "",
        }
        result = validate_source_mix(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("monoculture" in error.lower() for error in result["errors"]))

    def test_cross_source_synthesis_requires_layer_ownership_and_conflict_resolution(self):
        bad = {
            "sources": ["radix-primitives", "react-bits"],
            "layers": {
                "semantics": {"owner": "radix-primitives"},
                "motion": {"owner": "react-bits"},
            },
            "conflicts": [{"dimension": "focus", "sources": ["radix-primitives", "react-bits"], "resolution": ""}],
            "local_system": {},
        }
        bad_result = validate_cross_source_synthesis(bad)
        self.assertFalse(bad_result["valid"])
        self.assertTrue(any("local_system" in e or "resolution" in e for e in bad_result["errors"]))

        good = {
            "sources": ["radix-primitives", "react-bits"],
            "layers": {
                "semantics": {"owner": "radix-primitives", "local_override": "product action registry and naming"},
                "interaction": {"owner": "local", "local_override": "canonical keyboard/focus state machine"},
                "visual": {"owner": "local", "local_override": "project tokens and art direction"},
                "motion": {"owner": "react-bits", "local_override": "motion grammar and reduced-motion policy"},
            },
            "conflicts": [
                {"dimension": "focus", "sources": ["radix-primitives", "react-bits"], "resolution": "Radix semantics govern focus; the visual effect cannot move focus."}
            ],
            "local_system": {
                "tokens": "project-token-contract",
                "actions": "action-registry",
                "states": "state-matrix",
                "accessibility": "accessibility-contract",
            },
            "foreign_defaults_removed": ["demo labels", "demo radii", "demo color palette"],
        }
        good_result = validate_cross_source_synthesis(good)
        self.assertTrue(good_result["valid"], good_result["errors"])


if __name__ == "__main__":
    unittest.main()
