---
name: designing-responsive-panel-docking
description: Adapt docked inspectors, utility panels, and secondary work regions across space constraints while preserving workspace context and panel state.
---

# Designing responsive panel docking

Professional interfaces often rely on side panels that cannot remain permanently docked on small windows. Use this skill when inspectors, layers, properties, chat, help, or detail panels must dock, overlay, collapse, or move.

## Decision ownership

Own docking states, trigger conditions, panel size constraints, overlay behavior, persistence, resize handles, and interaction with the primary workspace. Decide which panels may coexist and which become mutually exclusive under constraint.

## Inputs and evidence

Collect minimum primary-canvas size, panel preferred/min/max widths, user-resized sizes, panel open state, multi-panel combinations, keyboard shortcuts, touch usage, and content that requires persistent comparison. Observe whether overlays obscure the exact object users need to inspect.

## Procedure

Define docked, collapsed, overlay, and hidden states with explicit transitions. Preserve panel identity, selected tab, scroll position, and user size preferences where appropriate. When switching to overlay, provide clear dismissal and avoid covering the invoking control without a return path.

Coordinate multiple panels through workspace-level policy rather than independent breakpoints. Reserve sufficient primary-area size so panels cannot squeeze the work surface below usability. If user resizing is supported, clamp responsibly and remember values per suitable scope.

## Failure topology

Independent side panels can collectively consume the entire workspace. Responsive remounting loses inspector state. Overlay panels can obscure the selected canvas object and force repeated open-close cycles.

Another failure is persisting a desktop panel width into a narrow window, producing immediate overflow after restore.

## Falsification

Open multiple panels, resize through all states, and verify state continuity. Restore sessions at radically different window sizes. Test focus, Escape, shortcuts, drag-resize, and screen-reader landmarks. Measure the remaining primary work area at each allowed combination.

If users must close a panel to see the target it describes, evaluate alternate placement or coordinated resizing.

## Output contract

Produce a `responsive-panel-docking-contract` with panel states, workspace constraints, coexistence rules, sizing and persistence, overlay semantics, focus/dismissal behavior, state retention, and session-restore tests.

## Handoffs

Use `designing-multi-panel-workspaces` for desktop orchestration, `designing-responsive-sidebar-behavior` for navigation sidebars, `designing-responsive-canvas-workspaces` for canvas constraints, and `verifying-responsive-state-parity` for panel functionality.