"""V13 seventh-wave independently authored rules for file browser."""
from __future__ import annotations

from ._capabilities import interaction_caps


FILE_BROWSER_RULES_V13 = [{'rule_id': 'ui.filebrowser.current-directory-identity-visible',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'File browsers must expose the exact current directory or collection identity beyond a truncated '
           'title',
  'statement': 'A file browser should provide enough breadcrumb, path, workspace, or stable parent context '
               'to distinguish same-named folders and know where new files or moves will land.',
  'intent': 'Prevent actions in the wrong location when directory names repeat across roots or workspaces.',
  'applies_when': ['Users can navigate nested file hierarchies with repeated folder names or multiple '
                   'storage roots.'],
  'does_not_apply_when': [],
  'failure_modes': ['The header shows only “Assets” while several Assets folders exist and the breadcrumb is '
                    'hidden or stale after navigation.'],
  'user_impacts': ['Users can upload, create, or move files into an unintended directory despite believing '
                   'they are in another location.'],
  'observables': ['Navigate to same-named folders through different roots and inspect header, breadcrumb, '
                  'route, and create/upload targets.'],
  'falsifiers': ['The active directory resolves to a unique visible path or scope and all new operations use '
                 'that same identity.'],
  'repairs': ['Derive navigation chrome and mutation target from one stable directory identity rather than '
              'independent display labels.'],
  'exceptions': [],
  'verification': ['Test deep links, back/forward, and renamed ancestors, verifying current-directory '
                   'context never becomes ambiguous.'],
  'owner_hints': ['designing-file-browser-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.selection-survives-benign-sort-change',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'File-browser selection should remain bound to item identity through benign reordering',
  'statement': 'Sorting or refreshing a directory must not move selection to whichever row inherits the '
               'previous index when the selected file still exists.',
  'intent': 'Prevent follow-up file actions from applying to a different item after list order changes.',
  'applies_when': ['The file browser supports selection plus sorting, live updates, or metadata refresh that '
                   'can reorder visible items.'],
  'does_not_apply_when': [],
  'failure_modes': ['A selected file moves after sort and selection stays on row five, now representing '
                    'another file.'],
  'user_impacts': ['Users can delete, share, or move the wrong file immediately after a harmless sort '
                   'change.'],
  'observables': ['Select several files, change sort and metadata that causes reordering, then inspect '
                  'stable selected IDs and action preview.'],
  'falsifiers': ['Selection remains attached to the same resources or is safely cleared if the item leaves '
                 'scope, never transferred by row index.'],
  'repairs': ['Store selection by stable file identity and resolve it after collection updates.'],
  'exceptions': [],
  'verification': ['Exercise sort, live rename, and modified-time changes, verifying action targets stay '
                   'aligned with the originally selected files.'],
  'owner_hints': ['designing-file-browser-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.inline-rename-validation-preserves-name',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inline rename validation must preserve the user’s attempted name when the change is rejected',
  'statement': 'When a rename fails because of invalid characters, conflicts, permissions, or server '
               'validation, the attempted text should remain editable with a reason instead of snapping back '
               'and forcing re-entry.',
  'intent': 'Make correction efficient while preserving the authoritative old name until commit succeeds.',
  'applies_when': ['Files or folders can be renamed inline and the server may reject the requested name.'],
  'does_not_apply_when': [],
  'failure_modes': ['Submitting an invalid name closes edit mode, restores the old label, and shows a '
                    'transient error without retaining what the user typed.'],
  'user_impacts': ['Users repeat complex names and may not understand which part violated the rule.'],
  'observables': ['Attempt names that fail for different reasons and inspect edit state, authoritative '
                  'label, and recovery after each rejection.'],
  'falsifiers': ['The stored name stays unchanged while the attempted value remains available for correction '
                 'with an applicable error reason.'],
  'repairs': ['Separate draft rename text from committed file name and keep the editor open on recoverable '
              'validation failure.'],
  'exceptions': [],
  'verification': ['Test local and server-side validation, name collision, and permission failure, verifying '
                   'no rejected draft is silently lost.'],
  'owner_hints': ['designing-file-browser-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.move-conflict-resolution-explicit',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Moving files into a destination with naming conflicts must require an explicit conflict policy',
  'statement': 'A move operation that collides with existing names must not silently overwrite, merge, skip, '
               'or auto-rename unless that behavior is declared and reviewable.',
  'intent': 'Protect file identity and destination contents during organization changes.',
  'applies_when': ['Files or folders can be moved into a location that already contains same-named items.'],
  'does_not_apply_when': [],
  'failure_modes': ['Dragging a file into a folder silently replaces the existing file or appends “copy” '
                    'while the user never chose a policy.'],
  'user_impacts': ['Users can lose destination data or end up with ambiguous duplicates they did not '
                   'intend.'],
  'observables': ['Create collisions for files and folders, move single and multiple items, and inspect '
                  'preview plus resulting destination identities.'],
  'falsifiers': ['The user or explicit product policy determines overwrite, keep-both, merge, or skip, and '
                 'the committed result matches that choice per item.'],
  'repairs': ['Detect destination conflicts before destructive commit and surface per-item resolution for '
              'mixed batches.'],
  'exceptions': [],
  'verification': ['Test concurrent creation of conflicting names during move, verifying stale previews are '
                   'revalidated before final mutation.'],
  'owner_hints': ['designing-file-rename-move-conflicts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.preview-bound-to-current-version',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'File previews must identify the version they render and reconcile when the file changes',
  'statement': 'A preview should not continue looking current after a file is replaced or edited unless the '
               'UI clearly indicates it is showing an older cached revision.',
  'intent': 'Prevent review or approval of stale file content.',
  'applies_when': ['Files can change while a preview pane, thumbnail, or modal remains open.'],
  'does_not_apply_when': [],
  'failure_modes': ['The file is updated elsewhere but the preview retains old bytes with the new filename '
                    'and no stale indication.'],
  'user_impacts': ['Users can approve, share, or act on content that is no longer the current file version.'],
  'observables': ['Open a preview, replace the file version externally, then refresh metadata and compare '
                  'preview revision or digest with current file state.'],
  'falsifiers': ['The preview either updates to the current version or displays the immutable revision it '
                 'still represents and offers refresh.'],
  'repairs': ['Key preview cache and URLs by file revision identity rather than mutable path alone.'],
  'exceptions': [],
  'verification': ['Test replacement, rename, and remote edits, verifying preview and metadata never combine '
                   'different revisions silently.'],
  'owner_hints': ['designing-file-preview-surfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.hidden-item-state-visible-when-enabled',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Hidden-file display mode must remain visibly active while hidden items are shown',
  'statement': 'If users enable normally hidden files, the browser should keep that mode discoverable so '
               'dotfiles, system files, or policy-hidden items are not mistaken for ordinary visible '
               'content.',
  'intent': 'Reduce accidental editing or sharing of files exposed only by a special visibility mode.',
  'applies_when': ['The file browser supports a toggle or preference to reveal hidden items.'],
  'does_not_apply_when': [],
  'failure_modes': ['Hidden items appear after a shortcut but the toggle state is not shown, and later users '
                    'cannot tell why sensitive configuration files are visible.'],
  'user_impacts': ['Users can act on files they would normally never encounter or misread the standard '
                   'directory population.'],
  'observables': ['Toggle hidden-file mode through all supported shortcuts and reopen the directory, '
                  'inspecting mode indicator and persistence.'],
  'falsifiers': ['The visibility mode is apparent whenever it materially changes the collection and its '
                 'persistence follows the declared preference scope.'],
  'repairs': ['Represent hidden-item visibility as explicit browser state and expose it near other '
              'collection controls.'],
  'exceptions': [],
  'verification': ['Test shared devices and workspace switches, verifying the mode does not leak '
                   'unexpectedly across scopes.'],
  'owner_hints': ['designing-file-browser-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.permission-denied-folder-distinct-from-empty',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'A folder the user cannot list must not be rendered as an empty accessible folder',
  'statement': 'File browsers must distinguish authorization failure from a successful directory listing '
               'that contains zero items.',
  'intent': 'Prevent “no files” from concealing a permission boundary or prompting users to create '
            'duplicates elsewhere.',
  'applies_when': ['Directory access can be denied independently of the ability to see the folder name or '
                   'parent hierarchy.'],
  'does_not_apply_when': [],
  'failure_modes': ['Opening a restricted folder shows the same empty-state message as a genuinely empty '
                    'folder.'],
  'user_impacts': ['Users can believe data was deleted or attempt uploads to a location they do not actually '
                   'have permission to inspect.'],
  'observables': ['Compare an empty accessible directory with one that returns list denial under the same '
                  'navigation path.'],
  'falsifiers': ['The restricted state explains the access boundary and disables actions that require '
                 'listing or write authority unless separately permitted.'],
  'repairs': ['Map authorization errors to a distinct directory state instead of coercing denied listings to '
              'empty collections.'],
  'exceptions': [],
  'verification': ['Test read-denied/write-allowed and inherited permission variants, verifying the browser '
                   'never invents an empty dataset.'],
  'owner_hints': ['designing-file-browser-interfaces'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.filebrowser.multi-select-command-scope-visible',
  'domain': 'filebrowser',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'File-browser bulk commands must expose the selected item count and cross-folder scope before '
           'commit',
  'statement': 'When selection spans many files or potentially multiple containers, destructive or sharing '
               'commands must summarize the effective stable identities rather than relying on highlighted '
               'rows alone.',
  'intent': 'Keep bulk file operations reviewable after scrolling, filtering, or selection persistence.',
  'applies_when': ['The browser supports multi-select, hidden/virtualized rows, or selection that can '
                   'persist across navigation.'],
  'does_not_apply_when': [],
  'failure_modes': ['Delete or share shows no selected count and includes items that scrolled out of view or '
                    'remained selected from another folder.'],
  'user_impacts': ['Users can modify or disclose files they no longer realize are part of the selection.'],
  'observables': ['Select items across viewport changes and supported folders, then open each consequential '
                  'bulk command and compare preview with selection state.'],
  'falsifiers': ['The action boundary identifies selection count and scope, and committed targets equal the '
                 'reviewed stable identities.'],
  'repairs': ['Maintain a canonical selection set and require command previews to resolve directly from it '
              'rather than visible row state.'],
  'exceptions': [],
  'verification': ['Test filters, virtualized lists, and navigation, verifying hidden selection is either '
                   'cleared or explicitly included in scope summaries.'],
  'owner_hints': ['designing-bulk-action-toolbars'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-file-browser-owners-v13'],
  'status': 'active'}]

__all__ = ["FILE_BROWSER_RULES_V13"]
