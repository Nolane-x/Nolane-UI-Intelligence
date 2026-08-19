from __future__ import annotations

import json
from pathlib import Path


GRAPH_PATH = Path(__file__).resolve().parents[1] / "skills" / "skill-graph.json"

BATCH_001_NODES = {
    "designing-press-feedback-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "press-feedback-motion-contract"},
    "designing-hover-response-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "hover-response-motion-contract"},
    "designing-focus-transition-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "focus-transition-motion-contract"},
    "designing-toggle-state-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "toggle-state-motion-contract"},
    "designing-menu-entry-exit-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "menu-motion-contract"},
    "designing-popover-origin-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "popover-origin-motion-contract"},
    "designing-modal-presentation-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "modal-presentation-motion-contract"},
    "designing-drawer-and-sheet-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "drawer-sheet-motion-contract"},
    "designing-accordion-expansion-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "accordion-expansion-motion-contract"},
    "designing-tab-transition-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "tab-transition-motion-contract"},
    "designing-list-insertion-removal-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "list-membership-motion-contract"},
    "designing-layout-reflow-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "layout-reflow-motion-contract"},
    "designing-shared-element-continuity": {"family": "motion-specialist", "parent": "designing-motion", "output": "shared-element-continuity-contract"},
    "designing-drag-inertia-and-snap": {"family": "motion-specialist", "parent": "designing-pointer-touch-pen-input", "output": "drag-inertia-snap-contract"},
    "designing-scroll-linked-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "scroll-linked-motion-contract"},
    "designing-staggered-reveal-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "staggered-reveal-contract"},
    "designing-numeric-change-motion": {"family": "motion-specialist", "parent": "designing-motion", "output": "numeric-change-motion-contract"},
    "designing-data-update-motion": {"family": "motion-specialist", "parent": "designing-data-visualization", "output": "data-update-motion-contract"},
    "designing-animation-interruption-and-retargeting": {"family": "motion-specialist", "parent": "designing-motion", "output": "animation-interruption-contract"},
    "designing-motion-performance-fallbacks": {"family": "motion-specialist", "parent": "designing-motion", "output": "motion-performance-fallback-contract"},

    "designing-command-palettes": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "command-palette-contract"},
    "designing-comboboxes-and-autocomplete": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "combobox-autocomplete-contract"},
    "designing-multiselect-token-inputs": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "multiselect-token-input-contract"},
    "designing-cascading-menus": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "cascading-menu-contract"},
    "designing-context-menus": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "context-menu-contract"},
    "designing-tooltip-systems": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "tooltip-system-contract"},
    "designing-popover-systems": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "popover-system-contract"},
    "designing-dialog-systems": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "dialog-system-contract"},
    "designing-drawer-and-sheet-components": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "drawer-sheet-component-contract"},
    "designing-tree-views": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "tree-view-contract"},
    "designing-split-pane-layouts": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "split-pane-layout-contract"},
    "designing-resizable-panels": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "resizable-panel-contract"},
    "designing-docking-workspaces": {"family": "workspace-specialist", "parent": "designing-editor-canvas-workspaces", "output": "docking-workspace-contract"},
    "designing-property-inspectors": {"family": "workspace-specialist", "parent": "designing-editor-canvas-workspaces", "output": "property-inspector-contract"},
    "designing-bulk-action-toolbars": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "bulk-action-toolbar-contract"},
    "designing-inline-editing": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "inline-editing-contract"},
    "designing-editable-data-grids": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "editable-data-grid-contract"},
    "designing-date-time-pickers": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "date-time-picker-contract"},
    "designing-file-uploaders": {"family": "component-specialist", "parent": "engineering-rich-interactive-components", "output": "file-uploader-contract"},
    "designing-search-filter-builders": {"family": "search-specialist", "parent": "designing-search", "output": "search-filter-builder-contract"},

    "designing-multi-selection-models": {"family": "manipulation-specialist", "parent": "designing-pointer-touch-pen-input", "output": "multi-selection-contract"},
    "designing-range-selection": {"family": "manipulation-specialist", "parent": "designing-multi-selection-models", "output": "range-selection-contract"},
    "designing-marquee-and-lasso-selection": {"family": "manipulation-specialist", "parent": "designing-multi-selection-models", "output": "region-selection-contract"},
    "designing-drag-reordering": {"family": "manipulation-specialist", "parent": "designing-accessible-drag-and-drop", "output": "drag-reorder-contract"},
    "designing-resize-handles": {"family": "manipulation-specialist", "parent": "designing-pointer-touch-pen-input", "output": "resize-handle-contract"},
    "designing-transform-gizmos": {"family": "workspace-specialist", "parent": "designing-editor-canvas-workspaces", "output": "transform-gizmo-contract"},
    "designing-snapping-and-guides": {"family": "manipulation-specialist", "parent": "designing-pointer-touch-pen-input", "output": "snapping-guides-contract"},
    "designing-pan-zoom-navigation": {"family": "manipulation-specialist", "parent": "designing-pointer-touch-pen-input", "output": "pan-zoom-navigation-contract"},
    "designing-object-grouping-and-locking": {"family": "workspace-specialist", "parent": "designing-editor-canvas-workspaces", "output": "object-group-lock-contract"},
    "designing-undo-redo-history": {"family": "interaction-specialist", "parent": "designing-interactions", "output": "undo-redo-history-contract"},

    "designing-spreadsheet-interfaces": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "spreadsheet-interface-contract"},
    "designing-cell-editing": {"family": "data-specialist", "parent": "designing-spreadsheet-interfaces", "output": "cell-editing-contract"},
    "designing-formula-authoring": {"family": "data-specialist", "parent": "designing-spreadsheet-interfaces", "output": "formula-authoring-contract"},
    "designing-frozen-panes": {"family": "data-specialist", "parent": "designing-spreadsheet-interfaces", "output": "frozen-pane-contract"},
    "designing-column-pinning": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "column-pinning-contract"},
    "designing-table-sorting": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "table-sorting-contract"},
    "designing-table-filtering": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "table-filtering-contract"},
    "designing-table-grouping": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "table-grouping-contract"},
    "designing-tree-grids": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "tree-grid-contract"},
    "designing-virtualized-grids": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "virtualized-grid-contract"},
    "designing-pivot-table-interfaces": {"family": "data-specialist", "parent": "designing-data-dense-interfaces", "output": "pivot-table-interface-contract"},
    "designing-dashboard-drilldown": {"family": "data-specialist", "parent": "designing-data-visualization", "output": "dashboard-drilldown-contract"},
    "designing-cross-filtering": {"family": "data-specialist", "parent": "designing-data-visualization", "output": "cross-filtering-contract"},
    "designing-time-series-exploration": {"family": "data-specialist", "parent": "designing-data-visualization", "output": "time-series-exploration-contract"},
    "designing-uncertainty-visualization": {"family": "data-specialist", "parent": "designing-data-visualization", "output": "uncertainty-visualization-contract"},

    "designing-operational-inboxes": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "operational-inbox-contract"},
    "designing-work-queues": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "work-queue-contract"},
    "designing-triage-surfaces": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "triage-surface-contract"},
    "designing-approval-workflows": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "approval-workflow-contract"},
    "designing-multi-stage-approval": {"family": "workflow-specialist", "parent": "designing-approval-workflows", "output": "multi-stage-approval-contract"},
    "designing-case-management": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "case-management-contract"},
    "designing-assignment-and-ownership": {"family": "workflow-specialist", "parent": "designing-collaboration-and-presence", "output": "assignment-ownership-contract"},
    "designing-escalation-workflows": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "escalation-workflow-contract"},
    "designing-sla-aware-interfaces": {"family": "workflow-specialist", "parent": "designing-task-flows", "output": "sla-aware-interface-contract"},
    "designing-audit-log-interfaces": {"family": "workflow-specialist", "parent": "designing-data-dense-interfaces", "output": "audit-log-interface-contract"},
    "designing-role-management": {"family": "admin-specialist", "parent": "designing-permissions-and-consent", "output": "role-management-contract"},
    "designing-rbac-matrices": {"family": "admin-specialist", "parent": "designing-role-management", "output": "rbac-matrix-contract"},
    "designing-policy-inheritance": {"family": "admin-specialist", "parent": "designing-permissions-and-consent", "output": "policy-inheritance-contract"},
    "designing-organization-administration": {"family": "admin-specialist", "parent": "routing-ui-work", "output": "organization-administration-contract"},
    "designing-bulk-administration": {"family": "admin-specialist", "parent": "designing-organization-administration", "output": "bulk-administration-contract"},

    "designing-subscription-management": {"family": "transaction-specialist", "parent": "designing-commerce-checkout", "output": "subscription-management-contract"},
    "designing-pricing-plan-comparison": {"family": "transaction-specialist", "parent": "designing-commerce-checkout", "output": "pricing-comparison-contract"},
    "designing-usage-metering": {"family": "transaction-specialist", "parent": "designing-subscription-management", "output": "usage-metering-contract"},
    "designing-quota-and-limit-ux": {"family": "transaction-specialist", "parent": "designing-subscription-management", "output": "quota-limit-contract"},
    "designing-payment-failure-recovery": {"family": "transaction-specialist", "parent": "designing-financial-transaction-ui", "output": "payment-failure-recovery-contract"},
    "designing-invoice-history": {"family": "transaction-specialist", "parent": "designing-subscription-management", "output": "invoice-history-contract"},

    "designing-calendar-interfaces": {"family": "temporal-specialist", "parent": "designing-task-flows", "output": "calendar-interface-contract"},
    "designing-time-slot-selection": {"family": "temporal-specialist", "parent": "designing-calendar-interfaces", "output": "time-slot-selection-contract"},
    "designing-timezone-aware-scheduling": {"family": "temporal-specialist", "parent": "designing-task-flows", "output": "timezone-scheduling-contract"},
    "designing-recurring-events": {"family": "temporal-specialist", "parent": "designing-calendar-interfaces", "output": "recurring-event-contract"},
    "designing-resource-booking": {"family": "temporal-specialist", "parent": "designing-task-flows", "output": "resource-booking-contract"},
    "designing-scheduling-conflicts": {"family": "temporal-specialist", "parent": "designing-task-flows", "output": "scheduling-conflict-contract"},

    "designing-geospatial-interfaces": {"family": "geospatial-specialist", "parent": "designing-data-dense-interfaces", "output": "geospatial-interface-contract"},
    "designing-map-marker-clustering": {"family": "geospatial-specialist", "parent": "designing-geospatial-interfaces", "output": "map-marker-clustering-contract"},
    "designing-map-layer-management": {"family": "geospatial-specialist", "parent": "designing-geospatial-interfaces", "output": "map-layer-management-contract"},
    "designing-map-list-coordination": {"family": "geospatial-specialist", "parent": "designing-geospatial-interfaces", "output": "map-list-coordination-contract"},
    "designing-route-comparison": {"family": "geospatial-specialist", "parent": "designing-geospatial-interfaces", "output": "route-comparison-contract"},

    "designing-version-history": {"family": "history-specialist", "parent": "designing-collaboration-and-presence", "output": "version-history-contract"},
    "designing-diff-interfaces": {"family": "history-specialist", "parent": "designing-version-history", "output": "diff-interface-contract"},
    "designing-conflict-resolution": {"family": "history-specialist", "parent": "designing-collaboration-and-presence", "output": "conflict-resolution-contract"},
}


def main() -> None:
    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    existing = set(graph["skills"]).intersection(BATCH_001_NODES)
    if existing:
        raise SystemExit(f"Batch 001 nodes already exist: {sorted(existing)}")
    if len(BATCH_001_NODES) != 100:
        raise SystemExit(f"Expected 100 nodes, got {len(BATCH_001_NODES)}")
    graph["skills"].update(BATCH_001_NODES)
    GRAPH_PATH.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
