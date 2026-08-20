---
name: designing-agent-plan-previews
description: Present agent plans at the level of decisions, dependencies, side effects, and checkpoints needed for user control without exposing unstable internal reasoning as authoritative truth.
---

# Designing agent plan previews

A useful plan preview helps users catch the wrong direction before execution begins. Use this skill when an agent can perform multi-step work whose route, scope, or side effects should be inspectable before or during execution.

## Decision ownership

Own what a plan preview includes, when it appears, how editable it is, what constitutes a material plan change, and how user approval relates to execution. Decide which steps are commitments versus provisional discoveries.

## Inputs and evidence

Collect task classes, typical step count, tool calls, side effects, unknown dependencies, approval thresholds, user expertise, and historical cases where agents pursued the wrong scope. Distinguish deterministic workflows from exploratory tasks whose exact steps cannot be known up front.

## Procedure

Present the plan as user-relevant milestones: intended outcome, resources or systems involved, consequential actions, dependencies, and checkpoints. Mark uncertainty explicitly. Avoid presenting speculative detail as guaranteed sequence; exploratory tasks can show a strategy and decision gates rather than fake precision.

Allow users to modify scope or prohibit actions without rewriting the entire prompt. When execution discovers material new work or a higher-risk side effect, surface a plan delta and require renewed approval if the boundary changed.

Keep plan state synchronized with actual progress so completed, skipped, blocked, and added steps are distinguishable.

## Failure topology

Overdetailed plans create ceremony and quickly become stale. Under-detailed plans hide destructive actions inside generic steps such as “update project.” Another failure is approval theatre: the user approves a plan, but the agent later executes materially different work without surfacing the deviation.

Plan previews can also encourage users to trust an agent’s proposed route even when the task is too uncertain to plan faithfully.

## Falsification

Compare plan previews to execution traces across simple, branching, and exploratory tasks. Inject new dependencies mid-run and verify material deltas are surfaced. Ask users whether they can identify files, services, or records that may be modified before approval.

If users regularly approve without understanding consequence, reduce verbosity but increase decision clarity.

## Output contract

Produce an `agent-plan-previews-contract` defining preview triggers, milestone schema, certainty labeling, side-effect disclosure, editable scope, delta thresholds, approval semantics, and trace-to-plan reconciliation.

## Handoffs

Use `designing-agent-action-confirmations` for final action approval, `designing-agent-permission-escalation` for capability grants, `designing-agent-action-progress` for live execution, and `designing-agent-side-effect-review` for post-plan consequence inspection.