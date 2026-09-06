# UX Intelligence v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a first-class UX Intelligence subsystem with canonical UX mechanisms, 32 cognitive skills, 16 falsifiable operational rules, deterministic query/status APIs, and quality gates that preserve NUI's no-quota and evidence-honesty principles.

**Architecture:** Add an isolated `src/nolane_ui/ux_intelligence/` package rather than modifying the mature V13 contract in the first iteration. The package separates semantic mechanisms, cognitive skills, operational rules and catalog/query validation. Tests lock the ontology before production code is added.

**Tech Stack:** Python 3.10+, pytest, dependency-free data/validation modules.

**Spec:** `docs/superpowers/specs/2026-09-06-ux-intelligence-v1-design.md`

## Global Constraints

- Do not modify existing V13 rule semantics or force migration in v1.
- Rule/skill counts are descriptive, never quality quotas.
- Contextual and convergence rules must never block.
- All UX rules must bind to a known mechanism and known owner skill.
- Query limits are strict integers in the range 1..100.
- Canonical outputs are sorted deterministically by stable ID.
- No generated rule loops or template-generated prose.

---

### Task 1: Lock the UX ontology with failing tests

**Files:**
- Create: `tests/test_ux_intelligence_v1.py`

**Interfaces:**
- Consumes: none.
- Produces: expected imports and invariants for `nolane_ui.ux_intelligence`.

- [ ] **Step 1: Write the failing test**

Create tests that import `UX_MECHANISMS`, `UX_SKILLS`, `UX_RULES`, `get_ux_mechanism`, `query_ux_mechanisms`, `get_ux_skill`, `query_ux_skills`, `get_ux_rule`, `query_ux_rules`, and `ux_intelligence_status`. Assert 14 mechanism IDs, 32 skill IDs, 16 rule IDs, unique IDs, exact ontology references, owner resolution, no quota fields, no blocking contextual/convergence rules, deterministic sorting and bounded query behavior.

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_ux_intelligence_v1.py -q`
Expected: FAIL during import because `nolane_ui.ux_intelligence` does not exist.

- [ ] **Step 3: Commit RED state**

Commit only the test file with message `test: define UX Intelligence v1 contract`.

---

### Task 2: Implement canonical UX mechanisms

**Files:**
- Create: `src/nolane_ui/ux_intelligence/mechanisms.py`

**Interfaces:**
- Produces: `UX_MECHANISMS: tuple[dict[str, object], ...]` containing 14 semantic primitives.

- [ ] **Step 1: Add the minimal mechanism registry**

Define the 14 canonical mechanisms from the spec with non-empty `mechanism_id`, `title`, `definition`, `diagnostic_question`, `signals`, and `non_examples` fields.

- [ ] **Step 2: Keep data explicitly authored**

Use literal records, not loops that manufacture mechanism prose.

---

### Task 3: Implement 32 canonical UX cognitive skills

**Files:**
- Create: `src/nolane_ui/ux_intelligence/skills.py`

**Interfaces:**
- Consumes: known mechanism IDs from `mechanisms.py`.
- Produces: `UX_SKILLS: tuple[dict[str, object], ...]`.

- [ ] **Step 1: Add four skills per UX domain**

Cover `goal-task`, `mental-model`, `information-architecture`, `journey-flow`, `cognitive-friction`, `comprehension`, `recovery`, and `evaluation` with four distinct cognitive operations each.

- [ ] **Step 2: Bind each skill to relevant mechanisms**

Every `related_mechanisms` entry must resolve to an existing mechanism ID.

---

### Task 4: Implement 16 high-confidence operational UX rules

**Files:**
- Create: `src/nolane_ui/ux_intelligence/rules.py`

**Interfaces:**
- Consumes: mechanism IDs and skill IDs.
- Produces: `UX_RULES: tuple[dict[str, object], ...]`.

- [ ] **Step 1: Author rules explicitly**

Create 16 rules covering progress preservation, task-context preservation, destructive-consequence disclosure, false completion, dead-end recovery, cross-step consistency, navigation identity, stale task context, repeated-input elimination when semantically redundant, recovery reachability, scope disclosure, interruption recovery, mental-model mismatch, hidden dependencies, premature commitment and product-template convergence.

- [ ] **Step 2: Preserve enforcement boundaries**

Mechanical/behavioral directly reproducible failures may block at major/critical severity. Contextual/convergence rules use `warn` or `review` only.

---

### Task 5: Add validation and deterministic query APIs

**Files:**
- Create: `src/nolane_ui/ux_intelligence/catalog.py`
- Create: `src/nolane_ui/ux_intelligence/__init__.py`

**Interfaces:**
- Produces: `get_ux_mechanism`, `query_ux_mechanisms`, `get_ux_skill`, `query_ux_skills`, `get_ux_rule`, `query_ux_rules`, `ux_intelligence_status`.

- [ ] **Step 1: Validate registries on import**

Reject duplicate IDs, unknown references, missing required fields, forbidden quota fields, blocking contextual/convergence rules, invalid enforcement/class/status values, and empty operational planes.

- [ ] **Step 2: Implement deterministic exact lookup**

Return `None` for missing IDs and immutable canonical dict copies for hits.

- [ ] **Step 3: Implement bounded queries**

Support optional filters by domain/mechanism/class/status/text where relevant. Require `1 <= limit <= 100`; reject booleans and non-integers.

- [ ] **Step 4: Implement status**

Report validity, version, counts by UX domain, mechanism coverage, orphan mechanisms, rule class counts, and `rule_count_is_quality_target: False`, `skill_count_is_quality_target: False`.

---

### Task 6: Verify GREEN and regression safety

**Files:**
- Test: `tests/test_ux_intelligence_v1.py`
- Existing suite: unchanged.

**Interfaces:**
- Consumes: completed UX Intelligence package.
- Produces: evidence that the new subsystem is green without weakening V13.

- [ ] **Step 1: Run focused suite**

Run: `pytest tests/test_ux_intelligence_v1.py -q`
Expected: PASS.

- [ ] **Step 2: Run V13 quality suites**

Run: `pytest tests/test_rules_v13_contracts.py tests/test_rules_v13_catalog.py tests/test_rules_v13_similarity.py tests/test_rules_v13_authorship_quality.py -q`
Expected: PASS.

- [ ] **Step 3: Run project CI / workflow gates**

Confirm branch CI succeeds on supported Python versions and existing repository gates.

- [ ] **Step 4: Review diff for generated-prose/quota regressions**

Confirm no count quota is encoded and every UX rule is explicitly authored.
