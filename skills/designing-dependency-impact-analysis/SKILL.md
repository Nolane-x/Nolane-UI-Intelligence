---
name: designing-dependency-impact-analysis
description: Own incident-time analysis of how failures may propagate across service dependencies, separating structural reachability, observed impact, hypothesis, and confidence.
---
# Designing Dependency Impact Analysis

## Decision ownership

Own impact reasoning across system dependencies during an incident. Decide how suspected propagation paths, confirmed affected dependents, blast-radius candidates, critical upstreams, and confidence are shown. Generic dependency graphs show structure; this skill binds structure to time-sensitive incident evidence without claiming causality merely from connectivity.

## Inputs and evidence

Require service topology, dependency direction, health/telemetry per entity, recent changes, request/traffic relationships if available, incident timeline, and evidence confidence. Identify missing or stale topology and dynamic dependencies that static maps may omit.

## Procedure

Start from confirmed affected entities and show structural upstream/downstream candidates separately from observed correlated impact. Mark paths as confirmed, suspected, or merely reachable. Allow focus by dependency type and request/region context. Use time alignment to test whether downstream symptoms follow plausible upstream changes, while displaying uncertainty. Blast-radius summaries should list affected, at-risk, and unknown segments instead of one inflated count. As evidence changes, preserve previous hypotheses and explain why confidence changed.

## Failure topology

Failures include treating every reachable node as impacted, causal arrows based only on topology, stale dependency maps presented as fact, circular dependencies producing infinite impact, and changing hypotheses with no history. Another failure is blast-radius numbers that mix confirmed customer impact with theoretical exposure.

## Falsification

Reject if structural reachability is visually indistinguishable from observed impact; if stale/missing topology has no cue; if a cycle cannot be handled; if confidence can change with no evidence link; if blast radius combines confirmed and possible entities; or if the interface implies causality where only temporal correlation exists.

## Output contract

Return a `dependency-impact-analysis-contract` containing: dependency direction; confirmed/suspected/reachable states; evidence/confidence links; topology freshness; cycle handling; segment/context filters; blast-radius categories; hypothesis history; and handoff to severity/mitigation. Include one stale-topology and one false-reachability example.

## Handoffs

Use dependency graph exploration for traversal mechanics, service health for observed state, hypothesis/evidence logs for causal reasoning, and severity declaration for impact-based coordination decisions.