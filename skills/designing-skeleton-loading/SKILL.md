---
name: designing-skeleton-loading
description: Use when initial content latency can be reduced perceptually by reserving the expected structure and the skeleton must match real layout, accessibility, motion, and failure transitions without becoming decorative shimmer.
---

# Designing Skeleton Loading

## Parent Contract
**Required parent:** `designing-empty-loading-error-states`.

This faculty owns placeholder structure shown before content resolves. Skeletons are not required for every load and are not generic gray rectangles. They are justified when the final layout is predictable enough to reserve meaningful geometry and reduce layout shift while users wait.

## Decision Boundary
Design the skeleton from the resolved component structure: title lines, media aspect ratio, metadata rows, controls, or table cells. Do not expose fake content details that imply data already exists. If the final cardinality is unknown, choose a bounded representative set rather than filling the viewport with dozens of shimmering placeholders.

The transition to content must preserve geometry where possible. A skeleton whose media block is 16:9 but loaded image is square causes exactly the layout instability the mechanism should prevent. When real content is already partially available, progressive reveal may be more truthful than keeping the whole surface in skeleton state.

Accessibility usually treats visual skeleton shapes as non-semantic. The region needs an understandable busy state and a status change when content becomes available, without making assistive technology traverse every placeholder. Motion/shimmer should respect reduced-motion settings and performance constraints; static placeholders are acceptable.

## Failure Topology
- Skeleton bears little resemblance to final content and causes a large reflow on resolution.
- Placeholder rows suggest data exists, then zero-results appears and feels like content vanished.
- Every placeholder is exposed as an accessibility element, producing meaningless navigation.
- Shimmer consumes GPU/CPU on a dense dashboard and delays real rendering.
- Partial data is ready but withheld until every request completes, making skeleton use increase latency perception.
- Error state replaces the skeleton with no stable space or causal message.

## Falsification and Recovery
Falsify with zero results, slow image dimensions, partial data arrival, error after prolonged loading, reduced motion, low-power device, 200% zoom, screen-reader busy-state handling, and content lengths much longer than placeholders. The design fails if skeleton geometry systematically mispredicts the resolved layout or if placeholders communicate fabricated data certainty.

Recover by deriving shapes from actual component geometry, reserving known dimensions, revealing available content progressively, hiding decorative placeholders from assistive technology, minimizing animation, and defining stable transitions to empty/error states.

## Output Contract
Return `skeleton-loading-contract` with eligibility criteria, placeholder geometry, cardinality policy, progressive reveal rules, layout-shift constraints, busy/accessibility semantics, motion/performance treatment, empty/error transitions, and falsification states.