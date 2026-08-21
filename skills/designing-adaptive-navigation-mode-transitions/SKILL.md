---
name: designing-adaptive-navigation-mode-transitions
description: Use when navigation changes between rail, sidebar, tabs, drawer, menu, or compact affordances and current location, hierarchy, reachability, open state, and orientation must survive the transition.
---

# Designing Adaptive Navigation Mode Transitions

## Navigation Is Stateful
Switching navigation presentation is not a visual substitution. A user may have a selected destination, expanded branch, search/filter state, unread counts, or focus inside navigation when the layout changes. This skill owns the state mapping between navigation modes.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent governs responsive layout. Base information architecture and destination taxonomy remain outside this specialist; it acts when the same navigation model changes physical mode.

## Mode Mapping
Declare navigation states such as expanded rail, compact rail, persistent sidebar, temporary drawer, tab row, and overflow menu only when they preserve the same destination model. Map selected item, ancestor expansion, badges, disabled destinations, and pending navigation consistently. Temporary containers need explicit open/close policy when crossing into a persistent mode.

The current location must never disappear merely because its destination moves into overflow. If a destination cannot be represented in a compact mode, the system needs a discoverable continuation rather than omission.

## Evidence
Evidence includes route-to-affordance mappings across modes, breakpoint transition while a branch is expanded, keyboard/focus continuity, deep-linked destinations, and overflow cases with long/localized labels. Verify both entering and leaving temporary navigation modes.

## Failure Modes
Failure includes drawer state persisting invisibly after becoming a sidebar, selected destinations hidden in “More” with no current-location cue, focus stranded in an unmounted drawer, hierarchy collapsed without ancestry indication, and route coverage differing by width.

## Falsification
Falsification deep-links to every navigation depth, transitions width while focus is inside navigation, changes modes with a branch expanded, and verifies every destination remains reachable. A destination or location cue lost solely due to mode change falsifies the contract.

## Recovery
Recovery reconstructs navigation state from route and hierarchy rather than local presentation state, moves focus to the equivalent affordance when the container changes, and gives overflow a selected/current state. If mode differences imply different information architecture, route to navigation architecture rather than hiding the mismatch.

## Output and Handoff
Output: `adaptive-navigation-mode-transitions-contract` containing mode mappings, selected/expanded/open state rules, reachability proof, and focus continuity. Handoff command overflow within toolbars to toolbar-overflow design.

## Sibling Boundary and delete-the-skill
Responsive region reordering governs general regions, not navigation's persistent route/hierarchy state. Removing this skill leaves destination reachability and navigation-state continuity across modes without a specialist owner.