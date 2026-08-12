---
name: critiquing-visual-design
description: Use when an independent reviewer must identify perceptual, compositional, typographic, color, spacing, surface, imagery, or distinctiveness defects in a UI design or render.
---

# Critiquing Visual Design

## Overview
Judge whether the chosen visual direction is executed coherently and supports the product hierarchy. Do not redesign from personal taste.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Use the accepted aesthetic direction, hierarchy, craft contracts, and inspectable artifact.

## Review lenses
### Thesis fidelity
Can you see the selected visual thesis, or did implementation regress to generic defaults? Identify the specific missing signature or incompatible trope.

### Hierarchy
Name first/second/third focal points. Report competing emphasis, hidden primary actions, excessively loud status/decor, or flat equivalence.

### Composition
Check alignment anchors, container logic, proportion, whitespace grouping, scroll ownership, repetitive section formulas, and nested framing.

### Typography
Check role separation, line length, wrapping, weight/size relationships, control text, numerals, fallback, and whether typography actually carries the intended personality.

### Color/surface
Check semantic role, contrast intent, chroma budget, state distinguishability, dark-theme layering, and unjustified gradient/elevation.

### Rhythm/detail
Check repeated gaps, optical alignment, icon consistency, borders/radii/shadows, media crop, and edge treatment after macro issues are stable.

### Genericity
Use contextual anti-slop rules. A familiar pattern is not a defect by itself; report only when it lacks product/brand function or damages hierarchy.

## Evidence discipline
Each finding cites a visible region/state and a violated design contract/principle. “I don’t like the font” is not a finding. “Utility labels use the display face at nearly heading weight, collapsing role separation specified by typography contract” is.

## Output
Produce typed findings only. Include a `preserve` note when an existing strength would be easy to damage during repair. End with `BLOCK`, `REPAIR_AND_RETEST`, or `NO_VISUAL_BLOCKER_FOUND` for this lens only.
