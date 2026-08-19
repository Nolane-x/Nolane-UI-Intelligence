---
name: designing-transcript-navigation
description: Use when long audio or video transcripts must function as navigable documents rather than undifferentiated walls of timed text.
---

# Designing Transcript Navigation

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns the document-navigation model of a transcript: structure, speaker changes, sections, searchability, reading order, and optional links to corresponding media positions. It is distinct from synchronized transcript playback, which owns the live coupling while media runs.

## Decision Boundary
Represent the transcript first as readable content that remains useful without the media player. Long material needs meaningful segmentation such as chapters, topics, speakers, or timestamps chosen from actual content structure. Timestamps can be actionable links when seeking is available, but they must not replace headings or produce hundreds of noisy tab stops. Speaker identification should be machine-readable and visually clear without forcing the speaker name into every sentence.

Search and copy behavior should operate on transcript text, not hidden caption fragments. If corrections or generated transcripts carry uncertainty, expose that status without interrupting every reading unit. On mobile, transcript controls must not consume the reading area or continually auto-scroll against a user's manual exploration.

## Failure Topology
- A two-hour transcript is one unbroken block with no semantic landmarks.
- Every sentence timestamp is a focusable link, making keyboard navigation slower than reading.
- Auto-follow repeatedly yanks the scroll position back while a user is reading an earlier section.
- Speaker identity is shown only through color.
- Transcript search highlights matches visually but exposes no count or next/previous navigation nonvisually.
- Copying text includes hidden timing metadata and control labels instead of clean content.

## Falsification and Recovery
Use keyboard, screen reader headings/search, text selection, transcript search, manual scrolling during playback, and narrow viewports on both short and very long media. The design fails if users cannot jump among meaningful sections, if playback automation prevents independent reading, or if removing timestamps destroys the transcript's information architecture.

Recover by adding content-derived structure, reducing timestamp tab stops, separating auto-follow from manual reading state, making speaker identity redundant, and treating transcript search as document navigation. Preserve a static readable transcript when synchronization features are unavailable.

## Output Contract
Return `transcript-navigation-contract` with structural segmentation, speaker semantics, timestamp/link policy, search behavior, auto-follow opt-in/escape rules, copy behavior, uncertainty labeling, and document-navigation verification cases.
