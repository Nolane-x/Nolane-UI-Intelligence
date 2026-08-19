---
name: designing-accordion-expansion-motion
description: Use when disclosure content expands or collapses and motion must preserve reading position, layout stability and causal association between trigger and revealed region.
---

# Designing Accordion Expansion Motion

## Parent Contract
**Required parent:** `designing-motion`.

This skill owns the transition of disclosure geometry. Disclosure semantics, heading structure and whether multiple sections may remain open are owned elsewhere.

## Decision Boundary
Expansion motion should teach **which trigger controls which region** while keeping the page navigable during geometry change. The hard problem is not easing; it is content whose height is dynamic, nested, asynchronous or large enough to move the user’s reading position substantially.

Prefer animations that can respond to measured content rather than hard-coded `max-height` ceilings. When content changes while open, decide whether to animate the delta, snap, or preserve the user’s scroll anchor. Nested accordions should not multiply long durations so opening a deep branch feels like waiting through several sequential curtains.

Collapse needs a focus policy. If focus is inside the region being collapsed, move it to an appropriate surviving control before or as the content becomes unavailable; never leave focus on hidden descendants. The visible motion should not run after semantics already claim the region is available/unavailable in a way that confuses assistive technology.

Large disclosures can use shorter or non-distance-proportional timing; animating 1200 pixels at the same speed as 80 pixels is often excessive. Reduced motion can snap geometry while preserving icon/state change.

## Failure Topology
- `max-height` animation clips long localized or user-generated content.
- Collapsing content causes the viewport to jump to an unrelated position.
- Nested transitions produce cumulative multi-second delay.
- Focus remains in hidden content.
- A rotating chevron animates correctly but the content state changes at a different time.

## Falsification and Recovery
Test short/long content, async additions, nested disclosures, text zoom, localization expansion, collapse while focus is deep inside, rapid open-close reversal and reduced motion. The contract fails if content clips, focus disappears, or reading position becomes unpredictable.

Recover by making semantic state authoritative, measuring real geometry only when necessary, preserving a stable scroll anchor, and shortening/removing motion for large deltas.

## Output Contract
Return `accordion-expansion-motion-contract` with geometry strategy, duration policy, scroll-anchor policy, nested behavior, focus-collapse rule, reversal handling, reduced-motion equivalent and stress fixtures.