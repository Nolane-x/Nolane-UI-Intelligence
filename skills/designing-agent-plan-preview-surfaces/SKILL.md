---
name: designing-agent-plan-preview-surfaces
description: Use when an agent can expose a proposed multi-step plan before execution and the interface must communicate intent, dependencies, uncertainty, side effects, and editable scope without implying the plan is guaranteed or already executed.
---

# Designing Agent Plan Preview Surfaces

## Decision owner
A plan preview is an execution contract proposal, not decorative chain-of-thought. This skill owns what planning information is safe and useful to expose: user-relevant steps, dependencies, side-effect boundaries, required approvals, estimated uncertainty, and places where the plan may legitimately branch. It explicitly does not require revealing private model reasoning. The surface should expose operational commitments and externally meaningful assumptions rather than internal hidden deliberation.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent defines the autonomy envelope: what the agent may decide or execute without intervention. This specialist starts when a plan needs to become a visible control surface before or during execution.

## Plan representation
Represent each visible step with a stable step identity, user-facing objective, prerequisites, side-effect class, expected evidence, approval requirement, and current disposition such as `proposed`, `accepted`, `edited`, `skipped`, `blocked`, or `invalidated`. A plan revision should be explicit; silently mutating the plan after approval destroys the meaning of approval.

Do not force every runtime action into the preview. Low-level implementation steps can remain hidden when they do not affect user intent, cost, privacy, permissions, or externally observable outcomes. Conversely, any step that changes irreversible state, crosses an authority boundary, spends meaningful resources, sends data externally, or materially changes the task should be represented even if the agent considers it routine.

## Preview interaction contract
Users need to understand the difference between reviewing the plan and authorizing execution. Editing a step should either update dependent steps or mark them invalid until replanning occurs. Reordering is allowed only where dependencies permit it. Removing a prerequisite must not leave a downstream step looking valid. If the system supports partial approval, the preview should reveal the exact approved subset and what remains blocked.

A good plan preview also shows uncertainty in the structure itself: branches may be conditional, later steps may depend on unknown tool results, and some actions may not yet have enough information to specify. Represent that uncertainty instead of fabricating a linear promise.

## Evidence
Evidence includes plan revision IDs, the user-visible plan at approval time, dependency edges, side-effect annotations, approval records, and the mapping from executed tool calls back to visible steps. Capture a case where replanning occurs after new evidence and prove that the interface marks the old plan as superseded rather than rewriting history.

## Failure modes
Characteristic Failure includes exposing verbose pseudo-reasoning instead of actionable commitments, showing a fixed checklist that the runtime does not actually follow, silently inserting side-effecting steps after approval, retaining stale approval after a plan edit, and presenting speculative later steps as guaranteed. Another failure is “ceremonial preview”: the user can see steps but cannot meaningfully change, reject, or constrain them despite the interface implying control.

## Falsification scenarios
Falsification should edit an early step with downstream dependencies, insert a newly required permission, make a planned tool unavailable, and force the agent to replan after partial execution. The contract fails if old approval remains attached to changed semantics, if executed actions cannot be mapped to a plan revision, if a hidden side effect appears that should have been previewed, or if the user cannot tell which parts are tentative.

## Recovery
When a plan becomes invalid, freeze future side-effecting steps, preserve completed evidence, and create a new revision that explicitly cites the invalidating event. Do not reset already completed work unless the new plan requires compensating actions. If a user edit produces contradictory constraints, surface the contradiction and route back to task clarification rather than guessing.

## Output and Handoff
Output: `agent-plan-preview-surfaces-contract`, containing step identity, plan revisions, dependency semantics, visible side-effect policy, approval attachment, edit rules, invalidation, and evidence links. Handoff approval interpretation to approval-scope boundaries; hand off runtime state to tool-call lifecycles; hand off branch semantics after execution begins to agent-run branching.

## Sibling Boundary and delete-the-skill
Sibling approval-scope design owns the legal/semantic extent of an authorization, while this skill owns how a plan is represented and revised. Background-run surfaces own long-lived execution visibility, not pre-execution intent. The delete-the-skill test passes because removing this owner leaves no rigorous interface contract connecting visible planned steps to the actions the agent later performs.