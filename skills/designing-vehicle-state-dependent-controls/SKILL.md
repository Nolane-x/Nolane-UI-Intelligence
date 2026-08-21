---
name: designing-vehicle-state-dependent-controls
description: Use when an automotive control’s meaning, valid range, availability, feedback, or consequence changes with vehicle state and the UI must bind the control to authoritative state so stale or visually similar controls cannot issue the wrong action.
---

# Designing Vehicle-State-Dependent Controls

## The same control can mean different things in different states
Climate, charging, drive modes, suspension, doors, lighting, assistance settings, parking functions, and vehicle configuration often depend on current vehicle state. A control that is valid while parked may be unavailable in motion; a value may represent a target in one mode and current state in another. This skill owns the semantic binding between authoritative vehicle state and control behavior.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent establishes conservative high-stakes decision rules. This specialist begins when a control remains part of the interface but its valid action semantics depend on current vehicle context.

## Control-state contract
Represent `(control_identity, authoritative_vehicle_state, displayed_value, allowed_commands, command_preconditions, feedback_state, transition_policy)`. The decision owner is which commands are valid under each state and how the interface communicates a semantic change.

Do not infer command validity from the rendered value alone. Revalidate authoritative state immediately before a side effect when state can change rapidly. If the vehicle enters a state where a control no longer applies, disable or transform it with an explanation rather than letting it send a stale command.

## Value semantics and modes
A slider, toggle, or selector may need different bounds, units, or interpretation by mode. Make mode changes visible enough that the user does not carry the previous mental model forward. Avoid reusing identical control appearance when the consequence changes materially.

When an action is pending, separate requested target from confirmed vehicle state. A user-selected climate target may update optimistically, but a door lock or charging command should still expose whether the vehicle acknowledged the change. Commanded state is not necessarily actual state.

## Transitions
State changes can occur externally: another occupant acts, a physical switch changes, the vehicle moves, charging connects/disconnects, or a subsystem enters fault. The UI should reconcile quickly and preserve user intent only when still valid. Do not retry a command automatically if its precondition no longer holds.

## Evidence
Evidence includes authoritative state source, state-to-command matrix, rendered control semantics, pre-dispatch validation, command acknowledgement, actual-state confirmation, and external-transition scenarios. Test state changes while the control is focused, while a command is pending, and immediately before activation.

## Failure modes
Characteristic Failure includes showing a toggle as on because a command was sent but the vehicle rejected it, retaining a valid-looking control after its precondition disappeared, reusing the same label for materially different mode semantics, retrying commands after state changed, and stale cached state enabling an unavailable action.

## Falsification
Change vehicle state immediately before activation, reject a command after optimistic feedback, mutate the same setting through a physical control, and enter a subsystem fault. The contract fails if the UI asserts actual state without confirmation, if a stale command executes, if users cannot tell a mode semantic changed, or if recovery repeats an invalid action.

## Recovery
Reconcile displayed state from the authoritative source, separate pending request from confirmed state, invalidate actions whose preconditions changed, and preserve user intent only as a draft where appropriate. If authoritative sources conflict, move the control to an explicit unavailable/unknown state rather than choosing the most convenient reading.

## Output and Handoff
Output: `vehicle-state-dependent-controls-contract`, containing state sources, command matrix, value semantics, pending/confirmed distinction, transition handling, and evidence. Handoff broad action prohibition to driving-state lockouts and warning conditions to vehicle-warning priority.

## Sibling Boundary and delete-the-skill
Sibling driving-state lockouts govern whether a class of interaction is allowed; this skill governs controls that remain visible but whose semantics depend on vehicle state. The delete-the-skill test passes because without this owner, UI state can drift from physical vehicle truth and issue commands based on stale or misinterpreted conditions.