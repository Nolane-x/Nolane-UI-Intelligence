---
name: designing-drag-reordering
description: Use when items can be reordered within or between ordered containers and the interface must communicate insertion position, source ownership, constraints, autoscroll, cancellation and keyboard-equivalent movement.
---

# Designing Drag Reordering

## Parent Contract
**Required parent:** `designing-accessible-drag-and-drop`.

This faculty narrows drag/drop to **order mutation**. General move/copy across arbitrary destinations, file drag/drop and free spatial placement are outside this boundary.

## Decision Model
Define the ordered collection and its persistence semantics. Is order globally shared, per-user, grouped, filtered, ranked by explicit position, or computed by another sort? Do not expose manual reordering when an active automatic sort will immediately undo it unless the product explains the interaction.

During drag, preserve source identity and preview exact insertion. A placeholder/gap can show where the item will land; the dragged representation should not duplicate content so convincingly that users think there are two real items. For cross-container reorder, state whether the move changes category/ownership in addition to position.

Autoscroll should support long lists without accelerating so aggressively that target acquisition becomes impossible. Virtualized lists need insertion calculation in logical item space, not only currently mounted DOM bounds.

Keyboard alternatives should support move up/down, move to beginning/end, or choose destination position with announcements appropriate to scale. The same ordering rules and constraints apply.

## Failure Topology
- Manual drag reorders a table currently sorted by Name; the item snaps back after drop.
- Placeholder position differs from committed insertion because virtualization indices shift.
- Dragging across a group silently changes another domain property.
- Touch scrolling becomes reorder because drag handle/intent is unclear.
- Cancelling leaves a placeholder gap or optimistic order saved.
- Keyboard “move down” changes a different order than pointer drag.

## Falsification and Recovery
Test active sort/filter, top/bottom autoscroll, virtualized lists, cross-group moves, cancel/Escape, network failure, concurrent reorder and keyboard movement. Compare preview insertion ID neighbors to committed order.

Recover by disabling/manualizing incompatible sorts, computing positions by stable IDs, making cross-group side effects explicit, using handles/intent thresholds and reconciling optimistic order on failure.

## Output Contract
Return `drag-reorder-contract` with order authority, drag initiation, insertion preview, group-transition semantics, autoscroll/virtualization, commit/cancel, persistence/conflict behavior, keyboard alternative and order-parity tests.