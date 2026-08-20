---
name: verifying-typography-under-zoom
description: Verify typography and text-bearing controls under browser zoom, text scaling, and magnification so content remains readable, reachable, and structurally coherent.
---

# Verifying typography under zoom

Typography can look perfect at 100% while failing when users enlarge text or zoom the page. Use this skill as an evidence gate for text systems, responsive layouts, forms, dialogs, tables, and dense interfaces.

## Decision ownership

Own the zoom/text-scaling test matrix, pass criteria, failure classification, and evidence required for completion. Decide which environment-specific scaling modes must be tested and which layout transformations are acceptable under magnification.

## Inputs and evidence

Collect supported browsers/platforms, WCAG reflow/text-resize requirements, typography roles, fixed-height controls, overflow regions, responsive breakpoints, dialogs, tables, navigation, and user content. Include 200% text enlargement and high page zoom where applicable.

## Procedure

Test both browser zoom and OS/app text scaling because they can affect layout differently. Verify content does not clip, overlap, disappear, or require two-dimensional page scrolling except where intrinsically necessary. Check that controls grow or wrap with text and that labels remain associated.

Inspect responsive state changes triggered by zoom; they must preserve task parity. Test sticky headers, fixed panels, modals, and virtual keyboards/magnifiers that reduce effective viewport.

Record screenshots or rendered evidence at exact scale settings.

## Failure topology

Fixed heights clip labels; absolute-positioned badges overlap text; dense tables force page-level horizontal scrolling. Another failure is hiding content at zoom through responsive “mobile” simplification that removes functionality.

Browser zoom may also trigger different breakpoints than text-only scaling, exposing inconsistent assumptions.

## Falsification

Run representative workflows at 100%, 200%, 300%, and 400% zoom where supported, plus platform text-size settings. Use longest localized copy and errors. Navigate with keyboard and screen reader while zoomed. Compare capability matrices before and after reflow.

Any clipped or unreachable text is a failure even if the page technically renders.

## Output contract

Produce a `typography-under-zoom-contract` containing environments, scale settings, tested surfaces, reflow/capability results, clipping/overlap evidence, exceptions for intrinsically two-dimensional content, and defects routed to owning specialists.

## Handoffs

Use `engineering-typographic-systems` for systemic role issues, `engineering-responsive-composition` for reflow failures, `designing-multiline-labels` for controls, and accessibility evidence skills for release gating.