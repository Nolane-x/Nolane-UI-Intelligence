---
name: designing-agent-tool-call-lifecycles
description: Use when an AI agent invokes tools whose requests move through proposed, authorized, dispatched, running, succeeded, failed, cancelled, timed-out, or indeterminate states and the UI must expose those transitions truthfully.
---

# Designing Agent Tool-Call Lifecycles

## Scope of ownership
A tool call is not a spinner attached to an assistant message. It is a stateful operation with identity, preconditions, authority, side effects, terminal evidence, and sometimes an ambiguous outcome. This skill owns the interface contract that maps execution state to what the user can see and do. Its central decision is which lifecycle state is currently justified by evidence and which actions—approve, cancel, retry, inspect, or reconcile—are valid from that state.

## Parent Contract
**Required parent:** `designing-human-ai-interaction`.

The parent governs human/AI collaboration generally. This specialist starts at the boundary where a model has selected or proposed a concrete tool operation and the product must make its execution lifecycle observable without confusing model intention with runtime fact.

## Execution state machine
Use explicit states such as `proposed`, `awaiting_authority`, `queued`, `dispatched`, `running`, `succeeded`, `failed`, `cancel_requested`, `cancelled`, `timed_out`, and `outcome_unknown`. Products may add domain states, but must not collapse `dispatched` into `succeeded` or `cancel_requested` into `cancelled`. The decision owner is the transition table: every transition needs an originating event, a timestamp or ordering token, and the authority allowed to emit it.

Tool-call identity must survive retries and reconnects. A retry may create a new execution attempt while retaining the same logical intent; the UI should preserve that relationship rather than overwrite the failed attempt. For side-effecting tools, idempotency capability influences which transitions may expose Retry. When the runtime loses contact after dispatch, the correct state may be outcome unknown, not failure.

## User-visible obligations
The surface should reveal what is being attempted at the level needed for informed control, while redacting secrets and irrelevant machine payload. Long-running operations need progress only when the runtime can substantiate progress; fabricated percentages are worse than an honest indeterminate state. Cancellation must distinguish “request sent” from “operation stopped.” Terminal success should be bound to a tool result or authoritative side-effect confirmation, not to an agent sentence.

Action affordances follow state. Approval is meaningful before dispatch; cancellation is meaningful only while the operation can still be stopped; retry is meaningful only after the previous attempt has a bounded result or the tool provides a safe recovery rule. If the runtime cannot determine whether a side effect happened, route to reconciliation rather than offering a blind retry.

## Evidence model
Evidence includes request identifiers, authority records, dispatch acknowledgements, runtime events, cancellation acknowledgements, terminal tool results, and authoritative domain checks for side effects. A useful trace lets a reviewer answer: what was proposed, who authorized it, which attempt ran, what the runtime reported, what the external system now says, and what the user saw at each step.

## Failure topology
Characteristic Failure includes premature success badges, spinners that survive a terminal error, duplicate attempts hidden behind one card, cancellation UI that claims certainty before acknowledgement, and retries that repeat an irreversible action. Another failure is conversational drift: the assistant says “done” while the tool card is failed or indeterminate. The runtime evidence is authoritative over generated narration.

## Falsification
Falsification should inject late success after a local timeout, duplicated terminal events, cancellation races, network loss immediately after dispatch, and a retry against a non-idempotent tool. The lifecycle contract is false if an impossible transition renders, if two attempts collapse into one history entry, if the UI asserts a terminal outcome without evidence, or if the available controls permit an unsafe transition.

## Recovery playbook
Recovery first preserves the last confirmed state and attempt identifier. Query the authoritative execution or domain system where possible. If the outcome remains unknown, label it as such and prevent automatic repetition of side effects. When a new attempt is appropriate, create it explicitly, link it to the previous attempt, and carry forward only still-valid preconditions.

## Output and Handoff
Output: `agent-tool-call-lifecycles-contract`, containing the state machine, event authority, attempt identity, control availability, ambiguity policy, evidence bindings, and recovery transitions. Handoff tool-result rendering to the presentation-lifecycle specialist; hand off permission changes to tool-permission escalation; hand off conflicting shared domain state to shared-state reconciliation.

## Sibling Boundary and delete-the-skill
Sibling approval-scope design owns what a human authorization covers, not whether an authorized operation is queued or running. Retry/replay design owns the user-facing policy for repetition across attempts, not the foundational lifecycle semantics. The delete-the-skill test passes because without this owner, execution truth collapses into ad hoc chat states and the interface cannot prove where a tool call actually is.