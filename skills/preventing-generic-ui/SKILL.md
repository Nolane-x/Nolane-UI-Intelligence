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
