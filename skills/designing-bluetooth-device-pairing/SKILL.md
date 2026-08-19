---
name: designing-bluetooth-device-pairing
description: Use when users pair Bluetooth peripherals and the product must distinguish OS discovery, pairing, bonding, app connection, permissions, device identity, and reconnect behavior.
---

# Designing Bluetooth Device Pairing

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns the pairing journey, not the full operation of the connected device. Bluetooth has layered states: discoverable hardware, OS-level paired/bonded device, app permission, profile/service compatibility, and active application connection. UI must not collapse them into one “Connected” toggle.

## Decision Boundary
Define which pairing layer the app controls versus OS settings. Some platforms require system pickers; others let apps scan after permission. Present device names with disambiguating identifiers only when needed, and handle identical-name peripherals. Pairing codes/passkeys must clearly identify the intended device and expire safely. After pairing, service discovery can still fail; report incompatibility separately from pairing failure.

Persist stable device identity where platform permits, but expect identifiers to rotate under privacy rules. Automatic reconnect should honor explicit forget/disconnect choices. If the user pairs at OS level outside the app, the app should reconcile rather than forcing a second fake “pair” workflow.

## Failure Topology
- UI says Pairing succeeded although required Bluetooth service is unsupported.
- Two devices named “Sensor” are indistinguishable and users pair the wrong one.
- Denied nearby/Bluetooth permission is reported as “No devices found.”
- App forget button removes only app state while OS remains bonded, creating confusing rediscovery.
- Auto reconnect immediately reconnects after user explicitly disconnects.
- Passkey is shown without device identity and users confirm on the wrong peripheral.

## Falsification and Recovery
Test permission states, identical names, OS-prepaired device, pairing code, incompatible service, device power-off, app restart, explicit disconnect/forget, identifier change, and reconnect. The design fails if users cannot tell whether failure is permission, pairing, compatibility, or active connection.

Recover by exposing layered state, using system-authoritative pairing where required, disambiguating identity, honoring disconnect intent, and reconciling OS/app state. Route unsupported profiles to capability explanation rather than repeated pairing.

## Output Contract
Return `bluetooth-pairing-contract` with pairing layers/states, permission/system-picker ownership, device identity/disambiguation, passkey flow, compatibility check, reconnect/forget semantics, and Bluetooth verification cases.
