---
name: designing-multi-agent-surfaces
description: Use when multiple AI agents, specialized workers, tools, or delegated processes operate concurrently or sequentially on shared tasks and users must understand identity, responsibility, progress, conflicts, and handoffs.
---

# Designing Multi-Agent Surfaces

## Overview
Multiple agents multiply context, not just throughput. Make who is doing what, under which authority, against which state, and with which dependencies legible without forcing users to monitor a wall of internal logs.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require agent roles, shared artifacts/state, parallelism, dependency graph, tool permissions, human approval points, conflict policy, and whether agents can mutate each other’s work.

## Decision Model
Give each agent a stable role identity tied to capability and responsibility, not a decorative persona. Users need to distinguish planner, researcher, coder, reviewer, or domain worker when their outputs have different authority. If identities are interchangeable, present work streams rather than anthropomorphic names.

Model work as tasks with owner, input revision, dependencies, current phase, produced artifact/evidence, and status. Parallel progress should aggregate without hiding blocked critical paths. Avoid five simultaneous animated spinners; surface changes that require user attention.

Shared-state conflicts are first-class. When agents edit the same artifact, preserve revision provenance and define merge/arbitration rules. A reviewer must inspect the correct revision. Handoff records state what is accepted, unresolved, and what authority transfers. Do not present one agent’s claim as consensus merely because another agent was silent.

Human approvals must identify which agent/action they authorize. A global “Approve all” needs explicit scope and consequences. Users should be able to stop one work stream without destroying unrelated progress.

## Evidence
Test parallel tasks, delayed dependencies, stale-input work, contradictory agent recommendations, same-file edits, reviewer-on-old-revision, one-agent failure, cancellation, permission mismatch, and handoff to human. Verify provenance from final artifact back to contributing agent/tool evidence.

## Output Contract
Return a `multi-agent-context-model` with `agent_roles[]`, `work_items[]`, `dependency_graph`, `revision_binding`, `progress_aggregation`, `attention_events[]`, `conflict_policy`, `handoff_contract`, `approval_scope`, `partial_cancellation`, and `multi_agent_tests[]`.

## Failure Traps
- One generic “AI working” state for multiple independent operations.
- Decorative agent personas with unclear responsibility.
- Reviewer approving a stale revision.
- Parallel progress hiding the one blocked critical dependency.
- Agent conflict resolved by last write wins without visibility.
- Approval scope ambiguous across agents/actions.
- Internal chain-of-thought-style logs used as the primary UI instead of concise task evidence.

Multi-agent UI is successful when concurrency increases capability without multiplying uncertainty for the user.

## V6 Multi-Agent Attribution Protocol
Maintain **agent-identity provenance** for every material suggestion/action: which agent/model/tool produced it, on whose authority, from which task/context, and whether another agent transformed it. Build a **delegation boundary map** showing what each agent may propose, execute, approve, or hand off.

Handle **concurrent-action conflict** when agents modify the same object, invoke incompatible tools, or pursue competing goals. Present an **attribution timeline** that lets users reconstruct material decisions without reading raw hidden traces. Specify **agent handoff recovery** so context, unresolved constraints, pending actions, and ownership survive when a different agent takes over.

### Falsification
Have two agents issue conflicting edits, retry after partial tool failure, and hand off mid-task. If the user cannot identify who did what or which action is authoritative, the surface fails.

### Recovery
Pause execution, surface the conflict, restore last known coherent state, and require explicit re-delegation where authority is ambiguous.
