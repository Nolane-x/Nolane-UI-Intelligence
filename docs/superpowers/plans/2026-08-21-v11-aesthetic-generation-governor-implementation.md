# NUI V11 Phase 4 — Aesthetic Generation Governor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Operationalize NUI's existing anti-generic/taste cognition into a generation-time governor, dynamic genericity engine, project-local design memory, blinded taste court, and bounded quality-residue loop on top of the current 874-skill graph.

**Architecture:** Keep canonical skill ownership unchanged. Phase 4 adds machine-readable protocol modules under `src/nolane_ui/runtime_v11/` and versioned schemas/knowledge registries, then routes every generated observation back to existing owners and the established V11 evidence/re-observation gates. Integrate Batch 006/main first so all verification runs against 874 canonical skills.

**Tech Stack:** Python standard library, JSON schemas/contracts, existing NUI runtime_v11 modules, unittest-based repository suite, GitHub Actions `Verify NUI`.

**Spec:** `docs/superpowers/specs/2026-08-21-v11-aesthetic-generation-governor-design.md`

## Global Constraints

- No new canonical skill by default; `skills/skill-graph.json` must retain all 874 Batch 006 skills.
- No NUI house style and no static style blacklist as aesthetic authority.
- Generator cannot self-certify `VERIFIED` or `RELEASED`.
- Missing required render/judge capability yields `UNKNOWN`/`BLOCKED`, never PASS.
- No scalar beauty score; comparative verdicts must remain dimension-level and allow `TIE`/`RE_DIVERGE`.
- Runtime/generation routing may only resolve existing canonical owners.
- Trend tells are time-bounded and cannot block after review expiry.
- Exact-head completion must pass repository validation, completion packet generation, full test suite, and 874-skill count.

---

### Task 1: Integrate V11 with Batch 006 / 874-skill main

**Status:** in progress — merge commit `440fc4a1bf4079aa31a861537851d71e953096e3` created with parents V11 + Batch 006 main; CI checkpoint pending.

**Files:**
- Merge current `main` into `build/v11-runtime-design-intelligence`.
- Preserve all Phase 1–3 V11 files.
- Preserve all Batch 006 skill/graph/research/test files.

**Interfaces:**
- Consumes: current `main` at Batch 006 merge and V11 branch head.
- Produces: one conflict-resolved branch containing V11 + 874 canonical skills.

- [x] Verify pre-merge graph count is 874 on main and no Phase 4 implementation exists.
- [x] Merge main into the V11 branch without modifying canonical Batch 006 prose.
- [ ] Run the full existing suite. Expected: PASS with 874 declared/validated skills.
- [ ] Audit `owner_hints` against the merged graph and record unresolved hints rather than synthesizing owners.
- [x] Commit integration checkpoint.

### Task 2: Design Intent Compiler

**Files:**
- Create: `schemas/aesthetic-generation-intent-v11.schema.json`
- Create: `src/nolane_ui/runtime_v11/aesthetic_intent.py`
- Test: `tests/test_runtime_v11_aesthetic_intent.py`
- Modify: `src/nolane_ui/runtime_v11/__init__.py`
- Modify: `src/nolane_ui/__init__.py`

**Interfaces:**
- Produces: `compile_aesthetic_intent(inputs: dict) -> dict`, `validate_aesthetic_intent(packet: dict) -> dict`.

- [ ] Write failing tests for required fields, mode/ambition enums, `claim_boundary=generation-intent-only`, no implicit redesign, and frozen/flexible axis conflicts.
- [ ] Run focused tests; expected RED because module is absent.
- [ ] Implement validation/compiler with standard-library-only deterministic behavior.
- [ ] Run focused tests; expected GREEN.
- [ ] Export public API and commit.

### Task 3: Generation Governor and Material Divergence

**Files:**
- Create: `src/nolane_ui/runtime_v11/aesthetic_governor.py`
- Test: `tests/test_runtime_v11_aesthetic_governor.py`

**Interfaces:**
- Produces: `evaluate_direction_candidates(intent, candidates, capabilities) -> dict`, `commit_direction(intent, candidate) -> dict`.

- [ ] Write failing tests for UTILITY/STANDARD/HIGH/FLAGSHIP candidate requirements.
- [ ] Add RED tests proving palette-only/radius-only variants are not materially divergent.
- [ ] Add RED tests proving identity invariant violation invalidates a candidate in `IDENTITY_LOCKED` mode.
- [ ] Implement causal-axis divergence ledger and capability-aware `UNKNOWN` for missing render evidence.
- [ ] Implement committed-direction contract with no verification/release authority.
- [ ] Run focused tests and commit GREEN implementation.

### Task 4: Dynamic Genericity Engine + Expiring Trend Tells

**Files:**
- Create: `knowledge/aesthetic-trend-tells-v11.json`
- Create: `schemas/aesthetic-trend-tells-v11.schema.json`
- Create: `src/nolane_ui/runtime_v11/genericity.py`
- Test: `tests/test_runtime_v11_genericity.py`

**Interfaces:**
- Produces: `validate_trend_registry`, `assess_genericity`, `product_substitution_assessment`.

- [ ] Write failing tests for `ACTIVE|WATCH|RETIRED`, ISO dates, `review_after`, falsifiers, research provenance, and independent implementation provenance.
- [ ] Write RED tests proving an expired tell cannot block and one tell alone cannot prove genericity.
- [ ] Write RED tests for accumulation-ledger output and `SPECIFIC|WATCH|GENERICITY_DEBT|UNJUDGABLE` verdicts.
- [ ] Implement a minimal independently authored seed registry with no universal style bans.
- [ ] Implement deterministic accumulation/provenance handling and commit after GREEN.

### Task 5: Project-local Design Memory

**Files:**
- Create: `schemas/aesthetic-design-memory-v11.schema.json`
- Create: `src/nolane_ui/runtime_v11/design_memory.py`
- Test: `tests/test_runtime_v11_design_memory.py`

**Interfaces:**
- Produces: `validate_design_memory`, `build_design_memory`, `assess_design_memory_staleness`.

- [ ] Write failing tests for project-local identity, provenance, accepted/rejected mechanisms, revision binding, and no global-style field.
- [ ] Write RED staleness tests: overlapping identity/design-system changes => `STALE`, unrelated source changes => `CURRENT`, missing required source => `UNKNOWN`.
- [ ] Implement deterministic memory contract using existing V11 digest semantics where applicable.
- [ ] Run focused tests and commit.

### Task 6: Blinded Taste Court

**Files:**
- Create: `schemas/aesthetic-taste-court-v11.schema.json`
- Create: `src/nolane_ui/runtime_v11/taste_court.py`
- Test: `tests/test_runtime_v11_taste_court.py`

**Interfaces:**
- Produces: `prepare_blinded_candidates`, `validate_taste_judgment`, `aggregate_taste_court`.

- [ ] Write RED tests proving generator preference/self-score/reference prestige are stripped from judge input.
- [ ] Write RED tests for per-dimension `LEFT|RIGHT|TIE|UNJUDGABLE`, evidence refs, observable causes, and preserve constraints.
- [ ] Write RED tests proving no scalar beauty score and no aesthetic win may compensate a hard accessibility/product-truth regression.
- [ ] Implement blinded packet/judgment aggregation with `TIE` and `RE_DIVERGE` support.
- [ ] Run focused tests and commit.

### Task 7: Craft-floor Runtime Rules

**Files:**
- Modify: `knowledge/runtime-detector-rules-v11.json`
- Modify: `src/nolane_ui/runtime_v11/detector.py`
- Test: `tests/test_runtime_v11_craft_floor.py`

**Interfaces:**
- Extends existing V11 rule registry/detector; no new skill owners.

- [ ] Add failure-first tests for a small evidence-strong set only: repeated decorative pills/badges, repeated all-caps micro-label accumulation, and uncontrolled repeated nested shell/border containment accumulation.
- [ ] Add negative tests proving semantic status pills, authorized metadata labels, and justified independent object boundaries do not hard-fail.
- [ ] Admit only contextual/genericness/advisory rules whose falsifiers and owner hints are valid on the 874 graph.
- [ ] Keep all genericness/advisory rules outside edit-tier blocking.
- [ ] Run registry/detector/adjudication tests and commit.

### Task 8: Quality Residue Loop and Closure Integration

**Files:**
- Create: `src/nolane_ui/runtime_v11/quality_residue.py`
- Test: `tests/test_runtime_v11_quality_residue.py`
- Modify: `src/nolane_ui/runtime_v11/reobserve.py`
- Modify: `src/nolane_ui/runtime_v11/live.py`

**Interfaces:**
- Produces: `plan_quality_residue_pass`, `assess_quality_residue_closure`.

- [ ] Write RED tests for bounded pass count, causal region/dimension ownership, preserve set, and no macro redesign inside residue mode.
- [ ] Write RED tests proving persistent thesis failure returns `RE_DIVERGE` instead of endless polish.
- [ ] Integrate with existing re-observation so `CLEAN` remains runtime-scope only, never release authority.
- [ ] Run focused tests and commit.

### Task 9: End-to-end Phase 4 Protocol + Exact-head Verification

**Files:**
- Create/modify: `tests/test_runtime_v11_aesthetic_integration.py`
- Modify: `docs/RUNTIME-DESIGN-INTELLIGENCE.md`
- Modify: PR #22 body after verification only.

**Interfaces:**
- End-to-end path: intent -> candidates -> commitment -> genericity/memory -> render judgment input -> taste court -> residue -> re-observation -> existing evidence gate boundary.

- [ ] Write integration tests proving no canonical skill synthesis, no house-style field, no stale trend blocking, and no self-VERIFIED claim.
- [ ] Run all Phase 4 tests.
- [ ] Run full repository suite.
- [ ] Generate fresh bounded completion packet for exact head.
- [ ] Run `scripts/nui-validate` against exact revision.
- [ ] Confirm skill count remains 874 declared/validated and changed-path audit contains no canonical skill prose edits.
- [ ] Update PR #22 body with Phase 4 architecture and exact-head CI evidence; do not merge without explicit user instruction.
