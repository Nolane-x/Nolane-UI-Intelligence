---
name: designing-supervisory-control-room-hmi
description: Use when operators monitor and control industrial, energy, utility, transport, manufacturing, nuclear, infrastructure, or other continuous processes where alarms, modes, trends, command authority, abnormal states, and shift handoffs determine safety and performance.
---

# Designing Supervisory Control-Room HMI

## Overview
A control-room HMI supports diagnosis and coordinated intervention over time. Design the operational picture around process state, deviation, cause, mode, trend, alarm priority, and command consequence rather than a decorative mimic diagram full of equally salient values.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require process model, operator roles, normal/abnormal/emergency states, control authority, alarm philosophy, update rates, handoff model, automation modes, safety classification, physical control room, and applicable industry standards. Mandatory companions are human factors and independent safety critique for safety-critical operation.

## Decision Model
Build information hierarchy from operator questions: Is the process within normal envelope? What changed? What is moving toward a limit? What caused the deviation? What automation/control mode is active? What action is available and what will it affect? A screen full of green values can hide the few relationships needed for diagnosis.

Use trends and deviation to support temporal reasoning. Current value alone is insufficient when rate/direction matters. Show units, limits, source/freshness, inhibited/bypassed state, and quality where operationally material. Alarm design distinguishes priority, new/active/acknowledged/shelved/suppressed/resolved states and avoids flooding operators with correlated consequences of one root event.

Control modes and authority must be explicit. Manual/automatic/remote/local/maintenance states change whether a command is accepted and who owns it. Command dialogs identify equipment, target/setpoint, current state, consequence/interlocks, and result. Failed or rejected command must not look like state change.

Support abnormal situation management and handoff. Preserve event history, outstanding alarms, bypasses, manual overrides, maintenance conditions, and work in progress across shifts. During high workload, stable layout and prioritized signals matter more than animation.

## Evidence
Use process simulator/scenario testing, representative operators, alarm floods, sensor bad-quality/stale data, mode transitions, command rejection, abnormal/emergency scenarios, shift handoff, hardware input, display failures, and applicable IEC/domain HFE validation. Consumer-dashboard usability is not sufficient evidence.

## Output Contract
Return a `supervisory-control-contract` with `operational_questions[]`, `process_overview`, `normal_envelope`, `trend_and_deviation_rules`, `alarm_state_model`, `mode_and_authority_model`, `command_verification`, `bad_quality_and_staleness`, `abnormal_situation_views`, `handoff_state`, `formal_validation_dependencies[]`, and `control_room_tests[]`.

## Failure Traps
- Every normal value colored bright green, creating visual noise.
- Alarm acknowledgement removing evidence of an unresolved condition.
- Current value without trend when rate is operationally critical.
- Manual/automatic mode difficult to distinguish.
- Command appears successful before plant feedback confirms it.
- Shift handoff loses bypasses or outstanding abnormal states.
- Generic web-dashboard design used to claim safety-critical HMI readiness.

A supervisory HMI is effective when operators can detect, diagnose, decide, act, and verify under abnormal conditions without reconstructing the process from scattered widgets.