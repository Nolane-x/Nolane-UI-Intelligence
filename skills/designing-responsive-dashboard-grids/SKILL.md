---
name: designing-responsive-dashboard-grids
description: Recompose dashboard cards and data regions across widths while preserving analytical priority, comparable scales, and stable user customization.
---

# Designing responsive dashboard grids

Dashboards combine cards that may tolerate different widths poorly. Use this skill when KPI tiles, charts, tables, alerts, and controls must reflow without turning analytical hierarchy into arbitrary masonry.

## Decision ownership

Own grid state, card minimums, span changes, order, grouping, row alignment, and behavior of user-resized or rearranged dashboards under constraint. Decide which cards may stack, expand, simplify, or move to secondary views.

## Inputs and evidence

Collect card content requirements, chart minimum plotting area, table columns, KPI comparison groups, alert priority, personalization state, common viewport sizes, and localization. Identify cards whose meaning depends on side-by-side comparison or shared scale.

## Procedure

Define card constraints from content, not equal-column aesthetics. Keep comparison groups adjacent where possible and avoid changing chart scales merely because a card narrows without signaling the change. Establish deterministic reflow order based on analytical hierarchy.

For personalized dashboards, preserve user intent while applying responsive normalization. A six-column arrangement may need a stable serialization into two columns; document the mapping and avoid overwriting the user’s desktop layout with the temporary mobile order.

Simplify chart annotations before shrinking the plot beyond legibility.

## Failure topology

Masonry layouts can reorder reading unpredictably as card heights change. Narrow cards may hide legends or change axes so comparisons become misleading. Another failure is persisting mobile auto-reflow as the user’s canonical arrangement, corrupting desktop personalization.

Equal card widths can waste space on KPIs while starving dense tables.

## Falsification

Test dashboards with long values, alerts, no-data states, many legends, and user-customized arrangements. Resize continuously and compare card order and chart semantics. Switch back to wide layout and verify prior user placement returns. Check keyboard reading order against visual order.

## Output contract

Produce a `responsive-dashboard-grids-contract` defining card constraints, span/order rules, comparison-group preservation, chart simplification policy, personalization mapping, reading order, and responsive regression scenarios.

## Handoffs

Use `designing-dashboard-composition` for analytical hierarchy, visualization skills for chart-specific adaptation, `designing-responsive-table-transformations` for embedded tables, and `verifying-responsive-state-parity` for data/action equivalence.