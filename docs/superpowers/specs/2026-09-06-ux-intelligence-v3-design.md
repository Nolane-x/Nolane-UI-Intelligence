# UX Intelligence v3 Design

## Status

Approved architectural direction: **Autonomous UX Scientist**.

This design follows the merged UX Intelligence v2 baseline on `main` and deliberately preserves its evidence and authority boundaries.

## Goal

Make NUI capable of discovering which user journeys matter, constructing evidence-bounded product/goal models, comparing UX behavior across revisions, and prioritizing verified regressions by user impact.

The v3 north-star pipeline is:

`product evidence -> product model -> goal graph -> journey hypotheses -> candidate ranking -> V11 execution -> verified journey evidence -> temporal regression ledger -> impact ranking`

The critical distinction is:

> **Discovery may infer hypotheses; only verification may assert findings.**

An inferred goal, task, journey, or product relationship is never automatically elevated into blocking UX authority. V3 uses inference to decide what to inspect and test, not to fabricate UX failures.

## Why v3 exists

UX Intelligence v2 is intentionally strong at verification once callers provide:

- a structured `UXJourneySpec`;
- explicit runtime evidence or V11 bindings;
- product-local expectations and success criteria.

That boundary is correct, but it leaves three important capabilities outside the system:

1. **What should be tested?** V2 does not discover critical journeys on its own.
2. **What changed over time?** V2 verifies one observation set but does not retain revision-to-revision semantic UX history.
3. **What should be fixed first?** V2 findings inherit severity/enforcement but do not rank by product goal criticality, task frequency, recoverability, or regression evidence.

V3 closes those gaps without turning heuristic discovery into blocking authority and without creating a second browser runtime.

## Design principles

1. **Hypothesis before authority.** Product/goal/journey discovery may produce candidates with explicit confidence and evidence refs, but candidates do not become blocking findings merely because the discovery engine believes them.
2. **Evidence lineage is first-class.** Every discovered node, edge, journey candidate, temporal comparison, and impact signal identifies the observations or product contracts that support it.
3. **V11 remains the runtime owner.** V3 may request or consume captures, but browser execution and normalization remain V11 responsibilities.
4. **V2 remains the finding authority.** When a candidate becomes executable, journey verification delegates to the existing v2 verifier and existing UX rules/evaluators.
5. **No universal UX folklore.** V3 does not encode fixed click-count targets, universal friction minimization, or arbitrary information-capacity limits.
6. **Semantic novelty over catalog size.** V3 adds model/discovery/regression capabilities, not count-based rule expansion.
7. **Temporal comparison is semantic, not merely visual.** A regression may be a lost recovery path, extra required commitment, contradictory state, lost object context, or broken success evidence even when pixels barely change.
8. **Uncertainty is visible.** Inferred facts expose `origin`, `confidence`, and `evidence_refs`; missing evidence stays missing.
9. **Determinism at authority boundaries.** Heuristic scoring may rank what to inspect, but promotion into verified state, regression classification, and blocking findings follows explicit deterministic contracts.
10. **Backward compatibility.** V1 mechanisms/skills/rules and v2 bridge/provenance/journeys/evaluators/verifier remain valid public surfaces.

## Scope

V3 contains three tightly coupled core subsystems plus integration surfaces:

1. **Product/Goal Model** — a provider-neutral representation of what the product exposes and what users appear to be trying to accomplish.
2. **Autonomous Journey Discovery** — evidence-bounded generation and ranking of journey hypotheses that can be promoted into v2-compatible journey specs.
3. **Temporal UX Evidence & Regression** — immutable revision snapshots and semantic comparison of verified journey outcomes.
4. **Impact Ranking** — deterministic prioritization metadata applied only after a failure/regression is verified.

Counterfactual repair generation, multi-persona simulation, and large-scale empirical calibration are explicitly deferred to later v3.x work unless required to validate these foundations.

---

# 1. Product Model

## Purpose

Represent a product as meaningful objects, surfaces, actions, and observable states instead of a flat collection of pages.

The model answers questions such as:

- What user-facing objects exist?
- Which surfaces expose them?
- Which actions can change their state?
- What state transitions have actually been observed?
- Which relationships are declared, observed, or inferred?

## `UXProductModel`

Required top-level fields:

- `product_id`
- `revision`
- `surfaces`
- `objects`
- `actions`
- `states`
- `relationships`
- `evidence_refs`
- `provenance_ids`
- `status`

### Surface record

- `surface_id`
- `kind` — e.g. `route`, `dialog`, `panel`, `sheet`, `workspace`, `native-screen`
- `locator` — provider-neutral route/path/surface identifier
- `labels`
- `available_action_ids`
- `visible_object_ids`
- `origin`
- `confidence`
- `evidence_refs`

### Object record

- `object_id`
- `object_type`
- `labels`
- `identity_fields`
- `state_ids`
- `origin`
- `confidence`
- `evidence_refs`

### Action record

- `action_id`
- `label`
- `action_kind`
- `source_surface_id`
- `object_id`
- `observed_target_surface_ids`
- `observed_state_changes`
- `commitment_level`
- `origin`
- `confidence`
- `evidence_refs`

### State record

- `state_id`
- `object_id`
- `attributes`
- `origin`
- `confidence`
- `evidence_refs`

### Relationship record

- `relationship_id`
- `source_id`
- `relation`
- `target_id`
- `origin`
- `confidence`
- `evidence_refs`

Allowed initial relationship kinds:

- `contains`
- `acts-on`
- `navigates-to`
- `transitions-to`
- `preserves`
- `requires`
- `recovers-via`
- `succeeds-with`

The relationship vocabulary is closed in v3.0 so graph semantics remain deterministic and testable.

## Origin and confidence

Every discovered semantic record carries:

- `origin`: `declared`, `observed`, or `inferred`;
- `confidence`: float in `[0.0, 1.0]`;
- non-empty `evidence_refs` unless the record is explicitly declared by a product contract with provenance.

Rules:

- `declared` and `observed` facts may participate in deterministic journey promotion if their evidence contracts are complete.
- `inferred` facts may rank exploration and propose candidates, but may not independently satisfy a v2 verification requirement.
- confidence is a ranking signal, never enforcement authority.

## Normalization

Product-model normalization may:

- sort IDs;
- canonicalize tuple/list containers;
- normalize route/path shapes;
- de-duplicate exact evidence refs;
- merge identical records with evidence union.

It may not invent missing object identity, state transitions, recovery semantics, or success criteria.

---

# 2. Goal Graph

## Purpose

Represent user intent above page-level navigation.

The graph should let NUI reason about:

`goal -> task -> object/action -> state transition -> success`

instead of treating UI structure as the product architecture.

## `UXGoalGraph`

Required fields:

- `product_id`
- `revision`
- `nodes`
- `edges`
- `evidence_refs`
- `provenance_ids`
- `status`

### Node kinds

- `goal`
- `task`
- `object`
- `action`
- `state`
- `outcome`

Node fields:

- `node_id`
- `kind`
- `label`
- `description`
- `origin`
- `confidence`
- `evidence_refs`

### Edge kinds

- `decomposes-to`
- `acts-on`
- `requires`
- `transitions-to`
- `succeeds-when`
- `blocked-by`
- `recovers-via`

Edge fields:

- `edge_id`
- `source_id`
- `relation`
- `target_id`
- `origin`
- `confidence`
- `evidence_refs`

## Goal discovery

V3.0 supports three goal sources:

1. **Declared goals** from product contracts or caller-supplied seeds.
2. **Observed goal evidence** from repeated action/state sequences whose terminal evidence matches a declared or explicit success signal.
3. **Inferred goal hypotheses** generated from labels, action/object structure, and repeated transition patterns.

Inferred goals must be marked `inferred`; label/NLP similarity cannot silently convert them to declared/observed facts.

## Anti-feature-first court

The goal graph includes diagnostics against generic feature-first architecture. Examples of non-blocking discovery diagnostics:

- candidate goal labels identical to navigation nouns without action/outcome semantics;
- a goal decomposes only into surfaces rather than user tasks;
- a task has no object/action/outcome relationship;
- multiple goals collapse to the same generic dashboard/settings route without distinct success evidence.

These diagnostics guide discovery quality but do not create blocking UX findings by themselves.

---

# 3. Discovery Evidence Packet

## Purpose

Create a provider-neutral input boundary for autonomous discovery without coupling product semantics directly to Playwright or repository-specific parsers.

`UXDiscoveryPacket` contains:

- `product_id`
- `revision`
- `captures`
- `declared_goals`
- `declared_success_signals`
- `declared_object_hints`
- `provenance_ids`

Each capture contains:

- `capture_id`
- optional `runtime_v11` packet or normalized runtime evidence reference;
- `surface_id`
- `action_evidence`
- `transition_evidence`
- `object_evidence`
- `state_evidence`
- `success_evidence`
- `evidence_refs`

V3 does **not** require the discovery packet to expose browser-driver objects. V11 remains responsible for collection and normalization.

A caller may provide already-normalized captures, allowing offline/repository tests without a browser.

---

# 4. Autonomous Journey Discovery

## Purpose

Generate candidate journeys from product/goal evidence so callers no longer need to author every `UXJourneySpec` manually.

## `UXJourneyCandidate`

Fields:

- `candidate_id`
- `product_id`
- `revision`
- `goal_node_id`
- `title`
- `entry_state`
- `step_hypotheses`
- `success_hypotheses`
- `critical_state_hypotheses`
- `discovery_score`
- `score_components`
- `origin_summary`
- `evidence_refs`
- `provenance_ids`
- `status`

Candidate statuses:

- `hypothesis`
- `promotable`
- `promoted`
- `rejected`

A candidate is not a `UXJourneySpec` until promotion succeeds.

## Step hypothesis

Each candidate step contains:

- `candidate_step_id`
- `intent_hypothesis`
- `action_id`
- `source_surface_id`
- `expected_target_surface_ids`
- `required_context_hypotheses`
- `preserved_context_hypotheses`
- `recovery_hypotheses`
- `evidence_refs`
- `origin`
- `confidence`

## Discovery algorithm boundary

V3.0 discovery is graph-driven and bounded:

1. start from a declared/observed goal or inferred goal hypothesis;
2. enumerate reachable action/state paths from the product graph;
3. stop at explicit success evidence, explicit dead-end, bounded depth, or repeated state;
4. collapse exact duplicate paths;
5. score candidates;
6. retain explicit evidence lineage for every candidate step.

The bounded-depth control is a computational safety limit, not a UX click-count rule and never becomes a user-facing quality criterion.

## Candidate ranking

`discovery_score` is for **selection priority only**.

Initial score components:

- `goal_confidence`
- `success_evidence_strength`
- `path_evidence_coverage`
- `critical_action_presence`
- `recovery_relevance`
- `novelty_against_verified_journeys`

Each component is normalized to `[0.0, 1.0]` and exposed in `score_components`.

No hidden weighted score may create enforcement authority. The weight vector is versioned and queryable.

## Promotion to v2 journey contract

`promote_ux_journey_candidate(candidate, product_model, goal_graph, ...)` may create a v2-compatible `UXJourneySpec` only when deterministic promotion requirements are satisfied.

Minimum v3.0 promotion requirements:

1. goal resolves to a declared or observed goal node;
2. every promoted step resolves to an observed action/transition path;
3. at least one success criterion is declared or directly observed;
4. expected transitions used by the spec are supported by explicit evidence;
5. required/preserved context is included only when supported by object/state identity evidence;
6. recovery expectations are included only when declared or observed;
7. provenance resolves;
8. no inferred-only semantic field is silently treated as verified fact.

If these requirements are not met, the candidate remains `hypothesis` or `promotable-with-gaps`; the API returns structured promotion gaps rather than fabricating a spec.

A promoted candidate is fed to the existing v2 `verify_ux_journey` pipeline.

---

# 5. Autonomous Exploration Planning

## Purpose

Let NUI decide which evidence should be collected next without creating a second browser agent.

`plan_ux_discovery(candidate_or_graph, available_capabilities)` returns a bounded list of **observation requests**, not browser commands.

Observation-request fields:

- `request_id`
- `purpose`
- `target_surface_id`
- `target_action_id`
- `required_evidence_fields`
- `preferred_v11_capabilities`
- `priority`
- `because`

V11 or another authorized runtime may execute those requests and return evidence packets.

The planner cannot claim that an action succeeded merely because it requested the action.

This keeps the architecture:

`V3 planner -> observation request -> V11 collector/executor -> normalized evidence -> V3 model/discovery -> V2 verifier`

rather than introducing `V3 Playwright` alongside V11.

---

# 6. Temporal UX Evidence Ledger

## Purpose

Preserve semantic UX evidence across repository/product revisions so NUI can detect regressions rather than only evaluate isolated runs.

## `UXEvidenceSnapshot`

Fields:

- `snapshot_id`
- `product_id`
- `revision`
- `journey_id`
- `journey_fingerprint`
- `verification_status`
- `finding_fingerprints`
- `step_evidence_fingerprints`
- `success_evidence_fingerprints`
- `runtime_evidence_refs`
- `provenance_ids`
- `created_from`

Snapshots are immutable values. V3.0 may expose serialization/deserialization but does not require a hosted database.

A caller can persist them in files, artifacts, or another store. The core package remains storage-provider neutral.

## Stable fingerprints

Fingerprints are deterministic hashes over normalized semantic content, not timestamps or object addresses.

A journey fingerprint includes stable journey structure and product-local expectations. A finding fingerprint includes rule identity plus normalized step/expected/observed semantic identity.

Evidence refs are retained separately so two equivalent findings can be compared even if the capture IDs differ.

---

# 7. Semantic UX Regression Engine

## Purpose

Compare verified snapshots across revisions and identify meaningful UX regressions.

`compare_ux_snapshots(baseline, candidate)` returns:

- `comparison_id`
- `baseline_revision`
- `candidate_revision`
- `journey_id`
- `status`
- `regressions`
- `improvements`
- `unchanged`
- `evidence_refs`

Initial regression classes:

- `journey-pass-to-fail`
- `journey-pass-to-insufficient-evidence`
- `new-rule-finding`
- `reintroduced-rule-finding`
- `success-criterion-lost`
- `required-step-became-unobserved`
- `recovery-path-lost`
- `preserved-context-regressed`
- `new-premature-commitment`
- `new-hidden-dependency`
- `new-false-completion`

The engine compares v2 verification outputs and stable fingerprints; it does not infer failure solely from visual or DOM difference.

## Regression authority

A regression means a previously evidenced semantic condition worsened at a later revision.

- If the candidate revision lacks evidence, classify as evidence regression/insufficient evidence, not as a proven UX failure unless v2 verification itself proves failure.
- A new blocking regression can only inherit blocking authority from the underlying existing UX rule/finding.
- Temporal comparison cannot escalate a `warn` rule into `block`.

---

# 8. Impact Ranking

## Purpose

Prioritize verified failures/regressions without changing rule authority.

`rank_ux_impacts(...)` adds a separate prioritization score.

Initial components:

- `goal_criticality`
- `task_frequency`
- `completion_blockage`
- `recoverability_cost`
- `affected_scope`
- `regression_confidence`
- `evidence_completeness`

Each component has:

- `value`
- `origin`
- `evidence_refs`

Inputs may be declared, observed, or inferred. Inferred impact components lower confidence and cannot alter rule enforcement.

Output:

- `priority_score`
- `priority_band`: `p0`, `p1`, `p2`, `p3`
- `confidence`
- `components`
- `because`

Priority is triage metadata, not UX truth. A `warn` finding ranked P0 remains a warning; a blocking finding ranked P3 remains blocking according to its rule authority.

---

# 9. Quality Court

V3 deterministic validation covers:

## Product model

- unique/sorted IDs;
- closed enums for record/relationship kinds;
- all graph references resolve;
- confidence is numeric, non-bool, finite, and within `[0,1]`;
- inferred records cannot omit evidence lineage;
- observed relationships cannot reference nonexistent endpoints;
- exact duplicate semantic records merge or fail deterministically.

## Goal graph

- unique nodes/edges;
- allowed node/edge kinds;
- source/target resolution;
- no self-referential invalid decomposition;
- every observed edge carries evidence;
- inferred-only goal paths remain non-authoritative.

## Journey discovery

- deterministic candidate IDs/fingerprints;
- no duplicate candidate path after normalization;
- score components bounded and queryable;
- no hidden rule-count or journey-count target;
- promotion rejects inferred-only required facts;
- promoted specs must pass existing v2 journey validation unchanged.

## Temporal ledger

- immutable normalized snapshot contract;
- revision/product/journey identity required;
- stable fingerprints independent of timestamp ordering;
- comparison requires compatible product/journey identity;
- missing candidate evidence cannot be converted to proven failure.

## Impact ranking

- authority and priority fields remain separate;
- missing impact evidence lowers confidence instead of inventing values;
- no priority calculation mutates `severity` or `enforcement`.

---

# 10. Proposed package boundaries

New v3 modules:

- `src/nolane_ui/ux_intelligence/product_model.py`
- `src/nolane_ui/ux_intelligence/goal_graph.py`
- `src/nolane_ui/ux_intelligence/discovery.py`
- `src/nolane_ui/ux_intelligence/discovery_planner.py`
- `src/nolane_ui/ux_intelligence/temporal_evidence.py`
- `src/nolane_ui/ux_intelligence/regression.py`
- `src/nolane_ui/ux_intelligence/impact.py`
- `src/nolane_ui/ux_intelligence/v3_catalog.py`

Modified integration surfaces:

- `src/nolane_ui/ux_intelligence/__init__.py`
- `src/nolane_ui/__init__.py`
- `src/nolane_ui/mcp_server.py`

V1 and v2 implementation files remain unchanged unless a verified compatibility issue requires a narrowly scoped fix.

---

# 11. Public Python API

Initial v3 public API:

- `validate_ux_product_model`
- `normalize_ux_product_model`
- `build_ux_product_model`
- `validate_ux_goal_graph`
- `build_ux_goal_graph`
- `discover_ux_journeys`
- `get_ux_journey_candidate`
- `query_ux_journey_candidates`
- `promote_ux_journey_candidate`
- `plan_ux_discovery`
- `create_ux_evidence_snapshot`
- `compare_ux_snapshots`
- `rank_ux_impacts`
- `ux_v3_status`

Read/query APIs return defensive copies and preserve the repository convention that bounded integer limits reject `bool`.

---

# 12. MCP namespace

V3 read/plan/verify surfaces remain namespaced and non-mutating with respect to product systems:

- `nui_ux_v3_status`
- `nui_build_ux_product_model`
- `nui_build_ux_goal_graph`
- `nui_discover_ux_journeys`
- `nui_query_ux_journey_candidates`
- `nui_promote_ux_journey_candidate`
- `nui_plan_ux_discovery`
- `nui_create_ux_evidence_snapshot`
- `nui_compare_ux_snapshots`
- `nui_rank_ux_impacts`

`nui_plan_ux_discovery` returns observation requests. It does not directly click/type/navigate a live product.

---

# 13. V11 integration

V11 remains the only browser/runtime collection layer.

V3 consumes either:

1. provider-neutral normalized discovery captures; or
2. V11 packets through explicit adapters/bindings.

V3 may add a discovery-specific V11 adapter, but that adapter must reuse V11 normalization and expose evidence refs for every extracted product-model fact.

No Playwright page/browser/context object may cross into `ux_intelligence` public contracts.

---

# 14. V2 integration

V3 does not replace the v2 verifier.

The contract is:

1. discovery produces a candidate;
2. deterministic promotion produces a valid v2 `UXJourneySpec` or structured promotion gaps;
3. existing `verify_ux_journey` evaluates the promoted journey;
4. verified output is snapshotted;
5. regression engine compares snapshots;
6. impact engine ranks verified failures/regressions.

This separation prevents the discovery engine from becoming a second authority system.

---

# 15. Testing strategy

Use standard-library `unittest` to match existing CI.

TDD sequence for v3:

1. contract tests for product model and goal graph before production implementation;
2. discovery candidate tests, including inferred-vs-observed authority boundaries;
3. promotion tests proving inferred-only facts cannot become v2 expectations;
4. planner tests proving it emits requests rather than execution claims;
5. temporal snapshot fingerprint tests;
6. semantic regression tests for pass->fail, lost recovery, context regression, and evidence loss;
7. impact tests proving priority cannot mutate severity/enforcement;
8. public API/MCP/status tests;
9. focused v1+v2+v3 regression;
10. repository validator;
11. exact-head GitHub Actions Python 3.10/3.11/3.12 + Real Chromium + release gate.

Negative/adversarial cases include:

- inferred goal with no evidence;
- cyclic graph paths;
- duplicate semantic actions with different IDs;
- candidate whose success criterion is only guessed from label text;
- candidate promotion with missing object identity;
- snapshot comparison across different products;
- missing evidence incorrectly classified as failure;
- impact score trying to escalate enforcement;
- arbitrary navigation noun incorrectly treated as user goal;
- browser request incorrectly treated as observed completion.

---

# 16. Initial acceptance scenarios

V3.0 is not complete until at least these scenarios pass end-to-end.

## A. Declared goal, observed route/action path

Given a declared goal and V11-backed observed transitions, discovery produces a promotable candidate, promotion returns a valid v2 journey spec, and v2 verification can pass it with explicit evidence.

## B. Inferred-only goal

Given only navigation labels and no success/transition evidence, discovery may rank a goal hypothesis but promotion refuses to synthesize authoritative success criteria.

## C. Context regression

Given baseline snapshot where object identity survives same-goal navigation and candidate snapshot where identity changes, v2 emits the existing context-preservation finding and v3 classifies a semantic regression without inventing a new rule authority.

## D. Evidence loss

Given baseline PASS and a later run missing required observation fields, v3 reports an evidence regression / insufficient evidence, not a proven UX failure.

## E. Recovery regression

Given baseline evidence of an accessible recovery path and a later verified failure of the existing recovery rule, v3 classifies `recovery-path-lost` and preserves the underlying rule severity/enforcement.

## F. Priority without authority escalation

A high-criticality verified warning may receive P0 priority, but its enforcement remains `warn`.

---

# 17. Non-goals for v3.0

V3.0 explicitly does not:

- build a second browser automation stack;
- let NLP/LLM inference directly create blocking findings;
- auto-promote inferred goals into authoritative product contracts;
- replace v2 journey verification;
- merge UX findings into V13 authority;
- create rule/skill/journey count quotas;
- claim human usability evidence from browser telemetry alone;
- use pixel difference as sufficient proof of UX regression;
- automatically edit the target product;
- generate counterfactual fixes as verified improvements;
- persist evidence in a mandatory hosted database;
- simulate unlimited personas or users;
- encode fixed click-count, memory-count, or friction folklore.

---

# 18. Success criteria

UX Intelligence v3.0 is complete only when:

1. a provider-neutral product model can be validated and built from bounded evidence;
2. every semantic model record exposes origin/confidence/evidence lineage;
3. a goal graph distinguishes user goals/tasks from surfaces/features;
4. autonomous discovery can produce deterministic journey candidates from a bounded graph;
5. inferred-only facts remain hypotheses and cannot independently satisfy promotion requirements;
6. promotable candidates become valid v2 journey specs without weakening v2 validation;
7. discovery planning emits observation requests while runtime execution remains owned by V11;
8. verified journey outputs can be converted to immutable deterministic evidence snapshots;
9. snapshot comparison detects semantic UX regressions while distinguishing evidence loss from proven failure;
10. impact ranking prioritizes verified findings/regressions without mutating severity/enforcement;
11. v1 and v2 public behavior remains backward compatible;
12. repository validation is green;
13. exact-final-head Python 3.10/3.11/3.12, real Chromium, and release-gate CI are green.

## Architectural invariant

The v3 system must always preserve this invariant:

> **Discovery decides what is worth testing. Evidence decides what happened. Existing UX rule authority decides what may be called a UX failure.**
