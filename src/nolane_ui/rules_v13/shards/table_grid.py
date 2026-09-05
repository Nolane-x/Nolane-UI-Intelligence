"""V13 interactive table and grid rules with explicit record, focus, and semantic boundaries."""
from __future__ import annotations

from ._capabilities import interaction_caps


TABLE_GRID_RULES_V13 = [
    {'rule_id': 'ui.table.grid-focus-survives-virtualization',
     'domain': 'table',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Virtualized grids must preserve logical keyboard focus as rows recycle',
     'statement': 'When row virtualization unmounts and reuses DOM nodes, keyboard focus and active-cell semantics must '
                  'remain bound to the same logical record or move by an explicit navigation rule rather than jumping '
                  'with recycled elements.',
     'intent': 'Keep two-dimensional keyboard navigation stable when rendering optimization changes the physical '
               'elements underneath a logical data grid.',
     'applies_when': ['An interactive data grid virtualizes rows or columns while keyboard users can navigate, select, '
                      'or edit cells.'],
     'does_not_apply_when': [],
     'failure_modes': ['Scrolling or data-window recycling moves focus to a different logical row because the focused '
                       'DOM node was reused for another record.'],
     'user_impacts': ['Keyboard and screen-reader users can edit, select, or activate the wrong record after ordinary '
                      'scrolling.'],
     'observables': ['Focus a cell, force virtualization across multiple windows, and compare active descendant, row '
                     'key, column key, and announced position before and after recycling.'],
     'falsifiers': ['The focused logical cell remains the same until a defined navigation action changes it, even if its '
                    'backing DOM element is replaced.'],
     'repairs': ['Persist focus by stable row and column identity and restore it when virtualized elements mount instead '
                 'of keying focus to render index.'],
     'exceptions': [],
     'verification': ['Navigate a large grid with keyboard paging, filtering, and recycling while asserting stable '
                      'logical focus and accessibility-tree position.'],
     'owner_hints': ['designing-virtualized-grids'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-wai-aria12-v13', 'nui-data-viz-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.edit-cancel-restores-authoritative-cell',
     'domain': 'table',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Cancelling an editable-grid cell must restore the pre-edit authoritative value',
     'statement': 'If cell editing is cancellable, cancelling must restore the value and validation state that were '
                  'authoritative when the edit began instead of leaving a partially normalized, formatted, or locally '
                  'mutated intermediate value.',
     'intent': 'Make grid edit cancellation a real rollback boundary rather than a cosmetic exit from edit mode.',
     'applies_when': ['Cells can enter an edit mode with local parsing, formatting, validation, lookup, or optimistic '
                      'state before commit.'],
     'does_not_apply_when': [],
     'failure_modes': ['Pressing Escape or Cancel exits edit mode but leaves the transformed draft, error state, or '
                       'partially written model value behind.'],
     'user_impacts': ['Users can silently change data even though they chose the explicit cancel path.'],
     'observables': ['Begin edits that trigger formatting and validation, cancel at several intermediate states, then '
                     'compare displayed and stored values with the pre-edit authoritative snapshot.'],
     'falsifiers': ['Cancellation restores the original cell value and dependent local state unless the product '
                    'explicitly documents a non-revertible edit operation.'],
     'repairs': ['Snapshot the authoritative cell state at edit entry and route cancel through the same rollback '
                 'semantics used for aborted transactions.'],
     'exceptions': [],
     'verification': ['Exercise cancel before validation, during async lookup, after formatting, and after focus '
                      'movement and verify no draft mutation survives.'],
     'owner_hints': ['designing-editable-data-grids'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-wai-aria12-v13', 'nui-data-viz-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.sort-state-announced-with-active-column',
     'domain': 'table',
     'class': 'mechanical',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Interactive tables must expose which column is sorted and in which direction',
     'statement': 'When a table or grid applies sorting, the active sort column and direction must be represented in '
                  'programmatic semantics as well as visible styling so nonvisual users receive the same ordering state.',
     'intent': 'Keep the ordering model discoverable and aligned across header visuals, accessibility semantics, and the '
               'actual record sequence.',
     'applies_when': ['A table header can sort records by one or more columns and communicates sort state through header '
                      'controls.'],
     'does_not_apply_when': [],
     'failure_modes': ['Records reorder but the active header has no accessible sort state, announces the wrong '
                       'direction, or retains stale state after sorting changes.'],
     'user_impacts': ['Users relying on assistive technology can misread the meaning of row order or believe a different '
                      'sort is active.'],
     'observables': ['Toggle each sortable header and inspect record order, header indicator, focus, and '
                     'accessibility-tree sort state after every transition.'],
     'falsifiers': ['The active sort semantics match the actual order and inactive headers do not falsely claim an '
                    'active direction.'],
     'repairs': ['Bind header sort semantics to the same canonical sort descriptor that drives the data query or local '
                 'comparator.'],
     'exceptions': [],
     'verification': ['Sort ascending, descending, clear sorting, and switch columns while verifying visual and '
                      'accessibility states remain synchronized with row order.'],
     'owner_hints': ['designing-table-sorting'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-wai-aria12-v13', 'nui-data-viz-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.group-selection-scope-visible',
     'domain': 'table',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Grouped tables must make group-selection scope explicit before bulk actions',
     'statement': 'When selecting a group header or grouped row set, the UI must make clear whether selection includes '
                  'only visible children, loaded children, all records in the group, or descendants across collapsed '
                  'subgroups before a bulk action uses that selection.',
     'intent': 'Prevent grouping from hiding a multiplicative selection scope that can make bulk actions affect more '
               'records than the user can see.',
     'applies_when': ['A data grid supports grouping, collapsing, remote paging, or nested groups together with '
                      'group-level selection.'],
     'does_not_apply_when': [],
     'failure_modes': ['A group checkbox appears fully selected while its scope silently includes unloaded or collapsed '
                       'records the user did not inspect.'],
     'user_impacts': ['Bulk edits or destructive actions can affect an unexpectedly large record set because grouping '
                      'obscured selection semantics.'],
     'observables': ['Select groups with collapsed and unloaded descendants, then inspect selected identifiers and the '
                     'count/scope communicated before invoking bulk actions.'],
     'falsifiers': ['The UI communicates the exact selection basis and mixed states when only part of a group is '
                    'selected or loaded.'],
     'repairs': ['Model group selection as an explicit scope descriptor and surface visible, loaded, and total selection '
                 'counts where they differ.'],
     'exceptions': [],
     'verification': ['Exercise nested groups across filtering, paging, collapse, and select-all transitions and verify '
                      'the pre-commit scope matches authoritative selected IDs.'],
     'owner_hints': ['designing-table-grouping'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-data-viz-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.bulk-edit-partial-failure-maps-to-records',
     'domain': 'table',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Bulk grid edits must map partial failures back to the affected records',
     'statement': 'When a multi-row edit commits only some records, the result must identify which rows succeeded, '
                  'failed, or remain pending instead of presenting one aggregate success or failure banner for the whole '
                  'operation.',
     'intent': 'Preserve record-level truth after partial bulk mutations so users can repair failures without reapplying '
               'successful changes.',
     'applies_when': ['A table supports editing or applying an action to multiple records in one transaction or batched '
                      'request.'],
     'does_not_apply_when': [],
     'failure_modes': ['Some rows fail validation or authorization but the grid reports generic success, generic '
                       'failure, or resets all rows to a uniform state.'],
     'user_impacts': ['Users can retry already successful mutations, miss failed records, or believe unsaved changes are '
                      'authoritative.'],
     'observables': ['Force heterogeneous row outcomes in one bulk edit and compare server results with each row state, '
                     'error indicator, selection, and retry target.'],
     'falsifiers': ['Every affected record resolves to a truthful success, failure, pending, or unchanged state and '
                    'retry targets only unresolved records.'],
     'repairs': ['Key bulk-result reconciliation by stable record identity and preserve row-local error details after '
                 'the aggregate request completes.'],
     'exceptions': [],
     'verification': ['Run partial validation, permission, and network failures across selected rows and verify '
                      'per-record state survives sorting and filtering.'],
     'owner_hints': ['designing-editable-data-grids'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-data-viz-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.pinned-columns-do-not-cover-row-actions',
     'domain': 'table',
     'class': 'mechanical',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Pinned columns must not occlude essential row actions during horizontal scroll',
     'statement': 'Frozen or pinned columns may remain fixed while the grid scrolls, but their stacking and width '
                  'behavior must not cover essential cells, focus targets, or row actions that users need to complete '
                  'the table task.',
     'intent': 'Keep column pinning from turning a navigation convenience into an inaccessible overlay over the scrolled '
               'data plane.',
     'applies_when': ['A wide table permits column pinning or frozen identity columns while other columns scroll '
                      'horizontally underneath.'],
     'does_not_apply_when': [],
     'failure_modes': ['Pinned regions overlap the active cell, hide row actions, or trap focus beneath a fixed layer at '
                       'realistic viewport widths.'],
     'user_impacts': ['Users can lose access to controls or read the wrong cell because visual layers no longer '
                      'correspond to the grid geometry.'],
     'observables': ['Pin multiple columns, shrink the viewport, scroll to each edge, and inspect clipping, hit testing, '
                     'focus visibility, and action reachability.'],
     'falsifiers': ['Pinned regions consume defined layout space or collision rules so every essential cell and focused '
                    'control remains reachable without hidden overlap.'],
     'repairs': ['Include pinned widths in grid geometry and constrain pinning when the remaining viewport cannot expose '
                 'essential content safely.'],
     'exceptions': [],
     'verification': ['Test maximal pinning across responsive widths, keyboard navigation, row menus, and zoom and '
                      'verify no required target is hidden behind the pinned plane.'],
     'owner_hints': ['designing-column-pinning'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(**{'visual-render': 'REQUIRED', 'browser-runtime': 'REQUIRED'}),
     'provenance_ids': ['nui-data-viz-owners-v13', 'w3c-wcag22-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.column-visibility-preserves-header-association',
     'domain': 'table',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Hiding table columns must preserve correct header associations for remaining cells',
     'statement': 'When users hide, reveal, or reorder columns, the programmatic relationship between each remaining '
                  'data cell and its row or column headers must update to match the visible logical structure rather '
                  'than stale original indexes.',
     'intent': 'Keep dynamic column personalization from corrupting the semantic table model presented to assistive '
               'technology.',
     'applies_when': ['A table or grid allows runtime column visibility, ordering, grouping, or responsive column mode '
                      'changes.'],
     'does_not_apply_when': [],
     'failure_modes': ['After hiding or reordering columns, screen readers announce headers belonging to previous '
                       'indexes or expose inconsistent row and column counts.'],
     'user_impacts': ['Nonvisual users can interpret values under the wrong field names even though the visible table '
                      'appears correct.'],
     'observables': ['Hide and reorder several columns while inspecting accessibility-tree ownership, header labels, '
                     'column indices, and announced values for representative cells.'],
     'falsifiers': ['Every remaining cell is associated with the header that currently defines its logical column, and '
                    'hidden columns do not corrupt reported positions.'],
     'repairs': ['Derive semantic row and column metadata from the post-transformation column model instead of physical '
                 'DOM position or original schema index.'],
     'exceptions': [],
     'verification': ['Exercise column hide, reveal, reorder, responsive collapse, and persistence reload and verify '
                      'header associations after each transition.'],
     'owner_hints': ['designing-accessible-data-table-navigation'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-wai-aria12-v13', 'nui-data-viz-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.table.treegrid-collapse-restores-logical-focus',
     'domain': 'table',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Collapsing a treegrid branch must move focus to a surviving logical ancestor',
     'statement': 'If collapsing a treegrid branch removes the row or cell that currently owns focus, focus must move to '
                  'a predictable surviving ancestor or controlling row rather than disappear, jump to the document, or '
                  'land on an unrelated recycled row.',
     'intent': 'Preserve keyboard location and hierarchy comprehension when treegrid structure removes descendants from '
               'the active interaction model.',
     'applies_when': ['An interactive treegrid supports expanding and collapsing branches while focus may reside on a '
                      'descendant row or control.'],
     'does_not_apply_when': [],
     'failure_modes': ['Collapsing an ancestor destroys the focused descendant and leaves focus lost, offscreen, or '
                       'reassigned to a different record by DOM recycling.'],
     'user_impacts': ['Keyboard users can lose their place in the hierarchy and accidentally operate the wrong row after '
                      'collapse.'],
     'observables': ['Focus deep descendants, collapse each ancestor by keyboard and pointer, then inspect active '
                     'element, logical row identity, and accessibility-tree focus.'],
     'falsifiers': ['Focus lands on the collapsing row or another documented surviving ancestor with hierarchy state '
                    'announced correctly.'],
     'repairs': ['Before removing descendants, resolve the nearest surviving logical focus target and restore focus '
                 'after the structural update completes.'],
     'exceptions': [],
     'verification': ['Test nested collapse with edited cells, virtualized rows, and async child loading and verify '
                      'focus follows the defined ancestor rule.'],
     'owner_hints': ['designing-tree-grids'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-wai-aria12-v13', 'nui-data-viz-owners-v13'],
     'status': 'active'},
]

__all__ = ['TABLE_GRID_RULES_V13']
