---
name: engineering-visual-legibility
description: Use when typography, density, expert-tool pressure, or responsive rendering can push text and glyphs below a protected legibility floor.
---

# Engineering Visual Legibility

## Parent Contract
**Required parent:** `crafting-typography`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own executable legibility evidence from rendered/computed styles and resolved font behavior. Do not choose the typographic personality; crafting-typography owns that.

## Product Truth
Expert user does not imply tiny text. Source CSS intent is weaker evidence than the browser's resolved result. A nominal font family that falls back on another machine is not a proven typeface decision.

## Decision Model
Apply a microtext budget: below 11px requires a semantic reason; below 10px cannot carry required information; below 9px is decorative/auxiliary only. Escalate compound risk when small text also has low contrast, uppercase transformation, or tracking. Audit computed styles rather than regex counts when browser evidence exists. For fonts capture intended family, actual resolved family, loading state, fallback visual delta, numeric metrics where critical, x-height/width considerations, glyph coverage, and CLS/layout-shift risk. Optimize expert density as a Pareto problem: information throughput, scanability, aesthetic hierarchy, and emotional power subject to a protected legibility floor.

## Evidence
Return representative computed samples across important roles/breakpoints plus resolved-font evidence. Required information under 10px is a blocking finding regardless of how technically sophisticated it looks.

## Output Contract: `visual-legibility-evidence`
Return the canonical `visual-legibility-evidence` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Using px grep as the only audit; expert⇒small; accepting 8px because it fits more data; low contrast + uppercase + tracking compounding; declaring a font choice from CSS stack only; fixing microtext by globally enlarging everything without rebalancing hierarchy.
