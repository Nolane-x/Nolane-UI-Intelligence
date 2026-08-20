---
name: designing-backlog-grooming
description: Use when this specialist's decision ownership is materially in scope. Own prioritization and refinement of unscheduled work, including ordering confidence, readiness, decomposition, stale items, and promotion into planned execution.
---
# Designing Backlog Grooming

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the backlog as a decision surface for what is not yet committed to execution. Decide how priority, readiness, age, uncertainty, dependencies, sizing, and decomposition are surfaced; how items move into planned work; and how stale or duplicate items are resolved. A backlog is not merely a long task list and should not silently imply commitment.

## Inputs and evidence

Require intake sources, prioritization model, readiness criteria, planning cadence, item age distribution, estimation practices, dependency links, ownership expectations, duplicate rate, and promotion rules to sprint/milestone/queue. Identify whether priority is manual rank, scoring formula, service class, or product decision.

## Procedure

Separate priority from readiness: a high-value item may still be unready because acceptance criteria, dependencies, or ownership are missing. Provide a refinement queue based on concrete signals such as age, missing evidence, oversized scope, or approaching planning window. Bulk triage should support discard, merge, defer, assign owner, request detail, or move to a plan without requiring full item editing. Decomposition should preserve parent intent and links to children. When priority is formula-driven, show score factors and allow controlled overrides with rationale. Promotion into a sprint or milestone should verify capacity and unresolved blockers rather than treating drag as purely visual.

## Failure topology

Failures include a backlog becoming an unbounded graveyard, manual ordering mistaken for objective priority, ready and unready items mixed without cues, duplicates splitting discussion/evidence, old items resurfacing with stale assumptions, and bulk grooming that destroys context. Another failure is turning grooming into mandatory field completion for every low-value idea.

## Falsification

Reject if users cannot distinguish prioritized from merely recently edited items; if a stale item can be promoted with obsolete dependencies unnoticed; if duplicate merge loses comments/links; if decomposed children lose their original outcome context; if score overrides have no provenance; or if the backlog requires full specification before low-confidence ideas can be captured.

## Output contract

Return a `backlog-grooming-contract` containing: backlog membership rule; priority authority; readiness criteria; refinement signals; stale-item policy; duplicate/merge behavior; decomposition semantics; bulk triage actions; promotion gates; scoring transparency; and provenance for overrides. Include one unready-high-priority item and one stale-duplicate case.

## Handoffs

Use sprint planning or milestone tracking after promotion, effort estimation for sizing, dependency networks for blockers, and project templates only when repeatable intake structure is justified. Generic list sorting does not own backlog priority semantics.