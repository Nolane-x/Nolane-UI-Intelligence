---
name: designing-media-chapter-navigation
description: Use when long-form media has semantic sections and users need to discover, jump among, resume within, and understand chapters without treating them as arbitrary timeline ticks.
---

# Designing Media Chapter Navigation

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns named temporal structure: chapters, segments, lesson units, scenes, or agenda sections. It does not own generic scrubbing. Chapters encode content meaning and provide a navigation layer over the raw timeline.

## Decision Boundary
Define chapter boundaries and titles from content authority. The active chapter should follow playback position, while selecting a chapter performs a seek with the user's current play/pause intent preserved. Long chapter lists need search, grouping, or hierarchical structure only when content warrants it. Show duration or start time when it aids choice, but title/sequence should carry primary meaning.

Chapter navigation must remain usable independently of thumbnail imagery. In educational or meeting content, completed/progress states may be useful but should not imply mastery merely because playback crossed an endpoint. When chapters are edited after users save positions, map bookmarks by time/content identity carefully rather than assuming chapter indexes remain stable.

## Failure Topology
- Chapters are generated every five minutes and presented as semantic structure despite having meaningless titles.
- Selecting a chapter always starts playback even when the user was paused.
- Active chapter indicator lags behind after manual seek.
- Thumbnails are the only way to distinguish sections.
- Screen readers encounter a long flat list with no current chapter or timing context.
- Content edits reorder chapter IDs and saved progress points to the wrong section.

## Falsification and Recovery
Test selection while playing/paused, seek across boundaries, replay from end, long lists, keyboard/screen reader, missing thumbnails, content revisions, and mobile disclosure. The design fails if chapter state can disagree with actual playback position or if chapter labels do not help users predict content.

Recover by binding active chapter to timeline boundaries, preserving transport intent, using content-derived titles/IDs, and adding scalable navigation for long structures. Treat viewing progress as separate evidence from learning/completion semantics.

## Output Contract
Return `media-chapter-contract` with chapter identity/boundaries, active-state derivation, selection seek behavior, title/timing presentation, long-list scaling, revision mapping, progress separation, and chapter navigation verification cases.
