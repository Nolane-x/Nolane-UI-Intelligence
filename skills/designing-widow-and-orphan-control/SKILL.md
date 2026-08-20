---
name: designing-widow-and-orphan-control
description: Control isolated lines and stranded headings in paged, printed, columnar, and constrained digital content without creating excessive gaps or unstable reflow.
---

# Designing widow and orphan control

A single line stranded at the top or bottom of a column can weaken reading flow, especially in print, PDFs, documentation, and multi-column layouts. Use this skill where pagination or fixed-height regions make such breaks material.

## Decision ownership

Own widow/orphan thresholds, heading keep-with-next behavior, block cohesion rules, and when preserving flow outweighs strict packing. Decide whether controls apply only to print/export or also to on-screen columns and paginated readers.

## Inputs and evidence

Collect target renderers, page sizes, columns, paragraph lengths, heading structures, figures, captions, print styles, browser support, and content-generation constraints. Inspect real pagination across languages and dynamic data.

## Procedure

Use native fragmentation controls where available and define graceful fallback where support differs. Keep headings with at least enough following content to establish context. Avoid forcing large paragraphs to stay together when that creates huge blank regions.

Coordinate with figures, tables, captions, and manual page breaks. Treat authored keep-together directives as exceptional because they can conflict with automatic layout under localization.

Prioritize print/export environments where page boundaries are persistent; ordinary scrolling screens rarely need strict widow/orphan control.

## Failure topology

Overaggressive keep rules create half-empty pages or overflow. Browser support differs, making a perfectly paginated preview diverge from exported PDF. Another failure is keeping a heading with one line of content while the rest of the paragraph moves, technically satisfying a rule but still producing poor flow.

## Falsification

Render long documents with varied paragraph lengths, languages, page sizes, and figures. Search automatically or visually for stranded headings and one-line fragments. Reduce page height to stress fragmentation. Verify rules degrade safely in engines that ignore specific properties.

## Output contract

Produce a `widow-and-orphan-control-contract` with target environments, minimum line thresholds, heading/block cohesion rules, figure/caption relationships, fallback policy, and pagination test documents.

## Handoffs

Use `designing-paragraph-spacing` for block rhythm, `designing-heading-hierarchy` for section semantics, `designing-print-interfaces` for print-specific layout, and `designing-content-fidelity-audits` for export verification.