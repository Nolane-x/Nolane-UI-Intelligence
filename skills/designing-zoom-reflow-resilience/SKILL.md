---
name: designing-zoom-reflow-resilience
description: Use when magnification or narrow effective viewports can transform a desktop composition and the product must preserve content and actions without requiring two-dimensional hunting.
---

# Designing Zoom Reflow Resilience

## Parent Contract
**Required parent:** `designing-low-vision-and-high-contrast`.

This faculty owns behavior under browser zoom, OS text scaling, and equivalent narrow effective viewports. It asks whether users can magnify content while preserving task reachability and a coherent reading path. It does not merely check a responsive breakpoint screenshot; zoom can expose overflow and fixed-size assumptions that ordinary device testing misses.

## Decision Boundary
Model magnification as a change in available layout space, not as a user error. Identify regions that may stack, wrap, collapse, or become scroll containers, and distinguish true two-dimensional work surfaces from ordinary content that should reflow. Persistent toolbars must not consume the majority of the magnified viewport. Fixed overlays, sticky headers, and bottom actions need bounded dimensions so they do not create a narrow slit of usable content.

Preserve task relationships during recomposition. Labels must remain associated with controls, error text with fields, and table context with the data it explains. If a specialized canvas or large table legitimately needs two-dimensional exploration, provide navigational aids and avoid forcing the entire page into simultaneous horizontal and vertical scrolling.

## Failure Topology
- At high zoom, primary actions move beyond a clipped fixed-width container.
- A sticky header and cookie/banner stack consume most of the viewport and cannot be dismissed.
- Text reflows but floating icons and badges overlap the enlarged lines.
- A desktop three-column form becomes horizontally scrollable instead of stacking semantically.
- Modal minimum widths exceed the effective viewport and hide close/submit controls.
- Component-level overflow creates multiple nested horizontal scroll areas with no clear ownership.

## Falsification and Recovery
Exercise representative flows at multiple browser zoom levels, text scaling, narrow desktop windows, and mobile landscape. Inspect both reachability and reading order, including open dialogs, validation errors, autocomplete menus, and sticky regions. The design fails if a common task requires panning in two axes when the information itself is one-dimensional, or if fixed chrome obscures the active control.

Recover by removing hard minimum widths, converting visual columns to semantic stacks, bounding sticky surfaces, allowing text-driven growth, and assigning horizontal scrolling only to intrinsically two-dimensional content. Re-run with localized long strings because zoom and expansion failures compound.

## Output Contract
Return `zoom-reflow-contract` with effective-viewport thresholds, stack/wrap rules, permitted two-dimensional regions, sticky/overlay bounds, text-scaling behavior, overflow ownership, localized stress cases, and magnified-flow verification evidence.
