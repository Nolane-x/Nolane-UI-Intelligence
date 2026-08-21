---
name: preserving-responsive-state-continuity
description: Use when responsive mode changes can remount, relocate, hide, or transform interface regions and selection, input, focus, scroll, disclosure, and transient task state must survive correctly.
---

# Preserving Responsive State Continuity

## Continuity Contract
Users do not expect changing window size, orientation, or responsive mode to restart their task. This skill owns which UI state is presentation-independent, how it maps between alternate layouts, and what must happen to focus/scroll when a stateful region moves or changes representation.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent chooses responsive modes. This specialist ensures those modes share one task state rather than behaving like separate mini-applications.

## State Classification
Classify state as domain data, draft input, selection, navigation location, disclosure, focus, scroll/viewport, async operation, or purely presentational. Domain and draft state should normally live above layout-specific branches. Presentation-only state such as “drawer open” needs a mapping when the drawer becomes permanently visible.

For transformed representations, map identity rather than coordinates: selected row `id=42` can become an active card; pixel scroll position may need to become “keep item 42 visible.”

## Transition Rules
Before unmounting a region, capture only state that should persist. Restore focus to an equivalent control or logical task anchor, not blindly to the first element. Pending operations continue or cancel based on operation ownership, not breakpoint change.

## Evidence
Evidence includes transitions with partially typed forms, selected rows, open disclosures, active modals, keyboard focus, scrolled content, and inflight operations. Test both directions and rapid threshold oscillation. Record stable identities used for restoration.

## Failure Modes
Failure includes drafts cleared because mobile and desktop forms are separate trees, focus falling to body after a sidebar becomes a drawer, selected items disappearing, duplicated async submissions from remount effects, and scroll restoration to the wrong semantic location after layout reordering.

## Falsification
Falsification establishes each state class, crosses the breakpoint repeatedly, changes orientation, and continues the task without reload. Lost or duplicated state, stale presentation state applied to the new mode, or focus without a logical continuation disproves the contract.

## Recovery
Recovery lifts durable state to a layout-independent owner, adds explicit representation mappings, cancels duplicated effects by operation identity, and restores focus/visibility by semantic target. Avoid persisting every local UI flag; stale presentation state can be as harmful as lost state.

## Output
Output: `responsive-state-continuity-contract` containing state classes, persistence owners, cross-mode mappings, focus/scroll rules, async handling, and transition evidence.

## Handoff
Handoff session continuation across physically separate devices to cross-device continuity; handoff navigation-specific mode mapping to adaptive navigation transitions.

## Sibling Boundary and delete-the-skill
Responsive reordering governs spatial sequence, not persistence of task state. Removing this skill leaves cross-layout remount/state-loss failures without a dedicated owner, so the delete-the-skill test passes.