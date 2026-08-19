---
name: designing-live-stream-player-states
description: Use when media is genuinely live and the player must represent pre-live, live edge, behind-live DVR, ended, unavailable, reconnecting, and replay-transition states without pretending it is ordinary VOD.
---

# Designing Live Stream Player States

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns semantic state for scheduled and active live streams. It separates stream lifecycle from transport buffering. A live event can be “not started,” “live but stalled,” “ended,” or “replay available,” each with different user expectations.

## Decision Boundary
Model event state from authoritative stream/schedule signals: scheduled, waiting, starting, live, ended, canceled, and replay-processing/available where relevant. Within live, distinguish at-live-edge from behind-live when DVR exists. A “LIVE” badge should represent proximity to the live edge, not merely that the asset originated as a live stream.

Define what happens before start: countdown, refresh/retry, notification opt-in, or schedule context. After end, avoid leaving an eternal spinner; communicate whether replay will appear and whether the same URL/player transitions automatically. Reconnection should preserve the user's behind-live position unless policy intentionally jumps to live.

## Failure Topology
- “LIVE” remains lit while the viewer is twenty minutes behind in a DVR window.
- Scheduled stream shows generic playback error before the event begins.
- Event ends and player spins forever because ended is treated as buffering.
- Reconnect jumps users from a chosen delayed position to live edge without warning.
- Canceled event continues to display a countdown.
- Replay processing is presented as permanent unavailability.

## Falsification and Recovery
Simulate before-start, delayed start, live edge, paused/behind live, reconnect, source failure, normal end, abrupt end, cancellation, and replay publication. The design fails if users cannot tell event lifecycle from network failure or cannot explain whether they are watching live versus delayed content.

Recover by binding UI to authoritative lifecycle state, deriving live-edge status from temporal distance, preserving deliberate DVR position across transient transport failures, and providing explicit ended/replay states. Separate schedule truth from media-engine readiness.

## Output Contract
Return `live-stream-state-contract` with event lifecycle, live-edge derivation, pre-live behavior, DVR/behind-live state, reconnect policy, ended/canceled/replay transitions, labels/actions, and live-stream lifecycle verification cases.
