---
name: designing-metrics-exploration
description: Use when operators inspect time-series metrics and need to reason about aggregation, dimensions, units, rate versus count, comparison windows, missing data, cardinality, and alert context without treating charts as self-explanatory truth.
---

# Designing Metrics Exploration

## Parent Contract
**Required parent:** `designing-data-visualization`.

This faculty owns exploratory interaction with aggregated measurements over time. It does not own trace-level causality or raw event logs. Metrics compress many events, so the interface must expose aggregation and unit semantics strongly enough that operators do not mistake a derived series for raw ground truth.

## Decision Architecture
Every series needs a metric identity, unit, aggregation, dimensions, and time resolution. A counter displayed as a raw cumulative number differs from its rate; a latency histogram differs from an average; CPU percent requires a denominator. Legends and query summaries should preserve these semantics rather than showing only short labels such as `requests` or `p95` without scope.

Time range and resolution must cooperate. Long windows may require downsampling; the viewer should disclose resolution changes that can hide spikes. Comparison periods—previous hour, previous week, deployment baseline—must use aligned timestamps and clear styling. Missing samples, zero values, and no-data periods are not interchangeable and should render differently where the distinction matters.

Dimension filtering can create cardinality explosions. Let users inspect service, region, endpoint, version, host, or other meaningful labels without accidentally requesting thousands of series that make both backend and chart unusable. Top-N or aggregation fallback is acceptable when explicit. Alert overlays, deployments, incidents, or annotations can provide context but cannot establish causality by mere temporal overlap.

## Failure Topology
- Counter is graphed cumulatively but labeled “requests/sec.”
- Downsampled 24-hour view hides a five-minute outage with no indication resolution changed.
- Missing telemetry is drawn as zero and suggests the service was healthy but idle.
- Selecting `host=*` produces 20,000 lines and freezes chart/query backend.
- Dual y-axes visually imply correlation between unrelated units.
- Deployment marker appears near a spike and UI labels deployment as the cause without evidence.

## Falsification and Recovery
Falsify with counter resets, sparse data, no-data intervals, histogram percentiles, long-range downsampling, high-cardinality dimensions, comparison periods across DST, alert/deployment overlays, keyboard/screen-reader data access, and a backend returning approximate aggregates. The design fails if users cannot determine unit/aggregation/resolution for a visible series or distinguish zero from missing evidence.

Recover by keeping metric semantics visible, differentiating no-data states, exposing resolution/downsampling, bounding dimension cardinality, avoiding unjustified dual-axis comparisons, and treating contextual overlays as investigation cues rather than causal conclusions.

## Output Contract
Return `metrics-exploration-contract` with metric/unit/aggregation semantics, time range/resolution, downsampling disclosure, dimension filtering, cardinality controls, zero-vs-missing behavior, comparison windows, contextual overlays, accessible data representation, and falsification cases.