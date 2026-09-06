# UX Intelligence v2 Design

## Status

Approved architectural direction: layered end-to-end UX intelligence.

## Goal

Make NUI capable not only of describing UX reasoning, but of binding fine-grained UX cognition to canonical agent execution skills, explicit provenance, structured user journeys, provider-neutral runtime observations, and evidence-bounded UX findings.

The v2 pipeline is:

`UX cognition -> canonical skill bridge -> provenance/evidence boundary -> journey semantics -> V11-compatible runtime observations -> verified UX findings`

V2 does **not** create UX rule/skill quotas, duplicate the browser runtime, or merge UX findings into V13 canonical-rule authority.

## Design principles

1. **Semantic novelty over count.** New skills, rules, mechanisms, evaluators, or provenance records exist only when they add a distinct capability.
2. **Bridge before duplication.** The 32 v1 `UX_SKILLS` entries remain fine-grained reasoning operations. When an existing canonical NUI skill can execute that operation without distortion, v2 binds to that node instead of minting a duplicate `SKILL.md`.
3. **New canonical nodes require a semantic gap.** A new skill-graph node is justified only when no existing canonical skill can own the reasoning procedure, required output, and evidence discipline.
4. **Evidence before authority.** A finding exposes what was observed, what was expected, the UX rule/mechanism that explains the proven failure, and the verification/provenance basis.
5. **Runtime reuse, not duplication.** Browser collection remains owned by V11. UX v2 consumes provider-neutral mappings and never imports Playwright-specific objects into the verifier boundary.
6. **Missing evidence is not failure.** An activated check lacking required evidence yields `insufficient-evidence`.
7. **UX and V13 remain separate authority domains.** UX findings inherit UX-rule authority only and cannot masquerade as V13 canonical-rule findings.
8. **No folklore enforcement.** V2 does not encode fixed click counts, arbitrary memory limits, or unconditional friction minimization.
9. **Deterministic quality court first.** Structural and exact semantic-contract checks may block invalid catalog content. Fuzzy similarity is non-blocking.

## Scope

V2 contains four coupled deliverables:

1. selective UX-cognition -> canonical-skill bridge;
2. UX provenance/evidence ledger;
3. structured journey semantics plus deterministic rule evaluators/verifier;
4. namespaced Python/MCP read-and-verify surfaces.

## 1. Selective canonical skill bridge

### Purpose

The v1 `UX_SKILLS` registry describes 32 cognitive operations, while `skills/skill-graph.json` already contains broad canonical execution skills. V2 makes the relationship explicit without duplicating the graph.

### Initial bridge

The initial bridge is deliberately small and end-to-end. The selected count is descriptive, not a target:

| UX cognition | Existing canonical skill |
| --- | --- |
| `identifying-user-goals` | `modeling-users-and-tasks` |
| `mapping-critical-user-journeys` | `designing-task-flows` |
| `conducting-cognitive-walkthroughs` | `critiquing-user-experience` |
| `testing-mental-model-alignment` | `critiquing-user-experience` |
| `assessing-recovery-completeness` | `critiquing-user-experience` |
| `evaluating-task-success` | `evaluating-usability-evidence` |

These bindings form intent -> journey -> walkthrough/model check -> recovery -> outcome evidence without adding synonymous canonical nodes.

### Bridge record

Each explicit bridge record contains:

- `skill_id`
- `canonical_slug`
- `canonical_path`
- `reason_for_canonicalization`
- `required_outputs`
- `supported_mechanisms`
- `verification_dependencies`

Package validation requires the UX `skill_id` to resolve, record IDs to be unique/sorted, operational fields to be non-empty, and `supported_mechanisms` to be a subset of the source UX registry entry's `related_mechanisms`.

A checkout-level integration test additionally proves that every `canonical_slug` exists in `skills/skill-graph.json`, every `canonical_path` exists, and the target `SKILL.md` declares the same canonical name. Package import remains independent of repository-root filesystem layout.

The bridge is read-only metadata. It never rewrites the canonical graph at runtime.

## 2. UX provenance and evidence boundary

### Problem

V1 rules identify mechanisms and cognitive owners but do not describe the bounded basis for journey expectations or runtime verification.

### Provenance record

V2 adds immutable records with:

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

Allowed source kinds include `internal-empirical`, `runtime-observation`, `standards`, `research`, `product-contract`, and `expert-review`.

The initial ledger contains only evidence needed by the v2 verifier:

- declared product journey contract;
- UX-rule authority inheritance;
- V11 provider-neutral runtime observation boundary.

A provenance record documents a bounded basis; it does not prove a universal UX law.

## 3. Journey semantics

A `UXJourneySpec` is a structured mapping with:

- `journey_id`
- `title`
- `user_goal`
- `entry_state`
- `steps`
- `success_criteria`
- `critical_state`
- `provenance_ids`
- `status`

Each step contains:

- `step_id`
- `intent`
- `action`
- `expected_transition`
- `required_context`
- `preserved_context`
- `allowed_detours`
- `recovery_expectation`
- `evidence_requirements`

Validation is independent of browser execution. Normalization may canonicalize containers and make defensive copies but cannot invent transitions, evidence, or recovery semantics.

The verifier accepts provider-neutral observation mappings containing step-scoped route/state/context/interaction/recovery/completion evidence. If a required field is unavailable, the result is an evidence gap rather than a fabricated finding.

## 4. Deterministic evaluator registry

V2 begins with explicit evaluators for ten high-value v1 rules:

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

- `evaluator_id`
- existing `rule_id`
- activation evidence;
- required evidence;
- verification mode;
- provenance IDs.

An evaluator returns `not-executed` if its activation evidence is absent, `insufficient-evidence` when activated but incomplete, and only returns `fail` when a deterministic predicate proves the rule-specific failure.

There is no fuzzy/NLP rule matcher in the blocking path.

## 5. Journey verifier

### Input

`verify_ux_journey(journey, observations, *, rule_catalog=UX_RULES, provenance_catalog=UX_PROVENANCE)`

### Output

- `journey_id`
- derived `status`
- `step_results`
- `findings`
- `evidence_gaps`
- `success_criteria_results`
- `provenance_ids`

Step states are `pass`, `fail`, `insufficient-evidence`, or `not-executed`.

Journey status is derived:

- `failed` if a step or required success criterion is proven to fail;
- `insufficient-evidence` if no failure is proven but required execution/evidence is missing;
- `passed` only when all required checks and success criteria are evidenced as passing.

Expected-transition mismatch may fail the product-local journey contract without synthesizing a UX rule finding. A UX finding is emitted only when an existing UX rule is proven.

### Finding contract

A UX finding contains:

- `finding_id`
- `journey_id`
- `step_id`
- `rule_id`
- inherited `mechanism_id`
- `summary`
- `observed`
- `expected`
- `evidence_refs`
- `provenance_ids`
- inherited `severity`
- inherited `enforcement`
- `verification_mode`

Mechanism, severity, and enforcement come from the referenced UX rule. Evaluators cannot redefine authority.

## 6. Quality court

V2 deterministic validation covers:

- bridge ID uniqueness, sorting, UX-skill resolution, and mechanism compatibility;
- checkout-level canonical graph/path resolution;
- provenance ID uniqueness, allowed source/status values, transfer boundaries and contraindications;
- journey/step shape, duplicate step IDs, success criteria, critical state, and provenance resolution;
- evaluator -> existing UX rule resolution;
- evaluator activation/required evidence contracts and provenance resolution;
- contextual/convergence rules cannot gain blocking authority;
- no count-quota fields in v2 catalogs;
- v1 exact operational-signature duplicate detection remains untouched.

Fuzzy similarity may support later review diagnostics but cannot automatically reject content in v2.

## 7. Public Python API

V2 adds, without removing v1 APIs:

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

Read/query surfaces use defensive copies; bounded queries accept integer limits 1..100 and reject `bool`.

## 8. MCP namespace

Read/verify tools remain in the UX namespace:

- `nui_ux_v2_status`
- `nui_get_ux_provenance`
- `nui_query_ux_provenance`
- `nui_get_ux_canonical_skill_bridge`
- `nui_query_ux_canonical_skill_bridge`
- `nui_verify_ux_journey`

No v2 MCP surface mutates the canonical skill graph, V13 rules, or product evidence state.

## 9. Files and boundaries

New package files:

- `src/nolane_ui/ux_intelligence/canonical_bridge.py`
- `src/nolane_ui/ux_intelligence/provenance.py`
- `src/nolane_ui/ux_intelligence/journeys.py`
- `src/nolane_ui/ux_intelligence/evaluators.py`
- `src/nolane_ui/ux_intelligence/verifier.py`
- `src/nolane_ui/ux_intelligence/v2_catalog.py`

Modified integration files:

- `src/nolane_ui/ux_intelligence/__init__.py`
- `src/nolane_ui/__init__.py`
- `src/nolane_ui/mcp_server.py`

V1 `mechanisms.py`, `skills.py`, `rules.py`, and `catalog.py` remain unchanged in v2 unless a verified regression requires a compatibility fix.

No new canonical `SKILL.md` node is part of v2 because the selected cognition operations resolve to existing graph nodes.

Tests:

- `tests/test_ux_intelligence_v2_bridge.py`
- `tests/test_ux_intelligence_v2_provenance.py`
- `tests/test_ux_intelligence_v2_journeys.py`
- `tests/test_ux_intelligence_v2_verifier.py`
- `tests/test_ux_intelligence_v2_api_mcp.py`
- `tests/test_ux_intelligence_v2_quality_court.py`
- `tests/test_ux_intelligence_v2_status.py`

## 10. Testing strategy

Use standard-library `unittest` to match repository CI.

TDD sequence:

1. contract tests were committed before production v2 modules and captured by pull-request run #1248;
2. bridge/provenance/journey/evaluator/verifier/public integration are implemented on the same draft PR;
3. focused v1+v2 regression suite must be green;
4. full official GitHub Actions must be green on the final feature head, including Python 3.10/3.11/3.12, dedicated Real Chromium runtime, and current-head release gate.

Negative coverage includes unresolved bridge/provenance/rule references, unsupported mechanisms, duplicate journey steps, missing evidence, false completion, and authority-boundary violations.

## 11. Non-goals

V2 explicitly does not:

- create a second browser/runtime stack;
- duplicate existing canonical skills merely to mirror UX registry names;
- promote all 32 registry entries;
- create rule/skill count targets;
- automatically block fuzzy near-duplicates;
- claim universal empirical superiority;
- rewrite or merge V13 canonical-rule authority;
- infer failure from missing evidence;
- treat lower friction as universally better;
- encode arbitrary click-count or memory-count folklore.

## 12. Success criteria

V2 is complete only when:

1. selected UX cognition records resolve to validated existing canonical skill nodes and paths;
2. bridge records agree with source registry mechanism coverage and expose operational outputs/dependencies;
3. UX provenance is queryable and transfer-bounded;
4. a structured journey validates independently of browser execution;
5. V11-compatible observations can be checked without Playwright-specific coupling;
6. missing evidence produces `insufficient-evidence`, never a fabricated failure;
7. emitted findings inherit existing UX rule authority exactly;
8. Python and MCP surfaces expose the complete v2 read/verify API;
9. v1 behavior remains backward compatible;
10. final-head GitHub Actions core, real-browser, and release-gate jobs are green.
