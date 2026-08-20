---
name: designing-project-and-work-management
description: Use when this specialist's decision ownership is materially in scope. Own the information and interaction architecture for coordinated project work across plans, work items, dependencies, time horizons, people, status, risk, and closure.
---
# Designing Project and Work Management

## Parent Contract

**Required parent:** `designing-task-flows`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the project-management layer that turns generic work items into a coordinated plan with scope, sequencing, time horizon, ownership, progress, and risk. Decide the canonical work-item model, how projects relate to boards/backlogs/roadmaps, which state belongs to an item versus a project, and how users move between execution detail and planning overview. This owner does not replace generic task flows, assignment, approvals, or calendars; it composes them into project semantics.

## Inputs and evidence

Require project types, actor roles, work-item taxonomy, hierarchy and dependency needs, planning cadence, status model, scheduling precision, estimation model, portfolio relationships, permissions, and completion/archival rules. Inspect active projects at several scales: a small personal effort, a cross-functional project with dependencies, and a long-running portfolio initiative. Identify which fields are authoritative versus derived.

## Procedure

Define one canonical work-item identity that survives presentation in board, list, timeline, backlog, and dashboard views. Separate work-item state from view-specific grouping so dragging a card does not accidentally rewrite semantics unless the board explicitly maps columns to states. Establish hierarchy, dependency, ownership, scheduling, and risk as orthogonal dimensions rather than packing them into one status field. Provide project-level summary from evidence—completed scope, blocked critical path, overdue milestones, capacity—not arbitrary color. Planning views should deep-link to executable work, while operational work should retain project context. Define archive/closure as a lifecycle transition with retained history, not deletion.

## Failure topology

Failures include duplicate task identities across views, boards whose columns silently mutate business state, roadmaps disconnected from actual work, project health reduced to manual traffic-light labels, hidden dependency blockers, and portfolio summaries that double-count nested projects. Another failure is allowing configuration complexity to overwhelm small projects by forcing every item to carry sprint, milestone, estimate, dependency, and portfolio metadata.

## Falsification

Reject if the same work item can show contradictory status in two views; if a roadmap item cannot be traced to underlying deliverables; if project health remains green while a critical milestone is blocked with no explanation; if closing a project destroys audit/history access; if nested portfolio rollups double-count work; or if a basic project cannot operate without filling advanced planning fields.

## Output contract

Return a `project-and-work-management-contract` containing: work-item taxonomy; canonical identity; project lifecycle; hierarchy/dependency model; ownership model; status authority; view semantics; scheduling/estimation hooks; health derivation; portfolio relationship; archive/closure rules; and minimal-versus-advanced configuration. Include one cross-view identity example and one blocked-project example.

## Handoffs

Delegate boards, backlog, sprint, roadmaps, milestones, dependencies, hierarchy, workload, status transitions, recurrence, templates, bulk edit, views, dashboards, time tracking, estimation, risks, portfolio, and closure to dedicated owners. Reuse generic assignment, workflow, approvals, collaboration, calendar, and data-dense skills as lower-level authorities.