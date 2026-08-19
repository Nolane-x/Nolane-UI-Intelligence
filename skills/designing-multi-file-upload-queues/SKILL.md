---
name: designing-multi-file-upload-queues
description: Use when users transfer many files and need per-item state, aggregate progress, concurrency, ordering, pause/cancel/retry, and failure isolation without treating the batch as one indivisible operation.
---

# Designing Multi File Upload Queues

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns orchestration across multiple upload items. It is not simply a repeating file-uploader component. It defines queue identity, concurrency, aggregate progress, per-file outcomes, and what batch-level actions mean when some files succeed and others fail.

## Decision Boundary
Every selected file becomes a stable queue item with its own transfer and processing state. Define concurrency based on bandwidth/server constraints rather than starting hundreds of transfers at once. Aggregate progress should account for file sizes where meaningful; “5 of 10” can mislead when the remaining file is 90% of total bytes, while byte-weighted progress can hide server-processing time. Expose both when consequence warrants it.

Batch pause/cancel/retry must have precise scope. Canceling queued items is different from canceling active server sessions, and already completed files usually remain completed. Allow users to remove or reorder pending items only when it has actual effect. Duplicate detection and naming conflicts may resolve per item without blocking unrelated transfers.

## Failure Topology
- One failed file marks the entire batch failed despite nine successful uploads.
- The queue launches every file simultaneously and saturates the browser/network.
- “Cancel all” deletes files that already completed successfully.
- Aggregate progress jumps backward when a new large file is added without explanation.
- Retry duplicates already successful items because batch state is replayed wholesale.
- A naming conflict modal blocks all transfers even though only one item is affected.

## Falsification and Recovery
Test mixed sizes, hundreds of items, concurrency limits, add-during-transfer, per-item failure, batch pause/cancel, duplicate/conflict, retry, navigation away, and processing-after-upload. The design fails if the user cannot identify which items are durable versus provisional or if a batch action has surprising effects on completed files.

Recover by modeling stable per-item states, bounded concurrency, independent retry/conflict resolution, and aggregate progress derived from explicit semantics. Keep batch summary as an aggregation over item truth, never a separate competing state machine.

## Output Contract
Return `multi-file-upload-queue-contract` with queue-item identity/states, concurrency policy, aggregate progress semantics, batch/per-item actions, add/remove/reorder rules, partial-failure handling, conflict isolation, and queue verification scenarios.
