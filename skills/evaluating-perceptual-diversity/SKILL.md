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

## V6 Cross-Surface Perceptual Diversity
Create a **screen-family signature** for each major surface family: dominant geometry, density, primary content/media, hierarchy gesture, color mass, surface treatment, signature mechanism, interaction cadence and spatial rhythm. Compare families, not screenshots in isolation.

Demand a **recurrence justification** for repeated structures. Repetition is valid when it supports learned navigation, shared task grammar, semantic consistency or brand recognition. Repetition is invalid when every feature is forced into the same sidebar + header + bordered panel template simply because the framework makes it cheap.

Generate a **template fingerprint** from recurring proportions, panel topology, card radius/border treatment, title placement, toolbar pattern, empty-state composition and visual accent. A product-wide fingerprint that overwhelms task-specific structure is a template attractor.

Judge **coherence-versus-repetition** explicitly. Coherence should live in tokens, interaction semantics, typography roles, icon grammar and recognizable signatures; composition may vary when tasks differ. Conversely, arbitrary layout novelty that destroys learned structure is not diversity.

Use qualitative **cross-surface entropy** to detect both cloned screens and gratuitous variety. Compare against the product's task families and experiential arc rather than an abstract optimum.

### Falsification
Blind navigation labels and compare unrelated feature screens. If they remain visually interchangeable despite materially different tasks, diversity is insufficient. Then compare related screens; if they become impossible to recognize as one product, coherence is insufficient.

### Recovery
For template repetition, redesign the screen family's primary task composition while preserving shared system grammar. For excess diversity, consolidate interaction and token semantics before flattening all layouts into one template.
