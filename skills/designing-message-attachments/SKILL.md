---
name: designing-message-attachments
description: Use when messages can include files or media and the interface must coordinate selection, upload, preview, scanning, failure, send coupling, download safety, and lifecycle independently from plain text.
---

# Designing Message Attachments

## Parent Contract
**Required parent:** `designing-message-composers`.

This faculty owns attachment state inside conversational messaging. It inherits general upload mechanics but adds a crucial coupling question: when does an uploaded asset become part of a message, and what happens when file transfer and message send succeed or fail independently?

## Decision Model
Separate local selection, preprocessing, uploading, server-staged asset, message-bound asset, and failed/cancelled asset states. A file that finished uploading is not yet a sent message. Conversely, if the service supports deferred upload after message creation, expose that the message contains content still processing rather than presenting a complete artifact prematurely.

Show enough metadata to verify selection—name, type, size, preview where safe—and allow removal before send. Media previews must not execute active content. Malware/content scanning may introduce a pending state after upload; the UI should distinguish “uploaded” from “available to recipients.”

Define send coupling explicitly. Does Send wait for all attachments, allow text to send while files continue, or block only failed files? If a retry occurs, preserve the message draft and successful attachments. Download/open actions should reflect file type, platform, permission, and security posture rather than assuming every attachment is safe inline content.

## Failure Topology
- Attachment shows 100% uploaded and users assume the message was sent.
- One failed file clears all successful attachments and draft text.
- Message sends before a required scan completes, then recipients see a broken placeholder.
- Removing a staged file from the composer does not delete or release the orphaned server asset.
- Preview executes untrusted HTML/SVG content in the product origin.
- Attachment permissions outlive conversation access and direct links remain usable indefinitely.

## Falsification and Recovery
Falsify with mixed successful/failed files, send pressed during upload, scan delay, oversized file, offline interruption, duplicate selection, message draft restoration, permission revocation, keyboard removal/retry, and unsafe preview types. The design fails if file lifecycle cannot be reconciled with message lifecycle or if a recipient can access an attachment outside intended conversation authority.

Recover by modeling staged assets explicitly, binding them to message IDs only at defined commit points, preserving successful stages, quarantining unsafe previews, cleaning orphan uploads, and enforcing authorization on every asset access.

## Output Contract
Return `message-attachment-contract` with attachment lifecycle, preview metadata, upload/scan states, send coupling, retry/removal/orphan cleanup, message binding, recipient availability, permission/download policy, accessibility controls, and falsification cases.