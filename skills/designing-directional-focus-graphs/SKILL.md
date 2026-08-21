---
name: designing-directional-focus-graphs
description: Use when users navigate an interface with directional input such as a gamepad, remote, D-pad, or keyboard arrows and the product needs a deterministic focus graph that survives dynamic layout, disabled items, virtualized content, overlays, and spatial ambiguity.
---

# Designing Directional Focus Graphs

## Focus is a graph, not nearest-neighbor geometry
Directional interfaces fail when focus movement is delegated to whichever element happens to be closest on screen. Grids, staggered cards, nested rails, overlays, disabled items, and dynamic content create ambiguous geometry. This skill owns the semantic graph that maps directional intent to the next valid focus target.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist when directional navigation is a material interaction mode. Broader gamepad/remote accessibility guidance may supply platform constraints, but this skill owns the focus topology itself.

## Node and edge model
Represent each focusable target as a stable node with region membership, availability, priority, and restore identity. Directional edges may be explicit, derived from geometry under bounded rules, or delegated to a container. The decision owner is when geometry is safe and when semantic edges are required.

A graph should avoid dead ends unless the end is intentional. Disabled or removed nodes must not remain destinations. Virtualized nodes need a strategy for scroll-then-focus rather than pretending offscreen elements already exist. Overlay activation should create a temporary focus subgraph and preserve the prior return node.

## Region semantics
Large-screen interfaces often contain rails, grids, sidebars, and toolbars whose internal navigation differs from cross-region navigation. Define entry and exit anchors for each region. A horizontal rail may preserve the last focused child when the user returns from a vertical move, while a grid may choose the nearest row-aligned item. Those are product decisions, not incidental browser behavior.

## Dynamic updates
When content inserts, sorts, filters, or becomes unavailable, recompute only edges affected by the change and preserve focus identity when the underlying item still exists. If the focused item disappears, move to the most semantically adjacent fallback and communicate context when necessary. Do not jump to the first item globally merely because a DOM node unmounted.

## Evidence
Evidence includes graph snapshots for representative states, directional traversal traces, entry/exit behavior, overlay transitions, disabled-item handling, and focus restoration after dynamic updates. Capture paths with real controller/remote input where platform event behavior matters.

## Failure modes
Characteristic Failure includes focus oscillation between two nodes, invisible offscreen destinations, geometry-based jumps across unrelated regions, disabled targets capturing focus, virtualized lists losing identity, and overlays returning focus to an arbitrary default. Another failure is asymmetry with no rationale: Right from A reaches B, but Left from B cannot return to A even though nothing changed.

## Falsification
Randomly disable nodes, insert content, change aspect ratio, open nested overlays, virtualize a long rail, and traverse every edge from representative nodes. The contract fails if a reachable node has no sensible exit, if focus lands on hidden/unavailable content, if return paths lose context, or if graph behavior changes unpredictably with small layout shifts.

## Recovery
Freeze the problematic state, serialize the current node/edge graph, identify whether the defect is missing semantic ownership or unstable geometry, and repair the smallest region. Restore a stable focus identity after updates rather than resetting navigation. If a region’s structure no longer fits its original navigation model, route back to layout/interface architecture.

## Output and Handoff
Output: `directional-focus-graphs-contract`, containing node identity, region membership, edge rules, dynamic invalidation, virtualization, overlays, and restoration. Handoff device-specific button semantics to remote-control navigation and controller input handling to input-device prompt switching/remapping where relevant.

## Sibling Boundary and delete-the-skill
Sibling remote-control navigation owns remote-specific command mapping and long-range navigation conventions; this skill owns spatial focus adjacency for any directional device. The delete-the-skill test passes because without a focus graph owner, large-screen navigation becomes an emergent property of geometry and DOM order rather than a designed interaction model.