---
name: documenting-design-decisions
description: Use when a durable UI architecture, interaction, accessibility, platform, design-system, or high-risk choice needs its rationale, evidence, alternatives, consequences, and future reversal conditions preserved for other teams or agents.
---

# Documenting Design Decisions

## Overview
A design decision record preserves why a choice exists so future agents can distinguish a constraint from an accident. Record enough evidence and reversal conditions to support evolution without freezing taste forever.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require an actual decision with alternatives or material consequence. Do not create records for every pixel value; routine implementation belongs in tokens/components/docs.

## Decision Model
Capture the problem before the chosen solution. State users/tasks, constraints, authority sources, evidence, and what would go wrong if left unresolved. List serious alternatives and why they were rejected *in this context*. Avoid strawman alternatives.

The decision includes scope and invariants: what it governs and what remains free. “Use side navigation” might be scoped to expert desktop workspace above a certain information depth, not all company products. Record downstream consequences: components required, accessibility behavior, migration, performance, analytics/research, and maintenance cost.

Every record has confidence and expiry/review triggers. Evidence can become stale; platform conventions change; product workflows evolve. Reversal triggers are concrete: task model changes, adoption data shows excessive navigation cost, new standard invalidates behavior, device mix changes, or a planned migration completes.

Link decisions to artifacts and tests. If a component exists because of a decision, its API and eval should reference the record. When a decision is superseded, preserve history and state what replaced it rather than editing old rationale into hindsight.

## Evidence
A record cites authoritative sources, research findings, metrics, prototypes, audit findings, or domain constraints actually used. “Best practice” with no source or task rationale is weak evidence. For aesthetic direction, accepted creative intent may be valid evidence but must not masquerade as usability proof.

## Output Contract
Return a `design-decision-record` with `decision_id`, `status`, `problem`, `scope`, `users_tasks`, `constraints[]`, `evidence_refs[]`, `alternatives[]`, `decision`, `invariants[]`, `consequences[]`, `confidence`, `review_or_expiry`, `reversal_triggers[]`, and `linked_artifacts[]`.

## Failure Traps
- Recording only “we chose X.”
- Rejected alternatives described unfairly.
- No scope, causing local decision to become global dogma.
- No expiry/reversal condition.
- Aesthetic preference documented as empirical proof.
- Updating old record instead of superseding it.
- Record with no connection to implementation or eval.

Good decision history increases future freedom because teams know what can safely change.

## V6 Decision Memory Protocol
Store a **decision rationale capsule**: decision, problem, constraints, chosen mechanism, evidence, and expected consequence. Maintain a **rejected-alternative ledger** with the reason each serious alternative lost so future agents do not repeat the same exploration or mistake rejection for universal invalidity.

Assign **assumption expiry** to facts likely to drift—platform APIs, library versions, user behavior, business policy, regulation, content volume. Define a **decision reversal trigger** specifying what new evidence or condition should reopen the decision. Write for a **maintenance audience** that did not attend the original conversation: exact artifacts, owners, boundaries, and migration consequences.

### Falsification
Remove the author/context and ask another agent to reproduce why the decision was made and when to revisit it. If they cannot, documentation is not operational.

### Recovery
Reconstruct from source/evidence, mark unknown rationale honestly, and supersede—not silently edit—historical decisions when the product changes.
