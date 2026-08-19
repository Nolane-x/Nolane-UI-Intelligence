---
name: designing-table-grouping
description: Use when records are organized into expandable groups with headers or aggregates and the interface must define hierarchy, group identity, sorting/filtering interaction, selection scope and aggregate truth.
---

# Designing Table Grouping

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This specialist owns grouped tabular presentation. General tree hierarchy and pivot tables are separate faculties.

## Decision Boundary
A group represents a meaningful category, bucket or key. Define stable group identity and whether groups are one or multiple levels. Group headers can show label, count, aggregate and actions, but they are not ordinary data rows and should not inherit row semantics accidentally.

Expansion/collapse controls visibility, not data membership. Selected hidden children may remain selected only with explicit scope feedback. Group-level selection can mean select visible children, all matching children including unloaded pages, or the group object itself—these must not share one checkbox without state explanation.

Sorting can occur **between groups**, **within groups**, or both. Filtering may remove children and empty groups; decide whether empty groups disappear or remain as structural categories. Aggregates must identify whether they reflect all group data or only filtered/loaded records.

Large server-backed groups can lazy-load. Expanding should preserve header position, show loading/error inside the group and avoid reordering other groups unexpectedly when counts arrive.

## Failure Topology
- Group header is announced as a normal row and column relationships become confusing.
- Sorting globally interleaves children and destroys grouping.
- Group checkbox selects only loaded 50 of 5,000 children with no disclosure.
- Aggregate sum represents filtered data but header label implies total group value.
- Collapsing hides focused cell without moving focus safely.
- Empty groups disappear during filter and reappear in unstable order.

## Falsification and Recovery
Test multi-level groups, sort/filter combinations, hidden selection, group select, lazy load, empty groups, aggregates and keyboard focus collapse. The contract fails if group membership or aggregate scope cannot be stated from visible UI.

Recover by formalizing group identity/scope, separating group header semantics, defining sort layers, exposing aggregate/filter scope and moving focus to surviving group controls on collapse.

## Output Contract
Return `table-grouping-contract` with group keys/levels, header semantics, expansion, sort/filter layers, selection scope, aggregate truth, lazy loading, focus handling and grouped-order tests.