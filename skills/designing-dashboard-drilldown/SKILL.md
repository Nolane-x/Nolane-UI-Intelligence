---
name: designing-dashboard-drilldown
description: Use when an overview metric or visualization leads into progressively more detailed evidence and the interface must preserve analytical scope, filters, time range and return path across levels.
---

# Designing Dashboard Drilldown

## Parent Contract
**Required parent:** `designing-data-visualization`.

This faculty owns transitions from summary analytics into detail. It does not choose the source chart encoding, prove causal interpretation or define the underlying data warehouse.

## Decision Boundary
A drilldown must answer **what subset did the user ask to inspect?** Carry forward the exact dimension member, measure, time range, global filters, comparison baseline and data freshness that gave rise to the clicked summary. Do not open a generic details page that silently resets those conditions.

Distinguish drill-down, drill-through and navigation. Drill-down changes level within a hierarchy such as year → quarter → month or region → country → site. Drill-through opens underlying records supporting a summary. Navigation merely moves to another product area. Use different affordances and return behavior when these semantics differ.

The detail surface should expose inherited context visibly enough to audit. Breadcrumbs, scope chips, title text or a query summary can show `Revenue / EMEA / Q2 / Enterprise`. Hidden inherited filters create analytical traps because users may interpret the detail as global.

Returning must restore a meaningful overview state: filters, time window, scroll, chart selection and focus where feasible. A browser Back or explicit breadcrumb should not trigger a fresh default dashboard that erases investigative context.

When a selected mark represents aggregated or sampled data, be explicit about whether drill-through can enumerate exact supporting records. If the summary is approximate, the detail cannot pretend to be an exact decomposition unless the backend supports it.

## Failure Topology
- Clicking a bar labeled “EMEA” opens all-region transactions.
- Detail inherits a hidden date filter but the title implies all time.
- Breadcrumb reflects page hierarchy rather than analytical hierarchy.
- Back navigation resets zoom/filter state and the analyst loses the investigation path.
- Approximate KPI drills into exact-looking records whose totals do not reconcile.
- Cross-filter state from sibling charts disappears during drill without explanation.

## Falsification and Recovery
Falsify by drilling from filtered, compared, sampled and stale dashboards; traverse multiple hierarchy levels; switch timezones; use Back/forward; open in a new tab; and reconcile detail totals to the source mark. The contract fails if scope changes silently or return cannot reconstruct the prior analytical state.

Recover by serializing drill context, displaying inherited scope, distinguishing hierarchy drill from record drill-through and retaining/restoring overview state with stable IDs rather than screen coordinates.

## Output Contract
Return `dashboard-drilldown-contract` with source-mark identity, inherited analytical context, drill type, target scope, hierarchy/breadcrumb model, approximation/provenance disclosure, return-state restoration, accessibility/focus behavior and reconciliation tests.