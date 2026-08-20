# UI Industry Batch 005 Research-First Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add exactly 100 independently authored, non-duplicative canonical UI skills to the 674-skill NUI graph.

**Architecture:** Research and admission are separated from prose authoring. An explicit court inventory is locked in a failing acceptance test, each admitted `SKILL.md` is authored independently, graph/provenance integration is deterministic, and exact-head validation gates completion.

**Tech Stack:** Markdown canonical skills, JSON skill graph, Python `unittest`, NUI repository validators, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-20-ui-industry-batch-005-research-first-design.md`

## Global Constraints

- Exactly 100 new canonical skill owners must survive semantic overlap review.
- Canonical skill prose must not be produced or transformed by loops, templates, Cartesian products, noun substitution, or bulk generation.
- Closed PR #19 prose and inventory are not canonical input and must not be reused as Batch 005 content.
- External repositories are evidence/mechanism sources, never trade-dress templates.
- Automation is limited to deterministic bookkeeping, tests, graph registration, provenance indexing, hashes, and collision detection.
- Missing evidence is UNKNOWN/BLOCKED, never PASS.

---

### Task 1: Lock research courts and TDD acceptance

**Files:**
- Create: `tests/test_ui_industry_batch_005.py`
- Create: `docs/research/UI-INDUSTRY-1000-BATCH-005-INVENTORY.md`

**Interfaces:**
- Consumes: 674-node `skills/skill-graph.json` baseline.
- Produces: explicit 100-slug `BATCH_005` inventory and exact metadata expectations.

- [ ] **Step 1: Write failing acceptance test** asserting exactly 100 unique slugs, 774 graph nodes, file/frontmatter presence, locked parent/family/output metadata, output uniqueness, parent reachability, required substantive sections, provenance presence, and duplicate/trivial-rename rejection.
- [ ] **Step 2: Commit only tests/inventory and open/update draft PR.**
- [ ] **Step 3: Observe CI RED because Batch 005 skill files and graph nodes do not exist yet.**

### Task 2: Research and provenance ledger

**Files:**
- Create: `docs/research/UI-INDUSTRY-1000-BATCH-005.md`

**Interfaces:**
- Consumes: external repositories/standards plus the 674-skill ownership graph.
- Produces: one provenance/ownership row per admitted slug with source role, parent, output, decision boundary, and rejected-overlap notes.

- [ ] **Step 1: Record current source families and mechanism observations by court.**
- [ ] **Step 2: Record anti-overlap decisions against existing NUI owners.**
- [ ] **Step 3: Ensure all 100 admitted slugs have provenance rows before completion.**

### Task 3: Author mobile-native + visual-builder skills

**Files:**
- Create: 22 `skills/<slug>/SKILL.md` files.

**Interfaces:**
- Consumes: Task 1 locked metadata and Task 2 evidence.
- Produces: individually authored mobile-native and visual-builder decision owners.

- [ ] **Step 1: Author each mobile-native skill separately from its domain state and failure model.**
- [ ] **Step 2: Author each visual-builder skill separately; do not reuse prose structure as a body template.**
- [ ] **Step 3: Review sibling boundaries before graph registration.**

### Task 4: Author BI + clinical skills

**Files:**
- Create: 26 `skills/<slug>/SKILL.md` files.

**Interfaces:** same canonical skill contract as Task 3.

- [ ] **Step 1: Author 12 BI skills around metric/query/dashboard lineage and analysis continuity.**
- [ ] **Step 2: Author 14 clinical skills around patient/encounter/order/result/imaging safety semantics.**
- [ ] **Step 3: Explicitly distinguish clinical safety authority from generic high-stakes UX.**

### Task 5: Author public-service + marketplace skills

**Files:**
- Create: 20 `skills/<slug>/SKILL.md` files.

- [ ] **Step 1: Author public-service skills around eligibility, evidence, save/return, assisted digital, identity and change reporting.**
- [ ] **Step 2: Author marketplace skills around seller/listing/inventory/order/fulfillment/dispute/payout/trust boundaries.**
- [ ] **Step 3: Remove any candidate whose decision collapses into an existing forms/commerce owner and replace only with independently admitted coverage.**

### Task 6: Author realtime + XR skills

**Files:**
- Create: 20 `skills/<slug>/SKILL.md` files.

- [ ] **Step 1: Author realtime communication skills around membership, synchronization, encryption, calls, screenshare and moderation.**
- [ ] **Step 2: Author ten XR specialists under the existing `designing-spatial-xr-interfaces` parent.**
- [ ] **Step 3: Preserve boundaries against existing chat, collaboration, gaze-hand-spatial-input and 3D/CAD owners.**

### Task 7: Author personalization + design-to-code skills

**Files:**
- Create: 12 `skills/<slug>/SKILL.md` files.

- [ ] **Step 1: Author six recommendation/personalization skills with ranking-feedback and user-control semantics.**
- [ ] **Step 2: Author six design-to-code handoff skills with mapping, intent and drift evidence.**
- [ ] **Step 3: Audit for overlap with existing AI personalization, token, design-system and fidelity owners.**

### Task 8: Deterministic graph integration

**Files:**
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: exact locked `BATCH_005` metadata.
- Produces: 774-node canonical graph.

- [ ] **Step 1: Insert exactly 100 nodes with locked family/parent/output metadata.**
- [ ] **Step 2: Confirm no output collisions and all chains reach `using-nolane-ui`.**
- [ ] **Step 3: Remove any one-time bookkeeping artifact; no finalizer remains in product tree.**

### Task 9: Documentation/count integration

**Files:**
- Modify: `README.md`
- Modify: `README-VN.md`
- Modify: `README-CN.md`
- Modify other repository-facing canonical-count assertions only where they represent current graph count rather than historical baselines.

- [ ] **Step 1: Change current canonical count from 674 to 774.**
- [ ] **Step 2: Preserve historical 174/274/374/474/674 batch evidence where those values describe past states.**

### Task 10: GREEN verification and exact-head completion

**Files:** no production additions unless verification finds a defect.

- [ ] **Step 1: Run `python -m unittest tests.test_ui_industry_batch_005 -v`.**
- [ ] **Step 2: Run full `python -m unittest discover -s tests -v`.**
- [ ] **Step 3: Run `python scripts/nui-validate .`.**
- [ ] **Step 4: Inspect duplicate/near-duplicate and suspicious-scaffold findings; fix substance, never suppress valid findings.**
- [ ] **Step 5: Verify GitHub Actions on the exact PR head.**
- [ ] **Step 6: Merge only the verified head, then re-read `main` and confirm exactly 774 canonical skills.**
