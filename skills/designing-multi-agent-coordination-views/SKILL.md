---
name: designing-multi-agent-coordination-views
description: Represent concurrent or cooperating agents so users can understand roles, dependencies, conflicts, shared resources, and aggregate progress without monitoring raw logs.
---

# Designing multi-agent coordination views

When several agents work in parallel, a single linear chat transcript no longer reflects the system. Use this skill for orchestrators, swarms, specialist teams, reviewer agents, or parallel research/coding tasks.

## Decision ownership

Own role representation, task assignment, dependency visualization, conflict state, shared-resource contention, aggregate progress, and drill-down. Decide what coordination detail is useful to users versus internal scheduler noise.

## Inputs and evidence

Collect agent roles, task graph, dependencies, shared files/services, concurrency, conflicts, retries, delegated permissions, and result-merging logic. Review real traces for races and duplicated work.

## Procedure

Present agents primarily through owned work and state, not anthropomorphic avatars. Show which tasks run concurrently, which are blocked on dependencies, and which outputs are awaiting synthesis or review. Surface conflicts when agents propose incompatible edits or compete for the same resource.

Provide aggregate status plus drill-down to each assignment and provenance. Keep user intervention scoped: pause one agent, cancel a branch, approve a conflict resolution, or change priority without necessarily stopping all work.

## Failure topology

A wall of agent cards can be visually impressive but operationally useless. Linear logs obscure parallelism. Another failure is showing each agent as independently successful while final integration has unresolved conflicts.

Resource contention may look like inactivity if the UI does not distinguish waiting from failure.

## Falsification

Simulate parallel success, dependency blocking, conflicting edits, one-agent failure, resource lock, and cancellation of a branch. Ask users to identify what is on the critical path and whether final synthesis is safe. Compare displayed dependencies to scheduler traces.

## Output contract

Produce a `multi-agent-coordination-views-contract` defining role/task representation, dependency and conflict states, aggregate progress, drill-down, intervention controls, shared-resource visibility, and test scenarios for parallel execution.

## Handoffs

Use `designing-agent-delegation-handoffs` for assignment boundaries, `designing-agent-action-progress` for task state, `designing-agent-partial-completion` for mixed outcomes, and conflict/version skills when agents edit shared artifacts.