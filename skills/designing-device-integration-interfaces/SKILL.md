---
name: designing-device-integration-interfaces
description: Use when software depends on cameras, scanners, printers, nearby devices, sensors, displays, or other hardware and the product needs one state model for capability, permission, connection, ownership, interruption, and fallback.
---

# Designing Device Integration Interfaces

## Parent Contract
**Required parent:** `adapting-platform-conventions`.

This faculty owns the product-level boundary between software state and external hardware state. It is the parent for capture, pairing, discovery, printing, location, displays, and sensors in this batch. It does not own a specific device protocol.

## Decision Boundary
Model hardware interactions using explicit states: unsupported, unavailable, permission unknown, permission denied, ready, discovering, connecting, connected, busy, interrupted, disconnected, and failed where relevant. Distinguish product capability from current device presence. A laptop may support camera capture while no usable camera is currently available; a printer may be known but offline.

Define authority among OS permissions, device connection, app selection, and current task. UI must never claim a device action succeeded only because an API call was issued; wait for device/platform acknowledgment when consequence matters. Hardware can disappear asynchronously, so every long-lived operation needs interruption behavior and a software fallback or recovery path when possible.

## Failure Topology
- A device button is enabled because the browser exposes an API even though no device is available.
- Permission denied, device absent, and device busy all collapse into “Something went wrong.”
- UI keeps showing Connected after Bluetooth/USB/network device disappears.
- A hardware operation is retried blindly after the device already completed it, causing duplicate output.
- Platform settings are required for recovery but the UI gives only an in-app retry loop.
- Device selection persists across machines and points to a nonexistent identifier.

## Falsification and Recovery
Test unsupported platforms, no device, first permission, denied/revoked permission, hot-plug/disconnect, busy device, OS interruption, app restart, stale saved selection, and success acknowledgment. The design fails if software state can remain green while the physical capability is unavailable or if recovery requires users to infer the failing layer.

Recover by separating capability/permission/presence/connection/task states, listening to authoritative platform changes, scoping saved selections to stable device identity, and routing recovery to the layer that can actually resolve the problem.

## Output Contract
Return `device-integration-contract` with canonical hardware states, platform/permission/device/task authorities, selection persistence, acknowledgment semantics, interruption/disconnect behavior, fallback strategy, and device-integration verification cases.
