---
name: designing-mobile-safe-area-integration
description: Use when mobile content must coexist with notches, status/navigation bars, home indicators, rounded corners, dynamic cutouts, edge-to-edge layouts, and changing system insets without double padding or unreachable controls.
---

# Designing Mobile Safe Area Integration

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This skill owns inset geometry and edge-to-edge composition. It does not choose the overall responsive layout; it decides which region consumes which system inset, where visual material may extend behind system chrome, and where interactive or readable content must remain protected.

## Geometry model

Treat safe areas as dynamic environment inputs rather than fixed top/bottom padding tokens. Insets can change with orientation, window mode, call/navigation overlays, keyboard, platform navigation mode, cutout geometry, device posture, and system-bar visibility. Define an owner for each edge. If the outer shell consumes a bottom inset, a nested tab bar must not consume the same inset again unless it is intentionally drawing its own protected background.

Separate **background extension** from **content placement**. A photo, map, video, color field or decorative surface may extend edge to edge while labels and controls remain inset. Conversely, a full-screen immersive experience may intentionally place controls near edges but still needs hit-target protection from home/back gestures and cutouts. Do not encode the policy as one global `padding: safeArea` wrapper.

Scrollable regions require special treatment. The content inset, scroll indicator inset, sticky headers/footers, pull-to-refresh geometry and initial scroll offset should agree. Applying padding inside a virtualized list can change item measurement; applying external padding can hide the last item behind a floating bar. Specify which layer participates in scrolling and which remains chrome.

Landscape/tablet and split-window states may introduce lateral insets. Directionality and device rotation can change which physical edge is constrained; use platform-provided logical geometry and actual measured values instead of model-name tables.

## Evidence

Capture system inset values and rendered screenshots on representative devices/emulators: notch/cutout and non-cutout phones, gesture and button navigation where applicable, portrait/landscape, keyboard open/closed, tablet/multitasking, full-screen media and modal/sheet states. Evidence must show touch targets, not only background bounds.

## Failure topology

Double-applied safe areas create inexplicable whitespace and misalign app chrome. Ignored bottom insets place primary buttons under home indicators or system navigation. Fixed status-bar heights break on dynamic cutouts and accessibility display settings. A background that stops at the safe area exposes an unintended strip when the design expects edge-to-edge material. Another failure appears when keyboard insets are merged with safe-area insets by simple addition, pushing content far above the usable viewport.

## Falsification

Continuously rotate and resize supported windows while opening keyboard, sheets and system overlays. Inspect top/bottom/side controls and the last scrollable item. The contract fails if an inset is visibly consumed twice, if an actionable target overlaps a protected system gesture/cutout region, if scroll indicators disagree with content bounds, or if edge-to-edge visual intent changes unpredictably between devices with equivalent product state.

## Recovery

Trace each inset to one explicit consumer. Remove global compensating magic numbers, make background and content layers independent, and recompute geometry from current platform data after window/system changes. When a sticky control overlaps scrolled content, fix the scroll container's content/indicator inset or reserve space in the correct layer rather than inserting arbitrary spacer rows.

## Output contract

Return a `mobile-safe-area-integration-contract` with inset sources, per-edge consumers, background-extension policy, interactive protection zones, scroll-container behavior, sticky chrome rules, keyboard interaction, orientation/window deltas, full-screen exceptions, and device verification scenes.

## Handoffs

Use `designing-virtual-keyboard-avoidance` when IME geometry drives adaptation, `designing-mobile-gesture-navigation-conflicts` when protected edges compete with gestures, responsive owners for broader composition changes, and platform-specific guidance whenever the OS defines stronger behavior.