---
name: designing-nonvisual-chart-equivalents
description: Use when a visualization communicates relationships, trends, outliers, or comparisons that need an equivalent analytical path for users who cannot perceive the chart geometry.
---

# Designing Nonvisual Chart Equivalents

## Parent Contract
**Required parent:** `designing-data-visualization`.

This faculty owns an equivalent route to the analytical meaning of a chart without requiring sight of marks, axes, or spatial position. It does not require replacing every chart with a giant raw-data table. The equivalent should preserve the questions and findings the visualization supports: comparison, trend, extrema, distribution, or exact lookup.

## Decision Boundary
Start with the chart's analytical task. A trend chart may need a concise trend summary plus navigable data points; a categorical comparison may work with a sorted accessible table; a dense scatterplot may need filters, summaries, and outlier lists rather than thousands of sequential points. Provide underlying exact values when users need them, but do not pretend a CSV download is the only accessible experience.

Expose chart title, scope, units, series identity, notable annotations, and current filters. Interactive charts need keyboard/nonvisual equivalents for selecting series, changing ranges, and inspecting values. Generated narrative summaries must be bound to the same data state and should distinguish computation from editorial interpretation.

## Failure Topology
- The only alternative text says “chart showing sales” and omits the actual analytical result.
- A 5,000-point visualization is flattened into a 5,000-row screen-reader sequence with no structure.
- An accessible data table contains stale values after filters change.
- Tooltips are the sole source of exact values and require pointer hover.
- Color-series names are exposed but units, time range, and filtering context are missing.
- A generated summary invents causal interpretation not present in the data.

## Falsification and Recovery
For each chart, state the user questions it supports, then attempt to answer them without viewing the marks. Test filtering, range changes, annotations, series toggles, keyboard inspection, and exported/printed states. The design fails if nonvisual users can access raw numbers but cannot efficiently reach the same material comparisons or findings.

Recover by matching equivalent structure to analytical task, adding summaries plus structured values, synchronizing alternatives with chart state, and providing non-pointer inspection controls. Keep provenance and units explicit so accessibility does not become a lower-trust data path.

## Output Contract
Return `nonvisual-chart-equivalent-contract` with analytical task, required summaries, structured value access, title/unit/filter context, interactive equivalence, synchronization rules, narrative-claim limits, and nonvisual question-answer verification cases.
