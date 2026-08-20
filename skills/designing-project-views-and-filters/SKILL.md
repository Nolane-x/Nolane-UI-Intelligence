---
name: designing-project-views-and-filters
description: Use when this specialist's decision ownership is materially in scope. Own project view definitions across list, board, timeline, grouped, personal, and saved perspectives while preserving one canonical work-item truth.
---
# Designing Project Views and Filters

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how project work is projected into saved views without duplicating data semantics. Decide view types, filter/group/sort definitions, personal versus shared scope, saved view ownership, defaults, filter visibility, and how counts/aggregates disclose excluded items. This owner ensures a view is a query/presentation, not a second source of truth.

## Inputs and evidence

Require canonical work-item fields, expected view types, filter dimensions, permission model, personal/team sharing needs, default project perspective, large-data performance, and whether view configuration can encode workflow consequences such as board columns mapped to state. Identify filters that can hide critical work or alter summary counts.

## Procedure

Represent every view as explicit query + grouping + sorting + presentation settings. Keep active filters discoverable even when compacted; a user should not mistake filtered absence for missing work. Saved views need names, owner/scope, and permission behavior. Shared view edits should either version/change for everyone intentionally or support personal forks. When switching list/board/timeline, preserve the query if the semantics still apply. Counts and health summaries must state whether they reflect filtered or total project scope. Deep links should restore the same view definition and selected item where permissions allow.

## Failure topology

Failures include view-specific copies of tasks diverging, hidden filters causing "missing" work, shared views changing under users without attribution, board grouping that silently changes status semantics, counts based on filtered data presented as project totals, and deep links reopening a default unfiltered view. Another failure is an explosion of nearly identical saved views with no ownership/cleanup model.

## Falsification

Reject if editing an item in one view does not immediately reflect in another canonical view; if users cannot identify active filters; if a shared view can be mutated without knowing who is affected; if summary counts conceal filter scope; if deep-link restoration loses query context; or if switching presentation types changes item membership unexpectedly.

## Output contract

Return a `project-views-and-filters-contract` with: supported presentation types; query/filter model; grouping/sort rules; active-filter disclosure; personal/shared view lifecycle; ownership and permissions; cross-presentation preservation; count/aggregate scope; deep-link state; and stale-view cleanup. Include one filtered-health summary example.

## Handoffs

Kanban boards, roadmaps, and dashboards consume view/query scope but retain their own presentation semantics. Saved search/filter builders provide lower-level query controls; this owner governs their project-wide consistency.