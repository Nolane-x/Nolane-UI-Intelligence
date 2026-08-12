---
name: adapting-responsive-layouts
description: Use when a UI must preserve task priority, content integrity, navigation, interaction, and visual hierarchy across changing viewport, container, input, or content conditions.
---

# Adapting Responsive Layouts

## Overview
Responsive design is semantic adaptation under constrained space, not a desktop screenshot squeezed through breakpoints.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume hierarchy, composition, navigation, component states, density, platform, and content stress cases.

## Start with invariants
Write what must survive adaptation:
- primary task/action
- object/context identity
- critical status/errors
- required comparison relationships
- safe destructive behavior
- keyboard/touch access
- readable content order

Then decide what can transform, collapse, reorder, scroll, paginate, summarize, or move behind disclosure.

## Breakpoints from pressure
Choose transitions where the current composition fails because of content geometry or interaction—not because a device list says 768/1024. A table may need a different transformation than the surrounding shell at the same width.

Use container-aware reasoning when a component can appear in multiple pane sizes.

## Transformation strategies
- stack/reorder by priority
- collapse navigation into explicit disclosure while preserving location
- switch master/detail into back-stack
- convert dense side inspector into sheet/drawer
- preserve table as horizontal scroll when comparison requires columns; do not automatically turn every table into unrelated cards
- summarize secondary metadata with access to detail
- reduce nonessential decoration before reducing legibility or targets

## Mobile is not narrow desktop
Account for touch, safe areas, one-handed reach where relevant, virtual keyboard, browser chrome, gesture conflicts, orientation, and limited hover.

## Content stress
Verify short/long labels, localization expansion, empty/loading/error, maximum values, and zoom/reflow. Breakpoints that work only for English demo data are invalid.

## Density preservation
Responsive does not always mean more whitespace. Expert mobile/compact tools may need dense but touch-safe presentation. Separate visual density from target hit area.

## Responsive typography/media
Adjust type and media based on hierarchy/measure, not arbitrary scaling. Preserve focal point and meaningful crop. Do not shrink screenshots/diagrams until labels become unreadable; use detail views, scroll, or alternative representation.

## Output: `responsive-contract`
Return `invariants`, `pressure_points`, `transformations`, `container_rules`, `navigation_changes`, `data_density_strategy`, `touch_changes`, `content_stress`, `media_behavior`, `test_matrix`, and `unsupported_ranges`.

## Gate
For each target range, users must still be able to locate context, complete critical tasks, understand feedback, and recover. If a capability disappears, the contract must explicitly permit it.
