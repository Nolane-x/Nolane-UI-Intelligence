---
name: deepening-signature-mechanisms
description: Use when an aesthetic direction claims a signature element or interaction and NUI must determine whether it is product-specific and deep enough to justify that claim.
---

# Deepening Signature Mechanisms

## Parent Contract
**Required parent:** `exploring-aesthetic-directions`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own depth of the signature mechanism, not the entire art direction. Evaluate semantic_depth, interaction_depth, visual_depth, information_gain, product_specificity, reusability, memorability, and failure_if_removed.

## Product Truth
A radial diagram, topology, orbit, glow, or unusual layout can be memorable while carrying almost no product meaning. ‘Has a signature’ is weaker than ‘the signature is semantically and interactively indispensable’.

## Decision Model
Trace the mechanism to domain truth. Ask what it reveals, what the user can do through it, what relationships it encodes, how it changes across states/time, and what would be lost if removed. A high visual_depth score cannot compensate for near-zero semantic_depth and information_gain at exceptional ambition. Reusability is not automatically bad, but very high reusability plus low product_specificity is a warning. For diagrams, coordinate with encoding provenance so decorative positions cannot masquerade as science.

## Evidence
Produce the eight-dimension contract with concrete evidence, required level, and removal counterfactual. For high ambition, a shallow signature is BLOCKED or returned for redesign.

## Output Contract: `signature-depth-contract`
Return the canonical `signature-depth-contract` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
One memorable ornament treated as product identity; fixed radial nodes presented as topology; novelty without user value; forcing all screens to repeat the signature; declaring failure_if_removed based only on aesthetics.
