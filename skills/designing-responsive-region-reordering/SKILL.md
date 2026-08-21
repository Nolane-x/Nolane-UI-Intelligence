---
name: designing-responsive-region-reordering
description: Use when responsive composition changes the visual order of major regions and reading order, focus order, task sequence, and semantic relationships must remain coherent across layouts.
---

# Designing Responsive Region Reordering

## Order Has Semantics
Grid and flex tools can visually reorder content without changing source order. This skill owns the decision about when region order may change and how visual, reading, focus, and task order stay aligned enough to preserve meaning. It is not a generic accessibility checklist; it addresses responsive cross-state order transitions.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent authorizes responsive composition changes. This specialist governs region sequence when those changes alter apparent task structure.

## Order Ledger
For each composition state record visual order, DOM/source order, accessibility reading order, keyboard focus order, and task dependency order. Differences are allowed only with rationale. A secondary panel may move above content visually for visibility, but if its controls depend on a selection made below, task order may become contradictory.

Prefer source order that remains semantically valid in every mode and use layout for presentation. When impossible, consider conditional composition that preserves one coherent order rather than using CSS order to create two conflicting narratives.

## Evidence
Evidence includes screen-reader/reading traversal, keyboard focus sequence, screenshot comparison, task execution, and DOM inspection across transitions. Include stateful regions such as open filters, validation summaries, and sticky actions because their placement often changes in narrow modes.

## Failure Modes
Failure includes a visually first action reached last by keyboard, headings read after their controlled content, filters displayed before a context selector they depend on, and focus jumping to an unrelated region after breakpoint transition. Another failure is source order optimized for one layout but nonsensical when CSS fails.

## Falsification
Falsification navigates each responsive state without a pointer, disables layout CSS to inspect semantic source order, moves across the breakpoint while focus is inside a relocated region, and checks announcement sequence. Inconsistent task or reading sequence disproves the contract.

## Recovery
Recovery chooses a source order that expresses durable semantics, removes decorative reordering, or conditionally re-composes at a component boundary with explicit focus preservation. Avoid positive `tabindex` as a patch for visual/source disagreement.

## Output
Output: `responsive-region-reordering-contract` with per-state order ledger, allowed divergences, focus transition behavior, and traversal evidence.

## Handoff
Handoff decisions about hiding or summarizing regions to priority collapse; handoff low-level accessible reading semantics to relevant accessibility specialists.

## Sibling Boundary and delete-the-skill
Priority collapse decides presence/fidelity, not sequence. Generic responsive layout can rearrange boxes but lacks an owner for cross-modal ordering coherence. Removing this skill leaves that material decision unowned.