---
name: conducting-task-analysis
description: Use when a UI supports complex goals, expert workflows, branching decisions, handoffs, safety-critical actions, repeated operational work, or a redesign risks optimizing screens before understanding the work itself.
---

# Conducting Task Analysis

## Overview
Decompose work before decomposing screens. Task analysis identifies what people are trying to accomplish, the information and decisions each step requires, where errors occur, and what the interface must preserve across interruptions and handoffs.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume product intent and user/task model when available. If stakeholders provide only a screen list, treat it as implementation history rather than proof of the correct task structure.

## Decision Model
Start from an observable end condition: what becomes true when the user succeeds? Map normal, alternate, exception, and recovery paths. For each step record trigger, required information, decision, action, resulting system state, feedback, and next dependency. Distinguish user goal from system operation; “submit POST request” is not a user task.

Identify critical transitions: irreversible actions, context switches, permission boundaries, external handoffs, waiting states, mode changes, and places where users must reconcile two representations. Mark information that must persist. If step B requires remembering a value from step A, decide whether that memory demand is inherent or an interface defect.

Analyze frequency and expertise. Repeated expert tasks benefit from stable spatial memory, batch operations, shortcuts, and fewer forced confirmations. Rare/high-consequence tasks may benefit from richer consequence previews and guided verification. Optimize the path with the highest weighted impact, not automatically the shortest path.

Use failure-oriented decomposition: what if data is stale, permission changes, network drops, another collaborator edits the object, AI output is partial, hardware is unavailable, or the user resumes tomorrow?

## Evidence
Ground analysis in observation, domain interviews, existing logs/support evidence, current workflow artifacts, incident/error data, and realistic scenarios. Mark inferred steps as assumptions. Validate high-consequence sequences with domain experts or representative users rather than UI intuition alone.

## Output Contract
Return a `task-analysis` with `goal`, `success_state`, `actors[]`, `normal_path[]`, `alternate_paths[]`, `critical_transitions[]`, `information_dependencies[]`, `memory_dependencies[]`, `error_modes[]`, `recovery_paths[]`, `frequency_and_expertise`, and `evidence_gaps[]`.

## Failure Traps
- Treating current navigation as the task model.
- Click-count optimization that removes necessary verification.
- Screen-by-screen analysis with no end-to-end state transitions.
- Ignoring waiting, background, or handoff periods.
- Assuming exceptions are edge cases when operators handle them daily.
- Forcing experts through novice onboarding every time.
- Designing recovery after the happy path is already frozen.

Task analysis should make the later IA and interaction architecture feel inevitable rather than ornamental.