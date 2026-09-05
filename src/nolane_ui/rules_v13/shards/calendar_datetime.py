"""V13 seventh-wave independently authored rules for calendar datetime."""
from __future__ import annotations

from ._capabilities import interaction_caps


CALENDAR_DATETIME_RULES_V13 = [{'rule_id': 'ui.calendar.all-day-distinct-from-timed-event',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Calendar interfaces must preserve the distinction between all-day and timed events',
  'statement': 'An all-day event must not be silently converted into a midnight timed event, and a timed '
               'event must not become all-day merely because its local rendering spans a date boundary.',
  'intent': 'Preserve calendar intent across display, editing, and time-zone changes.',
  'applies_when': ['The calendar supports both date-only events and events with specific start or end '
                   'times.'],
  'does_not_apply_when': [],
  'failure_modes': ['An all-day item is stored or rendered as 00:00–24:00 and shifts dates when the viewer '
                    'changes time zone.'],
  'user_impacts': ['Users can see birthdays, leave, deadlines, or timed meetings on the wrong date or with '
                   'false clock precision.'],
  'observables': ['Create all-day and midnight timed events, change viewer zones, edit each, and inspect '
                  'interchange or stored semantics.'],
  'falsifiers': ['Date-only and timed event types remain distinct through display and editing, and their '
                 'zone behavior matches the declared event model.'],
  'repairs': ['Preserve event value type in state and serialization rather than inferring all-day from clock '
              'values.'],
  'exceptions': [],
  'verification': ['Test all-day, midnight, multi-day, and zone changes, confirming event type and intended '
                   'calendar dates remain stable.'],
  'owner_hints': ['designing-calendar-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.calendar-system-visible-when-non-gregorian',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Non-Gregorian calendar use must expose the active calendar system and preserve date identity',
  'statement': 'When a product supports alternate calendar systems, date pickers and displayed dates must '
               'make the active system clear enough to prevent Gregorian interpretation of the same '
               'numerals.',
  'intent': 'Avoid ambiguous dates when year, month, and era semantics differ across calendar systems.',
  'applies_when': ['Users can choose or inherit a non-Gregorian calendar for display or date entry.'],
  'does_not_apply_when': [],
  'failure_modes': ['The picker shows month and day numbers without naming the active calendar, while '
                    'downstream text silently converts to Gregorian or vice versa.'],
  'user_impacts': ['Users can schedule, submit, or interpret the wrong civil date despite entering '
                   'apparently valid values.'],
  'observables': ['Switch calendar systems and locales while entering the same numeric date, then inspect '
                  'stored date identity and downstream summaries.'],
  'falsifiers': ['The active calendar system is identifiable and conversions preserve the intended date '
                 'without changing the underlying semantic type silently.'],
  'repairs': ['Carry calendar-system metadata through parsing, formatting, and controls, and label it where '
              'numeric ambiguity is material.'],
  'exceptions': [],
  'verification': ['Exercise at least two supported calendar systems across edit, review, and export, '
                   'verifying round trips preserve date meaning.'],
  'owner_hints': ['designing-non-gregorian-calendar-support'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.disabled-date-reason-available',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Disabled dates must expose why they cannot be selected when the reason affects user recovery',
  'statement': 'A date picker should make policy-driven unavailability understandable rather than rendering '
               'disabled dates with no explanation when users can take another action or choose another '
               'context.',
  'intent': 'Turn a blocked date into actionable scheduling information instead of an unexplained visual '
            'state.',
  'applies_when': ['Dates may be unavailable because of lead time, capacity, eligibility, blackout rules, '
                   'permissions, or dependent field state.'],
  'does_not_apply_when': [],
  'failure_modes': ['A date is disabled but the user cannot determine whether it is past, fully booked, '
                    'outside policy, or blocked until another field changes.'],
  'user_impacts': ['Users repeatedly try alternatives or abandon the workflow because they cannot infer the '
                   'selection constraint.'],
  'observables': ['Create dates disabled for different causes and inspect pointer, keyboard, screen-reader, '
                  'and helper-text access to the explanation.'],
  'falsifiers': ['The relevant constraint is available without requiring activation of an impossible control '
                 'and does not reveal protected internal information.'],
  'repairs': ['Associate disabled-date state with a user-facing reason or surrounding rule explanation and '
              'update it when dependencies change.'],
  'exceptions': [],
  'verification': ['Test dynamic availability and keyboard navigation, verifying every policy-driven '
                   'disabled state has a discoverable recovery-relevant explanation.'],
  'owner_hints': ['designing-date-time-pickers'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.range-end-inclusion-semantics-visible',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Date-range controls must make inclusive and exclusive end semantics unambiguous',
  'statement': 'A selected date range must communicate whether the final date is included, especially for '
               'bookings, reports, leave, and query intervals whose APIs may use exclusive end boundaries.',
  'intent': 'Prevent one-day discrepancies between what users see and what backend intervals include.',
  'applies_when': ['A date range controls a time interval and the product or API distinguishes inclusive '
                   'versus exclusive endpoints.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI displays Jan 1–Jan 3 while the query or reservation actually covers through the '
                    'start of Jan 3 and excludes that date.'],
  'user_impacts': ['Users can underbook, overreport, or omit data from the final day without realizing the '
                   'boundary mismatch.'],
  'observables': ['Select single-day and multi-day ranges and compare visible summary, stored endpoints, and '
                  'records or nights included.'],
  'falsifiers': ['The human-facing range language matches the effective inclusion model, with API-exclusive '
                 'boundaries translated appropriately.'],
  'repairs': ['Normalize backend interval semantics into a user-facing range contract rather than exposing '
              'raw exclusive endpoints as if inclusive.'],
  'exceptions': [],
  'verification': ['Test date-only and date-time ranges across export and review summaries, confirming '
                   'included periods exactly match the displayed range.'],
  'owner_hints': ['designing-date-time-pickers'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.recurring-instance-distinct-from-series-edit',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Editing one recurring occurrence must remain distinct from editing the recurrence series',
  'statement': 'Calendar edit flows must state whether a change applies to only this occurrence, this and '
               'following occurrences, or the entire series before commit.',
  'intent': 'Protect users from changing many scheduled events when they intended to adjust one exception.',
  'applies_when': ['The product supports recurring events and modifications to individual occurrences or '
                   'recurrence rules.'],
  'does_not_apply_when': [],
  'failure_modes': ['Opening one occurrence and changing its time updates every event in the series because '
                    'scope was inferred rather than explicitly chosen.'],
  'user_impacts': ['Meetings, shifts, or reminders can be moved or cancelled at scale unintentionally.'],
  'observables': ['Edit one occurrence, a middle occurrence, and recurrence metadata while inspecting '
                  'confirmation scope and resulting instance identities.'],
  'falsifiers': ['The action scope is explicit and the committed changes match only the selected recurrence '
                 'boundary.'],
  'repairs': ['Model occurrence exceptions and series-rule edits separately and require a clear scope choice '
              'when more than one interpretation is possible.'],
  'exceptions': [],
  'verification': ['Test moved, deleted, and detached instances plus series changes, verifying history and '
                   'future instances reflect the declared edit scope.'],
  'owner_hints': ['designing-recurring-events'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.availability-slot-staleness-visible',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Availability slots must be revalidated before booking when capacity can change concurrently',
  'statement': 'A displayed open slot must not be treated as reserved merely because it was rendered '
               'earlier; the final booking step must reconcile current availability and explain stale '
               'selection failure.',
  'intent': 'Prevent oversubscription and false booking success in shared scheduling systems.',
  'applies_when': ['Slots can become unavailable after they are displayed because other users or systems '
                   'reserve capacity.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user selects an old slot, submits later, and the UI shows success optimistically even '
                    'though the authoritative booking failed or moved.'],
  'user_impacts': ['Users can believe an appointment exists and act on a reservation that was never '
                   'committed.'],
  'observables': ['Open the same slot in multiple sessions, reserve it from one, then submit from the stale '
                  'session.'],
  'falsifiers': ['The stale submission is revalidated, and conflict recovery preserves the user’s context '
                 'while offering current alternatives.'],
  'repairs': ['Bind final booking to current slot identity/version and treat rendered availability as '
              'provisional until commit.'],
  'exceptions': [],
  'verification': ['Race slot reservations and cancellations repeatedly, confirming only authoritative '
                   'bookings produce success and calendar insertion.'],
  'owner_hints': ['designing-time-slot-selection'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.week-start-and-week-number-follow-locale',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Calendar week layout and week-number semantics must follow the selected locale or explicit user '
           'preference',
  'statement': 'Week starts and numbered weeks should use locale-aware conventions or a visible explicit '
               'preference instead of assuming Sunday or Monday universally.',
  'intent': 'Prevent orientation and reporting errors for users whose regional week convention differs from '
            'the product default.',
  'applies_when': ['A calendar displays week grids, week numbers, or weekday-relative navigation across '
                   'multiple locales.'],
  'does_not_apply_when': [],
  'failure_modes': ['The locale changes names and dates but leaves a hardcoded week start or computes week '
                    'numbers under a different convention than the displayed grid.'],
  'user_impacts': ['Users can select the wrong week or reconcile reports against mismatched regional '
                   'calendars.'],
  'observables': ['Switch locales with different first-day and week-number rules and compare grid order, '
                  'week labels, and date-to-week mapping.'],
  'falsifiers': ['Calendar layout and numbering derive from one locale/preference model and remain '
                 'internally consistent.'],
  'repairs': ['Use locale calendar data for first-day and week-number conventions and expose overrides as '
              'explicit settings.'],
  'exceptions': [],
  'verification': ['Test year boundaries and locale switches, verifying week identity remains consistent '
                   'across picker, calendar, and exported labels.'],
  'owner_hints': ['designing-calendar-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.calendar.date-time-picker-preserves-entered-zone-context',
  'domain': 'calendar',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Date-time pickers must preserve whether the user entered local, floating, or zone-bound time',
  'statement': 'When a date-time value is tied to a named zone or intentionally floating local time, editing '
               'and review must not silently reinterpret it in the viewer’s current device zone.',
  'intent': 'Keep scheduled intent stable when users travel, collaborate across zones, or edit existing '
            'events.',
  'applies_when': ['The product accepts date-time values with more than one temporal interpretation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A meeting created for 09:00 Europe/Paris reopens as 03:00 local time and saving it '
                    'rewrites the event to the viewer zone without an explicit zone change.'],
  'user_impacts': ['Events shift for participants because merely editing a field changes its temporal '
                   'authority.'],
  'observables': ['Create zone-bound and floating events, change the device zone, reopen and resave without '
                  'edits, then compare stored temporal metadata.'],
  'falsifiers': ['A no-op edit preserves the original zone/floating semantics and any intentional conversion '
                 'is explicit before commit.'],
  'repairs': ['Keep temporal value type and zone metadata in form state rather than reconstructing from '
              'localized display strings.'],
  'exceptions': [],
  'verification': ['Round-trip values through picker, review, reload, and cross-zone clients, verifying '
                   'semantic identity is unchanged unless the user changes it.'],
  'owner_hints': ['designing-time-zone-selection'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-calendar-owners-v13'],
  'status': 'active'}]

__all__ = ["CALENDAR_DATETIME_RULES_V13"]
