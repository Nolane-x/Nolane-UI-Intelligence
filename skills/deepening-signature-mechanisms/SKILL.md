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

## V6 Signature Mechanism Depth
A signature is not a recurring decoration; it is a product-specific causal relationship. Write the **signature causal chain**: product truth → user meaning → interaction/information behavior → visual expression → emotional consequence. If any link is generic (“looks futuristic”), the mechanism is not deep enough.

Test **recognition-without-logo** across representative states. Could a knowledgeable observer identify the product family from the relationship between content, controls, motion, geometry and media with branding hidden? Recognition must not depend on copying another product's trade dress.

Run a **copyability test**: how easily could a competitor reproduce the signature by copying CSS tokens or one component? Deep signatures depend on domain data, interaction rituals, information architecture, procedural media, state transitions or unique composition logic, making surface imitation insufficient.

Retain the v5 **failure-if-removed** criterion but make it causal. Removing the signature should cause a describable loss in identity, comprehension, agency or emotional reward. If removal only makes the screen slightly less decorative, it is styling, not signature.

Watch **signature saturation**. A strong mechanism loses impact when applied to every card, title and button. Define where the signature is primary, supporting, absent, and transformed. Signature rhythm creates authorship without turning the product into a theme demo.

### Falsification
Substitute unrelated product content and see if the signature still feels equally appropriate. If yes, product specificity is weak. Replace the signature with a generic fashionable effect of similar visual intensity; if adequacy critics cannot tell which better serves the intent, the causal chain is unproven.

### Recovery
If the mechanism is shallow, deepen its semantic or interaction layer before adding visual complexity. If saturation is the problem, reduce frequency and concentrate it at moments of high product meaning. If recognition depends on borrowed upstream visual language, rebuild locally from product truths.
