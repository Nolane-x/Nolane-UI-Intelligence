---
name: designing-retry-and-recovery-actions
description: Use when a failed operation needs an actionable recovery path and the UI must choose safe retry scope, preserve intent, prevent duplication, and offer alternatives when retry cannot solve the cause.
---

# Designing Retry and Recovery Actions

## Parent Contract
**Required parent:** `designing-empty-loading-error-states`.

This faculty owns the action model after failure. It does not own generic error wording or guarantee that every failure is retryable. A retry control is valid only when repeating an operation has defined semantics and the failure class plausibly changes on repetition.

## Decision Boundary
Classify failures before offering actions. Transient transport/service errors may justify Retry. Validation errors require correction. Permission failures require access change. Quota exhaustion may require waiting or plan change. Conflicts need resolution. A generic “Try again” on every error teaches users to hammer deterministic failures.

Preserve the operation intent needed for recovery: inputs, target IDs, selected objects, upload handles, or draft state. If retry can duplicate side effects, require idempotency keys or a server status check before repeating. The UI should communicate scope—“Retry 3 failed uploads” is safer than “Retry all.”

Recovery alternatives matter. Provide Save draft, Download unsent data, Copy error details, Change connection, Request access, Edit inputs, or Contact support only when they actually address the failure. After success, reconcile state and remove stale failure banners; do not leave users wondering whether the retry created a second object.

## Failure Topology
- “Retry” repeats a non-idempotent purchase after a timeout with unknown server outcome.
- Validation failure offers retry instead of returning focus to invalid input.
- Retrying one failed item resubmits the entire batch.
- Recovery clears the user’s inputs before the new attempt begins.
- Success after retry leaves both old error and new success state visible.
- Exponential backend rate limiting is hidden behind a button users can press continuously.

## Falsification and Recovery
Falsify with timeout after server commit, deterministic validation failure, permission denial, rate limit with retry-after, offline state, partial batch failure, expired upload token, and recovery success after one or more failed attempts. The design fails if action labels do not correspond to a failure class or if repeating an operation can create unbounded duplicate side effects.

Recover by mapping failure taxonomy to specific actions, preserving recoverable intent, checking authoritative operation status when outcome is unknown, using idempotent retry primitives, scoping retries narrowly, respecting retry-after/backoff, and reconciling recovered state atomically in the UI.

## Output Contract
Return `retry-recovery-action-contract` with failure classes, eligible recovery actions, preserved intent, retry scope, idempotency/status dependencies, backoff/rate-limit behavior, alternative recovery paths, post-success reconciliation, focus behavior, and falsification cases.