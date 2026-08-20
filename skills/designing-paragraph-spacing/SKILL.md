---
name: designing-paragraph-spacing
description: Design paragraph and block spacing so content groups remain legible without creating double-spacing, collapsed hierarchy, or inconsistent authored markup.
---

# Designing paragraph spacing

Paragraph spacing is a content-structure decision, not merely margin-bottom. Use this skill when long instructions, documentation, settings descriptions, legal copy, or rich text need stable rhythm across nested blocks.

## Decision ownership

Own spacing between paragraphs and adjacent block types, margin-collapse policy, first/last-child behavior, list relationships, and how authored content maps into system spacing. Decide whether rhythm is owned by parent flow layout or individual text elements.

## Inputs and evidence

Collect real rich-text structures, markdown/HTML output, lists, headings, callouts, blockquotes, nested containers, localization, and editor-generated markup. Inspect double margins and missing spacing around dynamically inserted blocks.

## Procedure

Prefer parent-owned flow spacing where possible so adjacent block relationships are controlled in one place. Define spacing by relationship: paragraph-to-paragraph, heading-to-body, list-to-paragraph, callout-to-copy, and so on. Keep paragraph spacing sufficient to signal separation without mimicking blank sections.

Handle empty paragraphs, nested lists, and authoring artifacts explicitly. Avoid relying on a final `:last-child` hack if components may append actions or validation after content.

Coordinate paragraph spacing with line height and overall section rhythm.

## Failure topology

Margins on every element can collapse unpredictably or double when components nest. Editors may emit empty paragraphs that create giant gaps. Another failure is equal spacing above and below headings, weakening which content the heading labels.

Tight spacing can turn legal or instructional text into an unreadable wall; excessive spacing fragments a coherent explanation.

## Falsification

Render a matrix of adjacent block types, nested lists, empty nodes, localized long paragraphs, and dynamically inserted notices. Compare both authoring preview and shipped rendering. Remove or reorder blocks and verify spacing remains relational rather than depending on accidental sibling positions.

## Output contract

Produce a `paragraph-spacing-contract` specifying flow ownership, block-to-block spacing relationships, margin-collapse strategy, nested-content rules, empty-node handling, and representative rich-text test cases.

## Handoffs

Use `designing-line-height-rhythm` for intra-paragraph rhythm, `designing-heading-hierarchy` for heading relationships, `designing-rich-text-editors` for authoring semantics, and `designing-legal-and-disclosure-typography` for dense regulated content.