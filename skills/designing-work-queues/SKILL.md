---
name: designing-work-queues
description: Use when a team processes a bounded or continuously replenished backlog and the interface must expose ordering, claim/assignment, eligibility, concurrency, throughput and queue scope without confusing priority with arrival order.
---

# Designing Work Queues

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns queue semantics for work awaiting processing. It does not own inbox attention state, triage classification or assignment administration across the whole organization.

## Decision Boundary
A work queue has an **eligibility set and an ordering policy**. Define both explicitly. Items may be ordered FIFO, priority, due time, severity, service tier, dependency, fairness policy or a computed score. If the order is algorithmic, show enough rationale to support operator trust without exposing irrelevant internals. Do not label a list “priority queue” when it is simply newest first.

Clarify acquisition model: agents may pull next work, claim a specific item, receive push assignment, or operate on preassigned queues. Claiming needs concurrency control. Two operators viewing the same unclaimed item must not both believe they exclusively own it after simultaneous action.

Queue counts require scope: total eligible, currently available, claimed by me, in progress, blocked or waiting. Server-side filtering/permissions can make personal counts differ from global counts; expose the scope rather than presenting contradictory totals.

Processing flow should preserve throughput without hiding exceptions. After completing one item, define whether the next is auto-opened, suggested or left to the user. Auto-advance can be efficient but dangerous if completion state has not been committed or the next item is high-risk.

## Failure Topology
- List order looks chronological while the backend is actually severity-weighted, making operators distrust changes.
- Two people claim the same item because the UI optimistically assigns without conflict handling.
- “23 remaining” means eligible for this user while managers assume organization-wide backlog.
- Completed items stay in the visible queue until refresh and get processed twice.
- Auto-advance opens the next task while the previous save is still pending.
- Filtering the queue changes priority semantics without indicating that the user is seeing only a subset.

## Falsification and Recovery
Falsify with concurrent claims, priority changes while visible, permission changes, completion failure, queue refill, filtered personal views and auto-advance. Compare visible ordering and ownership to authoritative queue records at each transition.

Recover by exposing ordering rationale, using atomic claim state, scoping counts, reconciling queue membership immediately after commits and delaying auto-advance until the previous state is authoritative.

## Output Contract
Return `work-queue-contract` with eligibility definition, ordering authority, claim/push model, ownership concurrency, queue/count scope, processing/auto-advance policy, blocking states, real-time reconciliation and multi-operator tests.