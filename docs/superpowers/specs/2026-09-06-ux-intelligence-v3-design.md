# UX Intelligence v3 Design

## Status

Approved architectural direction: **Autonomous UX Scientist**.

This design starts from merged UX Intelligence v2 and preserves its evidence and authority boundaries.

## Goal

Make NUI capable of discovering which user journeys are worth testing, representing products in terms of user goals rather than pages, preserving UX evidence across revisions, detecting semantic regressions, and prioritizing verified problems by user impact.

The v3 north-star pipeline is:

`product evidence -> product model -> goal graph -> journey hypotheses -> candidate ranking -> observation planning -> V11 evidence -> v2 verification -> temporal snapshot -> semantic regression -> impact ranking`

The architectural invariant is:

> **Discovery decides what is worth testing. Evidence decides what happened. Existing UX rule authority decides what may be called a UX failure.**

An inferred goal, task, journey, or product relationship may guide exploration, but it cannot silently become blocking UX authority.

## Why v3 exists

UX Intelligence v2 is intentionally strong once callers already provide:

- a structured `UXJourneySpec`;
- explicit runtime evidence or V11 bindings;
- product-local expectations and success criteria.

That leaves four capabilities outside the system:

1. **What should be tested?** V2 does not discover important journeys by itself.
2. **What is the product actually about?** V2 receives journey semantics but does not maintain a product/goal representation above routes and screens.
3. **What changed over time?** V2 verifies one evidence set but does not retain revision-to-revision semantic history.
4. **What should be fixed first?** V2 findings inherit severity/enforcement but do not rank verified problems by goal criticality, completion blockage, recoverability, affected scope, or regression confidence.

V3 closes those gaps without adding a second browser runtime and without converting heuristic discovery into UX truth.

## Design principles

1. **Hypothesis before authority.** Discovery may infer candidates; verification alone may assert findings.
2. **Evidence lineage is first-class.** Every observed semantic record, candidate, promotion decision, snapshot, regression, and impact signal identifies its evidence or declared provenance.
3. **V11 remains runtime owner.** V3 plans observations and consumes normalized packets; it does not own Playwright/browser objects.
4. **V2 remains journey-verification authority.** Promoted candidates must become valid v2 journey specs and are verified by the existing v2 verifier.
5. **User intent is not directly observable from UI behavior.** Goal/task nodes may be declared or inferred, but browser telemetry alone cannot upgrade an inferred goal to declared truth.
6. **No folklore enforcement.** No fixed click-count targets, arbitrary memory limits, or unconditional friction minimization.
7. **Semantic regression over pixel regression.** Context loss, recovery loss, hidden commitment, false completion, and success-evidence loss are first-class even when visuals barely change.
8. **Uncertainty is explicit.** Inferred records expose confidence and cannot satisfy authority-gated requirements by themselves.
9. **Determinism at authority boundaries.** Heuristics may rank exploration; promotion, regression classification, and finding authority follow explicit contracts.
10. **Backward compatibility.** V1 mechanisms/skills/rules and v2 bridge/provenance/journeys/evaluators/verifier remain valid public surfaces.
11. **Semantic novelty over count.** V3 adds capabilities, not rule/skill/journey quotas.

## Scope

V3.0 contains four core subsystems plus integration surfaces:

1. **Product Model** — evidence-bounded representation of surfaces, objects, actions, states, and relationships.
2. **Goal Graph + Autonomous Journey Discovery** — explicit separation of declared user goals from inferred hypotheses, graph-driven candidate generation, ranking, and promotion.
3. **Temporal UX Evidence + Semantic Regression** — immutable revision snapshots and deterministic comparison of verified journey outcomes.
4. **Impact Ranking** — prioritization metadata for already verified findings/regressions without modifying their rule authority.

Counterfactual repair generation, multi-persona simulation, automatic target-product editing, and large-scale empirical calibration are deferred to later v3.x work.

---

# 1. Product Model

## Purpose

Represent a product as meaningful objects, surfaces, actions, and states instead of a flat list of pages.

The model answers:

- what user-facing objects exist;
- where those objects appear;
- which actions operate on them;
- which state transitions were declared or observed;
- what context must survive between surfaces;
- where recovery or success paths exist.

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

Allowed model statuses:

- `experimental`
- `active`
- `deprecated`

## Surface record

- `surface_id`
- `kind`
- `locator`
- `labels`
- `available_action_ids`
- `visible_object_ids`
- `origin`
- `confidence`
- `evidence_refs`

Initial surface kinds:

- `route`
- `dialog`
- `panel`
- `sheet`
- `workspace`
- `native-screen`

## Object record

- `object_id`
- `object_type`
- `labels`
- `identity_fields`
- `state_ids`
- `origin`
- `confidence`
- `evidence_refs`

## Action record

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

`commitment_level` is descriptive product metadata, not a universal UX judgment. Initial values:

- `none`
- `reversible`
- `state-changing`
- `destructive`
- `external-effect`

## State record

- `state_id`
- `object_id`
- `attributes`
- `origin`
- `confidence`
- `evidence_refs`

## Relationship record

- `relationship_id`
- `source_id`
- `relation`
- `target_id`
- `origin`
- `confidence`
- `evidence_refs`

Initial relationship kinds:

- `contains`
- `acts-on`
- `navigates-to`
- `transitions-to`
- `preserves`
- `requires`
- `recovers-via`
- `succeeds-with`

The vocabulary is closed in v3.0 so graph semantics remain deterministic and testable.

## Origin and confidence

Semantic records use:

- `origin`: `declared`, `observed`, or `inferred`;
- `confidence`: finite numeric value in `[0.0, 1.0]`, explicitly rejecting `bool`;
- `evidence_refs`: non-empty for `observed` and `inferred` records.

A `declared` record may rely on resolved provenance instead of runtime evidence refs.

Rules:

- `declared` or `observed` object/action/state facts may participate in deterministic journey promotion when required evidence is complete;
- `inferred` facts may rank exploration and propose candidates but cannot independently satisfy v2 verification requirements;
- confidence is a selection signal, never severity/enforcement authority.

## Normalization

Product-model normalization may:

- sort IDs;
- normalize tuple/list containers;
- normalize route/path values;
- deduplicate exact evidence refs;
- merge exact semantic duplicates by evidence union.

It may not invent object identity, state transitions, recovery semantics, success criteria, or user goals.

---

# 2. Goal Graph

## Purpose

Represent user intent above page-level navigation so NUI reasons about:

`goal -> task -> object/action -> state transition -> outcome`

rather than confusing routes or feature nouns with user goals.

## `UXGoalGraph`

Required fields:

- `product_id`
- `revision`
- `nodes`
- `edges`
- `evidence_refs`
- `provenance_ids`
- `status`

## Node kinds

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

### Origin rule for intent nodes

`goal` and `task` nodes may be:

- `declared` — supported by caller/product contract provenance;
- `inferred` — proposed from product structure, wording, repeated transitions, or explicit success evidence.

They are **not** marked `observed` merely because a user/browser traversed a path. Behavior can support an inference about intent, but it does not directly prove intent.

`object`, `action`, `state`, and `outcome` nodes may use all three origins where appropriate.

## Edge kinds

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

## Goal sources

V3.0 supports:

1. **Declared goal seeds** from caller/product contracts.
2. **Inferred goal hypotheses** from labels, object/action structure, repeated transitions, and explicit outcome evidence.

A hypothesis can become highly ranked, but it remains inferred until a caller/product contract explicitly accepts it as a goal seed.

## Anti-feature-first diagnostics

Non-blocking discovery diagnostics include:

- goal label identical to a navigation noun with no action/outcome semantics;
- a goal decomposes only into surfaces instead of user tasks;
- a task has no object/action/outcome relationship;
- multiple candidate goals collapse to the same generic route with no distinct outcome evidence.

These diagnostics improve model quality. They do not create UX findings by themselves.

---

# 3. Discovery Evidence Packet

## Purpose

Provide a browser/provider-neutral input boundary for product-model and journey discovery.

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
- `surface_id`
- `action_evidence`
- `transition_evidence`
- `object_evidence`
- `state_evidence`
- `success_evidence`
- `evidence_refs`
- optional `runtime_v11` packet or normalized runtime-evidence metadata.

No Playwright page/browser/context object crosses the public UX boundary.

A caller may supply already-normalized captures for deterministic offline tests. When V11 data is supplied, v3 adapters must reuse V11 normalization and retain evidence refs for every extracted fact.

---

# 4. Autonomous Journey Discovery

## Purpose

Generate and rank candidate journeys so callers no longer need to manually author every possible `UXJourneySpec`.

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

A candidate is not a v2 journey contract until promotion succeeds.

## Step hypothesis

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

1. start from a declared goal or inferred goal hypothesis;
2. enumerate reachable action/state paths from the product graph;
3. stop at explicit outcome evidence, explicit dead-end, configured exploration depth, or repeated semantic state;
4. collapse exact duplicate normalized paths;
5. calculate selection scores;
6. retain evidence lineage for every candidate step.

Exploration depth is a computational safety control, not a UX click-count rule and never becomes a product-quality criterion.

## Candidate ranking

`discovery_score` decides what is worth inspecting first. It cannot create enforcement authority.

Initial normalized score components:

- `goal_confidence`
- `success_evidence_strength`
- `path_evidence_coverage`
- `critical_action_presence`
- `recovery_relevance`
- `novelty_against_verified_journeys`

The weight vector is versioned and exported by `v3_catalog.py`. No hidden weight may influence blocking authority.

## Stateless candidate querying

The core package does not create a mandatory candidate database.

`query_ux_journey_candidates(candidates, ...)` filters/sorts a caller-supplied candidate collection and returns defensive copies. Candidate persistence belongs to callers/artifacts until a future storage layer is explicitly designed.

---

# 5. Promotion to v2 Journey Contracts

`promote_ux_journey_candidate(candidate, product_model, goal_graph, ...)` returns either:

- a valid v2-compatible `UXJourneySpec`; or
- structured `promotion_gaps` explaining why authoritative promotion is not allowed.

## Minimum promotion requirements

1. the referenced goal node is `declared`;
2. every promoted step resolves to a declared or observed action/transition path;
3. at least one success criterion is declared or directly evidenced as an outcome linked to the declared goal;
4. every expected transition inserted into the spec has explicit evidence/provenance;
5. required/preserved context is inserted only when supported by object/state identity evidence;
6. recovery expectations are inserted only when declared or observed;
7. provenance resolves;
8. inferred-only semantic fields are never silently rewritten as declared/observed facts;
9. the resulting mapping passes the existing v2 `validate_ux_journey_spec` unchanged.

If requirements are incomplete, the candidate remains `hypothesis` or `promotable` with separate `promotion_gaps`; no undeclared status such as `promotable-with-gaps` exists.

A candidate may be marked `promotable` when all structural/evidence conditions are complete except explicit acceptance of an inferred goal. Acceptance converts that goal into a declared seed through caller/product provenance, after which promotion may produce the v2 spec.

---

# 6. Autonomous Exploration Planning

## Purpose

Let NUI decide which evidence should be collected next without becoming a second browser agent.

`plan_ux_discovery(candidate_or_graph, available_capabilities)` returns bounded **observation requests**, not execution claims.

Observation request fields:

- `request_id`
- `purpose`
- `target_surface_id`
- `target_action_id`
- `required_evidence_fields`
- `preferred_v11_capabilities`
- `priority`
- `because`

The planner may say “observe whether action A preserves object identity” but cannot claim that A was executed or that identity was preserved.

Architecture:

`V3 planner -> observation request -> V11 collector/executor -> normalized evidence -> V3 model/discovery -> V2 verifier`

No `V3 Playwright` layer is introduced.

---

# 7. Temporal UX Evidence Ledger

## Purpose

Preserve semantic UX evidence across revisions so NUI can detect regressions rather than only evaluate isolated runs.

## `UXEvidenceSnapshot`

Fields:

- `snapshot_id`
- `product_id`
- `revision`
- `journey_id`
- `journey_fingerprint`
- `verification_status`
- `step_results`
- `success_criteria_results`
- `findings`
- `finding_fingerprints`
- `runtime_evidence_refs`
- `provenance_ids`
- `created_from`

Snapshots are normalized immutable values. The core package exposes serialization-safe mappings but does not require a hosted database.

Callers may persist snapshots in files, CI artifacts, databases, or external stores.

## Stable fingerprints

Fingerprints are deterministic hashes over normalized semantic content, excluding timestamps, object addresses, and transient capture IDs.

- journey fingerprint: stable journey structure + product-local expectations;
- finding fingerprint: rule identity + step identity + normalized observed/expected semantic content;
- evidence refs remain separately preserved so equivalent findings can be compared even when capture IDs differ.

---

# 8. Semantic UX Regression Engine

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

## Regression authority

- A regression records that a previously evidenced semantic condition worsened.
- Missing candidate evidence is classified as evidence loss / insufficient evidence, not automatically as a proven UX failure.
- A blocking regression may inherit blocking authority only from the underlying existing verified UX rule/finding.
- Temporal comparison cannot escalate `warn` to `block` or create a new rule identity.
- DOM/visual difference alone is never sufficient proof of a semantic UX regression.

---

# 9. Impact Ranking

## Purpose

Prioritize already verified failures/regressions without changing UX truth or rule authority.

`rank_ux_impacts(...)` produces `UXImpactAssessment` records.

Initial components:

- `goal_criticality`
- `task_frequency`
- `completion_blockage`
- `recoverability_cost`
- `affected_scope`
- `regression_confidence`
- `evidence_completeness`

Each component contains:

- `value`
- `origin`
- `evidence_refs`

Assessment output:

- `status`: `ranked`, `provisional`, or `insufficient-evidence`
- `priority_score`
- `priority_band`: `p0`, `p1`, `p2`, `p3`, or `unknown`
- `confidence`
- `coverage`
- `components`
- `because`

Rules:

- declared/observed impact evidence may produce `ranked`;
- inferred components may produce only `provisional` ranking;
- missing required ranking evidence yields `insufficient-evidence` with `priority_band="unknown"` rather than invented numeric defaults;
- priority never mutates underlying `severity` or `enforcement`.

A P0 warning remains a warning. A P3 blocking finding remains blocking according to its rule authority.

---

# 10. Quality Court

## Product model

- unique/sorted semantic IDs;
- closed enums;
- all references resolve;
- confidence numeric, finite, non-bool, within `[0,1]`;
- observed/inferred records carry evidence;
- exact semantic duplicates are rejected or deterministically merged;
- normalization invents no product semantics.

## Goal graph

- unique nodes/edges;
- source/target resolution;
- allowed node/edge kinds;
- invalid self-decomposition rejected;
- intent nodes cannot be marked `observed` merely from browser traversal;
- inferred goal paths remain non-authoritative until explicitly accepted.

## Journey discovery

- deterministic candidate IDs/fingerprints;
- duplicate normalized paths collapsed;
- selection scores bounded/queryable;
- computational depth is not exposed as a UX quality rule;
- no rule/skill/journey count target;
- candidate persistence remains caller-owned.

## Promotion

- declared goal required for authoritative v2 contract;
- inferred-only required facts rejected;
- all promoted expectations have evidence/provenance;
- promoted spec passes existing v2 validation unchanged;
- promotion gaps are explicit and deterministic.

## Temporal evidence

- snapshots immutable after normalization;
- product/revision/journey identity required;
- stable fingerprints independent of timestamp ordering;
- incompatible product/journey comparisons rejected;
- evidence loss never becomes fabricated UX failure.

## Impact ranking

- priority and authority remain separate;
- missing impact evidence does not receive invented defaults;
- inferred impact signals lower ranking status to provisional;
- no ranking operation mutates rule severity/enforcement.

---

# 11. Package boundaries

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

V1/v2 production modules remain unchanged unless a verified compatibility issue requires a narrowly scoped fix.

---

# 12. Public Python API

Initial v3 surfaces:

- `validate_ux_product_model`
- `normalize_ux_product_model`
- `build_ux_product_model`
- `validate_ux_goal_graph`
- `build_ux_goal_graph`
- `discover_ux_journeys`
- `query_ux_journey_candidates`
- `promote_ux_journey_candidate`
- `plan_ux_discovery`
- `create_ux_evidence_snapshot`
- `compare_ux_snapshots`
- `rank_ux_impacts`
- `ux_v3_status`

Read/query functions return defensive copies. Bounded integer limits follow existing repository conventions: 1..100, rejecting `bool`.

---

# 13. MCP namespace

V3 MCP tools are read/build/plan/compare operations and do not mutate target products:

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

`nui_plan_ux_discovery` returns observation requests only. It does not click/type/navigate a live product.

---

# 14. V11 integration

V11 remains the only browser/runtime collection layer.

V3 consumes either:

1. provider-neutral normalized discovery captures; or
2. V11 packets through explicit evidence-preserving adapters.

Any v3 V11 adapter must reuse V11 normalization and expose evidence refs for every extracted semantic fact.

No Playwright-specific object enters the public `ux_intelligence` contracts.

---

# 15. V2 integration

V3 does not replace the v2 verifier.

The contract is:

1. discovery produces a candidate;
2. promotion either produces a valid v2 `UXJourneySpec` or explicit gaps;
3. existing `verify_ux_journey` evaluates the promoted journey;
4. verified output becomes a temporal snapshot;
5. regression compares snapshots;
6. impact ranking prioritizes verified findings/regressions.

This prevents discovery from becoming a second finding-authority system.

---

# 16. Testing strategy

Use standard-library `unittest` to match repository CI.

TDD sequence:

1. RED product-model contract tests;
2. RED goal-graph contract tests;
3. RED discovery candidate/authority tests;
4. RED promotion tests proving inferred-only facts cannot become authoritative v2 expectations;
5. RED planner tests proving requests are not execution claims;
6. RED temporal fingerprint/snapshot tests;
7. RED semantic regression tests;
8. RED impact tests proving priority cannot mutate severity/enforcement;
9. RED public API/MCP/status tests;
10. implementation in bounded layers;
11. focused v1+v2+v3 regression;
12. repository validator;
13. exact-head GitHub Actions Python 3.10/3.11/3.12 + Real Chromium + release gate.

Adversarial coverage includes:

- inferred goal with no declared acceptance;
- cyclic graph path;
- duplicate semantic actions with different IDs;
- success criterion guessed only from label text;
- promotion with missing object identity;
- snapshot comparison across different products;
- missing evidence incorrectly classified as failure;
- impact ranking attempting enforcement escalation;
- navigation noun incorrectly treated as declared user goal;
- observation request incorrectly treated as observed completion.

---

# 17. Initial acceptance scenarios

## A. Declared goal + observed path

Given a declared goal and V11-backed transitions, discovery yields a promotable candidate, promotion returns a valid v2 journey spec, and v2 verification can pass it with explicit evidence.

## B. Inferred-only goal

Given navigation labels and route structure but no accepted goal seed, discovery may rank a goal/journey hypothesis. Promotion must refuse authoritative v2 conversion and return a goal-acceptance gap.

## C. Context regression

Baseline preserves object identity across same-goal navigation; candidate revision changes identity. V2 emits the existing context-preservation finding and v3 classifies a semantic regression without inventing new rule authority.

## D. Evidence loss

Baseline PASS; later revision lacks required observation fields. V3 reports evidence loss / insufficient evidence, not a proven UX failure.

## E. Recovery regression

Baseline has verified accessible recovery; later revision proves the existing recovery rule failure. V3 classifies `recovery-path-lost` and preserves underlying rule severity/enforcement.

## F. Priority without authority escalation

A verified warning with strong criticality evidence may rank P0, but enforcement remains `warn`.

## G. Planner/runtime separation

Planner requests evidence for a candidate step. Until V11 returns a normalized observation, neither product state nor journey success may be marked observed.

---

# 18. Non-goals for v3.0

V3.0 explicitly does not:

- build a second browser automation stack;
- let NLP/LLM inference directly create blocking findings;
- infer user intent as observed truth from clicks alone;
- auto-promote inferred goals without explicit acceptance/provenance;
- replace v2 journey verification;
- merge UX findings into V13 authority;
- create rule/skill/journey count quotas;
- claim human usability evidence from browser telemetry alone;
- use pixel difference as sufficient UX-regression proof;
- automatically edit the target product;
- treat counterfactual repair suggestions as verified improvements;
- require a hosted evidence database;
- simulate unlimited personas;
- encode fixed click-count, memory-count, or friction folklore.

---

# 19. Success criteria

UX Intelligence v3.0 is complete only when:

1. a provider-neutral product model can be validated and built from bounded evidence;
2. semantic product records expose explicit origin/confidence/evidence lineage;
3. goal graph distinguishes declared user intent from inferred hypotheses and from surfaces/features;
4. autonomous discovery creates deterministic journey candidates from bounded graph evidence;
5. inferred-only facts remain hypotheses and cannot independently satisfy promotion requirements;
6. promotable candidates become valid v2 journey specs without weakening v2 validation;
7. discovery planning emits observation requests while runtime execution remains owned by V11;
8. verified v2 outputs become immutable deterministic evidence snapshots;
9. snapshot comparison detects semantic UX regressions and distinguishes evidence loss from proven failure;
10. impact ranking prioritizes verified failures/regressions without mutating severity/enforcement;
11. v1/v2 public behavior remains backward compatible;
12. repository validator is green;
13. exact-final-head Python 3.10/3.11/3.12, Real Chromium, and release-gate CI are green.
