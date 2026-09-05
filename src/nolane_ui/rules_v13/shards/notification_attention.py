"""V13 notification rules for event identity, badges, suppression, actions, chronology, and grouping."""
from __future__ import annotations

from ._capabilities import interaction_caps


NOTIFICATION_ATTENTION_RULES_V13 = [
    {'rule_id': 'ui.notifications.cross-channel-duplicates-collapse-by-event',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'The same notification event delivered through multiple channels should not appear as unrelated duplicates',
     'statement': 'When one authoritative event is delivered by push, email, in-app, desktop, or another channel and all '
                  'copies enter the same notification center, the product should reconcile them by event identity rather '
                  'than multiplying unread items.',
     'intent': 'Keep delivery-channel multiplicity separate from event multiplicity so attention state reflects what '
               'happened, not how many transports carried it.',
     'applies_when': ['The same product event can be delivered through multiple channels and later represented together '
                      'in one notification or activity surface.'],
     'does_not_apply_when': [],
     'failure_modes': ['Each transport creates an independent unread notification with no shared event identity, causing '
                       'one event to appear several times.'],
     'user_impacts': ['Users can overestimate activity, clear the same event repeatedly, or lose trust in unread counts '
                      'and notification grouping.'],
     'observables': ['Deliver one event over several channels with different arrival orders and compare notification '
                     'IDs, event IDs, unread count, and action targets.'],
     'falsifiers': ['Channel deliveries reconcile into one logical event or an explicitly grouped representation while '
                    'transport metadata can remain available separately.'],
     'repairs': ['Propagate stable event identity through channel delivery and deduplicate notification-center ingestion '
                 'against that identity.'],
     'exceptions': [],
     'verification': ['Test out-of-order delivery, one channel failure, repeated push, email ingestion, and device sync '
                      'and verify one event does not inflate logical unread state.'],
     'owner_hints': ['designing-notification-centers'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.badge-count-scope-visible',
     'domain': 'notifications',
     'class': 'contextual',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Notification badge counts must have a stable and understandable counting scope',
     'statement': 'If a badge shows unread, unseen, actionable, or total notifications, its semantics must remain stable '
                  'across surfaces and should not silently switch between item count, grouped thread count, or event '
                  'count.',
     'intent': 'Keep compact attention indicators interpretable so users know what clearing or opening the badge is '
               'expected to change.',
     'applies_when': ['The product displays numeric badges on app icons, tabs, navigation items, notification centers, '
                      'or categories.'],
     'does_not_apply_when': [],
     'failure_modes': ['The same badge sometimes counts raw deliveries, sometimes grouped conversations, and sometimes '
                       'only actionable items without exposing the change.'],
     'user_impacts': ['Users cannot reconcile the badge with the notification center and may repeatedly search for '
                      'supposedly missing unread items.'],
     'observables': ['Generate grouped, duplicated, read, dismissed, and actionable notifications and compare badge '
                     "values with the product's declared counting basis on every surface."],
     'falsifiers': ['Each badge uses a documented stable scope or clearly changes label/context when a different '
                    'counting metric is shown.'],
     'repairs': ['Define badge count from an explicit query over logical notification state and reuse that definition '
                 'across surfaces instead of recomputing ad hoc.'],
     'exceptions': [],
     'verification': ['Test grouping, read, archive, mute, cross-device sync, and duplicate delivery and verify badge '
                      'changes correspond to the same logical scope.'],
     'owner_hints': ['designing-notification-centers'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.snooze-mute-effective-state-visible',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Snooze and mute controls must expose their currently effective scope and duration',
     'statement': 'When users mute or snooze notifications, the UI must show what source or category is affected and '
                  'when the suppression ends if it is temporary, rather than leaving an ambiguous silent state.',
     'intent': 'Give users control over interruption policy without forcing them to remember hidden timers or whether '
               'they muted one thread versus an entire channel.',
     'applies_when': ['Notification settings support temporary snooze, thread mute, category mute, channel mute, or '
                      'other scoped suppression.'],
     'does_not_apply_when': [],
     'failure_modes': ['After applying suppression, the center shows only a generic muted icon and does not reveal which '
                       'scope is active or whether a temporary timer expired.'],
     'user_impacts': ['Users can miss important events longer than intended or repeatedly reconfigure notifications '
                      'because effective suppression state is unclear.'],
     'observables': ['Apply overlapping mute and snooze settings, inspect their scope and expiration, advance time, and '
                     'compare visible state with notification delivery decisions.'],
     'falsifiers': ['The effective suppression scope and temporary boundary remain inspectable and update when timers '
                    'expire or broader settings override narrower ones.'],
     'repairs': ['Model suppression as scoped policy records and render the effective result plus origin of the active '
                 'policy rather than a single boolean.'],
     'exceptions': [],
     'verification': ['Test thread, category, channel, device, temporary, and permanent suppression combinations and '
                      'verify visible state matches actual delivery behavior.'],
     'owner_hints': ['designing-notifications-and-interruptions'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.action-failure-remains-recoverable',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Failed notification actions must keep the originating event recoverable',
     'statement': 'If a user acts directly from a notification and the action fails, the notification must not disappear '
                  'as if the task completed unless another surface preserves a clear retry or recovery path tied to the '
                  'same event.',
     'intent': 'Keep dismissal and action success separate so quick actions cannot erase the only route back to '
               'unfinished work.',
     'applies_when': ['Notifications expose inline actions such as approve, reply, archive, retry, join, accept, or '
                      'dismiss that can fail independently of the notification itself.'],
     'does_not_apply_when': [],
     'failure_modes': ['Tapping an action removes or marks the notification complete optimistically and a later failure '
                       'leaves no visible way to retry or reopen the target.'],
     'user_impacts': ['Users can lose a time-sensitive task because an action failed after the attention item was '
                      'already cleared.'],
     'observables': ['Force each notification action to fail after optimistic UI and inspect notification state, retry '
                     'controls, target continuation, and cross-device synchronization.'],
     'falsifiers': ['Failure restores or retains a recoverable event state and never equates action attempt with '
                    'successful completion.'],
     'repairs': ['Treat action lifecycle as child state of the notification event and only apply completion or '
                 'auto-dismiss semantics after authoritative action success.'],
     'exceptions': [],
     'verification': ['Test network failure, authorization change, stale target, provider timeout, and duplicate action '
                      'and verify the original event remains recoverable.'],
     'owner_hints': ['designing-notification-to-app-continuation'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.timestamp-distinguishes-event-from-delivery',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Notification time should distinguish when the event happened from when it was delivered if delay matters',
     'statement': 'When delivery can be materially delayed, showing only the receive time as if it were event time can '
                  'mislead users; the product should preserve the event timestamp or otherwise communicate the delay '
                  'where chronology affects decisions.',
     'intent': 'Keep event chronology from being rewritten by offline delivery, push backlog, email ingestion, or device '
               'resume.',
     'applies_when': ['Notification transport may deliver events minutes or hours after the underlying event occurred '
                      'and users rely on chronology to prioritize or interpret them.'],
     'does_not_apply_when': [],
     'failure_modes': ['A delayed notification is stamped only with local arrival time and sorted as newly occurring '
                       'even though the event itself is old.'],
     'user_impacts': ['Users can react to stale alerts, misread the sequence of changes, or duplicate work that was '
                      'already resolved after the event occurred.'],
     'observables': ['Create events with known origin times and deliver them late or out of order, then inspect '
                     'displayed timestamps, sorting, and action availability.'],
     'falsifiers': ['The product retains event chronology and, where useful, separately exposes delivery delay rather '
                    'than substituting arrival time for event time.'],
     'repairs': ['Carry both event and delivery timestamps through notification transport and choose display and '
                 'ordering semantics explicitly per product domain.'],
     'exceptions': [],
     'verification': ['Test offline device resume, push backlog, email bridge, clock-zone change, and out-of-order '
                      'delivery and verify event order remains truthful.'],
     'owner_hints': ['designing-notification-centers'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.channel-disable-does-not-imply-event-deletion',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Disabling a delivery channel must not be represented as deleting the underlying notification events',
     'statement': 'Turning off push, email, SMS, or another delivery channel changes future transport policy and must '
                  'not silently clear historical in-app events or claim those events no longer exist unless deletion is '
                  'a separate explicit action.',
     'intent': 'Separate how users receive notifications from the lifecycle of the events those notifications represent.',
     'applies_when': ['The product has channel-level delivery settings and also maintains an in-app notification or '
                      'activity history.'],
     'does_not_apply_when': [],
     'failure_modes': ['Disabling a channel empties or hides historical events, or the settings UI implies old '
                       'notifications were deleted as a side effect of stopping future delivery.'],
     'user_impacts': ['Users can lose audit or task context and may confuse transport preference with record deletion.'],
     'observables': ['Populate notification history, disable each channel, and compare historical event records, future '
                     'delivery behavior, unread state, and retention policy.'],
     'falsifiers': ['Channel disable affects future transport only unless a distinct documented retention action is '
                    'invoked.'],
     'repairs': ['Model delivery preferences separately from event storage and notification-center state, and avoid '
                 'coupling channel toggles to history deletion.'],
     'exceptions': [],
     'verification': ['Test disable/re-enable, multi-channel combinations, account restore, and device sync and verify '
                      'history lifecycle remains independent of delivery policy.'],
     'owner_hints': ['designing-notifications-and-interruptions'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.archive-distinct-from-read',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Archiving a notification must remain distinct from marking it read',
     'statement': 'Removing a notification from the primary inbox and acknowledging that it has been seen are different '
                  'state changes; if the product supports both, one must not silently imply the other unless that '
                  'coupling is explicitly part of the interaction model.',
     'intent': 'Preserve attention semantics when users organize notifications without necessarily consuming or '
               'resolving them.',
     'applies_when': ['The notification center supports both read or unread state and archive, hide, move, or '
                      'inbox-removal state.'],
     'does_not_apply_when': [],
     'failure_modes': ['Archiving automatically marks unread events as read with no indication, or marking read removes '
                       'them from the inbox even when archive is presented separately.'],
     'user_impacts': ['Users can lose track of unseen events or have badge counts change in ways that contradict the '
                      'controls they used.'],
     'observables': ['Archive unread events, mark archived events read, restore them, and compare inbox membership, read '
                     'state, badge count, and cross-device synchronization.'],
     'falsifiers': ['Read and archive remain separately represented unless the product explicitly defines and '
                    'consistently applies a combined action.'],
     'repairs': ['Store attention state and inbox-organization state independently and derive controls and counts from '
                 'their separate values.'],
     'exceptions': [],
     'verification': ['Test read, unread, archive, restore, bulk actions, and device sync and verify neither state '
                      'mutates the other unexpectedly.'],
     'owner_hints': ['designing-notification-centers'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.notifications.grouped-summary-does-not-hide-actionable-child',
     'domain': 'notifications',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Grouped notification summaries must not hide unresolved actionable children',
     'statement': 'When several notifications are grouped into one summary, the group must still expose that one or more '
                  'child events require distinct action when resolving the summary does not automatically resolve those '
                  'children.',
     'intent': 'Prevent visual grouping from collapsing multiple obligations into a misleading single completed state.',
     'applies_when': ['The notification center groups events by conversation, project, source, time window, or category '
                      'and some child events have independent actions or deadlines.'],
     'does_not_apply_when': [],
     'failure_modes': ['The summary appears resolved or dismissible while actionable child notifications remain hidden '
                       'and unresolved behind the group.'],
     'user_impacts': ['Users can clear a group believing all work is handled and miss a specific approval, reply, alert, '
                      'or deadline contained inside it.'],
     'observables': ['Create groups with mixed informational and actionable children, resolve different subsets, and '
                     'inspect summary state, child visibility, and remaining action counts.'],
     'falsifiers': ['The group communicates unresolved actionable children and summary-level actions cannot falsely mark '
                    'them complete unless the action actually covers their scope.'],
     'repairs': ['Aggregate group state from child action requirements and expose expansion or direct child actions '
                 'whenever unresolved obligations differ.'],
     'exceptions': [],
     'verification': ['Test mixed groups, child expiry, partial resolution, new arrivals, and cross-device updates and '
                      'verify the summary never conceals remaining action authority.'],
     'owner_hints': ['designing-notification-centers'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-notification-interruption-owners-v13'],
     'status': 'active'},
]

__all__ = ['NOTIFICATION_ATTENTION_RULES_V13']
