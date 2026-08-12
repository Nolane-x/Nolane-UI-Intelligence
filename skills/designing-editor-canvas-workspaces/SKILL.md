---
name: designing-editor-canvas-workspaces
description: Use when a UI supports visual, code, document, diagram, media, layout, CAD-like, node, timeline, map, or creative editing with selection, tools, canvas navigation, inspectors, direct manipulation, modes, and history.
---

# Designing Editor and Canvas Workspaces

## Overview
Editors are state-rich environments built around a stable object model, selection, tool/mode semantics, and reversible history. The UI should let users manipulate complex artifacts without losing where they are or what will be affected.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require artifact/object model, selection granularity, direct manipulation operations, tool/mode set, history semantics, collaboration/AI involvement, zoom/pan, keyboard needs, and persistence. Coordinate with desktop, drag-drop, and keyboard faculties as applicable.

## Decision Model
Define selection before tools. Single/multi/range/group/nested selection determines inspector content, commands, copy/paste, drag, and history. Visually separate hover target, focused control, selected object, active tool, and locked/read-only state.

Choose mode architecture deliberately. Temporary modes (space-to-pan), persistent tools (pen), modal contexts (crop), and object-specific inspectors need visible state and predictable escape. Avoid hidden modes where the same gesture changes meaning without a strong indicator.

Canvas navigation — pan, zoom, fit, center, minimap — must preserve spatial orientation. Zoom should anchor to pointer/focus or selected object according to convention. Infinite canvas needs origin/scale cues and recovery when users become “lost.”

History is a contract, not a button. Define atomic action boundaries, grouping, undo/redo across selection versus content, external/AI operations, collaboration, and irreversible side effects. AI-generated edits should create a stable checkpoint/diff rather than mutate history opaquely.

Inspector/toolbars show controls relevant to selection but keep command discoverability beyond pointer hover. Direct manipulation needs constraints/snapping feedback and numeric alternative for precision/accessibility.

## Evidence
Test complex selection, nested objects, undo/redo around batch/AI operations, mode escape, accidental drag, zoom at extremes, offscreen/lost canvas recovery, keyboard commands, screen-reader/alternative representation where in scope, collaborative edits, and persistence after reload.

## Output Contract
Return an `editor-workspace-contract` with `object_model`, `selection_states`, `tool_and_mode_model`, `canvas_navigation`, `direct_manipulation`, `inspector_binding`, `snapping_constraints`, `history_model`, `ai_collaboration_checkpoints`, `precision_alternatives`, and `editor_tests[]`.

## Failure Traps
- Hover, focus, selection, and active tool all styled the same.
- Hidden persistent mode causing unexpected edits.
- Undo skips AI changes because they were “background.”
- Zoom/pan loses the selected object with no recovery.
- Drag is the only precision placement method.
- Inspector silently edits multiple selected objects inconsistently.
- One giant component owns canvas, toolbar, inspector, and history state.

An editor feels powerful when state complexity is visible and reversible rather than mysterious.