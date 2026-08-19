---
name: designing-picture-in-picture-playback
description: Use when video can continue in a system or app picture-in-picture surface and playback, controls, captions, ownership, and return-to-context must survive the reduced externalized mode.
---

# Designing Picture In Picture Playback

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns the transition into, behavior within, and return from picture-in-picture. PiP is not merely a smaller CSS player; it may be controlled by the operating system, have a restricted control set, and outlive the route that launched it.

## Decision Boundary
Define who owns PiP—the browser/OS or an app-managed floating player—and which controls are actually available. Entering PiP should preserve media position, track selection, play state, and accessibility choices supported by the platform. If captions or alternate audio cannot transfer, inform users before or during the transition. Returning to the main application should navigate/focus to a meaningful player context, not a stale destroyed route.

Decide behavior when users open a second video, close the source tab, navigate to another route, lock the device, or press the PiP close button. A single active media session should not spawn multiple competing floating players. PiP controls must reflect canonical state even when the main page is backgrounded.

## Failure Topology
- Entering PiP creates a second decoder while the in-page video continues playing audio.
- Captions vanish with no indication although users relied on them.
- Closing PiP stops playback but main UI still shows Playing.
- “Return to tab” lands on a route where the original player no longer exists.
- Starting another video leaves the old PiP window playing concurrently.
- The app displays a PiP control on unsupported platforms with no disabled explanation.

## Falsification and Recovery
Test enter/exit while playing/paused, route navigation, tab background, source-player unmount, caption/audio selections, second-media start, OS-level controls, and unsupported platforms. The design fails if PiP and in-page surfaces can disagree about ownership or state.

Recover by enforcing one canonical media session, negotiating capabilities, preserving supported track/preferences, defining source-route restoration, and reconciling all exit paths. Do not fake PiP with an overlay when the requirement depends on OS-level persistence without making that limitation explicit.

## Output Contract
Return `picture-in-picture-contract` with PiP ownership/capability, entry/exit transitions, control subset, track/accessibility transfer, route/source lifecycle, multi-media arbitration, unsupported behavior, and PiP verification cases.
