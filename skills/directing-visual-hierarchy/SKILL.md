---
name: directing-visual-hierarchy
description: Use when a UI contains competing information, actions, status, or content and the agent must make perceptual priority match task and product priority.
---

# Directing Visual Hierarchy

## Overview
Hierarchy is the order in which attention, comprehension, and action should happen. It is not “make the heading bigger.”

## Parent Contract
**Required parent:** `routing-ui-work`.

Use the product decision hierarchy and IA layers. If visual priority conflicts with product/task priority, product/task priority wins unless the contract explicitly asks for a dramatic editorial moment.

## Build an attention map
Classify visible elements by role:
- `P0 orientation/safety`: identity, critical status, destructive context, blocking error
- `P1 primary decision/action`
- `P2 supporting evidence/context`
- `P3 secondary control/metadata`
- `P4 tertiary/ambient/decorative`

This is not a fixed count. The key is relative priority.

## Hierarchy channels
Use multiple compatible channels rather than maxing one:
- position and reading order
- scale
- typographic weight/contrast
- spacing/isolation
- alignment
- color/luminance
- surface/elevation
- imagery/motion

A priority system is fragile when it relies only on color or only on type size.

## Competing focal points
For each viewport identify the intended first, second, and third attention targets. If several elements independently demand first attention—giant title, bright CTA, saturated chart, floating badge, animated widget—the design has no hierarchy.

## Emphasis budget
Emphasis is scarce. Primary actions should not share identical visual weight with secondary actions. Status colors should not overpower the decision they support. Decorative accents should not become the loudest object unless they are intentionally the product thesis.

## Information density
Dense UIs need **stronger relational hierarchy**, not necessarily more whitespace. Use alignment, consistent row anatomy, typography, grouping, frozen columns, summaries, and selective emphasis so experts can scan quickly. Marketing-page spacing can destroy operational scanability.

## Repetition and rhythm
Repeated visual weight communicates equivalence. If every feature is inside the same card with the same heading/action, the UI tells users all features matter equally. Vary structure when importance/function differs; keep structure stable when comparison matters.

## State hierarchy
Errors, warnings, success, selection, focus, and live updates change hierarchy temporarily. Define how transient states gain attention without causing permanent visual chaos or masking the main task.

## Accessibility interaction
Hierarchy must survive grayscale/color-vision differences, zoom, reflow, high contrast, and screen-reader reading order where applicable. Visual hierarchy and semantic heading/landmark order should not contradict each other.

## Output: `hierarchy-map`
Return `priority_classes`, `attention_sequence_by_view`, `hierarchy_channels`, `emphasis_budget`, `competing_focal_points`, `state_overrides`, `density_strategy`, and `semantic_alignment`.

## Adversarial checks
- Blur the screen: can you still identify major groups and focal point?
- Remove color: does hierarchy survive?
- Replace copy with long content: do priorities remain clear?
- Look at the page at 25% scale: does rhythm still read?
- Read semantic headings only: do they tell the same story as the visual hierarchy?

## V5 Experiential Priority Class
Add `PX — experiential identity` beside safety/orientation and task priorities. **PX** does not automatically outrank P0/P1, but it is not demoted to decoration when emotion, awe, role projection, memorability or institutional presence is a product success criterion. The hierarchy plan must state where experiential identity gets a legitimate focal/scale moment and where task throughput deliberately wins.
