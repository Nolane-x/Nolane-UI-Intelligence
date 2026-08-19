# UI Industry 1000 — Batch 001 Coverage & Provenance

## Status

Batch 001 adds **100 independently authored canonical specialist faculties** to the existing NUI graph. The canonical graph grows from the historical 174-skill baseline to **274 skills**.

This document records what the batch adds, what it deliberately does not claim, how source material was used, and how the batch avoids numerical inflation through duplicate or mechanically generated skills.

## Authorship declaration

The substantive bodies of the 100 `SKILL.md` files in this batch were authored individually for NUI.

Batch 001 did **not** use:

- loop-generated skill prose;
- Cartesian products such as `domain × component × platform`;
- a single prose template with renamed nouns;
- numbered cosmetic variants;
- bulk copying from OpenDesign, design-system catalogs, `awesome-*` repositories, or vendor guidelines;
- a script that generated the reasoning, decision model, failure topology, falsification or output contracts of the skills.

Automation was used only for repository mechanics: structural acceptance tests, graph registration, validation, count checks, and integrity gates. One-time graph bookkeeping used an explicit 100-node mapping and was removed after the canonical graph was updated.

Shared NUI concepts such as **Parent Contract**, **Decision Boundary**, **Failure Topology**, **Falsification/Recovery**, and **Output Contract** appear where useful because they are repository-level contracts. They do not make the substantive reasoning of the skills interchangeable.

## Promotion standard

A candidate entered Batch 001 only when it could defend a distinct interaction, decision or failure class. The practical test was:

1. Can the trigger be recognized independently?
2. Does the skill own a material decision that a current owner does not completely settle?
3. Can the boundary against parent and sibling owners be stated?
4. Does the problem have characteristic edge cases or failure topology?
5. Do modality, accessibility, temporal, platform, state or data semantics materially alter the answer?
6. Can a recommendation be falsified against runtime or authoritative state?
7. Can downstream work consume a bounded output contract?

If the answer was merely “this is another visual style,” the concept did not qualify as a canonical skill.

## Historical baseline preservation

V6/V8 depth obligations preserve a historical **174-skill depth-locked baseline**. Batch 001 does not reinterpret those 174 files as disposable just because the graph is growing.

Repository validators now enforce the intended invariant:

- the 174 historical baseline must remain present;
- historical V8 depth coverage remains exactly 174 owners;
- the canonical graph may expand beyond that baseline;
- Batch 001 separately proves that its 100 specialist slugs exist, are unique, are registered, have unique outputs, and reach the canonical root.

This avoids a future anti-pattern where Batch 002, Batch 003, and later batches must weaken old tests merely because the canonical count increases.

---

# Batch 001 coverage

## A. Motion and temporal behavior — 20

1. `designing-press-feedback-motion`
2. `designing-hover-response-motion`
3. `designing-focus-transition-motion`
4. `designing-toggle-state-motion`
5. `designing-menu-entry-exit-motion`
6. `designing-popover-origin-motion`
7. `designing-modal-presentation-motion`
8. `designing-drawer-and-sheet-motion`
9. `designing-accordion-expansion-motion`
10. `designing-tab-transition-motion`
11. `designing-list-insertion-removal-motion`
12. `designing-layout-reflow-motion`
13. `designing-shared-element-continuity`
14. `designing-drag-inertia-and-snap`
15. `designing-scroll-linked-motion`
16. `designing-staggered-reveal-motion`
17. `designing-numeric-change-motion`
18. `designing-data-update-motion`
19. `designing-animation-interruption-and-retargeting`
20. `designing-motion-performance-fallbacks`

### Why these are not one `designing-motion` skill

The parent owns motion grammar globally. These children own materially different state machines and failure modes: press commitment vs cancellation, hover capability, semantic focus tracking, persistent toggle state, anchored overlay origin, modal interruption, sheet detents and scroll handoff, disclosure geometry, peer-tab continuity, membership change, layout identity, shared-object identity, post-drag physics, scroll progress, group reveal timing, numerical truth, analytical correspondence, mid-flight retargeting and constrained-runtime degradation.

A single motion checklist cannot make all of those decisions without becoming too broad to route or falsify.

## B. Rich controls and structured input — 20

21. `designing-command-palettes`
22. `designing-comboboxes-and-autocomplete`
23. `designing-multiselect-token-inputs`
24. `designing-cascading-menus`
25. `designing-context-menus`
26. `designing-tooltip-systems`
27. `designing-popover-systems`
28. `designing-dialog-systems`
29. `designing-drawer-and-sheet-components`
30. `designing-tree-views`
31. `designing-split-pane-layouts`
32. `designing-resizable-panels`
33. `designing-docking-workspaces`
34. `designing-property-inspectors`
35. `designing-bulk-action-toolbars`
36. `designing-inline-editing`
37. `designing-editable-data-grids`
38. `designing-date-time-pickers`
39. `designing-file-uploaders`
40. `designing-search-filter-builders`

These specialists intentionally distinguish semantic primitives that AI systems often collapse into “dropdown,” “modal,” “panel,” or “editable table.” Their responsibilities include popup ownership, focus management, managed keyboard navigation, async races, mixed values, selection scope, upload lifecycle, structured query logic and workspace persistence.

## C. Selection and direct manipulation — 10

41. `designing-multi-selection-models`
42. `designing-range-selection`
43. `designing-marquee-and-lasso-selection`
44. `designing-drag-reordering`
45. `designing-resize-handles`
46. `designing-transform-gizmos`
47. `designing-snapping-and-guides`
48. `designing-pan-zoom-navigation`
49. `designing-object-grouping-and-locking`
50. `designing-undo-redo-history`

The batch separates selection membership from focus, range anchors from general multiselect, spatial region acquisition from list ranges, reordering from free movement, resize from general transforms, snap semantics from inertia, viewport navigation from object manipulation, structural grouping from authorization, and semantic undo commands from version history.

## D. Data, spreadsheet and analytical exploration — 15

51. `designing-spreadsheet-interfaces`
52. `designing-cell-editing`
53. `designing-formula-authoring`
54. `designing-frozen-panes`
55. `designing-column-pinning`
56. `designing-table-sorting`
57. `designing-table-filtering`
58. `designing-table-grouping`
59. `designing-tree-grids`
60. `designing-virtualized-grids`
61. `designing-pivot-table-interfaces`
62. `designing-dashboard-drilldown`
63. `designing-cross-filtering`
64. `designing-time-series-exploration`
65. `designing-uncertainty-visualization`

The key boundary here is that **table ≠ interactive grid ≠ spreadsheet ≠ treegrid ≠ pivot table**. Each has a different state model and navigation contract. Analytical skills additionally protect data scope, temporal truth, aggregation, correspondence and uncertainty rather than treating charts as visual decoration.

## E. Enterprise workflow and administration — 15

66. `designing-operational-inboxes`
67. `designing-work-queues`
68. `designing-triage-surfaces`
69. `designing-approval-workflows`
70. `designing-multi-stage-approval`
71. `designing-case-management`
72. `designing-assignment-and-ownership`
73. `designing-escalation-workflows`
74. `designing-sla-aware-interfaces`
75. `designing-audit-log-interfaces`
76. `designing-role-management`
77. `designing-rbac-matrices`
78. `designing-policy-inheritance`
79. `designing-organization-administration`
80. `designing-bulk-administration`

These faculties deliberately separate attention state from work state, queue ordering from triage judgment, a single approval decision from approval-graph orchestration, role definition from permission matrices, and named roles from inherited/effective policy.

## F. Subscription and billing lifecycle — 6

81. `designing-subscription-management`
82. `designing-pricing-plan-comparison`
83. `designing-usage-metering`
84. `designing-quota-and-limit-ux`
85. `designing-payment-failure-recovery`
86. `designing-invoice-history`

The batch separates recurring entitlement state from checkout, commercial comparison from purchase capture, measured usage from enforced limits, payment-method failure from subscription entitlement, and immutable invoice history from transaction status.

## G. Calendar and scheduling — 6

87. `designing-calendar-interfaces`
88. `designing-time-slot-selection`
89. `designing-timezone-aware-scheduling`
90. `designing-recurring-events`
91. `designing-resource-booking`
92. `designing-scheduling-conflicts`

These skills treat dates and times as domain data: instants vs wall-clock times, authoritative timezone, recurrence rules plus exceptions, provisional availability, resource constraints and conflict privacy. They do not assume every scheduling problem is a date picker.

## H. Geospatial interaction — 5

93. `designing-geospatial-interfaces`
94. `designing-map-marker-clustering`
95. `designing-map-layer-management`
96. `designing-map-list-coordination`
97. `designing-route-comparison`

The geospatial family separates viewport/projection/accuracy from screen-space marker clustering, layer provenance and scale visibility, dual map/list representations, and route-alternative comparison. The parent requires structured non-map alternatives when map interaction carries material task access.

## I. Historical state and divergent edits — 3

98. `designing-version-history`
99. `designing-diff-interfaces`
100. `designing-conflict-resolution`

Version history owns durable revision identity and restore semantics; diff interfaces own comparison representation; conflict resolution owns human reconciliation of incompatible divergent states. They intentionally remain distinct from local command undo/redo.

---

# Source and authority posture

## Normative and primary mechanism authorities

The batch relies on the repository’s existing authority hierarchy. The most important primary mechanisms include:

- W3C/WAI WCAG for accessibility obligations;
- WAI-ARIA Authoring Practices for composite-widget semantics, keyboard/focus models, dialog, menu, combobox, grid, tree, treegrid, tooltip and splitter behavior;
- Apple Human Interface Guidelines for platform behavior, direct manipulation, menus, drag/drop, motion and device conventions;
- authoritative platform/browser behavior where a native control or input modality is involved.

These sources constrain semantics and interoperability. NUI does not copy their prose into every skill.

## Mature design-system corroboration

Mature systems such as IBM Carbon, Microsoft Fluent, Adobe Spectrum, Material and GOV.UK are used to compare component anatomy, state coverage, content patterns and accessibility practice. A mature design system can reveal a mechanism or edge case without becoming a universal aesthetic authority.

## Discovery corpora

OpenDesign, VoltAgent/awesome-design-md, bergside/awesome-design-skills and other public design-skill/design-system repositories are treated as discovery corpora. They may expose:

- a component or interaction family NUI has not yet decomposed;
- a useful mechanism worth researching against stronger sources;
- a visual/interaction pattern that needs a neutral, non-brand formulation;
- a failure class visible in a concrete template or professional product.

They are **not** treated as permission to clone brand trade dress, copy a complete skill collection, or equate a rendering template with canonical design cognition.

## Product and professional-tool evidence

For workspace, spreadsheet, calendar, GIS and enterprise patterns, product behavior and domain conventions can be useful evidence, but NUI extracts the mechanism rather than copying a recognizable product composition. Where implementation/code reuse is ever material, license and provenance remain explicit under `adapting-external-ui-patterns`.

---

# Distinct-ownership examples

The following pairs were kept separate intentionally:

- `designing-press-feedback-motion` vs `designing-toggle-state-motion`: transient contact acknowledgment vs persistent value transition.
- `designing-popover-origin-motion` vs `designing-popover-systems`: temporal anchor continuity vs nonmodal surface semantics/focus/dismissal.
- `designing-drawer-and-sheet-motion` vs `designing-drawer-and-sheet-components`: detent/drag physics vs component role/modality/responsive transformation.
- `designing-multi-selection-models` vs `designing-range-selection`: set membership vs anchor/extent over an ordering.
- `designing-drag-reordering` vs `designing-drag-inertia-and-snap`: ordered-container mutation vs post-contact movement physics.
- `designing-spreadsheet-interfaces` vs `designing-editable-data-grids`: workbook/cell/range/formula paradigm vs editable tabular records.
- `designing-frozen-panes` vs `designing-column-pinning`: spreadsheet coordinate quadrants vs wide-table context retention.
- `designing-operational-inboxes` vs `designing-work-queues`: attention/read-resolution stream vs eligibility/ordering/claim backlog.
- `designing-approval-workflows` vs `designing-multi-stage-approval`: one request’s decision lifecycle vs graph/quorum/conditional orchestration.
- `designing-role-management` vs `designing-rbac-matrices` vs `designing-policy-inheritance`: role lifecycle vs dense permission comparison vs effective-value precedence.
- `designing-usage-metering` vs `designing-quota-and-limit-ux`: measured consumption truth vs enforcement/recovery at a boundary.
- `designing-calendar-interfaces` vs `designing-time-slot-selection`: temporal workspace layout vs provisional interval acquisition.
- `designing-timezone-aware-scheduling` vs `designing-recurring-events`: wall-clock/instant/zone semantics vs rule + exception identity.
- `designing-geospatial-interfaces` vs `designing-map-marker-clustering`: spatial workspace truth vs scale-dependent point aggregation.
- `designing-undo-redo-history` vs `designing-version-history`: local semantic command reversal vs durable historical revisions.
- `designing-diff-interfaces` vs `designing-conflict-resolution`: evidence comparison vs choosing/merging an authoritative outcome.

## Rejected style of candidate

Batch 001 intentionally rejected the following *classes* of candidate rather than inflating the graph:

- `beautiful-button-*` or other aesthetic adjectives without a separate decision class;
- one skill per brand merely because a design-system package exists;
- separate “mobile/desktop” copies of a capability when platform adaptation belongs inside one owner;
- `fintech-X`, `healthcare-X`, `education-X` variants where domain semantics do not materially change the interaction;
- generated micro-skills for every possible state combination;
- separate skill files whose only difference is timing constant, color, radius, shadow or component library.

---

# Verification posture

Batch 001 structural acceptance verifies:

- exactly 100 unique new slugs in the batch inventory;
- every directory contains `SKILL.md`;
- frontmatter name matches the directory slug;
- every skill contains substantive decision, failure, falsification and output material;
- every skill is in the canonical graph;
- every parent exists;
- no batch node self-parents;
- batch outputs are unique;
- every parent chain reaches `using-nolane-ui`;
- the expanded graph retains at least the original 174 historical owners.

These checks are **structural evidence**, not proof that every future UI produced with NUI is superior. NUI V10’s empirical claim discipline remains unchanged.

## Current count after Batch 001

```text
Historical canonical baseline: 174
Batch 001 specialists:         100
Current canonical graph:       274
Long-term roadmap target:     1000
```

The 1,000 target is a coverage roadmap, never a justification for duplicate ownership. Future batches must pass the same novelty and boundary discipline before the count is allowed to grow.
