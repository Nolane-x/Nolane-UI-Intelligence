---
name: designing-audio-track-selection
description: Use when video or rich media carries multiple audio programs and users need to choose language, commentary, descriptive audio, alternate mix, or channel configuration without losing playback continuity.
---

# Designing Audio Track Selection

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns general alternate-audio track identity and switching. Audio description has an accessibility-specific child contract elsewhere; this owner handles language dubs, director commentary, original audio, alternate mixes, and other programs.

## Decision Boundary
Expose original versus dubbed language explicitly where that distinction matters. Track labels should include language plus purpose, not generic “Audio 1/2.” Some programs may differ in channel layout or loudness; switching should not reset position and should handle decoder transition without creating a false stopped state. Define preference hierarchy between “original audio” and “preferred language” because users may value one over the other.

Persist choices by semantic preference, not media-local ID. If commentary was intentionally chosen, do not propagate it to unrelated media as though it were a language preference. When the selected language is missing, decide whether to fall back to original, another regional variant, or prompt. External playback and downloads need capability negotiation so the selected program is actually transferred.

## Failure Topology
- The menu lists codec/channel metadata but no human purpose or language.
- A commentary track becomes the default for the next episode because track index 2 was persisted.
- Switching audio restarts the video or loses current seek position.
- Original-language preference is overridden by UI locale without consent.
- Offline download excludes the user's selected alternate audio track.
- Casting shows one active track locally while the receiver plays another.

## Falsification and Recovery
Test original/dub/commentary/alternate mixes, missing languages, episode/item transitions, resume, switching during buffering, offline download, and external playback. Verify active track via actual audible result where possible, not only UI state. The design fails if preference semantics are reduced to numeric IDs.

Recover by storing semantic track purpose/language, separating persistent preferences by purpose, preserving timeline state during switch, and reconciling receiver/offline capabilities. Coordinate audio-description tracks with the accessibility owner so they are labeled consistently without losing their special status.

## Output Contract
Return `audio-track-contract` with track purposes/labels, original-versus-preferred-language policy, persistence semantics, missing-track fallback, switch continuity, decoder/output considerations, and offline/external verification cases.
