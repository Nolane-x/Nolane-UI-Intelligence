---
name: designing-container-query-layouts
description: Design component-local responsive behavior from the space a component actually receives, with stable query ownership and non-oscillating state transitions.
---

# Designing container-query layouts

Components reused in sidebars, cards, dashboards, modals, and full-width pages should not infer their available space from the viewport. Use this skill when local composition must adapt to its containing region.

## Decision ownership

Own which element establishes query containment, what dimensions or style signals may trigger variants, how nested query contexts interact, and which adaptations belong locally versus at the application shell. Decide whether a threshold changes geometry only or changes component semantics enough to require a higher-level owner.

## Inputs and evidence

Inventory every placement of the component, actual inline/block sizes, nested containers, min/max constraints, writing modes, zoom, dynamic side panels, and content lengths. Inspect component variants currently selected by viewport media queries even when the component occupies very different widths on the same screen.

## Procedure

Choose a stable containment boundary that corresponds to the region allocating space. Define query states from component pressure points: when labels wrap, controls collide, data loses scanability, or important actions can no longer remain inline. Keep query logic near the component that owns the adaptation.

Avoid feedback loops where a queried style changes the container dimension that determines the query, causing oscillation. Use containment and threshold hysteresis where necessary. For nested components, ensure child queries respond to the child’s assigned space rather than duplicating the parent’s breakpoints.

Document fallback behavior for environments or renderers without equivalent query support.

## Failure topology

Using the wrong container creates surprising behavior when intermediate wrappers change. Querying on thresholds copied from viewport breakpoints preserves device-centric thinking. Another failure is cyclic sizing: entering compact mode changes intrinsic width enough to re-enter expanded mode repeatedly.

Container queries can also fragment system behavior if every component invents arbitrary states without shared responsive principles.

## Falsification

Render the same component simultaneously in several container widths within one viewport. Resize only one container and verify siblings do not change. Stress nested containment, dynamic panel resizing, long content, and zoom. Instrument transitions around thresholds to detect rapid state flipping.

Remove a wrapper or change parent layout mode; if behavior changes without the component’s allocated space changing, containment ownership may be accidental.

## Output contract

Produce a `container-query-layouts-contract` specifying containment owners, queried axes or style features, threshold rationale, local layout states, anti-oscillation rules, nested-query behavior, fallback policy, and test cases across multiple simultaneous placements.

## Handoffs

Use `engineering-responsive-composition` for shell-level composition, `designing-content-driven-breakpoints` for deriving thresholds, `designing-responsive-priority-collapse` when content must be hidden or deferred, and `verifying-responsive-state-parity` to validate functional equivalence.