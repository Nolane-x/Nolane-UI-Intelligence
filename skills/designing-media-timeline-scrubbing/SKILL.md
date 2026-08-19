---
name: designing-media-timeline-scrubbing
description: Use when users seek within time-based media and the timeline must distinguish current position, buffered/available ranges, preview state, drag intent, keyboard steps, and committed seek position.
---

# Designing Media Timeline Scrubbing

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns temporal seeking through a timeline. It separates preview position from actual playback position and defines drag, click, keyboard, touch, and assistive semantics. It does not own clip selection or live latency, though those features may constrain the seekable range.

## Decision Boundary
Represent at least current playback position, seekable range, and provisional scrub position. During drag, decide whether media follows continuously or only seeks on release; the choice depends on decoder/network cost and expected precision. Provide meaningful keyboard increments plus larger-step affordances where duration is long. The slider's accessible value should expose human-readable time and, when useful, nearby chapter/title context.

Buffered range is not the same as seekable range. For live DVR windows, the minimum/maximum move as time advances. Preview thumbnails or waveform snippets can aid visual targeting but may not become mandatory to perform the seek. Touch scrubbing needs sufficient geometry and should avoid fighting page scroll in embedded players.

## Failure Topology
- The thumb jumps during drag because playback updates overwrite the provisional scrub position.
- Keyboard arrows move by a fixed tiny amount on a six-hour recording.
- Buffered progress is presented as if content beyond it cannot be sought.
- Touching the timeline starts page scroll and seeking simultaneously.
- Screen readers announce only a raw percentage rather than elapsed/remaining time.
- A live-window timeline exposes positions that have already expired.

## Falsification and Recovery
Seek by click, drag, touch, keyboard, assistive slider commands, rapid repeated moves, slow network, long duration, short clips, and moving live windows. The design fails if preview and committed positions cannot be distinguished or if the chosen input modality makes precise movement effectively impossible.

Recover by separating provisional/actual state, scaling increments to media/task, modeling seekable range explicitly, and disabling or correcting positions that expire. Preserve pause/play intent across the seek rather than assuming every seek resumes media.

## Output Contract
Return `media-scrubbing-contract` with temporal state model, seekable/buffered ranges, provisional versus committed behavior, pointer/touch/keyboard increments, accessible value text, live-window rules, preview policy, and seeking verification cases.
