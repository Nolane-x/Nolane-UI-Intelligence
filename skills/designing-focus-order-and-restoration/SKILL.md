---
name: designing-focus-order-and-restoration
description: Use when dialogs, route changes, conditional regions, destructive actions, or dynamic content can move or remove keyboard focus and the interface must preserve a coherent working position.
---

# Designing Focus Order and Restoration

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns temporal focus continuity: where focus begins, how it moves when structure changes, and where it returns after transient surfaces or removed objects disappear. It does not define every keyboard shortcut. Its decision is whether the user's active working position remains semantically coherent through UI mutations.

## Decision Boundary
Derive focus order from task and reading sequence, not visual pixel coordinates or positive tabindex values. Opening a modal, popover with keyboard interaction, or full-screen task may intentionally move focus to a meaningful start point. Closing it should normally restore focus to the invoker, unless that object no longer exists or the completed action makes a different destination more useful. In those cases define a deterministic fallback such as the next sibling, parent collection, or new primary result.

Route transitions require a separate policy from dialog restoration. A route change initiated by navigation may need focus at the new page's primary heading or task start, while an in-place filter update usually preserves the user's control. When a focused row is deleted, do not send focus to document body; preserve collection context and announce the outcome.

## Failure Topology
- Closing a dialog resets focus to the browser chrome or document start.
- Deleting the focused item leaves focus on a detached node with no visible indicator.
- Responsive reordering changes DOM order to match columns visually but creates a nonsensical keyboard sequence.
- Client-side navigation keeps focus on the old navigation link while screen content changes silently.
- Every asynchronous update steals focus to a newly rendered message or result.
- Restoration targets an invoker that became disabled or hidden during the operation.

## Falsification and Recovery
Record focus position before and after opening/closing overlays, route changes, CRUD operations, validation failures, filtering, sorting, pagination, and responsive recomposition. Test keyboard, screen reader, and programmatic focus indicators. The design fails if the next focus target cannot be predicted from the user's task or if focus movement is used merely to force an announcement.

Recover by defining explicit focus transition tables, stable fallback targets for removed elements, semantic route-entry targets, and preservation rules for in-place updates. Remove positive tabindex sequencing and repair DOM/task order instead of encoding visual layout numerically.

## Output Contract
Return `focus-order-restoration-contract` with baseline order rules, focus-entry triggers, overlay restoration, removed-object fallbacks, route-transition policy, in-place-update preservation, responsive considerations, and transition verification cases.
