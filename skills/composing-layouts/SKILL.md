---
name: composing-layouts
description: Use when a UI needs an intentional spatial composition, grid, container model, section rhythm, alignment system, or relationship between content, controls, and media.
---

# Composing Layouts

## Overview
Layout is the geometry of meaning. Compose from content relationships, task flow, and visual thesis before choosing arbitrary columns or card grids.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume IA, hierarchy, aesthetic direction, density requirements, and responsive constraints.

## Establish the spatial grammar
Define:
- viewport/container behavior: fixed max width, fluid, full bleed, pane-based, canvas, split view
- primary grid: columns/tracks and gutters
- alignment anchors: edges/centers/baselines that repeated elements obey
- vertical rhythm: spacing relationships, not a pile of one-off margins
- major zones: navigation, work area, inspector, utility rail, contextual controls, media
- overlap/stacking rules if the direction uses layers

## Compose by relationships
Elements that users compare should align. Elements that form one decision should stay perceptually close. Elements with different semantic roles need enough spatial distinction to avoid false grouping.

Prefer whitespace and alignment over borders when containment is not semantically needed. Use bounded surfaces when they communicate object identity, interaction boundary, layering, or state.

## Container test
Before adding a card/panel ask:
1. Does the content represent one bounded object or interaction region?
2. Does the boundary help scanning, selection, drag/drop, or layering?
3. Would whitespace/grouping alone be clearer?
4. Is this creating a surface inside a surface inside a surface?

Nested framing is a cost: every border/radius/elevation introduces another hierarchy level.

## Section/page rhythm
For long surfaces vary scale, density, media ratio, alignment, and whitespace **without inventing unrelated component families**. Rhythm comes from controlled contrast within a coherent grammar.

For operational products prefer stable spatial memory: critical controls and repeated columns should not move merely to make each screen visually novel.

## Asymmetry
Asymmetry is useful when it expresses priority, direction, or brand character. It becomes noise when alignment relationships disappear. Preserve invisible anchors even in expressive compositions.

## Content-led dimensions
Do not fix heights around demo content unless the product requires it. Define min/max behavior, wrapping, truncation policy, scroll ownership, sticky regions, and overflow semantics.

## Scroll architecture
Decide who owns scroll: document, pane, table region, canvas, drawer. Multiple nested scroll regions require strong justification and clear focus/keyboard behavior.

## Output: `composition-contract`
Return `container_model`, `grid`, `anchors`, `zones`, `vertical_rhythm`, `containment_rules`, `scroll_ownership`, `sticky_rules`, `overflow_policy`, `section_rhythm`, `content_stress`, and `responsive_implications`.

## Common failures
- Centering everything by default.
- Large rounded wrapper around the entire app plus nested cards for every region.
- Arbitrary max-width that makes dense tables unusable.
- Using equal columns when one region is clearly primary.
- Fixed viewport-height sections that clip content or break zoom.
