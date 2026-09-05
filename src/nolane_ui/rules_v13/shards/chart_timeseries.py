"""V13 seventh-wave independently authored rules for chart timeseries."""
from __future__ import annotations

from ._capabilities import interaction_caps


CHART_TIMESERIES_RULES_V13 = [{'rule_id': 'ui.chart.axis-scale-and-baseline-visible',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Charts must expose scale and baseline choices that materially affect visual interpretation',
  'statement': 'A quantitative chart must make nonzero baselines, logarithmic scales, reversed axes, dual '
               'axes, or other interpretation-changing scale choices visible rather than relying on shape '
               'alone.',
  'intent': 'Keep visual magnitude claims traceable to the coordinate system actually used.',
  'applies_when': ['A chart encodes quantities where axis transformation or baseline choice can change '
                   'perceived difference.'],
  'does_not_apply_when': [],
  'failure_modes': ['A truncated or logarithmic axis makes a small change look dramatic while no visible '
                    'label indicates the transformation.'],
  'user_impacts': ['Users can infer the wrong magnitude or direction from an otherwise accurate dataset.'],
  'observables': ['Render the same data under default and transformed scales and inspect labels, ticks, '
                  'accessible descriptions, and exported image context.'],
  'falsifiers': ['Any interpretation-changing scale is explicitly indicated and the encoded positions match '
                 'the declared axis mapping.'],
  'repairs': ['Surface scale type and baseline in axis semantics and preserve that context in tooltips, '
              'accessible equivalents, and exports.'],
  'exceptions': [],
  'verification': ['Test zero, nonzero, log, reversed, and dual-axis variants, confirming no transformed '
                   'scale is visually silent.'],
  'owner_hints': ['designing-data-visualization'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.legend-series-mapping-stable',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Legend entries must remain stably mapped to the same series across filtering and reordering',
  'statement': 'A legend must preserve the identity relationship between label, visual encoding, and '
               'underlying series when data order, visibility, or filters change.',
  'intent': 'Prevent users from reading a line, bar, or area as another series after dynamic updates.',
  'applies_when': ['The chart contains multiple series whose rendered order can change with filtering, '
                   'sorting, or live data.'],
  'does_not_apply_when': [],
  'failure_modes': ['Color or marker assignment is regenerated from array position so hiding one series '
                    'causes remaining series to inherit different legend encodings.'],
  'user_impacts': ['Users can attribute values or trends to the wrong entity even though each individual '
                   'value is numerically correct.'],
  'observables': ['Toggle series visibility and reorder source data while tracking stable series IDs, '
                  'rendered encoding, and legend labels.'],
  'falsifiers': ['Each series keeps an identity-bound encoding or any intentional remapping is explicit and '
                 'updates chart plus legend atomically.'],
  'repairs': ['Key visual encodings by stable series identity rather than transient array index and '
              'centralize legend mapping.'],
  'exceptions': [],
  'verification': ['Exercise filters, live insertion, and saved views, verifying series identity never '
                   'changes because neighboring series appear or disappear.'],
  'owner_hints': ['designing-data-visualization'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.missing-data-gap-not-rendered-as-zero',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Missing time-series observations must not be silently rendered as measured zeros',
  'statement': 'When data is absent, delayed, or unknown, the chart must distinguish that state from a '
               'genuine observed value of zero unless the domain explicitly defines missing as zero.',
  'intent': 'Preserve the difference between no evidence and evidence of no quantity.',
  'applies_when': ['A series can contain null, missing, delayed, or unavailable intervals alongside '
                   'legitimate zero values.'],
  'does_not_apply_when': [],
  'failure_modes': ['The renderer coerces null samples to zero or connects through them in a way that '
                    'implies a measured decline and recovery.'],
  'user_impacts': ['Users can infer outages, performance drops, or business events that never occurred in '
                   'the underlying data.'],
  'observables': ['Provide identical sequences with explicit zero and missing samples and compare lines, '
                  'points, tooltips, and nonvisual representations.'],
  'falsifiers': ['Missing observations are visually and semantically distinguishable from zero, with '
                 'interpolation used only under an explicitly defined policy.'],
  'repairs': ['Preserve missingness in the data pipeline and map it to gaps or uncertainty treatment rather '
              'than numeric coercion.'],
  'exceptions': [],
  'verification': ['Test null, delayed, zero, and interpolated policies across exports and accessible '
                   'equivalents, confirming their meanings remain distinct.'],
  'owner_hints': ['designing-time-series-exploration'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.aggregation-window-visible',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Aggregated chart values must reveal the time or population window they summarize',
  'statement': 'A chart that rolls up records into bins, moving windows, percentiles, or period summaries '
               'must expose the effective aggregation window and statistic.',
  'intent': 'Allow users to interpret a point as an aggregate rather than as a raw instantaneous '
            'observation.',
  'applies_when': ['Raw records are summarized over time buckets, groups, rolling windows, or statistical '
                   'functions before visualization.'],
  'does_not_apply_when': [],
  'failure_modes': ['A point labelled 10:00 appears to be an instantaneous value even though it represents '
                    'an hourly average or trailing seven-day metric.'],
  'user_impacts': ['Users can compare incompatible values or draw conclusions about events at times the '
                   'aggregate does not precisely represent.'],
  'observables': ['Switch aggregation granularity and statistic while inspecting axis labels, tooltips, '
                  'chart title, and data export.'],
  'falsifiers': ['The aggregate function and effective window are available wherever a user needs them to '
                 'interpret or compare values.'],
  'repairs': ['Carry aggregation metadata through the query and visualization layer and include it in labels '
              'or contextual details.'],
  'exceptions': [],
  'verification': ['Compare raw, hourly, daily, trailing-window, and percentile views, verifying every '
                   'rendered value exposes its summarization basis.'],
  'owner_hints': ['designing-time-series-exploration'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.cross-filter-source-and-scope-visible',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cross-filtered charts must expose which selection currently constrains other views',
  'statement': 'When clicking or brushing one visualization filters other data, the active source selection '
               'and affected scope must remain visible and reversible.',
  'intent': 'Prevent hidden cross-filter state from making downstream charts look like complete datasets.',
  'applies_when': ['A dashboard or analytical workspace supports chart-to-chart filtering or brushing.'],
  'does_not_apply_when': [],
  'failure_modes': ['Selecting one segment changes several charts but leaves no persistent filter indicator '
                    'after hover ends.'],
  'user_impacts': ['Users can report or export a subset believing it represents the full population.'],
  'observables': ['Apply cross-filters from several charts, navigate among panels, and inspect filter '
                  'indicators, reset paths, and query payloads.'],
  'falsifiers': ['The active source selection and downstream filter scope remain discoverable until '
                 'explicitly cleared.'],
  'repairs': ['Represent cross-filter state in the same canonical query model as ordinary filters and '
              'surface its origin in affected views.'],
  'exceptions': [],
  'verification': ['Stack multiple cross-filters and clear them in different orders, verifying every chart '
                   'and export reflects the visible canonical filter state.'],
  'owner_hints': ['designing-cross-filtering'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.tooltip-value-time-basis-visible',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Chart tooltips must identify the timestamp or interval that gives each value meaning',
  'statement': 'A tooltip for time-indexed data must state whether a value belongs to an instant, local day, '
               'UTC bucket, market session, or interval when that distinction affects interpretation.',
  'intent': 'Avoid attaching a precise value to an ambiguous time label.',
  'applies_when': ['Chart points summarize data whose time semantics differ by zone, session, or interval '
                   'boundaries.'],
  'does_not_apply_when': [],
  'failure_modes': ['A tooltip says “Jan 3 — 42” while the value is actually a UTC day bucket that spans '
                    'different local dates for the viewer.'],
  'user_impacts': ['Users can correlate the point with the wrong business event or compare values from '
                   'mismatched periods.'],
  'observables': ['Change viewer time zone and bucket semantics while inspecting tooltip labels and '
                  'underlying query intervals.'],
  'falsifiers': ['Tooltip time context maps to the exact interval or instant used to compute the value and '
                 'remains consistent with axis and export semantics.'],
  'repairs': ['Bind tooltip labels to the same canonical temporal metadata used by aggregation rather than '
              'formatting a display-only x value.'],
  'exceptions': [],
  'verification': ['Test local, UTC, session, and interval data near date boundaries, verifying tooltip time '
                   'never changes the underlying meaning silently.'],
  'owner_hints': ['designing-time-series-exploration'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.zoom-selection-reset-state-visible',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Chart zoom or brush state must remain visible and offer a clear reset to the full domain',
  'statement': 'When users zoom, pan, or brush into a subset, the chart must communicate that its current '
               'domain is restricted and provide a deterministic way back to the baseline extent.',
  'intent': 'Prevent a cropped view from masquerading as the full dataset after interaction.',
  'applies_when': ['An interactive chart supports zooming, panning, range brushing, or drill-in that changes '
                   'visible domain.'],
  'does_not_apply_when': [],
  'failure_modes': ['After zooming, axes rescale but no control or indicator shows that earlier or later '
                    'data is excluded.'],
  'user_impacts': ['Users may conclude data outside the viewport does not exist or compare a zoomed view '
                   'against an unzoomed peer.'],
  'observables': ['Zoom and pan through several nested extents, then navigate away and back while inspecting '
                  'domain labels and reset behavior.'],
  'falsifiers': ['Restricted domain state is discoverable and reset restores the defined baseline extent '
                 'without altering unrelated filters.'],
  'repairs': ['Persist chart-domain interaction state separately from data filters and surface a clear reset '
              'or breadcrumb for that domain.'],
  'exceptions': [],
  'verification': ['Exercise touch, mouse wheel, brush, and saved-view restoration, verifying restricted and '
                   'full extents cannot be confused.'],
  'owner_hints': ['designing-time-series-exploration'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.chart.nonvisual-equivalent-uses-same-data',
  'domain': 'chart',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Nonvisual chart equivalents must derive from the same filtered and transformed dataset as the '
           'graphic',
  'statement': 'Tables, summaries, or accessible descriptions offered as chart alternatives must reflect the '
               'same series visibility, filters, aggregation, and time range as the rendered visualization.',
  'intent': 'Ensure alternative access is equivalent rather than a stale or differently scoped dataset.',
  'applies_when': ['A chart provides a table, screen-reader summary, data view, or downloadable equivalent '
                   'for nonvisual access.'],
  'does_not_apply_when': [],
  'failure_modes': ['The visual chart is filtered to one segment while the accessible table still contains '
                    'all records or uses a different aggregation.'],
  'user_impacts': ['Users relying on the alternative receive materially different information and cannot '
                   'participate in the same analysis.'],
  'observables': ['Apply filters, hide series, change time range and aggregation, then compare stable '
                  'record/value identities across graphic and nonvisual representations.'],
  'falsifiers': ['Alternative and visual representations consume the same canonical transformed dataset or '
                 'explicitly disclose intentional additional context.'],
  'repairs': ['Generate all presentation modes from one query/transform result and test equality at the data '
              'boundary before rendering.'],
  'exceptions': [],
  'verification': ['Exercise every chart interaction and verify the nonvisual equivalent updates to the same '
                   'values, labels, missingness, and scope.'],
  'owner_hints': ['designing-nonvisual-chart-equivalents'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-chart-timeseries-owners-v13'],
  'status': 'active'}]

__all__ = ["CHART_TIMESERIES_RULES_V13"]
