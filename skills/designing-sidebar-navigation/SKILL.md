---
name: designing-sidebar-navigation
description: Use when a persistent vertical navigation region must represent hierarchy, expansion, selection, density, scrolling, and responsive collapse without becoming a generic list of links.
---

# Designing Sidebar Navigation

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns vertical navigation as an information-dense orientation instrument. It does not own arbitrary side panels, inspectors, or the whole application shell. A sidebar is justified when persistent section visibility, hierarchy, or rapid switching is valuable enough to spend horizontal space.

## Decision Model
Decide whether the sidebar represents a flat destination set, a tree, grouped sections, user-created objects, or a hybrid. Do not visually indent items without defining hierarchy semantics. Expansion state, current destination, selected object, and hover/focus are different states and need distinct cues.

If the sidebar can collapse, define what “collapsed” preserves. Icon-only modes require recognizable icons, accessible names, and a discoverable expansion path; they are not a free density win. A drawer on narrow screens changes persistence and focus behavior, so it must be treated as a mode transition rather than the same sidebar squeezed thinner.

Scrolling needs ownership. Keep global controls such as workspace switchers or account actions from being accidentally pushed out by a long destination list. User-created lists may need virtualization or search, but navigation order should remain stable enough for spatial memory.

## Failure Topology
- Parent and child rows look identical, so indentation is the only hierarchy cue.
- Collapsed icons are ambiguous and tooltips become the only way to understand navigation.
- Active destination disappears above the scroll viewport after deep linking.
- Expanding a group unexpectedly navigates to its overview and loses disclosure state.
- Sidebar scroll competes with page scroll and traps wheel/touch input.
- Responsive drawer closes before route confirmation and loses focus restoration.

## Falsification and Recovery
Falsify with hundreds of user-created items, long localized names, deep links to a collapsed child, keyboard traversal, screen reader list/tree semantics, compact viewport, persisted collapse state, and permission changes that remove the current item. The design fails if users cannot distinguish disclosure from navigation or recover the current location after the sidebar’s structure changes.

Recover by declaring row roles, separating expansion from activation, preserving current-path ancestors, bounding fixed versus scrollable regions, providing labeled compact representations, and defining focus/scroll restoration for responsive mode changes.

## Output Contract
Return `sidebar-navigation-contract` with hierarchy model, row roles, grouping, active/expanded/selected states, scroll regions, collapse semantics, responsive drawer behavior, persistence policy, keyboard/accessibility model, deep-link reveal rules, and falsification cases.