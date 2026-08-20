---
name: designing-virtual-keyboard-avoidance
description: Use when a mobile on-screen keyboard changes usable geometry and a form, chat, editor, picker, or bottom action must preserve focused input, context, and reachable controls without unstable jumps.
---

# Designing Virtual Keyboard Avoidance

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This owner handles the geometry and interaction consequences of an IME/virtual keyboard. It does not decide field semantics or form validation. Its responsibility is to keep the focused editing task understandable and operable while keyboard height, accessory rows, prediction surfaces, floating keyboards, hardware keyboard attachment, and window resizing vary.

## Decision model

Start from the focused element and the minimum context needed to edit it safely. Decide whether the platform resizes the app window, overlays content, exposes animation/inset progress, or leaves avoidance to the application. Choose one authoritative geometry path; combining automatic OS resize, safe-area padding and custom translation often produces triple compensation.

Classify surfaces. A conventional scrollable form usually needs scroll-to-visible with context retained. A chat composer may stay docked above the keyboard while the conversation preserves its bottom anchor. A code/editor canvas may need viewport pan without changing document coordinates. A bottom sheet can change detent or internal scroll region. Do not apply one keyboard-avoidance primitive to every screen.

Preserve user intent through keyboard transitions. Opening the keyboard should not reset scroll position, dismiss selections, close necessary autocomplete, or trigger layout animations that move the field after the user's finger arrives. Closing it should return to a stable viewport rather than an old stale offset. If focus advances to the next field, compute visibility after the new field becomes authoritative.

Account for IME composition and accessory controls. East Asian composition, dictation, emoji/picker keyboards and password/autofill UI can alter height and timing. A hardware keyboard may reduce or remove software keyboard geometry while focus remains active. Treat keyboard visibility as an observed capability state, not a synonym for text-field focus.

## Evidence

Collect platform keyboard/inset APIs, animation timing traces, representative forms and editors, long localized labels, multiline inputs, autocomplete menus, landscape/split window, hardware keyboard, floating keyboard where supported, and accessibility zoom/font settings. Record the focused control's visible rect before, during and after transition.

## Failure topology

Common failures are a submit button hidden behind the IME; an app translated upward so the navigation header disappears; nested scroll views fighting over scroll-to-visible; chat history jumping when the keyboard animates; a dropdown positioned using pre-keyboard coordinates; keyboard dismissal losing an unsaved composition; and a layout that works with the default Latin keyboard but fails with taller prediction or handwriting surfaces.

## Falsification

Focus every field near viewport edges, switch keyboard types, rotate while editing, open autocomplete, move between multiline and single-line fields, attach/detach hardware keyboard and dismiss interactively. The contract fails if the insertion point or required context becomes obscured, if geometry oscillates, if content jumps after animation settles, or if IME composition is committed/cancelled by an avoidance side effect.

## Recovery

Remove duplicate geometry authorities, anchor adaptation to current insets and focused rect, and give each surface one scroll/pan owner. Preserve logical scroll anchors rather than raw pixel offsets when container height changes. Delay optional decorative transitions until the keyboard state is stable; never delay the actual focused-control visibility needed for typing.

## Output contract

Return a `virtual-keyboard-avoidance-contract` with keyboard geometry source, surface classification, focus-visibility rule, scroll/pan owner, docked-control behavior, animation synchronization, IME/composition considerations, hardware/floating keyboard states, dismissal behavior, and verification matrix.

## Handoffs

Use `designing-mobile-safe-area-integration` for system-edge geometry, form and editor owners for semantic editing behavior, `designing-comboboxes-and-autocomplete` for popup semantics, and accessibility focus/zoom owners when enlarged content changes visibility constraints.