---
name: designing-playback-speed-control
description: Use when users can alter playback rate and the product must define available rates, persistence, pitch handling, live/DRM constraints, labeling, and recovery to normal speed.
---

# Designing Playback Speed Control

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns playback-rate choice, not generic player settings. It decides which speeds are meaningful for the content, how the active rate is exposed, when it persists, and what happens on media types or playback modes that cannot honor the selected rate.

## Decision Boundary
Choose a rate set from listening/viewing tasks rather than using arbitrary increments. Spoken learning may benefit from fine control around 1× and higher speeds; music or safety training may intentionally restrict speed. Preserve pitch where the engine supports it and disclose exceptions where altered pitch materially harms comprehension. The active rate should remain visible enough that users can explain unusual audio/video behavior and return to 1× quickly.

Define persistence scope: current item, series, media type, user profile, or session. A podcast speed preference should not necessarily apply to music videos. Live streams may support only constrained catch-up rates. Casting or external playback may reject custom rates; transfer should surface the downgrade instead of showing a stale 1.5× badge while the receiver plays at 1×.

## Failure Topology
- Rate changes visually but engine remains at the previous speed after casting.
- A global 2× preference unexpectedly applies to music or interactive training.
- The menu lists floating-point artifacts such as 1.249999×.
- Pitch shifts make speech unusable despite a nominally supported rate.
- Users cannot see the current non-default speed once the settings menu closes.
- Resuming an item restores position but silently resets speed.

## Falsification and Recovery
Test all rates on representative content, item transitions, resume, background playback, live content, casting, and unsupported engines. Verify timing labels continue to represent media time rather than wall-clock time. The design fails if UI and engine rates diverge or if persistence crosses content classes without an explicit policy.

Recover by centralizing rate state with engine acknowledgment, scoping preferences by content/media class, formatting labels canonically, and reverting visibly when a mode cannot honor the preference. Keep a one-action return to normal speed.

## Output Contract
Return `playback-speed-contract` with allowed rates by media class, active-rate visibility, pitch policy, persistence scope, live/external-playback constraints, fallback behavior, labeling, and rate verification cases.
