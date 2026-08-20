---
name: designing-agent-permission-escalation
description: Escalate agent permissions just in time with narrow scope, reason, duration, and visible revocation rather than requesting broad access at setup.
---

# Designing agent permission escalation

Agents often need access to files, accounts, tools, or external services only when a task reaches a particular step. Use this skill to design just-in-time permission requests that preserve least privilege and user comprehension.

## Decision ownership

Own permission-request timing, scope, duration, rationale, fallback behavior, and re-use of prior grants. Decide when a permission can be requested as a category versus a specific resource and when elevation must expire automatically.

## Inputs and evidence

Collect tool capability scopes, provider authorization models, user roles, sensitive resources, task dependencies, denial/revocation behavior, and logs of overbroad permission requests. Distinguish “connect account” from “allow this agent to perform this action.”

## Procedure

Request the narrowest grant when the need becomes concrete. Explain what capability is needed, why the current task requires it, what resource range it covers, and whether it persists. Offer a lower-privilege or manual alternative when feasible.

Separate authentication from authorization. Being signed in to a service does not mean the agent may freely mutate it. Surface active grants and provide a clear revocation surface. Revalidate permission before consequential actions if the grant context changed.

## Failure topology

Setup-time requests for broad access normalize excessive privilege. Vague wording such as “access your Drive” hides read/write or folder scope. Another failure is treating a denied permission as a generic task error rather than offering a safe alternate path.

Persistent grants can outlive the user’s original intent and silently expand to future tasks.

## Falsification

Run tasks that need no permission, read-only permission, narrow write permission, and cross-service escalation. Deny requests and verify the agent can explain impact without coercion. Revoke access mid-task and observe recovery. Inspect whether a grant intended for one folder can reach another.

## Output contract

Produce an `agent-permission-escalation-contract` defining permission classes, request timing, scope/duration, rationale fields, persistence/revocation, denial alternatives, revalidation triggers, and audit evidence.

## Handoffs

Use `designing-agent-action-confirmations` for action-level consent after access exists, `designing-agent-tool-selection-visibility` for tool choice, security/privacy skills for data handling, and `designing-agent-memory-controls` for retained information permissions.