"""V13 eighth-wave independently authored rules for threathunt."""
from __future__ import annotations

from ._capabilities import interaction_caps


THREAT_HUNT_RULES_V13 = [{'rule_id': 'ui.threathunt.query-time-range-authoritative',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Threat-hunt results must remain bound to the exact authoritative query time range',
  'statement': 'A hunt result set must expose the evaluated start, end, timezone, and relative-time '
               'resolution so analysts know which telemetry interval the backend actually searched.',
  'intent': 'Prevent investigations from reasoning over a different temporal scope than the query that '
            'produced the evidence.',
  'applies_when': ['Threat hunting queries can use explicit or relative time ranges across one or more '
                   'telemetry sources.'],
  'does_not_apply_when': [],
  'failure_modes': ['A saved query says “last 24 hours” but results are reopened later with no record '
                    'of the original evaluated timestamps.'],
  'user_impacts': ['Analysts can compare or bookmark evidence without knowing which events were '
                   'actually eligible for the original hunt.'],
  'observables': ['Run relative and absolute hunts, reopen them later, and compare displayed range, '
                  'backend parameters, bookmarks, and exports.'],
  'falsifiers': ['Each result snapshot records the resolved time interval used for execution and '
                 'distinguishes it from any newly edited query range.'],
  'repairs': ['Persist evaluated temporal parameters with each query attempt and display them alongside '
              'the human-friendly time expression.'],
  'exceptions': [],
  'verification': ['Rerun and reopen hunts across timezone and daylight-offset boundaries, verifying '
                   'each result snapshot keeps its original evaluated interval.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.partial-backend-coverage-visible',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Partial telemetry backend coverage must be visible in threat-hunt results',
  'statement': 'When one or more requested data sources fail, lag, or cannot cover the entire interval, '
               'the result set must not present itself as a complete negative or complete search.',
  'intent': 'Keep zero findings from being mistaken for evidence of absence when telemetry coverage is '
            'incomplete.',
  'applies_when': ['A hunt fans out across multiple indices, tenants, sensors, regions, or data '
                   'providers that can fail independently.'],
  'does_not_apply_when': [],
  'failure_modes': ['Three sources return zero matches while a fourth times out, and the UI shows a '
                    'single “No results” state.'],
  'user_impacts': ['Analysts can dismiss a hypothesis because the interface concealed a detection gap '
                   'rather than a true negative.'],
  'observables': ['Fail selected backends and inspect result counts, source coverage indicators, query '
                  'summary, saved hunt, and export.'],
  'falsifiers': ['Complete, partial, failed, and unavailable source coverage are separately represented '
                 'and remain attached to the result snapshot.'],
  'repairs': ['Aggregate backend outcomes alongside records and require negative-result surfaces to '
              'disclose incomplete coverage before implying absence.'],
  'exceptions': [],
  'verification': ['Exercise mixed success, timeout, permission denial, and lagging-source conditions '
                   'and verify coverage state remains explicit.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.schema-version-bound-to-query',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Threat-hunt query interpretation must be bound to the schema version used at execution',
  'statement': 'Field names, parser behavior, and entity mappings can evolve, so a saved hunt must '
               'retain enough schema context to explain how the executed query was interpreted.',
  'intent': 'Prevent historical hunts from silently changing meaning when telemetry schemas or mappings '
            'evolve.',
  'applies_when': ['Hunt queries reference fields or normalized entities whose schemas can be versioned '
                   'or migrated.'],
  'does_not_apply_when': [],
  'failure_modes': ['A saved query using process.name is reopened after a mapping migration and '
                    'executes against a different field semantics without warning.'],
  'user_impacts': ['Reproducing prior investigations can yield different populations for reasons '
                   'unrelated to new telemetry.'],
  'observables': ['Execute a query, change or simulate schema mapping, then reopen and rerun while '
                  'inspecting resolved fields and migration warnings.'],
  'falsifiers': ['The original execution keeps its schema context and reruns either reproduce that '
                 'context or explicitly disclose migration to a new interpretation.'],
  'repairs': ['Persist schema or mapping version with query attempts and require deliberate migration '
              'when a saved expression cannot preserve prior semantics.'],
  'exceptions': [],
  'verification': ['Run schema-versioned fixtures and verify historical result snapshots remain '
                   'explainable while reruns disclose any mapping change.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.result-pagination-snapshot-stable',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pagination through threat-hunt results must operate over a stable result snapshot',
  'statement': 'As new telemetry arrives, moving between result pages should not duplicate, omit, or '
               'reorder already evaluated records unless the analyst explicitly refreshes the hunt.',
  'intent': 'Keep investigative review deterministic while live data continues entering the underlying '
            'stores.',
  'applies_when': ['Hunt results are paginated or virtualized over datasets that can receive new events '
                   'during analyst review.'],
  'does_not_apply_when': [],
  'failure_modes': ['New high-timestamp events arrive after page one, shifting offsets so records move '
                    'between pages and some events are reviewed twice while others are skipped.'],
  'user_impacts': ['Analysts can miss evidence or believe they inspected a complete result set when '
                   'pagination changed underneath them.'],
  'observables': ['Page through a large result set while injecting new telemetry and compare stable '
                  'event identities across page transitions.'],
  'falsifiers': ['Within one result snapshot, each event identity appears at a stable logical position '
                 'or cursor and refresh is the explicit boundary for new data.'],
  'repairs': ['Use cursor or snapshot-bound pagination and separate refresh semantics from navigation '
              'through the existing result set.'],
  'exceptions': [],
  'verification': ['Inject records during traversal and verify the current snapshot has no duplicate or '
                   'missing identities; refresh should create a new snapshot deliberately.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.evidence-bookmark-stable',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bookmarked hunt evidence must resolve to stable event identity rather than transient row '
           'position',
  'statement': 'Analyst bookmarks, annotations, and case links should bind to durable telemetry '
               'identity so sorting, pagination, or reruns cannot retarget them to a different event.',
  'intent': 'Ensure investigative notes continue referring to the evidence the analyst actually '
            'selected.',
  'applies_when': ['Threat-hunt results allow bookmarking or sending individual events to another '
                   'investigative surface.'],
  'does_not_apply_when': [],
  'failure_modes': ['A bookmark stores page number and row index; after sorting changes, opening it '
                    'highlights a different event with the same row position.'],
  'user_impacts': ['Case conclusions and notes can become attached to unrelated telemetry without any '
                   'obvious error.'],
  'observables': ['Bookmark events, change sort, filters, pagination, and rerun the query, then reopen '
                  'bookmarks and compare stable identifiers.'],
  'falsifiers': ['Each bookmark resolves to the same underlying event or explicitly reports that the '
                 'event is no longer retrievable.'],
  'repairs': ['Persist source plus stable event identity and use query position only as optional '
              'presentation context, never as bookmark authority.'],
  'exceptions': [],
  'verification': ['Reorder and refresh hunt results repeatedly, verifying bookmarks and annotations '
                   'never migrate to a different event.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.query-modification-diff-visible',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Modifying a saved threat-hunt query must make the semantic diff from the prior version '
           'inspectable',
  'statement': 'Changes to filters, time range, joins, entity scope, or data sources should be '
               'reviewable so analysts can tell why two executions cover different populations.',
  'intent': 'Preserve investigative reasoning when hunts evolve through iterative hypothesis testing.',
  'applies_when': ['Analysts edit and rerun saved hunts during an investigation or share them with '
                   'teammates.'],
  'does_not_apply_when': [],
  'failure_modes': ['A teammate removes an exclusion and changes the entity scope, but the next result '
                    'set is displayed with the same saved-hunt name and no visible change history.'],
  'user_impacts': ['Differences in findings can be attributed to telemetry rather than to silent query '
                   'edits, corrupting investigative conclusions.'],
  'observables': ['Create several query revisions and compare stored expressions, resolved parameters, '
                  'execution snapshots, and change history.'],
  'falsifiers': ['Each execution identifies the query revision used and analysts can inspect the '
                 'material differences between revisions.'],
  'repairs': ['Version saved hunt definitions and expose structured or textual diffs for parameters '
              'that influence result membership.'],
  'exceptions': [],
  'verification': ['Change filters, source sets, and time semantics, then verify executions remain tied '
                   'to their exact query revision and differences are recoverable.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.async-query-cancel-stops-authority',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Canceling an asynchronous hunt must stop that attempt from becoming the authoritative '
           'result',
  'statement': 'If an analyst cancels a long-running query, late backend responses from that attempt '
               'must not overwrite a newer hunt or appear as a completed authoritative result.',
  'intent': 'Prevent stale asynchronous work from replacing the investigation state the analyst '
            'intentionally moved on from.',
  'applies_when': ['Hunt execution is asynchronous and multiple attempts can overlap because of rerun, '
                   'edit, or cancellation.'],
  'does_not_apply_when': [],
  'failure_modes': ['Attempt A is canceled and attempt B is started, but A completes later and the UI '
                    'replaces B’s partial results with A as if cancellation never happened.'],
  'user_impacts': ['Analysts can act on results from a query they deliberately abandoned or from '
                   'parameters no longer visible.'],
  'observables': ['Start overlapping hunts with controlled response delays, cancel older attempts, and '
                  'watch result ownership and saved-history state.'],
  'falsifiers': ['Canceled attempts remain canceled even if backends finish later, while their late '
                 'responses cannot become the current authoritative result.'],
  'repairs': ['Assign immutable attempt identities and gate result promotion on current execution '
              'state, discarding or quarantining late canceled responses.'],
  'exceptions': [],
  'verification': ['Race cancel, edit, and rerun operations across slow backends and verify only the '
                   'active attempt can own current results.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.threathunt.zero-results-distinct-from-detection-gap',
  'domain': 'threathunt',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Zero threat-hunt matches must remain distinct from telemetry or parser detection gaps',
  'statement': 'A result count of zero should only mean no records matched the evaluated query over '
               'available coverage, not that a parser failed, a field was absent, or a source produced '
               'no usable telemetry.',
  'intent': 'Keep absence-of-match semantics separate from inability-to-detect semantics.',
  'applies_when': ['Hunts depend on parsers, normalized fields, telemetry availability, or enrichment '
                   'that can fail independently from query execution.'],
  'does_not_apply_when': [],
  'failure_modes': ['A field extractor stops producing process hashes and the query returns zero, but '
                    'the UI labels the hunt clean instead of exposing the extraction gap.'],
  'user_impacts': ['Analysts can wrongly conclude an adversary behavior is absent because the interface '
                   'collapsed data-quality failure into a negative result.'],
  'observables': ['Break parser output and telemetry coverage independently while running '
                  'known-positive and known-negative hunt fixtures.'],
  'falsifiers': ['Zero-match results state the evaluated coverage, and parser or telemetry gaps surface '
                 'as separate degradations that prevent a clean negative interpretation.'],
  'repairs': ['Propagate data-quality and parser health into result metadata and reserve “no matches” '
              'for queries that actually evaluated usable data.'],
  'exceptions': [],
  'verification': ['Test known positives under normal and degraded telemetry, verifying the UI '
                   'distinguishes true zero matches from unavailable detection capability.'],
  'owner_hints': ['designing-threat-hunting-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-threat-hunt-owners-v13'],
  'status': 'active'}]


__all__ = ["THREAT_HUNT_RULES_V13"]
