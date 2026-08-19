---
name: designing-modal-presentation-motion
description: Use when modal presentation or dismissal needs temporal hierarchy that marks an interruption, preserves focus/state truth and avoids turning a blocking task into spectacle.
---

# Designing Modal Presentation Motion

## Parent Contract
**Required parent:** `designing-motion`. Modal semantics, inertness, focus trap and decision safety belong to dialog/accessibility/high-stakes owners.

## Decision Boundary
This skill owns the temporal expression of a modal boundary: the point at which the previous surface becomes unavailable and the dialog becomes the active task context. Motion may reinforce that boundary, but it cannot define it. Semantic modality and focus must become correct independently of animation completion.

Classify the interruption. A lightweight confirmation can appear quickly with restrained scale/opacity. A task editor that visually originates from an object may use shared continuity if that helps users understand what is being edited. A critical alert should prioritize recognition and action over cinematic travel. Full-screen mobile modals may follow platform navigation conventions rather than desktop dialog motion.

Coordinate surface and backdrop deliberately. The backdrop exists to reduce competing attention and express inert context; large opacity pulses or blur transitions can be expensive and visually dominant. The dialog should not bounce after focus is ready, because moving focused controls undermines targeting.

Dismissal semantics differ by outcome. Cancel can visually return toward origin when one exists; successful completion may transition into changed underlying content. Destructive confirmation should not use celebratory motion. If validation blocks dismissal, do not play an exit and snap back.

## Failure Topology
- Focus enters the dialog while it is still scaled too small or offscreen.
- Background remains clickable during the entrance because modality waits for animation end.
- Closing animation runs after navigation already destroyed the origin, producing a jump.
- Spring overshoot moves buttons under the pointer.
- Backdrop blur causes frame drops that make the modal feel slower than the task.

## Falsification and Recovery
Open with keyboard, pointer and screen reader; press Escape during entrance; submit instantly; trigger validation; resize; remove the origin; throttle performance; enable reduced motion. The design fails if animation changes which controls are operable, makes focus visually ambiguous, or communicates the wrong task outcome.

Recover by establishing semantic modality immediately, reducing displacement, stabilizing focused geometry and choosing outcome-specific dismissal only where the causal relationship is real.

## Output Contract
Return `modal-presentation-motion-contract` containing interruption class, entrance/dismissal semantics, backdrop treatment, focus-timing constraints, outcome branches, interruption behavior, performance/reduced-motion fallbacks and runtime scenarios.