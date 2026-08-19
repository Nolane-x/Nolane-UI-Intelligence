---
name: designing-route-comparison
description: Use when users compare alternative routes and the interface must expose time, distance, cost, constraints, uncertainty, segment differences and route identity without ranking one option solely by visual prominence.
---

# Designing Route Comparison

## Parent Contract
**Required parent:** `designing-geospatial-interfaces`.

This faculty owns comparison interaction for route alternatives. Route computation, traffic prediction, safety constraints and legal navigation rules remain external authorities.

## Decision Boundary
Treat each route as a stable alternative with origin/destination, waypoints, mode, departure/arrival assumptions, total duration/distance/cost, relevant restrictions and route geometry. Do not infer that the visually shortest line is fastest or safest.

Expose the dimensions that matter for the task. Driving may compare duration, tolls, traffic and road restrictions; transit may compare transfers, walking, fares and service reliability; logistics may need vehicle restrictions, delivery windows and route feasibility. Use authoritative route metadata and avoid generic “Best” labels unless the ranking criterion is declared.

Highlight differences, not just totals. Users benefit from knowing that Route B adds one toll segment, Route C avoids a closure, or two routes share 80% of the path. Selecting an alternative should synchronize map geometry and textual/step summary while keeping other options faintly comparable when useful.

Uncertainty/freshness matters. Traffic ETA or transit arrival is predictive; show update time/range where the routing source supports it. A route recalculation after missed turn or traffic change should identify whether the chosen route changed rather than silently replacing geometry under an existing label.

Accessibility requires a structured comparison independent of map color. Route colors must remain distinguishable with labels/patterns and list/table summaries.

## Failure Topology
- Primary blue route is interpreted as recommended but ranking criterion is hidden.
- Two routes differ mainly in tolls, yet only time/distance are shown.
- Recalculation replaces Route A with a different path while history/selection still calls it the same alternative.
- Traffic ETA is displayed as exact minutes with no freshness/uncertainty context.
- Color is the only way to distinguish overlapping routes.
- Map comparison is excellent but screen-reader users get only one selected route’s steps.

## Falsification and Recovery
Falsify with near-equal routes, toll/avoid constraints, overlapping geometry, prediction updates, route recalculation, different modes and nonvisual comparison. Verify selected route ID and comparison metrics against routing-engine response.

Recover by naming ranking criteria, surfacing task-relevant differences, versioning/reidentifying recalculated alternatives, preserving structured summaries and treating predictive time as bounded evidence.

## Output Contract
Return `route-comparison-contract` with alternative identities, ranking criteria, comparison dimensions, segment-difference presentation, selection/map synchronization, predictive freshness, recalculation identity, accessible comparison and route-response parity tests.