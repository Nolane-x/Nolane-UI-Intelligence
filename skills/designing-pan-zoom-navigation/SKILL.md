---
name: designing-pan-zoom-navigation
description: Use when users navigate a large 2D/3D work surface by panning and zooming and the design must preserve focal point, scale limits, coordinate orientation, input conflicts and recovery to meaningful views.
---

# Designing Pan and Zoom Navigation

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This faculty owns viewport navigation over a larger world. It does not own object movement, map-specific semantics or camera orbit in a full 3D scene.

## Decision Model
Represent viewport state explicitly: translation, scale and optional rotation/origin. Zoom should usually preserve a meaningful focal point—the pointer position, gesture centroid, selected object or viewport center depending on modality/context. Arbitrary zoom toward top-left makes spatial navigation expensive.

Set min/max scales from task semantics. Minimum may fit the whole canvas; maximum may reach pixel/feature precision. At extremes, adjust detail level rather than allowing labels/handles to become unusable. Provide deterministic commands such as Fit all, Fit selection, 100%, Reset view or Zoom to result.

Input mappings must avoid conflict. Wheel may scroll a page, pan a canvas or zoom with modifier; pinch usually zooms; space-drag may pan in creative tools; middle mouse may follow platform conventions. When the canvas is nested in a scrollable page, clearly define when gesture ownership transfers.

Panning can use inertia only if precision permits. Zoom animation should be interruptible and should not prevent immediate interaction with the destination.

## Failure Topology
- Wheel unexpectedly zooms when users expect page scroll, trapping them in the canvas.
- Zoom changes around viewport origin and selected object flies away from the pointer.
- Handles/text scale into unusability at zoom extremes.
- Fit selection includes hidden/off-canvas artifacts and produces a tiny view.
- Pinch and object transform gestures compete.
- Users get lost with no reset/overview path.

## Falsification and Recovery
Test mouse wheel, trackpad pinch/pan, touch pinch, keyboard zoom, nested page scroll, zoom at edges, fit commands, huge extents and reduced motion. Verify inverse transform accuracy from screen to world coordinates.

Recover by clarifying gesture ownership, zooming around a stable focal point, clamping semantic scale, adding overview/reset commands and separating viewport gestures from object manipulation modes.

## Output Contract
Return `pan-zoom-navigation-contract` with viewport state, focal-point rules by modality, scale bounds/detail adaptation, gesture map, scroll ownership, fit/reset commands, inertia/animation policy and coordinate tests.