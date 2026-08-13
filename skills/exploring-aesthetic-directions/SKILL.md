---
name: exploring-aesthetic-directions
description: Use when a UI has meaningful visual freedom and the agent must discover a distinctive art direction rather than default to a familiar template or blindly imitate a category aesthetic.
---

# Exploring Aesthetic Directions

## Overview
Aesthetic exploration turns product meaning into visual hypotheses. It is not a style lottery and not a prompt to maximize novelty.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume product intent, user/task model, information architecture, brand/reference constraints, and novelty tolerance. If an accepted authoritative design already fixes the visual direction, record that and do not generate alternatives merely for ceremony.

## Build the aesthetic search space
Define axes before proposing directions:
- **semantic source:** objects, materials, tools, environments, rituals, history, data shapes, or cultural cues native to the subject
- **emotional target:** calm, rigorous, energetic, intimate, authoritative, playful, urgent, archival, tactile, cinematic, etc.
- **trust posture:** invisible/neutral, transparent/technical, warm/human, premium/controlled, operational/reassuring
- **density:** sparse presentation ↔ information-dense operation
- **formal character:** geometric ↔ organic, editorial ↔ utilitarian, soft ↔ precise, quiet ↔ expressive
- **novelty budget:** familiar conventions that should remain vs axes where the product can take a real risk
- **media character:** photography, illustration, diagrams, code/data, texture/material, 3D, no imagery
- **motion character:** static, functional, choreographed, ambient

Do not choose an axis value because it is currently fashionable. Tie it to product/user evidence.

## Generate structurally different hypotheses
When exploration is valuable, create 2–4 candidates that differ in **composition logic, type character, density, surface/material treatment, media role, and signature behavior**. Recoloring one layout is not divergence.

For each candidate state:
- thesis: what makes this direction appropriate to this product
- signature: one memorable element or interaction that embodies the thesis
- quiet system: what remains restrained so the signature has contrast
- typography character
- palette behavior, not only hex values
- layout/composition principle
- image/icon strategy
- motion posture
- risks: what could become gimmicky, inaccessible, slow, or distracting
- rejection conditions

## Distinctiveness test
Ask: if product name, logo, and copy were removed, would this direction still plausibly belong to dozens of unrelated AI/SaaS sites? If yes, find a more subject-specific semantic source or composition.

A direction can still be minimal or conventionally styled; distinctiveness may come from typography, rhythm, information form, image treatment, or a small signature rather than loud decoration.

## Novelty budget
Spend visual risk where it increases recognition, emotion, or comprehension. Keep critical controls and high-frequency task mechanics familiar unless the interaction benefit justifies novelty. An interface can be visually original while behavior stays predictable.

## Selection
Score candidates against the actual contract:
- product truth
- user/task fit
- hierarchy potential
- brand/subject specificity
- implementation feasibility
- accessibility/inclusive risk
- responsive durability
- memorability

Do not average candidates into a bland hybrid. Choose the strongest thesis and deliberately import only compatible details from another direction.

## Output: `visual-direction-set`
Return `search_axes`, `candidates[]`, `comparison`, `selected_direction`, `selection_rationale`, `frozen_axes`, `flexible_axes`, and `known_risks`.

## Common failures
- Defaulting to purple/blue AI gradients, dark neon dashboards, cream editorial serif pages, or bento grids without product-specific justification.
- Making every region “signature,” eliminating hierarchy.
- Confusing maximalism with originality or minimalism with taste.
- Producing directions that differ only by palette.
- Inventing fake content/metrics to make the composition impressive.

## V5 Divergence Artifact Gate
For flagship+ ambition with high visual freedom, prose alternatives are insufficient. Produce **at least three** materially different **rendered candidates** when the runtime can render. They must be **materially different** in several of: composition logic, typography character, density/rhythm, surface/material behavior, media/visualization role, and signature mechanism; recoloring is not divergence. Bind accepted reference mechanisms to each candidate and compare the selected direction against both a reference frontier and at least one alternative. Route each claimed signature through `deepening-signature-mechanisms`.
