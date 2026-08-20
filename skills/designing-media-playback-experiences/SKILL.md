---
name: designing-media-playback-experiences
description: Use when audio or video is a first-class interactive surface and playback state, temporal control, accessibility, continuity, interruption, and mode transitions need one coherent product contract.
---

# Designing Media Playback Experiences

## Parent Contract
**Required parent:** `routing-ui-work`.

This faculty owns the playback state machine shared by audio/video experiences. It is the parent for specialized controls such as scrubbing, tracks, casting, live latency, offline media, and queues. It does not author media assets or replace the accessibility owners for captions and descriptions.

## Decision Boundary
Define canonical playback states before drawing controls: unavailable, loading, ready, playing, paused, seeking, stalled, ended, failed, and mode-specific variants such as live edge. Decide which state changes are user intent, which are network/runtime consequences, and which should preserve intent across interruption. A user who pressed Play before buffering should not have to press Play again merely because transport delayed readiness unless platform policy requires it.

Treat time, position, duration, and live-window semantics as typed values. Finite media has an end and seekable duration; live media may have a moving window and no stable total. Define resume position, autoplay eligibility, background behavior, audio focus, interruption recovery, and what state persists between sessions. Playback UI must expose the same truth to keyboard, assistive technology, and remote controls as to pointer users.

## Failure Topology
- Play/pause icon reflects the last click rather than actual playback state after an error.
- Seeking, buffering, and paused are visually collapsed into one “not playing” state.
- Returning from a phone call resumes media despite the user having paused before interruption.
- A live stream is modeled as duration-zero VOD and controls become nonsensical.
- Resume position is saved after credits or a completed item and restarts at the end.
- Player controls and OS/media-session controls disagree about current state.

## Falsification and Recovery
Exercise slow startup, play-before-ready, seek while buffering, interruptions, background/foreground, ended/replay, network failure, route changes, multi-device media-session controls, and both finite/live assets. The design fails if the UI can display a playback state that the media engine does not share or if recovery loses explicit user intent.

Recover by binding controls to one canonical playback state machine, separating intent from transport outcome, recording interruption provenance, and defining persistence boundaries. Child specialists may refine parts of the state machine but may not invent incompatible playback truth.

## Output Contract
Return `media-playback-contract` with canonical states/transitions, intent-versus-runtime events, temporal value types, resume/autoplay/background policy, interruption handling, OS/session synchronization, accessibility truth, and baseline playback verification scenarios.
