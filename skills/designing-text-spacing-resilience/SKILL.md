---
name: designing-text-spacing-resilience
description: Use when users may override line, letter, word, or paragraph spacing and the interface must remain readable and operable instead of relying on tightly fixed text geometry.
---

# Designing Text Spacing Resilience

## Parent Contract
**Required parent:** `designing-low-vision-and-high-contrast`.

This faculty owns resilience to user-controlled text spacing and related typographic overrides. It does not choose the brand type scale; it ensures the component geometry can tolerate spacing changes without clipping information, covering controls, or severing label relationships.

## Decision Boundary
Locate text-bearing elements whose dimensions are constrained by height, absolute positioning, single-line assumptions, or vertically centered icons. Buttons, chips, tabs, alerts, floating labels, compact table rows, and navigation items are common risk zones. Define where containers grow with content and where wrapping is acceptable. If a control truly requires a single line, specify how overflow remains understandable rather than simply hiding it.

Spacing changes affect more than paragraphs. Increased line height can move helper text, expanded word spacing can alter button width, and paragraph spacing can separate a message from the control it describes. Preserve grouping with layout primitives rather than relying on exact baseline distances. Icons used as affordances should align with the control box, not with a hard-coded text baseline that breaks when users override typography.

## Failure Topology
- A fixed-height button clips the lower half of a two-line label after spacing overrides.
- Floating labels collide with entered values because vertical positions assume default line height.
- A tab wraps but its indicator remains at the old single-line height.
- Increased paragraph spacing makes an error message appear to belong to the next field.
- Ellipsis hides the differentiating portion of commands without another way to inspect the full text.
- Dense rows overlap because line-height is treated as a visual token rather than user-adjustable content geometry.

## Falsification and Recovery
Apply text-spacing overrides to real rendered screens with long labels, validation, selected tabs, badges, table rows, and narrow viewports. The design fails if information is lost, controls overlap, focus indicators are clipped, or semantic groups become visually ambiguous. Test browser zoom simultaneously because users frequently combine accommodations.

Recover by removing fixed text heights, using intrinsic sizing, letting critical labels wrap, revising alignment around content boxes, and increasing group containment where spacing changes weaken proximity. If density must be preserved, reduce nonessential decoration before constraining user text.

## Output Contract
Return `text-spacing-resilience-contract` with vulnerable component classes, intrinsic sizing rules, wrap/overflow policy, grouping protections, icon alignment behavior, prohibited clipping patterns, combined zoom/locale tests, and rendered spacing verification cases.
