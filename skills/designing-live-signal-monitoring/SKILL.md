---
name: designing-live-signal-monitoring
description: Use when this specialist's decision ownership is materially in scope. Own high-frequency live signal views, including timebase, channel selection, buffering, triggering, freshness, dropped samples, freeze/inspect, and return-to-live behavior.
---
# Designing Live Signal Monitoring

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own continuous temporal inspection of incoming measurement signals. Decide visible time window, sampling/display decimation, channel overlays, trigger/freeze behavior, buffer state, dropped-data cues, cursor inspection, and transitions between live-follow and historical inspection. This differs from generic charting because source cadence and temporal control are operational state.

## Inputs and evidence

Require sampling rate, display update rate, buffer length, channel count, units/scales, trigger capabilities, transport latency, dropped-sample metadata, clock source, synchronization across channels, and performance limits. Determine whether users need exact sample values or only trends during live observation.

## Procedure

Separate acquisition rate from display refresh. Show the current timebase and whether the view is following live data, paused/frozen, delayed, or disconnected. Decimation/aggregation should preserve important transients or disclose when it may hide them. Multi-channel overlays require unit/scale compatibility or explicit axes. Trigger events should remain inspectable without immediately scrolling away. When users pan into history, stop auto-follow and provide an obvious return-to-live control. Surface dropped samples, buffer overruns, and clock gaps as data-quality events, not invisible rendering glitches.

## Failure topology

Failures include charts that look live while frozen, auto-follow fighting manual inspection, downsampling erasing spikes, different units sharing an unlabeled axis, dropped samples drawn as continuous lines, and reconnect joining two time ranges without a visible gap. Another failure is refreshing so rapidly that labels and controls become unreadable while providing no analytical benefit.

## Falsification

Reject if users cannot identify live versus historical mode; if a known data gap renders as continuous signal; if decimation method/window is unknowable when transients matter; if mixed units can be miscompared; if manual pan cannot suspend follow; or if return-to-live loses the selected channels/timebase unexpectedly.

## Output contract

Return a `live-signal-monitoring-contract` with: acquisition/display rates; timebase; live/frozen/history/disconnected states; channel/axis rules; decimation; trigger markers; buffer status; data-gap/dropped-sample cues; cursor inspection; follow suspension; and return-to-live behavior. Include one buffer-overrun scenario.

## Handoffs

Waveform analysis owns detailed measurement operations on selected ranges, spectrum analysis handles frequency domain, telemetry dashboards summarize channels, and experiment run control supplies run phase/context.