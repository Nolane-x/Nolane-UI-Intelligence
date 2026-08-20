---
name: designing-line-height-rhythm
description: Set line-height relationships that preserve readability, vertical rhythm, control fit, and script safety across roles, fonts, and zoom.
---

# Designing line-height rhythm

Line height controls both readability and component geometry. Use this skill when text feels cramped, vertically loose, misaligned across roles, or breaks controls under alternate fonts and languages.

## Decision ownership

Own line-height values and relationships by typographic role, minimum allowances for scripts and diacritics, and policies for single-line controls versus wrapping text. Decide whether line height scales proportionally or uses tuned values by role.

## Inputs and evidence

Collect font metrics, cap height, x-height, ascenders/descenders, supported scripts, text roles, control heights, wrapping behavior, density modes, and zoom. Inspect clipping in real browsers/platforms rather than assuming font bounding boxes match design-tool previews.

## Procedure

Tune line height for function. Body text needs comfortable interline separation; large display headings often need tighter leading; small labels may need more generous relative leading for readability. Keep line boxes sufficient for diacritics and scripts with tall marks.

For controls, avoid making line height the only mechanism that centers text if it risks clipping alternate fonts. Coordinate line-height tokens with spacing and type size, but do not force all roles onto one mathematical baseline when platform rendering makes it harmful.

Test multi-line labels and errors inside constrained components.

## Failure topology

Unitless global ratios can be too loose for headings and too tight for small text. Fixed pixel line heights can become invalid when text size changes. Another failure is clipping Vietnamese diacritics, Arabic marks, or emoji because line boxes were tuned only against Latin samples.

Dense modes can shrink row height without adjusting line-height strategy, causing visual collision.

## Falsification

Render worst-case glyphs, mixed scripts, emoji, superscripts, and multi-line content across supported fonts. Test font fallback and browser zoom. Inspect baseline alignment among adjacent controls and typography roles. If line-height changes are needed per component to prevent clipping, system roles may be underspecified.

## Output contract

Produce a `line-height-rhythm-contract` defining line-height per role, font/script safety constraints, control integration rules, density adaptations, wrapping behavior, and rendered evidence under fallback and zoom.

## Handoffs

Use `designing-type-scale-relationships` for size roles, `designing-paragraph-spacing` for block rhythm, `designing-multiline-labels` for compact component wrapping, and `designing-font-loading-fallback-behavior` for metric substitution.