---
name: designing-mega-navigation
description: Use when a large destination space needs a multi-column or panel-based navigation surface that supports scanning, grouping, keyboard access, and deliberate disclosure without becoming a marketing collage.
---

# Designing Mega Navigation

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns large disclosed navigation panels typically opened from a global category. It does not justify adding a mega menu when a simple list is enough, and it does not let promotional content override navigation clarity. The underlying destination taxonomy remains owned by information architecture.

## Decision Architecture
A mega navigation surface should solve a breadth/scanning problem. Group destinations by user-recognizable concepts, not by arbitrary column balancing. Decide which items are direct destinations, which labels are group headings, whether featured links are genuinely navigational, and how secondary descriptions aid disambiguation without overwhelming scan speed.

Opening and dismissal must have explicit semantics across pointer, keyboard, touch, and screen readers. Hover intent may supplement click/focus, but pure hover ownership creates accidental openings and inaccessible dead zones. Once open, users need stable movement between trigger, panel, groups, and adjacent top-level categories without the panel collapsing during normal pointer travel.

Layout should tolerate localization and dynamic permissions. A three-column design that only works with short English labels is not a navigation contract. If sections disappear for a role, regrouping must not create orphan headings or unpredictable order.

## Failure Topology
- Every top-level item opens a giant panel despite having only three destinations.
- Columns are visually balanced by mixing unrelated categories.
- Panel disappears as the pointer crosses a small gap from trigger to content.
- Keyboard focus enters the panel but Escape or reverse navigation cannot return predictably.
- Marketing cards dominate visual attention and hide primary destination links.
- Permission filtering leaves empty groups and broken spatial rhythm.

## Falsification and Recovery
Falsify with keyboard-only traversal, screen-reader navigation, touch devices without hover, long translations, restricted roles, pointer diagonal movement, viewport edge collision, zoom at 200%, and a category with radically different item count. The design fails if opening modality changes which destinations are reachable or if visual grouping cannot be described as a coherent destination taxonomy.

Recover by using mega navigation only for genuine breadth, binding groups to semantic taxonomy, implementing explicit open/focus/dismiss state, adding hover-intent tolerances rather than hover-only control, and making featured content subordinate to destination reachability.

## Output Contract
Return `mega-navigation-contract` with trigger categories, group taxonomy, destination roles, open/dismiss mechanics, hover intent, keyboard/focus traversal, touch behavior, localization/permission adaptation, responsive fallback, promotional-content limits, and falsification cases.