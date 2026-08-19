---
name: designing-rich-text-editors
description: Use when users author structured formatted content in a WYSIWYG surface and the editor must preserve document semantics, selection, formatting state, paste, keyboard behavior, accessibility, and serialization without becoming a decorative contenteditable.
---

# Designing Rich Text Editors

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns structured rich-text authoring where users manipulate headings, paragraphs, lists, links, emphasis, embeds, tables, or other schema-defined nodes through a rendered editing surface. It does not own Markdown source editing or the broader publishing workflow. Visual formatting must remain a projection of a semantic document model.

## Decision Architecture
Define the document schema before the toolbar. Establish allowed block and inline structures, nesting rules, normalization, and serialization. Toolbar availability should reflect the current selection and schema validity rather than offering formatting commands that later produce malformed or unsupported output.

Selection and command behavior are central. Inline commands should preserve or intentionally move selection, block transformations need predictable cursor placement, and undo/redo must treat one user intent as one history unit where possible. Pasting from office suites, web pages, or plain text requires sanitization and semantic normalization; importing foreign markup should not smuggle arbitrary styles or active content into the product.

Accessibility requires genuine text-editing semantics, not a keyboard-hostile canvas. Heading/list/link meaning should survive serialization and screen-reader use. Placeholder text cannot be the only label. Rich embeds need navigable entry/exit and a text-equivalent or inspectable representation where appropriate.

## Failure Topology
- Toolbar toggles bold visually but serialization loses the semantic mark.
- Pasting from a word processor imports dozens of foreign styles and hidden markup.
- Backspace at a list boundary deletes an entire adjacent block unexpectedly.
- Undo reverses every keystroke individually after one formatting command, making recovery unusable.
- Selection disappears when a toolbar button receives focus, so command applies to the wrong range.
- Custom editor surface is not operable with screen readers or keyboard text navigation.

## Falsification and Recovery
Falsify with mixed-format paste, nested lists, links across selections, IME text, undo after structural transforms, drag/drop content, keyboard-only formatting, screen-reader navigation, copy between two documents, unsupported imported nodes, and serialization round-trip. The design fails if the semantic document cannot round-trip through edit/save/reload without changing meaning or if standard text-editing operations behave unpredictably.

Recover by using an explicit schema, normalizing commands and paste, preserving selection through toolbar interaction, grouping history by intent, sanitizing external markup, and verifying semantic serialization plus assistive-technology editing behavior.

## Output Contract
Return `rich-text-editor-contract` with document schema, command/toolbar mapping, selection rules, history grouping, paste/import sanitation, serialization, embed semantics, keyboard/IME behavior, accessibility model, round-trip tests, and falsification cases.