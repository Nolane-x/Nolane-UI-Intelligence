---
name: designing-file-sharing-expiration
description: Use when a file share or access grant is intentionally time-bounded and users need to set, understand, extend, revoke, and audit expiration without confusing link lifetime with file deletion.
---

# Designing File Sharing Expiration

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns temporal boundaries on file sharing. It does not own generic link sharing or collaboration permissions. Its concern is expiry: when access ends, whose clock/time zone governs it, what recipients experience, and what owners can extend or revoke.

## Decision Boundary
Define what expires: public link token, named-user permission, external-domain access, download ability, or a whole share invitation. File itself normally remains. Display expiration as an absolute date/time with time-zone context when consequence matters; “in 7 days” alone becomes ambiguous later. Owners should see active/expired/revoked state and whether reopening creates a new link/token or reactivates the old grant.

Recipients need a non-leaky expired state that explains access is no longer available without revealing sensitive metadata. Extension may require current authority and policy max duration. Downloads made before expiry cannot be remotely erased; do not imply expiration retracts copies already obtained.

## Failure Topology
- Expiration is shown as local midnight with no zone and ends earlier for another user.
- Expired link returns generic “file not found,” leading recipients to report deletion.
- Extending access silently reuses a compromised public token when policy intended rotation.
- Owner believes expiration revokes previously downloaded copies.
- Workspace policy caps external sharing at 30 days but UI allows a longer date and fails later.
- Revoked and naturally expired states are indistinguishable in audit history.

## Falsification and Recovery
Test future date selection, different zones, policy max/min, manual revoke, natural expiry, extension before/after expiry, recipient experience, link rotation, and permission loss by owner. The design fails if users cannot distinguish file existence from share validity or cannot determine exact end time.

Recover by naming the expiring grant, using explicit zone-aware timestamps, enforcing policy at configuration, separating revoke/expire, rotating tokens where required, and bounding claims about downloaded copies.

## Output Contract
Return `file-share-expiration-contract` with expiring grant type, time/zone semantics, policy constraints, recipient expired state, extension/revocation behavior, token rotation, audit events, and expiration verification cases.
