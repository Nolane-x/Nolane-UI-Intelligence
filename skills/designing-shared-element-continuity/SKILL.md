---
name: designing-shared-element-continuity
description: Use when an identifiable object persists across views and a shared-element transition could explain navigation, expansion or mode change without fabricating identity between merely similar visuals.
---

# Designing Shared Element Continuity

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns continuity for a semantic object that survives a view transition. It does not authorize navigation structure, determine object identity, or require a shared-element animation merely because two rectangles look alike.

## Decision Boundary
A valid shared element needs an **identity claim**: the thumbnail becoming the detail hero, the selected canvas object becoming an inspector preview, the compact player expanding into the full player. Similar color, image or geometry is insufficient if the objects represent different entities.

Define which properties may interpolate. Position and bounds often communicate continuity; crop, corner radius, material, typography and controls may need staged changes. Do not morph text between unrelated content or stretch raster media beyond acceptable quality. When source and destination aspect ratios differ, decide crop continuity explicitly rather than letting the renderer jump at midpoint.

Navigation must remain semantically complete even if the transition cannot run—deep link, reduced motion, back/forward restoration, server render and low-end devices may have no source geometry. The destination cannot depend on animation state to become usable.

Reverse transitions require fresh identity and geometry. If the list was resorted or the source item is offscreen on return, forcing a reverse flight to stale coordinates is worse than a simple exit.

## Failure Topology
- Two visually similar cards are treated as the same entity and the animation lies about object identity.
- Source is removed before destination captures geometry, causing a flash or jump.
- Back transition targets a recycled virtualized row representing another item.
- Text and controls stretch with the container and become unreadable.
- Deep links reveal an empty placeholder because there was no source animation.

## Falsification and Recovery
Enter from in-app source, deep link, browser history, virtualized/scrolled source, reordered list, image-loading failure and reduced motion. Verify identity IDs at both ends and sample intermediate crop/semantics. A transition fails if it teaches a false relationship or makes the destination depend on origin presence.

Recover by limiting continuity to properties with real semantic persistence, using destination-first rendering, and falling back to local entrance/exit when identity or geometry cannot be proven.

## Output Contract
Return `shared-element-continuity-contract` with semantic identity key, source/destination ownership, interpolated properties, crop/material staging, reverse eligibility, origin-missing fallback, interruption rules and identity tests.