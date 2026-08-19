---
name: designing-resumable-file-uploads
description: Use when uploads may be large or networks unreliable and users need interruption-safe progress that resumes the same logical transfer rather than restarting or duplicating the file.
---

# Designing Resumable File Uploads

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns continuation semantics for one upload across network loss, app restart, tab suspension, expiring credentials, or transient server failure. It does not own a multi-file queue. The central invariant is that resumption continues a known upload session for the same content and file object.

## Decision Boundary
Define what evidence allows a resume: upload session ID, acknowledged byte/chunk ranges, content fingerprint, file metadata, and session expiry. Progress must reflect server-acknowledged durable transfer rather than bytes merely read from the local disk. When the source file changes between attempts, do not resume against stale ranges. Reauthentication may renew authority without discarding already accepted chunks if the backend supports it.

Users need clear paused/interrupted/resuming states and a deliberate restart path. Automatic resume is useful after short connectivity loss, but repeated failures should stop looping and expose action. Persistence across browser/app restart requires permission to re-access local content; if the platform cannot reacquire the file, explain why a user must choose it again and how identity is verified.

## Failure Topology
- Progress reaches 90% based on sent bytes, then server acknowledges only 40% after reconnect.
- Resume session points to an older version of the local file and produces corrupted content.
- Authentication expiry restarts a multi-gigabyte transfer from zero unnecessarily.
- Automatic resume loops forever on a terminal quota or policy error.
- App restart claims “resuming” but no longer has permission to read the source file.
- Restarting creates a second remote object while the old partial upload remains orphaned.

## Falsification and Recovery
Test network drop at multiple offsets, app/tab restart, credential expiry, source-file modification, server session expiry, repeated retry, quota failure, and final integrity check. The design fails if reported progress cannot be reconciled with server state or if resume can combine chunks from different content.

Recover by anchoring resume to server-acknowledged ranges and content identity, renewing auth independently, verifying source continuity, expiring/cleaning abandoned sessions, and providing explicit restart when resume evidence is invalid.

## Output Contract
Return `resumable-upload-contract` with resumable-session identity, durable progress source, chunk/range acknowledgment, source-integrity checks, auth/session expiry behavior, auto/manual resume rules, restart cleanup, and interruption verification cases.
