---
name: designing-file-transfer-and-storage
description: Use when files are durable product objects whose upload, download, synchronization, storage, naming, availability, and lifecycle need one coherent state model beyond a single file-picker control.
---

# Designing File Transfer and Storage

## Parent Contract
**Required parent:** `routing-ui-work`.

This faculty owns the product-level state model for file movement and persistence. Existing file-uploader components may collect bytes; this owner defines what a file becomes before, during, and after transfer, how local/remote state is represented, and how dependent operations behave while availability changes.

## Decision Boundary
Define canonical file identity separately from transfer attempt. A file can exist as a local candidate, queued transfer, partially transferred object, server-accepted object under processing, synchronized object, unavailable remote reference, or deleted/recoverable record. File name is not sufficient identity because duplicates and renames exist. Track size, type, checksum or equivalent integrity evidence, ownership, and availability only when product semantics require them.

Separate transfer state from processing state. Upload completion does not mean virus scanning, transcoding, indexing, or import succeeded. Download availability does not mean a local cache is current. Decide which actions are allowed in provisional states and how users resume or abandon incomplete work. Security/privacy owners still govern whether a file may be stored or shared.

## Failure Topology
- UI shows “Uploaded” when bytes arrived but processing later fails and the file is unusable.
- Retrying creates duplicate file objects because identity is tied to transfer attempt.
- Renaming during sync produces two divergent copies with no conflict model.
- A local cached file is presented as current after the remote version changed.
- Deleting a transfer row cancels visibility but leaves a partial object consuming storage.
- File name collisions overwrite an existing object without explicit product policy.

## Falsification and Recovery
Exercise new upload, retry, cancel, reconnect, rename, move, server processing, local cache, remote change, delete, restore, and download using duplicate names and large files. The design fails if users cannot distinguish transfer success from object readiness or if one logical file can fork silently into multiple identities.

Recover by centralizing stable file identity, separating transfer/processing/sync states, recording partial-object cleanup, and defining collision/reconciliation rules. Child specialists refine queues, conflicts, previews, quota, and other file concerns but share this canonical lifecycle.

## Output Contract
Return `file-transfer-storage-contract` with file identity, canonical lifecycle states, transfer-versus-processing separation, local/remote availability, allowed actions per state, partial cleanup, collision policy, and baseline file-lifecycle verification cases.
