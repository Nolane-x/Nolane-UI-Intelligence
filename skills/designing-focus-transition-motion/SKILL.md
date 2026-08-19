---
name: designing-focus-transition-motion
description: Use when visible keyboard or assistive-technology focus moves through an interface and motion could clarify continuity, spatial position or focus ownership without delaying or obscuring the focus indicator.
---

# Designing Focus Transition Motion

## Parent Contract
**Required parent:** `designing-motion`. Semantic focus order and focus management remain owned by accessibility and interaction faculties.

## Decision Boundary
This skill owns the temporal treatment of **already-correct focus movement**. It never authorizes moving DOM focus merely to make an animation look continuous. A visible focus indicator must reflect the actual actionable target at every moment; decorative interpolation may bridge positions, but it cannot create a temporary fictional target.

Use motion only when it adds orientation. In a segmented control or toolbar, a shared focus halo can help users track directional movement. Across distant regions, however, animating a ring through unrelated controls may falsely imply a traversal path. When focus enters a dialog, disclosure, virtualized grid or newly mounted region, prioritize immediate visibility and scroll positioning over flourish.

Separate `focus`, `focus-visible`, `selection` and `active/pressed`. A keyboard user should not see a selected tab lose its selected appearance merely because focus moved elsewhere. When focus moves because content is removed, restored or programmatically redirected, the temporal treatment should communicate continuity without concealing the cause.

Scroll-to-focus and focus-ring motion must coordinate. Avoid a ring animating to coordinates that are themselves moving under scroll. Under reduced motion, snap the indicator to the new target while preserving strong contrast and shape.

## Failure Topology
- The focus ring arrives after DOM focus, leaving a period where assistive technology and sighted keyboard feedback disagree.
- A shared animated outline crosses unrelated controls and suggests a false relationship.
- Focus movement triggers smooth scrolling that causes vestibular discomfort or hides the target under sticky chrome.
- Virtualization destroys the old node and the animation targets stale geometry.
- Focus, selected and hover visuals collapse into one color treatment.

## Falsification and Recovery
Navigate rapidly with Tab, arrows and Shift+Tab; hold a navigation key in a composite widget; open/close a modal; delete the focused item; trigger validation focus; test zoom and reduced motion. If visible focus ever lags actual focus enough to misidentify the active element, disable interpolation for that transition.

Recover by making focus state instantaneous, then layering optional spatial continuity on top of stable geometry. For dynamic lists, key focus identity to semantic item IDs rather than DOM instance coordinates.

## Output Contract
Return `focus-transition-motion-contract` containing focus contexts, semantic target identity, indicator behavior, scroll coordination, dynamic-content rules, state-separation matrix, reduced-motion equivalent and verification scenarios.