---
name: designing-rag-and-line-break-quality
description: Improve line endings and break opportunities so paragraphs, labels, and headings avoid distracting shapes without forcing brittle authored breaks.
---

# Designing rag and line-break quality

The right edge of wrapped text affects reading rhythm and perceived polish. Use this skill when text creates extreme short lines, repeated shapes, orphaned punctuation, or unstable wrapping across responsive layouts.

## Decision ownership

Own acceptable rag quality, break-opportunity policy, where balancing is appropriate, and when content editing, hyphenation, measure changes, or layout changes are preferable. Decide which text types deserve manual review versus automatic handling.

## Inputs and evidence

Collect real text corpora, language/script mix, widths, font metrics, hyphenation dictionaries, dynamic strings, labels, and headings. Capture problematic line endings rather than judging only idealized samples.

## Procedure

First fix measure and font metrics. Then use language-aware wrapping, hyphenation, balancing, nonbreaking spaces, or controlled authoring features according to text type. Avoid inserting nonbreaking spaces broadly because they can create overflow at narrow widths.

For interface labels, favor concise content and layouts that tolerate wrapping. For long-form prose, prioritize reading continuity over perfect visual symmetry. For headings, stricter optical treatment may be justified.

Document protected terms such as product names or number-unit pairs that should remain together when space permits.

## Failure topology

Manual `<br>` tags and `&nbsp;` patches fix one width and break another. Over-hyphenation disrupts comprehension. Text-wrap balancing on long paragraphs can create unnecessary reflow cost or unnatural line distribution.

Rag optimization can become cosmetic overengineering if it changes content semantics or harms localization.

## Falsification

Test a corpus across continuous widths, languages, and fallback fonts. Disable special rules to understand whether they solve real defects. Inject long proper nouns, URLs, and numbers. Check overflow at high zoom and narrow containers.

If exceptions accumulate per string, change the layout or content system instead of continuing micro-patches.

## Output contract

Produce a `rag-and-line-break-quality-contract` defining text categories, acceptable rag criteria, wrap/hyphenation tools, protected-term rules, manual-authoring limits, fallback behavior, and corpus-based responsive tests.

## Handoffs

Use `designing-line-length-and-measure` for width control, `designing-hyphenation-behavior` for dictionaries and language rules, `designing-optical-heading-balance` for display text, and `designing-text-truncation` when wrapping is intentionally limited.