---
name: designing-split-pane-layouts
description: Use when two or more work regions must remain simultaneously visible and users need a stable relationship between panes, dividers, minimum sizes, collapse behavior and responsive alternatives.
---

# Designing Split Pane Layouts

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns the structural interaction of simultaneously visible panes. It does not decide the information architecture inside each pane or the visual styling of the workspace shell.

## Decision Model
Begin with pane roles. A master/detail split, editor/preview split, code/terminal split and comparison split have different symmetry. Some panes are primary with a bounded auxiliary region; others are peers whose relative size is user-controlled. The divider behavior and default ratio should reflect that relationship.

Define sizing in semantic constraints, not only percentages: minimum readable width, minimum controls fit, optional maximum, preferred default and collapse threshold. A pane should never be resized into a technically nonzero but unusable sliver. When the viewport becomes too narrow, transform the composition deliberately—tabs, navigation stack, overlay panel or sequential view—while preserving task access.

The separator is an interaction target. Pointer drag, touch drag and keyboard resizing must map to the same bounds. Keyboard steps should allow both coarse and fine adjustment where precision matters. The separator needs a perceivable focus state and an accessible value/relationship where the platform pattern supports it.

Persistence is contextual. Remembering a user’s ratio can be useful for stable workspaces, but stale pixel sizes from a 4K monitor should not make a laptop unusable. Persist normalized or semantic intent and clamp on restore.

## Failure Topology
- A secondary pane can be shrunk until its controls clip but it never formally collapses.
- Resize handle is visually 1 px and effectively impossible to acquire.
- Keyboard users cannot resize or collapse the split.
- Responsive mode silently drops one pane’s capability.
- Restored size from another display pushes primary content offscreen.
- Nested splits create ambiguous handles and runaway minimum-width conflicts.

## Falsification and Recovery
Test minimum/maximum drag, keyboard resize, touch, nested splits, 200% text zoom, narrow viewport, orientation/display change and persisted restore. The design fails if both panes cannot reach a usable state or if a user cannot identify which divider controls which regions.

Recover by reducing nesting, defining semantic collapse states, expanding hit targets without changing visual weight, clamping persisted sizes and providing a sequential responsive alternative.

## Output Contract
Return `split-pane-layout-contract` with pane roles, size constraints, divider semantics, resize modalities, collapse/restore policy, responsive transformation, persistence strategy, nesting limits and usability tests.