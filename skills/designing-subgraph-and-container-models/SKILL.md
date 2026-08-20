---
name: designing-subgraph-and-container-models
description: Use when this specialist's decision ownership is materially in scope. Define nested graph containers, subgraphs, collapse behavior, reparenting, boundary-crossing edges, and the semantics of hidden structure.
---
# Designing Subgraph and Container Models

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own structural grouping when a graph needs containers that are more than visual rectangles. Decide whether membership changes semantics, how nested containers work, how nodes are reparented, how collapse represents hidden nodes and crossing edges, and how users distinguish grouping for organization from domain ownership. Freeform object grouping remains with the generic workspace owner; this skill owns graph-aware containment.

## Inputs and evidence

Collect container types, allowed nesting depth, membership constraints, whether containers represent teams/stages/modules/security zones, boundary-crossing edge semantics, layout constraints, collapse frequency, permissions, and whether hidden internal state can still be operationally active. Identify cases where one node may belong to multiple conceptual groups even if physical containment allows only one parent.

## Procedure

Make the membership model explicit before drawing boxes. If containers imply hierarchy, show parentage in both canvas and an outline/inspector. Define valid reparenting targets and preview structural consequences before drop. Collapsing a container must preserve external relationships through boundary summaries, aggregated ports, counts, or proxy edges; do not simply make edges disappear. Specify selection semantics for container versus contents and how move/resize affects members. Nested collapse needs a stable breadcrumb or hierarchy path. If membership changes permissions or runtime behavior, treat drag-to-reparent as a consequential action with confirmation or policy feedback.

## Failure topology

Failures include decorative groups mistaken for semantic containers, nodes visually inside a region but structurally outside it, collapsed groups hiding critical dependencies, proxy edges that imply one connection where many incompatible relationships exist, accidental reparenting during drag, and deep nesting that traps users without a path back. Hidden active failures are especially dangerous when collapsed content can be unhealthy but the container looks normal.

## Falsification

Reject if visual containment and actual membership can diverge without a clear cue; if collapsing a subgraph makes external dependencies impossible to discover; if reparenting can alter permissions/runtime semantics with no consequence preview; if users cannot select a container without selecting its contents; or if nested containers can be entered but not navigated back through a visible hierarchy.

## Output contract

Return a `subgraph-and-container-models-contract` with: container taxonomy; membership semantics; nesting rules; selection/move behavior; reparenting protocol; collapse/expand representation; boundary-edge aggregation; hidden-state indicators; hierarchy navigation; permission/consequence rules; and serialization identity requirements. Include an example with at least one nested container and a cross-boundary relationship.

## Handoffs

Use `designing-graph-auto-layout-controls` for constrained arrangement, `designing-edge-routing-and-bendpoints` for paths crossing boundaries, and `designing-graph-validation-and-errors` for illegal membership. Swimlanes have their own owner because lane sequence/participant meaning differs from generic containment.