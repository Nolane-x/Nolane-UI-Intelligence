---
name: designing-fullscreen-media-modes
description: Use when media enters fullscreen and controls, orientation, captions, focus, safe areas, exit behavior, and browser/OS chrome differ from embedded playback.
---

# Designing Fullscreen Media Modes

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns fullscreen as a mode transition with altered geometry and platform behavior. It does not own ordinary responsive layout. Fullscreen can move elements into a special top layer, change orientation, hide system chrome, and alter keyboard escape semantics.

## Decision Boundary
Specify what enters fullscreen: video element only, entire player including captions/settings, or an app-defined presentation container. Controls and overlays needed to operate media must remain inside the fullscreen subtree. Preserve focus identity across entry and exit; if the fullscreen button invoked entry, focus should return coherently after exit without trapping users behind browser chrome.

Define orientation policy on devices that support locking, but do not force rotation when content/user settings argue otherwise. Respect safe areas, notches, and system gesture zones. Fullscreen should not reset position, selected tracks, quality, or playback intent. Escape/back handling must distinguish closing nested menus from exiting fullscreen where platform conventions expect that sequence.

## Failure Topology
- Only the video enters fullscreen while custom captions/settings remain outside and disappear.
- Entering fullscreen resets playback position because a new player instance mounts.
- Escape exits fullscreen even when a settings dialog inside it should close first.
- Focus disappears after exit because the original fullscreen button was replaced during mode change.
- Controls collide with device notches or gesture regions.
- Forced landscape rotation ignores user/device constraints and makes portrait content worse.

## Falsification and Recovery
Enter/exit from keyboard, pointer, touch, browser controls, orientation change, nested settings, captions, paused/playing/buffering, and end state. Test devices with safe-area insets. The design fails if fullscreen changes media truth or removes an action/accessible feature available in embedded mode.

Recover by fullscreening the correct player container, sharing one media instance/state, nesting overlays inside the top layer, defining focus restoration, and respecting platform orientation/safe areas. Verify exit paths initiated outside the app as well as the visible button.

## Output Contract
Return `fullscreen-media-contract` with fullscreen subtree, entry/exit triggers, focus restoration, control/overlay inclusion, orientation/safe-area policy, nested escape behavior, state preservation, and fullscreen verification scenarios.
