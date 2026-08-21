---
name: designing-driving-state-interaction-lockouts
description: Use when an automotive interface must enable, simplify, defer, or block interactions according to driving state, vehicle motion, task demand, legal/platform constraints, or driver role while preserving clear recovery paths and essential controls.
---

# Designing Driving-State Interaction Lockouts

## Lockouts are authority decisions
An automotive UI cannot treat all interactions as equally available at all times. Vehicle motion, driver workload, jurisdictional constraints, system state, and task type may require some interactions to be simplified or deferred. This skill owns the interface contract that decides which actions are available in each authoritative driving state and how unavailable actions are explained.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent establishes high-stakes decision principles: authority, error containment, evidence, and conservative behavior under uncertainty. This specialist begins when interaction availability depends on vehicle/driving context.

## State inputs and precedence
Use authoritative vehicle-state inputs where available: parked/moving, gear state, speed class, driver/passenger role, automation mode, and system health. Do not infer safety-critical availability from animation state or stale UI cache. Define precedence for conflicting signals and an explicit unknown state. Unknown should not silently fall through to the most permissive mode.

The decision owner is the action availability matrix. Classify tasks by demand and consequence rather than by screen. A screen may contain both always-available essential controls and high-demand configuration that should defer. Lock the risky action, not necessarily the entire surface.

## Presentation of unavailable actions
When an action becomes unavailable, preserve context where safe. Explain the condition in concise language such as “Available when parked” rather than making the control disappear without reason. If the user was mid-task when state changed, preserve draft data and define whether the flow pauses, simplifies, or exits.

Avoid repeated prompts that encourage the driver to fight the lockout. Offer a safe continuation path: passenger completion, voice alternative where permitted and reliable, or resume-later state. Alternative modalities must be independently evaluated; voice is not automatically low-distraction.

## Transition behavior
Driving state can change while a control is focused or a dialog is open. Reevaluate before executing side effects. If a formerly allowed action becomes blocked, prevent the action and preserve the user’s work. When state becomes permissive again, restore only still-valid context and never auto-execute the previously blocked action.

## Evidence
Evidence includes authoritative state inputs, availability matrix, transition traces, blocked-action copy, preserved draft behavior, and tests for stale/unknown signals. Validate representative state transitions rather than only static parked/moving screenshots. Regulatory or OEM obligations should be versioned and cited separately from design heuristics.

## Failure modes
Characteristic Failure includes checking driving state only when the screen opens, hiding essential controls with a blanket lockout, using stale speed/gear state, allowing a focused action to execute after motion begins, losing user input when a task becomes blocked, and replacing one high-demand interaction with an equally demanding alternative.

## Falsification
Change driving state at the moment of activation, inject stale/unknown signals, switch driver/passenger role, and resume a partially completed task after returning to a permissive state. The contract fails if a blocked action executes, if unknown state defaults to permissive without authority, if essential controls vanish, or if resume bypasses current-state validation.

## Recovery
On state ambiguity, move affected high-demand actions to a conservative blocked/deferred state while keeping essential information available. Requery authoritative vehicle state, preserve valid drafts, and re-enable only after current conditions are proven. If a lockout rule is wrong or conflicting, escalate to the governing safety/platform authority rather than patching presentation locally.

## Output and Handoff
Output: `driving-state-interaction-lockouts-contract`, containing authoritative inputs, action-demand classes, availability matrix, transition handling, explanation copy, draft preservation, and evidence. Handoff warning urgency to vehicle-warning priority and role distinctions to driver/passenger authority splits.

## Sibling Boundary and delete-the-skill
Sibling vehicle-state-dependent controls governs controls whose semantics/value change with vehicle state; this skill governs whether an interaction may occur at all. Distraction-aware density governs information load, not action permission. The delete-the-skill test passes because without this owner, lockout logic becomes scattered screen conditions that can miss transition races and authoritative-state uncertainty.