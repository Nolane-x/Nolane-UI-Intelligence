---
name: preventing-generic-ui
description: Use when a design risks looking templated, trend-driven, over-carded, over-decorated, repetitive, or indistinguishable from unrelated AI-generated interfaces.
---

# Preventing Generic UI

## Overview
This is a contextual anti-slop skill. It does **not** ban styles. It detects when a design choice has become detached from product meaning, hierarchy, or interaction.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use the product model, aesthetic direction, composition, and component semantics. A user-requested style is authoritative unless it conflicts with a higher-level requirement such as accessibility.

## The six-part test
Evaluate suspicious patterns as:

`pattern × context × intent × frequency × user impact × justification`

A pattern becomes a finding when its cost outweighs its function in this specific interface.

## Genericity signals
Investigate—not automatically fail—when you see:
- ubiquitous gradient/glow with no brand/product relationship
- bento/card grid as default page architecture
- nested rounded containers
- eyebrow + giant heading + subcopy + gradient CTA used mechanically
- icon-in-colored-square repeated for every feature
- random pills/badges used as decoration
- fake metrics or dashboard chrome in marketing surfaces
- same centered section formula repeated through long page
- excessive glass/blur/neon labeled “futuristic”
- generic AI copy: “supercharge,” “unlock,” “seamless,” “next-generation” without concrete product meaning
- overuse of tiny gray metadata and uppercase labels to simulate sophistication

## Contextual decision
For each signal ask:
1. What semantic/brand/task function does it serve?
2. Would removing it reduce comprehension, identity, emotional thesis, or interaction?
3. Is it repeated so often that it loses contrast?
4. Does it compete with higher-priority information?
5. Is it a product-specific choice or a category default?
6. What alternative structural solution exists?

If the pattern is justified, keep it. Do not redesign merely to prove originality.

## Anti-dogma
Never write rules such as “no gradients,” “no cards,” “serif fonts are premium,” “minimalism is best,” or “maximalism is unique.” These are style superstitions. NUI seeks **intentional specificity**, not a new house style.

## Similar-prompt counterfactual
Imagine three unrelated products receiving the same layout with only logo/color/copy changed. If the design remains equally plausible, identify which free axes were spent on defaults rather than subject-specific choices.

## Edit pass
When genericity is real, repair in this order:
1. strengthen product/content thesis
2. simplify unnecessary containment
3. clarify hierarchy
4. choose one signature with a reason
5. refine typography and rhythm
6. remove decorative repetition
7. only then add distinctive material/motion/imagery if needed

Do not solve genericity by adding more effects.

## Output: `anti-slop-findings`
Return `signals[] {pattern, context, function, cost, frequency, justification, verdict}`, `template_counterfactual`, `signature_strength`, `recommended_edits`, and `preserve_list`.

## Severity
Genericity is usually a craft finding, not a critical defect. Escalate only when the trope obscures product truth, misleads interaction, harms accessibility, or materially damages the requested brand/fidelity.

## V5 Global Accumulation and Counterfactual Gate
Evaluate genericity globally, not one component at a time. Inventory repeated mechanisms and judge **accumulation** using semantic necessity, **subject specificity**, frequency, information gain, emotional contribution, and **removal cost**. A hundred individually “justified” tiny mono labels can form one systemic trope. Include technical-sophistication slop (unearned coordinates, fake rulers, terminal atmosphere, hairline grids, SIGNAL/LIVE/SYS vocabulary, generic node/orbit diagrams) without hard-banning any style. Run a blind/counterfactual product-specificity test by masking nouns/branding and asking whether the same shell plausibly fits unrelated domains. At flagship+, timidity is also a finding when no memorable mechanism exists without a deliberate reason.

## V6 Genericity Falsification Engine
Create a **genericity fingerprint** from layout topology, typography roles, container geometry, palette, icon family, motion pattern, imagery, copy cadence, data visualization and empty/onboarding states. Genericity is a system-level resemblance, not the presence of one fashionable component.

Run **blind-product substitution**: remove brand/product names, replace domain nouns with another plausible SaaS/AI/finance product, and inspect whether the interface still feels equally appropriate. If yes, subject specificity is weak.

Run a **reference substitution test**: replace the current reference set with another fashionable collection from the same trend. If the chosen direction and mechanism rationale barely change, research is following style gravity instead of product truth.

For every signature candidate record **mechanism necessity**: what product meaning, interaction, information relationship or emotional invariant would be lost if it disappeared? Low-necessity repeated mechanisms are genericity debt even when attractive.

Detect **timidity failure** after removing clichés. An interface with no generic glow/cards/gradients can still be generic because it has no authored visual thesis. High ambition requires at least one memorable, product-specific relationship or a deliberately distinctive quietness proven against references.

### Falsification
Ask independent critics to infer product archetype and experiential intent from screenshots with text partially masked. If outputs fit many unrelated categories, specificity claims fail. Compare with a minimally styled semantic baseline; if the elaborate version adds no stronger identity, the added craft is decorative noise.

### Recovery
Do not randomly add unusual effects. Return to domain objects, competence rituals, spatial dramaturgy, signature mechanism, imagery/media role or typography character. Genericity is solved by authored causality, not novelty for its own sake.
