---
name: designing-product-tours
description: Use when a product needs an optional multi-stop orientation sequence that explains a small set of connected capabilities in context without hijacking navigation or pretending exposure equals learning.
---

# Designing Product Tours

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns ordered, multi-stop orientation across real product surfaces. A tour is not first-run initialization and is not a sequence of arbitrary tooltips. It should help users understand a coherent workflow or mental model after enough product context exists for the stops to mean something.

## Decision Boundary
Define one learning objective for the tour. “Show every feature” is not an objective. A useful tour might teach how work moves from inbox to case, how an editor’s canvas-inspector-history regions relate, or where account versus workspace settings live. Every stop must contribute to that model; remove stops that are merely promotional.

Bind stops to resilient semantic targets, not brittle CSS coordinates. Decide what happens when a target is absent because of permissions, responsive layout, feature flags, empty state, or product evolution. The tour can skip a nonessential stop, re-route to an equivalent target, or terminate with explanation; it must not trap users behind an overlay pointing at empty space.

Users own pacing. Provide clear Next/Back/Exit and preserve normal context enough that users can inspect what is being explained. Avoid automatically triggering destructive or expensive actions to demonstrate them. Completion means the tour sequence ended or was explicitly dismissed, not that the user mastered the feature; behavioral adoption needs separate evidence.

## Failure Topology
- Tour begins immediately on signup before the user knows what problem the product solves.
- Step target is hidden on mobile and the overlay points off-screen.
- Permission-limited users are blocked because the next highlighted control does not exist.
- Overlay disables the underlying interface so thoroughly that users cannot inspect the feature being explained.
- Closing a tour marks all features as learned and suppresses future contextual help.
- Product update moves a target and every downstream step becomes misaligned.

## Falsification and Recovery
Falsify with responsive breakpoints, missing permissions, feature flag disabled, target loaded asynchronously, browser zoom, keyboard/screen-reader navigation, user exiting at step two, returning later, and a route change during the tour. The design fails if progress depends on brittle visual coordinates or if exiting a voluntary tour blocks access to normal product use.

Recover by defining a narrow learning objective, resolving semantic targets at runtime, supporting skip/exit, adapting or omitting unavailable stops, keeping overlays non-destructive, and treating tour completion as exposure metadata rather than competence proof.

## Output Contract
Return `product-tour-contract` with learning objective, ordered stops, semantic target bindings, availability fallbacks, navigation/pacing controls, overlay interaction policy, exit/resume semantics, completion meaning, responsive/accessibility behavior, and falsification cases.