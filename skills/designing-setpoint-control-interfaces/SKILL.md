---
name: designing-setpoint-control-interfaces
description: Use when this specialist's decision ownership is materially in scope. Own operator changes to instrument or process setpoints with present/target distinction, units, bounds, ramping, authority, preview, acknowledgement, and verification of actual effect.
---
# Designing Setpoint Control Interfaces

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own intentional changes to controlled target values such as temperature, pressure, speed, flow, or voltage. Decide current setpoint versus measured process value, target entry, allowable range, rate/ramp, step size, pending/application state, control authority, and confirmation proportional to consequence. This owner does not implement control loops.

## Inputs and evidence

Require control variable identity/unit, current measured value, current setpoint, safe/allowed bounds, precision, ramp/step capabilities, interlocks, operator roles, command latency, device acknowledgement, and process response expectations. Identify setpoints where abrupt changes can damage equipment or samples.

## Procedure

Keep measured value, active setpoint, and proposed setpoint distinct. Validate units/range before commit and show rate/ramp semantics when the device transitions gradually. High-impact changes need consequence preview including target equipment and expected transition. After command, show pending/acknowledged/applied/failed state; do not immediately replace active value on optimistic UI if the instrument has not accepted it. Track who changed what and when. If local/manual control or another operator owns authority, disable with explanation rather than accepting doomed commands.

## Failure topology

Failures include measured value mistaken for setpoint, unit mismatch, overly coarse sliders, optimistic state showing a target that device rejected, simultaneous operators issuing competing values, setpoint change blocked by interlock with generic error, and no indication that ramping is still in progress.

## Falsification

Reject if active/proposed/measured values are visually confusable; if bounds/units are unknown; if command success is shown before device acknowledgement; if another control owner can override silently; if a rejected interlock command gives no reason/source; or if ramping has no current progress/target indication.

## Output contract

Return a `setpoint-control-interfaces-contract` with: controlled variable/unit; measured/active/proposed values; allowable bounds/precision; ramp/step behavior; authority; validation; consequence preview; command states; device acknowledgement; interlock response; concurrency policy; and audit history. Include one rejected command and one ramped transition.

## Handoffs

Safety interlocks govern hard constraints, alarm thresholds observe deviations, process trends show response, experiment run control binds setpoint changes to run provenance, and high-stakes controls govern dangerous changes.