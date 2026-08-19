---
name: designing-popover-origin-motion
description: Use when a nonmodal anchored surface needs motion that communicates attachment to its invoker while remaining correct under collision avoidance, arrow repositioning, scrolling and anchor movement.
---

# Designing Popover Origin Motion

## Parent Contract
**Required parent:** `designing-motion`.

This specialist owns spatial continuity between an anchor and an anchored nonmodal surface. It does not decide popover semantics, dismissal rules or whether a popover is the correct component.

## Decision Model
Treat final placement as an input to motion, not a styling afterthought. Popovers may appear above, below or beside the anchor; collision middleware can shift or flip them. Derive transform origin and directional bias from the **resolved geometry**. When an arrow is present, its attachment point can guide origin, but do not force exaggerated scaling from a tiny arrow tip.

Choose whether the popover tracks a moving anchor. A color inspector attached to a canvas selection may need continuous repositioning; a transient help popover may close when its anchor scrolls away. If tracking, avoid an animation chasing layout updates with lag. Geometry updates should be critically damped or snapped when motion would make targeting difficult.

The entrance should clarify attachment without delaying reading or interaction. Content height may change after async data arrives; do not replay the entrance each time. For nested or chained popovers, preserve clear ownership so multiple surfaces do not appear to emerge from the same point.

If the anchor disappears, decide explicitly: dismiss, retarget to a semantic successor, or detach into a persistent panel. Never animate toward stale coordinates.

## Failure Topology
- The surface flips above the trigger but still grows from its bottom edge.
- Position animation trails a scrolling anchor and creates a rubber-band effect.
- Async content resize repeatedly retriggers scale motion.
- The arrow and body animate on different coordinate systems and visibly separate.
- A popover survives anchor deletion with no intelligible attachment.

## Falsification
Open near four edges/corners, scroll containers, zoom, resize, change anchor dimensions, load dynamic content, delete the anchor, and test reduced motion. Capture geometry at intermediate frames: the motion fails if it communicates an origin inconsistent with the actual anchor relationship or harms pointer acquisition.

## Recovery
Base motion on resolved placement, reduce travel, separate content-resize transitions from entrance, and choose a deterministic anchor-loss policy. When placement is highly unstable, prefer opacity or immediate appearance over directional motion.

## Output Contract
Return `popover-origin-motion-contract` with anchor identity, resolved-placement mapping, transform-origin logic, tracking policy, resize behavior, anchor-loss policy, reduced-motion equivalent and geometry stress tests.