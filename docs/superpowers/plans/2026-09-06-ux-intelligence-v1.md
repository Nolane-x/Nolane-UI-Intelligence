# UX Intelligence v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a first-class UX Intelligence subsystem with canonical UX mechanisms, 32 cognitive registry entries, 16 falsifiable operational rules, deterministic query/status APIs, public Python/MCP integration, and semantic quality gates that preserve NUI's no-quota and evidence-honesty principles.

**Architecture:** Add an isolated `src/nolane_ui/ux_intelligence/` package rather than modifying the mature V13 contract in the first iteration. The package separates semantic mechanisms, cognitive skills, operational rules and catalog/query validation. Public API and MCP expose this subsystem through an explicitly distinct UX namespace so V13 rule authority is not blurred.

**Tech Stack:** Python 3.10+, standard-library `unittest`, dependency-free data/validation modules, GitHub Actions matrix on Python 3.10/3.11/3.12 plus the real Chromium smoke gate.

**Spec:** `docs/superpowers/specs/2026-09-06-ux-intelligence-v1-design.md`

## Global Constraints

- Do not modify existing V13 rule semantics or force migration in v1.
- Rule/skill counts are descriptive, never quality quotas.
- Contextual and convergence rules must never block.
- All UX rules must bind to a known mechanism and known owner skill.
- At least one owner skill for every UX rule must explicitly cover that rule's mechanism.
- Exact normalized `(failure_modes, repairs, verification)` signature clones are rejected even under a new rule ID.
- Query limits are strict integers in the range 1..100.
- Canonical outputs are sorted deterministically by stable ID.
- No generated rule loops or template-generated prose.
- Public UX tools remain read-only and use a distinct namespace from V13 rule tools.

---

### Task 1: Lock the UX ontology with failing tests

**Files:**
- Create: `tests/test_ux_intelligence_v1.py`

**Interfaces:**
- Consumes: none.
- Produces: expected imports and invariants for `nolane_ui.ux_intelligence`.

- [x] **Step 1: Write the failing test**

The contract imports `UX_MECHANISMS`, `UX_SKILLS`, `UX_RULES`, `get_ux_mechanism`, `query_ux_mechanisms`, `get_ux_skill`, `query_ux_skills`, `get_ux_rule`, `query_ux_rules`, and `ux_intelligence_status`. It locks 14 mechanism IDs, 32 skill IDs, 16 rule IDs, unique IDs, exact ontology references, owner resolution, no quota fields, non-blocking contextual/convergence rules, deterministic sorting and bounded query behavior.

- [x] **Step 2: Run the repository's real test runner and verify RED**

Actual CI command: `PYTHONPATH=src python -m unittest discover -s tests -v`

Observed RED baseline: import failed because `nolane_ui.ux_intelligence` did not yet exist, while prior repository behavior remained independently testable.

- [x] **Step 3: Commit RED state**

Committed the contract before production implementation.

---

### Task 2: Implement canonical UX mechanisms

**Files:**
- Create: `src/nolane_ui/ux_intelligence/mechanisms.py`

**Interfaces:**
- Produces: `UX_MECHANISMS: tuple[dict[str, object], ...]` containing 14 semantic primitives.

- [x] **Step 1: Add the minimal mechanism registry**

The 14 canonical mechanisms use non-empty `mechanism_id`, `title`, `definition`, `diagnostic_question`, `signals`, and `non_examples` fields.

- [x] **Step 2: Keep data explicitly authored**

Mechanism prose is literal and authored rather than loop-generated.

---

### Task 3: Implement 32 canonical UX cognitive registry entries

**Files:**
- Create: `src/nolane_ui/ux_intelligence/skills.py`

**Interfaces:**
- Consumes: known mechanism IDs from `mechanisms.py`.
- Produces: `UX_SKILLS: tuple[dict[str, object], ...]`.

- [x] **Step 1: Add four entries per UX domain**

Covers `goal-task`, `mental-model`, `information-architecture`, `journey-flow`, `cognitive-friction`, `comprehension`, `recovery`, and `evaluation` with four distinct cognitive operations each.

- [x] **Step 2: Bind each entry to relevant mechanisms**

Every `related_mechanisms` entry resolves to an existing mechanism ID. These entries remain a UX cognition registry in v1 and are not silently promoted into canonical `skills/<slug>/SKILL.md` graph nodes.

---

### Task 4: Implement 16 high-confidence operational UX rules

**Files:**
- Create: `src/nolane_ui/ux_intelligence/rules.py`

**Interfaces:**
- Consumes: mechanism IDs and cognitive registry IDs.
- Produces: `UX_RULES: tuple[dict[str, object], ...]`.

- [x] **Step 1: Author rules explicitly**

Rules cover progress preservation, task-context preservation, destructive-consequence disclosure, false completion, dead-end recovery, cross-step consistency, navigation identity, stale task context, semantically redundant re-entry, recovery reachability, scope disclosure, interruption recovery, mental-model mismatch, hidden dependencies, premature commitment and product-template convergence.

- [x] **Step 2: Preserve enforcement boundaries**

Mechanical/behavioral directly reproducible failures may block at major/critical severity. Contextual/convergence rules use `warn` or `review` only.

---

### Task 5: Add validation, semantic court and deterministic query APIs

**Files:**
- Create: `src/nolane_ui/ux_intelligence/catalog.py`
- Create: `src/nolane_ui/ux_intelligence/__init__.py`
- Test: `tests/test_ux_intelligence_v1.py`

**Interfaces:**
- Produces: `get_ux_mechanism`, `query_ux_mechanisms`, `get_ux_skill`, `query_ux_skills`, `get_ux_rule`, `query_ux_rules`, `ux_intelligence_status`.

- [x] **Step 1: Validate registries on import**

Reject duplicate IDs, unknown references, missing required fields, forbidden quota fields, blocking contextual/convergence rules, invalid enforcement/class/status values, empty operational planes, and rules whose declared owner IDs exist but none semantically covers the rule mechanism.

- [x] **Step 2: Implement deterministic exact lookup**

Missing IDs return `None`; hits return independent canonical record copies.

- [x] **Step 3: Implement bounded queries**

Optional domain/mechanism/class/status/text filters are supported where relevant. `1 <= limit <= 100`; booleans and non-integers are rejected.

- [x] **Step 4: Implement status**

Status reports validity, version, counts by UX domain, mechanism coverage, orphan mechanisms, rule class counts, and explicitly reports `rule_count_is_quality_target: False` and `skill_count_is_quality_target: False`.

- [x] **Step 5: Add semantic-owner and operational-signature mutation tests before production enforcement**

Observed local RED on the reconstructed CI-green project artifact: 9 focused UX tests ran, exactly 2 failed because the validator did not yet reject an existing-but-mechanism-unrelated owner or an ID-renamed rule clone with the same operational signature. After implementing the two courts, the same 9 focused tests passed.

- [x] **Step 6: Keep near-neighbor semantics distinct**

Signature comparison is exact after case/whitespace normalization of `(failure_modes, repairs, verification)`. v1 does not use fuzzy similarity as automatic blocking authority, so semantically distinct recovery rules are not collapsed merely because they share a domain/mechanism family.

---

### Task 6: Verify core GREEN and regression safety

**Files:**
- Test: `tests/test_ux_intelligence_v1.py`
- Existing suite: unchanged.

- [x] **Step 1: Verify focused UX contracts locally**

The final focused UX core suite is 9/9 GREEN after the semantic court implementation. The public/MCP integration suite is 6/6 GREEN on a reconstructed project artifact produced by an earlier successful repository CI run.

- [x] **Step 2: Investigate full local suite environmental failure without hiding it**

A 719-test local discovery run produced exactly one error: the real Playwright smoke attempted to launch Chromium because the local Python environment contains Playwright, but the browser binary is not installed. The traceback is outside UX code. The official workflow handles this intentionally: core CI installs no Playwright extra, while the independent browser job installs Playwright plus Chromium before requiring the smoke test.

- [ ] **Step 3: Verify latest-head project CI / workflow gates**

Required evidence before completion: Python 3.10, 3.11 and 3.12 core jobs pass, real Chromium passes, and the downstream current-head release gate succeeds on the final frozen feature head.

- [x] **Step 4: Review for generated-prose/quota regressions**

UX v1 retains explicitly authored records and no count target field is admitted as quality authority.

---

### Task 7: Expose UX Intelligence through public Python API and MCP

**Files:**
- Create: `tests/test_ux_intelligence_v1_api_mcp.py`
- Modify: `src/nolane_ui/__init__.py`
- Modify: `src/nolane_ui/mcp_server.py`

**Interfaces:**
- Public Python: three registries plus exact lookup, bounded query and status functions.
- MCP: `nui_ux_status`, exact mechanism/skill/rule lookups, and bounded mechanism/skill/rule queries.

- [x] **Step 1: Write public/MCP integration tests first**

The test requires the exact public exports, distinct `nui_ux_*`/`nui_get_ux_*` namespace, exact missing-ID failure behavior in MCP wrappers, bounded filters and preserved no-quota status.

- [x] **Step 2: Verify integration RED in real GitHub Actions**

Run `34017813154`, Python 3.12, executed 717 tests and failed only in the six new integration assertions/errors: missing top-level UX exports and missing MCP UX wrappers/tools. Core UX tests passed and the independent Chromium job passed. This is the production-integration RED baseline.

- [x] **Step 3: Implement the minimal GREEN integration**

Top-level `nolane_ui` now re-exports the UX registries/query/status surface. `mcp_server.py` exposes read-only, bounded UX wrappers and registers the seven distinct UX MCP tools without modifying V13 rule semantics.

- [x] **Step 4: Verify focused integration GREEN locally**

The reconstructed CI-green repository artifact with the post-artifact integration diff applied passes all 6 public/MCP integration tests.

- [ ] **Step 5: Verify integration GREEN on final remote head**

Require the complete GitHub Actions matrix and release gate to pass on the final feature-head SHA before closing this task.

---

### Task 8: Final quality court and delivery state

- [x] Inspect the PR integration diff for accidental authority mixing, API collisions and mutation surfaces: UX additions are read-only and namespaced separately from V13.
- [x] Remove implicit count-pressure language from the design spec; scale is defined by semantic novelty rather than a target rule/skill count.
- [x] Add semantic-owner compatibility and exact normalized operational-signature courts through observed RED→GREEN tests.
- [ ] Confirm final frozen-head CI evidence rather than reusing an earlier run.
- [ ] Update PR description so it reflects final RED/GREEN evidence rather than the obsolete pre-implementation state.
- [x] Keep `main` unchanged until the feature branch is review-ready with verified evidence.
