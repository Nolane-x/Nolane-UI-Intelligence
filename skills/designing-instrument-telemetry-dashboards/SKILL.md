---
name: designing-instrument-telemetry-dashboards
description: Use when this specialist's decision ownership is materially in scope. Own dense instrument telemetry overviews that preserve units, freshness, quality, alarm relevance, scale, and drill-down without turning measurements into decorative KPI cards.
---
# Designing Instrument Telemetry Dashboards

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the overview surface for many instrument measurements and states. Decide channel grouping, current-value presentation, trend context, units, quality/freshness, alarm emphasis, sparklines or summaries, update cadence, and drill-down. This owner does not set control values or define scientific interpretation; it makes telemetry legible and trustworthy under density.

## Inputs and evidence

Require channel catalog, units and ranges, nominal bands, sampling/update rates, quality flags, alarm relationships, instrument hierarchy, expected channel count, user tasks, and display latency. Determine which measurements are primary operational indicators versus specialist diagnostics, and whether values are directly measured or derived.

## Procedure

Group telemetry by instrument subsystem or operator task, not arbitrary card count. Every value retains unit and freshness; if space is constrained, abbreviate labels before removing units or quality state. Use visual prominence for actionable deviation, not for whichever number is largest. Tiny trends should communicate recent direction only when time window and scale can be recovered. Allow drill-down to signal history and provenance. Missing, stale, saturated, clipped, invalid, and estimated values require distinct states. Update at a rate users can perceive and act on; do not repaint faster merely because the source samples faster.

## Failure topology

Failures include dozens of equal cards, stale values looking live, engineering notation truncated into ambiguous numbers, auto-ranging sparklines making stable and unstable channels appear alike, derived values indistinguishable from sensors, and alarm colors used without text/icon/state. Another failure is hiding channel quality until drill-down, causing operators to act on invalid measurements.

## Falsification

Reject if a visible value lacks recoverable unit or timestamp/freshness; if invalid and valid measurements can look identical; if trend scales cannot be interpreted; if alerting channels are lost among equal visual weight; if a derived estimate looks like direct sensor evidence; or if update animation makes values harder to read than the underlying change warrants.

## Output contract

Return an `instrument-telemetry-dashboards-contract` with: channel grouping; value/unit formatting; freshness/quality vocabulary; update cadence; nominal/alarm cues; trend-window/scale disclosure; derived-versus-measured distinction; drill-down links; density/aggregation rules; and stale/missing behavior. Include one 100-channel degraded-data specimen.

## Handoffs

Live signal monitoring handles high-frequency temporal inspection, process trends handle longer operational history, alarm-threshold owners define threshold semantics, and the instrumentation root supplies identity and connection state.