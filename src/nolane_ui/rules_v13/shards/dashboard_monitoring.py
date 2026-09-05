"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

DASHBOARD_MONITORING_RULES_V13 = [{'rule_id': 'ui.dashboard.metric-time-window-visible',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dashboard metrics must expose the time window used to compute the displayed value',
  'statement': 'A metric, trend, rate, count, or aggregate used for monitoring must make its active time window or '
               'as-of boundary visible when changing that window can materially change interpretation.',
  'intent': 'Prevent operators from reading the right number against the wrong period when dashboards mix live, '
            'rolling, daily, and custom-range data.',
  'applies_when': ['A dashboard metric depends on a configurable or implicit time range, sampling interval, '
                   'reporting period, or as-of timestamp.'],
  'does_not_apply_when': [],
  'failure_modes': ['A value is displayed without enough temporal context to distinguish whether it represents the '
                    'last minute, hour, day, reporting period, or current snapshot.'],
  'user_impacts': ['Users can misdiagnose incidents, performance, finances, or operational health because they '
                   'compare metrics computed over incompatible windows.'],
  'observables': ['Change the dashboard time control and inspect whether each affected metric exposes the resulting '
                  'period or inherited time context.'],
  'falsifiers': ['The active window is visible globally or locally in a way that unambiguously binds the displayed '
                 'metric to its temporal basis.'],
  'repairs': ['Propagate time-window metadata with metric values and render inherited or overridden ranges at the '
              'point where interpretation depends on them.'],
  'exceptions': [],
  'verification': ['Switch among live, rolling, fixed, and custom ranges and confirm metric labels, drilldowns, '
                   'exports, and refreshed values retain the same time basis.'],
  'owner_hints': ['designing-dashboard-filter-scope'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.stale-data-state-visible',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Monitoring surfaces must distinguish stale data from fresh authoritative telemetry',
  'statement': 'A dashboard that cannot refresh one or more data sources must expose the age or stale state of the '
               'retained values instead of continuing to present old telemetry as current.',
  'intent': 'Keep operational decisions bounded by data freshness when caches, polling, streaming, or upstream '
            'systems fail.',
  'applies_when': ['The dashboard can continue displaying previously loaded data after a source refresh, '
                   'subscription, query, or telemetry path stops updating.'],
  'does_not_apply_when': [],
  'failure_modes': ['Old values remain visually indistinguishable from fresh data after the product knows the source '
                    'has stopped updating.'],
  'user_impacts': ['Operators can assume a system is healthy or unchanged while actually acting on obsolete '
                   'telemetry.'],
  'observables': ['Interrupt the data source after a successful load and compare timestamps, freshness indicators, '
                  'and rendered values as time passes.'],
  'falsifiers': ['The dashboard marks affected values stale or shows their last authoritative update without '
                 'fabricating freshness it cannot verify.'],
  'repairs': ['Track freshness per source or metric and surface stale state independently from the cached value so '
              'useful historical data can remain visible.'],
  'exceptions': [],
  'verification': ['Pause polling, sever a stream, and restore connectivity while confirming stale indicators '
                   'appear, persist, and clear only after fresh evidence arrives.'],
  'owner_hints': ['designing-live-signal-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.alert-threshold-context-visible',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Alert indicators must expose the threshold or policy context that caused the alert',
  'statement': 'When a dashboard marks a metric as warning, critical, breached, or anomalous, the user must be able '
               'to discover the threshold, comparison basis, or policy that produced that state.',
  'intent': 'Make alert color and severity interpretable instead of treating red or warning badges as unexplained '
            'visual authority.',
  'applies_when': ['Monitoring UI derives alert state from configured thresholds, baselines, policies, service '
                   'objectives, or rule evaluation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A metric is marked critical but the interface gives no way to determine which threshold or '
                    'policy was crossed or what value would clear it.'],
  'user_impacts': ['Operators can overreact, underreact, or tune the wrong rule because alert severity lacks a '
                   'visible decision basis.'],
  'observables': ['Trigger alerts through different threshold or policy configurations and inspect whether the '
                  'rendered state exposes the active evaluation context.'],
  'falsifiers': ['Users can identify the governing threshold or rule and the observed value that caused the alert '
                 'without relying on hidden implementation knowledge.'],
  'repairs': ['Attach policy identifiers and evaluated threshold context to alert state and surface them in '
              'drilldown, detail, or accessible description.'],
  'exceptions': [],
  'verification': ['Change alert policies and thresholds while holding metric values constant and confirm the '
                   'displayed rationale updates to the active configuration.'],
  'owner_hints': ['designing-alert-triage-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.drilldown-preserves-filter-context',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dashboard drilldown must preserve the filter context that produced the selected aggregate',
  'statement': 'Opening detail from an aggregate, chart segment, card, or alert must carry the relevant time, scope, '
               'environment, cohort, and filter context so the detail explains the selected value.',
  'intent': 'Keep drilldown causally connected to the observation that motivated it instead of dropping users into a '
            'broader unrelated dataset.',
  'applies_when': ['A dashboard aggregate or visualization links to a detailed table, trace, log, record set, or '
                   'analysis surface.'],
  'does_not_apply_when': [],
  'failure_modes': ['The drilldown opens with default filters and shows data that cannot reproduce or explain the '
                    'aggregate the user selected.'],
  'user_impacts': ['Users can waste time investigating the wrong population and may conclude that the dashboard and '
                   'detail views contradict each other.'],
  'observables': ['Apply non-default filters, select a specific aggregate or segment, and compare the resulting '
                  'detail query context with the source dashboard state.'],
  'falsifiers': ['The drilldown carries or explicitly represents the relevant inherited filters, while any '
                 'intentionally broadened scope is clearly disclosed.'],
  'repairs': ['Encode drilldown context in navigation state or query parameters and initialize the destination from '
              'that context rather than global defaults.'],
  'exceptions': [],
  'verification': ['Drill from filtered metrics, chart segments, saved views, and alerts and confirm the destination '
                   'can reproduce the source population.'],
  'owner_hints': ['designing-dashboard-drilldown'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.partial-aggregate-distinct-from-complete',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Aggregates computed from partial data must not look like complete population results',
  'statement': 'If a dashboard metric or chart is based on sampled, delayed, permission-limited, timed-out, or '
               'otherwise incomplete input, the result must expose that partial basis rather than presenting a '
               'definitive total.',
  'intent': 'Protect interpretation when the aggregation engine can return a useful but incomplete result before all '
            'contributing data is available.',
  'applies_when': ['The analytical backend can produce values from partial partitions, incomplete pagination, '
                   'sampled datasets, delayed sources, or bounded query time.'],
  'does_not_apply_when': [],
  'failure_modes': ['A partial aggregate is formatted like a final complete value with no indication that records or '
                    'sources were excluded.'],
  'user_impacts': ['Users can make operational or financial decisions from an understated or distorted metric while '
                   'believing the full population was measured.'],
  'observables': ['Force one contributing source or partition to time out and compare returned completeness metadata '
                  'with the rendered aggregate state.'],
  'falsifiers': ['Partial results are labelled with their incompleteness or withheld until complete when the product '
                 'cannot support a meaningful partial interpretation.'],
  'repairs': ['Propagate completeness metadata through aggregation and render it alongside values, confidence, or '
              'source coverage as appropriate.'],
  'exceptions': [],
  'verification': ['Test full, partial, sampled, and permission-limited datasets and confirm the same visual value '
                   'cannot imply completeness across different coverage states.'],
  'owner_hints': ['designing-instrument-telemetry-dashboards'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.refresh-failure-not-rendered-as-zero',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dashboard refresh failures must not be converted into zero-valued metrics',
  'statement': 'When a query or telemetry refresh fails, the dashboard must preserve failure or unknown state rather '
               'than substituting zero, empty, or “all clear” values that imply successful measurement.',
  'intent': 'Prevent transport or query failures from masquerading as healthy operational values.',
  'applies_when': ['A dashboard refresh can fail independently of the underlying real-world metric and zero is a '
                   'legitimate measured value.'],
  'does_not_apply_when': [],
  'failure_modes': ['A network or query error causes the metric to display zero or an empty chart indistinguishable '
                    'from a valid zero-result measurement.'],
  'user_impacts': ['Operators can interpret missing evidence as absence of incidents, traffic, errors, cost, or '
                   'demand and make unsafe decisions.'],
  'observables': ['Return an explicit refresh error for a metric that previously had nonzero data and inspect '
                  'rendered value, state, and accessibility output.'],
  'falsifiers': ['The failure remains distinct from a measured zero and any cached value is clearly identified as '
                 'retained historical data.'],
  'repairs': ['Represent query failure, no-data, zero, and stale-value states separately in the metric state model '
              'and rendering logic.'],
  'exceptions': [],
  'verification': ['Exercise successful zero, no-result, timeout, permission error, and server failure responses and '
                   'confirm users can distinguish every state.'],
  'owner_hints': ['designing-instrument-telemetry-dashboards'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.permission-redaction-distinct-from-no-data',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Permission-redacted dashboard values must be distinct from genuine no-data states',
  'statement': 'When access policy hides a metric, dimension, or record set, the dashboard must not represent that '
               'redaction as zero, empty, or unavailable data from the source itself.',
  'intent': 'Prevent authorization boundaries from corrupting the user’s interpretation of operational or analytical '
            'completeness.',
  'applies_when': ['A dashboard aggregates or displays data that can be selectively hidden by role, row policy, '
                   'field policy, tenant boundary, or privacy rule.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user without permission sees an empty chart or zero count that is visually identical to a '
                    'legitimately empty dataset.'],
  'user_impacts': ['Users can make false conclusions about business state or system health because hidden '
                   'information appears not to exist.'],
  'observables': ['Compare the same dashboard under full and restricted permissions while the underlying dataset '
                  'remains non-empty.'],
  'falsifiers': ['The restricted view communicates that data is hidden or unavailable by policy without revealing '
                 'the protected values themselves.'],
  'repairs': ['Carry redaction metadata from authorization through aggregation and render a permission-specific '
              'state distinct from no-data semantics.'],
  'exceptions': [],
  'verification': ['Test field, row, tenant, and feature-level restrictions and confirm restricted users never '
                   'receive a misleading zero or empty-state interpretation.'],
  'owner_hints': ['designing-dashboard-permission-boundaries'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dashboard.live-pause-state-visible',
  'domain': 'dashboard',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Paused monitoring must remain visibly different from a live updating dashboard',
  'statement': 'If users can pause, scrub, inspect history, freeze auto-refresh, or otherwise stop live updates, the '
               'interface must keep that paused state visible until real-time updating resumes.',
  'intent': 'Prevent operators from mistaking a frozen analytical view for current telemetry during investigation or '
            'handoff.',
  'applies_when': ['A dashboard supports live updates plus a user-controlled or system-controlled paused, '
                   'historical, or frozen inspection mode.'],
  'does_not_apply_when': [],
  'failure_modes': ['After pausing updates, the dashboard looks identical to live mode and the user can no longer '
                    'tell that new telemetry is not being incorporated.'],
  'user_impacts': ['Users can continue monitoring under the false belief that the screen reflects current events '
                   'while it is actually frozen in the past.'],
  'observables': ['Pause or enter historical inspection, let new telemetry arrive, and compare live-state '
                  'indicators, timestamps, and update behavior.'],
  'falsifiers': ['Paused state is persistently visible and resuming live mode clearly reconciles the view to current '
                 'data.'],
  'repairs': ['Model live versus paused as explicit application state and expose the mode in the monitoring chrome '
              'rather than only in transient controls.'],
  'exceptions': [],
  'verification': ['Pause, navigate within the dashboard, drill down, return, and resume while confirming the mode '
                   'indicator and data freshness remain truthful.'],
  'owner_hints': ['designing-live-signal-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-dashboard-monitoring-owners-v13'],
  'status': 'active'}]

__all__ = ["DASHBOARD_MONITORING_RULES_V13"]
