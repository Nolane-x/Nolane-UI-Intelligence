---
name: designing-agent-reversible-action-surfaces
description: Use when an agent performs actions that can be undone, rolled back, or compensated and the interface must represent what reversal really means, how long it remains available, and which consequences cannot be restored exactly.
---

# Designing Agent Reversible Action Surfaces

## Reversal is not a generic Undo
Agent systems often expose “undo” after a side effect, but the semantics vary radically. Deleting a draft may be exactly reversible from a recycle bin; sending a message may only support a follow-up correction; changing a permission may be reversible while access already exercised during the interval is not. This skill owns the decision model that classifies reversal and turns it into truthful controls.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent defines what actions the agent may execute. This specialist starts after or immediately around a side effect for which the product claims some form of reversal, rollback, restoration, or compensation.

## Reversibility classes
Classify each action as `exactly_reversible`, `state_restorable_with_loss`, `compensatable`, `time_bounded_reversible`, or `irreversible`. Exact reversal should restore the prior externally authoritative state and relevant identity. Restoration with loss may recreate content but not timestamps, links, audit identity, or downstream references. Compensation creates a new counteracting action; it does not erase history.

The decision owner is whether the UI can ethically label a control Undo. Use that label only when the user’s meaningful prior state can be restored with bounded side effects. Otherwise name the actual operation: restore, revoke, refund, revert commit, send correction, or create compensating entry.

## Preconditions and windows
Reversal often has a validity window. A resource may be edited by someone else after the agent’s action, a reservation may enter a non-refundable phase, or an external system may garbage-collect the previous version. Capture the snapshot/revision required for reversal and revalidate it before execution. Do not keep an enabled undo affordance whose preconditions have expired.

For chained actions, reversal order matters. Undoing an early step after downstream steps consumed its result can create a new inconsistency. The surface should expose dependent effects and either reverse them in a safe order or require an explicit recovery plan.

## Evidence
Evidence includes the original side-effect ledger entry, prior-state identity or snapshot, reversal capability, expiry, dependency graph, reversal attempt, and authoritative post-reversal check. A successful tool response is insufficient if the domain state was not restored as promised.

## Failure modes
Characteristic Failure includes calling compensation “undo,” restoring visible content but losing permissions or references without disclosure, leaving expired undo controls active, reversing one step while dependent side effects remain, and claiming rollback before the external system confirms it. Another failure is ephemeral undo state stored only in the current tab, making a supposedly recoverable action irreversible after navigation.

## Falsification
Test reversal after the resource changes concurrently, after the advertised time window, after a dependent action occurs, after reconnect, and against a tool that reports success while the external state remains changed. The contract fails if the control promises stronger restoration than evidence supports, if reversal can corrupt newer state, or if the user cannot distinguish exact reversal from compensation.

## Recovery
When exact reversal is no longer valid, degrade the control honestly to the strongest remaining remediation. Preserve the original side-effect record and append the reversal or compensation as a new linked event. If a reversal partially succeeds, stop chaining additional reversals until authoritative state is reconstructed.

## Output and Handoff
Output: `agent-reversible-action-surfaces-contract`, containing reversibility classification, user-facing labels, validity windows, dependency ordering, precondition checks, authoritative confirmation, and evidence. Handoff durable action history to the side-effect ledger and ambiguous tool states to tool-call lifecycles.

## Sibling Boundary and delete-the-skill
Sibling retry/replay controls repeat attempts toward an intended outcome; this skill changes or compensates an outcome that already occurred. Partial-completion recovery decides what unfinished work remains, not what can be undone. The delete-the-skill test passes because without a dedicated reversibility owner, products routinely overstate “Undo” and conceal irreversible residue.