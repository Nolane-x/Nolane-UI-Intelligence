---
name: designing-media-library-interfaces
description: Use when authors manage reusable images, video, audio, documents, or other media assets and the interface must support identity, metadata, search, usage, variants, replacement, rights, and insertion without treating files as anonymous thumbnails.
---

# Designing Media Library Interfaces

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns the reusable asset workspace between raw upload and content placement. It does not own generic file upload mechanics or visual-media art direction. Media library objects have persistent identity, metadata, transformations, usage references, and possibly rights constraints that must survive reuse across content.

## Decision Architecture
Define the asset record beyond filename: stable ID, media type, dimensions/duration, created/source information, alt/caption metadata where relevant, focal/crop data, rights/license/expiry when applicable, variants/derivatives, and current usage. Thumbnails are browsing aids; they cannot replace the metadata needed to distinguish visually similar assets.

Search and filtering should reflect author tasks: media type, orientation, dimensions, usage, collection, uploader, date, tags, rights state, or domain-specific metadata. Selection for insertion needs a clear boundary between choosing the underlying asset and choosing a crop/variant. Do not silently create duplicate uploads when the same asset is reused.

Replacement and deletion are high-impact because one asset may appear in many published locations. Show usage before destructive change. Decide whether replacement preserves asset identity and updates every usage, creates a new version, or affects only a selected insertion. Rights expiry or deletion may require warnings and remediation without exposing broken media silently.

## Failure Topology
- Library is a wall of thumbnails with no way to distinguish same-looking assets, versions, or rights.
- Deleting an image instantly breaks twenty published pages with no usage preview.
- “Replace asset” changes every existing usage when the author intended one article only.
- Alternate crops are uploaded as unrelated files and provenance is lost.
- Rights-expired media remains selectable for new publication with no warning.
- Keyboard users cannot inspect/select assets because every action appears only on hover.

## Falsification and Recovery
Falsify with thousands of assets, duplicate filenames, multiple crops, asset replacement while published, rights expiration, missing thumbnails, video/audio duration, multi-select insertion, keyboard/screen-reader browsing, and an asset referenced by several content versions. The design fails if destructive actions cannot identify downstream usages or if selected media identity is ambiguous beyond its thumbnail.

Recover by using stable asset records, searchable metadata, derivative relationships, usage indexing, explicit replacement scope, rights state, hover-independent controls, and safe deletion/deprecation workflows tied to published references.

## Output Contract
Return `media-library-interface-contract` with asset schema, metadata/rights fields, browse/search facets, selection/insertion state, derivative/crop relationships, usage evidence, replace/delete semantics, rights-expiry behavior, accessibility interaction, and falsification cases.