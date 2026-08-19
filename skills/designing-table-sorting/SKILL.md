---
name: designing-table-sorting
description: Use when users reorder tabular records by one or more columns and the interface must expose sort priority, direction, comparator semantics, server latency and selection/focus continuity.
---

# Designing Table Sorting

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns sort interaction and its representation. Backend comparator correctness and domain ranking definitions remain source-of-truth concerns.

## Decision Model
Define sortable columns and comparator semantics per data type: numeric, locale-aware text, date/time, enum/domain order, missing values and derived metrics. Never assume lexicographic sort is correct because values render as strings.

Choose single or multi-column sorting. Multi-sort needs visible priority (`1`, `2`, `3` or equivalent) and a discoverable way to add/remove/reorder sort keys. The cycle—ascending, descending, none—should be consistent and reflect meaningful domain order; “ascending” for severity may not equal low-to-high alphabetical labels.

Preserve record identity while order changes. Selection should follow selected IDs rather than row positions. Focus may stay on the header that triggered sort or the active row, depending on task; do not send keyboard users to a new row merely because its index changed.

Server-side sort needs pending/freshness behavior. Keep the existing table usable or indicate pending according to consistency needs, reject stale responses and avoid showing the new sort indicator before data can be understood as sorted unless pending state is explicit.

## Failure Topology
- Numeric values `2, 10, 100` sort lexicographically.
- Sort icon changes instantly but server data is still in old order with no pending cue.
- Selected row remains “row 5” and now points to a different record.
- Multi-sort priority is hidden behind a tooltip.
- Clearing sort returns to an undefined order rather than a known default.
- Null values jump between top/bottom inconsistently across directions.

## Falsification and Recovery
Test numeric/text/date/enum/null, single/multi sort, server races, selection, pagination, keyboard and restore/default sort. Compare UI order to declared comparator rules, not visual intuition.

Recover by formalizing comparators/default order, keying state by record ID, exposing multi-sort priority and representing async pending truth explicitly.

## Output Contract
Return `table-sorting-contract` with sortable fields, comparator/null rules, single/multi interaction, priority/direction display, default/reset state, async race policy, selection/focus continuity and order fixtures.