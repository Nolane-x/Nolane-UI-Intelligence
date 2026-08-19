---
name: designing-synchronized-transcript-playback
description: Use when transcript units track the current media position and users can follow, seek from, or temporarily decouple the transcript without losing their reading position.
---

# Designing Synchronized Transcript Playback

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns live coupling between transcript segments and playback position. It assumes a transcript navigation document may exist independently. Its unique state is synchronization: active cue, auto-follow, manual reading override, seek-from-text, and rejoin behavior.

## Decision Boundary
Define cue granularity appropriate to content—sentence, phrase, speaker turn, or caption block. Active highlighting should aid orientation without producing constant screen-reader announcements. Auto-scroll is useful only while the user is following; manual scroll, text selection, search, or focus movement should suspend it. Provide an explicit or predictable way to return to the current playback cue.

Clicking or activating a transcript segment may seek to its start, but the action must be discoverable and not turn every word into a focus target. Preserve play/pause intent. If transcript timing is approximate or generated, avoid false frame-level precision. Virtualized transcripts must keep active-cue identity stable as segments mount/unmount.

## Failure Topology
- Auto-follow continuously pulls the document away while users read an earlier paragraph.
- Every active cue change is announced, overwhelming screen-reader speech.
- Clicking text seeks unexpectedly even when users are trying to select/copy it.
- Highlighted cue lags behind after a rapid seek.
- Virtualization destroys keyboard focus when the active segment changes.
- Generated transcript timing presents exact-looking timestamps despite uncertain alignment.

## Falsification and Recovery
Run playback while following, manually scrolling away, searching, selecting text, seeking through player controls, activating transcript segments, pausing, and using screen readers. The design fails if users cannot independently read without fighting automation or cannot intentionally rejoin live position.

Recover by modeling follow/suspended states explicitly, suppressing announcement noise, limiting seek activation to clear affordances, and deriving active cue from canonical media time. Surface timing uncertainty where it affects navigation rather than pretending alignment is perfect.

## Output Contract
Return `synchronized-transcript-contract` with cue granularity, active-cue derivation, auto-follow/suspend/rejoin states, seek-from-transcript behavior, focus/selection rules, timing uncertainty, virtualization handling, and synchronization verification cases.
