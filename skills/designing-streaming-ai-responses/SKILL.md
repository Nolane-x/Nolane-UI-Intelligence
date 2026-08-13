---
name: designing-streaming-ai-responses
description: Use when model or tool output arrives incrementally, takes noticeable time, can revise earlier content, invokes tools, or exposes partial results before the final answer or artifact is stable.
---

# Designing Streaming AI Responses

## Overview
Streaming is a temporal state machine, not a typing animation. Make partial content usable without implying finality, preserve the reader’s place, and represent tool/action progress separately from generated prose.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require expected latency distribution, output structure, whether earlier chunks can change, tool phases, cancellation semantics, persistence, and what counts as complete. Coordinate with generic latency/progressive feedback.

## Decision Model
Define states: queued, model-starting, streaming content, waiting on tool, receiving tool result, synthesizing/revising, complete, cancelled, failed, partial-recoverable. The UI must expose meaningful state transitions without exposing implementation noise.

Stability is a design constraint. Do not continuously reflow or replace paragraphs the user is reading. Use stable anchors, append-first behavior, section reservation, or explicit “revising” boundaries. When citations or tool results arrive late, attach them without scrambling the reader’s locus unless correctness demands revision; if text changes materially, make that change legible.

Distinguish “stop generating” from undoing already executed tool actions. Cancellation should state what stopped and what external changes remain. Preserve partial useful output when safe, and offer retry from the failed stage rather than deleting everything.

Streaming controls need accessible status. Screen readers should not announce every token; batch semantic updates. Autoscroll follows only when the user remains at the tail; once the user scrolls upward, new content should not drag them away. Show a clear completion transition so a half-finished answer cannot be mistaken for final.

## Evidence
Test slow/fast models, long tool calls, late citations, partial failures, cancellation at each phase, reconnect, user scrolling away from tail, screen-reader announcements, tab/background return, and persisted thread reload. Measure layout churn and duplicated action risk.

## Output Contract
Return a `stream-contract` with `states[]`, `state_transitions`, `stability_strategy`, `tool_progress_model`, `autoscroll_policy`, `partial_output_policy`, `cancel_semantics`, `retry_semantics`, `accessible_status_batching`, `completion_signal`, and `streaming_tests[]`.

## Failure Traps
- Token-by-token live-region announcements.
- Earlier paragraphs constantly changing while read.
- Stop button implying already sent emails or tool calls were undone.
- Infinite spinner during tool execution with no phase information.
- Forced autoscroll after the user inspects earlier content.
- Failure erasing useful partial output.
- No clear distinction between partial and complete answer.

Streaming should reduce perceived waiting without increasing state ambiguity.

## V6 Streaming AI Protocol
Set a **token-stream commitment boundary**: partial text is provisional until claims, citations, tool results, or structured outputs reach the necessary validation state. Maintain **partial-answer stability** so text above the reading cursor does not continually rewrite without explanation.

Represent **tool-call transition** distinctly from narrative generation—queued/running/succeeded/failed/cancelled with scope. Support **citation-late-binding** without temporarily attaching unsupported sources to claims. Define **stream-cancel semantics**: what generation/tool work actually stops, what partial output remains, and whether follow-up can safely continue.

### Falsification
Cancel mid-tool, delay citations, revise an earlier claim, reconnect after stream interruption, and scroll while tokens arrive. False completed-state/provenance invalidates streaming behavior.

### Recovery
Mark partial output provisional, reconcile tool state, attach citations only after binding, and restart from a stable checkpoint rather than duplicating actions.
