---
name: designing-media-ingest-and-bins
description: Own media import, verification, metadata, duplicate handling, organization, checksum/copy state, clip identity, and source-location provenance before editing begins.
---
# Designing Media Ingest and Bins

## Decision ownership

Own the boundary where external media becomes trusted project source. Decide import versus managed copy, checksum/verification, duplicate detection, metadata extraction, clip naming, bin/tag organization, camera-card preservation, ingest progress, failures, and stable project identity. Generic file import moves bytes; this owner preserves editorial source provenance.

## Inputs and evidence

Require source files/cards, codecs, metadata, file size, capture timestamps/timecode, checksums if used, storage destinations, copy/transcode/proxy options, duplicate criteria, project bin taxonomy, permissions, and removable-media behavior. Identify spanned clips or sidecar metadata that must remain associated.

## Procedure

Preview ingest set and destination before copying. Preserve camera/original filenames as metadata even if editorial clip names change. When managed copy is enabled, distinguish queued, copying, verifying, complete, failed, and source-removed states. Duplicate detection should reveal whether identity is checksum, path, metadata, or user decision. Import metadata and sidecars as a coherent source record. Users can organize clips into bins/tags without changing underlying file identity. Removing source media before verification should produce an explicit incomplete state, not a silent broken clip.

## Failure topology

Failures include editing directly from a removable card unintentionally, duplicate copies under different clip names, renamed clips losing original filename, partial copies appearing ready, sidecar/timecode metadata dropped, and one corrupt file blocking the entire ingest with no itemized recovery. Another failure is automatic transcode/proxy generation obscuring which asset is the preserved source.

## Falsification

Reject if a clip cannot trace to original source/location; if an unverified copy appears equivalent to completed ingest; if duplicate logic is opaque; if changing editorial name loses original identity; if partial failures are not itemized; or if source/transcode/proxy relationships cannot be inspected.

## Output contract

Return a `media-ingest-and-bins-contract` with: ingest set; source identity/path; managed-copy policy; destination; checksum/verification; duplicate rule; metadata/sidecar handling; clip naming; bin/tag organization; per-item progress/failure; source/transcode/proxy lineage; and removable-source warnings. Include one duplicate and one interrupted-copy case.

## Handoffs

Proxy workflows create lower-resolution derivatives, relink/recovery handles missing sources later, generic file-transfer skills provide copy progress, and nonlinear editor root consumes established clip identities.