---
name: designing-sprint-planning
description: Use when this specialist's decision ownership is materially in scope. Own timeboxed planning interfaces that balance candidate work, capacity, carryover, goals, dependencies, and commitment without equating a sprint with a filtered task list.
---
# Designing Sprint Planning

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the transition from backlog candidates to a bounded iteration commitment. Decide how sprint goal, capacity, candidate selection, carryover, estimate totals, dependencies, and unplanned scope are represented. This skill does not define the team's process methodology; it ensures the UI makes commitment and capacity consequences explicit.

## Inputs and evidence

Require iteration duration, team membership, capacity model, estimate unit, historical carryover, sprint-goal practice, dependency constraints, permissions, holidays/availability, and handling of work added after start. Determine whether capacity is team-level, person-level, or intentionally not estimated.

## Procedure

Present candidate work and committed work as distinct states. Show capacity as an evidence-backed envelope, not a precision guarantee; include availability changes and unestimated work separately. Selection should reveal blockers and dependencies before commitment. Sprint goal belongs above the item list and should remain visible when trade-offs are made. Starting a sprint needs a summary of scope, unestimated items, unresolved blockers, and carryover. Mid-sprint additions should be attributable and distinguish planned from unplanned work. Closing should disposition incomplete items explicitly instead of silently moving everything forward.

## Failure topology

Failures include capacity totals that imply false certainty, sprint start with hidden blockers, carryover that erases historical missed commitment, goal text buried after planning, adding work mid-sprint with no scope-change record, and closing a sprint by automatically rolling unfinished work into the next iteration. Another failure is forcing individual capacity when the team intentionally plans collectively.

## Falsification

Reject if users can start a sprint without seeing unresolved critical dependencies; if unestimated work is counted as zero; if added-after-start work cannot be distinguished in retrospective evidence; if carryover loses its original sprint history; if capacity remains unchanged after a member becomes unavailable; or if the interface requires a planning granularity the team does not use.

## Output contract

Return a `sprint-planning-contract` with: sprint lifecycle; goal placement; candidate/committed states; capacity model; estimation aggregation; blocker disclosure; start gate; mid-sprint scope-change attribution; carryover semantics; close/disposition flow; and historical evidence. Include one over-capacity plan and one mid-sprint addition scenario.

## Handoffs

Use backlog grooming for candidate readiness, workload balancing for person-level constraints when applicable, effort estimation for estimates, dependency networks for blockers, and project health dashboards for post-start monitoring.