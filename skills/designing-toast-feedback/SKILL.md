---
name: designing-toast-feedback
description: Use when a product needs transient non-blocking acknowledgement for completed actions and must decide timing, stacking, action affordances, announcement, and escalation without losing important information.
---

# Designing Toast Feedback

## Parent Contract
**Required parent:** `designing-notifications-and-interruptions`.

This faculty owns short-lived feedback that confirms or reports a local event without becoming a durable notification queue. A toast is not appropriate for information the user must read later, a blocking decision, or an error whose recovery control disappears with the message.

## Decision Boundary
Classify the event by consequence. Routine success often needs no toast when the changed interface state is self-evident. Use transient feedback when causality would otherwise be unclear: background save completed, item copied, reversible deletion queued, export started, or action affected an off-screen object. High-impact failures should escalate to inline or persistent surfaces rather than vanish on a timer.

Timing must follow content and interaction. A toast containing an action such as Undo cannot expire so quickly that users cannot perceive and reach it, and hover/focus should not create unpredictable dismissal. Multiple toasts require a queue or coalescing policy; stacking ten nearly identical success messages is an interruption failure.

Accessibility announcements need restraint. Use appropriate live-region politeness and avoid re-announcing every trivial state change. Visual location should be consistent and avoid covering primary controls, virtual keyboards, or system safe areas.

## Failure Topology
- Every successful click creates a toast, turning routine use into notification noise.
- A destructive failure disappears automatically before the user can act.
- Undo expires while keyboard focus is still traveling toward the toast.
- Ten batch operations create ten stacked messages that obscure the workspace.
- Toast is visually visible but never announced to assistive technology, or an assertive live region interrupts continuously.
- Mobile toast overlaps a bottom navigation bar or software keyboard.

## Falsification and Recovery
Falsify with rapid repeated actions, screen-reader use, keyboard-only Undo, reduced motion, a narrow viewport with keyboard open, background events arriving while the tab is hidden, and errors requiring multi-step repair. The design fails if a transient lifetime can cause loss of necessary information or if users must watch the toast region to know whether ordinary actions worked.

Recover by eliminating redundant success messages, escalating durable/recoverable failures, coalescing repeated events, pausing interaction-sensitive expiry, binding Undo to the underlying reversible operation, and using bounded accessible announcements.

## Output Contract
Return `toast-feedback-contract` with eligible event classes, suppression/escalation rules, placement, lifetime policy, stack/coalescing behavior, action/Undo semantics, hover/focus treatment, live-region strategy, responsive safe areas, and falsification cases.