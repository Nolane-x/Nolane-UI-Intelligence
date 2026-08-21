---
name: designing-responsive-regression-matrices
description: Use when a surface changes structure, priority, navigation, density, or interaction across available space and verification needs a bounded matrix of widths, heights, container states, orientations, zoom, and content pressure rather than a few device screenshots.
---

# Designing Responsive Regression Matrices

## Responsive evidence is about mode transitions
Responsive correctness is not a list of popular device widths. The important defects appear where composition changes: a toolbar overflows, navigation changes mode, columns reorder, a table becomes cards, a pane disappears, or content pressure forces an earlier transition. This skill owns the evidence matrix for those structural boundaries.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent defines evidence binding. This specialist starts when a claim depends on adaptive composition across changing geometry or environmental constraints.

## Matrix axes
Build axes from actual responsive triggers: viewport width/height, container size, orientation, split-screen state, zoom/text scaling, safe-area insets, content length, pointer/touch modality where it affects layout, and platform chrome where relevant. The decision owner is the minimal set of boundary cases that exercises every responsive mode and transition.

For each admitted cell, record layout mode, visible regions, navigation mode, overflow policy, ordering, focus/reading order, and critical actions. Prefer values immediately before, at, and after a structural transition over arbitrary round numbers. Container-query systems require container-local evidence even when the viewport remains fixed.

## Content pressure as a first-class dimension
Responsive layouts often fail because fixture content is unrealistically short. Include long labels, translated strings, large numeric values, empty and dense states, validation messages, and user-generated content where those change pressure. The goal is not combinatorial explosion; admit content cases only when they can alter a layout decision or reveal clipping/overlap.

## Cross-mode continuity
Evidence should prove not just that each mode renders but that state survives the transition. Selection, scroll context, form values, expanded regions, and focus should remain coherent when the user resizes, rotates, docks a pane, or crosses a container threshold unless the product contract says otherwise.

## Evidence forms
Useful artifacts include screenshots at transition boundaries, DOM/layout geometry captures, interaction traces through a resize, accessibility/reading-order checks, and viewport/container metadata. Bind every artifact to the exact responsive mode and fixture. Device screenshots without geometry metadata are weak because they cannot reveal why the mode was selected.

## Failure modes
Characteristic Failure includes testing only canonical phone/tablet/desktop widths, missing height-constrained states, a visual reorder that disagrees with focus order, content overflow appearing only under localization, container components tested only full-page, and state lost when crossing a breakpoint. Another failure is duplicated device coverage that adds evidence volume without exercising a new transition.

## Falsification
Move each structural threshold by a small amount, expand labels, increase zoom, constrain height, place a component inside a narrow container on a wide viewport, and resize during an active interaction. The contract fails if a mode transition lacks evidence on both sides, if visual and semantic order diverge, if state resets without design intent, or if the matrix claims coverage from devices that never exercise the relevant mode.

## Recovery
Derive transitions from the current responsive contract, remove redundant device cells, add missing boundary/content cases, and recapture stale artifacts. If evidence reveals a new emergent mode, route it back to responsive design ownership rather than silently adding a one-off baseline.

## Output and Handoff
Output: `responsive-regression-matrices-contract`, containing responsive axes, structural modes, transition-boundary cells, content-pressure cases, continuity invariants, and evidence bindings. Handoff cross-browser differences to browser/device evidence matrices and image references to visual-regression baselines.

## Sibling Boundary and delete-the-skill
Sibling browser/device evidence owns implementation variance across engines and hardware. This skill owns geometry-driven mode coverage even in one engine. Component state matrices own semantic states independent of responsive mode. The delete-the-skill test passes because without it, “responsive tested” usually means a few screenshots that can miss every actual layout transition.