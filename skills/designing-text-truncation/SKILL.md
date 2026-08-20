---
name: designing-text-truncation
description: Truncate text only when space constraints justify information loss, with discoverable full content, stable identity, and rules for critical or ambiguous strings.
---

# Designing text truncation

Ellipsis is an information-loss mechanism. Use this skill when labels, filenames, table cells, breadcrumbs, cards, or navigation items cannot always display full text and a deliberate truncation strategy is required.

## Decision ownership

Own eligibility for truncation, line limits, start/middle/end strategy, full-text access, interaction behavior, and exceptions for critical content. Decide which part of a string carries identity and therefore must remain visible.

## Inputs and evidence

Collect real string distributions, localization, filenames/paths, account identifiers, duplicate-prefix cases, mobile widths, table scanning tasks, and accessibility names. Identify strings where the beginning or end carries discriminating information.

## Procedure

Prefer wrapping or flexible layout before truncation when content is essential. Use end truncation for ordinary prose-like labels, middle truncation for paths or identifiers where both ends matter, and avoid truncating critical error, legal, financial, or confirmation content without a reliable expansion path.

Expose full text through a mechanism usable by keyboard, touch, and assistive technology—not hover tooltip alone. Keep accessible names aligned with full content while avoiding repetitive announcements.

Define whether truncation is responsive and how line clamping changes across states.

## Failure topology

Identical prefixes can make several truncated items indistinguishable. Hover-only disclosure excludes touch and keyboard. Multi-line clamping may cut content without an ellipsis in some engines. Another failure is truncating input values users are actively editing, hiding the caret or relevant suffix.

## Falsification

Test longest and most similar real strings at narrow widths. Use keyboard, touch, screen reader, zoom, and copy/paste. Verify users can distinguish duplicates and retrieve full content. Test bidirectional text and filenames with long extensions.

If truncated items cannot be uniquely identified in a common workflow, the strategy fails.

## Output contract

Produce a `text-truncation-contract` specifying eligible content, line/width constraints, truncation direction, full-content access, accessibility behavior, critical-content exemptions, and collision tests using representative strings.

## Handoffs

Use `designing-multiline-labels` when wrapping is allowed, `designing-rag-and-line-break-quality` for general wrapping, `designing-responsive-priority-collapse` when whole elements should move instead, and `designing-file-browsing` for path-specific semantics.