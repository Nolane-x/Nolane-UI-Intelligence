---
name: designing-camera-capture-flows
description: Use when users capture photos or video from a camera and the interface must manage permission, device choice, live preview, orientation, retake/confirm, quality, privacy indicators, and interruption.
---

# Designing Camera Capture Flows

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns camera capture as an intentional acquisition workflow. It does not own generic media playback or document-specific edge detection. It binds camera permission and device availability to preview, capture, review, and commit states.

## Decision Boundary
Separate permission grant from capture intent. Do not start camera access earlier than the task requires merely to speed up later UI. When multiple cameras exist, provide meaningful front/rear/external selection without exposing opaque hardware IDs. Live preview must communicate active capture clearly and respect platform privacy indicators. Define still/video modes, resolution/aspect constraints, orientation/rotation metadata, mirroring of front-camera preview versus saved output, and whether users review/retake before data leaves the device.

Interruption from calls, backgrounding, camera use by another app, or device removal needs a resumable state. Captured media should not be uploaded before confirmation unless the product explicitly promises immediate capture transmission. Accessibility needs nonvisual labels for capture/switch controls and an alternative path when visual alignment is required.

## Failure Topology
- Camera activates on page load before users understand why.
- Front preview is mirrored and the saved image is also incorrectly mirrored.
- Switching cameras resets already captured evidence without warning.
- Permission denial loops an in-app prompt even though only OS settings can recover.
- Background/foreground resumes to a frozen preview while UI says camera is live.
- Capture immediately uploads sensitive media before the user can review or discard.

## Falsification and Recovery
Test first permission, deny/revoke, multiple cameras, rotation, front/rear mirroring, background interruption, camera busy, still/video modes, retake, and upload-after-confirmation. The design fails if users cannot tell when camera data is actively being captured or if captured output differs materially from reviewed preview without disclosure.

Recover by delaying activation to explicit task entry, separating preview/captured/confirmed states, honoring platform orientation/mirroring, routing denied permission to real recovery, and preserving/discarding media according to explicit confirmation semantics.

## Output Contract
Return `camera-capture-contract` with activation/permission policy, device selection, preview/capture/review states, orientation/mirroring, quality constraints, interruption recovery, privacy/upload boundary, and camera verification cases.
