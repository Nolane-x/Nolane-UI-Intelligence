---
name: designing-nfc-interactions
description: Use when near-field taps read tags, exchange records, provision devices, authenticate, or initiate product actions and the interface must manage proximity, capability, session timing, payload trust, and repeated reads.
---

# Designing NFC Interactions

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns user interaction around NFC read/write sessions. It does not assume NFC payload is trusted. The user may need to physically hold a device near a tag for a short platform-owned window; software must show when scanning is active and what a successful read means.

## Decision Boundary
Declare read versus write/provision tasks and platform capability. Some systems expose system sheets instead of continuous app scanning. Start sessions only when user intent is clear, provide physical placement guidance without requiring exact visual alignment, and end or throttle after success to prevent repeated reads. Classify/validate payload before executing consequential actions.

Writing tags has stronger confirmation because it can modify a physical object. Verify the target tag and capacity/lock state where possible. For provisioning or authentication, use cryptographic/domain validation rather than tag UID as sole trust. If NFC is unsupported or disabled, offer the real recovery path—settings, QR/manual code, or another device—not an endless retry.

## Failure Topology
- NFC scan runs continuously in the background without visible user intent.
- Same tag triggers the action multiple times while held near the phone.
- Tag UID is treated as secure authentication despite being cloneable.
- Write flow overwrites a tag before showing the new payload/consequence.
- “No tag found” hides that NFC is disabled in system settings.
- Visual-only placement animation gives no usable guidance to blind users.

## Falsification and Recovery
Test unsupported/disabled NFC, first permission/system sheet, repeated same tag, multiple tags, malformed/untrusted payload, read versus write, locked/low-capacity tag, timeout, and alternative path. The design fails if mere proximity can execute a high-impact payload without validation or confirmation.

Recover by explicit session state, duplicate suppression, payload validation, stronger write confirmation, settings/alternative recovery, and nonvisual placement/status feedback. Keep physical tag identity distinct from application authority.

## Output Contract
Return `nfc-interaction-contract` with read/write modes, activation/session lifecycle, proximity guidance, duplicate suppression, payload validation/trust, write confirmation, unsupported/disabled recovery, and NFC verification cases.
