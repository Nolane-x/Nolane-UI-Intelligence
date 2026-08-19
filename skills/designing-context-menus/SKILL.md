---
name: designing-context-menus
description: Use when commands should be exposed at the object or location they affect and the interface must preserve context, platform invocation conventions, discoverability and alternative command paths.
---

# Designing Context Menus

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns object/location-scoped context menus. It does not invent the command set or replace required visible controls.

## Decision Boundary
A context menu is justified when the target already has a clear semantic identity and several secondary actions benefit from proximity. Right click, long press, keyboard context-menu invocation and platform-specific gestures may open it; the result must operate on the same canonical target regardless of modality.

Capture context at invocation. In a multi-select surface, define whether the menu applies to the clicked item, the whole current selection, or changes selection first. This is a major product decision: silently collapsing a multi-selection on right-click can make a destructive command affect the wrong set.

Menu contents should be contextual, not arbitrary. Prefer a stable core ordering with disabled/omitted commands based on applicability. Overly dynamic reshuffling harms learned position. State-changing commands need current state labels or checkmarks where platform conventions support them.

Context menus are secondary discovery. Critical or sole-path actions need visible, keyboard-reachable alternatives. Long-press should not steal gestures from scrolling/selection without clear intent thresholds.

## Failure Topology
- Right-click on one selected row clears the rest before a bulk action without warning.
- The same command changes label/order on every invocation, destroying muscle memory.
- Touch users cannot discover a command that exists only on right click.
- Menu position blocks the target state needed to understand the action.
- Invocation on empty space accidentally inherits the last object’s context.

## Falsification and Recovery
Test single selection, multi-selection, empty-space invocation, keyboard context key/Shift+F10 equivalents, long press, disabled permissions, stale objects and rapid target changes. The contract fails if the user cannot state which objects an action will affect before activation.

Recover by freezing target scope at invocation, showing scope in labels where needed, preserving alternative command paths and separating background/context menus from object menus.

## Output Contract
Return `context-menu-contract` with invocation modalities, target-resolution rule, selection interaction, canonical command bindings, ordering/applicability, discoverability alternatives, dismissal/focus behavior and scope tests.