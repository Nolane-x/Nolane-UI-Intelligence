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
