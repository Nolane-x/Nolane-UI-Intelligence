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

## V6 Directional Divergence Protocol
For high visual freedom, divergence must happen at the level of causal mechanisms rather than palette swaps. Require **mechanism-level divergence** across composition, typographic voice, material/surface logic, information density, imagery/icon grammar, motion behavior, and interaction emphasis. Two candidates with the same card grid and hierarchy but different gradients are one direction.

Use a **composition silhouette test** by reducing candidates to large masses, voids, axes, dominant alignments, and focal regions. Their silhouettes should demonstrate genuinely different spatial theses when the brief permits. Evaluate **material-language divergence** separately: flat/ink-like, tactile/layered, luminous/spatial, editorial, diagrammatic, or other surface logic must change boundary/depth behavior, not just shadow strength.

Force **typography-personality contrast** where type is expressive: compare at least one direction whose voice comes from proportion, rhythm, or family behavior rather than the same neutral grotesk scaled differently. Watch for a **direction-convergence alarm** during refinement: if independent candidates accumulate the same radius, cyan accent, dark panes, microtype, glass, or motion grammar, stop and re-diverge before selection.

### Falsification
Grayscale candidates, strip brand names, normalize copy, and compare silhouettes and interaction states. If an independent critic cannot state the distinct thesis/mechanism of each, divergence is false.

### Recovery
Return to experiential intent and reference contradictions, mutate one or more structural mechanisms, and regenerate candidates from different constraints. Do not manufacture variety with decoration.

## V9 Comparative Taste Discrimination
Aesthetic selection must distinguish **correct** from **refined**. A candidate can satisfy hierarchy, accessibility, brand and layout rules while still reading as cheap-looking, overdesigned, generically “AI,” visually timid, plasticky, template-derived, insufficiently premium, or insufficiently editorial for the intended product. Taste is therefore a comparative judgment layer, not another compliance checklist and not a single opaque score.

For flagship or materially aesthetic work, compare at least two rendered candidates or two materially different refinement states on explicit dimensions: focal authority, compositional tension, negative-space quality, density modulation, typographic character, optical alignment, material restraint, border/elevation calibration, visual rhythm, signature-to-quiet ratio, domain fit, audience fit, motion posture and perceived production maturity. Name which candidate is stronger **per dimension**, why, and what rendered evidence supports the distinction. If no candidate clearly wins, return `tie` or `re-diverge`; never invent confidence to close the task.

Use qualitative discriminators carefully. **Premium** should mean controlled hierarchy, material precision, intentional detail, confidence and absence of accidental residue—not simply dark backgrounds, thin fonts or more whitespace. **Editorial** should mean deliberate typography, pacing, image/text relationship and compositional authorship—not automatically serif display type. **Cheap-looking** is a diagnostic shorthand that must be decomposed into observable causes such as indiscriminate borders, stock gradients, uniform card radii, weak type metrics, default browser chrome, noisy shadows, decorative icon excess, over-rounded controls or undifferentiated density.

Calibrate against the curated benchmark gallery at the **mechanism** level. A reference can raise the perceptual threshold for density, typography, workspace organization, motion restraint or material precision, but cannot donate its exact expression. Compare more than one relevant reference when possible and state why a mechanism transfers to this product's domain/audience. If the candidate becomes recognizable as a specific reference rather than the product itself, taste has become imitation.

Taste never overrides hard product truth, security, accessibility, platform behavior or functional closure. A visually subtler treatment loses when it makes focus, state, consequence, selection, error or permission harder to perceive. The high bar is “more refined while preserving truth,” not “more beautiful at any cost.”

### V9 Falsification
Render two structurally valid candidates, remove logos/brand names, and ask an independent critic to compare them without knowing which one the generator preferred. If the critic can only repeat rule compliance or assign unexplained numeric scores, taste discrimination has not occurred. Also compare a deliberately polished-but-generic candidate against a more product-native one; if the court automatically chooses polish, it is rewarding fashion over fit.

### V9 Recovery
Identify the smallest causal differences driving the weaker perception—type metrics, spacing rhythm, material boundary, density distribution, focal competition, signature excess, residue or domain mismatch—and revise those mechanisms. Re-render and compare again. Do not “premiumize” by stacking decoration, glass, gradients, blur or animation.

## V10 Comparative Taste Identification
`H-TASTE-COMPARATIVE` is a causal hypothesis about selection behavior, not a declaration that NUI possesses objective taste. The intended effect is that **pairwise blinded evidence** makes a model more likely to prefer the candidate whose visible hierarchy, typography, material restraint, rhythm, domain fit and subject-specific authorship are stronger, while rejecting polished genericness and hard-constraint regressions.

The treatment must preserve at least two renderable candidates through the judgment stage. Generator labels, self-scores, reference names and preferred-direction rationale are stripped before pairwise judging. Each comparison records a named dimension, evidence references, observable cause and a `LEFT | RIGHT | TIE | UNJUDGABLE` verdict. `tie` is a valid result; forcing a winner creates false precision. A strong overall preference may emerge from several dimensions, but no scalar beauty score substitutes for the dimension ledger.

The mutation `taste-scalar-self-score` allows the generator to select by an opaque self-assigned score. The `taste-court` ablation removes comparative discrimination. On visual-taste tasks, full NUI should improve blinded preference and causal specificity relative to those controls. It must not win by violating accessibility, product truth, platform behavior or task clarity; those remain non-compensatory blockers.

### V10 reference control
Reference exposure can itself bias judgment. Record whether a reference was used in generation, evaluation, or both. When feasible, the judge should receive product-local artifacts and rubric dimensions without knowing the source brand that inspired a mechanism. If a candidate wins mainly because it resembles a prestigious reference, run the logo/name/trade-dress blindness test and compare a product-native countercandidate.

### V10 falsification topology
The hypothesis is not identified when:
- full NUI and `taste-court` ablation receive equivalent blinded preference;
- a non-semantic placebo moves preference as much as the semantic mutation;
- judges repeatedly prefer generic polish over subject-linked authorship while product truth is equal;
- win direction depends entirely on one judge lineage;
- full NUI raises visual preference but creates hard accessibility or functional regressions;
- only development tasks tuned during skill writing show an effect.

Artifact quality and efficacy are separate. A beautiful page demonstrates possibility, not causal contribution. Until real matched treatment runs survive ablation, holdout and judge-blindness gates, the repository may say the taste protocol exists and is testable, but its efficacy claim remains `STRUCTURAL_ONLY`.
