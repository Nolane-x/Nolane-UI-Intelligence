---
name: designing-storage-quota-management
description: Use when account, workspace, device, or managed offline storage has limits and users need to understand usage, approaching limits, reclaimable categories, upload consequences, and cleanup without accidental data loss.
---

# Designing Storage Quota Management

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns the interaction model around storage capacity and quota. It does not choose pricing or backend allocation. It explains what counts, where the limit applies, which data is reclaimable, and how transfers/edits behave at or near exhaustion.

## Decision Boundary
Distinguish remote account quota, workspace quota, local cache, offline media, temporary processing space, and device free storage. A single “storage full” label is insufficient if deleting local cache will not reduce cloud quota. Show used/limit values with category breakdown only when categories are accurate and actionable. Some usage may be delayed due to processing or shared ownership; state estimation uncertainty.

Warn before operations likely to exceed quota when size is known, but still handle race conditions at commit. Cleanup actions need consequence labels: remove local copy, move to trash, permanently delete, reduce version history, or change plan. Do not recommend deleting originals when temporary cache is the real issue.

## Failure Topology
- Storage meter combines local cache and cloud quota into one meaningless percentage.
- Upload starts despite known insufficiency and fails after hours of transfer.
- “Free up space” permanently deletes files when users expected cache eviction.
- Shared files are counted against the wrong owner's quota in UI.
- Usage remains stale after deletion and prompts users to delete more than needed.
- Temporary conversion space causes failure although headline quota appears available.

## Falsification and Recovery
Test near/full quota, large known/unknown uploads, shared ownership, trash retention, version cleanup, local cache, async usage recalculation, and concurrent changes from another device. The design fails if a recommended cleanup action cannot be tied to the constrained storage pool.

Recover by naming storage scope, separating local/remote categories, forecasting when possible, confirming destructive cleanup, and refreshing usage after asynchronous reclamation. Provide an upgrade/policy path only when it is genuinely relevant, not as a substitute for correct accounting.

## Output Contract
Return `storage-quota-contract` with storage pools/scopes, usage accounting, warning thresholds, operation admission, category breakdown, reclaim actions/consequences, recalculation latency, shared ownership, and quota verification cases.
