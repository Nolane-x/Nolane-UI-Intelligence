---
name: designing-3d-grid-and-snapping
description: Use when this specialist's decision ownership is materially in scope. Own precision snapping in three dimensions across grid, vertex, edge, face, midpoint, center, tangent, axis, plane, and custom references with visible target and coordinate context.
---
# Designing 3D Grid and Snapping

## Parent Contract

**Required parent:** `designing-3d-cad-authoring-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own spatial precision constraints used during 3D creation and movement. Decide grid planes/spacing, snap target types, priority, temporary modifiers, inferred axes/planes, custom references, tolerance, target highlighting, and unit-aware increments. Generic 2D snapping does not handle depth ambiguity or multiple reference planes.

## Inputs and evidence

Require coordinate system, model units/precision, supported geometry primitives, snapping algorithms, grid planes, construction geometry, transform tools, input modalities, zoom/scene scale, and CAD conventions. Identify operations where nearest-screen-point differs from nearest-3D target.

## Procedure

Show active working plane/grid and current snap modes. As pointer/gizmo moves, highlight the exact 3D target with type and, where ambiguous, coordinate/depth cue. Allow temporary override to disable or select a snap mode without opening settings. Priority rules should avoid jumping unpredictably among vertex/edge/face targets; provide cycling when candidates overlap. Grid increments follow units and zoom only when the change is visible. Custom planes/axes need stable identity and clear exit/reset to world context.

## Failure topology

Failures include snapping to a back-face vertex through visible geometry, grid plane unknown, changing grid scale invisibly, target highlight lagging behind committed point, unit increment mismatch, and inferred axes persisting unexpectedly. Another failure is a magnet icon that says snapping is on without revealing which target kinds are active.

## Falsification

Reject if committed location can differ from highlighted snap target; if depth/occlusion ambiguity is unresolved; if working plane cannot be identified; if overlapping targets cannot be cycled/disambiguated; if snap increments change without visible indication; or if temporary snap override can remain active accidentally after the operation.

## Output contract

Return a `3d-grid-and-snapping-contract` with: coordinate/grid plane; spacing/unit rules; snap target taxonomy; target priority/cycling; occlusion/depth policy; highlight/commit guarantee; temporary modifiers; custom references; inferred constraints; tolerance; and reset behavior. Include one overlapping front/back vertex case.

## Handoffs

Viewport navigation supplies camera context, measurement/parametric constraint owners use precision results, modeling operations invoke snapping, and generic snapping provides lower-level proximity mechanics.