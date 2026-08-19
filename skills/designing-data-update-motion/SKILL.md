---
name: designing-data-update-motion
description: Use when charts, tables or analytical marks update over time and motion must preserve correspondence between old and new data without suggesting false trends, causal certainty or freshness.
---

# Designing Data Update Motion

## Parent Contract
**Required parent:** `designing-data-visualization`.

This specialist owns temporal transitions between two data-encoding states. It does not choose the chart, validate the dataset or decide whether an update is trustworthy.

## Decision Model
Start with correspondence. A bar representing category A can move/grow to its new value if category identity is stable. If categories are added, removed or reordered, animate membership and value change separately enough to avoid implying that one category transformed into another. For scatterplots and networks, stable entity keys are mandatory before moving marks.

Animation should improve change detection, not smooth away important discontinuity. A sudden step in a safety metric may need an immediate alert rather than a gentle interpolation. Missing data, revised historical data and new live samples are distinct events and should not share one transition grammar.

Time bases matter. If the display updates every second but receives five samples at once after reconnection, interpolating them as if they arrived live fabricates freshness. Show catch-up/recovery state explicitly or jump to current state with provenance.

Axes and domains can move. Coordinating mark and axis transitions is critical; moving both independently can make direction unreadable. In analytical work, sometimes holding the scale stable is more truthful even if marks move farther.

## Failure Topology
- Reordered categories morph into one another because animation keys use array index.
- Axis rescale makes a value increase look like a decrease.
- Reconnected data is animated as a smooth live stream, hiding a gap.
- Transitions delay the latest state and analyst decisions use stale visuals.
- Color-only flashes signal changed points.

## Falsification and Recovery
Test add/remove/reorder categories, domain changes, missing intervals, corrected history, burst updates, filters and reduced motion. Freeze intermediate frames and ask whether a reasonable viewer could infer a trend or identity that the data does not support. If yes, the motion fails.

Recover by stabilizing keys/scales, separating update classes, annotating gaps/revisions, shortening or removing interpolation and preserving explicit timestamps/freshness.

## Output Contract
Return `data-update-motion-contract` containing entity correspondence, update classes, scale policy, temporal freshness, add/remove/change transitions, burst behavior, accessibility/reduced-motion equivalent and truth-preservation tests.