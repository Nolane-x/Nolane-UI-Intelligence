---
name: designing-roving-focus-composites
description: Use when a composite widget contains many peer items but should expose one tab stop while arrow, home/end, typeahead, or spatial keys manage focus within the component.
---

# Designing Roving Focus Composites

## Parent Contract
**Required parent:** `designing-keyboard-power-user-ux`.

This faculty owns focus management inside composite widgets such as tablists, toolbars, menus, grids, radio-like groups, and other collections where tabbing through every child would be inefficient. It does not authorize inventing a roving model for ordinary lists of independent links or controls.

## Decision Boundary
First establish whether the component is genuinely composite: the items share one interaction mode and users benefit from entering the component once, moving internally, then tabbing onward. If so, define the active descendant or roving `tabindex` strategy, the orientation-specific movement keys, wrapping policy, disabled-item treatment, and whether selection follows focus. Focus and selection must remain separate unless the pattern's semantics make immediate selection safe.

Dynamic collections need deterministic retention. When items are inserted, removed, reordered, virtualized, or filtered, the roving tab stop must remain on a valid item without jumping unpredictably. Home/End and typeahead should respect the same logical ordering users hear and see. Nested composites require an escape boundary so inner arrow handling does not capture keys that belong to the outer structure.

## Failure Topology
- Every child remains in the tab sequence, so a dense toolbar requires dozens of Tab presses.
- Arrow keys move visual highlight but DOM focus stays elsewhere.
- Selection fires on focus in a destructive or expensive control where users need exploration without activation.
- Removing the active item leaves no tabbable item in the composite.
- RTL or vertical orientation is treated as a cosmetic transform while directional behavior stays wrong.
- Nested components both consume the same arrows and trap the user.

## Falsification and Recovery
Test entry from both directions, all navigation keys, disabled items, first/last boundaries, dynamic insertion/removal, filtering, virtualization, RTL, and screen-reader browse/focus modes. The contract fails if Tab enters multiple peer items, if the active item differs between visual and programmatic focus, or if users cannot leave the composite without hidden knowledge.

Recover by choosing one canonical focus strategy, centralizing active-item identity, separating focus from selection, and recomputing a valid active target after collection mutation. If the collection behaves as independent controls rather than one composite, remove roving focus entirely.

## Output Contract
Return `roving-focus-contract` with composite eligibility, tab-stop model, movement key map, orientation/RTL behavior, selection coupling, disabled-item policy, mutation recovery, nested-boundary rules, and keyboard/assistive verification cases.
