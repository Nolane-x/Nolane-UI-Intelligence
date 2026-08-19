---
name: designing-markdown-editors
description: Use when users author Markdown or Markdown-like source and the editor must coordinate plain-text truth, syntax assistance, preview fidelity, source position, shortcuts, extensions, and round-trip behavior without pretending rendered preview is the editable document.
---

# Designing Markdown Editors

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns source-first lightweight markup authoring. It differs from rich-text editing because the canonical user-visible representation is text syntax, even when a preview or hybrid rendering exists. It does not own publishing or generic code-editor behavior beyond what Markdown authoring requires.

## Decision Model
Declare the supported dialect and extensions: CommonMark-like basics, tables, task lists, math, frontmatter, mentions, footnotes, custom directives, or product-specific embeds. Syntax assistance must match the actual parser; toolbar insertion that produces unsupported markup creates false affordance.

Source and preview need a fidelity contract. If split preview is present, preserve scroll/selection correspondence where practical without forcing brittle pixel synchronization. A preview refresh should not steal cursor position, and parser errors should identify source ranges rather than merely rendering a blank pane. In a hybrid mode, reveal enough syntax when editing ambiguous structures so users can understand the underlying source.

Text editing must respect standard expectations: selection-aware formatting shortcuts, tab behavior defined for lists/code blocks, IME composition, undo grouping, paste rules, and line ending preservation where material. If the product stores canonical Markdown, transformations must not rewrite user formatting unnecessarily on each save unless formatter behavior is explicit.

## Failure Topology
- Toolbar inserts table syntax although the configured parser does not support tables.
- Preview sanitization differs from production render and users publish content that changes later.
- Switching from preview to source jumps to the top and loses the editing position.
- Auto-format-on-save rewrites handcrafted source unexpectedly and produces noisy diffs.
- Pasting a URL over selected text deletes the selection instead of creating a link as expected by the product shortcut model.
- Custom extension renders in preview but its raw syntax has no accessible explanation or editing path.

## Falsification and Recovery
Falsify with large documents, malformed markup, unsupported extensions, split-view scrolling, IME, nested lists, code fences, source/preview toggle, save/reload round-trip, external diff, keyboard-only use, screen readers, and production rendering under the same parser configuration. The design fails if preview and publish semantics diverge materially or if editing operations mutate unrelated source without user intent.

Recover by pinning the dialect/parser contract, sharing render configuration between preview and production where possible, preserving source positions, limiting transformations to explicit commands, surfacing parse errors by range, and validating round-trip source stability.

## Output Contract
Return `markdown-editor-contract` with dialect/extensions, source canonicality, command insertion rules, preview renderer/fidelity, source-preview navigation, parse-error behavior, formatting policy, keyboard/IME semantics, sanitation boundaries, round-trip tests, and falsification cases.