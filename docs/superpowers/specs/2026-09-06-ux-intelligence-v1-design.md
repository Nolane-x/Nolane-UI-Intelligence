# UX Intelligence v1 Design

## Goal

Add a first-class UX reasoning subsystem to Nolane UI Intelligence without turning contextual UX guidance into brittle checklist rules. The subsystem must strengthen anti-AI UI generation at the product/experience level, preserve the V13 evidence boundary, and scale by semantic novelty rather than by a fixed skill or rule count.

## Problem

NUI already has strong UI truth, runtime truth, interaction integrity, accessibility, convergence and domain-specialist coverage. Its weaker layer is end-to-end UX reasoning: user goals, task structure, mental models, information architecture, journey continuity, cognitive/friction cost, comprehension, recovery and evaluation.

A second scaling problem appears as the V13 leaf-rule catalog grows: different domain rules can remain textually distinct while sharing a deeper failure mechanism. Without a semantic family layer, the catalog can become operationally non-duplicative yet conceptually fragmented.

## Architectural decision

Introduce `src/nolane_ui/ux_intelligence/` as a backward-compatible subsystem with four explicit layers:

1. `mechanisms.py` — canonical UX failure mechanisms. Mechanisms are not rules and do not block by themselves.
2. `skills.py` — canonical UX cognitive-skill registry. Skills define reasoning capabilities, not policy claims.
3. `rules.py` — a deliberately small first wave of falsifiable UX operational rules. Every UX rule binds to exactly one mechanism and declares observable/falsifiable/repair/verification planes.
4. `catalog.py` — deterministic read-only APIs, status, mechanism coverage, semantic-owner integrity, operational-signature uniqueness and rule/skill queries.

The subsystem is independent from the V13 canonical catalog in v1 so no existing V13 rule is forced to migrate. A future bridge may add optional mechanism-family metadata to V13 after empirical review. v1 therefore proves the ontology and integration boundary before mutating the mature V13 contract.

The public boundary is intentionally explicit: `nolane_ui` re-exports the UX read API for normal Python consumers, while MCP exposes a distinct UX namespace. UX tooling must never silently masquerade as V13 canonical-rule authority.

## UX ontology

The first version covers eight UX cognition domains:

- goal-task
- mental-model
- information-architecture
- journey-flow
- cognitive-friction
- comprehension
- recovery
- evaluation

Mechanisms are cross-domain primitives such as `context-loss`, `goal-displacement`, `mental-model-mismatch`, `navigation-disorientation`, `decision-overload`, `ambiguous-consequence`, `false-completion`, `unrecoverable-progress-loss`, `cross-step-inconsistency`, `unnecessary-recall`, `workflow-fragmentation`, `hidden-dependency`, `premature-commitment` and `state-without-explanation`.

## Anti-AI UX convergence

UX Intelligence must challenge latent product templates, not only visual templates. Typical convergence evidence includes feature-first information architecture, dashboards without a recurring user question, generic sidebar/card/tab shells that do not match domain tasks, onboarding that describes features rather than first value, and workflows mirroring database entities instead of user mental models.

These findings remain contextual/review-oriented unless the failure is operationally falsifiable. UX Intelligence must not encode folklore such as fixed click-count limits, universal progressive disclosure, or generic “less friction is better” claims.

## Skill model

Each UX skill record contains:

- `skill_id`
- `domain`
- `title`
- `purpose`
- `questions`
- `outputs`
- `anti_patterns`
- `related_mechanisms`

The first wave contains 32 registry entries across the eight domains. This count is descriptive. A future skill belongs only when it adds a distinct reasoning operation; registry size itself is never quality evidence. v1 registry entries are not automatically canonical `skills/<slug>/SKILL.md` owners.

## Mechanism model

Each mechanism contains:

- `mechanism_id`
- `title`
- `definition`
- `diagnostic_question`
- `signals`
- `non_examples`

Mechanisms are reusable semantic coordinates. Multiple leaf rules may map to one mechanism when their operational context is genuinely distinct. Mechanism membership alone never produces a finding and never grants blocking authority.

## Rule model

Each UX rule contains:

- `rule_id`
- `domain`
- `mechanism_id`
- `class`
- `severity`
- `enforcement`
- `title`
- `statement`
- `applies_when`
- `failure_modes`
- `user_impacts`
- `observables`
- `falsifiers`
- `repairs`
- `verification`
- `owner_skill_ids`
- `status`

The first wave contains 16 rules focused on high-confidence failures: progress loss, task-context loss, hidden destructive consequence, false completion, dead-end recovery, cross-step contradiction, navigation identity loss, stale task context, repeated input without semantic reason, inaccessible recovery, hidden scope change and interruption recovery.

Rules in `contextual` or `convergence` classes never block. Blocking is reserved for clearly mechanical/behavioral loss or deception with directly reproducible consequences.

`owner_skill_ids` is not merely referential metadata. Every rule must have at least one declared cognitive owner whose `related_mechanisms` includes the rule's `mechanism_id`; an existing-but-semantically-unrelated skill cannot satisfy ownership integrity.

## Semantic quality court

UX v1 rejects exact operational duplication independently of rule IDs. For each rule, the court normalizes case and whitespace in the `(failure_modes, repairs, verification)` planes and rejects a second rule with the same normalized operational signature. This catches ID-renamed clones while deliberately avoiding fuzzy similarity at v1, so legitimate near-neighbor rules can remain distinct when their failure/repair/verification semantics differ.

For example, “a recoverable failure has a viable recovery path” and “that recovery path is actually reachable by the affected user from the failure state” are related but distinct claims; the court must not collapse them simply because both belong to recovery and workflow-fragmentation.

## Determinism and quality gates

The subsystem must:

- sort all canonical outputs by stable IDs;
- reject duplicate mechanism, skill and rule IDs;
- reject unknown mechanism references;
- reject unknown owner skill references;
- require at least one mechanism-compatible owner skill for every rule;
- reject duplicate normalized failure/repair/verification operational signatures;
- reject missing operational planes;
- reject count-quota fields;
- keep contextual/convergence findings non-blocking;
- expose bounded query limits of 1..100;
- report mechanism coverage and orphan mechanisms deterministically;
- remain read-only through its public/MCP query surfaces;
- preserve a distinct authority namespace from the V13 rule catalog.

## Public Python API

The package and top-level `nolane_ui` surface expose the three registries plus:

- `get_ux_mechanism`
- `query_ux_mechanisms`
- `get_ux_skill`
- `query_ux_skills`
- `get_ux_rule`
- `query_ux_rules`
- `ux_intelligence_status`

## MCP API

MCP exposes read-only bounded tools under a separate UX namespace:

- `nui_ux_status`
- `nui_get_ux_mechanism`
- `nui_query_ux_mechanisms`
- `nui_get_ux_skill`
- `nui_query_ux_skills`
- `nui_get_ux_rule`
- `nui_query_ux_rules`

These tools do not mutate rules, write product state, escalate permissions, or upgrade UX reasoning into V13 authority.

## Testing strategy

TDD is mandatory. Tests first assert missing imports/API, schema integrity, ontology references, non-quota behavior, non-blocking convergence/contextual rules, deterministic bounded queries, exact first-wave inventory, top-level exposure, MCP separation, semantic-owner compatibility and duplicate operational-signature rejection. The repository's actual test runner is `PYTHONPATH=src python -m unittest discover -s tests -v`, exercised in GitHub Actions across Python 3.10/3.11/3.12 plus the independent real Chromium smoke gate.

RED evidence must fail for the intended missing behavior before production integration is added. GREEN evidence must come from the latest feature head; an earlier successful run cannot certify later changes. Existing V13 tests remain untouched.

The semantic court is itself mutation-tested in unit tests: a rule whose owner skill exists but does not cover its mechanism must fail validation, and an ID-renamed clone with the same normalized operational signature must fail validation. These tests were observed RED before the court implementation was added.

## Non-goals

v1 does not modify V13 rule contracts, does not claim empirical usability superiority, does not impose hard UX folklore, does not auto-generate hundreds of rules, does not make mechanism membership itself an enforcement signal, does not use fuzzy similarity as an automatic UX blocking authority, and does not silently convert the 32 cognitive registry entries into canonical skill-graph nodes.
