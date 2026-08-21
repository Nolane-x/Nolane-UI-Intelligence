---
name: designing-agent-approval-scope-boundaries
description: Use when a human approval must authorize a bounded set of agent actions and the interface must define exactly which operations, resources, parameters, duration, and side effects that approval covers.
---

# Designing Agent Approval Scope Boundaries

## Authority question
Approval is only meaningful if its scope can be stated precisely enough to reject actions outside it. This skill owns the decision contract for what one approval covers: operation class, target resources, parameter ranges, time window, quantity or spend limits, data disclosure, downstream delegation, and whether repeated executions remain authorized. The goal is not to add confirmation dialogs; it is to make authority machine-checkable and user-legible.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent establishes what the agent may do autonomously and when human authorization is required. This specialist begins once approval is required and must be turned into an explicit capability boundary rather than a vague “yes.”

## Scope dimensions
Represent an approval as `(principal, intent_revision, actions, resources, constraints, expiry, reuse_policy, delegation_policy, evidence_id)`. Scope dimensions may include recipient sets, monetary ceilings, environments, repositories, files, accounts, locations, or disclosure categories. Missing dimensions are not automatically wildcards. Products must define whether omission means deny, inherit, or prompt.

Bind approval to the semantics the user actually reviewed. If a plan changes the target account, broadens a recipient set, raises a quantity, introduces a new external service, or changes from reversible to irreversible behavior, previously captured approval may no longer apply. A UI that keeps an enabled “Run” state after those changes is granting authority that was never given.

## Reuse and delegation
Some approvals are single-use; others may cover a batch, session, workflow, or bounded period. Reuse must be intentional and visible. Do not infer “always allow” from repeated approvals unless the product explicitly offers that policy and explains revocation. Delegation is a separate axis: approving an agent to call one tool does not necessarily authorize that tool or sub-agent to make additional side effects on the user’s behalf.

## Evidence requirements
Evidence includes the exact user-visible summary at approval time, normalized scope fields, intent or plan revision, approving principal, timestamp, expiry, and every execution that consumes the authorization. Review should be able to answer both directions: which approval allowed this action, and which actions were consumed by this approval.

## Failure classes
Characteristic Failure includes approvals attached only to chat-message IDs, wildcard resources hidden behind friendly wording, an old approval surviving a material parameter change, session-wide authorization with no revocation path, and a sub-agent treating another agent’s permission as transferable. Another failure is semantic compression: the UI says “Allow access?” while the actual grant includes write, delete, or external sharing capability.

## Falsification
Falsification changes one scope dimension after approval, attempts an additional execution, swaps target resource identity while preserving the label, exceeds a numeric bound, waits past expiry, and delegates the action through another actor. The contract is disproved if any out-of-scope action proceeds, if the UI cannot explain why a scope still applies, or if a permitted action is rejected because the stored scope cannot be reconstructed deterministically.

## Recovery
If scope cannot be proven, default to blocked for side-effecting operations. Preserve the proposed action, show which dimension is uncovered, and request a new narrowly scoped approval. If a prior scope was accidentally over-broad, revoke it where possible, record affected executions, and route already-performed consequences to side-effect reconciliation rather than pretending the grant never existed.

## Output and Handoff
Output: `agent-approval-scope-boundaries-contract`, defining normalized scope dimensions, binding to intent revisions, reuse, expiry, delegation, revocation, evidence, and decision rules. Handoff runtime consumption of the grant to tool-call lifecycles; hand off escalation when a tool asks for more authority to tool-permission escalation.

## Sibling Boundary and delete-the-skill
Sibling plan-preview design owns how intended steps are represented. Approval-scope drift owns detecting when execution has moved beyond what was approved. This skill defines the authority envelope itself. The delete-the-skill test passes because without a canonical scope contract, every approval becomes an ambiguous natural-language promise that cannot reliably gate agent behavior.