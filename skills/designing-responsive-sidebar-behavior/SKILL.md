---
name: designing-responsive-sidebar-behavior
description: Transform sidebars across widths while preserving hierarchy, selection, disclosure state, efficient access, and a clear relationship to primary content.
---

# Designing responsive sidebar behavior

A sidebar may be persistent, collapsed to icons, converted to a drawer, or temporarily hidden depending on available space and task priority. Use this skill to design those transformations as one coherent navigation or utility system.

## Decision ownership

Own sidebar presentation states, width and collapse thresholds, icon-only eligibility, drawer conversion, persistence, and selected/expanded state continuity. Decide whether the sidebar pushes content, overlays it, or is replaced by another navigation surface.

## Inputs and evidence

Collect hierarchy depth, labels, icons, badges, resize preferences, active route, expanded groups, keyboard shortcuts, viewport/container constraints, and touch usage. Identify items whose icon is not independently recognizable and sections where collapsed state would hide necessary context.

## Procedure

Define expanded, compact, and transient states only where each is operationally complete. In icon-only compact state, preserve accessible names and provide discoverable labels; do not collapse items that rely solely on text distinctions into ambiguous glyphs.

Carry current selection and disclosure state between representations. If the narrow state becomes a drawer, ensure opening returns users to the relevant part of the hierarchy and closing restores focus to the trigger. Coordinate content offset and animation with the primary region.

## Failure topology

Icon-only sidebars often become memory tests. Drawers may reset scroll or expansion every time they open. Another failure is selected navigation hidden inside a closed drawer without any current-location indicator in the main shell.

Sidebar width persistence can break small windows, and duplicated desktop/mobile sidebars can both appear in the accessibility tree.

## Falsification

Navigate deep into the hierarchy, resize across states, and confirm route, expansion, scroll, and focus persist. Test labels in languages with long strings and with icons removed. Traverse by keyboard and screen reader. Restore a saved wide sidebar in a narrow window and verify safe clamping.

## Output contract

Produce a `responsive-sidebar-behavior-contract` defining states, thresholds, width rules, icon-label policy, hierarchy preservation, overlay/push behavior, focus restoration, persistence, and cross-state tests.

## Handoffs

Use `designing-sidebar-navigation` for base hierarchy, `designing-responsive-navigation-transitions` when the sidebar changes pattern entirely, `designing-responsive-panel-docking` for non-navigation utility panels, and `verifying-responsive-state-parity` for completeness.