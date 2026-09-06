# UX Intelligence v1 Design

## Goal

Add a first-class UX reasoning subsystem to Nolane UI Intelligence without turning contextual UX guidance into brittle checklist rules. The subsystem must strengthen anti-AI UI generation at the product/experience level, preserve the V13 evidence boundary, and scale toward roughly 1000 canonical skills and no more than roughly 1000 high-value operational rules without treating either count as a quality quota.

## Problem

NUI already has strong UI truth, runtime truth, interaction integrity, accessibility, convergence and domain-specialist coverage. Its weaker layer is end-to-end UX reasoning: user goals, task structure, mental models, information architecture, journey continuity, cognitive/friction cost, comprehension, recovery and evaluation.

A second scaling problem appears as the V13 leaf-rule catalog grows: different domain rules can remain textually distinct while sharing a deeper failure mechanism. Without a semantic family layer, the catalog can become operationally non-duplicative yet conceptually fragmented.

## Architectural decision

Introduce `src/nolane_ui/ux_intelligence/` as a backward-compatible subsystem with four explicit layers:

1. `mechanisms.py` — canonical UX failure mechanisms. Mechanisms are not rules and do not block by themselves.
2. `skills.py` — canonical UX cognitive-skill registry. Skills define reasoning capabilities, not policy claims.
3. `rules.py` — a deliberately small first wave of falsifiable UX operational rules. Every UX rule binds to exactly one mechanism and declares observable/falsifiable/repair/verification planes.
4. `catalog.py` — deterministic read-only APIs, status, mechanism coverage and rule/skill queries.

The subsystem is independent from the V13 canonical catalog in v1 so no existing V13 rule is forced to migrate. A future bridge may add optional `mechanism_id` metadata to V13 after empirical review. v1 therefore proves the ontology and API before mutating the mature V13 contract.

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

The first wave contains 32 skills across the eight domains. Count is descriptive; future skills are accepted only when they add a distinct reasoning operation.

## Mechanism model

Each mechanism contains:

- `mechanism_id`
- `title`
- `definition`
- `diagnostic_question`
- `signals`
- `non_examples`

Mechanisms are reusable semantic coordinates. Multiple leaf rules may map to one mechanism when their operational context is genuinely distinct.

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

## Determinism and quality gates

The subsystem must:

- sort all canonical outputs by stable IDs;
- reject duplicate mechanism, skill and rule IDs;
- reject unknown mechanism references;
- reject unknown owner skill references;
- reject missing operational planes;
- reject count-quota fields;
- keep contextual/convergence findings non-blocking;
- expose bounded query limits of 1..100;
- report mechanism coverage and orphan mechanisms deterministically.

## Public API

The module exports:

- `get_ux_mechanism`
- `query_ux_mechanisms`
- `get_ux_skill`
- `query_ux_skills`
- `get_ux_rule`
- `query_ux_rules`
- `ux_intelligence_status`

## Testing strategy

TDD is mandatory. Tests first assert missing imports/API, schema integrity, ontology references, non-quota behavior, non-blocking convergence/contextual rules, deterministic bounded queries, and exact first-wave inventory. After RED is observed, production modules are added until the focused suite is green. Existing V13 tests must remain untouched and CI must pass before merge.

## Non-goals

v1 does not modify V13 rule contracts, does not claim empirical usability superiority, does not impose hard UX heuristics, does not auto-generate hundreds of rules, and does not make UX mechanism membership itself an enforcement signal.
