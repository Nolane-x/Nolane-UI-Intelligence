---
name: designing-graph-minimap-overviews
description: Use when this specialist's decision ownership is materially in scope. Own miniature graph overview surfaces that communicate viewport location, distant structure, marked regions, and fast navigation without becoming deceptive decoration.
---
# Designing Graph Minimap Overviews

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the graph minimap/overview as a navigation instrument. Decide what structural detail survives compression, how the current viewport is represented, how users pan/jump through the minimap, which search/error/collaboration markers appear, and when the minimap should hide, expand, or become an overview mode. This skill does not own the full graph layout.

## Inputs and evidence

Collect graph aspect ratio, density, layout stability, viewport size range, zoom range, node criticality, marker types, theme/contrast constraints, touch target needs, and performance budget. Determine whether spatial location is stable enough that a minimap supports memory; if layout changes constantly, a minimap can create false orientation.

## Procedure

Start with the smallest structural encoding that preserves clusters, containers, major nodes, and empty space without attempting to render unreadable labels. The viewport rectangle or lens must remain visible against all graph regions and accurately match the main camera. Dragging the lens should pan continuously; clicking a distant region may jump but should preserve zoom unless the user requests fit. Search hits, errors, remote collaborators, or active runtime nodes can be marked only when the marker vocabulary remains sparse and prioritized. Provide an expand/overview action for dense graphs where the tiny minimap cannot answer orientation questions.

## Failure topology

Failures include a minimap that is merely a blurry screenshot, viewport rectangles too small to target, mismatch between minimap and main-camera coordinates, markers that overwhelm topology, click-to-jump unexpectedly changing zoom, and hidden minimaps that cover critical canvas controls. Another failure is implying stable spatial meaning when automatic layout is constantly moving nodes.

## Falsification

Reject if users cannot identify the current viewport at minimum supported zoom; if dragging the minimap can move to a different location than the lens indicates; if marker density obscures the underlying structure in representative worst cases; if touch users cannot manipulate the lens; or if layout churn makes the minimap stale relative to the main canvas.

## Output contract

Return a `graph-minimap-overviews-contract` with: structural representation; viewport-lens geometry; drag/click navigation semantics; zoom preservation rule; marker taxonomy and priority; expand/overview behavior; responsive placement; accessibility alternative; synchronization latency budget; and conditions under which the minimap is hidden or disabled.

## Handoffs

Use graph layout for coordinate truth, search/navigation for search markers and jump history, virtualization for large-graph summary data, and validation/collaboration owners for optional issue/presence markers. Generic pan/zoom supplies camera mechanics, not minimap semantics.