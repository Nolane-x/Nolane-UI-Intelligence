---
name: designing-task-dependency-networks
description: Use when this specialist's decision ownership is materially in scope. Own project-work dependency creation and inspection, including blocker direction, lag, critical chains, cycles, and scheduling consequences.
---
# Designing Task Dependency Networks

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own dependencies between work items: predecessor/successor meaning, blocker direction, relationship type, optional lag, cycle prevention, critical-chain visibility, and the consequences for readiness or schedule. This differs from generic graph dependency exploration because the relationships directly govern project work progression.

## Inputs and evidence

Require supported dependency types, whether dependencies are hard or advisory, schedule fields, lag/lead support, status/readiness rules, cycle policy, hierarchy interaction, permissions, and expected dependency density. Determine whether external-project dependencies can be linked or only referenced.

## Procedure

Use language that states consequence—"B is blocked by A"—rather than ambiguous arrows alone. Creation should search and disambiguate work items before commit and prevent or explicitly handle cycles. Show dependencies near the item and in focused network/timeline views; do not force users into a graph for simple one-hop checks. When a predecessor completes, define whether readiness updates automatically or still requires manual criteria. Schedule shifts should preview downstream date effects instead of silently moving every successor. External dependencies need ownership and freshness cues even if they cannot be edited locally.

## Failure topology

Failures include reversed blocker interpretation, cycles introduced through bulk edits, hidden cross-project blockers, automatic date cascades that surprise owners, hierarchy links mistaken for dependencies, and completed predecessors falsely implying a successor is ready. Another failure is rendering all dependencies on a board at once, producing unusable line clutter.

## Falsification

Reject if users cannot state dependency direction from text alone; if a cycle can be saved without explicit policy; if shifting one task silently reschedules downstream commitments; if an external dependency can become stale with no cue; if hierarchy and dependency relationships are visually conflated; or if readiness derives from dependency completion when other required criteria remain unsatisfied.

## Output contract

Return a `task-dependency-networks-contract` with: relationship types; direction language; creation/edit protocol; cycle handling; hard/advisory semantics; lag model; readiness effect; focused visualization; schedule-impact preview; cross-project reference freshness; and bulk-edit safeguards. Include one cycle attempt and one downstream-date impact case.

## Handoffs

Use project hierarchy for parent/child structure, milestone tracking for checkpoint dependencies, roadmaps for strategic sequencing, and generic dependency graph exploration only for large network inspection mechanics.