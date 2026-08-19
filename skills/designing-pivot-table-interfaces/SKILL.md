---
name: designing-pivot-table-interfaces
description: Use when users reshape multidimensional data into row, column, filter and measure axes and the interface must make aggregation, hierarchy, rearrangement and drill semantics inspectable.
---

# Designing Pivot Table Interfaces

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns the interaction model for pivoting dimensions and measures into a cross-tabular analytical view. It does not define statistical meaning of measures, source-data correctness or general spreadsheet formulas.

## Decision Boundary
A pivot table is a view transformation over data, not merely a table whose columns can be dragged. Model the configuration explicitly: available fields, dimensions, measures, aggregation functions, row axis, column axis, filters, value ordering and optional hierarchy levels. The rendered grid must be traceable back to that configuration.

Field movement needs semantic constraints. A numeric field placed as a measure may default to sum only when that aggregate is meaningful; IDs, ratios and percentages often require count, average, distinct count or domain-specific handling. Never silently choose an aggregate that can change analytical meaning. Show the active aggregation near the measure and provide a route to change it.

Drag-and-drop shelves can accelerate expert work, but keyboard commands and menus must provide equivalent placement. Preview insertion position and whether a field will become a row dimension, column dimension, measure or filter before drop. Reordering hierarchy levels must update both headers and drill behavior coherently.

Totals and subtotals need scope labels. A subtotal over filtered data, visible data, or all underlying records are different claims. Grand totals should not imply additivity for non-additive measures. Sparse combinations need deliberate empty-cell treatment so absence is not confused with numeric zero.

## Failure Topology
- A percentage field is automatically summed and produces meaningless totals.
- Dragging a field between axes changes aggregation without showing that change.
- Collapsed hierarchy visually hides child categories but subtotal scope is unclear.
- Blank cells are rendered as zero, inventing observations.
- Keyboard users can inspect a pivot but cannot rearrange its fields.
- Large pivots produce hundreds of columns with no hierarchy collapse or search path.

## Falsification and Recovery
Falsify with additive and non-additive measures, missing combinations, nested dimensions, filter changes, field removal, reordered hierarchies, keyboard-only configuration and large cardinality. Compare every displayed header/aggregate to the configuration model. If two different pivot definitions can produce an indistinguishable configuration UI, the design is under-specified.

Recover by exposing field roles and aggregation explicitly, constraining invalid placements, separating missing from zero and providing hierarchy collapse/search before rendering unbounded cross-tabs.

## Output Contract
Return `pivot-table-interface-contract` with field taxonomy, axis configuration, placement/reorder interactions, measure aggregation rules, hierarchy/drill behavior, subtotal/total scope, sparse-cell semantics, keyboard alternatives and configuration-to-render parity tests.