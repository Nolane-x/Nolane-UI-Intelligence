---
name: designing-medical-safety-critical-ui
description: Use when a UI contributes to medical, clinical, laboratory, industrial, emergency, or other safety-critical tasks where use error, delayed response, misidentification, alarm handling, or incorrect values can cause harm.
---

# Designing Medical and Safety-Critical UI

## Overview
Safety-critical UI is a risk-control system. Design from critical tasks, foreseeable use error, environment, and consequence; visual polish cannot compensate for ambiguous identity, units, state, alarm meaning, or confirmation.

## Parent Contract
**Required parent:** `routing-ui-work`.

Mandatory companions: `engineering-human-factors`, `conducting-task-analysis`, and `designing-high-stakes-decisions`; material completion requires `critiquing-human-factors-and-safety`. Require product classification/domain expert input and applicable regulatory/standard obligations. NUI does not certify regulatory compliance.

## Decision Model
Identify critical tasks where incorrect or omitted action could create serious harm. For each, bind the correct subject/object identity, parameter/value, unit, current state, intended action, consequence, and verification. Make similar-name/similar-value confusion pairs explicit. Critical context must not disappear because a row is compact.

Use hierarchy by risk and action, not aesthetics. Alarms distinguish priority, source, active condition, acknowledgement, silenced/suppressed state, resolution, and escalation. Warning fatigue is itself a hazard; do not turn every abnormal state red and modal.

Values need unit, range/context, freshness, source, and trend where decisions depend on change over time. Avoid silent unit conversion. Input constraints should prevent impossible values when domain rules allow; do not autocorrect a clinically meaningful value without making the change visible.

Design resilience: network loss, device disconnect, stale data, interrupted workflow, partial order, duplicate submission, and handoff between users/shifts. Maintain audit/traceability where the product requires it without overloading the operational view.

## Evidence
Use formal human-factors/usability process appropriate to the product, realistic representative users/environments, critical-task scenarios, hazard/use-related risk analysis, domain review, alarm tests, accessibility, interruption/recovery, and regulator-required validation. Desktop prototype walkthrough is not sufficient evidence for a safety claim.

## Output Contract
Return a `medical-safety-contract` with `critical_tasks[]`, `hazardous_use_scenarios[]`, `identity_and_value_checks[]`, `alarm_model`, `unit_and_freshness_rules`, `input_constraints[]`, `interruption_recovery`, `degraded_mode`, `traceability_needs`, `formal_validation_dependencies[]`, and `residual_risks[]`.

## Failure Traps
- Patient/object identity reduced to one ambiguous name.
- Unit omitted because “users know it.”
- Acknowledged alarm styled as resolved.
- Every warning using identical red modal treatment.
- Silent stale values after connectivity loss.
- Confirmation asking “Are you sure?” without subject/action/value.
- Claiming FDA/IEC compliance from this skill alone.

Safety design ends where evidence ends; uncertainty remains visible and blocking.