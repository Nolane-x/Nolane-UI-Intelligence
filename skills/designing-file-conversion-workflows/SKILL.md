---
name: designing-file-conversion-workflows
description: Use when users convert files between formats and must understand source/output fidelity, selectable options, asynchronous processing, failures, version ownership, and whether the conversion replaces or creates a new object.
---

# Designing File Conversion Workflows

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns format conversion as a transformation transaction. It is not generic export configuration: conversion starts from an existing file object and may lose capabilities, alter layout, or require server processing before a new file exists.

## Decision Boundary
Define source version and target format explicitly. Surface material losses before commit: formulas to values, layers flattened, transparency lost, fonts substituted, metadata removed, animation omitted, color profile changed, or quality recompressed. Options should correspond to real converter capabilities, not decorative settings. Decide whether output is a new sibling, downloadable artifact, replacement version, or attached derivative.

Conversion progress is processing, not upload/download. Users may navigate away while work continues; provide durable job identity and completion/error retrieval. Retry must not duplicate successful output. If conversion uses third-party services, privacy/data-transfer policy must be disclosed and authorized separately.

## Failure Topology
- “Convert to PDF” silently drops interactive form fields or comments.
- Source changes while conversion runs, but output is labeled as if derived from the latest version.
- Retry after timeout creates multiple indistinguishable converted files.
- UI shows 100% when upload to converter completed but transformation is still running.
- Conversion overwrites the original despite users expecting a new file.
- Sensitive source is sent to an external conversion service without product authorization.

## Falsification and Recovery
Test lossy/lossless formats, large files, corrupt sources, concurrent source edits, cancel/retry, background completion, target-name collision, and converter outage. Compare material content/fidelity of outputs. The design fails if users cannot know what source version and loss profile produced the result.

Recover by binding jobs to immutable source versions, listing material conversion losses/options, separating transfer/processing state, idempotently creating outputs, and making replacement-versus-derivative semantics explicit.

## Output Contract
Return `file-conversion-contract` with source-version binding, target formats/options, fidelity-loss disclosures, processing job lifecycle, output ownership/location, retry/idempotency, privacy handoff, and conversion verification cases.
