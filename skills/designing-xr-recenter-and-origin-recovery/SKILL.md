---
name: designing-xr-recenter-and-origin-recovery
description: Use when XR users must recover after tracking origin drift, changed play space, lost orientation, recenter, seated-standing change, or relocated content and the interface must restore a safe intelligible spatial frame.
---

# Designing XR Recenter and Origin Recovery

Spatial interfaces depend on a coordinate frame users rarely think about until it fails. Recenter and origin recovery must restore orientation without teleporting controls into unsafe or unreachable positions or breaking persistent anchors silently.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns the spatial scene. This skill owns recovery when the relationship between user pose, application origin, floor/seat reference, and placed UI becomes invalid or uncertain.

## Coordinate Frames
Declare the frames that matter: tracking origin, stage/play-space, local application origin, world/persistent anchor, seated reference, and user-relative head/hand poses. Recenter should specify which frame changes. Do not use one generic “reset view” action if some anchored content must remain world-fixed while menus become user-relative.

## Recovery Triggers
Support deliberate recenter plus system-detected conditions such as tracking reacquisition, guardian/play-space reconfiguration, large origin jump, app resume in a new physical location, and seated↔standing mode change. Automatic recovery should avoid moving world-anchored content without explicit evidence that its anchor is invalid.

## User Orientation
Before applying a large spatial shift, preview or explain which content will move when feasible. After recenter, re-establish a recognizable forward direction, floor/height reference, and safe reachable controls. Critical menus should remain locatable even if previously anchored panels are off-screen.

## Persistence Interaction
Persistent anchors can survive origin changes; some local anchors cannot. Distinguish recovered, unresolved, relocated, and lost anchors. Never silently reinterpret a lost world anchor as a new local placement while presenting it as the same physical location.

## Evidence
Test headset removal/resume, room change, tracking loss and reacquisition, floor-height recalibration, seated-to-standing switch, system recenter, controller origin drift, and persistent anchored content. Compare pre/post transforms for each frame.

## Failure Modes
- Recenter moves a world-anchored object that should remain fixed.
- User-relative controls remain behind the user after origin shift.
- Lost anchor is silently recreated at a new physical position.
- Floor-height correction pushes panels below floor or above reach.
- Automatic origin correction occurs during active manipulation.
- Recovery leaves no visible way to locate essential controls.

## Falsification
Place one world-anchored object and one user-relative menu, trigger tracking loss, move to a different room, and recover. Falsify if both are transformed identically despite different frame contracts or if the UI claims the world anchor survived when it did not.

## Recovery
Freeze active manipulation, classify affected frames, re-establish user-relative control access, validate persistent anchors, and ask for deliberate relocation when world evidence is lost. Keep unresolved spatial identity visible rather than snapping objects to convenient positions.

## Handoff
Anchor storage semantics use `designing-spatial-anchor-persistence`; safety zones use `designing-xr-safety-boundaries`; panel placement after recovery uses `designing-world-space-panel-placement`.

## Output Contract
Return an `xr-recenter-and-origin-recovery-contract` with `coordinate_frames[]`, `recenter_semantics`, `recovery_triggers[]`, `movement_preview_rules`, `post_recenter_orientation`, `anchor_recovery_states[]`, `manipulation_interrupt_policy`, `transform_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.