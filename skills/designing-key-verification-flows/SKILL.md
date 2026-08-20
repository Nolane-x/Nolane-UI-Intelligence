---
name: designing-key-verification-flows
description: Use when users verify another person or device's cryptographic identity through QR, emoji, short codes, device comparison, or other ceremonies and the interface must resist accidental trust, mismatch, coercion, and stale verification.
---

# Designing Key Verification Flows

Key verification is an explicit ceremony that turns cryptographic comparison into a human trust decision. It should be difficult to approve accidentally, easy to abort on mismatch, and clear about exactly which identity/device state becomes trusted.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns communication security state. This skill owns the verification ceremony and resulting trust record; general encryption availability belongs to `designing-end-to-end-encryption-state`.

## Ceremony Scope
State whether the user is verifying a device, a person through a device set, or a cross-signing identity according to protocol. Do not use “Verify user” if the action only trusts one transient device and future devices remain unverified.

Verification methods may include QR scan, side-by-side emoji, short authentication string, or out-of-band code. Show both parties the same ordered comparison and require an explicit match decision after comparison. Never preselect “matches” or place confirm adjacent to routine navigation.

## Mismatch and Abort
Mismatch is a security event, not a validation error to click through. Provide a clear “does not match” path that leaves trust unchanged and offers safe next steps such as retry from a trusted channel, inspect devices, or contact the person independently. Do not encourage users to repeat until values happen to match.

Handle interruption, app backgrounding, device rotation, remote cancellation, and expired verification session. A resumed ceremony must prove it is the same session; otherwise restart with new values.

## Post-Verification State
After success, show which identity/device became verified and synchronize trust to other trusted devices only if the protocol supports it. New devices should appear as new trust decisions according to policy. Preserve verification time/method for inspection without exposing sensitive key material unnecessarily.

## Evidence
Test matching and mismatching codes, scanning the wrong person's QR, remote cancellation, replay/expired session, new device after prior verification, multiple devices, and restored encryption keys without verification. Verify trust store state before and after every path.

## Failure Modes
- Confirm button is active before comparison evidence is shown.
- “User verified” is claimed when only one device is trusted.
- Mismatch offers “continue anyway” as a routine secondary action.
- Resuming an expired session reuses stale comparison values.
- Key recovery automatically marks identity verified.
- Verification result does not identify the device/person scope.

## Falsification
Complete verification on one device, add a second unverified device, then restore keys to it. Falsify if trust spreads beyond protocol guarantee. Run a mismatch session; falsify if any path marks trust without a fresh matching ceremony.

## Recovery
Clear stale ceremony state, keep trust unchanged on mismatch/uncertainty, regenerate comparison values, and present device-level scope. If verification evidence cannot be confirmed, require a new ceremony rather than inferring trust from successful decryption.

## Handoff
Encryption/decryption status remains with `designing-end-to-end-encryption-state`; membership identity context comes from `designing-room-channel-membership`.

## Output Contract
Return a `key-verification-flows-contract` with `verification_scope`, `methods[]`, `session_identity`, `comparison_steps`, `explicit_match_action`, `mismatch_path`, `expiry_interruption_rules`, `post_verification_state`, `trust_store_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.