---
name: designing-agent-autonomy-and-control
description: Use when an AI can plan, call tools, mutate data, send messages, purchase, schedule, deploy, publish, delete, or otherwise act beyond producing advisory content.
---

# Designing Agent Autonomy and Control

## Overview
Capability is not authority. Define exactly what an agent may decide, what it may prepare, what requires approval, what can run unattended, and how a person can inspect, interrupt, revoke, and recover.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require action inventory, permissions, reversibility, cost/risk, frequency, data boundary, user role, and observability. High-stakes actions also require `designing-high-stakes-decisions`; security-sensitive actions route to independent security critique.

## Decision Model
Create an autonomy envelope per action class: **suggest**, **draft**, **stage**, **execute with confirmation**, **execute under standing policy**, or **forbidden**. Do not choose one autonomy level for the whole agent. Base approval thresholds on consequence, reversibility, ambiguity, novelty, and the user’s explicit delegation.

Separate plan approval from action approval. A plausible plan can contain a risky tool call later. For standing delegation, expose scope in human terms — account, recipient class, budget, environment, time window, data type — and show when a proposed action exceeds it.

Agent state must be interruptible. Provide stop/pause when action can still be prevented, not a cosmetic cancel after commit. Keep an action ledger with intent, tool/action, target, input, authorization source, result, and recovery. Distinguish prepared, queued, executing, succeeded, partially succeeded, failed, rolled back, and externally irreversible.

Design partial failure explicitly. Multi-step actions may create state before failure; users need what changed, what did not, and safe options. Never hide destructive work inside a generic “AI is working” animation.

## Evidence
Test policy boundaries, ambiguous targets, privilege changes, stale context, confirmation timing, race conditions, partial failure, cancellation, rollback, audit logs, and attempts to exceed delegated scope. Verify server/tool authorization independently of UI affordances.

## Output Contract
Return an `autonomy-envelope` with `action_classes[]`, `authority_levels{}`, `approval_rules[]`, `standing_delegations[]`, `scope_boundaries[]`, `interruptibility`, `action_ledger_schema`, `partial_failure_model`, `rollback_rules[]`, `forbidden_actions[]`, and `agent_control_tests[]`.

## Failure Traps
- “Agent mode” granting blanket authority.
- Confirmation once at session start for unrelated future actions.
- Cancel button that cannot stop a queued external operation.
- No distinction between draft and sent/published state.
- Agent quietly expanding from one account/environment to another.
- Audit log recording success but not authorization source or target.
- UI permissions treated as backend authorization.

The user should be able to delegate without surrendering the ability to understand or regain control.

## V6 Agent Autonomy Control Protocol
Model an **autonomy-level ladder** from suggest → draft → execute reversible → execute bounded → high-consequence requiring approval. Place an **approval checkpoint graph** at points where scope, identity, cost, external side effect, or irreversibility materially changes.

Set a **blast-radius bound** for autonomous actions: object count, money, recipients, permissions, systems, time horizon, or data exposure. Prefer **reversible delegation** with preview, undo/compensation, logs, and scoped credentials. Verify **stop-control latency**—when a user pauses/cancels, how quickly new tool calls stop and what already-started work may still complete.

### Falsification
Expand a task from one object to many, change recipient/cost, and cancel mid-execution. If autonomy silently broadens or execution continues without truthful state, control fails.

### Recovery
Freeze delegation, revoke/limit tool authority, reconcile completed vs pending actions, and require renewed approval before resuming beyond the previous bound.
