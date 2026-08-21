# NUI V11 Runtime Intelligence Phase 3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn V11 findings into evidence-bound repair routes and prove repair closure through deterministic re-observation, while clarifying that Impeccable was research inspiration only and no implementation was transferred.

**Architecture:** Keep runtime observation subordinate to the existing NUI cognition graph. A new `runtime_v11/routing.py` resolves a finding's `owner_hints` against the canonical skill graph without changing ownership; a new `runtime_v11/reobserve.py` compares before/after observation batches and classifies each prior finding as `RESOLVED`, `PERSISTED`, or `UNKNOWN`, while identifying new regressions. Live sessions may record a re-observation summary but cannot self-certify release readiness.

**Tech Stack:** Python 3.12 standard library only, JSON contracts, existing NUI skill graph and finding vocabulary, unittest, GitHub Actions `Verify NUI`.

**Spec:** `docs/superpowers/specs/2026-08-21-runtime-design-intelligence-v11-design.md`

## Global Constraints

- Add no canonical skills and do not modify `skills/skill-graph.json`.
- Do not touch `design/ui-industry-1000-batch-006` or any Batch 006 skill file.
- Runtime rules remain evidence contracts, not design authority.
- Missing routing/evidence context must remain explicit `UNKNOWN`; never infer PASS.
- A clean re-observation closes only the matching runtime finding scope; it does not certify overall UI quality or release readiness.
- Use only Python standard library in the runtime core.
- Impeccable is research inspiration only; no Impeccable source code, detector rules, schemas, skill bodies, thresholds, or implementation artifacts are incorporated.

---

### Task 1: Clarify research-inspiration provenance semantics

**Files:**
- Modify: `knowledge/runtime-detector-rules-v11.json`
- Modify: `src/nolane_ui/runtime_v11/registry.py`
- Modify: `tests/test_runtime_v11_registry.py`
- Modify: `docs/research/impeccable-runtime-mechanism-transfer-v11.md`
- Modify: `docs/RUNTIME-DESIGN-INTELLIGENCE.md`

**Interfaces:**
- Consumes: existing `source_provenance` objects on runtime rules.
- Produces: provenance objects with `kind="independent-nui-rule"`, `implementation="independently-authored"`, and optional `research_inspiration` string list. `mechanism_sources` becomes invalid so wording cannot imply source transfer.

- [ ] **Step 1: Write failing registry tests**

Add tests that reject a provenance object containing `mechanism_sources`, require `research_inspiration` to be a list of non-empty strings when present, and accept independently authored rules with no external inspiration.

- [ ] **Step 2: Run the focused registry tests and verify RED**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_registry -v`

Expected: FAIL because the current validator still accepts `mechanism_sources` and does not validate `research_inspiration`.

- [ ] **Step 3: Implement the provenance contract and migrate the registry**

In `registry.py`, reject `mechanism_sources`; validate optional `research_inspiration`. In the rule JSON, convert entries such as `pbakaus/impeccable:...` into plain research labels under `research_inspiration`, while preserving `implementation="independently-authored"`. General NUI/WCAG/browser knowledge may also appear as research inspiration, not transferred source.

- [ ] **Step 4: Rewrite research/docs wording**

Rename the conceptual framing inside the research document from mechanism transfer to architectural research/inspiration. State explicitly that no code, rule text, schema, thresholds, skill body, or implementation artifact is imported. Keep the historical filename for link stability in this PR, but make its document title and body unambiguous.

- [ ] **Step 5: Run focused tests and commit**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_registry tests.test_runtime_v11_integration -v`

Expected: PASS.

Commit message: `refactor: clarify runtime research provenance`

---

### Task 2: Resolve runtime findings to existing NUI owners without changing ownership

**Files:**
- Create: `src/nolane_ui/runtime_v11/routing.py`
- Create: `tests/test_runtime_v11_routing.py`
- Modify: `src/nolane_ui/runtime_v11/__init__.py`
- Modify: `src/nolane_ui/__init__.py`

**Interfaces:**
- Consumes: `finding: dict`, validated runtime registry, canonical `skills/skill-graph.json` record.
- Produces: `route_runtime_finding(finding, registry, skill_graph) -> dict` with keys `finding_id`, `rule_id`, `status`, `owners`, `unresolved_owner_hints`, `evidence_only`, and `reason`.
- Produces: `route_runtime_findings(findings, registry, skill_graph) -> dict` with stable routes and aggregate unresolved count.

- [ ] **Step 1: Write failing routing tests**

Test that a finding for `runtime.browser.document-horizontal-overflow` resolves only to owner hints that exist in the graph; unknown hints are reported rather than invented; a missing runtime rule returns `UNKNOWN_RULE`; stable input produces stable owner ordering; and every route declares `evidence_only=True`.

- [ ] **Step 2: Run focused routing tests and verify RED**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_routing -v`

Expected: FAIL because `nolane_ui.runtime_v11.routing` does not exist.

- [ ] **Step 3: Implement routing**

Load owner hints from the matching registry rule, intersect them with `skill_graph["skills"]`, preserve registry order while deduplicating, return unresolved hints explicitly, and never synthesize a new owner or edit the graph. `status` is `ROUTED` when at least one owner resolves, `UNRESOLVED` when the rule exists but no hint resolves, and `UNKNOWN_RULE` when the finding references no registry rule.

- [ ] **Step 4: Export the public API and run focused tests**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_routing tests.test_runtime_v11_integration -v`

Expected: PASS.

- [ ] **Step 5: Commit**

Commit message: `feat: route runtime findings to existing owners`

---

### Task 3: Add deterministic re-observation closure

**Files:**
- Create: `src/nolane_ui/runtime_v11/reobserve.py`
- Create: `tests/test_runtime_v11_reobserve.py`
- Modify: `src/nolane_ui/runtime_v11/__init__.py`
- Modify: `src/nolane_ui/__init__.py`

**Interfaces:**
- Consumes: `before_findings: list[dict]`, `after_findings: list[dict]`, optional `capabilities_complete: bool`.
- Produces: `compare_runtime_observations(before_findings, after_findings, *, capabilities_complete=True) -> dict` containing `closures`, `regressions`, `counts`, and `decision`.
- Matching key: `(runtime.rule_id, runtime.path/url, runtime.line/locator)` using only fields present in the finding.

- [ ] **Step 1: Write failing closure tests**

Cover: prior finding absent after a complete re-observation => `RESOLVED`; same scoped finding remains => `PERSISTED`; missing capability => prior absence is `UNKNOWN`, never resolved; a new after-only finding appears in `regressions`; different locator/line does not falsely close another finding; stable ordering is deterministic.

- [ ] **Step 2: Run focused re-observation tests and verify RED**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_reobserve -v`

Expected: FAIL because the module/function does not exist.

- [ ] **Step 3: Implement closure comparison**

Normalize scope keys conservatively. Re-observation may resolve only an identical rule/scope when observation capability is complete. The aggregate decision is `CLEAN` only when every prior finding is resolved and no regression exists; `UNKNOWN` when any prior finding cannot be judged; otherwise `OPEN`. This decision is runtime-closure status only, not NUI release status.

- [ ] **Step 4: Export API and run focused tests**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_reobserve tests.test_runtime_v11_integration -v`

Expected: PASS.

- [ ] **Step 5: Commit**

Commit message: `feat: add runtime re-observation closure`

---

### Task 4: Bind re-observation summaries into Live Lab without self-certification

**Files:**
- Modify: `src/nolane_ui/runtime_v11/live.py`
- Modify: `tests/test_runtime_v11_live.py`
- Modify: `schemas/runtime-live-session-v11.schema.json`
- Modify: `docs/RUNTIME-DESIGN-INTELLIGENCE.md`

**Interfaces:**
- Consumes: the summary returned by `compare_runtime_observations`.
- Produces: an `APPLIED -> REOBSERVED` event payload containing `runtime_closure_decision`, `resolved_count`, `persisted_count`, `unknown_count`, and `regression_count`.

- [ ] **Step 1: Write failing Live Lab tests**

Require `reobserve` event payload to include all closure counters and a runtime closure decision in `CLEAN | OPEN | UNKNOWN`. Reject `CLEAN` when persisted/unknown/regression counts are non-zero. Reject negative counters. Confirm the session may still transition to `CLOSED` after an `OPEN` re-observation because closing a live session is not a release claim.

- [ ] **Step 2: Run focused Live tests and verify RED**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_live -v`

Expected: FAIL because `append_live_event` currently accepts arbitrary re-observation payloads.

- [ ] **Step 3: Implement payload validation and schema alignment**

Validate only the `reobserve` event payload at the transition boundary. Keep append-only replay behavior unchanged. Update the JSON schema so stored live sessions carry the same bounded closure summary.

- [ ] **Step 4: Document the closure boundary and run focused tests**

Document: `REOBSERVED/CLEAN` means the scoped runtime findings observed before repair are closed under the supplied capabilities; it does not mean the surface is `VERIFIED` or `RELEASED`.

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_live tests.test_runtime_v11_reobserve tests.test_runtime_v11_integration -v`

Expected: PASS.

- [ ] **Step 5: Commit**

Commit message: `feat: bind runtime closure into live sessions`

---

### Task 5: Exact-head verification and PR evidence update

**Files:**
- Modify: PR #22 body only after verification succeeds.

**Interfaces:**
- Consumes: exact branch head after Tasks 1–4.
- Produces: review-ready PR evidence with exact SHA and GitHub Actions run ID.

- [ ] **Step 1: Run the full repository suite through `Verify NUI`**

Expected gates: all unit/contract tests PASS; fresh bounded completion packet PASS; exact-revision `nui-validate` PASS; packaging/upload PASS.

- [ ] **Step 2: Confirm non-competition invariants**

Inspect PR changed paths and assert zero changes under `skills/` and no modification of `skills/skill-graph.json`. Confirm the canonical count remains whatever the branch base declares (currently 774) and do not absorb Batch 006 changes.

- [ ] **Step 3: Update PR #22 evidence**

Replace stale verification SHA/run/count in the PR body with the exact final head and final test count. Rename the section `Impeccable mechanism transfer` to `External architectural research` and state that Impeccable was research inspiration only.

- [ ] **Step 4: Keep PR unmerged**

Leave PR #22 open and review-ready. Do not merge until the concurrent Batch 006 integration point is coordinated.
