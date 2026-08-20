---
name: designing-interaction-specification-handoff
description: Use when design artifacts must communicate production interaction states, events, transitions, focus, keyboard, gestures, validation, loading, failure, recovery, and motion so code does not infer behavior from static frames.
---

# Designing Interaction Specification Handoff

Static design artifacts under-specify behavior. Interaction handoff must carry the state machine and event semantics that make controls function, including paths that prototypes often omit: keyboard, focus, loading, errors, interruption, cancellation, retry, and reduced motion.

## Parent Contract
**Required parent:** `designing-design-to-code-handoffs`.

The parent owns design-to-code translation. This skill owns behavior/state handoff into implementation; domain interaction owners remain authoritative for the actual behavior contract.

## State and Event Model
For each material interactive element identify states such as idle, hover where applicable, focus, pressed, selected, expanded, disabled, loading, success, validation error, system error, stale/conflict, and destructive confirmation according to domain. Do not force every component into the same state set; specify only meaningful states.

Bind transitions to events: pointer/touch, keyboard, gesture, input change, submit, async response, timeout, external update, route change, permission change, or cancel. Specify side effects and data mutations separately from visual motion. A prototype link from Frame A to B is not enough to determine backend mutation or accessibility focus.

## Focus and Accessibility
Record initial focus on opened dialogs/menus, focus trapping where appropriate, restoration target on close, keyboard commands, screen-reader announcements, accessible names, and live status behavior. Generated code should map these to production semantic components where available instead of recreating low-level ARIA behavior.

## Async and Recovery
Include loading/progress, optimistic versus confirmed state, retry/idempotency, cancellation, partial success, and stale revision. If the design lacks a failure state for a material network operation, mark the handoff incomplete rather than letting implementation invent one silently.

## Motion
Specify purpose and state relationship before duration/easing. Reduced-motion alternative should preserve the information conveyed by motion. Do not turn design-tool prototype animation settings into universal production timing without checking motion system authority.

## Evidence
Select representative controls including form submit, dialog, drag, async action, destructive action, and live update. Execute with mouse/touch/keyboard/screen reader where relevant and compare against the handed-off state transition table.

## Failure Modes
- Prototype frame links are treated as complete behavior spec.
- Keyboard/focus states vanish in generated code.
- Loading frame exists but failure/retry has no handoff.
- Visual “success” appears before server confirmation without optimistic semantics.
- Motion timing is copied while reduced-motion behavior is absent.
- Two design variants represent the same state with contradictory event rules.

## Falsification
Interrupt a material async action and repeat the same flow by keyboard. Falsify if implementation cannot derive recovery/focus behavior from the handoff or if generated state differs from what the domain contract specifies.

## Recovery
Build an explicit state/event transition table, route semantic components, add failure/cancellation and focus restoration, and bind motion to state meaning. Unknown behavior remains an implementation blocker instead of being filled by framework defaults.

## Handoff
Domain interactions still use their specialist owners; component identity uses `designing-component-mapping-to-code`; responsive state changes use `designing-responsive-intent-handoff`; drift inspection uses `designing-design-code-drift-review`.

## Output Contract
Return an `interaction-specification-handoff-contract` with `interactive_elements[]`, `state_sets`, `event_transitions[]`, `side_effects`, `focus_keyboard_rules`, `accessibility_announcements`, `async_recovery`, `motion_intent`, `execution_evidence[]`, and `recovery_actions[]`.