---
name: designing-agent-delegation-handoffs
description: Design handoffs when one agent delegates work to another actor so scope, authority, context, responsibility, and returned evidence remain explicit.
---

# Designing agent delegation handoffs

Delegation can improve specialization, but hidden handoffs make accountability opaque. Use this skill when a primary agent can assign subtasks to specialist agents, external services, human reviewers, or remote runtimes.

## Decision ownership

Own delegation visibility, transferred context, authority scope, acceptance criteria, return format, failure ownership, and whether users can inspect or constrain the delegate. Decide when delegation is implementation detail versus a meaningful trust boundary.

## Inputs and evidence

Collect delegate capabilities, permissions, data boundaries, cost/latency, context requirements, failure modes, identity, and audit obligations. Identify delegations that cross organizations, providers, machines, or privacy domains.

## Procedure

Represent delegated work as a bounded assignment with goal, inputs, allowed tools, side-effect authority, and expected output. Transfer only necessary context. Make material provider or privacy boundary changes visible before delegation.

The parent agent remains responsible for integrating and validating returned work unless the product explicitly assigns responsibility elsewhere. Preserve provenance from delegate output rather than flattening it into the parent’s voice.

If a delegate fails, surface whether the parent can retry, choose another delegate, or continue without the result.

## Failure topology

Invisible delegation can send sensitive context to unexpected providers. Delegates may receive broader permissions than the parent intended. Another failure is responsibility laundering: the parent cites a specialist agent as if delegation itself proves correctness.

Nested delegation can create unreadable trees and runaway cost if not bounded.

## Falsification

Run delegations across same-process, cross-provider, and human-review boundaries. Inspect actual context and permissions transferred. Force delegate failure or partial return and verify responsibility remains clear. Limit nesting and test enforcement.

## Output contract

Produce an `agent-delegation-handoffs-contract` defining delegation triggers, assignment schema, context/permission transfer, user visibility, nesting limits, return/provenance requirements, failure ownership, and audit scenarios.

## Handoffs

Use `designing-multi-agent-coordination-views` for concurrent delegates, `designing-agent-permission-escalation` for authority, `designing-agent-result-provenance` for returned evidence, and `designing-agent-side-effect-review` for delegated mutations.