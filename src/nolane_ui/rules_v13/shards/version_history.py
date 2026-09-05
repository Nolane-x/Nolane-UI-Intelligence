"""V13 seventh-wave independently authored rules for version history."""
from __future__ import annotations

from ._capabilities import interaction_caps


VERSION_HISTORY_RULES_V13 = [{'rule_id': 'ui.versioning.restore-target-version-previewed',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Version restore must preview the exact historical state that will become current',
  'statement': 'A restore action must identify the target revision and material state that will be '
               'reinstated rather than presenting a generic restore button beside an ambiguous timestamp.',
  'intent': 'Prevent users from replacing current work with the wrong historical state when revisions are '
            'dense, similarly named, or partially previewable.',
  'applies_when': ['The product supports restoring prior versions of documents, records, configurations, or '
                   'project state.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user can commit restore without a trustworthy preview or stable revision identity, '
                    'especially when timestamps collide or list order changes.'],
  'user_impacts': ['Current work can be overwritten by an unintended revision and the user may not realize '
                   'which historical state was chosen.'],
  'observables': ['Open several similar revisions, reorder or refresh history, then invoke restore and '
                  'compare the previewed revision ID with the resulting current state.'],
  'falsifiers': ['The confirmation binds to a stable revision identity and exposes enough material content '
                 'or metadata to distinguish it from neighboring versions.'],
  'repairs': ['Use immutable revision identifiers in restore commands and provide a revision-bound preview '
              'or change summary before commit.'],
  'exceptions': [],
  'verification': ['Restore revisions with identical labels and close timestamps, verifying the committed '
                   'state always matches the previewed immutable target.'],
  'owner_hints': ['designing-version-history'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.restore-preserves-newer-history',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Restoring an older version must not silently erase the versions created after it',
  'statement': 'A restore should create or select a new current state while preserving later history unless '
               'the product explicitly offers destructive history truncation with a separate consequence '
               'boundary.',
  'intent': 'Keep rollback reversible and preserve evidence of work that happened after the restored '
            'revision.',
  'applies_when': ['Version history is expected to be durable and users can restore an older revision while '
                   'newer revisions exist.'],
  'does_not_apply_when': [],
  'failure_modes': ['Restoring revision 4 deletes revisions 5 through 9 or makes them unreachable without '
                    'warning because the system rewinds the history pointer destructively.'],
  'user_impacts': ['Users can lose later work and the ability to undo the restore despite using a feature '
                   'presented as recovery.'],
  'observables': ['Create several versions, restore an early one, then inspect whether later versions remain '
                  'addressable and whether the restore itself has history identity.'],
  'falsifiers': ['Later revisions remain available or destructive truncation is explicitly previewed, '
                 'confirmed, and governed as an irreversible action.'],
  'repairs': ['Implement ordinary restore as a new revision or current-pointer transition that preserves '
              'prior lineage; separate history deletion into its own action.'],
  'exceptions': [],
  'verification': ['Restore repeatedly across a branched history and verify all pre-existing revisions '
                   'remain recoverable under the declared model.'],
  'owner_hints': ['designing-version-history'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.concurrent-edit-version-conflict-visible',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Concurrent edits must expose when a save targets an outdated version base',
  'statement': 'When optimistic or manual saves are based on an older revision than current authoritative '
               'state, the interface must not quietly overwrite newer work without the product’s declared '
               'conflict policy becoming visible.',
  'intent': 'Prevent lost updates when two editors or automation processes modify the same versioned '
            'resource.',
  'applies_when': ['A versioned resource can be edited from multiple sessions or by users and automation '
                   'concurrently.'],
  'does_not_apply_when': [],
  'failure_modes': ['Client A saves revision 10, then stale client B based on revision 9 saves and the UI '
                    'presents success even though A’s work is lost or silently merged.'],
  'user_impacts': ['Users can lose changes or trust a version history that conceals a conflict-producing '
                   'overwrite.'],
  'observables': ['Open two edit sessions from the same revision and commit incompatible changes in '
                  'alternating order, then inspect save result and history.'],
  'falsifiers': ['The stale save is rejected, merged under an explicit policy, or recorded as a distinct '
                 'branch/conflict rather than silently replacing unknown newer state.'],
  'repairs': ['Include base revision identity in writes and reconcile version conflicts through a '
              'product-defined merge, branch, or retry flow.'],
  'exceptions': [],
  'verification': ['Repeat conflicting saves across fields and large payloads, verifying the same conflict '
                   'policy appears in UI and version history.'],
  'owner_hints': ['designing-version-history'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.rename-move-preserves-history-continuity',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Renaming or moving a versioned item must preserve its history identity',
  'statement': 'A file or object history should follow the stable resource through rename and move '
               'operations instead of splitting into unrelated histories keyed only by path or display name.',
  'intent': 'Let users understand lineage after organizational changes and avoid treating moved content as '
            'newly created data.',
  'applies_when': ['A versioned item can be renamed or moved between folders, collections, or project '
                   'locations.'],
  'does_not_apply_when': [],
  'failure_modes': ['After a move, the destination shows no earlier versions or the source history appears '
                    'to belong to a deleted unrelated item because history was keyed by path.'],
  'user_impacts': ['Users cannot recover earlier content or establish lineage across routine organization '
                   'changes.'],
  'observables': ['Create versions before and after several renames and moves, then navigate history from '
                  'the current item and historical locations.'],
  'falsifiers': ['The current item exposes continuous lineage with move/rename events, while old paths '
                 'explain the transition rather than creating duplicate identities.'],
  'repairs': ['Bind history to stable resource identity and record path or name changes as versioned '
              'metadata events.'],
  'exceptions': [],
  'verification': ['Move and rename items across nested locations, then restore pre-move versions and verify '
                   'identity, path semantics, and history remain coherent.'],
  'owner_hints': ['designing-file-rename-move-conflicts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.lock-owner-and-expiry-visible',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Checkout or edit locks must show their owner, scope, and expiry or release condition',
  'statement': 'When editing is blocked by a lock, the product must explain who or what holds it and the '
               'condition under which it can be released, without inventing certainty if expiry is unknown.',
  'intent': 'Turn a blocked editing state into an actionable coordination problem rather than an unexplained '
            'disabled surface.',
  'applies_when': ['The product supports pessimistic locks, file checkout, leases, or exclusive edit '
                   'sessions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A document is read-only because of a lock but the UI gives no owner, scope, or release '
                    'information, or displays a countdown that is not authoritative.'],
  'user_impacts': ['Users may create duplicate copies, override legitimate work, or wait unnecessarily '
                   'because they cannot coordinate with the lock holder.'],
  'observables': ['Acquire a lock from another session, vary lease expiry and owner availability, and '
                  'inspect the blocked editor plus file browser.'],
  'falsifiers': ['The lock state identifies the holder or system source where permitted and shows only '
                 'authoritative expiry/release information with an appropriate recovery path.'],
  'repairs': ['Expose lock metadata from the authoritative lock service and provide refresh, '
              'request-release, or admin override according to policy.'],
  'exceptions': [],
  'verification': ['Test active, expired, orphaned, and remotely released locks, verifying all open clients '
                   'reconcile without false countdown or stale ownership.'],
  'owner_hints': ['designing-file-locking-and-checkout'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.trash-retention-and-deletion-state-visible',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Trash and retention state must make final deletion timing and recoverability explicit',
  'statement': 'Items moved to trash must communicate whether they are recoverable, until when, and whether '
               'policy or legal retention changes the normal deletion schedule.',
  'intent': 'Help users distinguish reversible removal from irreversible deletion without relying on generic '
            'trash metaphors.',
  'applies_when': ['Deleted items enter a trash, recycle-bin, retention, or soft-delete lifecycle before '
                   'possible permanent removal.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface says “deleted” without showing recoverability, or shows a fixed retention '
                    'countdown even when policy hold prevents final deletion.'],
  'user_impacts': ['Users can miss the recovery window or falsely believe sensitive data has been '
                   'permanently removed.'],
  'observables': ['Delete items under normal retention and under a hold or admin policy, then inspect trash, '
                  'detail, and restore surfaces over time.'],
  'falsifiers': ['The UI reflects current recoverability and authoritative retention state and does not '
                 'promise final deletion while a hold or unresolved policy condition remains.'],
  'repairs': ['Model soft-delete, retention, hold, restore, and final purge as distinct lifecycle states '
              'with authoritative timestamps where available.'],
  'exceptions': [],
  'verification': ['Exercise restore before expiry, hold insertion, expiry, and permanent purge, confirming '
                   'every state and action matches backend recoverability.'],
  'owner_hints': ['designing-trash-and-restore'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.compare-version-identities-stable',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Version comparison must keep left and right revision identities stable while navigating '
           'differences',
  'statement': 'A compare view must preserve which exact revisions occupy each side even when users jump '
               'between changes, change sorting, or open related history panels.',
  'intent': 'Prevent reviewers from interpreting a difference under the wrong baseline after UI navigation '
            'mutates comparison context.',
  'applies_when': ['Users can compare any two historical revisions and navigate through multiple changed '
                   'sections.'],
  'does_not_apply_when': [],
  'failure_modes': ['Selecting a history item, opening a side panel, or following next-change unexpectedly '
                    'updates one side of the comparison without clearly changing the header.'],
  'user_impacts': ['A user may approve or restore based on a diff they believe compares different versions '
                   'than the data actually shown.'],
  'observables': ['Choose nonadjacent revisions, navigate every diff affordance, and verify stable revision '
                  'IDs in the header and underlying request parameters.'],
  'falsifiers': ['The left and right immutable revision identities remain unchanged until the user '
                 'explicitly chooses a new comparison target.'],
  'repairs': ['Store comparison endpoints as explicit route or state parameters and require a deliberate '
              'action to replace either endpoint.'],
  'exceptions': [],
  'verification': ['Exercise back/forward navigation, deep links, and history selection, verifying the '
                   'displayed diff and labeled endpoints stay in sync.'],
  'owner_hints': ['designing-version-history'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.versioning.autosave-vs-published-boundary-explicit',
  'domain': 'versioning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Autosaved draft state must remain distinct from the last published or committed version',
  'statement': 'A versioned authoring surface must show whether recent edits are merely local/autosaved '
               'draft state or have become the published, shared, deployed, or otherwise authoritative '
               'version.',
  'intent': 'Prevent users from assuming visible edits are already live or from publishing stale content '
            'because draft and published states look identical.',
  'applies_when': ['The product has automatic draft persistence plus a separate publish, commit, submit, or '
                   'release boundary.'],
  'does_not_apply_when': [],
  'failure_modes': ['The editor says “Saved” after autosave without clarifying that the public or '
                    'authoritative version is still older.'],
  'user_impacts': ['Authors can leave important changes unpublished or communicate that content is live when '
                   'only a private draft exists.'],
  'observables': ['Edit a published item, allow autosave, reload, and inspect both editor and public '
                  'representation before and after explicit publish.'],
  'falsifiers': ['The editor distinguishes draft persistence from publication and identifies the currently '
                 'published revision independently of autosave success.'],
  'repairs': ['Use separate draft and published revision state, and label save feedback according to the '
              'boundary that actually completed.'],
  'exceptions': [],
  'verification': ['Exercise autosave failures, reload, multiple drafts, and publish, verifying “saved” and '
                   '“published” never collapse into one ambiguous state.'],
  'owner_hints': ['designing-builder-preview-publish-modes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-version-history-owners-v13'],
  'status': 'active'}]

__all__ = ["VERSION_HISTORY_RULES_V13"]
