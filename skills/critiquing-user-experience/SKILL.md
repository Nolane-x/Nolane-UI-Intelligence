---
name: critiquing-user-experience
description: Use when an independent reviewer must find task friction, ambiguity, dead ends, unsafe decisions, trust problems, misleading feedback, or unnecessary cognitive load in a UI flow.
---

# Critiquing User Experience

## Overview
Review the interface as a task system. Visual polish neither excuses nor proves UX quality.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Use product intent, user/task model, IA, flow, interaction contract, and observed artifact/behavior.

## Walk critical jobs
For each primary task inspect:
- entry: can the user find the start from realistic context?
- orientation: do they know object/scope/state?
- decision: is required information present at the moment of choice?
- action: is outcome predictable?
- feedback: does system state remain truthful?
- error: can they recover without losing unrelated work?
- completion: is success evidenced and is the next likely action clear?

## Friction taxonomy
Classify findings:
- discoverability
- comprehension/vocabulary
- unnecessary decision
- excessive interruption
- hidden dependency
- state ambiguity
- feedback latency
- destructive risk
- permission/trust mismatch
- dead end
- context loss
- expert inefficiency
- novice overload

Do not count clicks mechanically. One additional step that clarifies irreversible scope can be valuable; one modal per trivial edit can be harmful.

## Counterfactual users
Where relevant, replay as novice, expert, interrupted user, limited-permission user, and user returning from stale state. Do not invent personas; vary capabilities/context that matter to the task.

## Trust review
Check whether the UI implies certainty, completion, privacy, authorization, freshness, or reversibility the product cannot guarantee. Deceptive cleanliness is a major UX defect.

## Output
Return typed findings with affected job/step, evidence, violated constraint, user impact, falsifier, and minimal repair direction. Recommend `BLOCK` when a primary task is impossible/unsafe or the UI materially lies about consequential state.
