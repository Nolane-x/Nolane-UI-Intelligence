import json
import unittest
from pathlib import Path

import nolane_ui
import nolane_ui.runtime_v11 as runtime
from nolane_ui.runtime_v11.doctor import REQUIRED_RUNTIME_ARTIFACTS, diagnose_runtime_state

ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11Phase4IntegrationTests(unittest.TestCase):
    def test_top_level_phase4_api_is_explicit_and_callable(self):
        names = [
            "compile_runtime_aesthetic_intent",
            "validate_runtime_aesthetic_intent",
            "evaluate_runtime_direction_candidates",
            "commit_runtime_direction",
            "assess_runtime_genericity",
            "validate_runtime_trend_registry",
            "runtime_product_substitution_assessment",
            "build_runtime_design_memory",
            "validate_runtime_design_memory",
            "assess_runtime_design_memory_staleness",
            "prepare_runtime_blinded_candidates",
            "validate_runtime_taste_judgment",
            "aggregate_runtime_taste_court",
            "plan_runtime_quality_residue_pass",
            "assess_runtime_quality_residue_closure",
        ]
        missing = [name for name in names if not callable(getattr(nolane_ui, name, None))]
        self.assertEqual(missing, [])

    def test_doctor_inventory_covers_phase4_runtime_contract(self):
        expected = {
            "knowledge/aesthetic-trend-tells-v11.json",
            "schemas/aesthetic-generation-intent-v11.schema.json",
            "schemas/aesthetic-trend-tells-v11.schema.json",
            "schemas/aesthetic-design-memory-v11.schema.json",
            "schemas/aesthetic-taste-court-v11.schema.json",
            "src/nolane_ui/runtime_v11/aesthetic_intent.py",
            "src/nolane_ui/runtime_v11/aesthetic_governor.py",
            "src/nolane_ui/runtime_v11/genericity.py",
            "src/nolane_ui/runtime_v11/design_memory.py",
            "src/nolane_ui/runtime_v11/taste_court.py",
            "src/nolane_ui/runtime_v11/quality_residue.py",
        }
        self.assertTrue(expected.issubset(set(REQUIRED_RUNTIME_ARTIFACTS)), expected - set(REQUIRED_RUNTIME_ARTIFACTS))
        report = diagnose_runtime_state(ROOT)
        self.assertTrue(report["valid"], report["findings"])

    def test_phase4_end_to_end_keeps_generation_and_release_authority_separate(self):
        intent = runtime.compile_aesthetic_intent({
            "intent_id": "flagship-ops",
            "revision": "rev-phase4",
            "scope": ["app/page.tsx"],
            "ambition": "HIGH",
            "mode": "NEW_DIRECTION",
            "product_thesis": "An incident response workspace organized by operational risk.",
            "user_job": "Find and stabilize the highest-risk incident.",
            "subject_anchors": ["incident timeline", "risk", "service health"],
            "identity_invariants": [],
            "frozen_axes": [],
            "flexible_axes": ["composition", "typography", "density", "material"],
            "novelty_budget": {"familiar": ["critical controls"], "expressive": ["composition"]},
            "signature_mechanism": "risk-weighted incident timeline",
            "quiet_system": ["secondary metadata"],
            "composition_principles": ["highest risk owns focal authority"],
            "typography_character": "precise operational",
            "palette_behavior": "semantic status color",
            "surface_material_logic": "explicit operational planes",
            "media_role": "none",
            "motion_posture": "functional",
            "anti_references": ["generic SaaS card wall"],
            "preserve": ["status truth", "focus visibility"],
            "rejection_conditions": ["primary incident loses focal authority"],
            "required_owner_outputs": ["visual-direction-set", "anti-slop-findings"],
            "source_evidence_refs": ["evidence://intent/phase4"],
        })
        candidates = [
            {"direction_id": "timeline", "composition": "timeline-workbench", "typography": "condensed-operational", "density": "dense-core-quiet-edges", "material": "flat", "media": "none", "motion": "functional", "signature": "risk-timeline"},
            {"direction_id": "service-map", "composition": "split-service-map", "typography": "humanist-operational", "density": "mixed", "material": "layered", "media": "diagrammatic", "motion": "functional", "signature": "service-risk-map"},
        ]
        governed = runtime.evaluate_direction_candidates(intent, candidates, {"render": True})
        self.assertEqual(governed["status"], "READY")
        committed = runtime.commit_direction(intent, candidates[0])
        self.assertEqual(committed["status"], "COMMITTED")
        self.assertEqual(committed["claim_boundary"], "committed-direction-only")

        trend_registry = json.loads((ROOT / "knowledge" / "aesthetic-trend-tells-v11.json").read_text(encoding="utf-8"))
        genericity = runtime.assess_genericity(
            structural_signals=[], trend_matches=[], trend_registry=trend_registry, as_of="2026-08-21"
        )
        self.assertEqual(genericity["verdict"], "SPECIFIC")

        blinded = runtime.prepare_blinded_candidates([
            {**candidates[0], "render_ref": "render://timeline", "generator_preference": True, "self_score": 100},
            {**candidates[1], "render_ref": "render://service-map", "generator_preference": False, "self_score": 10},
        ])
        self.assertNotIn("generator_preference", repr(blinded))
        court = runtime.aggregate_taste_court([
            {"dimension": "subject_specificity", "verdict": "LEFT", "evidence_refs": ["render://timeline"], "observable_cause": "risk-weighted timeline exposes domain causality"},
            {"dimension": "focal_authority", "verdict": "LEFT", "evidence_refs": ["render://timeline"], "observable_cause": "highest-risk incident owns primary saliency"},
        ])
        self.assertEqual(court["status"], "PREFERENCE")
        residue = runtime.assess_quality_residue_closure(resolved=3, persisted=0, unknown=0, regressions=0)
        self.assertEqual(residue["status"], "CLEAN")
        boundaries = {intent["claim_boundary"], committed["claim_boundary"], genericity["claim_boundary"], court["claim_boundary"], residue["claim_boundary"]}
        self.assertFalse({"VERIFIED", "RELEASED"} & boundaries)

    def test_phase4_does_not_create_canonical_skill_owners(self):
        graph = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))
        registry = json.loads((ROOT / "knowledge" / "runtime-detector-rules-v11.json").read_text(encoding="utf-8"))
        self.assertEqual(len(graph["skills"]), 874)
        rule_ids = {rule["rule_id"] for rule in registry["rules"]}
        self.assertEqual(rule_ids & set(graph["skills"]), set())
        for rule in registry["rules"]:
            for owner in rule.get("owner_hints", []):
                self.assertIn(owner, graph["skills"], f"unresolved owner hint {owner} in {rule['rule_id']}")


if __name__ == "__main__":
    unittest.main()
