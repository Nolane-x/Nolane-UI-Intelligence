---
name: designing-remote-control-navigation
description: Use when a TV, console, set-top box, kiosk, or couch-distance interface is controlled by a limited remote and navigation must map sparse buttons, long-press behavior, back semantics, paging, focus memory, and accessibility expectations into predictable movement.
---

# Designing Remote-Control Navigation

## Sparse input changes the whole command model
A remote may provide only directional keys, select, back, home, play/pause, volume, channel, and a few platform-specific buttons. There is no pointer fallback and often no text keyboard. This skill owns the command semantics that turn that sparse device into a complete navigation model without overloading buttons differently from screen to screen.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent activates this specialist when remote-first interaction is material. Directional focus topology is delegated to `designing-directional-focus-graphs`; this skill owns command mapping and navigation conventions around that graph.

## Command vocabulary
Define stable meanings for directional move, activate/select, back, home/root, page/rail advance, context/options, media controls, and long-press where supported. The decision owner is whether a button performs local navigation, exits a region, dismisses an overlay, or delegates to the platform. Back behavior deserves explicit hierarchy: close transient overlay, leave detail, return to prior route, then exit only according to platform convention.

Do not hide essential actions behind a long-press unless the platform makes it discoverable and there is a fallback. Button hints should reflect the currently connected remote and its labels. If the device lacks a dedicated control assumed by the design, the interface needs an alternate reachable command.

## Long-range movement
Ten-foot UIs often contain long rails and grids. Repeated key presses need acceleration or paging only when movement remains predictable and focus never outruns visible context. Holding Right should not skip a selected item after the user releases. Define repeat rate ownership at the input layer and visual scroll/focus coupling at the UI layer.

## Back and escape semantics
Back is a safety valve. It should undo navigation depth before destructive app exit and should not silently discard unsaved work. In multi-pane interfaces, distinguish focus-region exit from route back. If a modal traps focus, Back may dismiss it only when dismissal is allowed by the underlying task contract.

## Evidence
Evidence includes physical-device or representative remote traces, button-to-command mappings, back-stack scenarios, long-press/repeat behavior, missing-button fallbacks, and screen-reader/voice coexistence where supported. Test from cold start, nested overlays, deep navigation, and interrupted media playback.

## Failure modes
Characteristic Failure includes Back exiting the app from a modal, Select triggering different semantic actions in visually similar cards, inaccessible actions requiring colored or platform-specific buttons, key-repeat causing focus to skip unpredictably, and button hints that show keyboard keys on a TV. Another failure is remote deadlock: a screen is visually complete but an essential action cannot be reached with the available command set.

## Falsification
Remove optional buttons from the simulated remote, hold directional keys, nest overlays, navigate deeply, and attempt every critical task with only the minimal command set. The contract fails if navigation depends on undocumented hardware, if Back semantics are inconsistent, if a repeated input outruns context, or if a critical action becomes unreachable.

## Recovery
When a device-specific button is missing, map the function to an accessible on-screen control or standard command rather than inventing a hidden gesture. For back-stack defects, reconstruct the navigation hierarchy and separate overlay dismissal from route history. Preserve focus memory when recovering from unexpected exits or route resets.

## Output and Handoff
Output: `remote-control-navigation-contract`, containing command vocabulary, back hierarchy, repeat/long-press policy, platform delegation, fallback controls, and evidence. Handoff adjacency to directional focus graphs and device-specific prompt rendering to input-device prompt switching.

## Sibling Boundary and delete-the-skill
Sibling directional focus graphs decide where focus moves spatially; this skill decides what a remote command means and how navigation depth behaves. Controller remapping owns user customization, not default remote semantics. The delete-the-skill test passes because without a remote-command owner, sparse input is handled as a reduced keyboard and essential platform/navigation semantics become inconsistent.