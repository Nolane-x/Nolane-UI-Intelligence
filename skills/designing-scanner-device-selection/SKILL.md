---
name: designing-scanner-device-selection
description: Use when dedicated document, flatbed, feeder, barcode, or network scanners are selectable and the interface must reconcile device identity, source capabilities, readiness, feeder state, and scan-job ownership.
---

# Designing Scanner Device Selection

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns choosing and preparing a dedicated scanner device. It is distinct from camera document capture. Hardware scanners expose sources such as flatbed/ADF/duplex, resolutions, color modes, paper size, and feeder errors that must match the intended job.

## Decision Boundary
Use platform/driver discovery as authority for available devices and capabilities. Persist selection only when identity is stable and scope is appropriate. Before scanning, validate source (flatbed/feeder), duplex, resolution, color, paper size, and feeder availability. Do not expose settings the driver will silently ignore. A scan job needs explicit start/cancel/progress and should identify the device so users do not load paper into another scanner.

Device busy, cover open, no paper, jam, offline, and driver permission errors are different recovery classes. Network scanners may disappear and return with stale session state. If users switch devices after configuring settings, revalidate against the new device rather than carrying incompatible options.

## Failure Topology
- Duplex remains selected after switching to a flatbed-only device.
- App says “Scanning…” while device is waiting for paper with no guidance.
- Two identical scanner names are indistinguishable across offices.
- Saved device selection resolves to a replaced scanner with different capabilities.
- Cancel button hides locally but scan continues physically and later imports pages unexpectedly.
- Driver error is shown as invalid document rather than device-layer failure.

## Falsification and Recovery
Test multiple devices, source changes, no paper/jam/busy/offline, switch-after-configure, network disconnect, cancel, driver failure, and app restart. The design fails if configured settings can exceed selected-device capability or if physical scan continues after UI claims cancellation.

Recover by capability-bound settings, stable identity/disambiguation, device-specific error states, acknowledged cancellation, and revalidation on device change. Route camera fallback separately when dedicated scanner is unavailable.

## Output Contract
Return `scanner-selection-contract` with discovery/identity, source/capability matrix, setting validation, readiness/errors, scan-job lifecycle, device switching, cancellation acknowledgment, and scanner verification cases.
