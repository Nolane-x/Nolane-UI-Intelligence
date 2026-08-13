---
name: directing-iconography-and-imagery
description: Use when icons, illustrations, photography, product renders, avatars, diagrams, generated images, or other visual assets materially affect meaning, brand, navigation, or interface fidelity.
---

# Directing Iconography and Imagery

## Overview
Visual assets are language. Use them to clarify meaning, establish subject-specific character, or carry content—never as filler for empty composition.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use aesthetic direction, component semantics, content model, target fidelity, and brand constraints.

## Icon system
Define:
- family/style: outline, filled, duotone, custom, symbolic
- stroke/fill weight
- corner character
- optical size grid
- baseline/alignment
- default/active/disabled/selected treatment
- container use
- directionality/RTL mirroring rules

Choose metaphors by user recognition in context. A visually similar icon is not equivalent if it changes meaning. For uncommon actions, pair icon with text until the metaphor is learned or persistent space truly forbids it.

Avoid mixing unrelated icon libraries unless you normalize geometry/stroke or the distinction carries meaning.

## Decorative icons
If an icon merely decorates a heading that already says the same thing, test removal. Repeated icon-in-colored-square feature grids are often generic because the icon adds no new information.

## Imagery roles
Classify each image as:
- content/evidence
- product demonstration
- identity/brand
- atmosphere
- explanation/diagram
- avatar/actor identity

The role determines crop, alt/semantic handling, priority, loading, and responsive behavior.

## Subject specificity
When generating/selecting imagery, derive motifs from the product’s world. Avoid generic abstract 3D blobs, glowing orbs, random dashboards, or synthetic people when they do not communicate product truth.

## Media framing
Define aspect ratios, crop/focal rules, edge treatment, captioning, background compatibility, and repeated frame geometry. Responsive crops must preserve the meaningful subject, not simply center-crop.

## Product screenshots/renders
Do not distort or fake critical product UI to make marketing imagery cleaner if fidelity/trust matters. Distinguish illustrative product concepts from actual screenshots.

## Accessibility
Decorative assets should not add semantic noise. Informative assets need an equivalent text/semantic path appropriate to their content. Do not use icon color alone to encode status.

## Output: `asset-direction-contract`
Return `icon_system`, `icon_inventory`, `metaphor_rules`, `imagery_roles`, `asset_inventory`, `generation_guidance`, `framing_rules`, `responsive_crop`, `semantic_treatment`, and `fidelity_constraints`.

## Common failures
- Generic sparkle/wand icon used for every AI feature.
- Mismatched icon stroke weights beside each other.
- Stock photo chosen solely to fill the right side of a hero.
- Generated image includes text that must remain editable/code-native.

## V5 Media as Product-Specific Evidence
At **high visual ambition**, media role is not automatically optional decoration. Consider procedural/domain-native assets—scientific fields, causal/lineage maps, model or memory landscapes, simulation imagery, dataset morphology, compute topology, temporal traces, uncertainty volumes, editorial evidence, material photography/illustration where appropriate. `procedural` does not mean random sci-fi texture: every media role must declare identity, explanation, evidence, atmosphere or product demonstration value. A text/border-only shell must justify why richer media would add no product-specific value.

## V6 Iconography, Symbol and Image Direction
Define a **symbol grammar** before selecting individual icons: stroke/fill philosophy, weight, corner character, perspective, grid, optical size, bounding-box usage, default detail, active/selected treatment and relationship to typography. Mixed families require an explicit normalization plan.

Inspect the source family’s **optical grid** and construction conventions. Do not assume identical SVG dimensions create identical apparent size; arrows, circles, dense pictograms and sparse strokes need optical correction. Define alignment with text baseline and control boxes.

Run a **metaphor collision** audit: the same symbol must not mean conflicting actions across the product, and two similar symbols should not encode materially different actions without labels. Domain-native concepts often need custom or combined symbols rather than forcing a generic icon catalog.

Check **cultural interpretation** and localization. Gestures, animals, flags, mailboxes, checkmarks, hand signs, directionality and metaphors can change meaning. RTL may mirror directional icons while semantic objects remain unmirrored.

Maintain **asset provenance** for icons, photography, illustrations, generated imagery and third-party art. Record source, license/usage boundary, transformations and whether the asset carries brand/trade-dress risk. AI-generated media requires its own provenance/policy where relevant.

Imagery has a product role: explain, orient, authenticate, evoke, demonstrate, create atmosphere, or carry primary content. Decorative imagery competes for attention and performance budget; justify its position in the visual hierarchy.

### Falsification
Hide labels and test whether repeated high-frequency icons remain distinguishable; then restore labels and check whether the icon is adding value or noise. Replace a stock/third-party image with a neutral placeholder; if product identity disappears, the visual system may be outsourcing authorship to assets.

### Recovery
When an icon family lacks critical concepts, create a compatible local extension or choose another family rather than mixing arbitrary glyphs. When imagery overwhelms tasks, reduce salience/crop/frequency or move it to experiential moments that deserve the attention.
