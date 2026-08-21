---
name: designing-variable-font-axis-behavior
description: Use when a variable font exposes weight, width, optical size, slant, grade, or custom axes and axis values must change predictably across roles, states, sizes, and responsive conditions.
---

# Designing Variable-Font Axis Behavior

## Axes Are Behavioral Parameters
A variable font turns type selection into a continuous parameter space. This skill owns how supported axes are mapped to semantic roles and runtime conditions so interpolation remains intentional rather than arbitrary. It does not own the product's overall typographic taste; it governs behavior inside the chosen variable font.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent selects hierarchy and font roles. This specialist takes a variable face already in use and defines the legal axis domain, mappings, and transition behavior.

## Axis Inventory
Record registered and custom axes, min/default/max, named instances, interactions, and whether the browser or font applies automatic behavior. Weight and grade are not interchangeable: weight can change advance widths while grade may preserve them. Optical size may alter spacing and contrast even when the nominal font size stays fixed.

Map semantic roles to axis values or bounded ranges. A responsive rule may slightly narrow a display face under pressure, but it must not erode legibility or silently change the hierarchy. Continuous interpolation needs stable end points and no unexplained magic constants.

## Behavior Invariants
Axis changes preserve readable glyph forms and intended emphasis. State transitions such as hover/selected do not use typography motion that destabilizes layout unless that movement is deliberate. Automatic optical sizing is either accepted and tested or explicitly disabled in favor of controlled values. Unsupported environments have a defined static instance fallback.

## Evidence
Evidence includes axis specimen grids, line-box and advance-width measurements, responsive cases, animation/transition tests where axes move, and screenshots at extreme permitted values. Inspect resolved CSS/font settings and actual face metadata; visual approximation alone cannot prove that the intended axis is applied.

## Failure Modes
Failure includes using width axis as an emergency fit mechanism until glyphs become hard to read, mapping emphasis to weight values that move neighboring layout, combining automatic and manual optical size unpredictably, custom-axis values outside the meaningful design space, and browsers falling back to static instances with no visible indication in evidence.

## Falsification
Falsification renders min/default/max and boundary role values, disables variable-font support, changes container size around responsive mappings, and compares task-relevant text. If hierarchy reverses, layout moves beyond tolerance, or a fallback silently loses a critical distinction, the axis contract fails.

## Recovery
Recovery narrows the permitted axis range, replaces continuous rules with named semantic instances, separates grade from weight where geometry matters, and provides a static fallback that preserves the most important distinction. Do not compensate a bad font choice with increasingly extreme axis manipulation.

## Output and Handoff
Output: `variable-font-axis-behavior-contract` with axis inventory, semantic mappings, legal ranges, interaction/responsive behavior, fallback instances, and edge-case evidence. Handoff overall type hierarchy to the parent and runtime loading concerns to webfont-loading engineering.

## Sibling Boundary and delete-the-skill
Readable-line measure and fallback metrics consume the resulting typography but do not decide axis semantics. Removing this owner leaves continuous font parameter behavior, axis interactions, and fallback equivalence without a dedicated decision contract.