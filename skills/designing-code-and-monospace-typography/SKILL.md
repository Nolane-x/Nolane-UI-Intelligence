---
name: designing-code-and-monospace-typography
description: Use when code, logs, terminals, diffs, identifiers, or structured technical text needs typography optimized for glyph disambiguation, indentation, line scanning, selection, wrapping, and dense developer workflows.
---

# Designing Code and Monospace Typography

## Technical Text Has Different Reading Tasks
Code is scanned for structure, symbols, indentation, and small token differences rather than read like prose. This skill owns typographic decisions for code-like content: monospacing policy, ambiguous glyphs, line height, ligatures, tab width, wrapping, whitespace visibility, and how dense technical text coexists with UI chrome.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent owns overall typography. Code-editor commands, syntax semantics, and editing behavior remain outside this specialist; this skill governs the rendered text system they depend on.

## Glyph and Spacing Contract
Verify distinction among `0/O`, `1/l/I`, braces, brackets, quotes, operators, and punctuation in the actual face. Decide whether programming ligatures improve or obscure the supported workflow; a ligature must not prevent users from identifying underlying characters. Define tab/indent width and whether alignment relies on true monospace metrics.

Line height should support long scanning sessions while preserving block density and clear cursor/selection geometry. Inline code inside prose may use a related but not identical size/line-height contract to full editor panes.

## Evidence
Evidence includes representative code in supported languages, diffs, logs, long identifiers, Unicode identifiers if supported, selection/caret screenshots, whitespace markers, zoom, fallback fonts, and copy/paste. Test rasterization at common display densities because thin punctuation can disappear even if metrics are correct.

## Failure Modes
Failure includes ambiguous zero/O causing operator error, ligatures concealing character count in diffs, fallback font breaking alignment, line height clipping underlines/diagnostics, wrapped logs whose continuation cannot be distinguished from new records, and `pre` blocks forcing page-wide horizontal overflow without a containment strategy.

## Falsification
Falsification asks reviewers to distinguish known ambiguous tokens, blocks the primary font, changes zoom, displays deep indentation and long lines, and compares copied source to visible glyphs. If typography can cause a reasonable user to misread the actual code or destroys structural alignment, the contract fails.

## Recovery
Recovery selects a more legible technical face, disables problematic ligatures by context, restores stable monospacing, and separates editor versus inline-code metrics. If long-line handling is an interaction decision such as soft wrap or minimap behavior, hand it to the code-editor owner rather than hiding it in type styling.

## Output
Output: `code-and-monospace-typography-contract` with face/fallback requirements, glyph disambiguation, spacing, ligature policy, line-height/wrap constraints, and technical-text evidence.

## Handoff
Handoff editing commands and cursor behavior to code-editor interaction specialists; handoff webfont availability to font-loading engineering.

## Sibling Boundary and delete-the-skill
General typography can establish hierarchy but does not own source-code character fidelity and structural scanning. Removing this skill leaves a distinct technical-reading failure class unowned.