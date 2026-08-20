---
name: designing-topology-map-interfaces
description: Own infrastructure and system topology maps where nodes, links, tiers, regions, and live health overlays must preserve structural truth under changing operational state.
---
# Designing Topology Map Interfaces

## Decision ownership

Own topology-oriented graph presentation for systems whose relationships describe physical, logical, service, network, or deployment structure. Decide tier/region grouping, live status overlays, link-state encoding, topology drift, discovery confidence, and how users move between overview and a local neighborhood. This is not geographic mapping unless coordinates themselves are spatially meaningful.

## Inputs and evidence

Collect topology source(s), discovery interval, node/link types, region/tier metadata, health and capacity signals, expected churn, cardinality, whether links are directional, and common operator questions. Identify ambiguity between "unknown", "disconnected", "healthy", and "not observed" before choosing status visuals.

## Procedure

Choose grouping around system structure—service tier, cluster, region, rack, namespace—rather than forcing every entity onto one flat canvas. Keep structural relationship and live health visually separable so a red status does not appear to mean a different edge type. Show freshness and discovery confidence for inferred topology. When new nodes or links appear, avoid destabilizing the entire mental map; mark drift and allow operators to compare before/after topology. Focus mode should retain upstream/downstream context and offer a stable route back to the overview. At high density, aggregate with explicit counts/types rather than decorative blobs.

## Failure topology

Failures include status colors overwriting structural meaning, unknown nodes appearing healthy by default, layout churn on each discovery poll, aggregates that hide one critical unhealthy member, directional links losing arrows at low zoom, and topology snapshots presented without freshness. Another failure is conflating topology with dependency impact so operators infer causal failure from mere connectivity.

## Falsification

Reject if operators cannot distinguish missing telemetry from healthy state; if the same topology snapshot rearranges materially on every refresh; if an aggregate can look healthy while containing a critical failure with no cue; if newly discovered links are impossible to identify; or if structural groups collapse such that external dependencies vanish.

## Output contract

Return a `topology-map-interfaces-contract` with: topology entity/link taxonomy; grouping hierarchy; health/status overlay rules; freshness/confidence treatment; drift/change cues; aggregation policy; focus/overview navigation; link direction behavior; unknown-state representation; and critical-member propagation. Include a topology-change scenario and a partially observed scenario.

## Handoffs

Use dependency exploration for causal/upstream-downstream questions, graph virtualization for scale, graph diff/history for snapshot comparison, and security attack-path visualization for adversarial reachability. Geospatial map owners apply only when geographic coordinates are part of the domain truth.