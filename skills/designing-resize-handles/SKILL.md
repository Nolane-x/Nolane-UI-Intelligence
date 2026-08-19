---
name: designing-resize-handles
description: Use when selected objects expose direct resize affordances and the design must define handle geometry, axis/aspect constraints, hit targets, feedback and accessible precision controls.
---

# Designing Resize Handles

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This specialist owns object-level direct resize handles. Panel dividers and general transform gizmos are sibling faculties.

## Decision Boundary
Choose handle set based on allowed degrees of freedom. Corner handles imply two-axis resize; edge handles imply one-axis; media may preserve aspect by default with a modifier to override; line/connector endpoints may change topology rather than bounding-box size and should use a different affordance.

Visual handle size and interactive hit target can differ. At high zoom, tiny screen-space handles are unusable; at low zoom, world-space handles can become enormous. Keep acquisition largely screen-space while maintaining accurate world-space geometry. Touch requires larger targets and enough separation from rotate/anchor controls.

During resize, reveal current dimensions or domain units when precision matters. Modifiers may resize from center, preserve ratio or snap, but do not overload hidden modifier chords as the only path—property inspector/numeric input can provide exact alternatives.

Respect minimum/maximum and content constraints. When bounds are reached, feedback should indicate resistance/limit rather than allowing the pointer to keep moving while the object silently stops with no explanation.

## Failure Topology
- Handles scale with object and become microscopic when zoomed out.
- Corner handle sits on top of rotate handle and touch users trigger the wrong transform.
- Aspect ratio suddenly breaks because modifier state was sampled only at drag start.
- Text box resizes geometry while text clipping is hidden until release.
- Visual handle is 6 px and hit area is also 6 px.
- Screen reader/keyboard users have no precision resize route.

## Falsification and Recovery
Test zoom extremes, touch/stylus, min/max, aspect modifiers changed mid-drag, rotated objects, text/media, keyboard numeric resize and snapping. The contract fails if the pointer can indicate a geometry that the object cannot reach without feedback.

Recover by separating screen-space handles from world-space transforms, enlarging invisible hit zones, exposing constraints/dimensions and providing property/nudge alternatives.

## Output Contract
Return `resize-handle-contract` with enabled handles, screen-space hit geometry, axis/aspect rules, constraint feedback, modifier behavior, precision/numeric alternatives, zoom/touch adaptation and transform tests.