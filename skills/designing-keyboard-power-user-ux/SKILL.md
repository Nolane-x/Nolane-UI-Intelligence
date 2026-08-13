---
name: designing-keyboard-power-user-ux
description: Use when a UI supports expert, desktop, editor, admin, developer, data-entry, accessibility, or repetitive workflows where commands, navigation, selection, or manipulation must be efficient without a pointer.
---

# Designing Keyboard Power-User UX

## Overview
Keyboard design is a command architecture, not a late list of shortcuts. Make every important action reachable, predictable, discoverable, conflict-safe, and able to return focus to the user’s working context.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require the command inventory, focus model, platform conventions, user expertise, and alternative-input needs. Do not invent shortcuts before command semantics are stable.

## Decision Model
Separate four layers. **Navigation** moves among meaningful regions and controls. **Selection** changes which object or range is targeted. **Command execution** acts on the selection or current context. **Text editing** follows platform-native conventions and must not be hijacked by global shortcuts.

Create a command registry with canonical action id, label, scope, shortcut, availability, destructive consequence, and conflict priority. Preserve standard platform shortcuts; add custom bindings only for frequent or domain-specific actions. Chords and sequences need discoverability and timeout semantics. Single-key shortcuts require caution when focus may be in text fields or assistive technology modes.

Model focus as state. Define entry, traversal, roving behavior where appropriate, modal containment, escape, and return after dialogs, menus, popovers, asynchronous refreshes, or route changes. Focus movement must follow logical operation, not merely DOM or visual order. When virtualized content unmounts, preserve a recoverable focus anchor.

Expose keyboard capability through menus, command palettes, contextual hints, shortcut reference, or visible labels. Allow remapping where platform/game conventions or accessibility make it valuable. Batch and repeated actions should support efficient selection without forcing hundreds of tab stops.

## Evidence
Test full workflows with pointer disconnected, standard platform shortcuts, screen-reader/Full Keyboard Access where applicable, focus-visible styling, text-field conflicts, modal escape, and focus restoration. Measure command discoverability for expert onboarding, not only execution speed after memorization.

## Output Contract
Return a `keyboard-contract` with `command_registry[]`, `navigation_regions[]`, `focus_graph`, `selection_model`, `shortcut_policy`, `conflict_rules[]`, `discovery_surfaces[]`, `remapping_policy`, `modal_focus_rules`, `async_focus_rules`, and `verification_scenarios[]`.

## Failure Traps
- Tab order as the entire keyboard strategy.
- Custom shortcuts that override copy, undo, browser, OS, or text-editing expectations.
- Focus disappearing after deletion or async refresh.
- Command palette that exposes actions but not their current availability or scope.
- Hundreds of individually tabbable cells where grid navigation is the proper model.
- Hidden single-key commands with destructive effects.
- Keyboard parity claimed from static linting without end-to-end operation.

A power-user interface should become faster as skill grows without becoming opaque or unusable to someone who has not memorized it.

## V6 Keyboard Power-User Protocol
Maintain a **shortcut namespace** by scope—global, workspace, editor, focused component, modal—so conflicts are predictable. Run a **chord conflict audit** against browser/OS/assistive technology/input-method shortcuts before claiming a binding.

Provide a **discoverability surface** such as menus, command palette, shortcut help, or contextual hints that reflects current availability. Preserve **focus-command coherence**: a command should act on the focus/selection/context users can infer, not a hidden stale target. Support **remapping support** where domain users/platform conventions make fixed bindings exclusionary.

### Falsification
Execute shortcuts across focus states, OS/browser conflicts, IME, and screen readers; open multiple workspaces/modals. If scope or target is ambiguous, the keyboard model fails.

### Recovery
Narrow scope, change conflicting chords, expose current target, and provide remapping or menu alternative without breaking semantic action identity.
