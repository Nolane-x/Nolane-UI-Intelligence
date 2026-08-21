---
name: designing-line-breaking-and-hyphenation
description: Use when text wrapping, break opportunities, hyphenation, unbreakable sequences, language rules, and narrow-column behavior must preserve readability without silently removing content.
---

# Designing Line Breaking and Hyphenation

## Wrapping Is Language-Aware Layout
When text meets a boundary, the browser must choose where to break. This skill owns break and hyphenation policy for visible text: preserving words and semantics while preventing layout overflow under realistic languages, URLs, identifiers, and narrow measures.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent chooses font and hierarchy. This specialist governs wrapping mechanics after size and measure create a finite line box.

## Break Classes
Separate ordinary prose, headings, labels, identifiers, URLs, code, numbers, and user-generated strings. Each has different safe opportunities. Hyphenation may improve prose in supported languages but can damage product names, IDs, or short labels. Emergency `overflow-wrap` is a containment mechanism, not a default typographic style.

Language metadata matters because hyphenation dictionaries and line-breaking conventions depend on it. CJK and scripts without spaces need rules different from English. Non-breaking spaces, punctuation, and number/unit pairs may intentionally stay together.

## Evidence
Evidence includes language-tagged fixtures, narrow widths, long compound words, URLs, identifiers, punctuation, numbers with units/currency, text scaling, and fallback fonts. Inspect actual line breaks and copy/select behavior. Include a no-hyphenation environment because support differs across engines and dictionaries.

## Failure Modes
Failure includes horizontal overflow caused by a single long token, aggressive break-all splitting ordinary words at arbitrary characters, hyphenation applied to codes that users must copy exactly, incorrect language tags producing absurd break points, and line-breaking rules that visually separate a sign or unit from its value.

## Falsification
Falsification injects the longest plausible strings for each class, switches document language, disables hyphenation support, and narrows the container below normal breakpoints. The contract fails if content becomes inaccessible, ambiguous, or altered in copy semantics, or if layout relies on a break algorithm unavailable in a supported environment.

## Recovery
Recovery chooses class-specific wrapping, marks language correctly, permits emergency breaks only for hostile/unbounded tokens, and redesigns narrow structures that cannot hold required identifiers. Do not truncate as a substitute when full text is required; truncation belongs to a different decision owner.

## Output
Output: `line-breaking-and-hyphenation-contract` with text classes, allowed/forbidden break behaviors, language requirements, emergency policy, and boundary fixtures.

## Handoff
Handoff deliberate content shortening to truncation-and-overflow truth and target measure to readable-line-measure design.

## Sibling Boundary and delete-the-skill
Truncation removes visible content; this skill preserves all content while choosing legal wrapping points. Without it, unbreakable and language-sensitive text failures have no specific owner.