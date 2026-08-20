---
name: designing-kanban-boards
description: Own column-based work visualization where card movement, WIP limits, swimlanes, ordering, and state mapping must be explicit and operationally safe.
---
# Designing Kanban Boards

## Decision ownership

Own board semantics: what columns mean, whether card movement changes workflow state, how ordering works, how WIP limits and swimlanes are represented, and how filtered/partial boards communicate missing work. Generic drag reorder supplies mechanics; this skill decides the consequence of moving a work item within or between lanes and columns.

## Inputs and evidence

Require workflow states, column-to-state mapping, allowable transitions, ordering rules, WIP policies, swimlane dimension, card fields, expected item count, permissions, mobile/touch use, and whether one item can appear on multiple boards. Observe actual high-density boards and transition edge cases rather than only a clean five-column demo.

## Procedure

Declare whether columns are states, categories, stages, or saved queries. If movement changes state, preview invalid transitions and permission constraints before drop. Preserve card identity and enough summary to decide without opening every card, but resist turning cards into miniature forms. Ordering within a column needs a stable rule—manual rank, priority, date, or query sort—and should visibly change when the rule is not manual. WIP limits must distinguish current count, limit, and policy consequence. Filtered boards should state that hidden items may affect counts or limits. Provide keyboard alternatives for moving cards and a low-motion state change equivalent.

## Failure topology

Failures include dragging a card to a column that looks available but represents an invalid transition, WIP counts ignoring hidden filtered items, manual ranking that resets under another sort, cards appearing duplicated across swimlanes, and touch interactions that scroll instead of drag with no recovery. Another failure is showing board order as priority when it is actually arbitrary retrieval order.

## Falsification

Reject if a user cannot tell whether cross-column movement changes state; if a WIP limit can be exceeded silently; if a card's position changes after refresh without an explicit sort reason; if filtered work makes column counts misleading; if keyboard users cannot perform an allowed transition; or if one item can appear twice on the same board without an intentional multi-membership explanation.

## Output contract

Return a `kanban-boards-contract` with: column semantics; movement consequences; transition validation; ordering authority; card summary fields; WIP policy; swimlane model; filtered-state disclosure; drag/keyboard behavior; optimistic update/recovery; and cross-board identity rules. Include one invalid transition and one WIP-limit scenario.

## Handoffs

Use work-item status transitions for state-machine authority, project views/filters for board query scope, workload balancing for people capacity, and generic accessible drag/reorder for motor mechanics. The board must not invent workflow rules that contradict the canonical project model.