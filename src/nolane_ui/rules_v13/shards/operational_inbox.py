"""V13 seventh-wave independently authored rules for operational inbox."""
from __future__ import annotations

from ._capabilities import interaction_caps


OPERATIONAL_INBOX_RULES_V13 = [{'rule_id': 'ui.inbox.unread-state-authority-consistent',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Operational inbox unread state must converge across sessions and devices',
  'statement': 'Read and unread markers in an operational inbox must resolve from a durable state model or '
               'an explicitly local model, not oscillate unpredictably as users open the same item from '
               'multiple clients.',
  'intent': 'Keep attention management trustworthy when inboxes drive incident, support, moderation, or '
            'administrative work.',
  'applies_when': ['The same operational queue can be opened from multiple tabs or devices and uses unread '
                   'state to prioritize work.'],
  'does_not_apply_when': [],
  'failure_modes': ['Opening an item on one client marks it read locally while other clients continue '
                    'presenting it as new indefinitely or later overwrite the read state.'],
  'user_impacts': ['Operators can duplicate work or miss genuinely new items because unread badges no longer '
                   'represent a coherent attention model.'],
  'observables': ['Open and read the same item from multiple sessions under delayed sync, then refresh and '
                  'observe list counts and detail state.'],
  'falsifiers': ['All clients converge according to the declared shared or local unread model, and '
                 'transitions cannot be reversed by stale state writes.'],
  'repairs': ['Store read state with a monotonic or versioned authority model and make intentionally local '
              'unread behavior explicit.'],
  'exceptions': [],
  'verification': ['Race reads and marks-unread across devices, verifying counts, badges, and filters '
                   'converge consistently after synchronization.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.assignment-owner-visible',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Assigned inbox work must expose the current accountable owner wherever the item is actionable',
  'statement': 'An inbox item that can be assigned must show who currently owns follow-up in both list and '
               'detail contexts and reconcile ownership changes before further assignment-sensitive actions.',
  'intent': 'Reduce duplicate handling and ambiguous responsibility in shared operational queues.',
  'applies_when': ['Multiple operators can claim, assign, transfer, or unassign items in a shared inbox.'],
  'does_not_apply_when': [],
  'failure_modes': ['The list appears unassigned while the detail was claimed elsewhere, or two operators '
                    'both see themselves as the current owner after a race.'],
  'user_impacts': ['Teams can perform conflicting work or leave an item unattended because accountability is '
                   'not trustworthy.'],
  'observables': ['Open one item in multiple clients, claim and transfer it concurrently, then inspect list, '
                  'detail, filters, and action permissions.'],
  'falsifiers': ['Every surface converges on the same authoritative owner or explicitly indicates unassigned '
                 'state, and stale claims cannot overwrite newer assignments silently.'],
  'repairs': ['Version assignment mutations and broadcast or refresh owner state wherever the item can be '
              'acted upon.'],
  'exceptions': [],
  'verification': ['Race claim, unassign, and transfer operations, confirming one authoritative owner '
                   'history and consistent UI across queue views.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.snooze-wake-time-visible',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Snoozed inbox items must show when and under which clock basis they will reappear',
  'statement': 'A snooze action must expose the effective wake time and make custom time-zone or calendar '
               'interpretation clear enough that users can predict when the item returns.',
  'intent': 'Prevent operational tasks from disappearing longer or shorter than intended because a relative '
            'label hides the enforced wake instant.',
  'applies_when': ['Inbox items can be snoozed until a relative duration, local date-time, business hour, or '
                   'custom schedule.'],
  'does_not_apply_when': [],
  'failure_modes': ['The item says “snoozed until tomorrow” without showing whose time zone or how '
                    'daylight-saving and business-hour rules are interpreted.'],
  'user_impacts': ['Operators can miss service deadlines or receive items during the wrong shift.'],
  'observables': ['Snooze items across time zones and DST boundaries, then inspect hidden-item metadata and '
                  'wake behavior after relaunch.'],
  'falsifiers': ['The effective wake instant or scheduling rule is visible and the item re-enters the '
                 'correct queue according to that same authority.'],
  'repairs': ['Store snooze state in a canonical time representation and render localized context without '
              'discarding the underlying zone or schedule semantics.'],
  'exceptions': [],
  'verification': ['Test relative, absolute, and business-time snoozes from multiple user zones, verifying '
                   'display and actual reappearance remain aligned.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.filter-count-consistent-with-items',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inbox filter counts must be derived from the same effective query as the visible items',
  'statement': 'Counts on inbox tabs, queues, or facets must reflect the canonical filter and permission '
               'scope that produces the corresponding item list, or identify that a count is approximate or '
               'delayed.',
  'intent': 'Keep workload estimates and navigation choices grounded in the actual queue population users '
            'can access.',
  'applies_when': ['Operational inboxes show counts for statuses, assignees, priorities, teams, or saved '
                   'filters.'],
  'does_not_apply_when': [],
  'failure_modes': ['A badge says 12 while opening the filter shows 7 because the count ignores current '
                    'permissions, stale filters, or a different time window without disclosure.'],
  'user_impacts': ['Operators may assume work is missing, misjudge queue health, or repeatedly search for '
                   'items they cannot access.'],
  'observables': ['Compare counts and item identities across filters, permission changes, and refresh timing '
                  'while the queue mutates.'],
  'falsifiers': ['Counts and lists share the same effective query boundary or any approximation and refresh '
                 'lag are explicitly communicated.'],
  'repairs': ['Centralize filter and permission semantics for count and item queries, with a declared '
              'freshness policy for cached aggregates.'],
  'exceptions': [],
  'verification': ['Exercise live inserts, permission changes, and saved filters, verifying count drift '
                   'stays within the declared approximation contract.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.bulk-action-partial-result-maps-items',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bulk inbox actions must map partial failures back to the affected items',
  'statement': 'When a bulk resolve, assign, label, archive, or escalate action has mixed outcomes, the '
               'result must identify which stable item IDs succeeded and which need further action.',
  'intent': 'Prevent a shared queue from looking clean when only part of a selected batch actually '
            'transitioned.',
  'applies_when': ['Users can apply one operational action to multiple selected inbox items.'],
  'does_not_apply_when': [],
  'failure_modes': ['The batch returns a generic success or failure while some items were stale, '
                    'unauthorized, or invalid for the requested transition.'],
  'user_impacts': ['Operators may skip unresolved items or replay actions on items that already succeeded.'],
  'observables': ['Select items with mixed eligibility and force one stale or unauthorized target, then '
                  'submit a bulk action and refresh.'],
  'falsifiers': ['Every selected item has a reconciled outcome, failed items remain discoverable, and retry '
                 'can target only the failed subset.'],
  'repairs': ['Execute and record per-item transitions under one batch identity rather than collapsing the '
              'operation into one boolean result.'],
  'exceptions': [],
  'verification': ['Test mixed status, permissions, and concurrency failures, confirming list state and '
                   'action summaries map outcomes to the same stable IDs.'],
  'owner_hints': ['designing-bulk-action-toolbars'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.duplicate-items-deduplicated-by-identity',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Operational inboxes must not create duplicate work cards for the same authoritative item '
           'identity',
  'statement': 'When the same underlying case or task arrives through retries, reconnect, pagination, or '
               'multiple feed sources, the inbox must preserve one logical item unless the product '
               'intentionally models distinct occurrences.',
  'intent': 'Avoid duplicate handling and contradictory status changes caused by transport-level '
            'duplication.',
  'applies_when': ['Inbox items can be delivered through real-time updates plus backfill, retries, or '
                   'paginated queries.'],
  'does_not_apply_when': [],
  'failure_modes': ['The same case ID appears twice with separate local selection or read state because the '
                    'client keys rows by arrival rather than authoritative identity.'],
  'user_impacts': ['Two operators may work the same case independently and status changes can appear to '
                   'affect only one duplicate representation.'],
  'observables': ['Deliver the same item through live and backfill paths and inspect row count, selection, '
                  'read state, and detail navigation.'],
  'falsifiers': ['One logical item exists per authoritative identity, or distinct occurrences have separate '
                 'explicit identifiers and semantics.'],
  'repairs': ['Deduplicate ingestion and rendering on stable item identity while merging newer state '
              'according to the queue’s version policy.'],
  'exceptions': [],
  'verification': ['Replay duplicate events before and after pagination boundaries, verifying item count and '
                   'lifecycle state remain coherent.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.priority-sort-basis-visible',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Priority ordering in an operational inbox must expose the effective ranking basis',
  'statement': 'If work is ordered by severity, SLA risk, manual priority, model score, age, or a composite, '
               'users need enough explanation to understand why an item appears ahead of another.',
  'intent': 'Prevent hidden ranking logic from masquerading as neutral chronology in high-attention queues.',
  'applies_when': ['The inbox order is not simply a transparent immutable timestamp sort.'],
  'does_not_apply_when': [],
  'failure_modes': ['Items move in the queue because a hidden score or manual override changed, but the UI '
                    'still looks like a standard chronological list.'],
  'user_impacts': ['Operators can miss urgent work or distrust the queue because apparent ordering has no '
                   'interpretable basis.'],
  'observables': ['Create items with conflicting age, severity, manual priority, and SLA state and inspect '
                  'ordering plus sort controls or explanations.'],
  'falsifiers': ['The active ranking basis is visible and material manual or policy overrides are '
                 'represented without requiring disclosure of protected model internals.'],
  'repairs': ['Expose the effective sort or ranking mode and relevant item-level priority indicators, with '
              'an explicit fallback for unknown scoring factors.'],
  'exceptions': [],
  'verification': ['Vary each priority input independently and verify resulting movement can be explained by '
                   'the displayed ranking contract.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inbox.resolution-retention-policy-visible',
  'domain': 'inbox',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resolved inbox items must make their post-resolution retention and visibility policy clear',
  'statement': 'After resolving or closing operational work, the product must communicate whether the item '
               'disappears, remains searchable, moves to history, or is retained under a policy boundary.',
  'intent': 'Prevent users from interpreting disappearance as deletion or persistent history as unresolved '
            'work.',
  'applies_when': ['Inbox items can transition to a resolved state and the product retains or hides them '
                   'according to queue policy.'],
  'does_not_apply_when': [],
  'failure_modes': ['Resolving an item removes it from the active list with no route to history, or a '
                    'retained resolved item looks indistinguishable from active work.'],
  'user_impacts': ['Operators can believe records were lost, redo completed work, or fail to locate evidence '
                   'for later review.'],
  'observables': ['Resolve items under different filters and retention conditions, then navigate active '
                  'queue, search, history, and deep links.'],
  'falsifiers': ['The UI distinguishes active from retained resolved state and provides the '
                 'policy-consistent route to historical records where the user has access.'],
  'repairs': ['Model resolution separately from deletion and expose the destination or retention outcome as '
              'part of the resolving action.'],
  'exceptions': [],
  'verification': ['Resolve, reopen, archive, and search items across retention windows, confirming state '
                   'and discoverability match the declared policy.'],
  'owner_hints': ['designing-operational-inboxes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-operational-inbox-owners-v13'],
  'status': 'active'}]

__all__ = ["OPERATIONAL_INBOX_RULES_V13"]
