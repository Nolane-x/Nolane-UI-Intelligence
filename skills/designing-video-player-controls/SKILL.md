---
name: designing-video-player-controls
description: Use when video playback needs controls that coexist with visual content, overlays, pointer/touch inactivity, keyboard operation, and responsive aspect ratios without obscuring essential imagery.
---

# Designing Video Player Controls

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns the video-player control layer and its visibility lifecycle. It does not own fullscreen, subtitles, or quality selection individually. It decides how transport, timeline, time labels, volume, settings, and mode controls appear over or around moving imagery while remaining reachable.

## Decision Boundary
Define control visibility by input modality and playback state. Pointer users may reveal controls on movement; touch users need explicit taps; keyboard focus must keep controls available and never allow an inactivity timer to hide the focused element. Paused, ended, error, and first-play states often require controls to remain visible. Make the control surface occupy bounded safe areas so it does not permanently cover captions or essential video details.

Prioritize controls responsively. A small embedded player may retain play/pause, time, fullscreen, and one settings entry while moving secondary actions elsewhere. Do not shrink hit targets until every desktop control fits. Define pointer/touch hit areas, focus order, keyboard shortcuts, and the relationship between center-overlay actions and the bottom control bar so duplicate Play buttons share one state.

## Failure Topology
- Controls auto-hide while a keyboard user is focused inside them.
- Mobile player compresses twelve desktop icons into tiny targets.
- A center play overlay and transport bar display conflicting playing/paused states.
- Captions are covered whenever the bottom controls appear.
- Hover is the only way to discover controls on a touch device.
- Ended state hides replay and makes the player look frozen.

## Falsification and Recovery
Test mouse, touch, keyboard, screen reader, control inactivity, paused/playing/buffering/ended/error, embedded/narrow/full-width layouts, and captions visible. The design fails if an operable control disappears due to timer state or if responsive compression sacrifices targetability and state clarity.

Recover by binding visibility to modality and focus, defining persistent states, reducing secondary controls by priority, reserving caption-safe geometry, and centralizing transport truth. Re-test after adding settings or accessibility controls because control-bar growth changes the collision model.

## Output Contract
Return `video-player-control-contract` with control inventory/priority, visibility state machine, input-modality behavior, focus/timer rules, responsive reduction, caption-safe zones, overlay/bar synchronization, and video-control verification cases.
