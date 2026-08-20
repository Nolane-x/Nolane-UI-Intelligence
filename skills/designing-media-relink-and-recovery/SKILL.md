---
name: designing-media-relink-and-recovery
description: Use when this specialist's decision ownership is materially in scope. Own recovery of missing or moved source media through identity matching, search, relink preview, batch mapping, mismatch detection, alternate takes, and preservation of edit provenance.
---
# Designing Media Relink and Recovery

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own what happens when project source media cannot be found at its recorded location. Decide offline state, identity evidence, manual/batch search, relink candidate matching, mismatch warnings, path remapping, alternate source handling, and confirmation. Generic file browser selection is insufficient because wrong media can silently corrupt editorial meaning.

## Inputs and evidence

Require missing clip identities, original path/name, checksum/size/duration/timecode/metadata, project usage, proxy availability, candidate files, folder remapping, removable volumes, and sequence references. Identify same-name media from different cameras/cards.

## Procedure

Mark offline clips visibly in bins and timelines without deleting edit positions. When relinking, show original identity evidence and compare each candidate on checksum where available, plus duration/timecode/codec/metadata. Directory-level remap should preview all matches, ambiguous candidates, and unmatched items before commit. Allow intentional replacement/alternate media through a separate explicit operation. Preserve original source identity/path history after relink. Proxy playback may continue, but must not make the source appear recovered.

## Failure topology

Failures include same-name wrong file accepted, batch remap silently mapping multiple clips incorrectly, proxy availability hiding offline source, relink changing duration/timecode and shifting edits, and original path/provenance overwritten. Another failure is one failed candidate aborting a large safe batch without itemized resolution.

## Falsification

Reject if relink candidate identity cannot be compared to original; if ambiguous matches auto-commit; if duration/timecode mismatch has no warning; if proxy online state is conflated with source online; if batch preview does not itemize uncertain/unmatched clips; or if original source provenance is lost.

## Output contract

Return a `media-relink-and-recovery-contract` with: offline identity; original evidence; candidate matching fields; confidence/ambiguity; manual/batch remap; mismatch warnings; intentional replacement path; proxy distinction; per-item result; and preserved source history. Include one duplicate-filename camera-card scenario.

## Handoffs

Ingest establishes source identity, proxy workflows supply temporary derivatives, file browser/search supplies locations, and nonlinear editor preserves sequence references during offline state.