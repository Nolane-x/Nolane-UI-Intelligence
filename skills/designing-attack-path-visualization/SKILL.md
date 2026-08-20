---
name: designing-attack-path-visualization
description: Use when analysts need to understand plausible privilege, trust, identity, network, or configuration paths an attacker could traverse and must distinguish observed movement from hypothetical reachability.
---
# Designing Attack Path Visualization

## Decision ownership

Own the representation of security attack paths as typed, evidence-bearing graph relationships. Decide how observed steps, inferred reachability, configuration-derived possibilities, blocked edges, prerequisites, privilege transitions, and remediation effects are distinguished. This faculty does not compute graph reachability itself and does not own generic node placement. Its job is to stop a visually compelling path from overstating what is actually known.

## Inputs and evidence

Require entity types, privilege and trust relationships, network reachability, identity membership, credential exposure, vulnerability prerequisites, control states, path-generation method, edge confidence, observation timestamps, and remediation simulations. Collect examples containing multiple alternative paths, stale relationships, loops, shared service accounts, conditional access, missing telemetry, and paths that exist structurally but are not known to have been exercised. Record whether a relationship comes from configuration, telemetry, analyst assertion, or threat-model inference.

## Procedure

Define a small path grammar before drawing. Every edge should answer: what capability moves from source to target, what prerequisite enables it, what evidence supports it, and whether it is observed or merely possible. Encode privilege change and trust boundary crossings more strongly than geometric distance. Support path comparison by risk, length, confidence, exposed critical asset, or remediation cost without reducing everything to one score. Let analysts collapse low-value intermediate nodes while preserving path semantics. When simulating a remediation, show which paths disappear, which alternatives remain, and which assumptions are unchanged. Preserve time validity because membership, credentials, routes, and vulnerabilities expire.

## Failure topology

- A shortest path is presented as the most likely attack path without behavioral evidence.
- Configuration-derived reachability looks identical to observed lateral movement.
- Edge color is the only cue for confidence or path type.
- Removing one relationship visually “fixes” the graph while equivalent alternative paths remain hidden.
- Stale group membership creates phantom privilege escalation routes.
- Graph layout suggests direction or importance unrelated to edge semantics.
- Dense paths become an unreadable hairball and analysts cannot inspect prerequisites.

## Falsification

Use a graph with one observed chain, two configuration-only alternatives, a stale privilege edge, a blocked network route, and a remediation that closes only one of several paths. The design fails if an analyst cannot tell observed from hypothetical movement, cannot inspect a path's prerequisites, or incorrectly concludes that remediation eliminated exposure when an alternate path survives.

## Output contract

Return `attack-path-visualization-contract` with node/edge taxonomy, observed-versus-possible encoding, prerequisite and confidence display, temporal validity, path-ranking controls, alternative-path treatment, remediation simulation behavior, accessibility equivalents, and path falsification scenarios.

## Handoffs

Use `designing-security-entity-investigation` for entity truth, `designing-security-event-correlation` for inferred relationships, and generic graph faculties for routing, zoom, minimap, or virtualization. Vulnerability-specific remediation priority routes to `designing-vulnerability-prioritization`; privilege-focused review routes to `designing-privilege-escalation-review`.