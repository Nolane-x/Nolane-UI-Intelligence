---
name: designing-agent-action-progress
description: Represent agent execution progress from real milestones, blocking states, and evidence rather than fabricated percentages or endless generic activity indicators.
---

# Designing agent action progress

Agent work can span seconds to hours and may branch as tools return new information. Use this skill when users need to know whether execution is advancing, blocked, waiting, retrying, or meaningfully complete.

## Decision ownership

Own progress semantics, milestone granularity, status labels, elapsed/remaining-time policy, background transition, and what evidence qualifies a step as complete. Decide when determinate percentage is justified and when milestone or activity state is more truthful.

## Inputs and evidence

Collect task traces, step durations, parallelism, tool queues, retries, waiting states, known/unknown work size, and user interruption needs. Identify tasks whose completion denominator changes during execution.

## Procedure

Use progress models that match task structure. For known bounded batches, determinate progress may be valid. For exploratory work, show completed milestones, current action, and outstanding known work without inventing a percentage. Distinguish active computation from waiting for permission, network, external job, or rate limit.

Collapse noisy substeps into meaningful user-level stages while preserving an inspectable detailed trace when useful. Show last meaningful activity for long tasks and allow transition to background without losing state.

## Failure topology

Fake percentages destroy trust when they stall at 99% or go backward. Generic spinners make blocked tasks appear active. Another failure is counting tool calls rather than outcomes, making progress advance despite repeated retries with no new result.

Parallel execution can also produce confusing step ordering if completion messages are serialized artificially.

## Falsification

Compare displayed progress to real traces for bounded, exploratory, parallel, retrying, and blocked tasks. Disconnect network or require permission mid-run. Ask users whether they can tell if action is needed from them. Verify completed milestones do not later revert without explicit explanation.

## Output contract

Produce an `agent-action-progress-contract` defining progress models by task class, milestone schema, active/waiting/blocked states, percentage eligibility, background behavior, evidence for completion, and representative trace mappings.

## Handoffs

Use `designing-agent-background-task-surfaces` for detached continuation, `designing-agent-retry-and-recovery` for retries, `designing-agent-interruption-and-cancel` for control, and `designing-agent-partial-completion` when work ends incomplete.