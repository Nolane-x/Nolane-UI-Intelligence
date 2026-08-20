---
name: designing-audio-description-access
description: Use when visual-only narrative information has an audio-description track or equivalent and users need to discover, select, preserve, and understand that accessibility option across playback contexts.
---

# Designing Audio Description Access

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns access to audio description as an accessibility feature: discoverability, selection state, track naming, persistence, and fallback when the platform cannot play a separate description track. It does not author the description script or generic audio-track selection for multilingual entertainment.

## Decision Boundary
Expose description using language users understand, not technical codec or track metadata. Distinguish “English” from “English — Audio Description” and preserve the choice when moving between episodes or related media where a compatible track exists. If descriptions are delivered as an alternate mixed audio program, explain that switching replaces the primary mix rather than layering on top.

Discovery must not require visually scanning a hidden player menu. The accessibility option should be reachable by keyboard and screen reader and reflected in the current playback state. When casting, offline downloads, or picture-in-picture cannot carry the selected description track, surface the limitation before mode transfer instead of silently reverting to ordinary audio.

## Failure Topology
- The track appears only as “Audio 2,” so users cannot know it contains descriptions.
- Selecting description closes a menu but provides no confirmation of the active track.
- The preference resets for every episode despite equivalent tracks being available.
- Casting silently switches back to the default audio program.
- Offline download fetches video without the selected descriptive audio and reveals the loss only after travel.
- A visually hidden track menu is technically focusable but has an unusable order or inaccessible labels.

## Falsification and Recovery
Operate track discovery and switching nonvisually from playback start, after seeking, across episode changes, offline preparation, casting, fullscreen, and resumed sessions. The design fails if a user cannot determine whether description is active or if playback-mode transitions silently remove it.

Recover by canonicalizing accessibility track labels, persisting compatible preference, announcing active-track changes, warning before unsupported transfers, and providing a documented alternative when separate tracks are unavailable. Confirm that switching tracks does not unexpectedly reset playback position.

## Output Contract
Return `audio-description-access-contract` with discovery location, track labeling, selection feedback, preference persistence, compatibility matching, casting/offline/PiP behavior, unsupported-mode warnings, and nonvisual playback verification cases.
