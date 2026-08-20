---
name: designing-mobile-native-application-shells
description: Use when a mobile product must coordinate native navigation, system chrome, safe areas, keyboard, lifecycle, deep links, privacy, gestures, and platform-owned surfaces as one coherent application shell.
---

# Designing Mobile-Native Application Shells

## Parent Contract

**Required parent:** `adapting-platform-conventions`.

This owner governs the application-level contract that makes a phone or tablet product behave like a native citizen rather than a responsive web page wrapped in a device frame. It does not replace specialist owners for individual navigation stacks, keyboards, safe areas, deep links, restoration, share intents, privacy snapshots, or gesture conflicts. It decides how those mechanisms compose, which state belongs to the application shell, and what must survive transitions between app, operating system, and external destinations.

## Decision ownership

A mobile shell has several simultaneous authorities: the application route graph, the operating system's foreground/background lifecycle, window and inset geometry, system navigation conventions, permission and intent boundaries, and the user's current task state. Define a shell state model that distinguishes at least cold launch, warm launch, active foreground, temporarily inactive, backgrounded, suspended/terminated, resumed from external intent, and restored after process recreation where the platform supports those states.

Decide which state is durable, reconstructible, sensitive, or disposable. A selected tab may be safe to restore; a half-entered medical identifier may require product-specific privacy treatment; an in-flight payment authorization cannot be guessed from a cached UI state. Define the authority that resolves conflicts when a deep link arrives while a modal is open, when authentication expires in background, when a device rotates or changes window size, or when an operating-system surface temporarily covers the app.

The shell also owns the relationship between app chrome and system chrome. Status/navigation bars, home indicators, notches, dynamic islands/cutouts, edge-to-edge content, system gestures, keyboard and share/picker surfaces are not decoration. The shell must define where content may extend, where controls must remain protected, and how visual appearance follows platform capabilities without hiding system affordances.

## Evidence to collect

Use platform lifecycle/navigation guidance, actual device and emulator traces, product route diagrams, representative authenticated and anonymous sessions, deep-link targets, privacy classification, keyboard-heavy screens, orientation/window-size changes, and accessibility services. Capture transitions rather than screenshots alone. Evidence should include at least one interrupted flow, one background/restore path, one external intent return, and one system-owned surface such as share, picker, permission, or authentication UI.

## Failure topology

A mobile shell fails when it treats navigation state as the whole application state; when process death returns users to a visually plausible but semantically stale screen; when a backgrounded session leaks sensitive content through the app switcher; when safe-area padding is applied globally and creates double insets inside native containers; when system back behavior contradicts the visible hierarchy; when a deep link bypasses required initialization; or when keyboard/system gesture regions make primary controls unreachable.

Another class of failure is false continuity. Restoring a screen without revalidating permissions, identity, network-backed objects, or transactional status can be more dangerous than starting fresh. Conversely, discarding every draft on a routine interruption teaches users that mobile multitasking is unsafe.

## Falsification

Exercise the same task through cold launch, warm resume, background for short and long intervals, process recreation, deep link, notification entry, orientation/window change, keyboard appearance, app-switcher exposure, and OS back/home gestures. The shell contract is falsified if the user cannot explain where they are after a transition, if stale state is presented as current truth, if an external entry bypasses a required gate, if sensitive content is exposed outside the active app, or if state recovery depends on a navigation library's incidental serialization rather than an explicit product decision.

## Recovery

When shell behavior fails, first re-establish authoritative state: identity/session, route intent, durable product objects, and transaction status. Reconstruct presentation from those authorities instead of replaying stale component state. If a transition cannot be safely restored, use a truthful recovery surface that explains what was preserved and what must be resumed. Remove global inset/gesture assumptions and move them to the boundary that actually owns the geometry.

## Output contract

Return a `mobile-native-application-shells-contract` containing lifecycle states, launch/resume decision table, route ownership, durable-versus-ephemeral state classes, system-chrome policy, inset ownership, external-intent entry rules, privacy snapshot policy, gesture/back expectations, restoration checkpoints, unsupported transitions, and device-level verification scenarios.

## Handoffs

Delegate stack history to `designing-native-navigation-stacks`, tab preservation to `designing-tab-bar-state-continuity`, safe-area geometry to `designing-mobile-safe-area-integration`, keyboard behavior to `designing-virtual-keyboard-avoidance`, external URLs to `designing-mobile-deep-link-routing`, process recreation to `designing-app-lifecycle-state-restoration`, OS sharing to `designing-native-share-sheet-intents`, switcher redaction to `designing-mobile-app-switcher-privacy`, and gesture collisions to `designing-mobile-gesture-navigation-conflicts`. Use authentication, permissions, offline, and high-stakes owners when those authorities materially constrain the shell.