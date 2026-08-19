---
name: designing-resizable-panels
description: Use when a single panel or region can be resized and the design must define handles, constraints, aspect behavior, content reflow, persistence and accessible resizing without conflating resize with layout navigation.
---

# Designing Resizable Panels

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This specialist owns resizing of a bounded panel, inspector, floating region or embedded object. Multi-pane relationship is owned by `designing-split-pane-layouts`; object transforms belong to transform/manipulation skills.

## Decision Boundary
Define which edges/corners resize and why. A side inspector may resize only horizontally; a floating console may allow width and height; a media preview may preserve aspect ratio unless explicitly unlocked. Invisible resize zones can be wider than visual borders, but they must not steal nearby click/drag interactions.

Constraints must come from content and task. Minimum size should preserve the smallest coherent layout, not just avoid negative dimensions. Maximum size may protect the primary workspace. When the panel crosses internal responsive thresholds, content should reflow intentionally rather than overflow under the handle.

During drag, provide immediate geometry feedback. Expensive contents can temporarily simplify rendering, but the user must see actual bounds and final size. If resize is persisted, distinguish per-document, per-workspace and global preferences.

Keyboard resizing needs discoverable focus on the handle or a command/settings route. Screen-reader users need the resize relationship and current extent conveyed in a meaningful unit or relative state, not raw pixels when those have no task meaning.

## Failure Topology
- Resize hitbox overlaps buttons near the panel edge.
- Minimum width is smaller than the longest nonwrapping control, creating horizontal traps.
- Dragging a panel causes heavy charts/editors to rerender on every pixel and lag behind the pointer.
- Persisted size applies globally when different workspaces need different density.
- Corner handles imply free aspect resizing for media that must remain constrained.

## Falsification and Recovery
Resize from every enabled edge, move rapidly, cross internal breakpoints, zoom text, test keyboard/accessibility, restore on smaller display and use heavy content. The contract fails if the visible edge and interactive edge diverge materially or if final content is unreachable at an allowed size.

Recover by narrowing resize axes, deriving constraints from actual component minima, throttling expensive internal work without lagging outer geometry, and scoping persistence correctly.

## Output Contract
Return `resizable-panel-contract` with enabled handles, hit geometry, min/max/aspect constraints, live-resize behavior, internal reflow, keyboard/AT path, persistence scope and constrained-size tests.