---
name: designing-file-locking-and-checkout
description: Use when collaborative file editing requires exclusive locks, checkout/check-in, lease expiry, ownership transfer, or read-only fallback and users need to know who can safely modify the object.
---

# Designing File Locking and Checkout

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns explicit exclusivity state around files. It does not own real-time merge conflict resolution. Some products intentionally prevent concurrent edits through lock or checkout; the UI must make lock authority, lease lifetime, and recovery unambiguous.

## Decision Boundary
Define lock type: hard exclusive, advisory, time-limited lease, manual checkout, or automatic editing lock. Show lock owner and actionable reason without exposing unnecessary identity data. The holder needs clear check-in/release behavior; other users need read-only/open-copy/request-access options where policy allows. If a client disconnects, define lease expiry or administrative recovery so stale locks do not block work indefinitely.

File version used for checkout must be explicit. Check-in should create or update according to versioning semantics and verify that the lock is still valid. Admin override is a high-impact action because the original editor may still hold local unsaved work; communicate that consequence.

## Failure Topology
- File appears editable until save, when server rejects because someone else holds a lock.
- Stale lock survives a crashed client forever.
- “Unlock” by an admin gives no warning that another user may still be editing offline.
- Checkout is associated with filename, so rename loses the lock.
- Lease expires silently while user edits for a long session.
- Read-only users can interact with editing controls that will never commit.

## Falsification and Recovery
Test two users, offline/crash, long edits, lease renewal/expiry, rename/move, check-in, admin override, permission change, and opening stale cached copies. The design fails if editing affordances do not correspond to actual write authority at that moment.

Recover by binding locks to stable file identity, surfacing lock state before editing, renewing/expiring leases visibly, making read-only mode explicit, and warning on override. Revalidate authority at check-in while preserving local recovery if the lock was lost.

## Output Contract
Return `file-lock-checkout-contract` with lock types/states, owner display, lease renewal/expiry, editor/read-only affordances, checkout version binding, check-in behavior, override/recovery, and multi-user locking verification cases.
