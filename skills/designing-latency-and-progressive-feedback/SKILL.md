---
name: designing-latency-and-progressive-feedback
description: Use when an action, navigation, save, upload, computation, AI call, sync, or remote operation can take long enough that users may wonder whether input was received, repeat an action, abandon, or lose state.
---

# Designing Latency and Progressive Feedback

## Overview
Latency is interaction state. A system must acknowledge intent quickly, represent what is actually happening, prevent unsafe duplicate actions, and provide cancel/retry/recovery semantics appropriate to whether work is local, queued, or externally committed.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require operation type, latency distribution, idempotency, cancellability, external side effects, progress measurability, background capability, and failure states. AI token streaming routes additionally to its specialized stream contract.

## Decision Model
Design three time horizons. **Immediate acknowledgement:** pressed/pending state or local optimistic result confirms the input was received. **Progress period:** explain what is happening at the right granularity. **Terminal transition:** success, partial success, failure, cancelled, or unknown outcome must be explicit.

Choose optimistic UI only when the action is likely to succeed and rollback is cheap/understandable. For financial, destructive, or externally uncertain operations, premature success creates serious ambiguity. Indeterminate progress is acceptable when true progress is unknowable; fake percentages are not. When progress is measurable, show meaningful units or stages rather than an animated bar disconnected from work.

Protect against duplicate intent. Disable or transform the initiating control only if users can still understand/cancel the state; server-side idempotency remains necessary for consequential operations. If the UI loses network after commit, distinguish failed from unknown. Blind retry can duplicate side effects.

Long work may move to background. Preserve a durable job record, notify appropriately, and let users leave/return without losing status. Cancellation semantics state whether work stops immediately, after current stage, or cannot undo external changes already made.

## Evidence
Test interaction responsiveness, slow/fast networks, duplicate input, navigation away/back, browser/app backgrounding, cancel at each phase, timeout, unknown response after commit, retries, screen-reader status, and layout stability. For web, field responsiveness such as INP can reveal feedback blocked by main-thread work but does not replace task-state correctness.

## Output Contract
Return a `latency-contract` with `operation_states`, `acknowledgement_budget`, `optimistic_policy`, `progress_model`, `duplicate_protection`, `background_job_model`, `cancel_semantics`, `timeout_policy`, `unknown_outcome_recovery`, `terminal_feedback`, and `latency_tests[]`.

## Failure Traps
- Button remains unchanged for seconds after click.
- Fake 73% progress with no measurable basis.
- Optimistic “Saved” before a high-risk remote commit.
- Disabled button with no way to understand or cancel work.
- Retry offered when prior transaction status is unknown.
- Spinner lost when user navigates away, along with job status.
- Cancellation visually claims rollback of an already executed external action.

Fast-feeling UI comes from timely truthful feedback, not merely animation.

## V6 Latency Perception Protocol
Classify operations by **latency perceptual threshold**: instant/local feedback, short wait needing activity acknowledgment, longer wait needing progress/context preservation, and background job. Use a **progress truth model**—determinate progress only when the system has meaningful completion fractions; otherwise expose stage/status rather than a fake percentage.

Declare the **optimistic boundary** for updates that may safely appear before server confirmation. Ensure **cancellation responsiveness**: cancellation must acknowledge immediately, state whether work actually stopped, and handle late completion. Support **long-task backgrounding** with durable job identity, notification/re-entry, result provenance, and retry semantics.

### Falsification
Inject variable latency, stalled progress, late success after cancel, and app/window closure. If UI feedback implies execution facts it does not know, the model is false.

### Recovery
Revert speculative state, expose actual job stage/uncertainty, background safely, and preserve a clear re-entry path instead of freezing the user behind a spinner.
