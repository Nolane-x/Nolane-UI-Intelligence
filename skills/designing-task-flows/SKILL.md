---
name: designing-task-flows
description: Use when a user goal spans multiple decisions, states, confirmations, asynchronous steps, permissions, or recovery paths and the sequence materially affects success.
---

# Designing Task Flows

## Overview
A flow is a state transition system around a user goal, not a sequence of pretty screens.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume critical jobs and product entity lifecycles. Define the flow before deciding how many screens it requires.

## Flow graph
Model nodes as meaningful user/system states and edges as actions/events. Include:
- entry conditions
- required context
- optional branches
- validation boundaries
- async waiting/processing
- permission checks
- cancellation
- commit point
- success evidence
- partial success
- failure/retry
- undo/reversal where possible
- re-entry after interruption

## Minimize irreversible commitment
Delay irreversible effects until users have enough information to make the decision. Prefer reversible actions plus undo when the product permits. Confirmation dialogs are not a substitute for reversibility.

For high-consequence actions, confirmation content must identify the target, consequence, scope, and recovery reality. Do not ask users to confirm facts the UI itself could verify.

## Preserve context
Each transition should answer:
- what changed?
- what remains selected/configured?
- where did I come from?
- what can I do next?

Avoid dumping the user onto a generic success page when the natural next task belongs in context.

## Async flow design
Separate accepted, processing, completed, partially completed, failed, cancelled, and unknown states when the backend/product can distinguish them. Prevent duplicate commits while an action is in flight unless repeat is explicitly valid.

## Branch complexity
If a flow has many branches, do not force all choices into one wizard. Group decisions by dependency: ask a question only before a downstream choice actually needs it. Conversely, do not split a simple reversible task across screens just to create “progress.”

## Interruption and resumption
For long or high-effort flows, define draft persistence, stale-data handling, and how re-entry communicates what has changed since the user left.

## Output: `task-flow-model`
Return `goal`, `entry_states`, `state_graph`, `commit_points`, `irreversible_edges`, `recovery_edges`, `async_states`, `permission_edges`, `interruption_policy`, `success_evidence`, and `flow_invariants`.

## Adversarial checks
- Close the browser halfway through.
- Lose network after commit but before response.
- Change permissions in another session.
- Submit twice.
- Return via a stale deep link.
- Complete only part of a batch.

If the UI would lie about state under these cases, the flow is incomplete.

## V6 Flow Transaction Model
Augment the flow graph with a **commit-point map**. Every edge that creates external side effects, consumes scarce resources, changes permissions, publishes content, charges money, or becomes difficult to reverse must declare exactly when commitment occurs and what evidence the user receives. Earlier steps are preparation, not fake success.

For every task that can outlive a single uninterrupted session, define an **interruption re-entry contract**: what state is persisted, what expires, where the user resumes, what changed while away, and how stale assumptions are surfaced. Specify **partial-success semantics** for batch, multi-service, upload, invite, import, or agentic actions; “success” may contain completed and failed subparts that require different next actions.

Run a **reversible-edge audit**. Prefer undo, draft, cancel, version restoration, or compensating actions when system semantics permit. Where reversibility is impossible, move consequence disclosure before the commit point and avoid confirmations that merely train users to click through. Execute a **flow dead-end probe** from error, permission denial, empty prerequisite, expired session, and cancelled async states; each must offer an intentional next path or an explicit terminal outcome.

### Falsification
Interrupt the flow before and after each commit point, fail one dependency after another succeeds, and revisit from history/deep link. If the user cannot tell what happened or safely continue, the happy-path sequence was never a complete flow.

### Recovery
When a dead end or ambiguous partial success is found, repair the state/transaction model first. Only then revise screens and copy. Never hide an unrecoverable edge with a generic toast.
