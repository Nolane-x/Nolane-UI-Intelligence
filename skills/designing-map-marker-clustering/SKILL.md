---
name: designing-map-marker-clustering
description: Use when many point features overlap at a map scale and the interface must aggregate them without implying false geography, hiding category differences or making cluster expansion unpredictable.
---

# Designing Map Marker Clustering

## Parent Contract
**Required parent:** `designing-geospatial-interfaces`.

This faculty owns visual/interaction aggregation of dense point features. It does not define server-side spatial indexing or general map zoom behavior.

## Decision Boundary
Clustering solves **screen-space collision at a given scale**, not a semantic claim that points belong to one real-world group. Preserve the underlying member IDs and distinguish statistical/administrative aggregation from purely visual clustering. If counts, category composition or severity are shown, calculate them from actual members rather than marker styles.

Choose clustering radius and level transition based on point density, marker size and task. Stable clustering is preferable to a cluster graph that completely reshuffles with tiny pans. Users should understand what activation does: zoom to member extent, spiderfy nearby coincident points, open a summary, or another explicit behavior. A cluster click should not arbitrarily select one hidden member.

Cluster markers need more than a count when composition changes decisions. A cluster of 50 low-priority sites and one critical alert may need a severity cue; however, aggregating severity requires a declared rule. Avoid averaging away rare high-impact states.

As zoom increases, preserve continuity between cluster and member appearance. Animation can help spatial orientation but must not delay access. Identical coordinates may never separate by zoom; provide spiderfy/list/detail or jitter-free offset strategy rather than an infinite zoom trap.

## Failure Topology
- Cluster count visually looks like a regional statistic rather than “markers currently grouped on screen.”
- Tiny pan changes cluster membership radically and selected context disappears.
- Critical item is hidden inside a neutral cluster average.
- Clicking a cluster zooms repeatedly but coincident points never become selectable.
- Cluster activation has no keyboard/list equivalent.
- Cluster count includes filtered-out points because aggregation state is stale.

## Falsification and Recovery
Falsify with uniform/dense hotspots, coincident coordinates, filtered categories, rare severe items, rapid pan/zoom and keyboard/list interaction. Compare cluster membership to visible filter/query scope.

Recover by stabilizing screen-space clustering, exposing composition/critical summaries, defining activation explicitly, handling coincident points with alternate expansion and recomputing clusters from current scope.

## Output Contract
Return `map-marker-clustering-contract` with clustering purpose/radius, member identity, composition aggregation, stability policy, activation/expansion behavior, coincident-point fallback, selection continuity, accessibility alternative and membership tests.