---
name: engineering-human-factors
description: Use when UI performance depends on task pressure, use environment, operator capability, error consequence, alarms, workload, safety, or interactions where a technically valid action can still create use-related risk.
---

# Engineering Human Factors

## Overview
Model the interface as one part of a human–task–environment system. The objective is not generic ease of use; it is to make the intended action reliably perceivable, understandable, executable, and recoverable under the conditions in which people actually operate.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require the task profile to identify users, environment, frequency, time pressure, risk class, and critical outcomes. If those are unknown for a high-risk product, create an evidence gap instead of inventing a safe operating context.

## Decision Model
Build a `use system` with five linked layers: users and capability range; goals and task sequence; physical/social environment; interface and connected devices; consequences of correct, delayed, omitted, or incorrect action. Identify critical tasks by consequence, not by UI prominence. For each critical task ask: what must be noticed, discriminated, remembered, decided, manipulated, confirmed, and verified? What predictable misuse or mode confusion could occur?

Treat workload dynamically. A layout that works in a quiet usability lab may fail under interruption, gloves, glare, vibration, fatigue, noise, divided attention, or emergency pacing. Model error-likely situations and reduce reliance on vigilance. Prefer forcing functions, constraint, direct consequence preview, salient state, and recovery over repeated generic warnings.

Alarms require a signal model: priority, source, condition, onset, persistence, acknowledgement, resolution, escalation, suppression, and history. Acknowledging a warning must never visually imply that the underlying condition is resolved.

## Evidence
Use task observation, domain-expert review, error/incident data, realistic scenario tests, accessibility evidence, and applicable regulator/platform guidance. In safety-sensitive work distinguish simulated usability evidence from formal domain validation. Record environment and participant assumptions because they define transferability.

## Output Contract
Return a `human-factors-model` with `user_classes[]`, `use_environments[]`, `critical_tasks[]`, `information_requirements[]`, `error_modes[]`, `workload_factors[]`, `alarm_or_warning_model`, `risk_controls[]`, `residual_risks[]`, `validation_evidence_needed[]`, and `assumption_bounds[]`.

## Failure Traps
- Calling a workflow safe because users can complete it slowly in ideal conditions.
- Adding confirmation dialogs instead of removing the error opportunity.
- Equating acknowledgement with resolution.
- Optimizing average users while excluding realistic capability ranges.
- Ignoring environmental constraints such as glare, noise, gloves, vibration, or shared attention.
- Using aesthetic salience without a priority model.
- Claiming medical or safety validation from expert review alone.

Human factors succeeds when the design reduces dependence on perfect attention and perfect memory rather than merely documenting that users should be careful.

## V6 Human-Factors Demand Model
Build a **task-demand model** across perceptual discrimination, memory, attention switching, motor precision, decision complexity, time pressure, interruption, emotional load, and environmental constraints. The interface should shift demands toward channels with available capacity rather than merely reducing element count.

Assign a **workload budget** to critical sequences: number of simultaneously held facts, required cross-references, mode changes, alerts, manual transformations, and time-sensitive decisions. Use a **signal-detection threshold** when users must separate important events from noise; false alarms and misses have different costs and should shape alert salience and thresholds.

Model **error-cost asymmetry** explicitly. The optimal control for a reversible preference change is not the optimal control for medication, financial transfer, vehicle state, or destructive infrastructure action. Define a **fatigue-exposure envelope** using session duration, repetition rate, lighting/noise, posture, vigilance demands, and circadian/shift context where relevant.

### Falsification
Stress the design under realistic interruption, low signal prevalence, repeated operation, and degraded attention. If success depends on perfect memory or sustained vigilance beyond the task-demand model, the human-factors claim is false.

### Recovery
Redistribute information, externalize memory, automate safe transformations, reduce false alarms, increase reversibility, or change workflow timing. Do not “train the user harder” to compensate for avoidable interface demand.
