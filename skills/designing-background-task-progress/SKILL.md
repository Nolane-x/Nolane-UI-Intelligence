---
name: designing-background-task-progress
description: Use when work continues after the initiating surface is left and users need truthful task identity, progress, cancellation, completion, failure, and return paths across routes or sessions.
---

# Designing Background Task Progress

## Parent Contract
**Required parent:** `designing-latency-and-progressive-feedback`.

This faculty owns long-running operations that outlive the initiating interaction: exports, imports, renders, migrations, bulk updates, scans, deployments, or analysis jobs. It does not turn synchronous latency into a job system; backgrounding is justified when users should be able to continue elsewhere without losing task observability.

## Decision Boundary
Give every background task durable identity and a lifecycle grounded in backend state: queued, starting, running, paused, waiting for input, cancelling, cancelled, succeeded, partially succeeded, failed, expired. “Running” cannot be inferred merely because the client has not heard otherwise.

Choose progress evidence according to what the worker actually knows. If total work is measurable, report completed/total or meaningful phase progress. If not, show phase and liveness rather than a fake smooth percentage. Estimated time should be labeled as an estimate and allowed to change without appearing broken.

Users need a place to find tasks after navigation. That may be a task center, status region, or object-local job history. Completion can trigger a notification, but notification is not the task record. Cancellation must define whether it is immediate, best-effort, or unavailable after a commit phase; the UI should not promise cancellation while irreversible work continues.

## Failure Topology
- Closing the initiating modal makes the job impossible to find even though it keeps running.
- Progress advances to 95% using a timer rather than worker evidence and stalls there for minutes.
- “Cancel” hides the task locally while the backend continues committing changes.
- Page refresh creates a duplicate job because client state was mistaken for task identity.
- Partial success is displayed as complete success and failed items are lost.
- Completion notification links to a transient route that no longer exists.

## Falsification and Recovery
Falsify with route changes, browser refresh, reconnect after sleep, worker retry, unknown totals, partial failure, cancellation during an irreversible phase, task completion while the app is closed, and two concurrent jobs of the same type. The design fails if users cannot recover authoritative task state from identity alone or if displayed progress is synthesized without evidence.

Recover by persisting task IDs, sourcing lifecycle from the worker/service, exposing phase-based indeterminate progress when necessary, defining cancel authority, retaining result/failure summaries, and providing durable destinations for task history and outputs.

## Output Contract
Return `background-task-progress-contract` with task identity, lifecycle states, progress evidence, phase/ETA policy, discovery surface, cancellation semantics, reconnect/resume behavior, partial-success representation, completion routing, notification handoff, and falsification cases.