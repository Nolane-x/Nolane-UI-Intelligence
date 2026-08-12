---
name: designing-tv-ten-foot-interfaces
description: Use when an interface is viewed from couch or room distance and operated primarily by remote, D-pad, controller, or voice, including streaming, media, games, signage, and living-room applications.
---

# Designing TV and Ten-Foot Interfaces

## Overview
Ten-foot interfaces optimize recognition, focus, and low-effort navigation at distance. Desktop density and pointer hover fail when users sit meters away and operate through a handful of directional controls.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require viewing distance, display resolution range, remote/controller model, shared-room/privacy context, primary content mode, and platform TV conventions. Always coordinate with `designing-gamepad-remote-focus` when directional input exists.

## Decision Model
Start from legibility at distance: larger type, stronger hierarchy, fewer simultaneous secondary labels, sufficient target separation, and imagery that reads from across the room. Do not merely scale CSS; restructure density and interaction depth.

Build navigation around focus regions and predictable Back behavior. Horizontal rails, grids, side navigation, players, and overlays need explicit directional edges. Focus treatment must be recognizable in peripheral vision and distinct from selected/playing state. Keep essential actions within a small number of directional moves and avoid pointer-style tiny icons.

Treat the room as shared. Search history, profile information, notifications, payment details, and private account data may be visible to multiple people. Authentication and text entry are expensive with remotes; use device handoff, voice, QR/link flows, or concise on-screen keyboards where platform-appropriate without sacrificing privacy.

Media controls need temporal clarity: play/pause, scrub, captions/audio, progress, current selection, and auto-hide behavior. Controls must reappear predictably and not steal focus unexpectedly. Voice can accelerate search but requires visible confirmation and fallback.

## Evidence
Test with an actual remote/controller from realistic distance, not mouse emulation alone. Verify focus graph, Back/exit behavior, long grids, text size, captions, player controls, shared-profile privacy, low-bandwidth states, and overscan/safe-area/platform requirements where relevant.

## Output Contract
Return a `tv-contract` with `viewing_distance_assumptions`, `scale_and_density_rules`, `focus_regions`, `directional_navigation`, `back_model`, `shared_room_privacy`, `text_entry_strategy`, `media_control_model`, `voice_fallback`, `safe_area_rules`, and `remote_tests[]`.

## Failure Traps
- “Responsive website” shipped to TV with mouse-sized controls.
- Focus ring too subtle to see from a couch.
- Focus and selected state conflated.
- Back button exiting the app instead of closing the current layer.
- Private account data exposed on a shared display.
- Long password entry forced through a remote with no handoff option.
- Autoplaying overlays stealing focus during media playback.

TV UI is successful when the user can operate it confidently without leaning forward to inspect the screen.