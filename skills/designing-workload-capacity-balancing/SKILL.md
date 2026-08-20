---
name: designing-workload-capacity-balancing
description: Use when this specialist's decision ownership is materially in scope. Own workload-versus-capacity views that help allocate work without presenting estimates, availability, or people as interchangeable precision units.
---
# Designing Workload Capacity Balancing

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own interfaces that compare assigned demand with available capacity across people, teams, or roles. Decide demand measure, capacity evidence, horizon, overload cues, unassigned work, skill/role constraints, and reassignment previews. This owner does not decide HR staffing policy or algorithmically optimize people; it makes planning assumptions visible and revisable.

## Inputs and evidence

Require assignment model, estimate units, availability calendars, part-time/leave data if permitted, work horizon, role/skill constraints, unestimated-work policy, team boundaries, privacy constraints, and whether work can have multiple owners. Identify which capacity figures are authoritative and which are rough planning assumptions.

## Procedure

Choose one demand metric per planning mode and label uncertainty. Do not convert story points to hours unless the organization has an explicit model. Show unestimated work separately rather than as zero. Capacity should account for known availability while respecting privacy—display planning availability, not personal reasons. Overload indicators need a horizon and cause, with drill-down to contributing items. Reassignment should preview impact on both source and target and flag permission/skill/dependency constraints. Provide team-level aggregation before individual detail when precise person allocation is not culturally or operationally appropriate.

## Failure topology

Failures include false precision, people ranked by utilization as if 100% is universally desirable, unestimated work disappearing, leave data exposing sensitive detail, assignments shifted solely to balance a chart, and capacity graphs that mix incompatible estimate units. Another failure is showing red overload with no list of contributing commitments.

## Falsification

Reject if unestimated work reduces apparent load; if two different estimate units are summed without a defined conversion; if capacity changes expose sensitive absence reasons; if an overload cannot be traced to items/horizon; if reassignment ignores required ownership or skills; or if the interface implies that maximizing individual utilization is the primary project goal.

## Output contract

Return a `workload-capacity-balancing-contract` with: demand metric; capacity source; horizon; uncertainty labeling; unestimated-work treatment; team/person aggregation; overload thresholds and evidence; unassigned-work view; reassignment preview; privacy rules; and skill/role constraints. Include one partially unavailable person and one unestimated critical item.

## Handoffs

Use effort estimation for demand inputs, sprint planning for iteration capacity, assignment/ownership for authoritative owner changes, and project health for aggregate delivery risk. Calendar availability may feed capacity but does not dictate allocation.