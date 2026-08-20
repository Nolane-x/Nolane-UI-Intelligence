---
name: designing-port-and-connector-authoring
description: Own discoverability, compatibility, direction, creation, reconnection, and cancellation of semantic graph connections through ports or connection targets.
---
# Designing Port and Connector Authoring

## Decision ownership

Own how a user expresses that two graph entities should be connected. Decide whether connection happens through explicit ports, whole-node targets, typed handles, command selection, or keyboard sequence; how compatibility is previewed; when direction is clear; and how an existing connection is safely reattached or cancelled. Edge geometry after a valid connection belongs to routing; this owner is about relationship intent and commit semantics.

## Inputs and evidence

Require edge types, source/target direction rules, port cardinality, type compatibility matrix, whether ports are fixed or dynamically generated, common connection frequency, graph density, precision constraints, touch/pen needs, keyboard access, and consequences of creating or breaking a relationship. Identify whether port labels carry domain meaning such as input/output channels, data type, signal direction, or control flow.

## Procedure

Make connectable origins discoverable without permanently flooding every node with handles. Reveal ports on focus/selection/intent when density demands it, but provide a persistent semantic cue where connection affordance is essential. Starting a connection must visually lock the origin and narrow target eligibility; incompatible targets should be distinguishable before release, not merely rejected afterward. Define direction explicitly with source/target semantics, not just arrow styling. On hover or keyboard traversal, expose port identity and compatibility. Reconnection should preserve the old edge until a valid new target commits or make the pending destructive change unmistakable. Provide cancellation via Escape/back action and a non-drag alternative for motor/accessibility needs.

## Failure topology

Common failures are microscopic handles, hidden ports discoverable only by mouse hover, compatible and incompatible targets looking identical, arrow direction lost at low zoom, connection drags that pan the canvas, accidental edge deletion during reconnection, and ports whose labels vanish while users need them most. Another failure is accepting a visually plausible connection that violates domain type constraints and only surfacing the error much later.

## Falsification

Reject if a first-time user cannot locate a connection affordance on a focused node; if keyboard users cannot choose source and target; if the design permits a relationship to be dropped onto an incompatible target without pre-commit warning; if reconnection can destroy the previous relationship on cancellation; if dense-node overlap makes target identity ambiguous; or if touch targets require precision below the product's accessibility target-size policy.

## Output contract

Return a `port-and-connector-authoring-contract` containing: connection origins; port visibility policy; compatibility matrix presentation; direction cues; start/pending/valid/invalid/committed/cancelled states; reconnection semantics; destructive-break handling; keyboard and touch alternatives; zoom-level behavior; and error/recovery rules. Include the semantic payload handed to edge routing after commit.

## Handoffs

Delegate post-commit path geometry to `designing-edge-routing-and-bendpoints`, structural rule enforcement to `designing-graph-validation-and-errors`, and type-specific modeling conventions to flowchart/UML/executable-graph owners. Generic accessible drag-and-drop and pointer-input skills provide motor mechanics but are subordinate to this relationship contract.