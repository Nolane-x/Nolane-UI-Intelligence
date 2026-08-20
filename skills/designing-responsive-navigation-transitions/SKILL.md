---
name: designing-responsive-navigation-transitions
description: Transform navigation structures across responsive states while preserving destination semantics, current location, hierarchy, and efficient return paths.
---

# Designing responsive navigation transitions

Desktop navigation cannot simply be hidden behind a hamburger without considering hierarchy and orientation. Use this skill when tabs, sidebars, global bars, breadcrumbs, drawers, or bottom navigation must transform as space changes.

## Decision ownership

Own the mapping between navigation forms, destination parity, current-location representation, hierarchy preservation, and state retention. Decide what becomes a drawer, menu, bottom bar, select-like control, or alternate route structure.

## Inputs and evidence

Collect navigation taxonomy, route frequency, depth, role differences, current-location markers, back behavior, persistent badges, keyboard shortcuts, and mobile usage. Identify items that disappear at narrow widths or change labels unexpectedly.

## Procedure

Create a destination mapping across states. Every important route should remain reachable with predictable semantics even if its presentation changes. Preserve current location visibly after transition and keep expanded/collapsed section state when feasible.

Use platform-appropriate navigation patterns without changing the information architecture accidentally. If a sidebar hierarchy becomes a drawer, retain grouping and labels rather than flattening everything into one list. Coordinate browser history and native back behavior with transient navigation surfaces.

Ensure focus moves logically when a navigation container opens or closes during resize.

## Failure topology

Responsive navigation often drops secondary destinations, losing functional parity. Current-route indicators may disappear inside collapsed controls. Another failure is depth collapse: a hierarchical sidebar becomes a flat menu whose labels are ambiguous without parents.

Resizing with an open drawer can strand focus or leave both desktop and mobile navigation exposed to assistive technology.

## Falsification

For every destination, verify reachability and current-location feedback at each state. Resize while a nested navigation item is focused or expanded. Test browser back, Escape, keyboard traversal, and screen-reader landmarks. Compare route count and hierarchy across representations.

If users must learn different destination names on mobile and desktop, document and justify the semantic change or correct it.

## Output contract

Produce a `responsive-navigation-transitions-contract` containing cross-state destination mapping, hierarchy representation, current-location rules, open/close behavior, state preservation, focus/back semantics, and parity tests for all priority routes.

## Handoffs

Use `designing-global-navigation-shells`, `designing-sidebar-navigation`, or `designing-bottom-navigation` for pattern-specific mechanics, `designing-responsive-region-reordering` for movement, and `verifying-responsive-state-parity` for cross-state completeness.