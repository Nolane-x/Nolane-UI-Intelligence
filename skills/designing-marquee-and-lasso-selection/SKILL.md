---
name: designing-marquee-and-lasso-selection
description: Use when users select many spatial objects by drawing a rectangle or freeform region and the design must define geometric inclusion, live preview, viewport autoscroll, additive modifiers and non-pointer alternatives.
---

# Designing Marquee and Lasso Selection

## Parent Contract
**Required parent:** `designing-multi-selection-models`.

This faculty owns region-based spatial acquisition. It does not own the underlying selection set semantics or object hit-testing outside region selection.

## Decision Model
Choose region type from spatial task. Rectangular marquee is predictable for grid/canvas layouts; freeform lasso helps irregular arrangements but costs more motor effort and needs robust geometry. Define inclusion rule: object center inside, any intersection, full containment, or domain-specific hit shape. The rule should be inferable from feedback before release.

Selection preview should update as the region changes, but distinguish provisional membership from committed membership. When modifier keys add/subtract/toggle relative to an existing set, preview the final result rather than only new intersections.

Starting conditions matter. Dragging on empty canvas may begin a marquee, while dragging an object begins move. Small pointer jitter after click should not accidentally create a selection region; use an intent threshold that still supports motor impairments.

Near viewport edges, autoscroll or canvas pan can extend selection. Define speed, activation zone and how region coordinates remain stable in world space. Do not let autoscroll make the marquee detach from the pointer.

## Failure Topology
- Users cannot tell whether touching an object edge selects it until release.
- Marquee starts when trying to drag an object because hit-test precedence is wrong.
- Autoscroll changes coordinate basis and selection jumps.
- Lasso path with self-intersection selects unpredictably.
- Selection is only possible with precise pointer motion, with no list/tree/keyboard alternative.
- Dense objects flash selected/unselected every frame due to unstable boundary tests.

## Falsification and Recovery
Test tiny drag, object vs empty start, overlap/containment cases, zoom, rotated objects, autoscroll, additive/subtractive modifiers, touch/stylus and large canvas. The contract fails if the same geometric relation produces different membership because of frame timing.

Recover by simplifying inclusion geometry, stabilizing world coordinates, showing provisional highlights, separating click/drag thresholds and offering structured selection alternatives.

## Output Contract
Return `region-selection-contract` with region type, inclusion geometry, intent threshold, preview/commit state, modifier composition, world/screen coordinates, autoscroll behavior, accessibility alternatives and geometry fixtures.