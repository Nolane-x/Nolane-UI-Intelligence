---
name: designing-transform-gizmos
description: Use when 2D or 3D objects need translation, rotation or scale controls and the interface must make coordinate axes, active constraints, local/world space, selection scope and precision legible.
---

# Designing Transform Gizmos

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns multi-degree transform manipulators. It does not own scene camera navigation, object selection or domain geometry math beyond interaction-facing constraints.

## Decision Model
Name transform modes and coordinate space explicitly. Translation, rotation and scale can use separate gizmos or a combined manipulator, but the user must know which axis/plane/control is active before movement begins. In 3D, local vs world orientation changes the meaning of the same colored axis; surface that mode persistently.

Hit testing must favor intent. Axis shafts, plane handles, rotation rings and center/free-move handles overlap in projection. Use priority based on pointer proximity and projected geometry, plus hover/focus highlighting before commitment. Do not rely solely on color to distinguish axes; shape, labels or orientation cues are needed.

Selection scope changes pivot behavior. Single object, multi-selection, group and component instance may transform around individual centers, selection center, active object or custom pivot. Make pivot mode clear and preserve it across pointer and numeric inspector edits.

Precision paths include snapping, modifier constraints, numeric entry and nudge. Direct manipulation should preview authoritative coordinates and support cancel/revert to pre-drag transform.

## Failure Topology
- Camera angle causes X/Y axes to overlap and the wrong one wins hit testing.
- Local/world mode changes but gizmo orientation lags behind.
- Multi-selection scale unexpectedly scales each object around its own center.
- Color-blind users cannot distinguish axis controls.
- Dragging the rotation ring also orbits the camera due to gesture ownership conflict.
- Cancel restores visual pose but not underlying transform values.

## Falsification and Recovery
Test oblique camera angles, tiny/huge objects, local/world switch, single/multi/group selection, modifiers, numeric edits during mode change, undo/cancel, touch/stylus and color-independent cues. The contract fails if the active degree of freedom is ambiguous before drag.

Recover by simplifying visible controls per mode, improving projected hit priority, exposing coordinate/pivot state, and separating camera and object gesture ownership.

## Output Contract
Return `transform-gizmo-contract` with transform modes, coordinate/pivot policy, projected hit regions, active-axis feedback, selection scope, precision/snap integration, camera conflict rules, cancel/undo and geometry tests.