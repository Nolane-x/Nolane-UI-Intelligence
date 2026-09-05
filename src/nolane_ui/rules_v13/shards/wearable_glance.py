"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

WEARABLE_GLANCE_RULES_V13 = [{'rule_id': 'ui.wearable.glance-surface-minimizes-sensitive-disclosure',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Wearable glance surfaces must minimize sensitive disclosure on casually visible displays',
  'statement': 'Complications, always-on displays, lock-screen cards, and short glance summaries should avoid '
               'exposing sensitive details unless the product has a deliberate privacy model for that viewing '
               'context.',
  'intent': 'Account for the unusually public and ambient nature of wearable screens that may be visible to nearby '
            'people without an explicit app-open gesture.',
  'applies_when': ['The product renders health, financial, message, identity, workplace, or other sensitive '
                   'information on wearable surfaces designed for passive glancing.'],
  'does_not_apply_when': [],
  'failure_modes': ['A glance surface exposes detailed sensitive content even when the corresponding phone or full '
                    'app would require a stronger reveal or authentication boundary.'],
  'user_impacts': ['Private information can be disclosed to bystanders or on an unattended wrist simply because the '
                   'summary surface optimized for convenience.'],
  'observables': ['Inspect locked, always-on, lowered-wrist, notification, and complication states with '
                  'representative sensitive content and privacy settings.'],
  'falsifiers': ['Sensitive detail is minimized, redacted, or intentionally permitted by an explicit user-controlled '
                 'policy appropriate to the wearable context.'],
  'repairs': ['Classify glanceable fields by disclosure sensitivity and render bounded summaries until '
              'authentication or an explicit reveal gesture occurs.'],
  'exceptions': [],
  'verification': ['Test privacy settings, lock states, wrist detection, notification previews, and always-on modes '
                   'and confirm sensitive detail follows the declared policy.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.stale-complication-state-visible',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Wearable complications must reveal when displayed data is stale or disconnected',
  'statement': 'A glanceable metric that cannot refresh because the companion app, network, sensor, or sync path is '
               'unavailable must not continue to look like a current live reading.',
  'intent': 'Keep tiny summary surfaces honest about freshness when users may act on a value without opening the '
            'full application.',
  'applies_when': ['A wearable complication or tile caches a value whose authoritative source can stop updating '
                   'independently of the wearable display.'],
  'does_not_apply_when': [],
  'failure_modes': ['An old metric remains visually indistinguishable from a freshly synchronized value after the '
                    'product knows updates are no longer arriving.'],
  'user_impacts': ['Users can make decisions from obsolete health, schedule, weather, finance, or operational '
                   'information while believing it is current.'],
  'observables': ['Interrupt the source or companion sync after a successful update and inspect age, stale '
                  'indicators, and refresh behavior over time.'],
  'falsifiers': ['The surface exposes freshness or a stale/disconnected state appropriate to its limited space '
                 'without fabricating a current timestamp.'],
  'repairs': ['Carry last-authoritative-update metadata into the complication model and reserve a compact stale '
              'treatment that survives ambient modes.'],
  'exceptions': [],
  'verification': ['Test offline, companion unavailable, sensor stopped, background refresh disabled, and recovery '
                   'states and confirm freshness never appears newer than the evidence.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.rotary-navigation-keeps-focus-identity',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Rotary navigation must preserve logical focus identity while lists recycle or reorder',
  'statement': 'When a crown, bezel, or rotary input scrolls through virtualized wearable content, the focused '
               'logical item must not jump to a different record merely because visible cells are recycled or '
               'reordered.',
  'intent': 'Maintain orientation on small screens where rotary input often controls both scrolling and selection '
            'without pointer confirmation.',
  'applies_when': ['The wearable interface uses a rotary control to navigate or focus dynamic lists, pickers, menus, '
                   'or virtualized collections.'],
  'does_not_apply_when': [],
  'failure_modes': ['After data refresh or cell recycling, continued rotation acts on a different logical item even '
                    'though focus styling appears to remain in the same visual position.'],
  'user_impacts': ['Users can select, dismiss, or change the wrong item because focus follows recycled view position '
                   'rather than stable content identity.'],
  'observables': ['Rotate through a dynamic or virtualized list while inserting, removing, and reordering items and '
                  'trace focus identity across updates.'],
  'falsifiers': ['Focus remains bound to stable item identity or deliberately moves to a predictable neighbor when '
                 'the focused item no longer exists.'],
  'repairs': ['Track rotary focus by stable record key and reconcile viewport position separately from logical '
              'selection.'],
  'exceptions': [],
  'verification': ['Exercise list refresh, virtualization, pagination, reorder, and focused-item deletion and '
                   'confirm rotary actions always target the visibly focused logical item.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
  'verifier_hints': ['critiquing-input-modality'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.quick-action-confirmation-matches-consequence',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Wearable quick actions must use confirmation proportional to their consequence',
  'statement': 'A one-tap or one-gesture wearable action that sends, pays, unlocks, deletes, stops a safety process, '
               'or causes another consequential side effect must preserve an appropriate confirmation or recovery '
               'boundary.',
  'intent': 'Prevent tiny-screen acceleration from bypassing safeguards merely because the wearable experience '
            'optimizes for short interactions.',
  'applies_when': ['A wearable surface exposes fast actions whose equivalent full application treats them as '
                   'consequential or difficult to reverse.'],
  'does_not_apply_when': [],
  'failure_modes': ['The wearable action commits immediately while the full app requires review, target '
                    'confirmation, authentication, or undo for the same consequence.'],
  'user_impacts': ['Accidental taps, wrist gestures, or misunderstood summaries can cause disproportionate side '
                   'effects with little opportunity to recover.'],
  'observables': ['Compare the same high-consequence action on wearable and full application surfaces, including '
                  'confirmation, target identity, authentication, and undo behavior.'],
  'falsifiers': ['The wearable path preserves an equivalent risk boundary adapted to limited space and interaction '
                 'time.'],
  'repairs': ['Route wearable quick actions through canonical action authority and use concise but sufficient target '
              'and consequence confirmation.'],
  'exceptions': [],
  'verification': ['Exercise accidental activation, stale notification actions, target changes, and offline retries '
                   'and confirm no consequence bypasses required safeguards.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.phone-handoff-preserves-task-context',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Handoff from wearable to phone must preserve the exact task context being continued',
  'statement': 'When a wearable delegates a complex step to a companion phone, the phone should open the relevant '
               'record, draft, action, or workflow state instead of dropping users at a generic app home screen.',
  'intent': 'Make cross-device continuation feel like one task rather than forcing users to rediscover the object '
            'they already selected on the watch.',
  'applies_when': ['A wearable intentionally defers detailed editing, authentication, review, media, or data entry '
                   'to a companion phone application.'],
  'does_not_apply_when': [],
  'failure_modes': ['The phone opens successfully but loses the selected item or unresolved action that caused the '
                    'handoff.'],
  'user_impacts': ['Users must repeat navigation or may continue on the wrong record because the small device did '
                   'not transfer stable task identity.'],
  'observables': ['Initiate handoff from different items and workflow steps, then inspect deep-link parameters, '
                  'destination state, and account context on the phone.'],
  'falsifiers': ['The companion opens the same logical task under the correct account and handles stale or '
                 'unavailable targets with an explicit recovery state.'],
  'repairs': ['Encode stable task and object identity into the handoff payload and validate account, version, and '
              'permission before restoring the destination state.'],
  'exceptions': [],
  'verification': ['Test handoff after data refresh, account switch, target deletion, and delayed phone opening and '
                   'confirm context is preserved or truthfully rejected.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.truncation-does-not-invert-status',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Glanceable truncation must not remove the words that distinguish opposite statuses',
  'statement': 'On compact wearable surfaces, shortening text must preserve the semantic fragment that '
               'differentiates states such as enabled versus disabled, sent versus not sent, or due versus overdue.',
  'intent': 'Prevent aggressive space reduction from turning a glance into a misleading status interpretation.',
  'applies_when': ['Status text can exceed available wearable width and the product truncates, abbreviates, or '
                   'compresses it for complications, tiles, lists, or notifications.'],
  'does_not_apply_when': [],
  'failure_modes': ['The visible truncated text removes negation, qualifiers, units, or target identity so two '
                    'materially different statuses appear the same.'],
  'user_impacts': ['Users can make a wrong quick decision because the compact display erased the exact information '
                   'needed to distinguish state.'],
  'observables': ['Render representative long localized statuses and compare full semantic text with the actual '
                  'visible fragment in the smallest supported surfaces.'],
  'falsifiers': ['Compact wording or layout preserves the differentiating semantic content, with a full-detail route '
                 'when the surface cannot safely summarize it.'],
  'repairs': ['Author dedicated glanceable status variants and prioritize semantic qualifiers over decorative or '
              'redundant wording during compression.'],
  'exceptions': [],
  'verification': ['Test long names, negation, units, localization expansion, and multiple text sizes and confirm '
                   'truncation never collapses opposite states into the same visible meaning.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.live-session-stop-boundary-visible',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Stopping a live wearable session must clearly distinguish pause, end, and save outcomes',
  'statement': 'For ongoing workouts, recordings, timers, navigation, monitoring, or similar sessions, the stop '
               'interaction must make clear whether the session pauses, ends permanently, saves, discards, or '
               'continues on another device.',
  'intent': 'Avoid irreversible session loss on a small device where pause and stop controls can be adjacent and '
            'task state may be valuable.',
  'applies_when': ['The wearable manages a live session with multiple lifecycle outcomes such as pause, resume, '
                   'stop, finish, save, discard, or handoff.'],
  'does_not_apply_when': [],
  'failure_modes': ['A generic Stop action commits an irreversible end or discard without making the resulting '
                    'session state clear before or immediately after activation.'],
  'user_impacts': ['Users can lose recorded activity or unintentionally keep a sensitive live session running '
                   'because lifecycle boundaries are ambiguous.'],
  'observables': ['Exercise pause, resume, stop, finish, save, and discard paths and compare visible labels with '
                  'authoritative session and persisted-history state.'],
  'falsifiers': ['Each lifecycle action has a distinct consequence and the resulting session state is visible and '
                 'recoverable where product policy permits.'],
  'repairs': ['Model session lifecycle explicitly and map compact controls to named transitions rather than '
              'overloading one ambiguous stop state.'],
  'exceptions': [],
  'verification': ['Test accidental activation, device lock, battery loss, companion handoff, and resume after '
                   'interruption and confirm session state remains unambiguous.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.wearable.offline-capability-visible-before-action',
  'domain': 'wearable',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Wearable actions that require connectivity must reveal offline capability before activation',
  'statement': 'A wearable surface should distinguish actions that can complete locally from those that require '
               'phone, network, or cloud connectivity before the user depends on them.',
  'intent': 'Avoid making tiny action affordances look equally available when some cannot succeed in the current '
            'connectivity state.',
  'applies_when': ['The wearable mixes locally executable actions with companion-dependent or network-dependent '
                   'actions and can become disconnected.'],
  'does_not_apply_when': [],
  'failure_modes': ['A cloud-dependent action appears normal offline and only fails after the user invests '
                    'interaction effort or assumes the consequence occurred.'],
  'user_impacts': ['Users can miss time-sensitive actions or believe a message, command, payment, or synchronization '
                   'succeeded when no route existed.'],
  'observables': ['Disconnect phone and network independently, inspect action availability, and compare attempted '
                  'results with authoritative local and remote state.'],
  'falsifiers': ['Connectivity-dependent actions are marked unavailable or queued truthfully while local actions '
                 'remain usable where supported.'],
  'repairs': ['Attach capability requirements to wearable action state and compute availability from current '
              'connectivity rather than from static feature presence.'],
  'exceptions': [],
  'verification': ['Test phone-only, network-only, fully offline, reconnecting, and queued states and confirm the '
                   'visible capability boundary matches actual execution.'],
  'owner_hints': ['designing-wearable-glanceable-interfaces'],
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
  'provenance_ids': ['nui-wearable-owners-v13'],
  'status': 'active'}]

__all__ = ["WEARABLE_GLANCE_RULES_V13"]
