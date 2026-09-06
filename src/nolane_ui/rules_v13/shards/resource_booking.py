"""V13 eighth-wave independently authored rules for resource booking."""
from __future__ import annotations

from ._capabilities import interaction_caps


BOOKING_RULES_V13 = [{'rule_id': 'ui.booking.timezone-basis-visible',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Booking times must expose the timezone used for availability and confirmation',
  'statement': 'Availability and confirmed times need an explicit zone basis so the same slot is '
               'not interpreted differently by organizer and attendee.',
  'intent': 'Keep resource reservations temporally unambiguous across locations and daylight '
            'changes.',
  'applies_when': ['A resource can be viewed or booked by users in different timezones.'],
  'does_not_apply_when': [],
  'failure_modes': ['A room shows 09:00 in search but the confirmation silently stores 09:00 in '
                    'another timezone.'],
  'user_impacts': ['Users can reserve the wrong real-world interval while every screen appears '
                   'internally plausible.'],
  'observables': ['Compare search, hold, confirmation, calendar export, and edit views from two '
                  'timezones.'],
  'falsifiers': ['Every displayed interval resolves to one disclosed zone or deliberately shows '
                 'both local and resource zones.'],
  'repairs': ['Persist the booking zone with the interval and render that zone wherever '
              'availability or commitment is shown.'],
  'exceptions': [],
  'verification': ['Book across a DST boundary from two zones and verify search, confirmation, '
                   'edit, and exported event resolve to the same instant.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.held-distinct-from-confirmed',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Temporary booking holds must remain distinct from confirmed reservations',
  'statement': 'A hold is provisional capacity, not a durable reservation, and its expiry and '
               'confirmation state must remain visible.',
  'intent': 'Prevent users from treating expiring inventory as a completed reservation.',
  'applies_when': ['The booking flow uses temporary holds while payment, approval, or user '
                   'confirmation is pending.'],
  'does_not_apply_when': [],
  'failure_modes': ['A slot marked “reserved” is only held for five minutes, but the UI omits the '
                    'provisional state and expiry.'],
  'user_impacts': ['Users may leave the flow believing a resource is theirs when the hold can '
                   'disappear.'],
  'observables': ['Create a hold, let it age and expire, then observe list, detail, notifications, '
                  'and competing availability.'],
  'falsifiers': ['Held, confirmed, expired, and released states remain distinguishable and expiry '
                 'is observable before commitment.'],
  'repairs': ['Represent holds as a first-class state with expiry metadata and transition them '
              'atomically to confirmed or released.'],
  'exceptions': [],
  'verification': ['Race hold expiry against confirmation and verify no surface reports '
                   'confirmation without the authoritative transition.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.capacity-checked-at-commit',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Capacity must be revalidated when a booking is committed',
  'statement': 'Displayed availability is advisory until the commit transaction verifies current '
               'capacity against competing reservations.',
  'intent': 'Prevent oversubscription caused by stale availability views.',
  'applies_when': ['Multiple actors can reserve the same finite-capacity resource concurrently.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two users see one remaining place and both confirmations succeed because '
                    'capacity was checked only when the page loaded.'],
  'user_impacts': ['The resource becomes overbooked and later users receive contradictory '
                   'reservation states.'],
  'observables': ['Open concurrent booking sessions at the final remaining capacity and submit '
                  'them nearly simultaneously.'],
  'falsifiers': ['At most the available capacity commits; losing attempts receive a conflict tied '
                 'to fresh availability.'],
  'repairs': ['Move capacity validation into the authoritative commit transaction and return a '
              'resolvable conflict when capacity changed.'],
  'exceptions': [],
  'verification': ['Submit concurrent commits under one remaining unit and verify committed count '
                   'never exceeds capacity.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.recurrence-exception-scope-visible',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Recurring booking edits must expose whether one occurrence or the series is affected',
  'statement': 'Editing a recurring reservation without visible exception scope can '
               'unintentionally rewrite past or future occurrences.',
  'intent': 'Keep recurrence mutations bounded to the user’s selected scope.',
  'applies_when': ['A booking belongs to a recurring series and supports edit, move, or cancel '
                   'actions.'],
  'does_not_apply_when': [],
  'failure_modes': ['Changing one Tuesday meeting silently moves every future occurrence because '
                    'the action scope is hidden.'],
  'user_impacts': ['Users can disrupt an entire recurring schedule while intending a single '
                   'exception.'],
  'observables': ['Edit one occurrence, this-and-future, and whole-series scopes and inspect '
                  'unchanged neighboring occurrences.'],
  'falsifiers': ['The selected recurrence scope is visible before commit and the resulting series '
                 'contains only the intended mutations.'],
  'repairs': ['Require an explicit recurrence scope and model single-instance exceptions '
              'separately from series definition changes.'],
  'exceptions': [],
  'verification': ['Apply each recurrence scope and verify generated occurrences and historical '
                   'instances match the chosen boundary.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.resource-dependencies-visible',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dependent resources must be visible in booking availability and confirmation',
  'statement': 'A reservation can be unusable when required rooms, equipment, staff, or linked '
               'resources are hidden from the availability decision.',
  'intent': 'Prevent apparently valid bookings whose required dependency cannot actually be '
            'supplied.',
  'applies_when': ['A bookable item requires one or more dependent resources or constraints.'],
  'does_not_apply_when': [],
  'failure_modes': ['A procedure room is available but its required equipment is already reserved, '
                    'while the booking UI reports the room as fully available.'],
  'user_impacts': ['Users can commit reservations that cannot be fulfilled operationally.'],
  'observables': ['Create conflicts in dependent resources and inspect availability, hold, '
                  'confirmation, and later edits.'],
  'falsifiers': ['Availability and confirmation reflect the effective dependency set or clearly '
                 'disclose unresolved dependent requirements.'],
  'repairs': ['Evaluate dependency availability as part of the booking contract and display which '
              'dependency causes a conflict.'],
  'exceptions': [],
  'verification': ['Reserve a dependency elsewhere and verify the parent booking is blocked or '
                   'explicitly marked incomplete before confirmation.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.cancellation-effective-scope-visible',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Booking cancellation must show the effective resource, interval, and recurrence scope',
  'statement': 'Cancellation is destructive and must identify exactly which reservation capacity '
               'will be released.',
  'intent': 'Prevent accidental cancellation of the wrong occurrence, attendee scope, or linked '
            'resource.',
  'applies_when': ['A confirmed booking can be cancelled partially, by occurrence, or with related '
                   'resources.'],
  'does_not_apply_when': [],
  'failure_modes': ['A “Cancel booking” action releases the whole series when the user intended '
                    'only one occurrence.'],
  'user_impacts': ['Operational plans and other attendees can be disrupted by an overbroad '
                   'cancellation.'],
  'observables': ['Cancel single, future-series, and linked-resource combinations and inspect '
                  'resulting availability and notifications.'],
  'falsifiers': ['The confirmation identifies the exact cancellation scope and only that scope '
                 'becomes available afterward.'],
  'repairs': ['Bind cancellation to an immutable reservation/occurrence identity and require '
              'explicit scope for broader release.'],
  'exceptions': [],
  'verification': ['Execute each supported cancellation scope and verify released capacity and '
                   'surviving reservations reconcile exactly.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.waitlist-promotion-state-visible',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Waitlist promotion must expose offer, expiry, and confirmed status separately',
  'statement': 'A promoted waitlist entry is an offer until accepted; presenting it as confirmed '
               'can misstate capacity and user commitment.',
  'intent': 'Make waitlist transitions understandable and prevent silent loss of promoted slots.',
  'applies_when': ['A booking system promotes users from a waitlist when capacity becomes '
                   'available.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user receives a promoted slot that expires after an hour, but the UI '
                    'immediately labels the booking confirmed.'],
  'user_impacts': ['Users may miss an acceptance deadline or assume capacity is secured when it is '
                   'still provisional.'],
  'observables': ['Trigger a cancellation, promote the next waitlisted user, then let the offer be '
                  'accepted and separately expire.'],
  'falsifiers': ['Waitlisted, offered, offer-expired, and confirmed states are distinct with an '
                 'observable acceptance deadline.'],
  'repairs': ['Model promotion as a time-bounded offer and transition to confirmed only after '
              'authoritative acceptance.'],
  'exceptions': [],
  'verification': ['Exercise accept, decline, and expiry paths and verify capacity and queue '
                   'position remain consistent in every state.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.booking.stale-availability-conflict-reconciled',
  'domain': 'booking',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Stale availability conflicts must reconcile before a reservation is presented as '
           'successful',
  'statement': 'When availability changes between selection and commit, the UI must replace the '
               'stale assumption with the authoritative conflict outcome.',
  'intent': 'Prevent stale optimistic success from surviving after the booking service rejects the '
            'slot.',
  'applies_when': ['Availability can change while the user is completing a booking flow.'],
  'does_not_apply_when': [],
  'failure_modes': ['The confirmation screen briefly says success even though the server rejects '
                    'the slot because another reservation committed first.'],
  'user_impacts': ['Users can act on a reservation that never existed and duplicate downstream '
                   'work.'],
  'observables': ['Change capacity after selection but before commit and observe optimistic UI, '
                  'retry options, and selected alternatives.'],
  'falsifiers': ['A rejected stale selection never remains as confirmed; the UI surfaces fresh '
                 'availability and preserves enough context to recover.'],
  'repairs': ['Treat commit conflict as authoritative, roll back provisional success, and rebase '
              'the user on current availability without silently changing the chosen slot.'],
  'exceptions': [],
  'verification': ['Race competing commits and verify the losing client converges to '
                   'conflict/reselection with no phantom reservation.'],
  'owner_hints': ['designing-resource-booking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-booking-owners-v13'],
  'status': 'active'}]

__all__ = ["BOOKING_RULES_V13"]
