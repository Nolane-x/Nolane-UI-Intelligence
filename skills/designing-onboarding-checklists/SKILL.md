---
name: designing-onboarding-checklists
description: Use when activation requires several independently completable milestones and users need a persistent view of progress, optionality, prerequisites, completion evidence, and next useful actions.
---

# Designing Onboarding Checklists

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns milestone-based activation tracking. It is not a linear wizard: checklist items may be completed out of order, from normal product surfaces, or by other collaborators. The checklist should reflect actual product state rather than clicks on the checklist itself.

## Decision Model
Choose items that represent meaningful activation outcomes: create first project, invite a collaborator, import real data, configure a required integration, publish first artifact, or complete a security step. Avoid vanity tasks such as “visit analytics” unless visiting creates an essential understanding or state. Each item needs an objective completion predicate grounded in the product.

Distinguish required, recommended, and optional items. A progress ring that treats all ten items as mandatory can create false incompleteness when only three are needed to operate. Dependencies should be visible when one task cannot yet be completed, but avoid imposing sequence where none exists.

Completion may happen outside the current session or through another user. Reconcile from authoritative state on load and after relevant events. Manual “mark complete” is appropriate only when the milestone is inherently subjective; otherwise it weakens trust. Completed items can collapse, but preserve enough history to explain why the overall checklist advanced.

## Failure Topology
- Checklist marks “Invite teammate” complete when the user merely opened the invite dialog.
- Optional marketing setup blocks a 100% progress claim and pressures users into irrelevant work.
- A collaborator completes an integration, but the owner’s checklist remains stale until refresh.
- Clicking a checklist item navigates into a workflow but browser Back loses checklist context.
- Completed tasks become permanently hidden, so users cannot understand what progress means.
- Product reorders items based on telemetry and makes the next step feel unstable across sessions.

## Falsification and Recovery
Falsify with milestones completed from another route, another collaborator, imported preexisting state, skipped optional tasks, dependency failure, checklist dismissal and later return, responsive/mobile layout, screen-reader operation, and a user whose account is already partially configured before first seeing the checklist. The design fails if completion is inferred from UI visitation instead of state evidence or if optional work is presented as a hard activation blocker.

Recover by defining authoritative predicates, classifying item necessity, syncing external completion, preserving deterministic ordering, keeping completed-state evidence inspectable, and routing each item into normal product flows with a reliable return path.

## Output Contract
Return `onboarding-checklist-contract` with milestone inventory, completion predicates, required/recommended/optional classification, prerequisites, ordering, external completion reconciliation, navigation/return behavior, dismissal/persistence, progress calculation, accessibility semantics, and falsification cases.