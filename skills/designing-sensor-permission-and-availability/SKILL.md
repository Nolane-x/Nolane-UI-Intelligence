---
name: designing-sensor-permission-and-availability
description: Use when motion, orientation, microphone-like environmental sensors, proximity, health, or other sensor data depends on platform permission, hardware presence, calibration, sampling, and degraded fallback.
---

# Designing Sensor Permission and Availability

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns the precondition model for sensor-dependent features. It does not define every sensor's domain interpretation. It distinguishes API support, physical sensor presence, permission, platform privacy restriction, calibration/quality, sampling availability, and feature readiness.

## Decision Boundary
Inventory the exact sensors and why each is needed. Request only at feature intent and group prompts only when purposes are genuinely connected. Some browsers expose APIs but gate them behind gestures or permission; some devices emulate values; some privacy modes reduce precision. Feature readiness must use the minimum trustworthy capability required, not a generic “sensor enabled” flag.

Provide fallback when the sensor is absent or denied: manual entry, device selection, reduced-precision mode, keyboard controls, or explicit unsupported state depending on task. If calibration is required, separate calibration quality from permission. Sampling can pause in background or under power policy; show stale/paused state rather than treating last sample as current.

## Failure Topology
- App requests every sensor permission on launch with no feature context.
- API existence is treated as proof the physical sensor is present and producing valid samples.
- Denied permission and low-quality calibration both show “sensor unavailable.”
- Background suspension leaves the last sample displayed as live telemetry.
- Feature blocks despite a valid manual fallback.
- Reduced-precision privacy mode is treated as exact measurement and causes wrong downstream behavior.

## Falsification and Recovery
Test unsupported hardware, API-supported/no sensor, first deny/revoke, calibration failure, reduced precision, background suspension, sampling loss, multiple device sources, and fallback entry. The design fails if stale or low-confidence sensor data is represented as current exact truth.

Recover by modeling support/presence/permission/quality/freshness separately, prompting at feature intent, degrading to alternative input, and labeling precision/freshness. Re-check capability after resume and platform-setting changes.

## Output Contract
Return `sensor-availability-contract` with required sensors/purpose, support/presence/permission states, precision/calibration/freshness, prompt timing, background behavior, fallback modes, and sensor capability verification cases.
