---
name: designing-large-graph-virtualization
description: Own interaction-preserving level-of-detail and virtualization policies for graphs too large to render every node, edge, label, and control simultaneously.
---
# Designing Large Graph Virtualization

## Decision ownership

Own the user-facing consequences of graph culling, clustering, progressive rendering, and level-of-detail. Decide which entities remain interactive when off-screen or aggregated, how selection/focus survive virtualization, when labels/ports/edges simplify, how asynchronous expansion communicates progress, and what accessible non-visual representation exists. The rendering engine is implementation detail; interaction continuity is this owner's responsibility.

## Inputs and evidence

Require node/edge scale distributions, worst-case graph size, typical viewport density, renderer limits, layout cost, search/index architecture, interaction latency targets, accessibility requirements, and which node/edge states are safety-critical or must never be visually suppressed. Measure realistic pan/zoom and selection workloads rather than only initial render time.

## Procedure

Define level-of-detail tiers by semantic usefulness: overview aggregates and cluster boundaries; mid-level nodes and major relationships; detail-level labels, ports, badges, and handles. Never discard identity when an entity leaves the render set; selection, focus, search, and history must refer to stable model IDs. Progressive expansion should show that more structure exists and avoid representing partial data as complete. High-priority errors or active states may pierce aggregation with markers. Edge culling should retain enough boundary summaries to prevent false disconnection. Provide a table/list or structured accessibility view that is not constrained by canvas rendering.

## Failure topology

Failures include selected nodes disappearing with no indication when zoom changes, aggregates whose counts lag behind the model, hidden edges making connected components look disconnected, hover-dependent controls disappearing before the pointer reaches them, keyboard focus jumping when items unmount, and asynchronous expansion changing layout underneath an active drag. Performance also fails if virtualization bookkeeping costs more than rendering at common sizes.

## Falsification

Reject if selection identity is lost when an item unmounts; if a search result exists in the model but cannot be revealed because it is virtualized; if critical error state can be fully hidden inside an apparently neutral cluster; if keyboard traversal depends on rendered DOM order only; if partial loading is indistinguishable from a complete graph; or if pan/zoom misses the defined interaction latency budget in worst-case samples.

## Output contract

Return a `large-graph-virtualization-contract` containing: size thresholds; level-of-detail tiers; aggregation semantics; stable identity requirements; selection/focus persistence; edge-culling policy; critical-state piercing; progressive-load states; search reveal behavior; accessibility alternative; latency budgets; and fallback when the graph exceeds planned scale. Include a worst-case density specimen.

## Handoffs

Coordinate with minimap/overview for global orientation, graph search/navigation for off-render lookup, node/connector owners for detail-level controls, and layout/routing implementations for progressive geometry. Generic list virtualization is not sufficient because graph connectivity must remain semantically truthful.