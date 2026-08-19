---
name: designing-tooltip-systems
description: Use when concise supplemental information must appear on hover or focus and the system needs consistent triggering, delay, persistence, placement and accessible alternatives without making tooltips a dependency for basic use.
---

# Designing Tooltip Systems

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns tooltip behavior across a product. It does not own help documentation, validation messages, rich popovers or essential labels.

## Decision Boundary
A tooltip is short supplemental information associated with a target. If content contains interactive controls, long structured explanation, confirmation, or workflow state, use another surface. If a control is otherwise unlabeled and comprehension depends on the tooltip, ensure an accessible name exists independently.

Coordinate pointer hover and keyboard focus. A tooltip opened by focus should remain while focus stays on the target; pointer movement into incidental gaps should not cause flicker. Define initial delay, sibling-transfer delay and dismissal so scanning a toolbar does not require waiting repeatedly or produce a swarm of bubbles.

Placement must avoid covering the target or information users are comparing. Collision handling can shift placement, but the tooltip should remain visibly associated. On touch-only devices, decide whether the information is unnecessary, available through another help path, or should become a different interaction; do not bolt long-press tooltips onto every icon and conflict with context menus.

Tooltip timing must not be tied to animation completion. Escape or target blur dismisses semantically even if a fade remains.

## Failure Topology
- Tooltips contain buttons/links, creating a focusable surface that disappears when users try to enter it.
- Every toolbar item waits a full delay while the pointer scans across siblings.
- Tooltip covers the value or chart mark being explained.
- Same message is redundantly announced as accessible name and tooltip description.
- Touch long-press conflicts with drag/context menu.
- Tooltip persists after target removal or scroll-out.

## Falsification and Recovery
Scan dense toolbars, tab through targets, move from target to tooltip, scroll, zoom, remove target, use touch/coarse pointer and screen reader. The design fails if essential meaning becomes unreachable without hover or if a tooltip behaves like an interactive popover.

Recover by moving essential labels into the interface, promoting rich content to popover/help, sharing a system delay model and deriving placement from live target geometry.

## Output Contract
Return `tooltip-system-contract` with content eligibility, trigger modalities, delay/persistence model, sibling transfer, placement/collision, dismissal, touch alternative, accessible naming/description policy and stress cases.