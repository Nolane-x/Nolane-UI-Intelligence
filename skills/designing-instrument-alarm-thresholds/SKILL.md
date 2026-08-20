---
name: designing-instrument-alarm-thresholds
description: Own alarm threshold configuration and review for instruments, including units, high/low bands, hysteresis, delay, latching, acknowledgement, authority, and change provenance.
---
# Designing Instrument Alarm Thresholds

## Decision ownership

Own the interface for defining and understanding measurement-triggered alarm thresholds. Decide high/low limits, warning versus trip levels, units, hysteresis/deadband, persistence delay, latching, acknowledgement semantics, effective scope, permissions, and audit. This owner does not determine scientifically correct threshold values; it prevents configuration ambiguity and alarm chatter.

## Inputs and evidence

Require channel identity/unit/range, threshold policy, current values, valid operating envelope, warning/trip levels, hysteresis/delay capabilities, latch/ack rules, notification routing, role authority, and historical alarm frequency. Identify unit conversion and sensor configuration changes that could invalidate a threshold.

## Procedure

Bind thresholds to stable channel identity and explicit engineering unit. Show warning and critical/trip bands together with current value and valid instrument range. Hysteresis and persistence delay need visual or textual explanation of when alarm enters and clears. Preview threshold changes against recent data where useful to reveal likely chatter. Changing a threshold records old/new, actor, time, rationale, and effective moment. Acknowledgement should mean "seen/owned", not "condition cleared". Disabled/suppressed alarms remain visible with reason/expiry.

## Failure topology

Failures include thresholds stored in old units after unit change, warning above trip due invalid ordering, no hysteresis causing chatter, acknowledgement clearing the underlying alarm state, temporary suppression becoming permanent, and threshold changes with no provenance. Another failure is a slider implying precision or range that the sensor cannot support.

## Falsification

Reject if channel/unit binding is ambiguous; if invalid threshold ordering can commit; if hysteresis/delay effect cannot be understood; if acknowledgement makes an active condition disappear; if suppression has no owner/expiry; if unit/config changes can silently reinterpret thresholds; or if change history cannot reconstruct prior limits.

## Output contract

Return an `instrument-alarm-thresholds-contract` with: channel/unit binding; warning/trip high/low limits; ordering validation; hysteresis; persistence delay; latch/clear/ack states; suppression/disable governance; change preview/history; authority; and invalidation on unit/config change. Include one unit-conversion and one chatter scenario.

## Handoffs

Telemetry and trend views display alarm context, setpoint controls remain separate, safety interlocks may impose non-overridable trip logic, and incident operations consume active operational alarms.