"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

REALTIME_FEED_RULES_V13 = [{'rule_id': 'ui.realtime.reconnect-gap-visible',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Realtime views must expose potential event gaps after reconnect until continuity is established',
  'statement': 'When a live stream disconnects, the interface must not immediately claim continuous live state after '
               'reconnect unless it has backfilled, replayed, or otherwise verified that no events were missed.',
  'intent': 'Preserve timeline truth across transport interruptions where reconnection alone does not prove '
            'continuity.',
  'applies_when': ['The product displays a realtime feed or state stream over a connection that can drop while '
                   'events continue to occur on the server.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI returns to a normal live indicator after reconnect even though events may have occurred '
                    'during the disconnected interval and no replay was verified.'],
  'user_impacts': ['Users can miss alerts, messages, status changes, or market/operational events while believing '
                   'they observed an unbroken feed.'],
  'observables': ['Disconnect the client while generating server events, reconnect with and without replay support, '
                  'and inspect gap indicators and resulting sequence.'],
  'falsifiers': ['The client backfills from a trusted cursor or explicitly marks the continuity gap until the user '
                 'or system reconciles missing history.'],
  'repairs': ['Persist a server-issued event cursor and validate continuity on reconnect rather than treating socket '
              'establishment as evidence of complete state.'],
  'exceptions': [],
  'verification': ['Test short and long disconnects, expired cursors, server restart, and replay failure and confirm '
                   'continuity claims match actual recovered history.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.out-of-order-events-reconciled',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Out-of-order realtime events must reconcile by authoritative ordering semantics',
  'statement': 'A live interface must not apply arrival order blindly when the protocol provides revision, sequence, '
               'version, or causal metadata that defines the authoritative order of state changes.',
  'intent': 'Prevent network jitter and parallel delivery from making newer state appear to revert to older state.',
  'applies_when': ['Realtime updates for the same entity can arrive out of order and the event model includes an '
                   'ordering or version signal.'],
  'does_not_apply_when': [],
  'failure_modes': ['A delayed older event arrives after a newer one and overwrites the visible entity back to stale '
                    'state.'],
  'user_impacts': ['Users can see transiently incorrect status or take actions based on a state that the server '
                   'already superseded.'],
  'observables': ['Delay selected events to invert delivery order and compare rendered state with server sequence, '
                  'revision, or version metadata.'],
  'falsifiers': ['The client ignores, merges, or reorders stale events according to the authoritative event model '
                 'and never regresses state solely from late arrival.'],
  'repairs': ['Apply updates through entity revision or sequence checks instead of direct arrival-order mutation.'],
  'exceptions': [],
  'verification': ['Inject out-of-order create/update/delete and reconnect events and confirm final and intermediate '
                   'UI state respects the protocol’s ordering semantics.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.duplicate-event-identity-deduplicated',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Repeated delivery of the same realtime event must not create duplicate visible side effects',
  'statement': 'At-least-once or replayed event delivery must be deduplicated by stable event or operation identity '
               'before creating duplicate feed entries, counters, notifications, or downstream mutations.',
  'intent': 'Make realtime UI robust to reconnect replay and transport retries that legitimately deliver the same '
            'event more than once.',
  'applies_when': ['The realtime protocol can redeliver events because of reconnect, replay windows, consumer retry, '
                   'replication, or at-least-once semantics.'],
  'does_not_apply_when': [],
  'failure_modes': ['The same authoritative event appears twice or increments derived state twice because each '
                    'delivery is treated as a new occurrence.'],
  'user_impacts': ['Users can see duplicate messages, alerts, transactions, counts, or activity records that never '
                   'existed twice on the server.'],
  'observables': ['Deliver identical event IDs repeatedly and compare rendered feed identity, derived counters, '
                  'notifications, and persisted local state.'],
  'falsifiers': ['Repeated delivery of one event identity produces one logical UI effect while genuinely distinct '
                 'events remain separate.'],
  'repairs': ['Track processed event or operation identity at the reconciliation layer and make derived side effects '
              'idempotent.'],
  'exceptions': [],
  'verification': ['Exercise reconnect replay, duplicate packets, consumer retry, and backfill overlap and confirm '
                   'one logical event remains one visible occurrence.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.paused-feed-not-presented-as-live',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'A user-paused realtime feed must remain visibly paused until live updates resume',
  'statement': 'When users freeze, pause, scrub, or hold a live feed for inspection, the interface must retain a '
               'visible paused state and must not keep a normal live badge while new events accumulate unseen.',
  'intent': 'Prevent users from mistaking a deliberately frozen historical view for the current event stream.',
  'applies_when': ['A realtime timeline or feed supports pause, scroll lock, historical inspection, or another mode '
                   'that stops automatic advancement.'],
  'does_not_apply_when': [],
  'failure_modes': ['The feed remains labelled live even though new events are buffered and the visible viewport no '
                    'longer represents the current head.'],
  'user_impacts': ['Users can believe they are monitoring current events while actually looking at an older frozen '
                   'position.'],
  'observables': ['Pause or scroll away from the live head while events continue, then inspect live indicators, '
                  'unseen-event counts, and resume behavior.'],
  'falsifiers': ['The UI clearly differentiates paused/historical position from live head and exposes a '
                 'deterministic route to catch up or jump to current.'],
  'repairs': ['Model viewport-live attachment separately from connection health and base the live indicator on '
              'whether the visible feed follows the current head.'],
  'exceptions': [],
  'verification': ['Test pause, manual scroll, backgrounding, new-event arrival, and resume and confirm “live” '
                   'appears only when the viewport is actually current.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.backfill-distinct-from-live-arrival',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Historical backfill must remain distinguishable from events arriving live now',
  'statement': 'When older records are inserted during reconnect, pagination, or history recovery, the interface '
               'must preserve their original event time and avoid presenting the backfill as newly occurring live '
               'activity.',
  'intent': 'Keep temporal interpretation correct when old history is delivered through the same transport or '
            'rendering path as current events.',
  'applies_when': ['A realtime feed can backfill historical events after reconnect, opening a thread, pagination, or '
                   'explicit gap recovery.'],
  'does_not_apply_when': [],
  'failure_modes': ['Backfilled events trigger “new now” affordances, reorder by arrival time, or appear to have '
                    'occurred at the moment they were fetched.'],
  'user_impacts': ['Users can misread old incidents as current, receive duplicate attention signals, or lose '
                   'chronological context.'],
  'observables': ['Backfill known historical events while live traffic continues and compare event time, insertion '
                  'behavior, unread state, and notification side effects.'],
  'falsifiers': ['Backfilled items retain original temporal identity and any “new” treatment reflects user-unseen '
                 'status rather than transport arrival time.'],
  'repairs': ['Carry event-time and delivery-mode metadata through reconciliation and keep attention logic separate '
              'from network arrival.'],
  'exceptions': [],
  'verification': ['Mix backfill and live events across reconnect and pagination and confirm ordering, timestamps, '
                   'badges, and notifications preserve original chronology.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.optimistic-event-rejection-reconciled',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Rejected optimistic realtime actions must reconcile the visible feed and derived state',
  'statement': 'If a locally inserted optimistic event is later rejected by server validation or authorization, the '
               'UI must remove, mark, or recover that event and reverse dependent counters or state rather than '
               'leaving a phantom success.',
  'intent': 'Keep realtime interaction fast without allowing optimistic local state to survive after authoritative '
            'rejection.',
  'applies_when': ['The feed immediately renders user actions such as messages, reactions, updates, or commands '
                   'before the server confirms them.'],
  'does_not_apply_when': [],
  'failure_modes': ['A rejected optimistic event remains in normal successful state or its derived count remains '
                    'incremented after the server denies the mutation.'],
  'user_impacts': ['Users can believe a message, reaction, command, or update reached others when it never became '
                   'authoritative.'],
  'observables': ['Force validation, permission, moderation, and conflict rejection after optimistic insertion and '
                  'inspect item state plus derived aggregates.'],
  'falsifiers': ['Rejected optimistic state reconciles to failed, removed, or recoverable status and dependent UI '
                 'returns to authoritative values.'],
  'repairs': ['Associate optimistic events with mutation identity and apply explicit confirmation or rejection '
              'transitions to all derived state.'],
  'exceptions': [],
  'verification': ['Test delayed rejection, reconnect before acknowledgement, duplicate acknowledgements, and retry '
                   'and confirm no phantom success remains.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.permission-loss-stops-authoritative-stream',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Realtime subscriptions must stop exposing protected data after permission loss',
  'statement': 'If a user loses authority to a realtime resource while subscribed, the client and server must '
               'terminate or redact the stream and reconcile visible protected state rather than continuing delivery '
               'until refresh.',
  'intent': 'Make long-lived subscriptions obey current authorization just like ordinary request boundaries.',
  'applies_when': ['Roles, membership, sharing, or policy can change while a user maintains a live subscription to '
                   'protected data.'],
  'does_not_apply_when': [],
  'failure_modes': ['The subscription continues receiving updates after the user’s access is revoked because '
                    'authorization was checked only when the stream opened.'],
  'user_impacts': ['Revoked users can continue observing sensitive changes even though other product surfaces '
                   'correctly deny access.'],
  'observables': ['Open a protected live feed, revoke access from another session, and inspect subsequent server '
                  'delivery, client visibility, and cached content.'],
  'falsifiers': ['Stream authority is revalidated or revoked, protected updates stop, and the UI transitions to an '
                 'appropriate access-loss state.'],
  'repairs': ['Bind subscription lifetime to current authorization and propagate policy changes into stream '
              'termination or scoped redaction.'],
  'exceptions': [],
  'verification': ['Test direct revoke, group removal, temporary-grant expiry, token refresh, and reconnect and '
                   'confirm no protected event arrives after effective access loss.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.realtime.order-not-derived-from-untrusted-client-clock',
  'domain': 'realtime',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Realtime event ordering must not rely on untrusted client clocks when authoritative order exists',
  'statement': 'Feeds involving multiple clients must avoid sorting authoritative event sequence solely by '
               'client-supplied wall-clock timestamps when clock skew can reorder events incorrectly.',
  'intent': 'Prevent device time drift from becoming false causality in chat, audit, monitoring, collaboration, or '
            'transaction timelines.',
  'applies_when': ['Events originate from multiple clients with potentially different local clocks and the server or '
                   'protocol supplies a more reliable sequence or event time.'],
  'does_not_apply_when': [],
  'failure_modes': ['A client with an incorrect clock causes its event to appear before or after unrelated events '
                    'contrary to authoritative server order.'],
  'user_impacts': ['Users can misinterpret causality, response order, audit history, or the sequence of operational '
                   'changes.'],
  'observables': ['Generate events from deliberately skewed client clocks and compare displayed ordering with server '
                  'sequence or authoritative timestamps.'],
  'falsifiers': ['Ordering uses authoritative sequence or normalized event time, while client timestamps are treated '
                 'only as metadata where appropriate.'],
  'repairs': ['Sort by server-issued revision, sequence, or trusted event-time semantics and display client time '
              'separately if it has product meaning.'],
  'exceptions': [],
  'verification': ['Test positive and negative clock skew, offline creation, replay, and simultaneous events and '
                   'confirm timeline order does not depend on arbitrary device time.'],
  'owner_hints': ['designing-realtime-communication-systems'],
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
  'provenance_ids': ['nui-realtime-feed-owners-v13'],
  'status': 'active'}]

__all__ = ["REALTIME_FEED_RULES_V13"]
