---
name: designing-hyphenation-behavior
description: Configure language-aware hyphenation and word breaking so narrow text remains readable without mangling names, code, URLs, or unsupported languages.
---

# Designing hyphenation behavior

Hyphenation can rescue narrow columns and justified text, but incorrect breaks damage comprehension and trust. Use this skill when interfaces support long words, multiple languages, editorial text, or constrained labels.

## Decision ownership

Own where automatic hyphenation is permitted, language metadata requirements, exceptions, minimum word/line constraints, and fallback breaking for unbreakable tokens. Decide which content classes—prose, headings, labels, code, identifiers—use different policies.

## Inputs and evidence

Collect supported locales, dictionary support, language tags, product names, technical identifiers, URLs, user-generated text, column widths, and typography settings. Identify content rendered without correct `lang` metadata because hyphenation quality depends on language.

## Procedure

Enable hyphenation only where language can be determined reliably. Set conservative limits for short words and consecutive hyphenated lines where controls exist. Protect product names, codes, and identifiers when breaking would obscure meaning.

For URLs and long machine tokens, use appropriate overflow-wrap or word-break rules rather than linguistic hyphenation. Test script-specific behavior; not all languages use word boundaries or hyphens similarly.

Provide editorial soft-hyphen support only when authors understand responsive consequences.

## Failure topology

Applying English hyphenation to another language creates invalid breaks. Generic `word-break: break-all` prevents overflow but destroys readability. Soft hyphens embedded in content may appear incorrectly in search, copy/paste, or alternate renderers.

Another failure is suppressing all breaks, causing page-level horizontal scrolling at high zoom.

## Falsification

Render curated words from each supported locale, proper nouns, URLs, identifiers, and mixed-language strings across narrow widths. Copy and search hyphenated text to ensure semantics remain intact. Remove language metadata and verify fallback does not produce misleading linguistic breaks.

## Output contract

Produce a `hyphenation-behavior-contract` defining eligible text classes, language requirements, automatic limits, protected terms, machine-token breaking, author controls, fallback behavior, and locale-specific test corpus.

## Handoffs

Use `designing-rag-and-line-break-quality` for overall line endings, `designing-line-length-and-measure` for column width, `designing-code-typography` for identifiers/code, and localization skills for correct language metadata.