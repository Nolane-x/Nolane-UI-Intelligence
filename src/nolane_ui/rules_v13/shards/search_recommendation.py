"""V13 search and recommendation rules for query state, result identity, personalization, and explanation truth."""
from __future__ import annotations

from ._capabilities import interaction_caps


SEARCH_RECOMMENDATION_RULES_V13 = [
    {'rule_id': 'ui.search.query-and-filter-state-distinct',
     'domain': 'search',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Search query text and structured filter state must remain separately recoverable',
     'statement': 'A search surface must not collapse free-text query and structured filters into one opaque display '
                  'value when users can independently edit, clear, save, or share those dimensions.',
     'intent': 'Preserve the actual search contract so clearing text does not silently remove filters and editing a '
               "filter does not rewrite the user's query.",
     'applies_when': ['The search experience combines a text query with facets, ranges, scopes, or structured filter '
                      'builders.'],
     'does_not_apply_when': [],
     'failure_modes': ['Query and filters are serialized into one label or local state such that clearing or restoring '
                       'one dimension unintentionally mutates the other.'],
     'user_impacts': ['Users can lose carefully chosen constraints, share a search that means something different, or '
                      'misread why results are included.'],
     'observables': ['Compose searches with text plus multiple filters, clear and restore each dimension, reload or '
                     'share the state, and compare the resulting query contract.'],
     'falsifiers': ['Text query and structured filters survive independent edits and round-trip through any supported '
                    'saved or shareable representation without semantic loss.'],
     'repairs': ['Store query and filter AST or descriptors separately and derive human-readable summaries rather than '
                 'using the summary string as the source of truth.'],
     'exceptions': [],
     'verification': ['Test clear-query, clear-one-filter, back navigation, saved search, shared URL, and restore and '
                      'verify each dimension remains independent.'],
     'owner_hints': ['designing-search-filter-builders'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.search.saved-search-definition-change-visible',
     'domain': 'search',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Saved searches must expose when their effective definition changed since creation',
     'statement': 'If a saved search depends on mutable defaults, taxonomy, available fields, organization scope, or '
                  'ranking configuration, the product should make a material definition change visible instead of '
                  'presenting the saved view as if it still means exactly what the user stored.',
     'intent': 'Protect saved-search intent from silent semantic drift as the product schema or search configuration '
               'evolves.',
     'applies_when': ['Saved searches can outlive changes to filter fields, default scopes, category taxonomies, '
                      'permissions, or query interpretation.'],
     'does_not_apply_when': [],
     'failure_modes': ['Opening an old saved search silently drops unsupported filters, widens scope, or reinterprets '
                       'values without telling the user its effective definition changed.'],
     'user_impacts': ['Users can make decisions from a view they believe is stable even though the product is now '
                      'querying a materially different set of records.'],
     'observables': ['Create saved searches, mutate schema and defaults in controlled fixtures, reopen them, and compare '
                     'stored definition with the effective query executed.'],
     'falsifiers': ['Material incompatibilities or migrations are surfaced, while compatible representation changes '
                    'preserve the stored search semantics.'],
     'repairs': ['Version saved-search definitions and perform explicit migration with a visible changed-definition '
                 'state when semantics cannot be preserved exactly.'],
     'exceptions': [],
     'verification': ['Test removed fields, renamed values, permission narrowing, default-scope changes, and ranking '
                      'changes and verify the saved search reports material drift.'],
     'owner_hints': ['designing-saved-searches-and-views'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.search.zero-results-distinct-from-search-failure',
     'domain': 'search',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'A valid zero-result search must be distinct from a failed or incomplete search',
     'statement': 'An empty result list may be shown only after a search completes successfully with zero matches; '
                  'network failure, parsing failure, authorization failure, or cancelled retrieval must retain their own '
                  'states.',
     'intent': 'Keep absence of matching data separate from inability to execute the search so recovery actions and user '
               'conclusions remain accurate.',
     'applies_when': ['The search request can fail, be cancelled, time out, or be blocked independently of the '
                      'underlying dataset containing zero matches.'],
     'does_not_apply_when': [],
     'failure_modes': ['Any failed request renders the normal no-results illustration and copy, suggesting that the '
                       'query was valid and nothing matched.'],
     'user_impacts': ['Users may weaken filters, assume data is absent, or stop searching when the system actually never '
                      'produced a valid result set.'],
     'observables': ['Force true zero matches and each request failure class, then compare query execution status, '
                     'empty-state copy, retry controls, and result-count semantics.'],
     'falsifiers': ['No-results appears only from a completed successful search; failures and incomplete states identify '
                    'the actual missing execution evidence.'],
     'repairs': ['Drive the result surface from an explicit search lifecycle with distinct completed-empty, failed, '
                 'cancelled, unauthorized, and loading branches.'],
     'exceptions': [],
     'verification': ['Test network, parser, permission, timeout, cancellation, and true-zero fixtures and verify only '
                      'the last case enters the zero-results state.'],
     'owner_hints': ['designing-search-result-interfaces'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.search.pagination-does-not-repeat-result-identity',
     'domain': 'search',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Paginated and infinite search results must not duplicate stable result identities across page boundaries',
     'statement': 'When search results are loaded in pages or cursor windows, items already present must not reappear as '
                  'new results solely because ranking shifted between requests or the client appended overlapping pages.',
     'intent': 'Keep incremental result loading stable enough that users can distinguish genuinely new records from '
               'retrieval-window overlap.',
     'applies_when': ['A search result surface appends remote pages, cursors, or infinite-scroll windows while the '
                      'underlying dataset or ranking can change.'],
     'does_not_apply_when': [],
     'failure_modes': ['The same stable record ID appears multiple times in the visible result set because page offsets '
                       'shifted or cursor overlap was not reconciled.'],
     'user_impacts': ['Users can waste actions on duplicates, misread result volume, or lose place as repeated entries '
                      'displace unseen results.'],
     'observables': ['Load multiple pages while inserting and reprioritizing records server-side, then inspect visible '
                     'stable IDs and pagination cursors for overlap.'],
     'falsifiers': ['Each logical result identity appears once in the current result collection unless the product '
                    'intentionally represents distinct occurrences with distinct identities.'],
     'repairs': ['Reconcile appended windows by stable result ID and prefer cursor semantics that remain valid under the '
                 "product's ranking mutation model."],
     'exceptions': [],
     'verification': ['Test offset and cursor pagination under inserts, deletes, and ranking changes and verify no '
                      'accidental duplicate identities enter the merged result set.'],
     'owner_hints': ['designing-search-result-interfaces'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.recommendation.personalization-toggle-changes-effective-ranking-input',
     'domain': 'recommendation',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Personalization controls must change the effective ranking inputs they claim to control',
     'statement': 'If a product offers a personalization off, reset, or reduced-personalization control, the '
                  'recommendation request and ranking context must actually stop using the covered signals rather than '
                  'only changing the control label.',
     'intent': 'Bind privacy and agency controls to the recommendation system inputs they describe so the visible '
               'preference has operational effect.',
     'applies_when': ['The recommendation surface exposes a user control that claims to disable, reset, or constrain '
                      'personalization signals.'],
     'does_not_apply_when': [],
     'failure_modes': ['The toggle updates settings UI but requests continue sending or consuming the same covered '
                       'personalization profile without a documented delayed boundary.'],
     'user_impacts': ['Users can believe they changed recommendation behavior while the system continues using the very '
                      'inputs the control says are disabled.'],
     'observables': ['Capture recommendation request context before and after each personalization control transition '
                     'and compare server-side effective ranking inputs with the visible preference.'],
     'falsifiers': ['The covered signals are removed, reset, or bounded according to the control semantics, and '
                    'unavoidable retained signals are disclosed separately rather than hidden.'],
     'repairs': ['Connect the control to the ranking-profile or request-building layer and expose any delayed or partial '
                 'effect explicitly.'],
     'exceptions': [],
     'verification': ['Test disable, re-enable, reset history, cross-device preference sync, and cached recommendations '
                      'and verify the effective input set follows the declared state.'],
     'owner_hints': ['designing-recommendation-personalization-surfaces'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.recommendation.feedback-target-bound-to-item',
     'domain': 'recommendation',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Recommendation feedback must remain bound to the item the user actually rated or dismissed',
     'statement': 'Like, dislike, not interested, save, or similar feedback must reference the stable recommendation '
                  'identity that was acted on even if the feed reranks or recycles cards before the mutation completes.',
     'intent': 'Prevent asynchronous feed movement from applying preference signals to a different recommendation than '
               'the one the user selected.',
     'applies_when': ['A recommendation feed can reorder, virtualize, refresh, or replace items while user feedback '
                      'requests are pending.'],
     'does_not_apply_when': [],
     'failure_modes': ['Feedback is keyed by visible index or recycled component state and lands on whichever item '
                       'occupies that position when the async handler runs.'],
     'user_impacts': ['Users can train or curate the system in the opposite direction from their intent and may see the '
                      'wrong item disappear or change state.'],
     'observables': ['Act on recommendations while forcing rapid rerank and virtualization, then compare submitted '
                     'feedback IDs with the identities visible at the interaction moment.'],
     'falsifiers': ['Every feedback operation is bound to the stable target identity captured at the action boundary and '
                    "reconciles only that item's state."],
     'repairs': ['Capture target identity synchronously with the user action and carry it through optimistic UI, '
                 'request, response, and rollback paths.'],
     'exceptions': [],
     'verification': ['Test fast scrolling, reranking, duplicate-looking items, undo, and offline feedback and verify '
                      'each mutation targets the intended recommendation ID.'],
     'owner_hints': ['designing-recommendation-personalization-surfaces'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.recommendation.explanation-does-not-invent-ranking-precision',
     'domain': 'recommendation',
     'class': 'contextual',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Recommendation explanations must not invent precise causal weights the ranking system cannot support',
     'statement': 'Explanations such as recommended because of, matched on, or scored for you must stay within evidence '
                  'the recommendation system can actually attribute and must not present fabricated percentages or '
                  'singular causes for opaque multi-signal ranking.',
     'intent': 'Give users useful provenance without converting a heuristic explanation into false certainty about model '
               'causality.',
     'applies_when': ['The product displays an explanation for why an item was recommended or how strongly a signal '
                      'influenced its rank.'],
     'does_not_apply_when': [],
     'failure_modes': ['The UI states an exact causal weight, probability, or single definitive reason that is not '
                       'produced or validated by the underlying ranking system.'],
     'user_impacts': ['Users can over-trust the explanation, misunderstand how to change recommendations, or infer '
                      'sensitive profiling that the system did not actually use.'],
     'observables': ["Compare displayed recommendation explanations with the ranking service's available attribution or "
                     'reason codes across diverse result cases.'],
     'falsifiers': ['Every explanation is bounded to supported reason evidence and uncertain or multi-factor attribution '
                    'remains appropriately qualified.'],
     'repairs': ['Generate explanations from actual reason codes or validated attribution outputs and remove invented '
                 'numeric precision or unsupported causal language.'],
     'exceptions': [],
     'verification': ['Test recommendations with no reason code, multiple signals, sparse history, and fallback ranking '
                      'and verify explanations never exceed available evidence.'],
     'owner_hints': ['designing-recommendation-explanations'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.recommendation.dismissed-item-does-not-immediately-reappear-with-same-identity',
     'domain': 'recommendation',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'A dismissed recommendation should not immediately reappear as the same item without explaining why',
     'statement': 'When a user explicitly dismisses or marks a recommendation not interested and the product claims that '
                  'action affects the feed, the same stable item should not immediately re-enter the same context '
                  'through reranking or pagination unless the product exposes a bounded reason.',
     'intent': 'Make negative feedback visibly effective rather than allowing feed mechanics to negate the control '
               'seconds later.',
     'applies_when': ['The recommendation interface offers item-level dismissal or negative feedback intended to remove '
                      'or suppress that recommendation in the current context.'],
     'does_not_apply_when': [],
     'failure_modes': ['The dismissed stable item is fetched again in the next page or rerank and appears '
                       'indistinguishably as a fresh recommendation.'],
     'user_impacts': ['Users lose trust in feedback controls and may repeat actions without understanding whether the '
                      'system recorded them.'],
     'observables': ['Dismiss items, trigger refresh, pagination, model rerank, and device sync, then compare returned '
                     'stable IDs and suppression state.'],
     'falsifiers': ['The dismissed item remains suppressed for the product-defined scope and duration, or its '
                    'reappearance explicitly indicates why the prior feedback no longer applies.'],
     'repairs': ['Carry suppression identifiers into feed assembly and deduplicate incoming recommendation windows '
                 'against active feedback state.'],
     'exceptions': [],
     'verification': ['Test session refresh, infinite-scroll pagination, cross-device sync, and feedback expiry and '
                      'verify reappearance follows the declared suppression contract.'],
     'owner_hints': ['designing-recommendation-personalization-surfaces'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-search-recommendation-owners-v13'],
     'status': 'active'},
]

__all__ = ['SEARCH_RECOMMENDATION_RULES_V13']
