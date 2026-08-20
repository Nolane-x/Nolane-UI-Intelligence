---
name: designing-bidirectional-layouts
description: Use when right-to-left and left-to-right reading systems require the interface's spatial flow, start/end alignment, panel order, and navigation progression to follow writing direction without blindly mirroring everything.
---

# Designing Bidirectional Layouts

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns layout-level directionality. It decides which spatial relationships follow inline/block direction, which remain physically anchored, and how responsive composition changes when the base document direction changes. It does not own mixed-direction text internals or icon-specific mirroring.

## Decision Boundary
Model positions using semantic start/end where meaning follows reading direction. Navigation progression, text alignment, disclosure flow, and many panel arrangements should adapt. Physical concepts such as compass directions, media timelines in some contexts, charts with conventional axes, hardware diagrams, and branded logos may remain unmirrored. Every exception needs product meaning, not a developer preference for left/right CSS properties.

Direction must propagate through overlays and portals. A menu rendered outside its trigger subtree still belongs to the same directional context. Responsive layouts should be re-evaluated rather than mechanically reversing desktop columns; mobile priority order may depend on task sequence more than visual mirroring. Scrolling and animation origins should match semantic direction where they communicate entry or progression.

## Failure Topology
- Main layout mirrors but portalled dialogs and menus remain LTR.
- Physical back/forward or navigation arrows point opposite the actual traversal semantics.
- A map legend, numeric axis, or media control is mirrored despite encoding physical/time meaning that should remain stable.
- CSS uses hard-coded left margins and floating badges overlap text in RTL.
- Desktop sidebars reverse correctly while mobile DOM/task order remains inconsistent.
- Direction changes at runtime but cached component geometry does not recompute.

## Falsification and Recovery
Render complete workflows in both directions, including menus, dialogs, tooltips, tables, forms, drawers, animations, and responsive states. Compare reading order, visual priority, pointer targets, and keyboard order. The design fails if mirroring changes task semantics or if LTR assumptions survive in nested/portalled surfaces.

Recover by replacing physical positioning with logical properties where appropriate, listing non-mirroring exceptions explicitly, propagating direction to overlays, and re-authoring responsive order around task sequence. Test with real RTL content rather than reversed English placeholders.

## Output Contract
Return `bidirectional-layout-contract` with directional regions, logical-property rules, physical/non-mirrored exceptions, overlay propagation, responsive order, animation/scroll deltas, runtime direction-change behavior, and paired LTR/RTL verification scenes.
