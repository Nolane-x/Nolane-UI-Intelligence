---
name: designing-coach-marks
description: Use when one newly relevant control or behavior needs a brief contextual teaching cue and the product must decide trigger, target, dismissal, recurrence, and non-interference without launching a full tour.
---

# Designing Coach Marks

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns a single-context teaching intervention attached to one capability or affordance. A coach mark is not a product tour and should not become a serial overlay campaign. It is justified when the user has reached a moment where a useful capability is relevant but reasonably non-obvious.

## Decision Boundary
Trigger from product context, not calendar time or arbitrary visit count. Examples include first arrival at a new editor mode, first eligible use of a shortcut, or a newly released capability whose location changed. Do not interrupt a destructive confirmation, active text entry, time-critical workflow, or accessibility focus sequence merely because the trigger condition became true.

The target must exist, be visible, and remain semantically stable. If a responsive layout moves the action into an overflow menu, the coach mark either targets the discoverable entry point or defers. Positioning must avoid covering the target or essential adjacent content. Teach one action or mental model in concise copy and make the mark dismissible without requiring the advertised action.

Recurrence needs memory. Decide whether dismissal means never show again, postpone, or suppress until a materially changed version. If the user independently performs the taught action before the mark appears, mark the teaching objective satisfied rather than displaying redundant guidance later.

## Failure Topology
- Coach mark appears while the user is typing and steals focus.
- Responsive layout hides the target but the callout remains at stale coordinates.
- Dismissed mark returns on every login because suppression is stored only in component state.
- The only way to close the mark is to perform an action the user does not want.
- Product shows five coach marks simultaneously after a release and obscures the workspace.
- User already discovered the capability organically, yet onboarding telemetry still triggers the lesson.

## Falsification and Recovery
Falsify with target absent, target moved into overflow, keyboard-only use, screen reader, mobile viewport, user dismissing immediately, user performing the feature before trigger, multi-device preference sync, and a product update that materially changes the taught behavior. The design fails if guidance can block normal operation or recur despite evidence that the learning objective is already satisfied.

Recover by using context-qualified triggers, checking target availability immediately before display, never forcing the advertised action, persisting suppression/objective state, limiting concurrent marks, and versioning guidance when behavior changes.

## Output Contract
Return `coach-mark-contract` with teaching objective, contextual trigger, target resolution, display deferral, placement constraints, dismissal semantics, objective-satisfied detection, recurrence/version policy, focus/accessibility behavior, and falsification cases.