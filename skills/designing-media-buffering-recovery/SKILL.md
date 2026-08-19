---
name: designing-media-buffering-recovery
description: Use when playback stalls or startup is delayed and the player must distinguish transient buffering from failure, preserve intent, communicate progress, and recover without looping indefinitely.
---

# Designing Media Buffering Recovery

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns the stalled-playback recovery state. It does not choose adaptive quality itself. It decides when buffering becomes visible, how long transient waiting is tolerated, which diagnostics/actions appear, and whether playback resumes automatically after data returns.

## Decision Boundary
Differentiate startup buffering, seek buffering, mid-playback stall, and rebuffer caused by source/DRM/network errors. Avoid flashing a spinner for subsecond normal transitions; establish a visibility delay while still maintaining accessible state truth when waiting becomes material. Preserve play intent: if the user was playing before a transient stall, successful recovery usually resumes; if they paused during buffering, do not resume unexpectedly.

Escalate progressively. Initial state may show bounded waiting; longer stalls can offer retry, lower quality, reconnect, or diagnostics according to known failure class. A spinner is not an infinite error state. Track repeated stall loops and stop auto-retrying when the product would otherwise trap users in repeated failure.

## Failure Topology
- Every tiny buffer transition flashes a large spinner over the content.
- Spinner persists forever after a terminal 404/DRM failure.
- Retry restarts from the beginning instead of the current position.
- User presses Pause during a stall, but recovery auto-resumes anyway.
- Screen reader receives no indication that playback stopped because buffering began.
- Auto retry repeatedly consumes bandwidth without surfacing a terminal action.

## Falsification and Recovery
Simulate slow startup, intermittent bandwidth, seek beyond buffer, dropped connection, terminal source error, DRM error, repeated retry, user pause during stall, and quality adaptation. The design fails if a terminal failure is represented as indefinite waiting or if recovery changes explicit transport intent.

Recover by classifying stall versus failure, adding elapsed thresholds, preserving current time/play intent, escalating to actionable recovery, and capping retry loops. Coordinate with adaptive-quality and connectivity specialists without conflating their state ownership.

## Output Contract
Return `media-buffering-recovery-contract` with buffering classes, visibility thresholds, intent preservation, retry/escalation policy, terminal-error handoff, accessible status, position preservation, and stall recovery verification scenarios.
