---
name: designing-safety-interlock-interfaces
description: Own operator visibility and interaction with hardware or process safety interlocks, including cause, protected scope, latched state, reset prerequisites, bypass authority, and evidence that protection is active.
---
# Designing Safety Interlock Interfaces

## Decision ownership

Own the interface around safety mechanisms that inhibit or stop equipment/process actions when defined conditions are unsafe. Decide active/latched/bypassed/fault states, cause and protected scope, reset prerequisites, control inhibition, bypass visibility/authority, and audit. This owner never assumes the UI itself is the safety mechanism; hardware/validated control remains authoritative.

## Inputs and evidence

Require interlock identities, protected equipment/actions, trigger conditions, latched behavior, reset prerequisites, hardware/controller state, bypass policy, authorized roles, maintenance mode, sensor quality, and audit/notification requirements. Identify fail-safe versus fail-open behavior and what state is available if communications fail.

## Procedure

Display interlock state near every affected control and in a persistent safety summary. Distinguish active trip, latched-after-condition-cleared, bypassed, disabled-for-maintenance, fault/unknown, and healthy. Explain the triggering condition using authoritative telemetry without implying a cause that the controller did not report. Reset should remain unavailable until prerequisites are satisfied and should state what will be re-enabled. Bypass, if policy allows it, requires strong authority, reason, duration/expiry, scope, and unmistakable persistent indication. On communication loss, treat safety state as unknown according to policy rather than optimistic healthy.

## Failure topology

Failures include disabled controls with no interlock reason, bypass indicated only by color, reset becoming available before prerequisites, UI showing healthy because interlock telemetry is missing, stale latch state, and bypass surviving maintenance unnoticed. Another critical failure is letting UI copy suggest that clicking reset makes conditions safe.

## Falsification

Reject if affected controls cannot identify which interlock blocks them; if bypass state can be overlooked; if reset prerequisites are unknown; if communications loss renders healthy; if bypass lacks authority/reason/expiry; if interlock state conflicts with controller truth without a stale/unknown cue; or if the UI claims to supersede the physical safety system.

## Output contract

Return a `safety-interlock-interfaces-contract` with: interlock identity/scope; healthy/active/latched/bypassed/fault/unknown states; trigger evidence; affected controls; reset prerequisites/action; bypass authority/reason/expiry; maintenance mode; communications-loss behavior; audit/notifications; and explicit hardware-authority statement. Include one comms-loss and one temporary-bypass case.

## Handoffs

Setpoint/run controls consume interlock state, alarm thresholds may provide related warnings, calibration/telemetry supply evidence, and high-stakes/safety authorities govern reset/bypass confirmation. The physical safety controller remains authoritative.