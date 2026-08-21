import unittest

import nolane_ui.runtime_v11 as runtime


class Phase4AestheticGovernorContractTests(unittest.TestCase):
    def fn(self, name):
        value = getattr(runtime, name, None)
        self.assertTrue(callable(value), f"Phase 4 public API missing: {name}")
        return value

    def base_intent(self, **overrides):
        data = {
            "intent_id": "intent-1",
            "revision": "rev-a",
            "scope": ["app/page.tsx"],
            "ambition": "HIGH",
            "mode": "NEW_DIRECTION",
            "product_thesis": "A focused operational workspace for incident response.",
            "user_job": "Triage the highest-risk incident without losing state.",
            "subject_anchors": ["incident timeline", "service health", "operator handoff"],
            "identity_invariants": [],
            "frozen_axes": [],
            "flexible_axes": ["composition", "typography", "density", "material"],
            "novelty_budget": {"familiar": ["critical controls"], "expressive": ["information composition"]},
            "signature_mechanism": "risk-weighted incident timeline",
            "quiet_system": ["utility controls", "secondary metadata"],
            "composition_principles": ["incident owns focal authority"],
            "typography_character": "precise operational",
            "palette_behavior": "semantic status color with restrained neutrals",
            "surface_material_logic": "flat operational planes with explicit state boundaries",
            "media_role": "no decorative imagery",
            "motion_posture": "functional and interruptible",
            "anti_references": ["generic dashboard card wall"],
            "preserve": ["status truth", "keyboard reachability"],
            "rejection_conditions": ["primary incident loses focal authority"],
            "required_owner_outputs": ["visual-direction-set", "anti-slop-findings"],
            "source_evidence_refs": ["evidence://product-intent/1"],
        }
        data.update(overrides)
        return data

    def test_intent_compiler_sets_claim_boundary_and_rejects_axis_conflicts(self):
        compile_intent = self.fn("compile_aesthetic_intent")
        validate = self.fn("validate_aesthetic_intent")
        packet = compile_intent(self.base_intent())
        self.assertEqual(packet["claim_boundary"], "generation-intent-only")
        self.assertTrue(validate(packet)["valid"])

        conflict = self.base_intent(frozen_axes=["typography"], flexible_axes=["typography", "density"])
        with self.assertRaises(ValueError):
            compile_intent(conflict)

    def test_intent_compiler_does_not_infer_redesign_authority(self):
        compile_intent = self.fn("compile_aesthetic_intent")
        locked = self.base_intent(
            mode="NEW_DIRECTION",
            established_identity=True,
            departure_authorized=False,
            identity_invariants=["existing typography family", "existing palette family"],
        )
        with self.assertRaises(ValueError):
            compile_intent(locked)

    def test_generation_governor_requires_material_divergence(self):
        evaluate = self.fn("evaluate_direction_candidates")
        intent = self.fn("compile_aesthetic_intent")(self.base_intent(ambition="HIGH"))
        candidates = [
            {
                "direction_id": "a",
                "composition": "single-workbench",
                "typography": "neutral-grotesk",
                "density": "dense",
                "material": "flat",
                "media": "none",
                "motion": "functional",
                "signature": "timeline",
                "palette": "blue",
            },
            {
                "direction_id": "b",
                "composition": "single-workbench",
                "typography": "neutral-grotesk",
                "density": "dense",
                "material": "flat",
                "media": "none",
                "motion": "functional",
                "signature": "timeline",
                "palette": "orange",
            },
        ]
        result = evaluate(intent, candidates, {"render": True})
        self.assertEqual(result["status"], "RE_DIVERGE")
        self.assertFalse(result["materially_divergent"])

    def test_generation_governor_preserves_identity_lock_and_render_unknown(self):
        evaluate = self.fn("evaluate_direction_candidates")
        intent = self.fn("compile_aesthetic_intent")(
            self.base_intent(
                ambition="FLAGSHIP",
                mode="IDENTITY_LOCKED",
                established_identity=True,
                departure_authorized=False,
                identity_invariants=["type-family:Inter", "palette-family:graphite"],
                frozen_axes=["typography-family", "palette-family"],
                flexible_axes=["composition", "density", "material"],
            )
        )
        candidates = [
            {"direction_id": "a", "composition": "workbench", "typography": "Inter", "density": "dense", "material": "flat", "media": "none", "motion": "functional", "signature": "timeline", "identity_changes": []},
            {"direction_id": "b", "composition": "split-focus", "typography": "Inter", "density": "mixed", "material": "layered", "media": "none", "motion": "functional", "signature": "service-map", "identity_changes": []},
            {"direction_id": "c", "composition": "editorial", "typography": "Serif", "density": "sparse", "material": "paper", "media": "none", "motion": "ambient", "signature": "story", "identity_changes": ["typography-family"]},
        ]
        result = evaluate(intent, candidates, {"render": False})
        self.assertEqual(result["render_evidence"], "UNKNOWN")
        invalid = {item["direction_id"] for item in result["candidates"] if not item["valid"]}
        self.assertIn("c", invalid)

    def test_committed_direction_never_claims_verified(self):
        commit_direction = self.fn("commit_direction")
        intent = self.fn("compile_aesthetic_intent")(self.base_intent())
        candidate = {
            "direction_id": "a",
            "thesis": "incident-first operational composition",
            "subject_causality": ["risk level controls focal weight"],
            "signature": "risk-weighted timeline",
            "composition": "workbench",
            "typography": "precise",
            "density": "mixed",
            "material": "flat",
            "media": "none",
            "motion": "functional",
        }
        contract = commit_direction(intent, candidate)
        self.assertEqual(contract["claim_boundary"], "committed-direction-only")
        self.assertNotIn(contract.get("status"), {"VERIFIED", "RELEASED"})

    def test_trend_registry_expires_tells_and_one_tell_cannot_prove_genericity(self):
        validate = self.fn("validate_trend_registry")
        assess = self.fn("assess_genericity")
        registry = {
            "version": 11,
            "tells": [
                {
                    "tell_id": "trend.example",
                    "observed_pattern": "fashionable shell used without product causality",
                    "first_observed": "2026-01-01",
                    "last_reviewed": "2026-01-01",
                    "review_after": "2026-02-01",
                    "source_provenance": ["research:test"],
                    "applicable_contexts": ["marketing"],
                    "non_applicable_contexts": ["brand-authorized"],
                    "falsifier": "product evidence proves semantic necessity",
                    "status": "ACTIVE",
                    "implementation": "independently-authored",
                }
            ],
        }
        self.assertTrue(validate(registry)["valid"])
        result = assess(
            structural_signals=[],
            trend_matches=[{"tell_id": "trend.example", "semantic_necessity": 0.1}],
            trend_registry=registry,
            as_of="2026-08-21",
        )
        self.assertEqual(result["verdict"], "SPECIFIC")
        self.assertEqual(result["active_trend_matches"], [])

    def test_genericity_uses_accumulation_not_scalar_ai_score(self):
        assess = self.fn("assess_genericity")
        result = assess(
            structural_signals=[
                {"signal_id": "containment", "subject_specificity": 0.1, "semantic_necessity": 0.1, "frequency": 5, "hierarchy_cost": 0.8, "removal_cost": 0.1},
                {"signal_id": "repetition", "subject_specificity": 0.2, "semantic_necessity": 0.2, "frequency": 6, "hierarchy_cost": 0.7, "removal_cost": 0.1},
            ],
            trend_matches=[],
            trend_registry={"version": 11, "tells": []},
            as_of="2026-08-21",
        )
        self.assertEqual(result["verdict"], "GENERICITY_DEBT")
        self.assertIn("accumulation", result)
        self.assertNotIn("ai_score", result)
        self.assertNotIn("beauty_score", result)

    def test_product_substitution_reports_interchangeability_without_beauty_score(self):
        assess = self.fn("product_substitution_assessment")
        result = assess(
            original_product="incident response",
            substitute_products=["crypto analytics", "project management", "AI assistant"],
            mechanism_fit={"crypto analytics": 0.9, "project management": 0.9, "AI assistant": 0.8},
        )
        self.assertEqual(result["verdict"], "WEAK_SUBJECT_SPECIFICITY")
        self.assertNotIn("beauty_score", result)

    def test_design_memory_is_project_local_and_revision_aware(self):
        build = self.fn("build_design_memory")
        validate = self.fn("validate_design_memory")
        stale = self.fn("assess_design_memory_staleness")
        memory = build(
            project_identity="acme-ops",
            revision="rev-a",
            source_digests={"tokens.json": "aaa", "app.css": "bbb"},
            accepted_mechanisms=[{"id": "incident-timeline", "provenance": "accepted-direction"}],
            rejected_mechanisms=[{"id": "generic-card-wall", "provenance": "rendered-evidence"}],
            identity_invariants=[{"value": "graphite palette", "provenance": "design-system"}],
        )
        self.assertTrue(validate(memory)["valid"])
        self.assertNotIn("global_style", memory)
        self.assertEqual(stale(memory, {"tokens.json": "aaa", "app.css": "bbb", "unrelated.py": "ccc"})["status"], "CURRENT")
        self.assertEqual(stale(memory, {"tokens.json": "changed", "app.css": "bbb"})["status"], "STALE")
        self.assertEqual(stale(memory, {"tokens.json": "aaa"})["status"], "UNKNOWN")

    def test_taste_court_blinds_generator_preference_and_rejects_scalar_beauty(self):
        prepare = self.fn("prepare_blinded_candidates")
        validate = self.fn("validate_taste_judgment")
        packet = prepare([
            {"direction_id": "a", "render_ref": "render://a", "generator_preference": True, "self_score": 99, "reference_brand": "PrestigeCo", "composition": "workbench"},
            {"direction_id": "b", "render_ref": "render://b", "generator_preference": False, "self_score": 40, "reference_brand": "OtherCo", "composition": "split-focus"},
        ])
        serialized = repr(packet)
        self.assertNotIn("generator_preference", serialized)
        self.assertNotIn("self_score", serialized)
        self.assertNotIn("PrestigeCo", serialized)
        bad = {"dimension": "focal_authority", "verdict": "LEFT", "evidence_refs": ["render://a"], "observable_cause": "primary work owns saliency", "beauty_score": 9.7}
        self.assertFalse(validate(bad)["valid"])

    def test_taste_court_hard_blockers_are_non_compensatory(self):
        aggregate = self.fn("aggregate_taste_court")
        judgments = [
            {"dimension": "focal_authority", "verdict": "LEFT", "evidence_refs": ["render://a"], "observable_cause": "clearer primary work"},
            {"dimension": "typographic_character", "verdict": "LEFT", "evidence_refs": ["render://a"], "observable_cause": "stronger role separation"},
        ]
        result = aggregate(judgments, hard_blockers=[{"kind": "accessibility", "candidate": "LEFT", "reason": "focus state hidden"}])
        self.assertEqual(result["status"], "BLOCKED")
        self.assertNotEqual(result.get("winner"), "LEFT")

    def test_quality_residue_is_bounded_and_escalates_thesis_failure(self):
        plan = self.fn("plan_quality_residue_pass")
        result = plan(
            findings=[{"kind": "thesis", "region": "main", "dimension": "subject_specificity", "cause": "signature absent"}],
            pass_index=2,
            max_passes=2,
            preserve=["status truth"],
        )
        self.assertEqual(result["decision"], "RE_DIVERGE")
        self.assertEqual(result["claim_boundary"], "quality-residue-only")

    def test_quality_residue_closure_never_upgrades_to_release_authority(self):
        assess = self.fn("assess_quality_residue_closure")
        result = assess(resolved=4, persisted=0, unknown=0, regressions=0)
        self.assertEqual(result["status"], "CLEAN")
        self.assertEqual(result["claim_boundary"], "quality-residue-only")
        self.assertNotIn(result.get("status"), {"VERIFIED", "RELEASED"})


if __name__ == "__main__":
    unittest.main()
