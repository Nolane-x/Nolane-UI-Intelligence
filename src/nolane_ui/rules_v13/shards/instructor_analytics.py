"""V13 eighth-wave independently authored rules for instructor."""
from __future__ import annotations

from ._capabilities import interaction_caps


INSTRUCTOR_ANALYTICS_RULES_V13 = [{'rule_id': 'ui.instructor.cohort-scope-visible',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor analytics must keep the evaluated cohort scope visible with every summary',
  'statement': 'Metrics should identify which course section, enrollment state, group, date range, or '
               'filter population they summarize so numbers are not detached from their denominator '
               'context.',
  'intent': 'Prevent instructors from comparing or exporting metrics whose learner population changed '
            'invisibly.',
  'applies_when': ['Instructor dashboards support filtering by section, cohort, enrollment status, '
                   'assignment, or learner group.'],
  'does_not_apply_when': [],
  'failure_modes': ['A retention metric remains on screen while the instructor switches from all '
                    'students to one section, but the label does not update to show the narrower '
                    'cohort.'],
  'user_impacts': ['Instructors can make intervention decisions from a metric whose population they '
                   'misunderstand.'],
  'observables': ['Change cohort and enrollment filters while inspecting metric cards, drilldowns, '
                  'charts, and exported files.'],
  'falsifiers': ['Every aggregate remains associated with the effective cohort definition and all '
                 'linked drilldowns use the same population unless clearly stated otherwise.'],
  'repairs': ['Carry cohort filter identity into every analytics query and render the effective scope '
              'beside summaries and exports.'],
  'exceptions': [],
  'verification': ['Switch among overlapping cohorts and verify counts, denominators, and exported '
                   'learner sets reconcile to the displayed scope.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.denominator-and-missing-learners-visible',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor rates must expose their denominator and distinguish excluded or missing learners',
  'statement': 'Percentages such as completion, pass rate, response rate, and mastery are ambiguous '
               'without the eligible population and treatment of learners with no data.',
  'intent': 'Keep analytics from hiding missingness behind a clean percentage.',
  'applies_when': ['Instructor dashboards calculate rates over enrolled, active, submitted, or '
                   'otherwise eligible learner populations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A dashboard says 90% passed using only the ten learners who submitted, while '
                    'twenty enrolled learners with no attempt are omitted and invisible.'],
  'user_impacts': ['Instructors can overestimate cohort performance because nonparticipants disappear '
                   'from the denominator.'],
  'observables': ['Construct cohorts with submitted, missing, withdrawn, and exempt learners and '
                  'inspect numerator, denominator, drilldown, and export.'],
  'falsifiers': ['The metric states or exposes its denominator basis and missing or excluded '
                 'populations can be inspected separately.'],
  'repairs': ['Define denominator policy explicitly in the analytics model and preserve counts for '
              'excluded, missing, and eligible populations.'],
  'exceptions': [],
  'verification': ['Test rates under changing enrollment and submission states, verifying displayed '
                   'percentages and drilldowns reconcile exactly.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.time-window-basis-visible',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor analytics must disclose the event-time window and timezone used for temporal '
           'metrics',
  'statement': 'Daily activity, lateness, engagement, and trend metrics can change meaning across '
               'timezone or event-time versus processing-time boundaries, so the evaluated window must '
               'be inspectable.',
  'intent': 'Prevent date-based analytics from implying a temporal scope different from the underlying '
            'events.',
  'applies_when': ['Analytics group learner events into days, weeks, terms, deadlines, or rolling '
                   'windows.'],
  'does_not_apply_when': [],
  'failure_modes': ['An instructor views “this week” near midnight and the graph groups events by '
                    'server UTC while the course operates in a local timezone.'],
  'user_impacts': ['Learner activity and late-work conclusions can shift across dates without an '
                   'obvious reason.'],
  'observables': ['Generate events around timezone and daylight-offset boundaries and compare chart '
                  'bins, filters, deadlines, and export timestamps.'],
  'falsifiers': ['The analytics surface exposes the effective timezone and resolved window and '
                 'consistently uses the intended event-time basis.'],
  'repairs': ['Persist temporal query boundaries with analytics snapshots and use course or explicitly '
              'selected timezone semantics for grouping.'],
  'exceptions': [],
  'verification': ['Test relative and fixed date ranges around boundary times, verifying every temporal '
                   'metric and export uses the disclosed basis.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.privacy-aggregation-state-visible',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Privacy aggregation or suppression must be visible when instructor analytics intentionally '
           'hide small populations',
  'statement': 'When metrics are bucketed, rounded, delayed, or suppressed to protect learner privacy, '
               'the interface should disclose that transformation instead of presenting the result as '
               'exact raw data.',
  'intent': 'Keep instructors from over-interpreting privacy-protected analytics as precise '
            'measurements.',
  'applies_when': ['Analytics products apply privacy thresholds, cohort minimums, rounding, or delayed '
                   'aggregation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A metric displays “0 learners” for a small protected cohort when the real meaning '
                    'is suppressed, making privacy masking look like absence.'],
  'user_impacts': ['Instructors can infer incorrect learner behavior or attempt to reverse-engineer '
                   'protected data from ambiguous outputs.'],
  'observables': ['Create cohorts below and above privacy thresholds and inspect metric labels, '
                  'drilldowns, exports, and filter behavior.'],
  'falsifiers': ['Suppressed, rounded, delayed, and exact metrics remain semantically distinct and the '
                 'UI does not expose protected raw values indirectly.'],
  'repairs': ['Model privacy transformations as explicit result states and propagate them to every '
              'derivative visualization and export.'],
  'exceptions': [],
  'verification': ['Test threshold crossings and filter combinations, verifying privacy state remains '
                   'visible and no surface contradicts the protected aggregate.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.late-submission-inclusion-visible',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor analytics must state whether late, excused, and resubmitted work is included in '
           'reported metrics',
  'statement': 'Submission timing categories can materially change completion and performance '
               'statistics, so inclusion policy should be visible rather than inferred from a total.',
  'intent': 'Prevent cohort comparisons from silently using different submission populations.',
  'applies_when': ['Courses allow late submissions, extensions, exemptions, retries, or resubmissions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A chart shows average score but excludes all late submissions while the gradebook '
                    'includes them, with no indication that the populations differ.'],
  'user_impacts': ['Instructors can compare metrics that look equivalent but summarize different '
                   'learner work.'],
  'observables': ['Create on-time, late, excused, and resubmitted records and compare dashboard '
                  'metrics, drilldowns, gradebook, and export.'],
  'falsifiers': ['Each metric exposes or inherits a clear inclusion policy and its underlying learner '
                 'rows reconcile to that policy.'],
  'repairs': ['Centralize submission inclusion rules in the analytics query definition and surface the '
              'effective policy in filters or metric details.'],
  'exceptions': [],
  'verification': ['Toggle inclusion policies and verify counts, averages, and exported populations '
                   'change consistently across analytics surfaces.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.gradebook-freshness-visible',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor analytics must disclose when gradebook data are not yet incorporated into '
           'summaries',
  'statement': 'Manual grading, external tools, rescoring, and synchronization can lag behind '
               'analytics, so performance dashboards need a freshness state rather than silently '
               'displaying outdated scores.',
  'intent': 'Prevent instructors from intervening on learners using metrics that omit recently '
            'completed grading.',
  'applies_when': ['Analytics consume gradebook data that can update asynchronously or through external '
                   'systems.'],
  'does_not_apply_when': [],
  'failure_modes': ['An instructor finishes grading essays but the dashboard remains based on earlier '
                    'provisional scores with no stale indicator.'],
  'user_impacts': ['Learners can be incorrectly identified as at risk because recent grades are absent '
                   'from the aggregate.'],
  'observables': ['Delay gradebook ingestion and compare updated grades with analytics timestamps, '
                  'pending counts, and recalculation behavior.'],
  'falsifiers': ['The analytics surface reveals its gradebook watermark or stale state and converges '
                 'when new scores are processed.'],
  'repairs': ['Carry grade source freshness into analytics snapshots and distinguish current, pending, '
              'and partially updated rollups.'],
  'exceptions': [],
  'verification': ['Publish batches of grades and rescoring events, verifying summaries never imply '
                   'freshness beyond the incorporated gradebook version.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.drilldown-population-consistent',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor analytics drilldowns must resolve to the same learner population represented by '
           'the aggregate',
  'statement': 'Clicking a metric or chart segment should show the records counted by that exact '
               'aggregate definition, not a newly evaluated or differently filtered population.',
  'intent': 'Keep summary-to-detail investigation trustworthy for instructional decisions.',
  'applies_when': ['Dashboards allow instructors to click aggregate metrics into learner-level lists or '
                   'assignment details.'],
  'does_not_apply_when': [],
  'failure_modes': ['A bar says twelve learners are below mastery, but clicking it opens fifteen '
                    'because the drilldown uses current filters while the chart reflects an older '
                    'snapshot.'],
  'user_impacts': ['Instructors cannot determine which learners actually produced the metric or may '
                   'contact the wrong students.'],
  'observables': ['Change filters and source data between aggregate load and drilldown, then compare '
                  'metric membership with learner identities shown.'],
  'falsifiers': ['Drilldown either uses the same snapshot and definition as the aggregate or clearly '
                 'announces that it has refreshed to a new population.'],
  'repairs': ['Carry aggregate query or snapshot identity into drilldown navigation and validate '
              'learner membership against that same evaluation.'],
  'exceptions': [],
  'verification': ['Race source updates and filter changes, verifying summary counts always reconcile '
                   'to their drilldown population or disclose a refresh boundary.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.instructor.export-preserves-analytics-filters',
  'domain': 'instructor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Instructor analytics exports must preserve the exact filters and cohort scope shown at '
           'export time',
  'statement': 'An exported table should correspond to the instructor’s evaluated dashboard selection '
               'and include enough metadata to reconstruct the applied cohort, date, and metric '
               'filters.',
  'intent': 'Prevent offline analysis from silently reverting to a broader or default learner '
            'population.',
  'applies_when': ['Instructor dashboards support exporting filtered charts, learner lists, or '
                   'performance tables.'],
  'does_not_apply_when': [],
  'failure_modes': ['An instructor filters to one section and exports, but the file contains every '
                    'course learner because the export endpoint ignores the dashboard filter state.'],
  'user_impacts': ['Sensitive or irrelevant learner data can be disclosed and downstream analysis can '
                   'contradict the UI.'],
  'observables': ['Apply combinations of cohort, time, status, and assignment filters and compare '
                  'visible rows with exported identities and metadata.'],
  'falsifiers': ['Exported membership and calculations match the effective analytics query and the file '
                 'records the material filter context.'],
  'repairs': ['Generate export jobs from a serialized evaluated query or snapshot rather than '
              'rebuilding selection from default parameters.'],
  'exceptions': [],
  'verification': ['Export multiple filtered views and verify row membership, metric values, and '
                   'documented filter scope exactly match the dashboard state.'],
  'owner_hints': ['designing-instructor-cohort-analytics'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-instructor-analytics-owners-v13'],
  'status': 'active'}]


__all__ = ["INSTRUCTOR_ANALYTICS_RULES_V13"]
