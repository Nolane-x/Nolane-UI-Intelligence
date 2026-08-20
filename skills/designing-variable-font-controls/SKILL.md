---
name: designing-variable-font-controls
description: Use variable-font axes deliberately so weight, width, optical size, grade, and custom axes improve typography without creating uncontrolled style combinations or layout shifts.
---

# Designing variable font controls

Variable fonts expose continuous design spaces that can easily become another source of arbitrary one-off values. Use this skill when a product or design system wants to use axes beyond fixed font instances.

## Decision ownership

Own which axes are exposed, semantic presets versus continuous control, interaction with type roles, runtime animation limits, fallback mapping, and compatibility across browsers/platforms. Decide whether an axis is a system decision or an author/user control.

## Inputs and evidence

Collect font axis metadata, supported ranges, named instances, optical-size behavior, licensing, browser/platform support, fallback fonts, layout metrics across axes, and actual typographic roles. Measure whether width or grade changes alter line breaks or control dimensions.

## Procedure

Prefer semantic presets mapped to axis values rather than arbitrary per-component numbers. Use optical size according to font design when it materially improves small or large text. Distinguish grade from weight when preserving text width matters.

If exposing width or slant interactively, constrain ranges and show consequences. Define fallback fixed-font instances for environments that lack variable support. Avoid animating axes that cause expensive reflow or reduce readability during transition.

Record axis combinations tested; variable fonts can have nonlinear behavior at extremes.

## Failure topology

Continuous controls produce stylistic inconsistency. Width-axis changes can break responsive layouts. Weight and grade may be confused, causing unexpected text reflow. Another failure is depending on an axis not present in fallback fonts, creating major visual hierarchy shifts during loading.

## Falsification

Render every semantic preset at axis extremes and representative combinations. Switch to fallback fonts and compare hierarchy and layout. Test zoom, localization, and print/export. Animate proposed axis transitions under performance profiling if motion is involved.

If designers frequently use unregistered axis values, governance is ineffective.

## Output contract

Produce a `variable-font-controls-contract` defining supported axes, semantic presets, allowed ranges, fallback mapping, layout-impact constraints, animation policy, author/user exposure, and tested combinations.

## Handoffs

Use `engineering-typographic-systems` for role mapping, `designing-optical-heading-balance` for display use, `designing-font-loading-fallback-behavior` for substitutions, and motion specialists if axis animation is justified.