# NUI v3 Product Closure & Learning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a product-wide UI closure plane and evidence-driven visual-learning loop so NUI can prove feature/surface/action/control/path/spec completeness instead of certifying disconnected screens.

**Architecture:** Keep v2 specialist ownership intact. Add focused `closure.py` and `visual_intelligence.py` validators, ten unique owner/verifier skills, deterministic router predicates, schemas/evals/research ledgers, then strengthen existing kernel/visual faculties to consume the new artifacts. Canonical IDs are machine-checked and runtime behavior evidence remains separate from static closure proof.

**Tech Stack:** Python 3.10+, stdlib `unittest`, JSON/JSON Schema artifacts, Markdown Agent Skills, GitHub Actions.

## Global Constraints

- Closure before polish; a visual score cannot compensate for functional hard-gate failure.
- Progressive disclosure is allowed when the action remains reachable/discoverable in its intended context.
- No new dependency outside Python standard library.
- Existing 125-skill ownership remains authoritative unless this plan explicitly adds a new decision class.
- External sources contribute mechanisms only; do not copy skill prose or proprietary interface expression.
- Missing material evidence remains `UNKNOWN/BLOCKED`.
- Project design memory is contextual, evidence-linked, expiring/supersedable, and cannot override correctness/accessibility floors.
- Canonical parent/output/action/surface/capability identifiers are machine-checked.

---

### Task 1: Canonical skill-contract integrity and repository hygiene

**Files:** create `tests/test_skill_contract_integrity.py`; modify `src/nolane_ui/validators.py`, 23 existing skill docs, `nui.config.json`, `pyproject.toml`, `.github/workflows/verify.yml`.

**Interface:** `validate_skill_contract_integrity(graph: dict, skill_root: Path) -> dict` returning `valid`, `errors`, `checked_skills`, `shared_outputs`.

- [ ] Write failing tests for exact output ID and parent contract; synthetic mismatch must fail.
- [ ] Run the targeted test and observe RED on the 23 existing drift cases.
- [ ] Implement the validator with explicit shared-output allowance for verifier `finding-set`.
- [ ] Normalize the 23 docs to canonical graph output IDs; do not rename graph outputs.
- [ ] Align version/authority metadata and remove `nui-v1-*` workflow artifact naming.
- [ ] Run targeted and full suites.

### Task 2: Functional closure kernel and schemas

**Files:** create `src/nolane_ui/closure.py`, `schemas/functional-closure.schema.json`, `schemas/ui-specification-bundle.schema.json`, `tests/test_functional_closure.py`; modify exports/facade.

**Interfaces:** `validate_functional_closure(bundle: dict) -> dict`; `validate_ui_specification(spec: dict, closure: dict) -> dict`.

- [ ] Write a minimal valid closure fixture.
- [ ] Add failing adversaries: orphan capability/surface, ghost action, missing binding, unaliased duplicate semantic action, conflicting label, secret-URL-only reachability, nonterminal dead end, unresolved critical scenario, material unknown.
- [ ] Run targeted tests and observe RED because module/functions do not exist.
- [ ] Implement indexes, referential checks, BFS reachability, dead-end/binding/action-anatomy/alias rules.
- [ ] Implement implementation-ready specification validation.
- [ ] Add JSON schemas mirroring canonical field names.
- [ ] Export and run targeted/full suites.

### Task 3: Deterministic closure routing

**Files:** create `src/nolane_ui/closure_routing.py`, `tests/test_closure_routing.py`; modify validator facade, router skill, task-profile schema.

**Interface:** `mandatory_closure_routes(profile: dict) -> set[str]`, unioned into existing mandatory routing.

- [ ] RED-test product-wide/system routes, implement/verify behavior verification, production spec, reference refresh, visual iteration, project memory, and a local element non-trigger.
- [ ] Implement profile-only deterministic predicates.
- [ ] Extend profile schema/prose with exact enums.
- [ ] Run route/full regressions.

### Task 4: Deep functional-closure skills

Create seven skills: `mapping-product-capabilities-to-ui`, `architecting-action-command-systems`, `proving-interface-reachability`, `modeling-ui-scenario-coverage`, `compiling-implementation-ready-ui-specifications`, `critiquing-functional-completeness`, `verifying-interface-behavior`; modify graph; create `knowledge/v3-skill-manifest.json` and `tests/test_v3_skill_depth.py`.

Exact outputs are `capability-surface-ledger`, `action-registry`, `reachability-proof`, `scenario-coverage-model`, `ui-specification-bundle`, `functional-closure-findings`, `behavior-verification-ledger`.

- [ ] RED-test registration, >=700 words, required deep sections, exact outputs, and unique ownership.
- [ ] Write capability mapping with product-truth reconciliation and missing-feature detection.
- [ ] Write action system with canonical semantics, aliases, disclosure, permissions, reversibility, async/idempotency, multimodal triggers, stable vocabulary.
- [ ] Write reachability proof with directed graph, role/permission subgraphs, hidden paths, exits, deep links, responsive/platform preservation.
- [ ] Write product-level scenario coverage with risk-directed material combinations.
- [ ] Write implementation-ready UI specification to exact control/copy/state/focus/a11y/responsive/visual detail.
- [ ] Write independent closure critic and runtime behavior verifier.
- [ ] Run depth/graph/contract tests.

### Task 5: Visual intelligence kernel, provenance, and learning skills

Create `src/nolane_ui/visual_intelligence.py`, two schemas, `tests/test_visual_intelligence.py`, skills `researching-interface-references`, `iterating-visual-design-with-evidence`, `learning-from-design-outcomes`, and `knowledge/source-ledger-closure-v3.json`; modify v3 manifest/graph.

**Interfaces:** `validate_reference_mechanism_ledger`; `validate_design_memory`; outputs `reference-mechanism-ledger`, `visual-iteration-ledger`, `design-memory-delta`.

- [ ] RED-test missing provenance/mechanisms/license boundary, context/reason/evidence, expiry, and unsuperseded contradiction.
- [ ] Implement structural/date/evidence/scope validators without subjective beauty scoring.
- [ ] Build a source ledger from mechanisms actually researched; record licensing and do not copy prose.
- [ ] Write reference decomposition, render-evidence iteration, and contextual memory skills.
- [ ] Run visual/depth/contract tests.

### Task 6: Integrate closure/learning into existing cognition and completion

Modify task-flow, navigation, component semantics/states, obligations, completion gate, aesthetic direction, anti-genericity, visual critic, and UI copy. Create `tests/test_v3_integration_contract.py`.

- [ ] RED-test canonical ID consumption, closure/behavior completion precedence, reference/memory consumption, render evidence requirement.
- [ ] Deepen each skill only at its existing boundary; do not duplicate registry/reachability ownership.
- [ ] Compile closure/runtime obligations when routed.
- [ ] Block completion when functional closure is FAIL/UNKNOWN regardless of visual quality.
- [ ] Run integration/full suite.

### Task 7: v3 evals and repository aggregation

Create `evals/v3/manifest.json`, closure and visual-learning cases, `tests/test_v3_eval_integrity.py`, research report; modify repository validator, README, usage docs.

- [ ] RED-test eval manifest exact coverage, unique IDs, failure/required-skills/falsifiable expectation fields.
- [ ] Encode adversaries including the motivating screen-with-no-navigation case.
- [ ] Require v3 schemas/manifests/source ledger/evals and v3 metrics in repository validator.
- [ ] Update usage/research docs with bounded claims and rejected duplicate mechanisms.
- [ ] Run full unit suite and `python scripts/nui-validate .`.

### Task 8: Exact-revision verification, PR, merge, and milestone preservation

- [ ] Run fresh local full suite and repository validator.
- [ ] Push one coherent tree to `build/ui-closure-intelligence-v3` and inspect `main...branch` diff.
- [ ] Open a PR with bounded claims/research attribution.
- [ ] Require PR CI on exact head and no unresolved blocker; repair failures rather than weakening gates.
- [ ] Merge with expected-head guard and verify post-merge CI on exact `main` SHA.
- [ ] Download CI project archive + completion packet and verify ZIP integrity/v3 contents.
- [ ] Build `Nolane-UI-Intelligence-v3-MILESTONE-COMPLETE-<sha>.zip` with full project, CI packet, checkpoint, checksums, research artifacts.
- [ ] Persist ZIP/checkpoint to Library `/Projects/Nolane-UI-Intelligence/` and return sandbox links.
