---
name: designing-column-pinning
description: Use when data-table columns can remain visible at a leading or trailing edge and the interface must manage pinned order, width budget, horizontal scroll, shadows/dividers and accessibility without duplicating cells.
---

# Designing Column Pinning

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns pinned columns in tables/grids. Spreadsheet freeze boundaries are handled by `designing-frozen-panes`.

## Decision Boundary
Pinning preserves context while horizontally scrolling wide data. Define which columns are eligible and whether the product allows leading, trailing or both-side pinning. Identity columns and critical row actions often justify pinning; pinning many arbitrary columns can consume all scrollable width and defeat the feature.

Pinned order must be deterministic. If users reorder columns, decide whether pinning moves a column into a pinned region, preserves its relative order, or stores two dimensions—global order and pin state. Drag previews should make cross-boundary behavior clear.

Set a width budget. If pinned regions exceed the viewport, choose horizontal scroll inside the pinned region, automatic unpin, or blocked action with explanation; never let the central data viewport collapse to zero.

Pinned cells remain the same logical grid cells. Avoid duplicated semantic trees or separate row heights. A divider/shadow can communicate the edge only when actual overflow exists; persistent heavy shadows on static layouts add false depth.

## Failure Topology
- Users pin ten columns and no unpinned content remains visible.
- Pinned copy and scrolled copy both expose the same action to screen readers.
- Row height differs between pinned and center regions after text wraps.
- Drag reordering across pin boundary produces a different persisted order after reload.
- RTL pin-to-start still pins visually left.
- Edge shadow remains even when there is no hidden content behind it.

## Falsification and Recovery
Pin/unpin/reorder, narrow viewport, long wrapped cells, RTL, keyboard grid navigation, virtualization and persisted restore. Verify one logical cell identity and adequate central viewport under all allowed states.

Recover by enforcing a pin-width budget, centralizing row geometry, using logical start/end, reconciling order/pin metadata and rendering overflow cues conditionally.

## Output Contract
Return `column-pinning-contract` with eligibility, leading/trailing semantics, order interaction, width budget, overflow cue, row/cell identity, RTL/persistence and grid-navigation tests.