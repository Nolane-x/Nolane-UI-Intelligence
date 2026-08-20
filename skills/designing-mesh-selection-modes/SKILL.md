---
name: designing-mesh-selection-modes
description: Use when this specialist's decision ownership is materially in scope. Own component-level mesh selection across object, vertex, edge, face, element, loop, ring, connected, and occlusion-aware modes with stable feedback and mode transitions.
---
# Designing Mesh Selection Modes

## Parent Contract

**Required parent:** `designing-3d-cad-authoring-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how users select sub-object mesh topology. Decide object/edit transition, vertex/edge/face modes, mixed selection, loop/ring/connected expansion, through-selection versus visible-only, backface/occlusion behavior, growth/shrink, and persistence across operations. Generic multi-selection does not own topology semantics.

## Inputs and evidence

Require mesh topology model, editable component types, viewport/render modes, occlusion data, modifier/derived geometry behavior, selection history, input shortcuts, and expected mesh scale. Identify whether selection applies to base cage, evaluated mesh, or both.

## Procedure

Persistently show current component selection mode and edited object. Mode changes should convert or preserve selection according to explicit rules, not arbitrary loss. Hover/preselection must distinguish vertex/edge/face target before click. Visible-only versus through selection needs an obvious toggle or modifier with depth cue. Loop/ring and connected operations should preview or allow immediate undo when topology yields surprising branches. Derived/modifier geometry should indicate whether visible components are directly selectable/editable. Selection statistics can reveal hidden component counts at high scale.

## Failure topology

Failures include face selection while users think they are in object mode, selecting vertices through the model unintentionally, mode switch clearing costly selection, loop select crossing non-manifold topology unexpectedly, and editing a base component that does not correspond clearly to evaluated geometry. Another failure is selection highlight obscured by materials or wire overlays.

## Falsification

Reject if current component mode cannot be identified; if hover target type is ambiguous; if through/visible selection state is hidden; if switching modes can discard selection without known rule; if non-editable derived geometry looks directly editable; or if selection remains invisible under supported viewport shading.

## Output contract

Return a `mesh-selection-modes-contract` with: object/edit state; component modes; conversion/preservation rules; preselection feedback; occlusion/through-selection; loop/ring/connected operations; topology exceptions; derived-geometry policy; selection statistics; and highlight requirements. Include one non-manifold loop-select case.

## Handoffs

Modeling operations consume component selection, viewport navigation must not change it, transform gizmos manipulate selected components, and generic selection supplies modifier keys/history but not mesh topology rules.