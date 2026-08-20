---
name: designing-offline-media-downloads
description: Use when users can prepare audio or video for offline playback and the interface must manage selectable tracks, storage, progress, expiry, partial files, policy restrictions, and offline readiness.
---

# Designing Offline Media Downloads

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns media-specific offline preparation and readiness. It is not generic file download UX: downloaded media may be encrypted, expire, include selected subtitle/audio tracks, occupy managed storage, and remain invisible to the operating-system file browser.

## Decision Boundary
Define what “downloaded” guarantees. A ready item must include all components required for the promised offline experience: media segments, selected audio, needed captions, metadata, license/DRM state, and artwork only if essential. Show progress and size estimates with uncertainty when adaptive media size is not exact. Allow pause/resume/retry and safe cleanup of partial downloads.

Surface expiry or license refresh before travel when known. Quality and track selection should influence size transparently. Storage pressure needs a product-owned management path that distinguishes removable offline copies from original user files. Deleting a download should not delete the user's library item unless the product semantics explicitly combine them.

## Failure Topology
- “Downloaded” item fails offline because the license was never cached.
- Selected caption or audio track was not included.
- Failed download leaves large orphaned partial segments consuming quota.
- Removing offline copy also removes the saved/library item unexpectedly.
- Size estimate is presented as exact and overshoots storage mid-transfer.
- Expiry occurs during a trip with no advance indication or refresh path.

## Falsification and Recovery
Test start/pause/resume, network loss, storage exhaustion, selected tracks, quality variants, license refresh, device reboot, app update, true airplane-mode playback, and delete/re-download. The design fails if the “available offline” state cannot be proven by required local components.

Recover by defining a readiness checklist, downloading dependent tracks/licenses atomically enough for truthful state, cleaning partial data, surfacing expiry/storage constraints, and separating offline copy lifecycle from catalog ownership.

## Output Contract
Return `offline-media-contract` with readiness components, progress/resume state, quality/track inclusion, size/storage policy, partial cleanup, expiry/license behavior, offline-copy deletion semantics, and airplane-mode verification cases.
