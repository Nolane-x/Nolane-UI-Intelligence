---
name: designing-log-viewers
description: Use when operators inspect high-volume timestamped event records and the interface must preserve chronology, source, severity, structured fields, tailing, filtering, retention, truncation, and copy/export safety.
---

# Designing Log Viewers

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns inspection of event/log streams. Logs are discrete records emitted by systems; they are not traces, which connect causal spans, or metrics, which aggregate measurements over time. The viewer should preserve raw evidence while helping operators reduce volume without changing the meaning of the underlying event stream.

## Decision Architecture
Define the canonical event schema: timestamp with timezone/precision, source/service, environment, severity when trustworthy, message, structured fields, correlation IDs, and ingestion metadata. Preserve original event order evidence when ingestion order can differ from event time. If clocks can skew, do not imply perfect chronology from timestamp alone.

Tailing and historical exploration need different behavior. In live-tail mode, new events can append while the user follows the edge; once the user scrolls away or selects text, stop auto-follow and surface a clear “resume live” control. Historical queries should have bounded time ranges, result limits, and stable anchors so loading older/newer records does not move the selected event.

Filtering must distinguish client-side view filtering from backend query constraints. Search highlighting should not alter the raw message. Structured-field expansion, line wrapping, JSON formatting, and stack-trace folding can improve readability but users need access to the original record for copy/export. Redaction policies must apply consistently to display, copy, share, and downloaded logs.

## Failure Topology
- Live tail keeps snapping to bottom while an operator is reading an earlier error.
- Viewer sorts by ingestion order but labels it as event chronology despite clock/queue delays.
- Client-side filter hides events but query cost still scans an enormous backend range with no indication.
- Pretty-printed JSON changes whitespace/escaping and copied output is mistaken for raw evidence.
- Secret values are redacted on screen but exposed in Copy raw or export.
- Rendering an unbounded stack trace or million-line result freezes the browser.

## Falsification and Recovery
Falsify with high event rate, out-of-order ingestion, clock skew, multiline stack traces, structured JSON, live-tail pause/resume, broad time query, secret redaction, keyboard selection/copy, screen-reader table/list navigation, and a source that stops emitting. The design fails if the operator cannot tell whether they are viewing raw versus transformed evidence or if following live data prevents stable historical inspection.

Recover by preserving canonical records, exposing ordering basis, separating live follow from historical mode, bounding query/render volume, making filter scope explicit, maintaining raw-view access, and applying redaction through every egress path.

## Output Contract
Return `log-viewer-contract` with event schema, ordering/time semantics, live-tail state, historical query model, filtering/search scope, structured/raw representation, selection/anchoring, redaction/export policy, rendering limits, accessibility behavior, and falsification cases.