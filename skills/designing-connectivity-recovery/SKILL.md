---
name: designing-connectivity-recovery
description: Use when network connectivity can disappear and return during work and the interface must reconcile local intent, queued operations, stale data, conflicts, and truthful online/offline state.
---

# Designing Connectivity Recovery

## Parent Contract
**Required parent:** `designing-offline-degraded-experiences`.

This faculty owns the transition from disconnected or degraded operation back to authoritative connected state. It is narrower than general offline UX: the key problem is reconciliation—what local actions happened, which reached the server, which are queued, and what must be resolved after connectivity returns.

## Decision Model
Separate connectivity signals from operation evidence. Browser/network APIs can suggest offline status but cannot prove a service is reachable; a healthy internet connection also does not prove the target API is available. Display state based on meaningful service reachability where possible, and avoid flapping banners during short transient failures.

Define local mutation classes. Some edits can queue safely with stable IDs and revisions; some reads can use cached data; high-risk transactions may require online authority and must remain blocked rather than “sync later.” On reconnection, replay only operations whose semantics are idempotent or conflict-aware. Keep ordering dependencies explicit when operation B assumes A succeeded.

Reconciliation should expose conflicts rather than silently selecting a winner. If remote state changed while local work was offline, show what can merge, what needs a user decision, and what was already applied. Successful synchronization must clear stale offline indicators only after pending work is actually reconciled, not merely when a socket reconnects.

## Failure Topology
- “Back online” appears immediately when network returns although queued edits are still failing to sync.
- Offline payment is queued like a note edit and later executes unexpectedly.
- Replayed operations arrive out of order and reference objects not yet created.
- Local edits overwrite newer remote state because revision checks are absent.
- Connectivity banner flickers on every intermittent request failure.
- Users close the app believing work is synced when it only exists in volatile memory.

## Falsification and Recovery
Falsify with brief network flaps, service-specific outage, app sleep/resume, multiple queued dependent operations, server changes during offline work, session expiry before replay, storage quota failure, and a high-risk action attempted offline. The design fails if “online” is treated as equivalent to “all local intent safely reconciled” or if replay can silently duplicate/overwrite work.

Recover by separating reachability from sync state, classifying offline-capable operations, persisting queues durably, preserving dependency/order metadata, using revision/idempotency controls, escalating conflicts, and reporting synchronization completion only after authoritative acknowledgement.

## Output Contract
Return `connectivity-recovery-contract` with reachability signals, offline-capable operation classes, queue durability, dependency ordering, replay/idempotency policy, session-expiry behavior, conflict reconciliation, sync-status messaging, high-risk blocking rules, and falsification cases.