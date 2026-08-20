---
name: designing-content-driven-breakpoints
description: Derive responsive breakpoints from observable content and interaction failure thresholds instead of device categories or inherited framework defaults.
---

# Designing content-driven breakpoints

A breakpoint should mark a change in what the interface can successfully communicate or operate, not a popular handset width. Use this skill when defining thresholds for layout transformations.

## Decision ownership

Own the evidence used to place breakpoints, the failure condition each threshold prevents, and whether the trigger should depend on width, height, aspect ratio, content size, or container state. Decide when two pressure points warrant separate transitions versus one coordinated state change.

## Inputs and evidence

Collect longest credible labels, localization expansion factors, user font scaling, validation messages, data ranges, minimum target sizes, action priority, chart legends, navigation depth, and actual resize observations. Measure the first width where a region wraps poorly, collides, hides semantics, or forces excessive scrolling.

## Procedure

Begin from the fully expressive composition and reduce available space until a specific failure appears. Record that pressure point, then design the next composition state and repeat. Add margin around exact collision points so tiny changes or font rendering differences do not cause jitter.

Use representative worst-case content, not lorem ipsum or English-only labels. Treat vertical constraints separately: short laptop windows and on-screen keyboards can require transitions even when width is generous.

Keep breakpoint count proportional to meaningful structural states, not every measurable change.

## Failure topology

Framework defaults create breakpoints unrelated to a product’s content. Choosing values from screenshots can hide failures at nearby widths. Another failure is deriving a threshold from one component while several siblings reach pressure at different points, causing cascading micro-transitions.

Content-driven breakpoints can still be brittle if evidence ignores font substitution, zoom, dynamic banners, or localization.

## Falsification

Sweep continuously through threshold neighborhoods with worst-case content and alternate fonts. Add and remove inline errors, badges, and optional actions. Test localization and 200% zoom. Verify transitions occur before actual failure and do not create larger problems in the next state.

Ask what concrete failure each breakpoint prevents. If the answer is only “tablet starts here,” remove or re-derive it.

## Output contract

Produce a `content-driven-breakpoints-contract` listing each threshold, governing region, observed pressure condition, measurement evidence, safety margin, resulting composition change, vertical/aspect considerations, and regression cases for worst-case content.

## Handoffs

Use `engineering-responsive-composition` to define resulting states, `designing-container-query-layouts` when local space is the correct trigger, `designing-responsive-form-layouts` for form-specific pressure, and `verifying-responsive-state-parity` after structural changes.