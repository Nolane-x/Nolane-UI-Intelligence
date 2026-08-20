---
name: designing-responsive-dialog-sizing
description: Adapt dialogs to available viewport and content constraints without trapping controls off-screen, breaking focus semantics, or disguising a full-screen task as a modal.
---

# Designing responsive dialog sizing

Dialogs that work on desktop can become unusable when the viewport is short, zoomed, or covered by a virtual keyboard. Use this skill when modal geometry and presentation must adapt responsively.

## Decision ownership

Own maximum/minimum dialog dimensions, internal scrolling, edge margins, full-screen transition criteria, header/footer persistence, and behavior under keyboard or browser UI occlusion. Decide when the task should stop being a dialog and become a page or sheet-like surface.

## Inputs and evidence

Collect worst-case content, localized titles/actions, forms and validation messages, viewport height/width, safe areas, virtual keyboard behavior, zoom, focus targets, and nested scroll regions. Observe whether important actions currently fall below the fold or multiple scroll containers compete.

## Procedure

Size dialogs from content needs constrained by available viewport, with explicit maximums and safe margins. Prefer one clearly owned scroll region; keep title, close affordance, and critical actions available when long content scrolls, but avoid sticky chrome that leaves too little content space.

At narrow widths, evaluate full-screen or edge-to-edge presentation if modal margins no longer convey meaningful context. Preserve modal semantics and focus containment through geometry changes. React to virtual keyboard occlusion without moving the focused input unpredictably.

## Failure topology

Fixed-height dialogs clip content. Nested scrolling makes wheel, touch, and keyboard navigation ambiguous. A full-screen mobile dialog may retain desktop close semantics while users expect back navigation, creating conflicting escape paths.

Aggressive centering can move the dialog every time content height changes, causing visual instability.

## Falsification

Test smallest supported viewport, large text, 400% zoom, long errors, and virtual keyboard. Navigate entirely by keyboard and assistive technology. Resize with focus near the footer and verify it remains visible or scrolls predictably. Inspect background scroll locking and focus restoration after close in every presentation state.

## Output contract

Produce a `responsive-dialog-sizing-contract` defining geometry constraints, presentation states, scroll ownership, persistent regions, full-screen criteria, keyboard/safe-area handling, focus and dismissal behavior, and edge-case tests.

## Handoffs

Use `designing-modal-dialogs` for base dialog semantics, `designing-bottom-sheet-motion` for sheet-specific motion, `designing-responsive-error-recovery` for modal error states, and `verifying-responsive-state-parity` for equivalent completion paths.