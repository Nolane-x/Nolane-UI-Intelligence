---
name: designing-process-control-trend-views
description: Use when this specialist's decision ownership is materially in scope. Own process trend interfaces that relate measured variables, setpoints, control outputs, events, limits, batches, and operating modes over time without confusing correlation with control causality.
---
# Designing Process Control Trend Views

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own historical/near-live trend analysis for controlled engineering processes. Decide aligned time axes, process variables, setpoints, controller outputs, operating modes, alarm/event overlays, limit bands, batch boundaries, comparison windows, and navigation from overview to a disturbance. This owner does not tune controllers.

## Inputs and evidence

Require tagged process variables and units, sampling/aggregation, setpoint history, actuator/controller outputs, operating modes, alarm/event records, batch/run boundaries, quality flags, and expected analysis windows. Identify channels with different sample rates or delays.

## Procedure

Align signals on one authoritative time basis while preserving gaps and quality flags. Visually distinguish measured variable, setpoint, and control output even if they share a scale. Mode changes and operator actions should be event markers, not inferred from line changes. Allow users to bracket a disturbance and compare pre/during/post windows. Aggregation at long time ranges must preserve extrema when safety excursions matter. Batch boundaries and maintenance periods should be optional overlays. Cross-signal lag should be inspectable without claiming causality merely because traces align.

## Failure topology

Failures include setpoint and measured value sharing indistinguishable line styles, data gaps interpolated as real process behavior, long-range averaging hiding excursions, events plotted at ingestion rather than event time, and mixed units on one axis. Another failure is automatic causal language based only on correlated trends.

## Falsification

Reject if a viewer cannot distinguish setpoint from measurement without color; if known gaps become continuous lines; if aggregation can hide threshold exceedance; if event timestamps are uncertain but plotted as exact; if incompatible units are overlaid without axes; or if the UI labels one signal as cause based solely on temporal correlation.

## Output contract

Return a `process-control-trend-views-contract` with: signal roles; units/axes; time alignment; quality/gap handling; setpoint/control-output distinction; mode/action/alarm overlays; aggregation/extrema policy; batch boundaries; disturbance-bracketing; lag inspection; and causality-language constraints. Include one hidden-excursion aggregation test.

## Handoffs

Setpoint controls own changes, alarm thresholds own events, live signal monitoring handles short windows, and experiment/batch provenance supplies run boundaries.