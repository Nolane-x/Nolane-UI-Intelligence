---
name: designing-download-progress-and-retry
description: Use when obtaining a file can be slow or fail and the product needs trustworthy progress, destination state, retry/resume semantics, integrity checks, and completion behavior beyond a one-click browser download.
---

# Designing Download Progress and Retry

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns managed download transfer state. It does not own media-specific offline downloads. It covers products where the application can observe or control download progress and must distinguish server preparation, byte transfer, local save, and completed availability.

## Decision Boundary
Break the operation into relevant phases. Large exports may spend time preparing before bytes are available; presenting that as 0% download can imply a stall. When total size is known, report durable received bytes; when unknown, use indeterminate state until a trustworthy denominator exists. Decide whether retry can resume a partial transfer using range/session support or must restart.

Completion means the file reached the promised destination and passed required integrity checks. In browser contexts, the application may not know final filesystem placement; do not claim “saved to Downloads” unless platform APIs confirm it. Duplicate download names, expired URLs, auth refresh, and destination permissions need explicit behavior.

## Failure Topology
- Progress reaches 100% when server preparation ends but byte transfer has not begun.
- Retry downloads a second full copy while an invisible partial file remains.
- The app claims a path it cannot actually inspect in browser sandbox.
- Expired signed URL is retried repeatedly without renewing authorization.
- Size denominator changes mid-transfer and percentage jumps nonsensically.
- Integrity failure is reported as successful because transport completed.

## Falsification and Recovery
Test prepared exports, known/unknown sizes, network interruption, range resume, auth expiry, destination permission denial, filename collision, integrity failure, cancel, and repeated retry. The design fails if progress represents a different phase than its label or if completion is declared before usable local availability.

Recover by modeling preparation/transfer/save/verify phases, using known denominators only, renewing auth separately, resuming when evidence supports it, cleaning abandoned partials, and bounding claims to what the platform can observe.

## Output Contract
Return `download-progress-retry-contract` with operation phases, progress source, known/unknown size behavior, destination observability, retry/resume policy, auth renewal, integrity/completion criteria, partial cleanup, and download verification cases.
