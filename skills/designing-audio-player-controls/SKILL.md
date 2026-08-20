---
name: designing-audio-player-controls
description: Use when an audio-first experience needs a control hierarchy for listening without relying on video framing, including compact states, background continuity, metadata, and output behavior.
---

# Designing Audio Player Controls

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns the control composition for audio-first playback such as music, podcasts, lessons, voice recordings, or spoken documents. It does not own queue semantics or playback-speed logic; it decides which actions and metadata remain available across full, mini, lock-screen, and background contexts.

## Decision Boundary
Start from listening tasks. Core transport normally includes play/pause, position, current item identity, and meaningful navigation appropriate to the content: previous/next track, skip interval, chapters, or none. Do not copy music-player controls into a podcast or voice-note product if “previous track” has no useful meaning. Define volume/output controls according to platform authority; mobile systems often own physical volume while web/desktop players may expose app volume.

Compact and background variants must preserve identity and safe control continuity. A mini-player should make the active item unmistakable and provide a path back to full context without stealing layout. Metadata such as title, creator, artwork, episode, or recording date should prioritize what helps users know what is playing rather than reproduce every catalog field.

## Failure Topology
- A podcast player uses track-skip icons whose meaning is confused with 15-second skip.
- A mini-player loses the active item's title and users cannot tell which recording is producing sound.
- App volume duplicates system volume on mobile and creates two inconsistent levels.
- Playback controls disappear during background transition while audio continues.
- Decorative waveform is mistaken for a seek control but is not operable.
- Long localized titles push play/pause or close controls out of the compact player.

## Falsification and Recovery
Test music-like, spoken-word, and short-recording content in full/mini/background states, narrow widths, long metadata, keyboard, screen reader, and system media controls. The design fails if transport semantics do not match content type or if users can hear audio while lacking a reliable way to identify or stop it.

Recover by aligning controls with listening tasks, preserving a minimal persistent control set, delegating platform-owned volume/output correctly, and making decorative versus interactive temporal visuals distinct. Verify child speed/chapter/queue features only when those capabilities exist.

## Output Contract
Return `audio-player-control-contract` with content-type transport map, full/compact/background control sets, metadata priority, platform volume/output ownership, mini-player transition, decorative-versus-interactive waveform rules, and audio-control verification cases.
