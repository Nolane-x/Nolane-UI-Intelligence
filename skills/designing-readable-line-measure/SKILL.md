---
name: designing-readable-line-measure
description: Use when prose, labels, or dense reading text needs an evidence-backed line-length policy across font metrics, viewport/container changes, text scaling, and content types.
---

# Designing Readable Line Measure

## Reading Width Is a Typographic Decision
A container can have spare horizontal space and still be too wide for comfortable reading. This skill owns the line-measure contract for sustained or task-critical text: which content types require bounded measure, how metrics influence that bound, and how the measure adapts without forcing arbitrary viewport constants.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent chooses typography and hierarchy. This specialist constrains the horizontal reading span produced by those choices.

## Measure Model
Describe measure in characters/glyph advances and observed reading behavior rather than a single pixel number copied across fonts. Distinguish body prose, compact help, code-like text, form guidance, legal disclosures, and scanning tables. A comfortable narrative measure may be inappropriate for a short command label or log stream.

Responsive rules should allow margins or multi-column structure to absorb extra width before prose stretches indefinitely. At narrow widths, maintain readable size and permit wrapping rather than shrinking text merely to preserve a target character count.

## Constraints and Invariants
Line measure must coexist with user text scaling, localization, nested containers, and zoom. It cannot create horizontal scrolling for ordinary prose. Adjacent images or side notes should not squeeze reading text below a usable width without a composition change. Headings may intentionally exceed body measure only when hierarchy and wrapping remain clear.

## Evidence
Evidence includes real paragraphs at representative widths, text scaling, several font/fallback states, long words/URLs, localization, and reading-task inspection. Measure actual rendered line lengths and line counts. Compare a control near the chosen upper/lower bounds instead of asserting one universal optimum.

## Failure Patterns
Failure includes full-width desktop paragraphs that require large eye travel, overly narrow columns creating choppy one- or two-word line endings, text reduced in size to fit a fixed card, reading width changing sharply after font swap, and “max-width” applied to containers whose internal text already has a different effective measure.

## Falsification
Falsification swaps to the supported fallback face, increases text size, changes container width, and renders representative long and short content. The contract fails if a supported state routinely exceeds the declared readable envelope or if the constraint harms comprehension more than the unconstrained layout.

## Recovery
Recovery adjusts the text container independently from decorative layout, changes column count or surrounding composition, and uses font-role-specific limits where metrics differ. If a product surface is not actually a sustained reading task, remove the artificial prose constraint rather than cargo-culting a measure rule.

## Output and Handoff
Output: `readable-line-measure-contract` with content classes, preferred/enforced range, scaling behavior, container rules, and evidence examples. Handoff wrap mechanics to line-breaking/hyphenation and overall type sizing to the parent.

## Sibling Boundary and delete-the-skill
Line breaking determines where a line can break; it does not decide how long the reading line should be. Removing this skill leaves a material reading-comfort and composition boundary without an owner.