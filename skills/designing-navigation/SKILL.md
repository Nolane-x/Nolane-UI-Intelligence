---
name: designing-navigation
description: Use when users must move among multiple spaces, objects, levels, modes, or destinations and need stable orientation, wayfinding, or scalable access.
---

# Designing Navigation

## Overview
Navigation is an externalized mental model. Choose a navigation structure by destination semantics, scale, frequency, and device constraints—not by whatever shell is fashionable.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require an information architecture and user/task model when navigation is nontrivial.

## Classify navigation
Separate:
- **global:** durable product areas
- **contextual/local:** sub-areas of the current object or workflow
- **object switching:** workspace/project/account/environment selectors
- **history/recency:** recent destinations
- **command/search:** direct destination access
- **mode switching:** changes how the same content behaves; do not disguise modes as destinations

Mixing these roles in one visual row creates ambiguity.

## Choose structures by constraints
Evaluate sidebar, top navigation, tabs, tree, breadcrumbs, command palette, hub/index, bottom navigation, or hybrid based on:
- destination count and future growth
- label length/localization
- hierarchy depth
- switching frequency
- need to preserve context while switching
- available viewport
- keyboard/touch access
- whether destinations are peer areas or nested objects

Do not use tabs for an unbounded set or unrelated destinations merely because they are compact.

## Orientation invariants
At any navigable state users should be able to answer, when relevant:
1. where am I?
2. which object/context am I inside?
3. what are sibling destinations?
4. how do I go back/up without losing work?
5. has navigation changed the mode, object, or route?

Active state must be perceptible without relying only on color.

## State preservation
Define what persists across navigation: filters, selection, scroll, unsaved state, query, object context. Reset only when the new destination semantically invalidates the state; surprise resets are lost work even when no data is deleted.

## Responsive transformation
Do not shrink desktop navigation until it disappears. Define semantic transformations: persistent sidebar → compact rail → disclosure drawer; peer tabs → horizontally scrollable only when discoverability remains acceptable; multi-column master/detail → explicit back-stack on narrow screens.

## Deep-link and permission behavior
Navigation must support direct entry into allowed destinations and a truthful response to unavailable ones. Do not silently redirect a forbidden/deleted link to a visually similar area that makes the user think the action succeeded.

## Output: `navigation-contract`
Return `nav_roles`, `destination_model`, `chosen_structures`, `orientation_rules`, `active_state`, `context_switching`, `state_persistence`, `responsive_transformations`, `deep_link_behavior`, `permission_behavior`, and `keyboard_model`.

## Common failures
- Breadcrumbs used as decoration rather than hierarchy.
- Multiple navigation rows with overlapping destination sets.
- Hiding core destinations behind “More” to preserve symmetry.
- Mobile drawer with no persistent indication of current location.

## V6 Navigation Wayfinding Protocol
Run a **place-versus-mode test** for each navigation-looking control. A place changes the destination/context and should participate in history/deep linking when appropriate; a mode changes how the same content behaves and needs persistent mode visibility. Conflating them creates back-button and mental-model failures.

Build a **wayfinding cue stack** using only cues the product can sustain: current destination, hierarchy/breadcrumb, object identity, workspace/environment, URL/history, and landmark structure. No single cue should carry all orientation if it disappears on small screens. Define a **deep-link history contract** for direct entry, browser/system back, forward, refresh, restored session, and links shared across permissions.

Specify **navigation-state persistence** for expanded groups, scroll position, selected subview, filters, and recently visited objects. Persistence must be scoped correctly—per account/workspace/device/session—so one context does not leak into another. Run **hierarchy-growth stress** with 2–5× destinations, long labels, nested objects, role-gated items, and archived spaces.

### Falsification
Enter every major destination from an external deep link, switch workspace, use back/forward, shrink viewport, and remove the primary navigation shell. If orientation or state becomes unknowable, the model relies on chrome rather than structure.

### Recovery
Split place/mode concepts, introduce scalable search/command access, or restructure hierarchy. Do not solve growth by endlessly shrinking labels or nesting menus.
