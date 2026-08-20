---
name: designing-responsive-canvas-workspaces
description: Adapt canvas-centric creative and spatial workspaces to constrained windows without sacrificing scene visibility, tool reachability, or manipulation continuity.
---

# Designing responsive canvas workspaces

Canvas applications depend on a large continuous work area surrounded by tools, inspectors, timelines, layers, or asset browsers. Use this skill when the shell must adapt without reducing the canvas to an unusable remnant.

## Decision ownership

Own minimum viable canvas area, tool/panel adaptation, viewport fit policy, overlay regions, command access, and preservation of zoom/pan/selection across layout transitions. Decide which peripheral regions collapse first and what becomes transient.

## Inputs and evidence

Collect common window sizes, canvas aspect ratios, zoom levels, selection workflows, open panels, timeline heights, tool usage frequency, pointer/touch/stylus modality, and user-customized layouts. Measure how much unobscured canvas users need for precise manipulation.

## Procedure

Treat the canvas as a primary invariant region with explicit minimum dimensions. Define a collapse hierarchy for inspectors, asset panels, tool labels, and timelines. Use overlays or drawers for secondary regions only when they do not repeatedly cover the selected object or manipulation handles.

Preserve world-space zoom, pan center, active tool, selected objects, and undo state when shell geometry changes. Recompute fit-to-view only when the user requests it or the existing view becomes wholly invalid; responsive resize should not constantly “helpfully” reset framing.

## Failure topology

Shell panels can squeeze the canvas below workable size while still technically fitting. Responsive reflow may reset zoom or recenter the scene, destroying spatial memory. Overlay controls can intercept drag gestures near canvas edges.

Mobile adaptation can become a desktop UI shrunk to tiny icons rather than a re-prioritized tool workflow.

## Falsification

Resize during drag, transform, text edit, and multi-selection. Verify scene coordinates and active tool remain stable. Test panel combinations, touch/stylus, virtual keyboard, and full-screen canvas modes. Measure occlusion of selected objects by overlays.

If users repeatedly toggle panels just to manipulate the current selection, the responsive shell needs better coordination.

## Output contract

Produce a `responsive-canvas-workspaces-contract` with minimum canvas geometry, peripheral-region priorities, overlay policy, tool-access transformations, spatial-state preservation, gesture boundaries, and tests during active manipulation.

## Handoffs

Use `designing-editor-canvas-workspaces` for base canvas architecture, `designing-responsive-panel-docking` for inspector behavior, `designing-responsive-toolbar-overflow` for tools, and `verifying-responsive-state-parity` for command availability.