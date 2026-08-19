---
name: designing-frozen-panes
description: Use when rows or columns remain fixed while the rest of a grid scrolls and the interface must preserve coordinate continuity, headers, focus movement and resize behavior across frozen boundaries.
---

# Designing Frozen Panes

## Parent Contract
**Required parent:** `designing-spreadsheet-interfaces`.

This specialist owns fixed row/column regions within a scrolling cell plane. Generic sticky headers and column pinning outside spreadsheet semantics route separately.

## Decision Model
Represent freeze as a boundary in logical row/column coordinates, not duplicated data. The same cell must not exist as two independent interactive instances. Frozen and scrollable quadrants share one selection, focus and edit model while using synchronized axes.

Define common states: none, freeze top N rows, freeze left N columns, or freeze at active-cell boundary. Users need a visible divider that differs from ordinary grid lines and a clear unfreeze path. If panes can be split independently rather than frozen, treat that as a different feature because both regions may scroll.

Focus/navigation can cross the boundary. Moving from frozen header column into scrolled data should keep the target visible without unexpectedly moving the frozen section. Editing a cell near the boundary must not be clipped by quadrant containers.

Resize row/column widths affects every quadrant consistently. RTL can invert the semantic “leading frozen columns”; avoid hard-coding left when the product means start/identifier columns.

## Failure Topology
- Frozen cells are duplicated DOM controls and both can receive focus.
- Horizontal scroll misaligns row heights between frozen and body quadrants.
- Freeze divider looks like a selectable cell border.
- Keyboard navigation crossing boundary scrolls the entire grid including supposedly frozen headers.
- Column resize updates body but not frozen copy until next render.
- RTL freezes the wrong side.

## Falsification and Recovery
Freeze rows/columns together, scroll both axes, edit/copy ranges crossing boundaries, resize dimensions, zoom, RTL, screen reader and virtualize large data. Verify each logical coordinate has one semantic identity.

Recover by centralizing grid state, synchronizing quadrant geometry, using logical start/end semantics and removing duplicated focusable representations.

## Output Contract
Return `frozen-pane-contract` with freeze boundary model, quadrant synchronization, divider affordance, cross-boundary focus/selection/edit behavior, resize/virtualization, RTL semantics and coordinate-identity tests.