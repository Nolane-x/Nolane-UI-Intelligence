---
name: designing-desktop-windowed-workspaces
description: Use when designing desktop productivity, editor, professional, or long-session applications where resizable windows, multiple displays, menus, dense commands, keyboard/pointer precision, and persistent workspace state matter.
---

# Designing Desktop Windowed Workspaces

## Overview
Desktop is not a wide phone. Use space, precision, windows, menus, and persistent customization to support long-running work without forcing every task through nested modal screens.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require task frequency, command inventory, multi-document needs, supported desktop platforms, minimum window size, keyboard/pointer modalities, and persistence expectations. Coordinate with `designing-keyboard-power-user-ux` for command efficiency.

## Decision Model
Choose the workspace model first: single-document window, multi-document windows, tabbed document frame, inspector-based editor, dashboard/console, or hybrid. Decide what users benefit from seeing concurrently. Large screens should reduce unnecessary navigation depth, but not become a dumping ground for every panel.

Design windows as user-owned state. Specify minimum/ideal size, resize behavior, sidebars/inspectors that collapse or detach, full-screen behavior, multi-display placement, restoration after relaunch, and what happens when a monitor disappears. Preserve work context across active/inactive application transitions.

Use the platform command surface. Menus provide complete command reachability and discovery even when toolbars expose frequent actions. Toolbars are customizable accelerators, not the canonical registry. Context menus accelerate local operations but must not contain unique essential commands. Keyboard shortcuts and command palettes mirror the same semantic command ids.

Support precision. Desktop users expect fine selection, drag handles, hover previews, right-click/context operations, multi-select modifiers, and batch actions, but every essential operation still needs keyboard/accessibility support. Dense layouts need stable geometry and readable information hierarchy more than oversized touch spacing.

## Evidence
Test at minimum/large window sizes, multiple displays and display removal, keyboard-only, precision pointer, long labels/locales, saved workspace restoration, document switching, inactive/active transitions, and command consistency across menu/toolbar/context/shortcut surfaces.

## Output Contract
Return a `desktop-workspace-contract` with `workspace_model`, `window_types[]`, `resize_rules`, `multi_display_rules`, `persistent_workspace_state`, `command_registry_binding`, `menus`, `toolbars`, `sidebars_and_inspectors`, `selection_model`, `document_model`, and `desktop_tests[]`.

## Failure Traps
- Mobile bottom navigation stretched across a desktop app.
- Every secondary task forced into a full-screen route.
- Toolbar as the only command inventory.
- Fixed window size or layout that breaks under resize.
- Losing inspector/panel state every launch.
- Context-menu-only essential actions.
- Touch-sized emptiness that slows scanning in professional work.

A strong desktop UI lets users arrange the tool around the work rather than continually rearranging their work around the tool.

## V6 Windowed Workspace Protocol
Define a **window restoration contract** for size, position, monitor, workspace/object, tabs, unsaved state, and privacy-sensitive content after relaunch. Maintain **multiwindow object identity** so the same document/entity opened in multiple windows has consistent edit/conflict semantics.

Require **shortcut-menu parity**: critical keyboard shortcuts are discoverable and do not silently diverge from menu labels/enabled state. Specify **drag-between-window semantics** for objects/files/tabs, including copy vs move, permissions, cancellation, and target highlighting. Handle **monitor-density migration** across DPI/scaling/color profiles and window movement without geometry corruption or unreadable UI.

### Falsification
Open the same object twice, edit concurrently, move windows between displays, restore after crash, and perform keyboard/menu equivalents. Divergent state or inaccessible off-screen restoration falsifies the workspace model.

### Recovery
Re-anchor windows, reconcile object versions, centralize command state, and provide safe conflict handling rather than assuming one-window ownership.
