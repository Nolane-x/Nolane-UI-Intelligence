---
name: designing-agentic-interaction-systems
description: Design the interaction architecture for agents that can plan, call tools, mutate state, wait, recover, and act with varying autonomy while keeping users oriented and in control.
---

# Designing agentic interaction systems

Agent UX is not chat plus a spinner. Use this skill when software can decompose goals, inspect context, invoke tools, modify external systems, continue over time, and return results whose completeness or certainty may vary.

## Decision ownership

Own the top-level user-control model for agent execution: intent capture, plan visibility, autonomy boundaries, action lifecycle, interruption, side-effect review, provenance, partial completion, and recovery. Decide what the user can inspect before, during, and after execution and which state transitions must be explicit.

## Inputs and evidence

Collect agent capabilities, tool side effects, latency distribution, failure modes, permission model, reversibility, memory/context sources, expected user expertise, task duration, and audit requirements. Observe real traces rather than designing around ideal successful runs.

## Procedure

Model the agent as a stateful actor with phases such as interpreting, planning, awaiting permission, executing, blocked, retrying, partially complete, complete, and reversed. Give each state a user-visible consequence. Separate internal reasoning detail from actionable operational state; users need to know what will happen, what happened, and what requires them—not an unbounded transcript.

Define autonomy tiers by consequence and reversibility. Low-risk read actions may proceed silently; high-impact mutations may require previews or confirmation. Preserve a persistent activity record for meaningful actions and evidence.

Design interruption and recovery as primary paths, not error afterthoughts.

## Failure topology

A chat-only surface hides side effects and execution boundaries. Overexposing low-level logs overwhelms users without improving control. Another failure is a single generic “working” state that cannot distinguish waiting on a tool, blocked permission, retry, or background continuation.

Agents can also appear more capable than they are when partial completion is phrased as success.

## Falsification

Run long, failing, permission-blocked, partially successful, cancelled, and reversible tasks. Ask users to identify current state, next likely action, external systems touched, and what remains undone. Interrupt execution at arbitrary points and verify recovery semantics are intelligible.

If users must infer side effects from prose instead of structured state, the interaction system is under-specified.

## Output contract

Produce an `agentic-interaction-systems-contract` containing agent lifecycle states, autonomy levels, user-visible transitions, permission/confirmation boundaries, activity evidence, interruption and recovery rules, side-effect representation, and representative traces for success and failure.

## Handoffs

Use the specialized agent skills for plan previews, confirmations, permissions, progress, memory/context, provenance, reversibility, and multi-agent coordination. Use `designing-chat-interfaces` only for conversational mechanics rather than execution governance.