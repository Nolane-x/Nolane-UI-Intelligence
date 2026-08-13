---
name: designing-screen-reader-experiences
description: Use when a UI contains complex semantics, dynamic updates, custom widgets, tables, dialogs, virtualized content, drag/drop, charts, realtime data, routing, or other behavior whose accessible reading and focus experience cannot be inferred from appearance.
---

# Designing Screen Reader Experiences

## Overview
A screen reader experiences an information and interaction graph, not a screenshot. Design semantic structure, names, states, virtual reading order, focus transitions, and announcements so the task remains coherent without spatial vision.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Require component semantics, information architecture, focus model, dynamic-state model, and accessibility annotations. Use native semantics before custom ARIA; APG-style patterns create behavioral promises that must be implemented fully.

## Decision Model
Model two navigation systems: **virtual/read navigation** through document semantics and **interaction focus** through controls/widgets. They overlap but are not identical. Create meaningful landmarks/headings, lists/tables, labels/descriptions, and relationships so users can scan by structure rather than listen linearly to every element.

Every control needs a stable accessible name that communicates purpose without redundant role words. Expose value, selected/expanded/checked/current/invalid/busy states when meaningful. Composite widgets need the correct interaction model: grid, tree, combobox, tabs, menu, listbox, dialog, or a simpler native control when possible.

Dynamic updates require prioritization. Announce completion, errors, consequential new content, and relevant state changes — not every animation or telemetry tick. Batch realtime/streaming updates and let users request detail. Moving DOM nodes must not cause virtual cursor or keyboard focus to jump unexpectedly.

Route and overlay transitions have explicit focus behavior. Dialog open moves focus inside; close returns meaningfully. Deletion moves focus to a logical neighbor or parent. Validation can use an error summary plus field-level associations. Virtualization must expose correct collection position/identity and preserve focus when rows recycle.

For visualizations, provide a structured summary/table or exploration model tied to the same data and conclusions, not an alt-text sentence that attempts to serialize an entire chart.

## Evidence
Test with at least the screen reader/browser/platform combinations relevant to the product, keyboard navigation, headings/landmarks, forms/errors, dialogs, custom widgets, dynamic updates, virtualization, routing, charts, and localization. Accessibility-tree snapshots support regression but do not replace listening and interaction testing.

## Output Contract
Return a `screen-reader-contract` with `semantic_structure`, `landmarks_headings[]`, `name_description_rules`, `state_property_map`, `virtual_vs_focus_order`, `widget_patterns[]`, `dynamic_announcement_policy`, `route_overlay_focus`, `virtualization_rules`, `visualization_alternatives[]`, and `screen_reader_tests[]`.

## Failure Traps
- Adding ARIA roles without matching keyboard behavior.
- Live region announces every character or numeric tick.
- Visual order changed while semantic reading order remains incoherent.
- Focus sent to page top after every route or deletion.
- Icon name duplicates role (“button button”).
- Virtualized list reports recycled rows inconsistently.
- Chart alt text says only “chart showing data.”

Screen-reader quality is demonstrated by completing the real task efficiently, not by an accessibility tree with many labels.

## V6 Screen-Reader Interaction Model
Separate **virtual-cursor versus focus** behavior. Reading/browse navigation and interactive focus are distinct models; do not move DOM focus merely because content changed or because a screen-reader user browsed to an element. For every interactive/control state produce a **name-role-value trace** including accessible name source, role, current value/state, description, relationship, and activation result.

Set **live-region cadence** by event importance and frequency. Streaming tokens, prices, progress, validation, chat messages, and background jobs need aggregation/debouncing rules so announcements convey change without overwhelming speech. Run a **DOM-visual-order audit** for CSS grid/flex reordering, portals, sticky regions, responsive transforms, modals, and virtualized lists; the reading order must match the conceptual sequence even when visuals are art-directed.

Define a **focus-restoration contract** for dialogs, popovers, deletion, navigation, inserted items, errors, async completion, and virtualized content. Restoration targets must still exist and remain meaningful; falling back to `body` is not recovery.

### Falsification
Complete the critical task without looking at the screen, using browse mode and focus mode intentionally. Trigger dynamic updates and responsive changes. Missing context, announcement storms, or focus loss falsify the experience.

### Recovery
Repair DOM semantics and focus ownership at the component/flow layer, simplify live updates, and provide structured alternatives for inaccessible visualizations. Avoid piling ARIA onto a fundamentally wrong interaction model.
