---
name: designing-multi-brand-theming
description: Structure multi-brand theming so brands express distinct identity without forking shared semantics, accessibility obligations, or component behavior.
---

# Designing multi-brand theming

Multi-brand systems fail when “brand” becomes a justification for duplicating the whole design system. Use this skill when several brands, sub-brands, white-label tenants, or acquired products must share foundations while preserving legitimately different identity decisions.

## Decision ownership

Own the boundary between shared semantics and brand-owned expression. Decide which token families may vary by brand, which component behaviors must remain invariant, how brand-specific assets are referenced, and how unsupported brand differences are escalated rather than smuggled into one-off overrides.

The skill does not invent each brand identity; it makes brand variation governable.

## Inputs and evidence

Inventory brand guidelines, actual product screens, token diffs, logos and imagery, typography licenses, contrast requirements, legal restrictions, component forks, and per-brand exceptions. Compare real implementations to identify differences that are semantic versus historical accident.

Map each divergence to a consumer need. A different primary hue may be brand-owned; a different focus indicator thickness may instead be an accessibility defect or platform requirement.

## Procedure

Define a common semantic layer first. Introduce brand mappings only where the same semantic role resolves differently. Keep brand assets, typography families, shape language, and optional expressive treatments in named domains so a brand switch does not alter unrelated behavior.

Create an exception process for genuinely brand-specific components. Require evidence that the need cannot be represented through shared component contracts before allowing a fork. For white-label systems, distinguish customer-configurable choices from internally curated brands; arbitrary customer values need stronger validation and fallback rules.

Test brand switching at representative component and page levels, including dark mode, high contrast, localization, print/export, and embedded surfaces.

## Failure topology

A full theme copy per brand causes drift and multiplies every bug fix. The opposite failure is over-normalization: forcing all brands into the same visual language until brand identity survives only as a logo and one color. Another failure occurs when a brand override changes semantic meaning, such as using the same token for decorative accent and critical action because both happen to share a hue.

Brand-specific typography can also break layout density, language coverage, or numeric alignment if treated as a cosmetic swap.

## Falsification

Diff resolved tokens across brands and classify every difference. Unexplained differences indicate drift; absence of expected identity differences indicates over-normalization. Introduce a new brand using the documented contract and measure how many component files require edits. If many components need bespoke conditions, the brand boundary is wrong.

Run accessibility and responsive checks independently for each brand. Shared behavior cannot be assumed merely because component source is shared.

## Output contract

Produce a `multi-brand-theming-contract` describing shared invariants, brand-owned domains, mapping strategy, asset and typography rules, exception/fork criteria, customer-configurability limits, validation and fallback behavior, and a cross-brand verification matrix for representative states and surfaces.

## Handoffs

Use `designing-theme-inheritance` for cascade authority, `designing-token-mode-architecture` for combination with dark/contrast/platform modes, `designing-component-api-governance` for brand-specific component capabilities, and `designing-cross-platform-component-parity` when brand expression differs by platform.