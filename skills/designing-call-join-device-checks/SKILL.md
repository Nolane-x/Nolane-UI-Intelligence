---
name: designing-call-join-device-checks
description: Use when users join realtime audio or video sessions and need to select devices, understand permissions, preview media, detect failures, choose initial mute/camera state, and recover before entering the shared call.
---

# Designing Call Join Device Checks

The pre-join surface is a local readiness checkpoint between private device state and a shared live session. It should let users intentionally choose what media will become visible or audible and detect failures before joining.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns the communication session. This skill owns pre-join media permission, device selection, preview, diagnostics, and initial publication state.

## Device and Permission Model
Separate OS/browser permission, device enumeration, selected input/output, device availability, media capture success, and call publication state. Camera permission granted does not mean video will be published; microphone selected does not mean it is unmuted.

Show a preview that is genuinely sourced from the selected camera and an input-level indicator for the selected microphone where feasible. For audio output, use a test sound only where platform capabilities permit. When labels are hidden before permission, avoid presenting duplicate “Device 1” choices as meaningful identification.

## Initial State
Make microphone and camera join state explicit at the final action. Respect remembered preferences only when safe and visible; do not surprise users by joining unmuted because a previous session used that state. For sensitive contexts, default policy may be muted/camera-off, but product requirements outrank generic preference.

## Failure and Fallback
Distinguish denied permission, no device, device busy, capture failure, unsupported browser, network/media path failure, and device disappearing mid-preview. Offer retry, choose another device, join listen-only, join without video, or open system settings according to capabilities.

## Evidence
Test first-time permission, prior denial, multiple microphones/cameras, Bluetooth connect/disconnect, device busy in another app, browser refresh, revoked permission, no camera, muted hardware switch, and network-limited conditions. Verify the actual published tracks after join match the pre-join controls.

## Failure Modes
- Preview shows one camera while another is published.
- Permission granted is shown as “mic on.”
- Remembered preference causes unexpected unmuted join.
- Device labels change and selection silently jumps to default.
- Permission denial is treated as no hardware.
- Join button blocks entirely when listen-only participation is allowed.

## Falsification
Select a non-default camera and muted microphone, disconnect another device, then join. Falsify if published tracks do not match the visible pre-join state. Deny camera permission; falsify if the UI claims hardware absence rather than permission state.

## Recovery
Re-enumerate devices, preserve selection by stable identity when possible, re-confirm publication toggles, and offer bounded fallback modes. If track publication cannot be verified after join, show the degraded state instead of assuming success.

## Handoff
Participant layout after entry belongs to `designing-call-participant-layouts`; screen source selection to `designing-screen-share-control`; encryption guarantee to security owners.

## Output Contract
Return a `call-join-device-checks-contract` with `permission_states[]`, `device_selection`, `preview_binding`, `initial_publication_state`, `failure_taxonomy`, `fallback_modes[]`, `prejoin_diagnostics`, `published_track_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.