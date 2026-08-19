---
name: designing-time-series-exploration
description: Use when users inspect values over time and the interface must coordinate temporal zoom, brush selection, aggregation resolution, gaps, timezone, live updates and precise cursor comparison.
---

# Designing Time-Series Exploration

## Parent Contract
**Required parent:** `designing-data-visualization`.

This faculty owns interaction for exploring temporal data. It does not validate the measured phenomenon, choose statistical smoothing or define scheduling/calendar input.

## Decision Boundary
Model the visible time domain explicitly: start, end, timezone/display zone, sampling or aggregation resolution, and whether the right edge is fixed to “now.” Panning or zooming changes domain; changing aggregation changes representation. Do not let one gesture silently alter both without exposing the consequence.

Temporal resolution must follow available density and analytical intent. A year view may aggregate by day or week; a five-minute view may show raw seconds. Label aggregation and avoid connecting sparse/missing samples as if continuous. Distinguish **zero**, **no observation**, **delayed observation** and **outage** where the data source supports those states.

Crosshair/cursor comparison should reveal exact timestamp/value and snap according to series semantics. Multiple series may have samples at different times; do not fabricate simultaneous values by careless nearest-neighbor matching. If interpolation is used, label or otherwise bound it.

Brush/range selection can zoom, filter peers or define an analysis interval. Make the mode explicit and provide numeric/date access for precise ranges. Wheel/pinch zoom must preserve a sensible temporal focal point and not trap page scrolling unexpectedly.

Live mode needs a clear paused/resume contract. Once a user pans into history, decide whether auto-follow stops. New data should not keep yanking the viewport back to now. A “Return to live” control can restore the real-time edge.

## Failure Topology
- DST transition produces duplicate/missing hour labels with no timezone context.
- Missing samples are connected by a line and look like measured stability.
- Panning history is repeatedly overridden by auto-follow live updates.
- Zoom changes aggregation granularity and apparent volatility without disclosure.
- Crosshair compares series at different timestamps as if simultaneous.
- Brush selection has no keyboard or form-based equivalent for exact intervals.

## Falsification and Recovery
Falsify across DST boundaries, timezone changes, missing/bursty samples, large date ranges, live-to-history transitions, multiple sampling rates and keyboard-only exploration. Reconcile tooltip/cursor timestamps to source samples.

Recover by making domain/resolution/timezone first-class, breaking lines over unknown intervals, pausing live-follow on exploration and exposing exact range controls.

## Output Contract
Return `time-series-exploration-contract` with time-domain model, timezone, resolution/aggregation, gap semantics, pan/zoom/brush interactions, cursor alignment, live-follow state, exact-input accessibility and temporal edge tests.