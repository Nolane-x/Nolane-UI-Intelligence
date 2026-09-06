# UX Intelligence v2 Design

## Status

Approved architectural direction: layered end-to-end UX intelligence.

## Goal

Make NUI capable not only of describing UX reasoning, but of executing that reasoning as canonical agent skills, binding it to explicit evidence/provenance, evaluating critical user journeys against real browser observations, and returning UX findings whose authority boundaries are unambiguous.

The v2 pipeline is:

`canonical UX skills -> provenance/evidence boundary -> journey semantics -> V11 runtime observations -> verified UX findings`

V2 does **not** turn all UX registry entries into canonical skills, does **not** create rule quotas, and does **not** merge UX findings into V13 canonical rule authority.

## Design principles

1. **Semantic novelty over count.** New skills, rules, mechanisms, or provenance records exist only when they add a distinct reasoning or verification capability.
2. **Selective canonicalization.** The 32 v1 UX registry entries remain a reasoning registry. Only entries that are sufficiently distinct, reusable, and operational become canonical `skills/<slug>/SKILL.md` nodes.
3. **Evidence before authority.** A UX finding must expose what was observed, what expectation it was compared with, what rule/mechanism explains the failure, and what verification mode supports the conclusion.
4. **Runtime reuse, not duplication.** Browser collection remains owned by V11 runtime. UX v2 consumes provider-neutral runtime observations rather than implementing another browser stack.
5. **Journey semantics are explicit.** V2 models user goals, journey steps, expected transitions, state preservation, recovery expectations, and success criteria as structured data rather than prose-only heuristics.
6. **UX and V13 remain different authority domains.** UX findings can reference V13 evidence and product state, but UX MCP/Python surfaces remain namespaced and cannot masquerade as V13 canonical rules.
7. **No folklore enforcement.** V2 does not encode fixed click counts, arbitrary memory limits, or unconditional friction minimization.
8. **Deterministic quality court first.** Structural and exact semantic-contract checks can block invalid catalog content. Fuzzy similarity remains advisory only.

## Scope

V2 contains four deliverables that form one testable end-to-end subsystem:

1. selective canonical UX skill bridge;
2. UX provenance/evidence ledger;
3. journey semantics and verification engine;
4. public Python/MCP surfaces for journey verification and evidence inspection.

## 1. Selective canonical UX skill bridge

### Purpose

The v1 `UX_SKILLS` registry describes 32 cognitive capabilities but does not make them canonical agent skill nodes. V2 introduces an explicit bridge from selected registry entries to canonical `skills/<slug>/SKILL.md` nodes.

### Initial canonical skill set

The initial bridge should remain deliberately small and cover the end-to-end reasoning loop:

- `identifying-user-goals`
- `mapping-critical-user-journeys`
- `conducting-cognitive-walkthroughs`
- `testing-mental-model-alignment`
- `assessing-recovery-completeness`
- `evaluating-task-success`

These six form a coherent chain from intent -> journey -> walkthrough -> conceptual fit -> failure recovery -> outcome evaluation. They are descriptive seed choices, not a target count or quota.

### Canonical bridge contract

Add a package-level mapping that records, for each promoted entry:

- `skill_id`
- `canonical_slug`
- `canonical_path`
- `reason_for_canonicalization`
- `required_outputs`
- `supported_mechanisms`
- `verification_dependencies`

Validation must ensure:

- every `skill_id` exists in `UX_SKILLS`;
- every canonical path exists;
- each skill document declares the same identity and purpose as the registry entry;
- required outputs are non-empty and operational;
- supported mechanisms are a subset of the registry entry's `related_mechanisms`;
- no registry entry is silently promoted without an explicit bridge record.

The bridge is read-only metadata. It does not rewrite the canonical skill graph at runtime.

## 2. UX provenance and evidence boundary

### Problem

V1 rules identify mechanisms and owners but do not have a UX-specific evidence ledger describing why a reasoning pattern or verification expectation is trusted, what its transfer boundary is, or what contraindications apply.

### Provenance record

Introduce immutable UX provenance records with fields:

- `provenance_id`
- `title`
- `source_kind`
- `source_reference`
- `claim`
- `supports`
- `transfer_boundaries`
- `contraindications`
- `verification_modes`
- `status`

`source_kind` is constrained to evidence categories such as `internal-empirical`, `runtime-observation`, `standards`, `research`, `product-contract`, and `expert-review`.

A provenance record never proves a rule universally. It documents the bounded basis for a mechanism, journey expectation, or verification method.

### Binding

Rules and journey expectations may reference `provenance_ids`. Validation requires references to resolve, but v2 does not require every v1 rule to gain provenance immediately. New journey verifier contracts introduced by v2 must have provenance or a declared `product-contract` basis.

## 3. Journey semantics

### Journey model

Introduce a structured `UXJourneySpec` represented as immutable mappings/tuples to match the existing package style.

Required fields:

- `journey_id`
- `title`
- `user_goal`
- `entry_state`
- `steps`
- `success_criteria`
- `critical_state`
- `provenance_ids`
- `status`

Each step includes:

- `step_id`
- `intent`
- `action`
- `expected_transition`
- `required_context`
- `preserved_context`
- `allowed_detours`
- `recovery_expectation`
- `evidence_requirements`

### Runtime observation adapter

The verifier consumes V11 provider-neutral observation packets. V2 must not depend on Playwright-specific types.

The adapter normalizes only the UX-relevant observation plane:

- current location/route;
- visible text and actionable labels;
- DOM/runtime state that V11 already exposes;
- interaction outcome;
- object identity/context markers;
- error/recovery affordances;
- completion/success evidence.

If an evidence requirement cannot be observed with the supplied packet, the verifier emits `insufficient-evidence`, not a failure finding.

## 4. Journey verification engine

### Input

`verify_ux_journey(journey, observations, *, rule_catalog=UX_RULES, provenance_catalog=UX_PROVENANCE)`

### Output

Return a deterministic report with:

- `journey_id`
- `status`
- `step_results`
- `findings`
- `evidence_gaps`
- `success_criteria_results`
- `provenance_ids`

Step result states:

- `pass`
- `fail`
- `insufficient-evidence`
- `not-executed`

Journey status is derived, never manually supplied:

- `failed` if any critical required step fails;
- `insufficient-evidence` if no failure is proven but required evidence is missing;
- `passed` only when all required critical checks and success criteria pass.

### Finding contract

A UX finding contains:

- `finding_id`
- `journey_id`
- `step_id`
- `rule_id`
- `mechanism_id`
- `summary`
- `observed`
- `expected`
- `evidence_refs`
- `provenance_ids`
- `severity`
- `enforcement`
- `verification_mode`

A finding can only reference an existing UX rule and must inherit its mechanism/severity/enforcement rather than redefining authority ad hoc.

### Rule matching

V2 should begin with explicit deterministic evaluators for high-value journey failures rather than a generic NLP matcher. Initial evaluators should cover:

- hidden dependency before commit;
- premature commitment;
- same-goal navigation losing context;
- cross-step contradiction;
- interruption losing resumable context;
- stale task context not revalidated;
- false completion;
- dead-end without recovery;
- recovery path unreachable;
- silent progress destruction.

Each evaluator declares:

- which rule it implements;
- required evidence fields;
- pass/fail/insufficient-evidence logic;
- the expected transition semantics it consumes.

This keeps the runtime proof surface auditable and testable.

## 5. Quality court

V2 catalog validation adds deterministic checks for:

- canonical skill bridge resolution and identity consistency;
- provenance ID uniqueness and reference resolution;
- journey ID/step ID uniqueness;
- required critical state and success criteria;
- rule evaluator -> UX rule resolution;
- evaluator required evidence declarations;
- finding rule/mechanism inheritance;
- no blocking authority from contextual/convergence classes;
- no quota fields;
- canonical sorting where catalogs are exposed publicly.

Exact operational-signature duplicate detection from v1 remains in force. Fuzzy similarity may generate review diagnostics later, but cannot automatically reject content in v2.

## 6. Public Python API

Add namespaced exports without removing v1 APIs:

- `UX_CANONICAL_SKILL_BRIDGE`
- `UX_PROVENANCE`
- `UX_JOURNEY_EVALUATORS`
- `get_ux_provenance`
- `query_ux_provenance`
- `get_ux_canonical_skill_bridge`
- `query_ux_canonical_skill_bridge`
- `validate_ux_journey_spec`
- `verify_ux_journey`
- `ux_v2_status`

All getters/queries return defensive copies. Query limits remain bounded to 1..100.

## 7. MCP namespace

Add read/verify tools under the existing UX namespace:

- `nui_ux_v2_status`
- `nui_get_ux_provenance`
- `nui_query_ux_provenance`
- `nui_get_ux_canonical_skill_bridge`
- `nui_query_ux_canonical_skill_bridge`
- `nui_verify_ux_journey`

`nui_verify_ux_journey` accepts a structured journey specification plus provider-neutral observation packet and returns the deterministic verification report.

No UX tool mutates V13 rule state or product evidence state.

## 8. Files and boundaries

New package files:

- `src/nolane_ui/ux_intelligence/provenance.py`
- `src/nolane_ui/ux_intelligence/canonical_bridge.py`
- `src/nolane_ui/ux_intelligence/journeys.py`
- `src/nolane_ui/ux_intelligence/evaluators.py`
- `src/nolane_ui/ux_intelligence/verifier.py`

Modified files:

- `src/nolane_ui/ux_intelligence/catalog.py`
- `src/nolane_ui/ux_intelligence/__init__.py`
- `src/nolane_ui/__init__.py`
- `src/nolane_ui/mcp_server.py`

Canonical skill nodes added under:

- `skills/identifying-user-goals/SKILL.md`
- `skills/mapping-critical-user-journeys/SKILL.md`
- `skills/conducting-cognitive-walkthroughs/SKILL.md`
- `skills/testing-mental-model-alignment/SKILL.md`
- `skills/assessing-recovery-completeness/SKILL.md`
- `skills/evaluating-task-success/SKILL.md`

Tests:

- `tests/test_ux_intelligence_v2_bridge.py`
- `tests/test_ux_intelligence_v2_provenance.py`
- `tests/test_ux_intelligence_v2_journeys.py`
- `tests/test_ux_intelligence_v2_verifier.py`
- `tests/test_ux_intelligence_v2_api_mcp.py`

## 9. Testing strategy

Use standard-library `unittest`, matching repository CI.

TDD sequence:

1. bridge tests RED before canonical bridge/skill nodes exist;
2. provenance tests RED before ledger exists;
3. journey-spec validation tests RED before model/validator exists;
4. evaluator/verifier tests RED before runtime verification exists;
5. public API/MCP tests RED before exports/tools exist;
6. focused v1+v2 regression suite GREEN;
7. full repository suite GREEN in official GitHub Actions, including the dedicated real Chromium job and current-head release gate.

Tests must include negative cases for unresolved skill/provenance/rule IDs, incompatible mechanism ownership, duplicate journey steps, missing evidence, false completion, lost context, dead-end recovery, and a complete passing journey.

## 10. Non-goals

V2 explicitly does not:

- create a second browser/runtime stack;
- promote all 32 registry entries into canonical skill nodes;
- create UX rule count targets;
- automatically block fuzzy near-duplicates;
- claim universal empirical superiority;
- rewrite or merge V13 canonical-rule authority;
- infer failures from missing evidence;
- treat lower friction as universally better;
- encode arbitrary click-count or memory-count folklore.

## 11. Success criteria

V2 is complete only when all of the following are true:

1. selected UX reasoning capabilities exist as validated canonical `SKILL.md` nodes;
2. every bridge record resolves and agrees with its registry source;
3. UX provenance is queryable and transfer-bounded;
4. a structured journey can be validated independently of browser execution;
5. V11-compatible observations can be verified against journey expectations;
6. missing evidence produces `insufficient-evidence`, never fabricated failure;
7. verified findings inherit existing UX rule authority exactly;
8. Python and MCP surfaces expose the complete v2 read/verify API;
9. v1 behavior remains backward compatible;
10. final-head GitHub Actions core, real-browser, and release-gate jobs are green.
