---
name: designing-heading-hierarchy
description: Design visual and semantic heading hierarchy so sections are scannable, document structure is valid, and visual prominence does not corrupt heading level.
---

# Designing heading hierarchy

Heading level and visual size are related but not identical. Use this skill when pages, dialogs, dashboards, settings, or long-form content need a clear structure that works visually and for assistive technology.

## Decision ownership

Own heading role semantics, mapping between document level and visual style, spacing relationships, skipped-level policy, and repeated-section patterns. Decide when a visually prominent title is not a semantic heading and when a small heading still needs a high document level.

## Inputs and evidence

Collect page outlines, component nesting, visual styles, screen-reader landmark/heading navigation, CMS content, reusable card titles, dialog titles, and nested sections. Identify components that hardcode an `h2` or `h3` regardless of where they are embedded.

## Procedure

Define semantic heading levels from document structure first. Map visual styles separately so reusable components can receive the correct level while retaining intended appearance. Maintain one clear primary page or surface heading where appropriate and avoid choosing levels based on desired font size.

Use spacing to reinforce hierarchy: headings should associate more strongly with following content than preceding unrelated content. For cards or repeated widgets, decide whether titles belong in the page heading outline or are better represented by other semantics.

Provide APIs that allow parent context to set levels safely.

## Failure topology

Hardcoded heading tags inside reusable components create skipped or duplicated levels. Styling every card title as a large heading can flood the outline with low-value entries. Another failure is making semantic headings visually indistinguishable, reducing visual scanability even while accessibility markup is correct.

## Falsification

Generate the document outline from representative pages and navigate headings with a screen reader. Remove CSS and inspect whether structure still makes sense. Reuse components at several nesting depths. Compare visual grouping when headings wrap to multiple lines.

If changing font size would require changing HTML heading level, semantics and appearance are too tightly coupled.

## Output contract

Produce a `heading-hierarchy-contract` with structural heading rules, visual role mapping, component API expectations, spacing relationships, repeated-region policy, and outline tests for representative compositions.

## Handoffs

Use `designing-type-scale-relationships` for visual sizing, `designing-optical-heading-balance` for display shaping, `designing-paragraph-spacing` for section rhythm, and accessibility structure skills for landmark/outline verification.