---
name: designing-responsive-region-reordering
description: Reorder interface regions across responsive states while preserving task logic, reading order, focus order, and state continuity.
---

# Designing responsive region reordering

Moving regions can preserve hierarchy when space changes, but visual order must not contradict semantic or keyboard order. Use this skill when sidebars become top sections, actions move below content, or secondary panels shift around a primary task.

## Decision ownership

Own whether reordering is justified, which order is canonical semantically, what may differ visually, and how focus/reading order remain coherent. Decide whether a region moves, duplicates, or is represented by a different control in another state.

## Inputs and evidence

Map task sequence, DOM or accessibility order, keyboard traversal, assistive-technology reading order, visual attention hierarchy, persistent state, and dependencies between regions. Observe users at several widths to see which information they need before acting.

## Procedure

Define a semantic order independent of layout coordinates. Prefer layout techniques that change visual placement without creating a misleading keyboard or reading sequence. If semantic order genuinely changes by context, restructure responsibly rather than relying only on CSS `order`.

When a region moves between containers, preserve its state identity so form input, selection, media playback, and scroll do not reset. Avoid rendering duplicate interactive controls solely to simplify layouts unless synchronization and accessibility are explicitly handled.

Provide orientation cues when a major region changes location across states.

## Failure topology

CSS visual reordering can make keyboard focus jump around the screen. Duplicate controls can receive conflicting state or duplicate accessible names. Moving a mounted subtree can reset uncontrolled input or virtualized scroll position.

A layout may also reorder based on visual aesthetics while breaking the cognitive sequence of review-then-action.

## Falsification

Traverse by keyboard and screen reader at every state and compare sequence with visual flow. Resize while focus is inside the moving region and verify focus remains meaningful. Enter unsaved data, resize, and ensure it persists. Inspect the accessibility tree for duplicate controls after responsive transformations.

Ask whether first-time users still encounter prerequisites before dependent actions.

## Output contract

Produce a `responsive-region-reordering-contract` containing semantic order, per-state visual order, focus/reading-order rules, movement or remount behavior, state-preservation requirements, duplication policy, orientation cues, and cross-state interaction tests.

## Handoffs

Use `engineering-responsive-composition` for overall state transitions, `designing-responsive-navigation-transitions` for navigation-specific reorderings, `designing-focus-order` for keyboard semantics, and `verifying-responsive-state-parity` for behavior after movement.