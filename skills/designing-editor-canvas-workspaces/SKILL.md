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

## V6 Editor/Canvas Workspace Protocol
Maintain **infinite-canvas coordinate truth** across world coordinates, viewport transforms, zoom, snapping, guides, minimap, and exported geometry. Use **zoom-level semantic scaling** so labels/handles/details appear at useful thresholds without changing object meaning.

Preserve **selection transform invariants** for multi-select, rotate/resize, grouped objects, locked items, and constraints. Integrate every mutation with **history-command integration** so undo/redo reflects semantic user actions rather than low-level pointer events. Provide a **canvas accessibility alternate**—structured object tree/list/properties/actions or other equivalent path—when pure spatial manipulation is inaccessible.

### Falsification
Zoom/pan deeply, transform grouped objects, undo complex gestures, reload, and complete a material action without canvas pointer manipulation. Geometry/history or accessibility mismatch falsifies the workspace.

### Recovery
Restore canonical world/object state, collapse low-level events into semantic commands, and provide structured alternate manipulation rather than adding keyboard emulation to raw drag coordinates.

## V9 Instrument Architecture
For tool-rich products, prove **instrument completeness** before composing panels. An editor is not “canvas + toolbar.” Build a capability-driven instrument architecture that considers, when the product semantics require them: global shell/orientation, object/document switching, modes, persistent and temporary tools, selection, context toolbar, **context inspector**, hierarchy/layers/object tree, canvas/timeline/work area, asset/resource discovery, command/search surface, history/undo-redo, zoom/navigation, status/progress, import/export/publish, comments/collaboration, version/history, help and preferences. Each instrument must trace to a capability; no category is mandatory merely because another editor has it.

Separate **canonical command ownership** from presentation. The same edit may be reachable from a toolbar, inspector, menu, shortcut, command palette or context action, but it remains one semantic command with one enabled/disabled/permission/history model. Frequent controls deserve direct reach; rare controls may use progressive disclosure. Completeness is preserved by reachability, not by showing every button simultaneously.

Bind instruments to context. Selection determines which inspector properties are meaningful; mode determines which tools and gestures are active; object/media type can change relevant controls; permission/read-only state removes mutation without erasing understandable status; timeline/canvas position changes spatial context without changing object identity. Avoid “panel dumping,” where many globally visible controls are technically complete but cognitively unrelated to the current work.

Treat **asset/resource** management as a workflow when the editor consumes media, components, templates, data, plugins or reusable objects. Model discovery, import, loading/progress, permission/licensing where relevant, placement, replacement, broken/missing resources, organization, recent/favorites and export linkage as required by the domain. A polished empty asset sidebar is not resource architecture.

For AI-assisted creative tools, AI is another instrument with explicit target, proposed change, preview/diff where material, commit semantics and history integration. AI must not bypass selection, permission, object model or undo merely because it operates from a chat/prompt surface.

### V9 Falsification
Hide the visual toolbar and reconstruct every meaningful edit capability from the command/instrument registry. Then hide all secondary panels and ask whether the primary work remains understandable. If essential operations exist only as icon placement, or if every panel must remain open for the product to feel complete, the instrument architecture is not coherent.

### V9 Recovery
Return to capability and command ownership, classify instruments by global/document/selection/mode/context scope, restore missing resource/history/status paths, then decide direct versus progressive disclosure. Do not fix incompleteness by adding more floating buttons around the canvas.
