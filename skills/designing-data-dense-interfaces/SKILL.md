---
name: designing-data-dense-interfaces
description: Use when expert or operational users must scan, compare, select, edit, monitor, or act on large amounts of structured information with limited screen space.
---

# Designing Data-Dense Interfaces

## Overview
Density is not clutter when every visible bit supports a repeated decision. The goal is high information throughput with stable orientation, not a marketing-style reduction in visible data.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use user/task frequency, comparison needs, data volatility, hierarchy, interaction/state models, and responsive constraints.

## Define the scan task
Before choosing table/list/grid answer:
- what fields users compare across rows/items?
- which fields identify the object?
- which values trigger action?
- which values are diagnostic/supporting?
- what is sorted/grouped/filterable?
- how frequently does data update?
- how many rows/items are typical and extreme?
- what bulk actions and multi-selection exist?

## Structure by comparison
Use aligned columns when cross-item comparison dominates. Cards are appropriate only when each object has heterogeneous content or strong object boundaries and comparison is secondary. Converting a 40-column operational table into cards can destroy the task even if the mobile result looks cleaner.

## Column priority
Classify columns:
- identity/anchor
- decision-critical
- action/status
- supporting/comparison
- optional detail

Define pin/freeze/hide/disclosure rules by priority and user customization. Hidden data must remain reachable when the task needs it.

## Spatial memory
Expert users learn positions. Keep row anatomy, columns, action placement, and sorting behavior stable. Do not reorder frequently due to decorative responsiveness or live updates while the user is selecting/acting.

## Live data
For real-time updates define:
- update cadence
- change highlighting duration
- row reorder policy
- stale indicator
- user pause/freeze behavior
- conflict with selection/editing

Never move the target under the pointer because its sort key changed during interaction unless the product explicitly requires live resorting and the user can maintain context.

## Bulk operations
Selection must remain distinct from keyboard focus/hover. Show selection count/scope, especially across pagination/filters. Destructive bulk actions must state whether they apply to visible, selected, filtered, or all matching items.

## Editing
Inline editing works when context/comparison must remain visible and validation can be localized. Use dedicated editing surfaces when fields have complex dependencies or high consequence. Preserve unsaved edits during incidental sorting/filtering only if the product contract supports it; otherwise warn explicitly.

## Density controls
User-adjustable density can be valuable for expert tools. Density changes spacing/row height/secondary visibility, not semantic capability. Touch targets and focus visibility remain sufficient even in compact mode.

## Performance perception
Virtualized lists/tables must preserve keyboard/focus semantics and avoid announcing or visually jumping as items mount/unmount. Loading additional data should not replace already readable content.

## Responsive strategy
Choose per data relationship:
- horizontal scroll with frozen identity columns
- column prioritization/disclosure
- grouped detail view
- master/detail
- alternate summary + full data route

Do not promise full parity if the product genuinely cannot support a dense task on tiny screens; state the supported task subset.

## Output: `dense-surface-contract`
Return `scan_tasks`, `data_anatomy`, `column_priority`, `alignment_rules`, `selection_model`, `bulk_scope`, `live_update_policy`, `editing_model`, `density_modes`, `responsive_strategy`, `performance_constraints`, and `stress_cases`.

## V6 Dense-Work Surface Protocol
Estimate an **information-compression ratio** for each view: decision-relevant facts visible per unit of space versus chrome/decoration and versus cognitive switching cost. Higher density is useful only while users can still locate, compare, and act. Build a **comparison-anchor map** for columns, row identifiers, frozen labels, units, thresholds, and status positions that must remain stable during scanning.

Define a **frozen-context contract** for sticky headers/columns, pinned identifiers, breadcrumbs, selected rows, aggregate context, and keyboard focus. Frozen regions must not occlude content at zoom or create nested scroll traps. Maintain **filter-sort provenance**: users can always tell which transformations are active, their order/scope, whether data is live/stale, and whether aggregates reflect filtered or total populations.

Run a **density degradation probe** by increasing row count, column count, label length, update frequency, zoom, localization, and alert volume. Detect the point where alignment, selection, or scan path breaks; then adapt hierarchy instead of globally shrinking type.

### Falsification
Ask an expert to compare two distant records, return to the same row after sorting/filtering, and interpret a changing value while updates stream. Loss of anchors, hidden transform state, or dependence on tiny text falsifies the density strategy.

### Recovery
Progressively disclose low-value fields, introduce pinning/grouping/detail-on-demand, preserve comparison columns, or split tasks. Do not convert everything into cards if cross-row comparison is the primary job.
