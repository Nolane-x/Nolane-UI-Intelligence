---
name: designing-background-location-awareness
description: Use when the product continues or requests location access outside an active foreground task and users need persistent awareness, purpose, control, battery/privacy boundaries, and recovery from platform restrictions.
---

# Designing Background Location Awareness

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns user-facing state for background location usage. It does not define whether the business is legally permitted to collect location; privacy/safety authority must establish purpose and retention. The UI ensures background collection is not invisible or confused with one-time foreground location.

## Decision Boundary
Separate foreground, while-in-use, background, and stopped states. Request background access only when the feature genuinely continues without the user looking at the app, and explain the concrete ongoing benefit. Show persistent in-product state and respect platform indicators/notifications rather than hiding them. Provide a direct stop/pause path that changes actual collection behavior, not just UI preference.

Battery and accuracy modes may be selectable when the feature supports them; describe consequences rather than implying precise continuous tracking if the OS batches updates. If background permission is downgraded by the platform, degrade functionality and surface the new state. Retention/sharing of location remains governed by privacy policy and should be reachable from the active feature.

## Failure Topology
- Background tracking continues after users toggle the feature “off” because only map display was disabled.
- Permission rationale says “better experience” without naming the ongoing background task.
- App requests Always access before users ever enable a background-dependent feature.
- Platform downgrades permission but UI still says Tracking active.
- Continuous-accuracy wording contradicts OS power-saving/batched behavior.
- Location history/sharing controls are disconnected from the feature that created the data.

## Falsification and Recovery
Test feature enable/disable, app background, force quit, permission downgrade, battery saver, OS indicators, restart, long idle periods, and privacy settings. The design fails if users cannot determine whether background collection is currently active or cannot stop it from the product/OS path.

Recover by binding visible active state to actual collection service, requesting permission at feature intent, handling platform downgrades, exposing pause/stop and retention/sharing context, and using bounded accuracy claims.

## Output Contract
Return `background-location-contract` with foreground/background states, purpose/rationale timing, persistent awareness, stop/pause semantics, battery/accuracy behavior, permission downgrade recovery, privacy handoff, and long-running verification cases.
