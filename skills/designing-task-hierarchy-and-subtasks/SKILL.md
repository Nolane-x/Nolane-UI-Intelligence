---
name: designing-task-hierarchy-and-subtasks
description: Use when this specialist's decision ownership is materially in scope. Own parent-child work decomposition, rollup semantics, depth limits, completion rules, moving subtrees, and visibility of hidden descendant work.
---
# Designing Task Hierarchy and Subtasks

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own decomposition of work into parent and child items. Decide allowed depth, whether parents are executable work or containers/outcomes, how completion and progress roll up, how subtrees move, what fields inherit, and how collapsed descendants remain discoverable. Dependency is separate from hierarchy even when a child must finish before a parent can complete.

## Inputs and evidence

Require work-item types, nesting depth expected in real projects, parent completion policy, field inheritance, ownership model, estimate/progress rollup, permissions, and how hierarchy appears across list, board, search, and roadmap views. Identify whether children may live in different projects or sprints.

## Procedure

Choose a hierarchy depth that matches actual planning needs rather than enabling arbitrary nesting by default. Make parent meaning explicit: summary/outcome, deliverable, epic, task, or generic container. Collapsed parents need descendant counts and risk/blocker indicators so hidden work does not vanish. Moving a subtree should preview changes to project, permissions, sprint, milestone, or inherited fields. Rollups must state whether values are sum, completion ratio, manual status, or not meaningful. Parent completion should enforce or explicitly waive required child states rather than silently closing unfinished work.

## Failure topology

Failures include infinite nesting, parents shown complete while required children remain open, double-counted estimates at parent and child levels, hidden blocked descendants, subtree moves stripping permissions or project context, and board views that flatten hierarchy so duplicate-looking cards lose lineage. Another failure is using hierarchy as a substitute for dependency.

## Falsification

Reject if a parent can appear healthy while a hidden required child is blocked with no cue; if aggregate estimates double-count parent plus children; if moving a subtree can relocate children across projects without preview; if search results cannot reveal ancestry; if users cannot distinguish parenthood from dependency; or if a child can be orphaned by deleting its parent without an explicit disposition.

## Output contract

Return a `task-hierarchy-and-subtasks-contract` containing: supported hierarchy types/depth; parent semantic roles; field inheritance; collapse/hidden-state cues; progress/estimate rollup; subtree move protocol; parent completion rule; orphan/delete handling; cross-view ancestry; and hierarchy-versus-dependency distinction. Include one collapsed blocked descendant example.

## Handoffs

Use dependency networks for ordering/blocking, bulk editing for subtree operations at scale, project views for flatten/group options, and portfolio rollups for project-level rather than work-item-level hierarchy.