---
name: designing-trace-exploration
description: Use when operators inspect distributed request traces and the interface must expose parent-child causality, timing, critical path, service boundaries, errors, attributes, missing spans, and navigation without reducing traces to colored timelines.
---

# Designing Trace Exploration

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns causal exploration of spans belonging to one distributed trace. It does not own raw log browsing or aggregate metrics. A trace explains how one request or operation propagated across components, with imperfect instrumentation and potentially missing evidence.

## Decision Model
Represent each span with stable identity, parent relation, service/operation, start/duration, status/error evidence, attributes/events, and links where the tracing model supports them. Timeline geometry helps reveal concurrency and latency but must remain synchronized with an inspectable tree or list so nested causality is not encoded only through pixels.

Highlight critical-path candidates cautiously. The longest visible span is not automatically the root cause, and missing instrumentation can make apparent gaps ambiguous. Distinguish self time from child time when supported, and show clock-skew or incomplete-trace warnings instead of rendering impossible negative/overlapping durations as if exact.

Navigation should preserve the selected span while filtering or zooming. Operators commonly move from a trace to related logs, metrics, service topology, or another linked trace; carry correlation/time/service context rather than forcing a new search. Large traces need collapsing, search, and virtualization while keeping ancestors of matches visible.

## Failure Topology
- Waterfall makes a long parent span look slow although all duration is spent in known child work.
- Missing spans are visually connected as if causal continuity were proven.
- Clock skew produces negative offsets and the chart silently normalizes them.
- Filtering to error spans hides ancestors, so operators lose request path context.
- Clicking “View logs” opens a generic log page without trace ID or time window.
- Thousands of spans render as DOM rows and make zoom/selection unusable.

## Falsification and Recovery
Falsify with incomplete sampling, missing parent, clock skew, fan-out concurrency, thousands of spans, asynchronous links, nested errors, span search, cross-link to logs, keyboard navigation, screen-reader tree representation, and a trace whose critical service has no instrumentation. The design fails if visual ordering implies causal evidence absent from the trace model or if selected context is lost during exploration.

Recover by pairing timeline with structural hierarchy, marking missing/incomplete evidence, using model-supported self/child timing, preserving ancestor context under filtering, carrying correlation to adjacent observability tools, and virtualizing large traces.

## Output Contract
Return `trace-exploration-contract` with span schema, causal hierarchy, timeline semantics, incomplete/skew handling, critical-path evidence limits, filtering/search behavior, selection/zoom anchoring, observability cross-links, scale strategy, accessibility representation, and falsification cases.