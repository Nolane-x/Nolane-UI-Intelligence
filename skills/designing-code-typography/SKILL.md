---
name: designing-code-typography
description: Design typography for code, logs, terminals, identifiers, diffs, and inline technical tokens so syntax remains scannable without sacrificing density or accessibility.
---

# Designing code typography

Code-like text carries alignment, punctuation, case, and whitespace semantics that ordinary prose typography may obscure. Use this skill in developer tools, logs, API explorers, diff views, terminals, documentation, and technical configuration surfaces.

## Decision ownership

Own font selection, monospace/fallback policy, line height, ligature usage, tab width, wrapping, whitespace visibility, inline-code treatment, and syntax-emphasis constraints. Decide when proportional technical text is acceptable and when fixed metrics are essential.

## Inputs and evidence

Collect code languages, logs, long identifiers, Unicode, indentation depth, diff markers, terminal sequences, syntax highlighting, zoom, font availability, and platform rendering. Identify glyph pairs that are easily confused: `0/O`, `1/l/I`, punctuation, braces, and quotes.

## Procedure

Choose a coding font with clear glyph differentiation and broad required character coverage. Use programming ligatures only if they do not hide source characters or confuse debugging; consider disabling them in contexts where exact glyph identity matters. Tune line height for dense scanning without overlapping annotations.

Define wrapping separately for code blocks, logs, and inline code. Preserve indentation and whitespace semantics; where wrapping occurs, continuation indentation should distinguish visual wrap from real newline.

Ensure syntax color is supplementary, with enough non-color structure for selection, errors, and diff state.

## Failure topology

Decorative monospace fonts can reduce legibility. Ligatures may make `!=` or `=>` appear as a single symbol that differs from copied source. Hard no-wrap creates unusable horizontal scrolling on narrow surfaces; aggressive wrapping destroys indentation structure.

Fallback to a proportional font can invalidate column alignment silently.

## Falsification

Render ambiguous glyph sets, deeply indented code, long logs, mixed scripts, diff markers, and 200% zoom. Copy/paste text with ligatures enabled and verify source identity. Disable webfont loading and inspect fallback alignment. Test keyboard selection and horizontal/vertical scroll behavior.

## Output contract

Produce a `code-typography-contract` defining font/fallback stack, glyph criteria, ligature policy, line height, tabs/whitespace, wrapping, inline-code treatment, syntax-emphasis constraints, and representative rendering tests.

## Handoffs

Use `designing-log-viewers` for log interaction, `designing-code-diff-interfaces` for diff semantics, `designing-font-loading-fallback-behavior` for runtime font failure, and `designing-hyphenation-behavior` to keep linguistic breaking away from identifiers.