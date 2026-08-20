---
name: designing-nearby-device-discovery
description: Use when an app discovers local-network, Bluetooth, cast, USB, or proximity devices and users need trustworthy availability, deduplication, refresh, privacy, and selection before connection.
---

# Designing Nearby Device Discovery

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns the discovery list before pairing/connection. It abstracts multiple transport scans into user-meaningful nearby candidates without pretending transient radio/network visibility is stable inventory.

## Decision Boundary
Define discovery sources and permissions independently. Results need stable-enough identity to deduplicate the same physical target announced through repeated broadcasts or multiple protocols. Show device name/type/status plus location or identifier only when it helps disambiguation and is privacy-appropriate. Devices may appear/disappear as signal changes; avoid resorting the list aggressively under the user's pointer/focus.

Scanning should have a bounded lifecycle and visible refresh/retry. “No devices” must distinguish no permission, unsupported transport, scan still running, and genuinely empty result. Previously known devices can be surfaced separately from newly nearby candidates. Do not expose raw MAC addresses or proximity estimates unless product need and platform privacy permit them.

## Failure Topology
- Same TV appears three times from mDNS, cast, and Bluetooth advertisements.
- Device rows reorder every second by signal strength while users try to select one.
- Permission denial produces an empty list indistinguishable from no devices.
- Stale device remains selectable long after it disappeared.
- Raw hardware identifiers are exposed unnecessarily to ordinary users.
- Auto-connect selects the first discovered device before users confirm identity.

## Falsification and Recovery
Test zero/many devices, duplicate protocol advertisements, devices entering/leaving range, denied permission, network change, identical names, scan timeout, focus stability, and known-device history. The design fails if discovery instability can make users connect to a different device than the row they selected.

Recover by deduplicating stable identities, freezing row identity/order while interaction is active, separating known/nearby states, labeling permission/scan errors, and requiring selection before connection. Expire stale results with visible status rather than silent reuse.

## Output Contract
Return `nearby-device-discovery-contract` with discovery sources, permission dependencies, candidate identity/deduplication, row stability, scan/refresh lifecycle, stale-result handling, privacy fields, and discovery verification scenarios.
