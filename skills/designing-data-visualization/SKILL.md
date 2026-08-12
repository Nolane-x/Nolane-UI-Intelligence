---
name: designing-data-visualization
description: Use when a UI must communicate quantitative magnitude, trend, distribution, relationship, composition, uncertainty, comparison, or change through charts or other visual encodings.
---

# Designing Data Visualization

## Overview
Choose a visualization from the analytical question and data semantics, then make the encoding truthful, legible, and accessible. Decorative charts are not evidence.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the decision users must make, data types/units, sampling/uncertainty, comparison groups, update behavior, and accessibility constraints.

## Start with the question
State the dominant question:
- compare magnitude
- track trend/change
- inspect distribution/outliers
- understand part-to-whole
- reveal correlation/relationship
- locate spatial pattern
- inspect flow/network
- monitor threshold/status

If there is no user question, reconsider whether a chart is needed.

## Encoding hierarchy
Prefer precise position on a common scale for exact comparison. Length is strong for magnitude. Angle/area/color intensity are weaker and should be used when the task tolerates lower precision or the semantic form justifies them.

Avoid 3D perspective when it distorts value comparison.

## Scales and axes
- Use zero baselines when magnitude interpretation depends on length/bar baseline; document justified exceptions.
- Avoid dual axes unless the relationship and scales cannot be communicated more honestly with aligned small multiples or normalization.
- Label units and time zone/context.
- Show gaps/missing data distinctly from zero.
- Do not smooth data in a way that hides material variation without making the transformation explicit.

## Context and uncertainty
Rates often need denominator/sample size. Forecasts need confidence/uncertainty. Partial current periods need differentiation from completed periods. Estimated/imputed values should not look identical to measured facts.

## Color
Choose categorical, ordinal, sequential, or diverging scales according to data semantics. Status palettes and series palettes should not collide. Use direct labels, line style, markers, annotations, or texture where color alone is insufficient.

## Annotation
Annotate what changes the decision: thresholds, events, anomalies, targets, definitions. Do not label every point if it reduces pattern recognition. Tooltips supplement; they should not be the only path to critical values for keyboard/touch/assistive users.

## Interaction
For zoom, brush, hover, selection, filtering, drill-down, and linked views define keyboard/touch alternatives where relevant and make the active filter/range visible. Preserve user context when data refreshes.

## Small multiples and dashboards
Use aligned small multiples when comparing series with similar structure; repeated mini charts should share scales when comparison requires it. Do not place unrelated KPIs in same-sized cards simply to fill a grid.

## Accessibility
Provide a semantic/textual equivalent suitable to the analytical task: data table, summary, direct labels, or accessible chart structure. The equivalent must expose the insight/data users need, not just “line chart showing sales.”

## Output: `data-viz-contract`
Return `analytical_question`, `data_semantics`, `chosen_encoding`, `rejected_encodings`, `scales_axes`, `uncertainty`, `color_encoding`, `annotations`, `interaction`, `refresh_behavior`, `accessible_equivalent`, and `truthfulness_risks`.
