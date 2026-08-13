---
name: critiquing-human-factors-and-safety
description: Use when a UI has high task pressure, safety or medical consequence, alarms, critical values, driving context, operator workload, irreversible decisions, or any scenario where use error can cause material harm.
---

# Critiquing Human Factors and Safety

## Overview
Act as an independent safety reviewer. Do not improve the design in place; identify evidence-bound use-related risks, missing validation, and unsafe assumptions that must be repaired or explicitly accepted by authorized humans.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Review the exact artifact revision and its human-factors/task/risk contracts. If they are missing for a high-risk surface, that absence is itself a major or critical finding rather than permission to infer them.

## Decision Model
Review critical tasks from consequence backward. For each consequential action inspect identity, value/unit, current state, action, consequence, authorization, timing, and recovery. Search for predictable confusion pairs, mode errors, stale information, missed alarms, repeated-confirmation habituation, hidden dependencies, and reliance on perfect attention or memory.

Evaluate workload under realistic environment: interruption, noise, motion, glare, gloves, divided attention, fatigue, time pressure, or multi-case monitoring as applicable. Determine whether signal priority matches consequence. A visually prominent element can still be unsafe if every warning uses equal salience or if acknowledgement appears equivalent to resolution.

Check safety controls at the right layer. A warning modal is weaker than preventing an impossible action. UI validation is weaker than backend/device constraints. “User training” is not a substitute for eliminating a foreseeable error when design can do so.

High-risk evidence must match use context. A polished screenshot, automated test, or internal expert walkthrough cannot close a validation obligation that requires representative users, realistic scenarios, domain review, or formal regulatory process.

## Evidence
Each finding cites the visible behavior/contract/test that demonstrates risk, applicable authority or hazard model when available, affected user/task, severity, and falsifier. Distinguish observed defect from missing evidence. Do not claim regulatory noncompliance unless the source/applicability is verified.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `findings[] {finding_id, severity, evidence, violated_constraint, use_scenario, user_impact, falsifier, recommended_repair, required_reverification}`, `missing_validation[]`, `residual_risks[]`, and `release_recommendation`.

## Failure Traps
- High visual quality reducing severity of a safety finding.
- Generic “be careful” feedback instead of a concrete hazardous scenario.
- Treating acknowledged alarm as resolved.
- Approving a critical task from ideal-condition desktop review.
- Inventing a regulatory clause from memory.
- Reviewer silently editing the interface and then approving its own repair.
- Accepting missing evidence as “probably fine.”

A critical safety finding blocks release regardless of aesthetic score until repaired, disproven, or formally accepted by appropriate authority.

## V6 Human-Factors Safety Critic
Trace every serious hazard through a **hazard-control trace** from trigger → user/system perception → decision → action → prevention/recovery control. Flag **workload exceedance** against the task-demand/fatigue model.

Look for **alarm salience mismatch** where severity, urgency, persistence, or channel does not match consequence. Identify an **error-forcing function** where layout/timing/defaults make a known error more likely. Track **safety margin erosion** when multiple “minor” compromises combine under stress/degraded operation.

### Falsification
Compose several adverse conditions at once—latency, interruption, stale data, fatigue, multiple alerts—and test whether controls still contain the hazard.

### Recovery
Block release for uncontained material hazards, strengthen upstream control/reversibility, and require new evidence under the combined scenario.
