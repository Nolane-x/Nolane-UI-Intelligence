# Nolane UI Intelligence v3 — Product Closure & Learning Design

**Date:** 2026-08-12  
**Scope:** architecture wave on top of NUI v2 (125-skill graph)  
**Goal:** make material UI work functionally closed, implementation-ready, visually evidence-driven, and capable of project-scoped learning without replacing existing specialist ownership.

## 1. Problem statement

NUI v2 has strong local faculties for task flows, navigation, component semantics, component states, visual direction, anti-genericity, accessibility, platform fit, human factors, AI agency, and release evidence. The remaining failure class is global: every local artifact can look reasonable while the product as a whole is incomplete.

Representative failures:

- a real product capability has no visible or discoverable UI entry point;
- a screen exists but no valid route, control, command, deep link, or contextual transition reaches it;
- a button exists but its action is undefined, duplicated under a conflicting label, or points at a nonexistent capability;
- an action exists in product logic but is reachable only by hidden knowledge;
- permission, offline, responsive, locale, concurrency, or async variants silently remove a capability;
- a flow reaches a terminal-looking screen with no next step, exit, recovery, or truthful blocked state;
- implementation invents labels, controls, states, icons, or transitions because the design handoff specified only screenshots or broad prose;
- repeated AI design sessions reset to generic visual defaults instead of learning which mechanisms succeeded, failed, or were rejected in this project;
- graph metadata and skill documents drift by a single canonical identifier, so one subsystem expects an artifact name that another never emits.

The v3 response is not a bigger checklist. It is a cross-artifact closure plane with deterministic referential-integrity gates plus a project-owned visual-learning loop.

## 2. Design principles

1. **Closure before polish.** Beauty cannot compensate for an unreachable capability, ghost action, dead end, or missing material state.
2. **Progressive disclosure is valid.** Completeness means reachable/discoverable at the right frequency and consequence, not that every action is simultaneously visible.
3. **One semantic action, one canonical identity.** Multiple entry mechanisms may alias the same action; they may not silently fork semantics.
4. **No orphan product truth.** Product requirements, routes, feature flags, existing UI, localization, analytics/event names, APIs/domain models, and tests are candidate evidence of real capabilities. Conflicts are surfaced, not averaged away.
5. **No screenshot-only specification.** A material design handoff identifies controls, labels, actions, states, transitions, feedback, permissions, responsive behavior, accessibility semantics, and visual contracts.
6. **Runtime evidence is different from static proof.** Static graph closure can show that an intended path exists in the model; behavioral verification is required to prove the implemented path executes.
7. **Visual research extracts mechanisms, not skins.** References may inform hierarchy, composition, typography, density, motion, interaction, or material treatment. NUI must not copy an external product's distinctive expression by default.
8. **Learning is contextual and reversible.** Design memory records context, evidence, confidence, expiry/decay, and supersession. A preference learned for one project/domain cannot silently become a universal law.
9. **Canonical identifiers are contracts.** Parent IDs, output IDs, action IDs, surface IDs, capability IDs, source IDs, and evaluator references are machine-checked.
10. **Unknown remains open.** If a product capability or user path cannot be established from available evidence, closure is `UNKNOWN/BLOCKED`, not inferred complete.

## 3. Architecture

### 3.1 Functional Closure Plane

The plane compiles:

`product truth → capabilities → surfaces → destinations → actions → controls/input bindings → states/transitions → feedback/recovery → scenarios → executable probes`

Each link has stable IDs and referential integrity.

#### A — `mapping-product-capabilities-to-ui`

**Owns:** whether every material user-visible capability has an intentional UI representation or explicit non-UI rationale.  
**Output:** `capability-surface-ledger`.

Record capability ID, source evidence, actor/role, user goal, frequency, consequence, lifecycle, prerequisites, feature/permission constraints, owning surfaces, entry points, primary/secondary actions, and approved non-UI rationale. Detect capabilities visible in routes/code/tests/requirements but absent from UI inventory.

#### B — `architecting-action-command-systems`

**Owns:** product-wide semantic action identity independent of presentation or modality.  
**Output:** `action-registry`.

Each action has canonical ID, verb/object/scope, preconditions, consequence, reversibility, permission, frequency, risk, trigger aliases, canonical label semantics, feedback, postcondition, failure/recovery, telemetry intent, and idempotency policy where applicable. Buttons, menu items, keyboard shortcuts, gestures, voice commands, context menus, links, and agent actions may bind to one canonical action. Duplicate semantic actions require explicit aliasing; one label may not silently mean incompatible actions in the same context.

#### C — `proving-interface-reachability`

**Owns:** whether required surfaces and actions are reachable from valid entry points under applicable role/permission/context constraints.  
**Output:** `reachability-proof`.

Model a directed graph of entry points, surfaces, overlays/modes, and transitions. Compute unreachable required surfaces, hidden-only paths, invalid targets, dead ends, cycles without escape, missing return/up behavior, permission traps, and responsive/platform capability loss. A direct URL counts only when it is an intentional product entry point, not a secret implementation path used to excuse missing navigation.

#### D — `modeling-ui-scenario-coverage`

**Owns:** product-level combinations that materially change capability or path availability.  
**Output:** `scenario-coverage-model`.

Combine only material dimensions: role, permission, account/data state, empty/large content, network/async state, locale/direction, viewport/posture, modality, concurrency, feature flag, external dependency, and interruption/re-entry. This is broader than component-state algebra: it asks whether the whole task/capability remains usable.

#### E — `compiling-implementation-ready-ui-specifications`

**Owns:** whether design artifacts are specific enough that implementation does not invent material UI decisions.  
**Output:** `ui-specification-bundle`.

For every material surface/region/control bind exact or governed copy, semantic role, action/destination ID, visibility/disclosure rule, states, feedback, focus/keyboard/accessibility semantics, responsive transformation, content stress, visual tokens/component variant, icon/media treatment, motion, permissions, analytics intent when relevant, and open unknowns. Cross-reference closure artifacts instead of duplicating them.

#### F — `critiquing-functional-completeness`

**Owns:** independent falsification of cross-artifact product closure.  
**Output:** `functional-closure-findings`.

Hunt orphan capabilities/destinations, ghost controls, duplicate or conflicting action semantics, invisible-only features, unreachable permission states, missing exits/recovery, inconsistent labels, capability loss across responsive/platform transformations, and specification gaps. Report concrete IDs and counterexample paths.

#### G — `verifying-interface-behavior`

**Owns:** runtime evidence that intended paths and controls actually execute in an inspectable implementation.  
**Output:** `behavior-verification-ledger`.

Derive behavioral probes from closure artifacts: navigate, activate, cancel, back/up, permission denial, failure/retry, async duplicate prevention, deep link, keyboard/alternative route, responsive route, and relevant scenario probes. Capture observed target/state/feedback and artifact revision. Without runtime capability, affected obligations stay UNKNOWN; static graph validity is not promoted to runtime PASS.

### 3.2 Aesthetic Learning Plane

#### H — `researching-interface-references`

**Owns:** collecting fresh relevant interface references and decomposing them into transferable mechanisms without copying visual identity.  
**Output:** `reference-mechanism-ledger`.

For each reference record source, authority/provenance, freshness, product/context similarity, inspected evidence, mechanism dimensions (hierarchy, composition, type, density, color behavior, surface/material, imagery, interaction, motion, content), transfer rationale, incompatibilities, license/copying constraints, and confidence. Cluster near-duplicate references so trend repetition does not masquerade as independent evidence.

#### I — `iterating-visual-design-with-evidence`

**Owns:** the render/compare/repair loop after a direction exists.  
**Output:** `visual-iteration-ledger`.

Track direction/candidate ID, render or screenshot evidence, viewport/state, intended thesis, observed strengths, critic findings, repair hypothesis, changed variables, preserved strengths, regression risks, and next verdict. Stabilize macro hierarchy/composition before micro-polish. A self-authored score without inspectable evidence cannot close the loop.

#### J — `learning-from-design-outcomes`

**Owns:** updating project-scoped design memory from observed outcomes rather than accumulating arbitrary taste rules.  
**Output:** `design-memory-delta`.

Memory entries contain context tags, learned mechanism/constraint, evidence, source event, confidence, scope, expiration/decay policy, contradictions, supersession, and positive/negative/unresolved result. A user correction may be stored only with enough reason/scope to generalize safely. Accessibility/correctness floors cannot be overridden by learned preference.

### 3.3 Existing faculties deepened, not duplicated

- `routing-ui-work`: add product scope, closure requirement, product-truth sources, implementation-spec requirement, and visual-learning mode; hard-route closure skills for feature-rich/multi-screen/material product work.
- `designing-task-flows`: reference canonical capability/action/surface IDs and distinguish local flow closure from product-wide closure.
- `designing-navigation`: consume reachability/action registry and expose intentional entry mechanisms.
- `modeling-component-semantics`: every interactive element binds a canonical action or destination ID.
- `modeling-component-states`: state IDs become consumable by scenario/spec/behavior artifacts.
- `compiling-ui-obligations`: compile hard closure and runtime behavior obligations.
- `gating-ui-completion`: require closure/spec proof when routed and runtime evidence for implemented-behavior claims.
- `exploring-aesthetic-directions`: consume reference mechanisms and relevant design memory while preserving real divergence.
- `preventing-generic-ui`: use project history and current-reference clustering to detect repeated agent defaults.
- `critiquing-visual-design`: require inspectable render evidence when the claim concerns rendered quality.
- `writing-interface-copy`: bind action labels/messages to canonical action identity across trigger/progress/success/failure/undo.

## 4. Deterministic kernel

Add `src/nolane_ui/closure.py` and `src/nolane_ui/visual_intelligence.py`.

### `validate_functional_closure(bundle)`

Machine-checkable invariants:

- unique capability/surface/action/control IDs and resolved references;
- every required capability has an owning surface or accepted non-UI rationale;
- every required surface is reachable from an applicable intentional entry point;
- every mandatory action has a discoverable binding for an applicable modality/context or explicit external/system-only rationale;
- controls cannot target nonexistent actions/destinations;
- duplicate semantic action keys require alias/supersession relation;
- labels cannot bind incompatible action semantics in the same context without disambiguation;
- required nonterminal surfaces cannot be dead ends;
- blocked/permission-denied paths expose truthful exit/escalation/recovery when applicable;
- material actions define precondition, postcondition, failure, feedback, and recovery;
- critical scenarios map to a path and expected outcome;
- known material UNKNOWNs block closure PASS.

### `validate_ui_specification(spec, closure)`

Require every required surface and interactive binding to be specified; each control binds exactly one semantic role/action-or-destination; material states/scenarios are covered or explicitly N/A; exact/governed copy exists; accessibility/focus/input behavior exists where applicable; responsive transformation preserves capability identity; visual component/token references resolve where relevant; material unresolved implementation decisions block `IMPLEMENTABLE`.

### `validate_skill_contract_integrity(graph, skill_docs)`

Require every graph skill file, exact Parent Contract, exact canonical graph output identifier in the skill Output Contract, and no silent output-ID drift. Shared output types such as verifier finding sets are explicit exceptions. This gate repairs the 23 output-ID drift cases found in v2.

### Visual validators

`validate_reference_mechanism_ledger` and `validate_design_memory` check provenance, context, evidence, scope, contradictions/supersession, and expiry. They never claim a style is objectively beautiful.

## 5. Routing

Add profile fields:

- `product_scope`: element | screen | flow | feature | multi-feature-product | system
- `closure_requirement`: local | flow | product-wide
- `product_truth_sources[]`: requirements, current-ui, routes, feature-flags, localization, analytics, domain-model-api, tests, component-explorer, research
- `implementation_spec_requirement`: none | bounded | production
- `visual_learning_mode`: none | reference-refresh | project-memory | evidence-iteration

Hard routes:

- `multi-feature-product`/`system` or explicit `product-wide` closure → A+B+C+D+E+F;
- material `implement`/`verify` with product-wide closure → G;
- production specification requirement → E;
- materially open visual direction + reference refresh → H;
- visual implementation with inspectable render capability + evidence iteration → I;
- project memory requested or existing → J while `exploring-aesthetic-directions` remains direction owner.

The router still chooses the smallest sufficient graph. A single button fix does not load product-wide closure.

## 6. Research and provenance

Create `knowledge/source-ledger-closure-v3.json` containing only mechanisms actually absorbed. Source classes include standards/accessibility guidance, government human-factors guidance, mature design systems, first-party agent skills, and open-source agent design systems. Each record carries licensing/copying constraints; no external skill prose is copied into NUI.

Mechanisms synthesized in this wave include model/task/path reasoning and error tolerance; consistent identification/focus/semantic operation; task/service navigation and progressive disclosure; menu/overflow discoverability; implementation inventories and browser/render fidelity loops; project-scoped design memory; and event/action/page-transition graph ideas from model-based GUI testing.

## 7. Evals

Add `evals/v3/` adversaries that must fail on incomplete models and pass only on repaired models:

1. screen exists but has no incoming reachable path;
2. feature exists but owns no surface;
3. control targets unknown action;
4. action exists but has no user-discoverable binding;
5. duplicate semantic actions lack aliasing;
6. same label binds incompatible actions in one context;
7. permission path dead-ends;
8. responsive transformation deletes a capability;
9. async action permits duplicate commit without pending/feedback semantics;
10. surface is reachable only by secret implementation URL;
11. scenario references nonexistent state/surface/action;
12. UI spec omits required control/state/copy/accessibility contract;
13. graph output ID and SKILL.md output ID disagree;
14. visual reference lacks mechanism/provenance;
15. design memory lacks scope/reason/evidence or is stale/superseded;
16. visual iteration claims PASS without render evidence;
17. high visual score attempts to compensate for functional closure failure.

## 8. Repository hygiene fixes

- align all 23 observed graph output identifiers with SKILL.md Output Contracts using graph IDs as canonical unless compatibility requires otherwise;
- align `nui.config.json` authority order with the graph authority taxonomy;
- bump package/config version from `0.1.0` to `0.3.0` for the v3 architecture milestone;
- update package description;
- rename legacy CI artifact/temp names from `nui-v1-*` to version-neutral/current names;
- add contract tests so these drifts cannot return silently.

## 9. Completion criteria

Merge only when all pre-existing and new tests pass; RED→GREEN closure regressions are demonstrated; parent/output integrity is clean; each new skill is substantive and uniquely owned; router hard routes cover closure/visual-learning cases; repository validator requires v3 schemas/manifests/source ledger/evals; PR CI passes on exact final head; merged `main` CI passes again; and the milestone ZIP contains the full project, tests, docs, research ledger, completion packet, and checkpoint metadata.

## 10. Explicit non-goals

- no claim of objectively guaranteed world-best beauty;
- no automatic copying of commercial/proprietary interfaces;
- no requirement that every function be a visible button at all times;
- no substitution of static graph validation for usability research/runtime verification;
- no monolithic mega-skill repeating specialist content;
- no permanent research-saturation claim.
