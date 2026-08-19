---
name: designing-drag-inertia-and-snap
description: Use when a draggable object continues, resists or settles after direct manipulation and the physics must support prediction, precision and safe target acquisition rather than ornamental momentum.
---

# Designing Drag Inertia and Snap

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This faculty owns post-contact movement physics and snapping behavior for direct manipulation. It does not define what can be dragged, drop semantics, accessible alternatives or the coordinate system itself.

## Decision Model
Start from task precision. Free panning, carousels and map surfaces can benefit from inertia; placing a node on a circuit diagram or resizing a crop box may require near-zero residual motion. Momentum is justified only when it reduces effort without reducing control.

If inertia is used, define velocity sampling, deceleration, bounds and interruption. The user must be able to re-contact and stop the object immediately. Do not let an object coast through destructive zones or commit a drop merely because a physics simulation crossed a target after release unless that behavior is explicitly expected.

Snapping is a semantic attraction system, not a magic number. Targets can be grid lines, guides, neighboring edges, timeline frames, detents or valid drop zones. Define activation radius, hysteresis and release behavior. Visual/haptic cues should reveal the active snap relation before commitment. When several targets compete, use deterministic priority based on task meaning and distance; avoid jitter between nearly equal candidates.

Zoom changes the relationship between screen pixels and world units. Snap tolerance should be defined in the coordinate space that matches human acquisition, often screen-space with semantic constraints.

## Failure Topology
- Inertia makes precision placement impossible.
- A snap target captures the object unexpectedly from too far away.
- Two guides compete frame-to-frame and the object vibrates.
- Snap tolerance becomes microscopic at one zoom level and enormous at another.
- Keyboard nudge and pointer snap land on different canonical coordinates.
- Momentum continues after modality changes or the object becomes invalid.

## Falsification and Recovery
Test slow and fast release, re-grab during inertia, competing snap targets, zoom extremes, constrained axes, boundary collisions, keyboard nudging and performance throttling. Plot final coordinate against declared rule; frame-rate-dependent outcomes are a failure.

Recover by reducing momentum, introducing hysteresis, stabilizing target priority, separating preview snap from committed coordinate and using semantic world coordinates for final values.

## Output Contract
Return `drag-inertia-snap-contract` containing task precision class, velocity/deceleration model, interruption, bounds, snap target taxonomy, tolerance/hysteresis, priority, feedback channels, zoom policy and deterministic tests.