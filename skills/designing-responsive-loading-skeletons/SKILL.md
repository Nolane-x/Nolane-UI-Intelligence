---
name: designing-responsive-loading-skeletons
description: Make loading skeletons reflect the responsive composition that will actually resolve, without causing large layout shifts or encoding false content structure.
---

# Designing responsive loading skeletons

Skeletons are useful only when they stabilize expectations and geometry. Use this skill when placeholder layouts must adapt to the same responsive state as eventual content across cards, lists, dashboards, forms, or pages.

## Decision ownership

Own skeleton geometry per responsive state, what structural regions receive placeholders, how uncertainty is represented, and how much size is reserved to minimize layout shift. Decide when a generic progress state is safer than a detailed skeleton that guesses wrong.

## Inputs and evidence

Collect resolved layout states, typical and extreme content sizes, asynchronous dependencies, image aspect ratios, server-rendered hints, cumulative layout shift metrics, and cases where loading occurs during resize. Identify regions whose final existence depends on permissions or data.

## Procedure

Base skeleton structure on stable layout invariants, not fake text lines copied from a mockup. Use the same container and responsive rules as final content where possible. Reserve predictable media and control geometry, but avoid implying a fixed number of items when the result cardinality is unknown.

When the composition changes by state, change the skeleton coherently rather than scaling a desktop placeholder. Avoid animation or shimmer that becomes visually noisy in dense mobile layouts or violates reduced-motion preferences.

## Failure topology

A desktop skeleton squeezed into mobile creates huge layout shifts when content reflows. Overly detailed skeletons communicate structure that never appears, harming perceived reliability. Another failure is placeholder height based on short sample copy, causing late expansion under localization.

Skeleton and content can choose different breakpoints if implemented separately.

## Falsification

Throttle loading while continuously resizing. Compare placeholder and final region positions and measure layout shift. Test long localized content, no-result responses, permission-gated regions, and reduced motion. Verify skeleton state never exposes inaccessible decorative placeholders as meaningful controls.

## Output contract

Produce a `responsive-loading-skeletons-contract` defining stable placeholder regions, responsive state mapping, reserved geometry, uncertainty policy, motion behavior, accessibility treatment, and measured placeholder-to-content shift scenarios.

## Handoffs

Use `designing-skeleton-loading` for general placeholder semantics, `engineering-responsive-composition` for state structure, `designing-responsive-media-crops` for media geometry, and `verifying-responsive-state-parity` for loading-to-loaded continuity.