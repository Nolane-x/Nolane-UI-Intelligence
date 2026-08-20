---
name: designing-optical-heading-balance
description: Tune heading width, wrapping, weight, tracking, and line breaks so prominent text feels balanced without distorting meaning or accessibility.
---

# Designing optical heading balance

Large headings amplify awkward line breaks, uneven rags, and isolated short words. Use this skill for hero titles, page headlines, modal titles, editorial headings, and major section labels where optical composition materially affects perceived quality.

## Decision ownership

Own heading-specific optical adjustments: maximum measure, balanced wrapping strategy, tracking, weight, line-height, and manual-break policy. Decide where author control is acceptable and where runtime content must remain fully automatic.

## Inputs and evidence

Collect real headings across languages, dynamic/user-generated titles, variable-font capabilities, supported widths, localization, SEO/CMS constraints, and line-break engine behavior. Identify headings whose design currently depends on hardcoded `<br>` tags.

## Procedure

Start with measure and font metrics before inserting manual breaks. Use balanced wrapping where supported and stable, but verify it does not create overly narrow lines. Tune tracking conservatively for large display text and test variable font optical-size axes where available.

Permit editorial line breaks only for controlled content with explicit authoring support; dynamic strings should not inherit fixed break positions. Keep semantic text intact for assistive technology even when visual balancing uses CSS.

Evaluate multi-line titles as shapes while preserving natural reading sequence.

## Failure topology

Hardcoded line breaks fail under translation and responsive widths. Aggressive negative tracking harms readability and can clip glyphs. Automatic balancing may produce a first line that is much shorter than the second or cause unexpected layout height changes.

Aesthetic editing can also alter wording or punctuation solely to fit a layout, creating content-quality problems.

## Falsification

Render a corpus of short, medium, long, and localized headings across width ranges. Disable balancing and compare whether manual constraints are still reasonable. Test browser/font fallback and zoom. Inspect headings containing long names, URLs, and unbreakable tokens.

If a heading only looks acceptable at one exact viewport, the optical strategy is too brittle.

## Output contract

Produce an `optical-heading-balance-contract` defining measure, wrap strategy, tracking/weight guidance, manual-break eligibility, localization behavior, fallback rules, and visual test examples across widths and languages.

## Handoffs

Use `designing-heading-hierarchy` for semantic structure, `designing-rag-and-line-break-quality` for general wrapping quality, `designing-variable-font-controls` for axis usage, and `designing-content-driven-breakpoints` if heading pressure changes layout.