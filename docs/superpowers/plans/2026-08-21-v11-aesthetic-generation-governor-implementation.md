# NUI V11 Phase 4 — Aesthetic Generation Governor Implementation Plan

**Status:** implementation complete; final exact-head verification is intentionally recorded in PR #22 after this committed completion record so the verification SHA is not invalidated by documenting it.

**Goal:** Operationalize NUI's existing anti-generic/taste cognition into a generation-time governor, dynamic genericity engine, project-local design memory, blinded taste court, craft-floor runtime perception, and bounded quality-residue loop on top of the 874-skill canonical graph.

**Architecture:** Canonical skill ownership remains unchanged. Phase 4 adds machine-readable protocol modules under `src/nolane_ui/runtime_v11/`, versioned schemas/knowledge registries, deterministic runtime observations, and explicit public APIs. All observations route only to already-existing canonical owners and remain below NUI's evidence/completion authority.

**Spec:** `docs/superpowers/specs/2026-08-21-v11-aesthetic-generation-governor-design.md`

## Completion invariants

- [x] No canonical skills were added by V11 Phase 4.
- [x] `skills/skill-graph.json` remains the Batch 006 874-skill graph.
- [x] PR changed-path audit contains zero paths under `skills/`.
- [x] No NUI house style or universal style blacklist was introduced.
- [x] Generator outputs cannot self-certify `VERIFIED` or `RELEASED`.
- [x] Missing render/judge capability remains `UNKNOWN`/`BLOCKED`, never PASS.
- [x] Taste comparison is vector/dimension based; no scalar beauty score is authoritative.
- [x] Runtime/generation routing resolves only existing canonical owners.
- [x] Trend tells are time-bounded and lose effect after review expiry.
- [x] Genericness/craft-floor rules remain non-edit-blocking observations.

## Task 1 — Integrate V11 with Batch 006 / 874-skill main

**Outcome:** complete. V11 was integrated with the Batch 006 mainline using a real two-parent merge while preserving the full 874-skill graph and all V11 runtime work.

- [x] Verify main contains exactly 874 declared/validated canonical skills.
- [x] Integrate Batch 006 without rewriting its canonical skill prose.
- [x] Run the full baseline suite on the integrated graph.
- [x] Audit runtime `owner_hints` against the merged graph.
- [x] Preserve unresolved hints as explicit debt during RED stages rather than synthesizing aliases/owners.

Baseline integration checkpoint: merge commit `816d31c6e3cd0d169beaa57935f0c53e58537cad`; GitHub Actions run `32470804410` passed unit/contract tests, completion packet generation, exact-revision validation, and packaging.

## Task 2 — Design Intent Compiler

**Implemented:**
- `schemas/aesthetic-generation-intent-v11.schema.json`
- `src/nolane_ui/runtime_v11/aesthetic_intent.py`

- [x] Compile explicit protectors, forbidden moves, aspirations, and mutable axes.
- [x] Reject conflicting protected/flexible axis declarations.
- [x] Refuse implicit redesign authority; only explicit authority may enable redesign.
- [x] Emit `claim_boundary: generation-intent-only`.
- [x] Export through `runtime_v11` and the top-level `nolane_ui` runtime API.

## Task 3 — Generation Governor and Material Divergence

**Implemented:** `src/nolane_ui/runtime_v11/aesthetic_governor.py`

- [x] Evaluate multiple direction candidates against the compiled intent.
- [x] Measure material divergence on causal axes such as hierarchy, interaction model, signature mechanism, spatial composition, product metaphor, and motion logic.
- [x] Refuse palette/radius-only variation as evidence of a distinct direction.
- [x] Invalidate frozen/identity-locked axis violations rather than compensating them with aesthetic scores.
- [x] Preserve missing render/interaction evidence as `UNKNOWN`.
- [x] Commit a direction with `generation-direction-commit-only` authority, never release authority.

## Task 4 — Dynamic Genericity Engine + Expiring Trend Tells

**Implemented:**
- `knowledge/aesthetic-trend-tells-v11.json`
- `schemas/aesthetic-trend-tells-v11.schema.json`
- `src/nolane_ui/runtime_v11/genericity.py`

- [x] Validate dated tells with falsifiers and independently-authored provenance.
- [x] Expire tell influence after `review_after`.
- [x] Require accumulation; one tell alone cannot prove genericity.
- [x] Return bounded `SPECIFIC | WATCH | GENERICITY_DEBT | UNJUDGABLE` outcomes instead of an opaque AI/genericity score.
- [x] Add product-substitution/interchangeability assessment without converting it into a beauty score.

## Task 5 — Project-local Design Memory

**Implemented:**
- `schemas/aesthetic-design-memory-v11.schema.json`
- `src/nolane_ui/runtime_v11/design_memory.py`

- [x] Bind memory to project identity, revision, provenance, and source digests.
- [x] Keep accepted/rejected mechanisms local to the project rather than turning them into global NUI style rules.
- [x] Mark overlapping source changes `STALE`, missing required state `UNKNOWN`, and unrelated changes `CURRENT`.

## Task 6 — Blinded Taste Court

**Implemented:**
- `schemas/aesthetic-taste-court-v11.schema.json`
- `src/nolane_ui/runtime_v11/taste_court.py`

- [x] Strip generator preference, self-score, reference prestige, and scalar beauty fields from judge input.
- [x] Prevent redaction metadata itself from leaking forbidden judge information.
- [x] Judge per dimension with `LEFT | RIGHT | TIE | UNJUDGABLE` and evidence/observable causes.
- [x] Keep accessibility/product-truth hard blockers non-compensatory.
- [x] Preserve `TIE` and `RE_DIVERGE` as first-class outcomes.

## Task 7 — Craft-floor Runtime Rules

**Implemented:**
- `knowledge/runtime-detector-rules-v11.json`
- `src/nolane_ui/runtime_v11/detector.py`
- `tests/test_runtime_v11_craft_floor.py`

Three evidence-bounded accumulation observations were admitted:

1. `runtime.genericness.decorative-pill-saturation`
2. `runtime.genericness.all-caps-micro-label-accumulation`
3. `runtime.genericness.uniform-boundary-accumulation`

- [x] Use accumulation thresholds rather than singleton bans.
- [x] Exempt semantic state/category/filter/metadata pill usage.
- [x] Exempt legitimate identifiers/metadata/table/axis roles from all-caps accumulation.
- [x] Exempt declared independent object/state/interaction boundaries from uniform-shell accumulation.
- [x] Keep all new rules at session tier with `observation` severity.
- [x] Route only to canonical 874-graph owners.
- [x] Repair historical owner-hint drift instead of creating aliases.

## Task 8 — Quality Residue Loop

**Implemented:** `src/nolane_ui/runtime_v11/quality_residue.py`

- [x] Bound micro-craft passes by explicit budget and causal region/dimension ownership.
- [x] Preserve a committed thesis/preserve set during residue work.
- [x] Return `RE_DIVERGE` when the thesis is false or the bounded budget is exhausted instead of endlessly polishing the wrong direction.
- [x] Keep residue closure at `quality-residue-only`; it never upgrades runtime closure into product verification/release authority.
- [x] Reuse existing V11 re-observation/Live claim boundaries rather than duplicating a second closure engine.

## Task 9 — End-to-end Phase 4 integration

**Actual test surfaces:**
- `tests/test_runtime_v11_aesthetic_phase4.py`
- `tests/test_runtime_v11_craft_floor.py`
- `tests/test_runtime_v11_phase4_integration.py`

- [x] Run explicit RED → GREEN cycles for Phase 4 behavior.
- [x] Prove generation and release authority remain separate end-to-end.
- [x] Expose all 15 Phase 4 public runtime callables at top-level `nolane_ui`.
- [x] Include Phase 4 modules/schemas/knowledge in Runtime Doctor installation inventory.
- [x] Ensure every runtime rule owner hint resolves to an existing canonical skill.
- [x] Confirm changed-path audit contains no canonical skill prose edits.
- [x] Pass the full 538-test implementation gate before documentation closure.

Implementation GREEN checkpoint before this documentation commit: head `f41195f04e7fb1845e890c36bbdaed042d735943`, GitHub Actions run `32472749380`. All unit/contract tests, fresh completion packet generation, exact-revision validation, artifact upload, project packaging, and archive upload passed.

## Final verification policy

The authoritative exact-head SHA/run is written into PR #22 **after** this committed plan/runtime documentation is complete. This avoids a recursive failure mode where writing a verified SHA into the repository creates a newer unverified SHA. PR metadata does not alter the branch tree, so it is the correct location for the final exact-head evidence.
