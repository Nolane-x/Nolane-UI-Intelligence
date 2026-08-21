# UI Industry Batch 006 Hybrid Depth Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the canonical NUI graph from 774 to exactly 874 individually authored UI faculties while preserving smallest-sufficient routing, explicit semantic ownership, falsifiability, provenance, and the no-template/no-Cartesian rules in the approved Batch 006 design.

**Architecture:** Treat the approved spec as the ontology contract and implement the batch in eight semantic courts. Tests lock the 100-slug inventory, graph metadata, provenance, anti-duplication alarms, and exact final count before prose is admitted; each court then adds independent `SKILL.md` bodies and graph nodes under existing canonical owners only.

**Tech Stack:** Markdown canonical skills, JSON skill graph, Python `unittest`, existing `scripts/nui-validate`, Git/GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-21-ui-industry-batch-006-hybrid-depth-design.md`

## Global Constraints

- Baseline is 774 canonical skills at `main@3fece1b74051b53830e0f677503533cf44d633d1`; target is exactly 874.
- No loop, template, generator, noun substitution, or Cartesian expansion may author or rewrite `SKILL.md` prose.
- No prose from closed PR #19 may be reused.
- Every new skill needs a distinct trigger, bounded decision owner, invariants/state, characteristic failure topology, evidence obligations, falsifier, recovery, output, handoff, sibling exclusion, and provenance.
- Parent links must resolve to existing canonical owners; no bridge node may be invented to make a court look tidy.
- Similarity automation is an alarm, not semantic authority; suspicious pairs require manual ownership review.
- The generating worker cannot self-certify release readiness; exact-head tests, `nui-validate`, and GitHub Actions are independent gates.

---

### Task 1: Lock Batch 006 acceptance tests before canonical prose

**Files:**
- Create: `tests/test_ui_industry_batch_006.py`
- Read: `skills/skill-graph.json`
- Read: `docs/superpowers/specs/2026-08-21-ui-industry-batch-006-hybrid-depth-design.md`

**Interfaces:**
- Consumes: the 100 frozen slugs and eight court budgets from the spec.
- Produces: `BATCH_006`, `SLUGS`, `EXPECTED`, and tests that later tasks must satisfy.

- [ ] **Step 1: Write the failing acceptance test.** Define the eight courts with exact budgets `18,12,12,18,12,12,8,8`; define exact family/parent/output metadata for every slug; test unique slugs, frontmatter name, substantive ownership language, `Evidence`, `Failure`, `Falsification`, `Recovery`, `Output`, `Handoff`, graph registration, parent reachability, unique outputs, 874 final graph count, provenance coverage, sibling/delete rationale, normalized duplicate bodies, near-rename alarm, paragraph reuse alarm, and prohibition against scripts containing code that writes `SKILL.md`.

Use this output rule in the test fixture:

```python
def output_for(slug: str) -> str:
    for prefix in ("designing-", "engineering-", "governing-", "auditing-", "detecting-", "diagnosing-", "preserving-", "resolving-"):
        if slug.startswith(prefix):
            return slug[len(prefix):] + "-contract"
    return slug + "-contract"
```

Use these parent families: token skills → `architecting-design-tokens`; component/design-system governance → `architecting-component-systems`; adaptive composition → `adapting-responsive-layouts`; type → `crafting-typography`; human-AI execution → `designing-human-ai-interaction`; agent execution/approval → `designing-agent-autonomy-and-control`; generated-surface execution → `designing-generative-ui`; multi-agent handoff → `designing-multi-agent-surfaces`; evidence court → `binding-ui-evidence`; game/ten-foot court → `routing-ui-work`; automotive safety court → `designing-high-stakes-decisions`; multi-surface continuity → `routing-ui-work`.

- [ ] **Step 2: Commit only the test and run CI through a draft PR.** Expected result: FAIL because Batch 006 files, graph nodes, provenance and 874 count do not exist yet. Record the failing workflow run id/commit SHA in the PR description or research ledger.

### Task 2: Establish Batch 006 research/provenance and ownership ledger

**Files:**
- Create: `docs/research/UI-INDUSTRY-1000-BATCH-006.md`

**Interfaces:**
- Consumes: approved spec inventory and current source snapshots.
- Produces: one auditable row for every admitted slug plus rejected-overlap record.

- [ ] **Step 1: Record authority roles and pinned evidence families.** Include DTCG Design Tokens, Open UI/WCAG/ARIA where applicable, Storybook, Godot GUI navigation, Android Automotive/Car App UX restriction guidance, AG-UI, React Spectrum/Fluent/Carbon, browser/platform font behavior, and current multi-device/platform guidance. For repositories, record inspected commit SHA when available; for normative documents, record document/version/date.
- [ ] **Step 2: For all 100 slugs record `parent`, `trigger`, `decision_owned`, `excluded_decisions`, `failure_class`, `falsifier`, `output`, `source_roles`, and `delete_the_skill_reason` in concise individual entries.**
- [ ] **Step 3: Record rejected candidates from the spec and any additional collisions found during full baseline review.** A rejected candidate is never silently renamed into another court.
- [ ] **Step 4: Run the Batch 006 test.** Expected: provenance-related assertions move toward green while skill/graph assertions remain red.

### Task 3: Author Court A — design-system governance and interoperability

**Files:**
- Create exactly 18 `skills/<slug>/SKILL.md` files for Court A from the spec.
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: `architecting-design-tokens`, `architecting-component-systems`, provenance ledger.
- Produces: 18 bounded governance owners with unique output contracts.

- [ ] **Step 1: Author token resolution/reference/type/extension/mode/layering/migration/deprecation skills independently.** Each must use a decision model suited to its failure topology rather than a shared paragraph skeleton.
- [ ] **Step 2: Author version compatibility, anatomy, slot, state, variant, exception, contribution, parity, adoption migration, and breaking rollout skills independently.** Explicitly distinguish compatibility policy, migration execution, deprecation lifecycle, and rollout authority.
- [ ] **Step 3: Register the 18 graph nodes and run `PYTHONPATH=src python -m unittest tests.test_ui_industry_batch_006 -v`.** Expected: Court A file/graph tests green; remaining courts still red.

### Task 4: Author Courts B and C — adaptive composition and typographic engineering

**Files:**
- Create exactly 12 Court B and 12 Court C `SKILL.md` files.
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: `adapting-responsive-layouts`, `crafting-typography`, existing accessibility/globalization/data owners.
- Produces: 24 specialists without responsive×component or language×font inflation.

- [ ] **Step 1: Author Court B around container context, content pressure, region priority/order, navigation mode transition, toolbar overflow, table task preservation, form reflow, pointer↔touch density, hover loss, foldable hinges, and in-layout state continuity.**
- [ ] **Step 2: Author Court C around font loading, fallback metrics, variable axes, subsets/glyph coverage, measure, line breaking, truncation truth, numeric alignment, financial alignment, code typography, mixed baselines, and runtime text drift.**
- [ ] **Step 3: Run the batch test and manually inspect any pair with normalized SequenceMatcher ratio ≥ 0.78 even though the hard failure threshold is 0.84.** If ownership collapses, delete/consolidate rather than paraphrase.

### Task 5: Author Court D — agentic supervision and generative-UI execution

**Files:**
- Create exactly 18 Court D `SKILL.md` files.
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: `designing-human-ai-interaction`, `designing-agent-autonomy-and-control`, `designing-ai-uncertainty-and-provenance`, `designing-generative-ui`, `designing-multi-agent-surfaces`.
- Produces: execution-state, approval, recovery, generated-component and handoff specialists.

- [ ] **Step 1: Author shared-state, tool-call lifecycle and human-correction owners under human-AI interaction.**
- [ ] **Step 2: Author plan preview, approval scope/drift, interrupt/resume, partial completion, retry/replay, branching, side-effect ledger, reversibility, background run and permission escalation owners under autonomy control.**
- [ ] **Step 3: Author tool-result lifecycle, generated-component authority and schema fallback owners under generative UI; handoff visibility under multi-agent surfaces.**
- [ ] **Step 4: Falsify boundaries against parent texts: a generic autonomy/human-AI/generative-UI answer must leave at least one material runtime decision unowned if each specialist is removed.** Record any consolidation in the ledger.

### Task 6: Author Court E — evidence, regression and DesignOps

**Files:**
- Create exactly 12 Court E `SKILL.md` files.
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: `binding-ui-evidence`, critique/release gates, component-system owners.
- Produces: evidence construction/coverage/baseline/noise/update owners while release authority remains external.

- [ ] **Step 1: Author state evidence matrices, interaction regression evidence, visual baselines, responsive matrices, browser/device matrices, accessibility evidence packets, manual review contracts, environment drift, consumer regression tests, story-state fixtures, diff-noise triage, and baseline-update governance.**
- [ ] **Step 2: Verify each skill states what it cannot certify.** None may convert structural or screenshot evidence into universal usability/accessibility/safety claims.
- [ ] **Step 3: Run the batch acceptance test plus `tests/test_completion_integrity.py` and `tests/test_clean_delivery_contract.py`.**

### Task 7: Author Courts F and G — game/ten-foot and automotive HMI

**Files:**
- Create exactly 12 Court F and 8 Court G `SKILL.md` files.
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: `routing-ui-work`, `designing-high-stakes-decisions`, platform behavior evidence.
- Produces: modality-specific state machines and safety-constrained HMI owners.

- [ ] **Step 1: Author directional focus, remote navigation, controller disconnect, prompt switching, remapping, multiplayer focus ownership, ten-foot density, HUD priority, pause overlays, split-screen safe regions, menu-stack recovery, and gameplay↔menu input handoff.** Use explicit focus/input state and recoverability evidence rather than web keyboard analogies.
- [ ] **Step 2: Author driving lockouts, warning priority, distraction-aware density, rotary focus, instrument-cluster priority, driver/passenger authority split, vehicle-state controls, and modality fallback.** Separate safety authority from mere responsive/adaptive behavior.
- [ ] **Step 3: Check automotive claims against applicable platform guidance; label jurisdiction/OEM-dependent rules instead of universalizing one platform implementation.**

### Task 8: Author Court H — cross-device and multi-surface continuity

**Files:**
- Create exactly 8 Court H `SKILL.md` files.
- Modify: `skills/skill-graph.json`

**Interfaces:**
- Consumes: existing sync, notification/deep-link, collaboration and responsive-state owners.
- Produces: handoff, companion authority, second-screen, continuation, capability negotiation, task preservation, conflict and proximity specialists.

- [ ] **Step 1: Author all eight skills with explicit source-device/target-device/authority/state/freshness models.**
- [ ] **Step 2: Run delete-the-skill tests against `preserving-responsive-state-continuity`, collaboration conflict owners, mobile deep links and generic synchronization owners.** Reject any Court H owner that cannot retain a unique cross-device decision.

### Task 9: Global graph, prose, routing, provenance and release-count integration

**Files:**
- Modify: `skills/skill-graph.json`
- Modify: `README.md`
- Modify: `README-VN.md`
- Modify: `README-CN.md`
- Modify any count/release artifact that the existing suite proves is authoritative.
- Update: `docs/research/UI-INDUSTRY-1000-BATCH-006.md`

**Interfaces:**
- Consumes: all 100 skill bodies and final graph.
- Produces: exact 874 count and synchronized public surfaces.

- [ ] **Step 1: Run Batch 006 duplicate/near-rename/paragraph/section-skeleton alarms across all 100 new bodies.** Manually review flagged pairs; do not lower thresholds to hide collisions.
- [ ] **Step 2: Verify every graph output is unique, every parent resolves to `using-nolane-ui`, and every new slug appears once.**
- [ ] **Step 3: Change README count strings from 774 to 874 only after `len(graph["skills"]) == 874`.** Do not change package version unless the repository release policy independently requires it.
- [ ] **Step 4: Record admitted/rejected final inventory and exact branch revision in the research ledger.**

### Task 10: Exact-head verification and branch completion

**Files:**
- No production edits unless a failing verification produces a concrete defect and a new red/green test cycle.

**Interfaces:**
- Consumes: candidate exact revision.
- Produces: independently verified completion evidence.

- [ ] **Step 1: Run the full repository suite.**

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Expected: exit 0, zero failures/errors.

- [ ] **Step 2: Generate a completion packet bound to the exact commit.**

```bash
PYTHONPATH=src python scripts/nui-release-packet --output /tmp/nui-b006-completion.json --revision "$REVISION" --source "Batch 006 exact-head verification"
```

- [ ] **Step 3: Validate the exact revision.**

```bash
PYTHONPATH=src python scripts/nui-validate . --packet /tmp/nui-b006-completion.json --revision "$REVISION"
```

Expected: exit 0.

- [ ] **Step 4: Push/refresh the PR and require GitHub Actions `Verify NUI` green on the exact head.** If CI disagrees with local evidence, CI wins and the batch remains incomplete.
- [ ] **Step 5: Compare branch to `main` and inspect changed-file count/content classes.** Expected: spec + plan + Batch 006 test + provenance ledger + 100 canonical skill files + graph/count integration; no generated copies, unrelated refactors or abandoned artifacts.
- [ ] **Step 6: Only after all gates are green, merge the branch and re-read `main` exact head to verify the merge result and canonical count.**
