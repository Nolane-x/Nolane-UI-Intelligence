---
name: critiquing-responsive-behavior
description: Use when an independent reviewer must verify that task priority, content, interaction, navigation, density, and hierarchy survive viewport, container, orientation, input, or content changes.
---

# Critiquing Responsive Behavior

## Overview
A responsive review is a task-preservation review across constraints, not a screenshot check at three standard widths.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Use the responsive contract and inspect target ranges/content stress states.

## Pressure tests
Review at widths just before/after each transformation, not only named device presets. Include:
- long translated text
- 200% zoom/reflow when applicable
- virtual keyboard/touch context
- empty/error/loading states
- maximum table/data values
- landscape/portrait when supported
- reduced available container due to side panels/embedding

## Preserve invariants
At each state verify:
- current object/location is identifiable
- primary task remains reachable
- critical status/error remains visible
- interactions remain operable by available modality
- content order remains meaningful
- no hidden control becomes the only path
- data comparison relationships are intentionally transformed, not accidentally lost

## Overflow diagnosis
Distinguish acceptable intrinsic two-dimensional scrolling (large table/canvas) from accidental page overflow. Identify the owning scroll region and keyboard/focus implications.

## Touch vs compactness
A compact desktop layout can remain information-dense on mobile, but hit areas/gesture affordance must adapt. Flag invisible hover-only controls and targets packed too tightly to operate reliably.

## Output
Return typed findings with exact pressure condition, broken invariant, evidence, and recommended transformation—not merely “fix mobile spacing.”
