---
name: designing-device-orientation-transitions
description: Use when rotating a phone, tablet, kiosk, camera, or convertible changes layout or media/capture behavior and the product must preserve task state, focus, scroll, and physical orientation semantics.
---

# Designing Device Orientation Transitions

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns state continuity across portrait/landscape and sensor-driven orientation changes. It is not generic responsive design; rotation can recreate native activities/views, change camera coordinates, alter safe areas, and happen while a user is mid-gesture or editing.

## Decision Boundary
Decide which surfaces support rotation and whether any orientation lock is truly required by task. Preserve canonical data, current route, form input, media position, selection, focus intent, and meaningful scroll anchor across layout reconstruction. Spatial controls such as camera overlays, maps, drawing canvases, and directional input may need coordinate transforms rather than simple component reflow.

Avoid treating raw accelerometer changes as immediate layout rotation; follow platform orientation state to prevent jitter. If orientation changes during modal input or keyboard display, ensure focused control remains visible. Save/restore lifecycle must tolerate operating-system recreation on platforms that destroy views during rotation.

## Failure Topology
- Rotating clears an unsaved form because the screen component remounts from defaults.
- Video restarts from zero after orientation change.
- Camera crop overlay rotates visually but capture coordinates remain in old orientation.
- Focus returns to document start and keyboard obscures the edited field.
- App forces landscape for a task that is fully usable in portrait, conflicting with accessibility/device posture.
- Rapid sensor movement causes repeated layout toggles before OS orientation settles.

## Falsification and Recovery
Rotate during editing, media playback, capture, modal dialogs, selection, scrolled lists, loading, and keyboard-visible states. Test platforms with view/activity recreation. The design fails if orientation changes mutate task data or physical coordinate meaning rather than only presentation.

Recover by storing canonical task state outside transient view geometry, mapping spatial coordinates, restoring focus/scroll anchors, following platform orientation events, and limiting locks to justified hardware/task constraints.

## Output Contract
Return `device-orientation-contract` with supported orientations, lock rationale, preserved state/anchors, spatial-coordinate transforms, OS recreation handling, keyboard/focus behavior, and rotation verification cases.
