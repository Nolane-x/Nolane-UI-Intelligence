# NUI V11 Runtime Design Intelligence Phase 2 Implementation Plan

> **For agentic workers:** Continue the approved V11 design. Use test-first development and keep the concurrent Batch 006 skill branch untouched.

**Goal:** Extend the green V11 source-runtime kernel with revision-bound evidence staleness, a runtime doctor, browser-observation findings, and a transactional/recoverable Live Lab protocol foundation.

**Architecture:** Reuse the existing V11 registry/finding vocabulary. Evidence bindings fingerprint only the source scope they actually certify; doctor reasons over those bindings and runtime capability declarations; browser observations become NUI findings through the same registry; Live Lab uses optimistic source digests and an append-only state machine so preview/accept/apply cannot overwrite concurrent source changes.

**Tech Stack:** Python 3.10+ standard library only, unittest, JSON schemas.

**Spec:** `docs/superpowers/specs/2026-08-21-runtime-design-intelligence-v11-design.md`

## Global Constraints

- Zero canonical skill additions and zero edits to `skills/skill-graph.json`.
- No edits to `design/ui-industry-1000-batch-006` work.
- No browser-vendor dependency in core.
- No evidence may remain current after an overlapping source digest changes.
- Unrelated source changes must not stale scoped evidence.
- Missing observation capability is UNKNOWN/BLOCKED, never fabricated PASS.
- Live apply must be optimistic-concurrency-safe and transactional.
- Full suite and exact-revision repository validation must pass before completion claim.

---

### Task 1: Revision-bound evidence bindings

**Files:**
- Create: `src/nolane_ui/runtime_v11/evidence.py`
- Create: `schemas/runtime-evidence-binding-v11.schema.json`
- Create: `tests/test_runtime_v11_evidence.py`

**Produces:** `sha256_text`, `sha256_file`, `build_evidence_binding`, `validate_evidence_binding`, `assess_evidence_staleness`.

- [ ] Write failing tests for overlapping change → STALE, unrelated change → CURRENT, missing current digest → UNKNOWN, invalid digests/scope rejected.
- [ ] Verify RED.
- [ ] Implement evidence binding and staleness without repository-global commit-count heuristics.
- [ ] Verify focused tests GREEN.

### Task 2: Runtime doctor

**Files:**
- Create: `src/nolane_ui/runtime_v11/doctor.py`
- Create: `src/nolane_ui/runtime_v11/doctor_cli.py`
- Create: `scripts/nui-runtime-doctor`
- Create: `tests/test_runtime_v11_doctor.py`

**Produces:** `diagnose_runtime_state(root, ...) -> dict`, JSON CLI report.

- [ ] Write failing tests for healthy installation, missing canonical detector artifact, stale evidence, capability gap, and the invariant that truth drift is not inferred from commit count.
- [ ] Verify RED.
- [ ] Implement maintenance findings grouped as schema/projection/evidence/capability; do not redesign or mutate as a side effect.
- [ ] Verify focused tests GREEN.

### Task 3: Browser observation court

**Files:**
- Modify: `knowledge/runtime-detector-rules-v11.json`
- Modify: `src/nolane_ui/runtime_v11/browser.py`
- Modify: `schemas/runtime-browser-observation-v11.schema.json`
- Create: `tests/test_runtime_v11_browser_findings.py`

**Produces:** `browser_observation_findings(record, registry) -> list[dict]`.

- [ ] Write failing tests for uncaught runtime error, document horizontal overflow, explicit text occlusion, clean counterexamples, complete NUI finding fields.
- [ ] Verify RED.
- [ ] Add independently-authored browser rules and typed observation fields; convert observations to existing finding semantics.
- [ ] Verify browser tests GREEN.

### Task 4: Transactional Live Lab protocol core

**Files:**
- Create: `src/nolane_ui/runtime_v11/live.py`
- Create: `schemas/runtime-live-session-v11.schema.json`
- Create: `tests/test_runtime_v11_live.py`

**Produces:** `create_live_session`, `append_live_event`, `validate_live_session`, `transactional_replace`.

- [ ] Write failing tests for legal state transitions, illegal skip/reorder, append-only sequencing, source-digest conflict, successful atomic replacement, and recovery after interrupted preview.
- [ ] Verify RED.
- [ ] Implement state machine and optimistic transactional source replacement with atomic filesystem replace.
- [ ] Verify focused tests GREEN.

### Task 5: Integration/export/docs

**Files:**
- Modify: `src/nolane_ui/runtime_v11/__init__.py`
- Modify: `src/nolane_ui/__init__.py`
- Create: `docs/RUNTIME-DESIGN-INTELLIGENCE.md`
- Modify: `tests/test_runtime_v11_integration.py`

- [ ] Extend integration tests for evidence/doctor/browser/live APIs and zero-skill invariant.
- [ ] Verify RED before exports.
- [ ] Export stable APIs and document execution tiers, doctor semantics, browser driver boundary, and Live Lab transaction contract.
- [ ] Run `PYTHONPATH=src python -m unittest discover -s tests -v` in CI.
- [ ] Run exact-revision release packet + `scripts/nui-validate` in CI.
