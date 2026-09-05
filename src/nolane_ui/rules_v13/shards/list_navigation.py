"""V13 seventh-wave independently authored rules for list navigation."""
from __future__ import annotations

from ._capabilities import interaction_caps


LIST_NAVIGATION_RULES_V13 = [{'rule_id': 'ui.list.pagination-stable-under-concurrent-insert',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Paginated lists must not skip or duplicate records when items are inserted concurrently',
  'statement': 'A list that pages through a changing dataset should use stable ordering and cursor semantics '
               'or explicitly snapshot the result set so new inserts do not shift unseen items across '
               'boundaries.',
  'intent': 'Preserve complete traversal of operational data even while the collection changes.',
  'applies_when': ['Users navigate multiple pages while new records can be added ahead of or inside the '
                   'active sort order.'],
  'does_not_apply_when': [],
  'failure_modes': ['Offset paging shifts after an insert, causing one item to appear twice and another '
                    'never to appear in the browsing session.'],
  'user_impacts': ['Users can miss records, process duplicates, or draw incorrect conclusions from an '
                   'incomplete collection.'],
  'observables': ['Load page one, insert records at several sort positions, then traverse remaining pages '
                  'and compare stable IDs with the authoritative result set.'],
  'falsifiers': ['The browsing contract is snapshot-stable or cursor-stable, with every record in scope '
                 'appearing once according to the declared live-data policy.'],
  'repairs': ['Use stable cursor keys or snapshot versions rather than raw positional offsets over mutable '
              'ordering.'],
  'exceptions': [],
  'verification': ['Repeat concurrent inserts at page boundaries under ascending and descending sorts, '
                   'checking for missing and duplicate identities.'],
  'owner_hints': ['designing-pagination'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.page-size-change-preserves-context',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Changing page size must preserve the user’s logical collection context',
  'statement': 'When users change the number of rows per page, the product should keep the previously '
               'focused or leading record in view where possible instead of jumping to an unrelated slice of '
               'the dataset.',
  'intent': 'Avoid disorienting users who adjust density while inspecting a specific record neighborhood.',
  'applies_when': ['A paginated list lets users change page size without changing filters or sort.'],
  'does_not_apply_when': [],
  'failure_modes': ['Switching from 25 to 100 rows resets to an arbitrary page or start position, losing the '
                    'record the user was inspecting.'],
  'user_impacts': ['Users must search again for their place and may act on the wrong neighboring records '
                   'after the jump.'],
  'observables': ['Navigate to a later page, focus a record, change page size repeatedly, and track whether '
                  'that record remains in the new visible slice.'],
  'falsifiers': ['The list computes the new page or cursor from the logical anchor record, or clearly resets '
                 'with an explicit reason when preservation is impossible.'],
  'repairs': ['Use stable record identity as the page-size transition anchor rather than reusing the old '
              'numeric page index blindly.'],
  'exceptions': [],
  'verification': ['Test several page sizes near collection boundaries and after record insertion, verifying '
                   'context preservation remains deterministic.'],
  'owner_hints': ['designing-pagination'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.sort-key-and-direction-visible',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'List ordering must expose the active sort key and direction when order affects interpretation',
  'statement': 'A sortable list must make its effective ordering visible, including secondary ordering where '
               'ties would otherwise appear arbitrary or unstable.',
  'intent': 'Let users understand why records appear where they do and reproduce the same order after '
            'refresh or export.',
  'applies_when': ['The list supports multiple sort keys or a default order that is not obvious from the '
                   'data itself.'],
  'does_not_apply_when': [],
  'failure_modes': ['Rows appear sorted but no header or control indicates whether the active order is '
                    'newest, priority, name, score, or another field.'],
  'user_impacts': ['Users can mistake rank for chronology, overlook high-priority items, or believe a stable '
                   'order has changed randomly.'],
  'observables': ['Apply sorts, reload deep links, and inspect tied values to compare displayed controls '
                  'with actual query ordering.'],
  'falsifiers': ['The effective primary sort and direction are visible, and deterministic tie-breaking '
                 'prevents unexplained reshuffling where order matters.'],
  'repairs': ['Bind sort controls and route state to the canonical query order and apply a stable secondary '
              'key when needed.'],
  'exceptions': [],
  'verification': ['Test equal primary values, locale-sensitive strings, and saved views, verifying the '
                   'visible sort contract fully explains row order.'],
  'owner_hints': ['designing-table-sorting'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.filter-reset-state-explicit',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resetting list filters must make the resulting query state explicit',
  'statement': 'A reset or clear-filters action must remove the intended filters while preserving unrelated '
               'query dimensions such as sort, scope, or saved view according to a documented contract.',
  'intent': 'Prevent “reset” from silently changing more of the user’s collection context than expected.',
  'applies_when': ['A list combines filters with sort, scope, search, saved views, or pagination.'],
  'does_not_apply_when': [],
  'failure_modes': ['Clear filters also resets the workspace scope or saved sort, or leaves a hidden filter '
                    'active while presenting an apparently clean toolbar.'],
  'user_impacts': ['Users can believe they are seeing the full expected dataset when hidden query state '
                   'still limits or reorders results.'],
  'observables': ['Create a complex query, invoke each reset affordance, and inspect canonical URL/query '
                  'state plus active filter chips and result population.'],
  'falsifiers': ['The post-reset query has no hidden targeted filters and any preserved dimensions remain '
                 'visibly represented.'],
  'repairs': ['Define reset semantics by query dimension and derive controls from the same canonical state '
              'object used for fetching.'],
  'exceptions': [],
  'verification': ['Test reset from saved views, deep links, and mobile filter sheets, verifying visible '
                   'controls and backend query agree exactly.'],
  'owner_hints': ['designing-table-filtering'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.infinite-scroll-end-and-retry-visible',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Infinite scrolling must distinguish true end-of-list from load failure or paused fetching',
  'statement': 'A continuously loaded list must make it clear whether no more records exist, loading is in '
               'progress, or the next batch failed and can be retried.',
  'intent': 'Prevent network failures from masquerading as the natural end of a collection.',
  'applies_when': ['The list fetches additional batches automatically near the scroll boundary.'],
  'does_not_apply_when': [],
  'failure_modes': ['A failed next-page request leaves blank space with no error or retry, which looks '
                    'identical to reaching the final item.'],
  'user_impacts': ['Users can assume records do not exist and stop searching or processing prematurely.'],
  'observables': ['Throttle and fail a later batch while records remain, then compare the boundary with a '
                  'genuine end-of-list response.'],
  'falsifiers': ['Loading, failed-more, and complete states are visibly and semantically distinct, with '
                 'retry preserving the current collection context.'],
  'repairs': ['Model incremental fetch lifecycle explicitly and require authoritative pagination completion '
              'before rendering an end marker.'],
  'exceptions': [],
  'verification': ['Exercise failures at several cursor positions and recoveries after reconnect, verifying '
                   'no failure is presented as final completion.'],
  'owner_hints': ['designing-pagination'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.selection-across-pages-scope-explicit',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cross-page list selection must expose whether actions target visible rows, selected rows, or the '
           'full query',
  'statement': 'When users select all or carry selection across pages, the interface must state the '
               'effective selection model before consequential bulk actions.',
  'intent': 'Avoid “select all” ambiguity between one rendered page and an entire filtered dataset.',
  'applies_when': ['A paginated or virtualized collection supports multi-select and bulk actions.'],
  'does_not_apply_when': [],
  'failure_modes': ['The header checkbox looks fully selected on one page while the action actually targets '
                    'every record in the filtered query, or only the current page without explanation.'],
  'user_impacts': ['Users can delete, export, assign, or modify far more or fewer records than they intend.'],
  'observables': ['Select all on one page, navigate, change filters, and open a bulk-action preview while '
                  'tracking stable selected identities.'],
  'falsifiers': ['The UI distinguishes page selection, explicit cross-page selection, and all-query '
                 'selection and shows the effective count or scope before commit.'],
  'repairs': ['Represent selection mode separately from rendered checkboxes and require a scope-aware '
              'confirmation for large or dynamic query selections.'],
  'exceptions': [],
  'verification': ['Test page changes and filter mutation after select-all, verifying committed scope '
                   'matches the last explicit selection contract.'],
  'owner_hints': ['designing-bulk-action-toolbars'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.filtered-empty-distinct-from-dataset-empty',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Filtered empty results must remain distinct from an actually empty collection',
  'statement': 'An empty list should explain whether the underlying dataset has no records or current '
               'filters/search hide existing records, and offer the appropriate recovery action.',
  'intent': 'Prevent users from creating duplicates or concluding data was deleted when a query simply '
            'excludes it.',
  'applies_when': ['The same list supports filters or search and can also genuinely have no records.'],
  'does_not_apply_when': [],
  'failure_modes': ['Both states use the same “No items yet” message and creation CTA even when clearing a '
                    'filter would reveal existing records.'],
  'user_impacts': ['Users may create duplicate objects, escalate false data-loss concerns, or fail to remove '
                   'an accidental filter.'],
  'observables': ['Populate records, apply an excluding filter, then compare empty-state copy and actions '
                  'with a newly created truly empty scope.'],
  'falsifiers': ['The filtered-empty state exposes active query constraints and a clear path to broaden '
                 'them, while true-empty state can focus on creation or onboarding.'],
  'repairs': ['Derive empty-state variant from total dataset/query metadata rather than only the zero-length '
              'rendered result.'],
  'exceptions': [],
  'verification': ['Test hidden filters from deep links and saved views, verifying empty messaging always '
                   'reflects the real cause of zero results.'],
  'owner_hints': ['designing-empty-loading-error-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.list.deep-link-restores-list-context',
  'domain': 'list',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Deep links back to a collection must restore the relevant list context without reviving stale '
           'state',
  'statement': 'A link that represents list state should restore its declared filters, sort, scope, and '
               'anchor while revalidating transient selections or inaccessible records.',
  'intent': 'Make collection URLs reproducible without resurrecting unsafe ephemeral client state.',
  'applies_when': ['Lists support routable query state, saved views, or return-to-list navigation from item '
                   'detail.'],
  'does_not_apply_when': [],
  'failure_modes': ['Opening a copied URL restores some hidden local filters from the previous session or '
                    'loses the declared sort and anchor encoded in the link.'],
  'user_impacts': ['Collaborators can see a different dataset than the sender intended or users lose their '
                   'place when returning from detail.'],
  'observables': ['Copy list URLs with nondefault query state into clean sessions and compare canonical '
                  'query, visible controls, and focused anchor.'],
  'falsifiers': ['A clean client reconstructs the routable context from the link while ephemeral selection '
                 'and authorization-sensitive state are revalidated.'],
  'repairs': ['Define which list dimensions are serializable, encode them canonically, and avoid merging '
              'undeclared stale local state during route restoration.'],
  'exceptions': [],
  'verification': ['Exercise copied links, browser back/forward, and permission changes, verifying restored '
                   'context is reproducible and safe.'],
  'owner_hints': ['designing-pagination'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-list-navigation-owners-v13'],
  'status': 'active'}]

__all__ = ["LIST_NAVIGATION_RULES_V13"]
