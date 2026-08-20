---
name: designing-3d-viewport-navigation
description: Use when this specialist's decision ownership is materially in scope. Own orbit, pan, dolly/zoom, frame, pivot, projection, navigation speed, clipping, and spatial orientation in 3D authoring without colliding with modeling gestures.
---
# Designing 3D Viewport Navigation

## Parent Contract

**Required parent:** `designing-3d-cad-authoring-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own camera movement during 3D authoring. Decide orbit pivot, pan, dolly/zoom, frame selection/all, navigation speed, perspective/orthographic switching, clipping awareness, view cube/axes, and input mappings. This owner ensures navigation remains distinct from selection and modeling commands.

## Inputs and evidence

Require supported mouse/touchpad/pen/3D mouse/gamepad inputs, scene scale range, coordinate axes, projection types, clipping controls, selection behavior, platform conventions, and expert shortcut expectations. Test tiny parts, huge site models, and dense scenes where default pivoting often fails.

## Procedure

Define one predictable orbit pivot strategy with explicit alternatives such as orbit around selection or cursor. Pan/dolly should scale appropriately to scene distance and offer speed adjustment for extreme scales. Frame selection establishes a meaningful pivot without changing model state. Show projection mode and orientation axes persistently enough to recover spatial context. Clipping that hides geometry needs a visible cue and an easy fit/recover action. Input mappings should respect platform conventions while exposing remapping where expert tools require it. Navigation gestures must never silently move selected geometry.

## Failure topology

Failures include orbiting around a distant origin, zoom speed making small parts impossible to approach, getting trapped inside geometry, clipping making objects appear deleted, orthographic mode hidden, and trackpad gestures colliding with transform operations. Another failure is camera state changing when users merely select an object.

## Falsification

Reject if framing a valid object cannot recover from a lost camera; if navigation can mutate geometry; if projection mode cannot be identified; if clipping hides selected geometry without explanation; if orbit pivot jumps unpredictably during a gesture; or if supported input devices lack a complete navigation path without precision-only controls.

## Output contract

Return a `3d-viewport-navigation-contract` with: orbit pivot; pan/dolly behavior; speed scaling; frame commands; projection modes; orientation aids; clipping cues/recovery; input mappings; gesture conflict rules; and camera-state persistence. Include one microscopic-part and one kilometer-scale model scenario.

## Handoffs

Camera view management saves/recalls authored views, grid/snapping handles spatial editing, transform gizmos manipulate geometry, and accessibility/alternative-input owners provide modality equivalents.