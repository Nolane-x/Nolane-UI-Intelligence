---
name: designing-cloud-sync-status
description: Use when local and remote file state synchronize asynchronously and users need truthful cues for current, uploading, downloading, offline, conflicted, paused, unavailable, or error states without false “saved” reassurance.
---

# Designing Cloud Sync Status

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns synchronization visibility between local and remote representations. It does not implement conflict resolution generally; it makes sync state and durability understandable at file, folder, and aggregate levels.

## Decision Boundary
Define what “synced” means: local changes durably accepted by remote authority and required remote changes applied locally. Separate locally saved from remotely synchronized. Track direction—uploading local change versus downloading remote update—when that affects user decisions. Offline changes may be safely queued, blocked, or local-only depending on product architecture; label the actual guarantee.

Aggregate indicators should not hide one critical conflicted/error item inside thousands of clean files. Provide drill-down from global status to affected objects. Sync icons need accessible labels and should not animate continuously for low-value background polling. If remote processing follows transfer, keep “sync complete” distinct from “processing/indexing complete.”

## Failure Topology
- “Saved” appears after local disk write although remote sync failed.
- Global green check hides one unsynced high-value document.
- Downloading remote change is shown with the same arrow/icon as uploading local edits, confusing direction.
- Offline badge disappears while queued changes still have not reached remote storage.
- App retries forever with no visible item-level error.
- Folder aggregate count includes deleted/ignored files inconsistently.

## Falsification and Recovery
Test edit while online/offline, reconnect, simultaneous remote update, server rejection, partial folder errors, app restart, large backlog, and processing-after-sync. Compare UI status to remote durability. The design fails if users can close/delete local data under a false belief that remote synchronization completed.

Recover by separating local save/remote sync/processing states, showing direction and actionable errors, escalating aggregate anomalies, and retaining queued-offline provenance until acknowledgment. Use stable file identity to reconcile later.

## Output Contract
Return `cloud-sync-status-contract` with sync-state taxonomy, local-versus-remote durability, direction, offline queue semantics, aggregate/drill-down behavior, error/retry visibility, processing separation, and synchronization verification cases.
