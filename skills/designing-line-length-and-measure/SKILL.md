---
name: designing-line-length-and-measure
description: Control text measure so reading, scanning, labels, instructions, and dense content remain efficient across responsive widths and zoom.
---

# Designing line length and measure

Text that spans an entire large monitor is difficult to track; text squeezed into narrow columns can become a wall of short broken lines. Use this skill to govern readable measure by text purpose.

## Decision ownership

Own target and maximum measures for sustained prose, instructions, form help, alerts, dialogs, and compact utility text. Decide when containers should stop growing, when columns should split, and when measure should follow a component rather than a page.

## Inputs and evidence

Collect text genres, typical sentence lengths, language expansion, font metrics, viewport/container sizes, zoom states, side panels, and real reading tasks. Identify layouts where line length changes dramatically because content simply fills available width.

## Procedure

Set measure ranges by reading behavior. Sustained paragraphs usually need tighter control than one-line labels or data cells. Use relative measures tied to character width or semantic container limits where practical rather than fixed pixels alone.

Coordinate measure with type size and line height. When a wide layout offers extra space, preserve readable text width and allocate space to supporting regions instead of stretching prose. On narrow layouts, allow natural wrapping but avoid columns so narrow that every phrase fragments.

Treat centered text cautiously at long measures because line starts become difficult to locate.

## Failure topology

Global max-width values can overconstrain dense instructions or underconstrain editorial copy. Character-count heuristics fail when fonts or scripts have very different glyph widths. Another failure is measure optimized for English but unusable for CJK, RTL, or long unbroken tokens.

## Falsification

Render representative text in several languages and fonts, including large text zoom. Observe reading and scanning at minimum and maximum widths. Inject long URLs, code, and unbreakable names. If the layout requires horizontal page scrolling for prose at high zoom, measure or wrapping rules are wrong.

Compare fatigue and line-tracking errors in controlled reading tasks when measure is a critical surface.

## Output contract

Produce a `line-length-and-measure-contract` with text categories, target/max/min measures, container ownership, wrapping exceptions, language considerations, zoom behavior, and tested representative layouts.

## Handoffs

Use `designing-line-height-rhythm` for vertical readability, `designing-rag-and-line-break-quality` for line endings, `designing-hyphenation-behavior` for language-aware wrapping, and `engineering-responsive-composition` for page-level allocation.