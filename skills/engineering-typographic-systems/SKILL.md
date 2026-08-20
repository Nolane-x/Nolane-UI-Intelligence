---
name: engineering-typographic-systems
description: Engineer a typographic system that coordinates hierarchy, rhythm, readability, numeric scanning, code, localization, zoom, and font behavior as one governed interface layer.
---

# Engineering typographic systems

Typography in software is an interaction system, not a set of font sizes. Use this skill when a product needs a coherent text architecture across navigation, forms, tables, dashboards, editorial content, dense tools, code, and responsive states.

## Decision ownership

Own the global typographic model: roles, scale relationships, line-height logic, weight and emphasis authority, text measures, numeric and code conventions, font fallback, and cross-platform invariants. Decide which properties are semantic roles and which remain component-local.

## Inputs and evidence

Collect actual text roles, font files and variable axes, language coverage, fallback metrics, platform rendering differences, zoom behavior, density modes, data-heavy screens, error/disclosure copy, and content length extremes. Inspect screenshots and computed styles; design files often hide browser fallback or runtime font substitution.

## Procedure

Define semantic roles from reading function rather than component names. Establish hierarchy through coordinated size, weight, spacing, color, and measure instead of relying on size alone. Model text rhythm across adjacent roles so headings, labels, body copy, helper text, numbers, and code feel related but remain distinguishable.

Separate display typography from high-frequency functional text. Create explicit conventions for numeric comparison, code, legal copy, and long-form reading. Test font loading and fallback early because metric shifts can invalidate layout assumptions.

Document what can adapt by density, viewport, platform, or locale and what should remain stable.

## Failure topology

A scale-only system produces mathematically neat sizes with poor hierarchy. Too many semantic roles create nearly indistinguishable styles and maintenance debt. Font swaps can change x-height, line breaks, and control height enough to break responsive layouts. Another failure is treating table numbers, code, and prose identically despite different scanning tasks.

## Falsification

Render representative screens with hierarchy labels removed and ask whether reading order remains obvious. Swap to fallback fonts, long translations, 200–400% zoom, and dense data. Compare line breaks and control heights. Remove one typographic role and see whether a genuine decision boundary disappears; if not, consolidate.

Audit pages for arbitrary one-off font values that bypass the system.

## Output contract

Produce a `typographic-systems-contract` containing semantic roles, scale and rhythm rules, emphasis authority, measure guidance, numeric/code conventions, fallback policy, responsive/density adaptations, localization/zoom constraints, and representative rendered verification.

## Handoffs

Use `designing-type-scale-relationships`, `designing-line-height-rhythm`, and `designing-heading-hierarchy` for core hierarchy mechanics; numeric specialists for data; `designing-font-loading-fallback-behavior` for runtime substitution; and `verifying-typography-under-zoom` for accessibility stress.