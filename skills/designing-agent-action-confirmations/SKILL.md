---
name: designing-agent-action-confirmations
description: Design confirmations for agent actions around consequence, scope, reversibility, and user intent instead of interrupting every tool call with generic approval prompts.
---

# Designing agent action confirmations

Agent confirmations should intercept meaningful risk, not create click fatigue. Use this skill when an agent is about to perform consequential actions such as sending messages, deleting data, spending money, publishing, merging code, or changing permissions.

## Decision ownership

Own confirmation thresholds, grouping, preview content, default action, expiry, and whether approval is one-shot or scoped. Decide which actions can be auto-approved because they are low-risk or reversible and which require explicit informed consent.

## Inputs and evidence

Collect side-effect classes, reversibility, affected entities, financial/security impact, frequency, user intent signals, prior authorization, and regulatory requirements. Inspect current confirmation rates and cancellation behavior to detect habituation.

## Procedure

Classify actions by consequence rather than tool name. A filesystem write to a temporary workspace differs from deleting production data. Show exactly what will change, affected scope, destination, and reversibility. For repeated homogeneous actions, allow bounded batch approval when the user can understand the set.

Avoid vague buttons such as “Continue” when the action is “Delete 42 records.” Make the confirm control describe the consequence. Provide a safe cancel path and preserve agent context after cancellation so users can modify the plan.

Allow scoped standing authorization only with visible boundaries and revocation.

## Failure topology

Confirming every action trains users to approve reflexively. Confirming too late—after data is uploaded or a message sent—turns the dialog into fiction. Another failure is hiding important variation inside a batch, such as one destructive action among many safe edits.

Users may also approve based on a plan preview whose target set changed since the preview.

## Falsification

Test confirmation behavior across low/high risk, one-off/batch, reversible/irreversible actions. Mutate the target set after preview and ensure stale approvals do not apply. Measure cancel and inspect behavior; if virtually nobody reads the preview, redesign around clearer consequence.

## Output contract

Produce an `agent-action-confirmations-contract` containing risk classes, trigger rules, preview fields, scope/batch semantics, stale-approval invalidation, labels, cancel behavior, standing-authorization rules, and examples of actions that do and do not require confirmation.

## Handoffs

Use `designing-agent-plan-previews` for earlier planning, `designing-agent-permission-escalation` for access grants, `designing-agent-side-effect-review` for final consequence review, and `designing-agent-reversible-actions` where undo can reduce confirmation burden.