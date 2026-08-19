---
name: designing-layout-reflow-motion
description: Use when existing interface regions change size or position and motion could preserve spatial orientation across reflow without obscuring responsive truth, causing overlap or fighting live input.
---

# Designing Layout Reflow Motion

## Parent Contract
**Required parent:** `designing-motion`.

This specialist owns transitions between two valid layouts of the same semantic objects. Responsive architecture, grid choice and content priority remain owned by layout/system faculties.

## Decision Model
First determine whether the before/after states represent **the same objects in a new arrangement**. If semantic identity changed, a shared reflow animation may mislead. For stable identity, motion can preserve object constancy when panels resize, filters appear, sidebars collapse, density changes or a grid repacks.

Separate layout calculation from visual interpolation. The destination geometry must already be valid at the target viewport and content size. Techniques that visually transform from old bounds to new bounds can be useful, but they must not leave text raster-scaled, focus outlines displaced or hit targets at stale coordinates.

Continuous resize is different from discrete mode change. During a user-dragged splitter or browser resize, the interface should usually track geometry directly rather than launching a new easing on every frame. After a discrete breakpoint transition or command, a short reflow may help if it remains interruptible.

Content rewrapping is especially sensitive. Animating block dimensions while text repeatedly reflows can create shimmer and unreadable intermediate lines. Prefer stable container transitions, crossfade only when information remains equivalent, or skip animation.

## Failure Topology
- Hit testing follows final layout while visuals still show old positions.
- Text scales like an image during reflow and becomes blurry.
- Every `ResizeObserver` event starts a new animation, producing perpetual lag.
- Responsive breakpoint motion hides content that should immediately become reachable.
- Focus ring and element geometry diverge during transforms.
- Masonry cards cross through one another and lose identity.

## Falsification and Recovery
Resize continuously, cross breakpoints back and forth, change text size, localize labels, open panels during reflow, tab through moving controls and throttle rendering. Inspect intermediate frames for overlap and semantic/visual mismatch. If motion makes the current actionable geometry ambiguous, remove it for that path.

Recover by snapping interaction geometry to visible geometry, limiting animation to discrete transitions, preserving object identity keys and avoiding interpolation of text-heavy dimensions.

## Output Contract
Return `layout-reflow-motion-contract` with stable identities, transition triggers, geometry strategy, continuous-resize policy, text/focus handling, interruption behavior, reduced-motion mode and intermediate-frame validation.