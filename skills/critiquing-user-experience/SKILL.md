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

## Output: `finding-set`
Return typed findings with affected job/step, evidence, violated constraint, user impact, falsifier, and minimal repair direction. Recommend `BLOCK` when a primary task is impossible/unsafe or the UI materially lies about consequential state.

## V6 Task-Causal UX Critique
Reconstruct the user's task rather than critiquing screens as pages. Track **information scent** at each choice: what cue tells the user where an action leads, what object it affects, and whether it matches their vocabulary? Weak scent is especially damaging when navigation is visually polished but semantically generic.

Measure **time-to-action** as interaction steps plus cognitive/search cost for frequent and critical tasks. Do not optimize step count blindly: one explicit confirmation may reduce irreversible error, while three hidden menus can be worse than a longer visible workflow.

Estimate **recovery cost** for mistakes, interruptions, permission failures, network failure, destructive actions and AI errors: time, lost work, cognitive reconstruction, trust damage and reversibility. Empty/loading/error states are part of the task path, not secondary polish.

Look for **mode error**: the same gesture/control meaning changes because the user is in an implicit mode, focus is captured by a canvas/editor, or agent autonomy changed state. Make modes visible, reversible and distinguishable where they materially affect action meaning.

Audit **state visibility** across local component state, process state, system/network state and collaborative/agent state. Users should know what has happened, what is pending, what is editable, who/what owns an action, and whether their changes are saved/applied.

### Falsification
Run scenario traces with novice, returning and expert assumptions; long/error/empty states; keyboard/touch where relevant. If a criticism depends only on the critic preferring a different layout and cannot connect to task success, comprehension, error or trust, it is not a UX defect.

### Recovery
For repeated local usability defects, return to task flow/information architecture/state models rather than patching labels. When a feature is unreachable or action semantics conflict, functional closure takes precedence over visual refinement.
