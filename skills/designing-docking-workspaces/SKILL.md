---
name: designing-docking-workspaces
description: Use when professional tools let users dock, tab, split, float or rearrange panels and the workspace needs predictable drop zones, layout persistence, recovery and keyboard-accessible alternatives.
---

# Designing Docking Workspaces

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns spatial composition of movable workspace panels. It does not decide the panel contents, command model or OS-level window management.

## Decision Model
Treat a docking layout as a tree of regions, tab groups, splits and optional floating windows, not a pile of absolute rectangles. Every panel has identity, allowable docking roles, minimum size, visibility state and restoration metadata. Some panels may be singleton tools; others may have multiple document instances.

Drag docking must preview the exact structural result before drop. Drop targets need sufficient size and unambiguous semantics: add as tab, split left/right/top/bottom, move to another group, or float. Avoid covering the entire workspace with competing target overlays. Pointer position alone should not commit a destructive restructuring without a visible preview.

Provide non-drag routes for arranging panels: commands such as move to group, dock left, reset layout, focus next panel or open panel. This is both accessibility and expert-workflow infrastructure.

Persistence needs versioning and recovery. Plugin removal, monitor topology changes and product upgrades can invalidate saved layouts. Preserve known panels, drop invalid references safely and always offer a reset/recover path rather than trapping the user in an offscreen or zero-size layout.

## Failure Topology
- Tiny drop zones make docking a precision game.
- Floating panels restore on a disconnected monitor.
- Closing a tab group accidentally closes documents rather than only the panel container.
- Saved layout schema breaks after an update with no migration/reset.
- Keyboard users can focus panels but cannot rearrange them.
- Drag preview shows tab insertion while drop creates a split.

## Falsification and Recovery
Rearrange nested splits, move between monitors, disconnect a display, remove a plugin panel, restore old layout version, use keyboard-only arrangement and reset. Serialize/deserialize repeatedly and ensure semantic panel identity survives.

Recover with a normalized layout tree, bounded docking targets, explicit document-vs-panel lifecycle, schema migration, display clamping and a safe default workspace.

## Output Contract
Return `docking-workspace-contract` with layout tree model, panel identities, docking actions/drop previews, keyboard commands, float/display policy, persistence schema, invalid-layout recovery and round-trip tests.