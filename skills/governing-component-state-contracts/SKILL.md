---
name: governing-component-state-contracts
description: Use when a reusable component has controlled, uncontrolled, transient, async, disabled, error, selection, or open states whose legal combinations and transitions must be part of its API contract.
---

# Governing Component State Contracts

## State Is Public Behavior
A component's state space is an API even when values are not all passed as props. This skill owns legal states, forbidden combinations, transition authority, controlled/uncontrolled boundaries, and externally observable state semantics for reusable components.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent owns component architecture. This specialist gives the state surface a formal contract so implementations and consumers do not invent incompatible interpretations.

## State Vector
List independent dimensions and derived states. Separate persistent domain state from ephemeral interaction state such as pressed/focused/dragging, and from async operation state such as pending/succeeded/failed. Identify mutually exclusive combinations and precedence rules—for example, whether disabled suppresses hover feedback but preserves an explanatory error.

For controlled state, declare source of truth, update request semantics, and what happens when the parent rejects or delays the request. For uncontrolled state, declare initialization and reset behavior.

## Transition Authority
Each transition identifies initiator, precondition, emitted event, commit point, and cancel/revert path. A component may request `open=true`; it cannot claim open until the controlling owner commits that state. This distinction matters for async validation and optimistic interaction.

## Evidence
Evidence includes statecharts, pairwise/targeted combinational fixtures, event traces, controlled/uncontrolled parity tests, focus/disabled transitions, and async race tests. Render evidence must cover semantically risky combinations rather than every Cartesian possibility.

## Failure Modes
Failure includes impossible combinations rendered anyway, controlled components mutating internal state ahead of the owner, disabled state that can still commit actions, stale async completion overwriting newer state, and visual variants that imply a state different from the actual machine.

## Falsification
Falsification races state updates, denies a controlled transition, toggles disabled during pending work, resets while an operation is inflight, and replays events out of order. Any observable state that cannot be explained by the contract disproves it.

## Recovery
Recovery restores a single source of truth, cancels stale transitions by identity/version, and collapses contradictory derived states. If a use case needs a genuinely new state dimension, add it explicitly rather than encoding it through styling variants.

## Output
Output: `component-state-contracts-contract` with state vector, legal combinations, transition table, event authority, race policy, and evidence cases.

## Handoff
Handoff visual/API variation axes to variant taxonomy and consumer-inserted content to slot governance.

## Sibling Boundary and delete-the-skill
Variant taxonomy decides which variation deserves API surface; it does not define runtime state legality. Removing this skill leaves transition ownership and impossible-state prevention unowned, so the delete-the-skill test passes.