---
name: designing-type-scale-relationships
description: Design type-size relationships from functional hierarchy and viewing context rather than applying a mathematical ratio mechanically.
---

# Designing type-scale relationships

A type scale should make roles distinguishable while preserving usable density and line wrapping. Use this skill when choosing how body, label, title, display, caption, and utility sizes relate.

## Decision ownership

Own the set of supported font-size steps, their semantic separation, allowed responsive or density adaptations, and rules for introducing exceptions. Decide whether a role difference needs size or can be expressed more effectively through weight, spacing, color, or placement.

## Inputs and evidence

Collect actual text roles, body size requirements, target viewing distance, device classes, density needs, localization, long headings, table density, and accessibility zoom. Compare current adjacent steps for perceptual distinguishability and layout cost.

## Procedure

Start from a body size that supports sustained reading and interaction, then add only the steps needed to express real hierarchy. Evaluate ratios perceptually rather than worshiping a modular scale. Small interfaces often need tighter upper steps than editorial pages; large displays may need broader separation.

Test each role in context with real text. Coordinate size with line height and measure: a larger heading that wraps into four lines may weaken hierarchy rather than strengthen it. Avoid using tiny text as the primary way to create hierarchy in dense interfaces.

Define whether compact density changes spacing only or may also alter specific text roles.

## Failure topology

A strict ratio can create oversized headings and microscopic captions. Too many close steps make hierarchy invisible while increasing token count. Role names like `font-size-14` leak implementation rather than intent. Another failure is shrinking secondary text below comfortable readability to preserve layout.

## Falsification

Render the full role set in representative interfaces and grayscale screenshots. Ask whether adjacent roles remain distinguishable without relying on color. Test long localized headings, narrow widths, and zoom. Remove steps one at a time and observe whether semantic distinction survives.

If designers repeatedly choose arbitrary in-between sizes, the scale may not fit product needs.

## Output contract

Produce a `type-scale-relationships-contract` defining size steps, role mappings, perceptual rationale, body baseline, upper/lower limits, density/responsive adaptations, exception criteria, and rendered examples across dense and spacious contexts.

## Handoffs

Use `designing-line-height-rhythm` for vertical metrics, `designing-heading-hierarchy` for heading semantics, `designing-optical-heading-balance` for display tuning, and `verifying-typography-under-zoom` for stress testing.