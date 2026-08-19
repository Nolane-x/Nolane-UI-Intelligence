---
name: designing-table-filtering
description: Use when tabular data is narrowed by column or global filters and the design must make active constraints, result scope, server state, empty results and hidden selections understandable.
---

# Designing Table Filtering

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns filter interaction around a table/grid. Complex boolean query construction is delegated to `designing-search-filter-builders`.

## Decision Model
Expose active filters in a place users can audit, not only inside closed column menus. Column header badges/counts, filter chips or a summary row can show that the visible dataset is constrained. A table with “0 rows” is misleading if the real state is “0 of 8,240 match 3 filters.”

Match controls to data type: text contains/prefix, numeric ranges, date ranges, enums, booleans, null/empty, domain-specific predicates. Avoid generic operator soup in routine tables. Define whether filters apply immediately, after debounce, or on explicit Apply based on data size/cost.

Filtering interacts with selection, pagination and aggregates. Hidden selected rows can remain selected only if scope is visible; aggregate totals must state whether they cover visible/matching/all data. Server-side filtering needs request identity and stale-response rejection.

Persisted filters can be useful, but stale schema or permission changes need recovery. Deep links should encode shareable filters only when values are safe to expose in URLs.

## Failure Topology
- Filter is active in a closed menu but no persistent indicator explains missing rows.
- Clearing the search box leaves hidden column filters active and users think data is lost.
- Selected rows remain hidden and bulk action count gives no warning.
- Aggregate total silently changes from all data to filtered data.
- A slow previous filter response overwrites the newest result.
- Sensitive filter values leak into shareable URL history.

## Falsification and Recovery
Apply multiple filters, clear one/all, reach no-results, change schema, paginate, select then hide rows, race server responses and restore saved state. The contract fails if users cannot reconstruct why a visible row set exists.

Recover by centralizing filter state, persistent active indicators, explicit scope for counts/selection/aggregates, stale-response guards and safe persistence rules.

## Output Contract
Return `table-filtering-contract` with filter types, activation/apply model, active-state presentation, result/aggregate scope, selection interaction, server lifecycle, persistence/share policy, empty/reset states and filter-parity tests.