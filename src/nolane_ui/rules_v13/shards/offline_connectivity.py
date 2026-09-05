"""V13 offline and connectivity rules for queued authority, freshness, updates, and reconciliation."""
from __future__ import annotations

from ._capabilities import interaction_caps


OFFLINE_CONNECTIVITY_RULES_V13 = [
    {'rule_id': 'ui.offline.queued-mutation-bound-to-account',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Offline mutation queues must stay bound to the identity that created them',
     'statement': 'An offline mutation created under one account or tenant must not be submitted later under a different '
                  'active identity merely because the client reconnects after an account switch.',
     'intent': 'Keep deferred side effects attached to the authority and data scope under which the user originally '
               'created them.',
     'applies_when': ['The client allows creating mutations while offline and also supports account, tenant, or '
                      'workspace switching before those mutations synchronize.'],
     'does_not_apply_when': [],
     'failure_modes': ['Queued operations are stored without creator identity and flush under whichever account happens '
                       'to be active at reconnect time.'],
     'user_impacts': ['Users can modify the wrong account or leak data across tenants even though the original offline '
                      'action was correctly scoped when created.'],
     'observables': ['Create offline mutations under account A, switch to account B, reconnect, and compare queue '
                     'identity, authorization checks, and authoritative mutation targets.'],
     'falsifiers': ['Each queued operation either syncs under its original still-valid identity context or pauses for '
                    'explicit reauthorization; it never silently adopts another account.'],
     'repairs': ['Persist identity and tenant scope with every deferred mutation and revalidate that scope before '
                 'submission after reconnect or account change.'],
     'exceptions': [],
     'verification': ['Test account switch, sign-out, tenant switch, role downgrade, and reconnect with pending '
                      'mutations and verify no operation crosses its original authority boundary.'],
     'owner_hints': ['designing-offline-degraded-experiences'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.cached-data-shows-last-authoritative-sync',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Offline cached data must expose when it was last synchronized authoritatively',
     'statement': 'When a surface renders cached records without current server contact, it must distinguish that '
                  'offline snapshot from freshly synchronized data and expose a meaningful last-authoritative-sync basis '
                  'when staleness affects decisions.',
     'intent': 'Let users understand the age and authority of cached state instead of treating local availability as '
               'proof of freshness.',
     'applies_when': ['The application can show previously synchronized data while offline or during degraded '
                      'connectivity.'],
     'does_not_apply_when': [],
     'failure_modes': ['Cached content keeps ordinary online freshness labels or a generic current state even though no '
                       'successful synchronization has occurred since a known earlier time.'],
     'user_impacts': ['Users can act on outdated balances, assignments, inventory, messages, or status while believing '
                      'the information is current.'],
     'observables': ['Synchronize at a known timestamp, go offline for controlled intervals, mutate server fixtures '
                     'separately, and inspect visible freshness state and last-sync metadata.'],
     'falsifiers': ['The offline view identifies its cached status and last authoritative synchronization without '
                    'resetting freshness just because the screen rerenders locally.'],
     'repairs': ['Persist authoritative sync completion time separately from local read time and derive stale/offline '
                 'presentation from that synchronization evidence.'],
     'exceptions': [],
     'verification': ['Test fresh cache, aged cache, failed refresh, partial refresh, app restart, and clock change and '
                      'verify freshness always reflects the last successful authority contact.'],
     'owner_hints': ['designing-offline-degraded-experiences'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.update-activation-preserves-unsaved-work',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Application update activation must not discard unsaved local work',
     'statement': 'When a service-worker, desktop bundle, or application update activates while a user has unsaved local '
                  'state, the update transition must preserve or deliberately hand off that work rather than forcing a '
                  'reload that erases it.',
     'intent': 'Keep software freshness from becoming an unexpected destructive action against in-progress user '
               'authorship.',
     'applies_when': ['The product can activate a new application version or reload client assets while editors, forms, '
                      'uploads, or other unsaved work remain open.'],
     'does_not_apply_when': [],
     'failure_modes': ['The update flow refreshes or replaces the running client without snapshotting local work, '
                       'causing drafts or pending input to disappear.'],
     'user_impacts': ['Users can lose substantial work because a maintenance event occurred independently of their '
                      'task.'],
     'observables': ['Open unsaved work, trigger update activation and reload paths at several lifecycle points, then '
                     'compare restored local state with the pre-update snapshot.'],
     'falsifiers': ['Unsaved work survives through migration or the product explicitly blocks activation until the user '
                    'resolves it; no silent data loss occurs.'],
     'repairs': ['Coordinate update activation with a local-draft persistence or handoff protocol and delay destructive '
                 'reloads when that protocol cannot complete safely.'],
     'exceptions': [],
     'verification': ['Test background update, manual refresh prompt, crash recovery, schema migration, and multi-tab '
                      'update activation and verify all valid unsaved work remains recoverable.'],
     'owner_hints': ['designing-offline-degraded-experiences'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.expired-auth-pauses-sync-with-local-work-preserved',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Expired authentication must pause offline synchronization without discarding local work',
     'statement': 'If authentication expires while offline changes are pending, reconnect must preserve the local queue '
                  'and require renewed authority before sync instead of deleting the queue or submitting it with stale '
                  'credentials.',
     'intent': 'Separate local authorship from server authorization so credential expiry blocks commit but not '
               'recoverable work.',
     'applies_when': ['Users can accumulate valid local changes while offline and their authenticated session can expire '
                      'before connectivity returns.'],
     'does_not_apply_when': [],
     'failure_modes': ['Reconnect either drops pending changes because the session is invalid or repeatedly submits them '
                       'under expired credentials until the client gives up.'],
     'user_impacts': ['Users can lose work or receive misleading sync failures even though reauthentication could '
                      'restore a valid commit path.'],
     'observables': ['Expire the session while offline mutations exist, reconnect, reauthenticate, and compare queue '
                     'contents and final authoritative results throughout the flow.'],
     'falsifiers': ['Pending work remains intact during the auth boundary and resumes only after renewed authorization '
                    'revalidates its targets and scope.'],
     'repairs': ['Pause the sync worker on authentication failure, persist the queue separately from credentials, and '
                 'resume through a deliberate reauthentication continuation.'],
     'exceptions': [],
     'verification': ['Test token expiry, explicit revocation, password change, account lock, and successful '
                      'reauthentication with pending offline work and verify no queue item is lost or prematurely '
                      'committed.'],
     'owner_hints': ['designing-connectivity-recovery'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13', 'nist-sp800-63b4-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.capability-boundary-visible-before-action',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Offline mode should reveal unsupported actions before users invest in them',
     'statement': 'When an action fundamentally requires online authority and cannot be queued or completed offline, the '
                  'interface should communicate that boundary before the user performs substantial input or reaches the '
                  'final commit step.',
     'intent': 'Prevent offline degradation from masquerading as full capability until the moment a task fails '
               'irrecoverably.',
     'applies_when': ['The product remains partially usable offline but some workflows cannot be completed, queued, or '
                      'safely validated without server contact.'],
     'does_not_apply_when': [],
     'failure_modes': ['Users fill a long form, compose an unsupported attachment workflow, or make complex selections '
                       'before the product reveals only at commit that offline completion is impossible.'],
     'user_impacts': ['Users waste effort and may lose input even though the client already knew the capability was '
                      'unavailable.'],
     'observables': ['Enter offline mode before each workflow and compare early control state, explanatory copy, draft '
                     'preservation, and the eventual commit behavior.'],
     'falsifiers': ['Unsupported online-only actions are identified at a useful early boundary while queueable or '
                    'locally valid work remains available.'],
     'repairs': ['Expose connectivity requirements from capability metadata near the action entry point and preserve '
                 'drafts if the boundary is reached after connectivity unexpectedly drops.'],
     'exceptions': [],
     'verification': ['Test entering offline before a task, losing connectivity mid-task, and restoring connectivity and '
                      'verify the UI distinguishes unavailable, queueable, and locally complete actions.'],
     'owner_hints': ['designing-offline-degraded-experiences'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.retry-queue-preserves-operation-order',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Offline retry queues must preserve required causal operation ordering',
     'statement': 'When queued mutations depend on one another, retry and reconnect logic must not reorder them in a way '
                  'that applies a later operation before the prerequisite state it references has become authoritative.',
     'intent': 'Preserve user-intended causality across deferred synchronization rather than treating every queued '
               'mutation as independently replayable.',
     'applies_when': ['Offline work can create, rename, edit, move, or delete the same logical object through a sequence '
                      'of dependent operations before reconnect.'],
     'does_not_apply_when': [],
     'failure_modes': ['Parallel retry or queue compaction submits later mutations ahead of their prerequisites, '
                       'producing invalid references, resurrected state, or server conflicts.'],
     'user_impacts': ['Users can see operations applied in an order they never performed and may be unable to '
                      'reconstruct the intended final state.'],
     'observables': ['Create dependency chains offline, inject transient failures into selected queue entries, '
                     'reconnect, and record actual server commit order and resulting object history.'],
     'falsifiers': ['Operations with causal dependencies preserve their required order, while independent operations may '
                    'be parallelized only when the model proves they commute safely.'],
     'repairs': ['Encode dependency or object-version relationships in the queue and schedule retries from those '
                 'constraints rather than from raw request readiness alone.'],
     'exceptions': [],
     'verification': ['Test create-then-edit, rename-then-move, edit-then-delete, and interleaved independent objects '
                      'under selective retry failures and verify authoritative order matches the declared dependency '
                      'model.'],
     'owner_hints': ['designing-offline-degraded-experiences'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.background-sync-result-reconciles-visible-state',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Background synchronization results must reconcile into the visible application state',
     'statement': 'If pending offline work synchronizes in the background, open surfaces must reconcile the confirmed '
                  'result, rejection, conflict, or transformed server value instead of continuing to display the earlier '
                  'optimistic local state indefinitely.',
     'intent': 'Close the loop between deferred background authority and the foreground UI so users do not act on a '
               'local fiction after sync has finished.',
     'applies_when': ['The platform can synchronize queued mutations while the initiating screen is backgrounded, '
                      'closed, or later reopened.'],
     'does_not_apply_when': [],
     'failure_modes': ['Background sync succeeds or fails but visible records remain in queued or optimistic state until '
                       'a full reload, with no conflict or server-normalization update.'],
     'user_impacts': ['Users can repeat work, miss failures, or trust values that no longer match the authoritative '
                      'server record.'],
     'observables': ['Queue mutations, allow background sync to resolve while the relevant view is inactive, reopen it, '
                     'and compare local state with the authoritative sync result and event log.'],
     'falsifiers': ['Foreground state consumes the sync outcome and transitions each affected record to confirmed, '
                    'transformed, failed, or conflicted state without requiring a blind reload.'],
     'repairs': ['Publish durable sync outcomes keyed by operation and record identity, then reconcile active stores '
                 'when the application resumes or observes those outcomes.'],
     'exceptions': [],
     'verification': ['Test success, normalization, rejection, conflict, and partial batch results while the app is '
                      'backgrounded and verify the resumed UI reflects each authoritative outcome.'],
     'owner_hints': ['designing-connectivity-recovery'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.offline.local-delete-conflict-does-not-silently-resurrect',
     'domain': 'offline',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'An offline local deletion must not silently resurrect after conflicting remote edits',
     'statement': 'When a user deletes an object offline and another client edits that same object before '
                  'synchronization, reconciliation must surface or resolve the delete-versus-edit conflict according to '
                  'explicit policy rather than quietly restoring the remote version as if the deletion never happened.',
     'intent': 'Protect destructive offline intent from disappearing inside last-writer behavior that the user cannot '
               'observe.',
     'applies_when': ['The product permits deleting or archiving shared objects offline while other clients may continue '
                      'mutating those objects online.'],
     'does_not_apply_when': [],
     'failure_modes': ['Reconnect applies the remote edit and recreates the object locally with no indication that the '
                       'queued deletion lost, or applies deletion without exposing that remote work existed.'],
     'user_impacts': ["Users can believe deletion succeeded when the object returns, or erase collaborators' new work "
                      'without understanding the conflict.'],
     'observables': ['Delete offline, edit remotely, reconnect in both event orders, and inspect conflict state, '
                     'history, resulting record lifecycle, and available recovery paths.'],
     'falsifiers': ['The product follows a documented conflict policy that preserves or exposes both intents before '
                    'irreversible loss and does not disguise one outcome as an ordinary refresh.'],
     'repairs': ['Treat lifecycle mutations as conflict-bearing operations with version preconditions and route '
                 'delete-versus-edit collisions into explicit resolution or auditable policy.'],
     'exceptions': [],
     'verification': ['Test delete/edit, archive/edit, restore/delete, and repeated reconnect ordering and verify every '
                      'conflict resolves according to the declared lifecycle policy.'],
     'owner_hints': ['designing-connectivity-recovery'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-offline-connectivity-owners-v13'],
     'status': 'active'},
]

__all__ = ['OFFLINE_CONNECTIVITY_RULES_V13']
