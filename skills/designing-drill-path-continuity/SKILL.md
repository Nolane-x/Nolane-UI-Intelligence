---
name: designing-drill-path-continuity
description: Use when analytical users move from aggregate summaries into progressively finer detail and the product must preserve population, filters, grain, orientation, and a reliable path back.
---

# Designing Drill Path Continuity

Drill is not navigation to a new page. It is a controlled change in analytical grain. The interface must make the retained context and the changed context equally explicit.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent owns the BI workspace. This skill owns continuity across aggregate → segment → record-detail transitions and any reversible path among those levels.

## Grain Contract
For each drill edge, declare source grain, target grain, retained predicates, introduced predicates, changed metric behavior, and the allowed return operation. A bar representing monthly revenue by region cannot blindly drill to transaction rows if the metric includes modeled allocations that do not exist as rows; the target must explain reconciliation differences.

Preserve an analytical breadcrumb composed of meaning, not merely page titles. Useful breadcrumb state may include metric, selected mark, time range, filter set, grouping, and sort. Avoid encoding critical state only in ephemeral client memory; deep links and reload should reconstruct the intended path when permissions and data still allow it.

Drill-through and drill-down are different. Drill-down changes aggregation within a semantic hierarchy; drill-through opens contributing entities or records. Label them by outcome rather than forcing users to learn hidden gesture differences.

When context cannot transfer exactly, stop and disclose the discontinuity. A target dataset may lack a dimension, a permission boundary may hide some contributing rows, or a derived metric may not reconcile one-to-one. Showing a detail table that sums to a different total without explanation destroys analytical trust.

## Orientation and Return
Return should restore the prior analytical state, including scroll/selection when useful, without replaying stale assumptions. If data refreshed between levels, communicate whether the parent view will reflect the new snapshot. A back button that reconstructs a different filter state is not continuity.

## Evidence
Trace a real drill path with known values and verify population invariants at each edge. Include hierarchical drill, record drill-through, unavailable detail due to permissions, late-arriving data, changed metric definition, browser back/forward, and copied deep link. Record expected reconciliation rules rather than only visual screenshots.

## Failure Modes
- Detail loses one of the parent filters.
- A derived aggregate pretends to reconcile directly to raw rows.
- Breadcrumbs list screens but omit analytical selections.
- Browser back returns to a fresh default instead of the prior state.
- Cross-permission drill makes missing rows look like zero-valued rows.
- The target grain changes without naming the new unit of analysis.

## Falsification
Select a known aggregate, drill two levels, then ask the user to reconstruct exactly which population is represented and why its total should or should not reconcile to the parent. Falsify if the answer requires memory of hidden steps, if copied links change the population, or if returning loses context.

## Recovery
Carry explicit context tokens, add reconciliation notes where grains differ, distinguish drill types, preserve meaningful back-stack state, and surface permission-induced incompleteness. If the product cannot prove a retained predicate, remove the implied continuity claim.

## Handoff
Filter inheritance coordinates with `designing-dashboard-filter-scope`; query execution tracing belongs to `designing-query-provenance-inspection`; lineage relationships belong to `designing-data-lineage-exploration`.

## Output Contract
Return a `drill-path-continuity-contract` containing `drill_edges[]`, `grain_transitions[]`, `retained_context`, `introduced_context`, `reconciliation_rules`, `analytic_breadcrumb_model`, `deep_link_state`, `return_behavior`, `permission_discontinuities[]`, `evidence[]`, and `recovery_actions[]`.