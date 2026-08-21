---
name: designing-multi-agent-handoff-visibility
description: Use when one agent delegates or transfers work to another agent and the interface must show responsibility, context transfer, authority boundaries, pending obligations, and return conditions so users do not lose track of who is acting or why.
---

# Designing Multi-Agent Handoff Visibility

## Handoff as responsibility transfer
Multi-agent systems create a distinct UX hazard: work can move between actors while the user sees one continuous conversation. This skill owns the visible contract for a handoff—who owns the task now, what context was transferred, what authority the receiving agent has, what remains with the sender, and how results return.

## Parent Contract
**Required parent:** `designing-multi-agent-surfaces`.

The parent defines how multiple agents coexist, coordinate, and appear in one product. This specialist begins at the moment responsibility for a material obligation moves from one agent to another.

## Handoff record
Represent handoff with `(from_agent, to_agent, obligation_set, context_snapshot, authority_subset, unresolved_questions, expected_return, status)`. The context snapshot should contain task-relevant artifacts and state, not private hidden reasoning. Authority should be explicit: delegation of work does not automatically delegate every permission available to the sending agent.

The decision owner is which obligations have transferred. A sending agent may remain responsible for synthesis while a specialist agent owns a bounded research or implementation task. Show split ownership rather than reducing the whole run to the name of whichever agent spoke last.

## User-visible cues
The UI should identify material handoffs without turning every internal routing event into noise. Surface actor changes when they alter capability, authority, expected latency, privacy boundary, or accountability. A handoff should answer “why this agent,” “what it is doing,” and “what happens when it finishes.”

If the user addresses the wrong agent after a handoff, the system should route intentionally or explain that responsibility resides elsewhere. Do not silently create parallel work that duplicates an active delegated obligation.

## Context integrity
Receiving agents need versioned context. If shared state changes after delegation, either update the receiving context through a defined channel or mark its work as based on an older revision. The interface should not merge stale delegated output into current state as if it were produced from the latest facts.

Results returning from a sub-agent retain provenance. The orchestrating agent may summarize or transform them, but the user should be able to trace consequential claims and side effects to the actor and evidence that produced them.

## Evidence
Evidence includes the handoff record, context revision, authority subset, receiving acceptance, tool calls by actor, completion status, return artifact, and any re-handoff. Test cases should include nested delegation, refusal by the receiving agent, a context update during delegation, and two agents attempting to own the same obligation.

## Failure modes
Characteristic Failure includes invisible delegation, permissions inherited implicitly, duplicate agents working the same side-effecting task, stale sub-agent results merged without warning, and handoffs with no defined return path. Another failure is false singularity: the UI attributes every action to one assistant identity even when different agents made decisions under different authority.

## Falsification
Delegate a task that requires narrower authority, change shared state while the sub-agent works, cancel the parent run, reject the handoff, and create overlapping obligation assignments. The contract fails if responsibility becomes ambiguous, if the receiver gains undeclared permissions, if stale output appears current, or if completed delegated work cannot be traced back to its actor.

## Recovery
When ownership overlaps, freeze duplicate side-effecting work, select a canonical obligation owner, preserve both evidence streams, and explicitly cancel or supersede the other assignment. When context is stale, revalidate the delegated result before synthesis. When authority transfer was too broad, revoke it and audit actions taken under the excess grant.

## Output and Handoff
Output: `multi-agent-handoff-visibility-contract`, containing obligation transfer, actor identity, context revision, authority subset, return conditions, user-visible cues, and evidence lineage. Handoff state conflicts to shared-state reconciliation and branch divergence to agent-run branching.

## Sibling Boundary and delete-the-skill
Sibling multi-agent surface design covers overall actor presence and coordination. This skill owns the transition of responsibility itself. Background-run surfaces own visibility across time/surfaces, not between agents. The delete-the-skill test passes because without it, delegation becomes invisible implementation detail even when responsibility, authority, and evidence materially change.