---
name: designing-file-uploaders
description: Use when users add local files or directories and the interface must manage acquisition, validation, queueing, progress, cancellation, retry, duplicate handling, security messaging and accessible alternatives to drag and drop.
---

# Designing File Uploaders

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns the user-facing upload lifecycle. Server storage policy, malware scanning, rights policy and domain processing are external authorities whose states must be surfaced but not invented here.

## Decision Model
Separate **selection** from **upload** and from **post-upload processing**. A file may be chosen, locally validated, queued, transferring, transferred, scanning/transcoding/importing, succeeded or failed. One spinner labeled “Uploading…” cannot represent all stages truthfully.

Provide multiple acquisition paths when material: file picker, drag/drop, paste, capture or directory selection. Drag/drop is an enhancement, never the only accessible route. Define accepted type/size/count constraints before users select where practical, then validate actual file metadata/content according to security policy.

For multiple files, choose queue behavior: parallelism, ordering, per-file cancel/retry and aggregate progress. Do not let one failed file erase successful siblings. Duplicate handling needs domain semantics—replace, keep both, skip or version—not a generic filename check if content identity matters.

Large uploads require resilience. Communicate whether leaving the page cancels, continues in background, or can resume. If resumable protocols exist, surface recovery state without promising resume that the backend cannot support.

## Failure Topology
- UI says 100% but backend is still scanning/transcoding with no status.
- Drag/drop zone has no keyboard-accessible file picker.
- A 1 GB invalid file uploads completely before size/type rejection that could be detected locally.
- Retrying one failed file restarts all successful uploads.
- Page close loses hours of transfer with no warning.
- Filenames are treated as safe display text or unique identity.

## Falsification and Recovery
Test invalid type/size, 1/100 files, duplicate names, network loss, cancel/retry, page navigation, post-processing failure, keyboard/screen reader and drag over wrong targets. The contract fails if progress stage or per-file outcome is ambiguous.

Recover by modeling lifecycle stages explicitly, separating per-file and aggregate state, exposing picker alternatives, validating early where authoritative and aligning resilience messaging with backend capability.

## Output Contract
Return `file-uploader-contract` with acquisition paths, constraints, file lifecycle, queue/concurrency, progress semantics, cancel/retry/resume, duplicate policy handoff, navigation consequences, accessibility and failure scenarios.