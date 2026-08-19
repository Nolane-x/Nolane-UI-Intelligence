---
name: designing-sensitive-file-handling
description: Use when files can contain confidential, regulated, secret, or highly personal information and the UI must carry sensitivity through preview, transfer, storage, sharing, download, cache, and deletion decisions.
---

# Designing Sensitive File Handling

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns how sensitivity classification changes file interaction. It does not define regulatory classification itself; privacy/security authorities provide labels and policy. This skill translates those constraints into visible state, restricted actions, safer defaults, and non-leaking representations.

## Decision Boundary
Determine sensitivity source: user label, policy engine, content scan, folder inheritance, external system, or unknown pending classification. Distinguish advisory labels from enforced policy. High-sensitivity files may suppress thumbnails, browser caching, public links, external conversion, clipboard/download, or offline copies. Explain unavailable actions with enough policy context to recover without revealing sensitive file content.

Sensitive metadata can itself leak. Recent-file lists, notification text, browser titles, analytics events, and thumbnails may expose names or previews even when access to the file body is protected. Define redaction/masking rules by channel. When classification changes after a file was already shared or cached, trigger remediation rather than only changing a badge.

## Failure Topology
- Confidential document thumbnail appears in a public recent-files widget.
- Public link button is visible and only fails after users attempt creation.
- Filename is sent to analytics despite sensitivity policy forbidding content metadata.
- Classification becomes restricted but existing offline copies/shares remain unreviewed.
- External preview/conversion service receives a file that policy forbids exporting.
- Sensitive badge is color-only and disappears in monochrome/forced colors.

## Falsification and Recovery
Test each sensitivity level through upload, preview, recent lists, search, share, download, offline, export/conversion, notifications, analytics, classification change, and deletion. The design fails if any lower-trust channel exposes content/metadata that the primary file view protects.

Recover by propagating classification as policy state, disabling/redirecting prohibited actions before transfer, redacting secondary surfaces, and triggering remediation of existing grants/caches. Keep authoritative policy source visible to admins while limiting sensitive details to permitted viewers.

## Output Contract
Return `sensitive-file-handling-contract` with classification sources/states, action restrictions, thumbnail/cache/download/share policy, metadata redaction channels, classification-change remediation, accessible sensitivity cues, and end-to-end leakage verification cases.
