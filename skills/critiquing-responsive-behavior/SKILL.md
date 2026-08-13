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

## Output: `finding-set`
Return typed findings with exact pressure condition, broken invariant, evidence, and recommended transformation—not merely “fix mobile spacing.”

## V6 Responsive Critic Court
Perform a **breakpoint discontinuity scan** by resizing continuously and recording abrupt jumps in order, visibility, focus, scroll position, control semantics, chart encoding, or content density. Named breakpoints are implementation details; the critic cares about behavioral discontinuities.

Run a **relationship-loss test** against the responsive relationship map: does an action drift away from its object, a label lose its value, comparison columns become incomparable, or navigation lose orientation? Execute a **capability-parity audit** so alternate mobile/compact representations preserve material actions, status, recovery, and information even when access mechanisms differ.

Use **zoom-reflow stress** at browser/text zoom and OS scaling, including 200% and higher where applicable, with long localized content. Add an **orientation-transition probe** during active editing, media, drag, selection, modal state, and async progress; state must survive layout transformation.

### Falsification
Choose widths just before/after every major structural transition and inject worst-case content. If the design only passes curated device widths, the responsive claim is false.

### Recovery
Return defects to responsive layout ownership with the exact lost relationship/capability, not a vague “mobile looks broken.” Block completion when task-critical parity is missing.
