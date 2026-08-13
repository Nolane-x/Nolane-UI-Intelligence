---
name: evaluating-perceptual-diversity
description: Use when handling multi-screen or multi-workspace products to verify coherent diversity rather than template repetition or fragmented art direction.
---

# Evaluating Perceptual Diversity

## Parent Contract
**Required parent:** `gating-ui-completion`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own cross-surface perceptual diversity. Do not demand every screen look different; coherence remains a first-class requirement.

## Product Truth
Content can change while macro grammar remains identical: same chrome, title placement, micro labels, borders, table language, chart grammar, inspector and color mass. A contact sheet reveals repetition that component-level critique misses.

## Decision Model
Build one row per meaningful screen with `signature`, `dominant_geometry`, `density`, `main_visualization`, `surface_pattern`, `typographic_gesture`, `color_mass`, and `interaction_signature`. Inspect repeated combinations rather than single fields. Too little coherence indicates a fragmented product; too little diversity indicates template repetition. Seek coherent diversity: shared institutional DNA with task-specific spatial/visual forms. At high ambition, each major workspace should earn its dominant visual mechanism from its task/data, not inherit one shell mechanically.

## Evidence
Return workspace-visual-matrix, contact-sheet or equivalent rendered references when available, similarity findings, and explicit coherence/diversity rationale.

## Output Contract: `workspace-visual-matrix`
Return the canonical `workspace-visual-matrix` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Maximal variation for its own sake; counting different copy as diversity; same three-pane shell everywhere; using color swaps as screen identity; breaking navigation conventions to create variety; evaluating screens independently without a contact-sheet view.
