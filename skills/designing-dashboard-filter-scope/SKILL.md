---
name: designing-dashboard-filter-scope
description: Use when dashboard filters can apply to different tiles, tabs, datasets, time ranges, or drill contexts and users must see exactly where each filter is effective before interpreting results.
---

# Designing Dashboard Filter Scope

A filter is part of the meaning of every number it affects. Filter interfaces fail when they optimize control compactness while hiding scope, inheritance, exclusions, or interaction with tile-local conditions.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent establishes analytical context continuity. This skill owns the mapping from filter intent to affected dashboard regions and the presentation of that mapping.

## Scope Topology
Model scope as explicit edges: filter → target tile/query/section. Do not infer scope solely from visual proximity. A filter in a global header can still exclude specific tiles, and a local panel filter can affect a nested drill result. Store and expose the actual target set.

Distinguish global dashboard filters, section filters, tile-local filters, cross-filter interactions, hidden default constraints, and security filters. Security predicates are not user-removable filters and should not be rendered as ordinary chips, but the interface may need to communicate that the visible dataset is permission-constrained.

When a filter cannot apply to a tile because of incompatible dimensions, decide explicitly whether to exclude the tile, translate the filter through a semantic mapping, disable the control, or surface a warning. Silent partial application is the most dangerous default because a dashboard still looks coherent.

Order and composition matter. Expose whether multiple filters combine with AND/OR semantics, whether empty selection means all or none, and whether a tile overrides a global time window. For relative dates, show evaluated bounds when users investigate historical snapshots.

## Interaction Rules
Highlight affected regions when editing filter scope. In consumption mode, make scope inspectable without permanent clutter; a user should be able to answer “why did this tile not change?” directly from the dashboard. Preserve scope through drilldowns only when the target analytical context can represent it faithfully.

## Evidence
Build cases with global filters, excluded tiles, semantic aliases, tile-level overrides, cross-filtering, and an incompatible target. Record the effective filter set for each tile and compare it with what the UI communicates. Test reset, bookmark/share, saved view, dashboard duplication, and edit/publish transitions.

Evidence is strongest when a machine-readable scope graph and rendered state agree. A screenshot with filter chips alone cannot prove application.

## Failure Modes
- A global-looking filter silently skips tiles.
- A local filter leaks into unrelated analyses.
- Filter chips show labels but not effective values or operators.
- Reset removes visible filters while hidden defaults remain unexplained.
- Cross-filter selections survive navigation after their source context disappears.
- Relative time scope changes after reopening a historical shared link without disclosure.

## Falsification
Create three tiles where one is compatible, one requires semantic translation, and one cannot accept the filter. Ask users to predict the outcome before applying it. Falsify the design if the actual target set differs from the understandable target set or if two analysts can read the same dashboard state and infer different populations.

## Recovery
Expose target mapping, introduce incompatibility states, distinguish user filters from policy constraints, and make composed operators explicit. If translation is approximate, present that approximation rather than treating it as an exact shared filter.

## Handoff
Use `designing-cross-filtering` for chart-to-chart selection behavior, `designing-semantic-metric-browsing` for dimension compatibility, and `designing-dashboard-edit-view-modes` for persistence scope. This skill owns where filters apply, not the visual encoding of filtered data.

## Output Contract
Return a `dashboard-filter-scope-contract` with `scope_graph`, `filter_classes[]`, `target_compatibility`, `composition_rules`, `override_policy`, `security_filter_boundary`, `inspection_behavior`, `persistence_rules`, `evidence_matrix[]`, `falsification_cases[]`, and `recovery_actions[]`.