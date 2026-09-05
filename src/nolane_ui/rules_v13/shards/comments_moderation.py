"""V13 comment, thread, mention, and moderation rules with explicit record and authority semantics."""
from __future__ import annotations

from ._capabilities import interaction_caps


COMMENTS_MODERATION_RULES_V13 = [
    {'rule_id': 'ui.comments.retry-does-not-duplicate-comment',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Retrying a comment submission must not create duplicate authored comments',
     'statement': 'If comment creation times out or the response is lost, retry must reconcile against the original '
                  'client operation identity or server result instead of blindly creating another identical comment.',
     'intent': 'Keep ambiguous delivery from turning one user-authored comment into multiple authoritative records.',
     'applies_when': ['A comment composer can retry after network timeout, reconnect, or uncertain creation response.'],
     'does_not_apply_when': [],
     'failure_modes': ['The retry issues a second create with no idempotency or reconciliation and both operations '
                       'appear as separate comments.'],
     'user_impacts': ['Users can spam a thread accidentally and cannot tell whether deleting one copy will remove the '
                      'intended contribution.'],
     'observables': ['Lose the first create response after server acceptance, invoke retry, and compare client operation '
                     'ID with resulting authoritative comment records.'],
     'falsifiers': ['Exactly one comment becomes authoritative for the original submission while retry either resolves '
                    'that record or creates a new record only after explicit new authorship.'],
     'repairs': ['Assign stable client submission identity and reconcile ambiguous responses before enabling a fresh '
                 'create operation.'],
     'exceptions': [],
     'verification': ['Test timeout-before-commit, timeout-after-commit, reconnect, and double-click retry and verify '
                      'one authoritative comment per intentional submission.'],
     'owner_hints': ['designing-comment-systems'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.mention-resolves-stable-identity',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Mentions must bind to stable recipient identity rather than mutable display text',
     'statement': 'A mention inserted from identity search must retain the intended account or entity reference even if '
                  'the recipient later changes display name, duplicate names exist, or the composer rerenders.',
     'intent': 'Keep notification and reference authority attached to the selected person rather than to ambiguous '
               'rendered text.',
     'applies_when': ['Comments support @mentions or references that can notify or link to identities with non-unique or '
                      'mutable display names.'],
     'does_not_apply_when': [],
     'failure_modes': ['The stored mention is resolved again from visible text at submit or render time and can target a '
                       'different account with the same or changed name.'],
     'user_impacts': ['Notifications can go to the wrong person and historical comments can silently change who they '
                      'appear to reference.'],
     'observables': ['Create mentions for duplicate names, rename identities before submit and after submit, then '
                     'compare stored identity IDs, rendered labels, and notification recipients.'],
     'falsifiers': ['The underlying mention identity remains stable while display text can update according to product '
                    'policy without retargeting the reference.'],
     'repairs': ['Serialize stable identity references in comment content or metadata and render the current display '
                 'label from that reference.'],
     'exceptions': [],
     'verification': ['Test duplicate names, renames, deactivated accounts, and composer reloads and verify the mention '
                      'target never changes without an explicit edit.'],
     'owner_hints': ['designing-mentions-and-references'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.edited-state-visible-after-change',
     'domain': 'comments',
     'class': 'contextual',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Materially edited comments should expose that the published content changed',
     'statement': 'When a product permits editing already-published comments, a material text or attachment change '
                  'should be distinguishable from the original publication state so readers are not shown revised '
                  'content as if it were unchanged history.',
     'intent': 'Preserve conversational trust and reviewability without requiring the product to expose a full public '
               'edit history when that is not its policy.',
     'applies_when': ['Published comments can be edited after other participants may have read, replied to, moderated, '
                      'or acted on them.'],
     'does_not_apply_when': [],
     'failure_modes': ['A comment changes materially with no edited indicator or state while replies and moderation '
                       'context continue to imply the original text.'],
     'user_impacts': ['Readers can misinterpret old replies or moderation decisions because the visible content no '
                      'longer matches what participants originally saw.'],
     'observables': ['Publish, reply to, and then materially edit comments and inspect edited state, timestamps, '
                     'moderation metadata, and rendered thread context.'],
     'falsifiers': ['Material changes expose an edited state or equivalent product-defined signal, while trivial '
                    'rendering normalization is not falsely presented as a substantive edit.'],
     'repairs': ['Record edit metadata at authoritative update time and surface a bounded edited indicator consistent '
                 'with the product retention policy.'],
     'exceptions': [],
     'verification': ['Test text, attachment, mention, whitespace-only, and moderator edits and verify edited state '
                      "follows the product's defined material-change boundary."],
     'owner_hints': ['designing-comment-systems'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.deleted-parent-preserves-thread-context',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Deleting a parent comment must not orphan surviving replies without context',
     'statement': 'If replies remain visible after a parent comment is deleted or removed, the thread must preserve '
                  'enough structural context to show that a parent existed rather than promoting child replies into an '
                  'unrelated top-level conversation.',
     'intent': 'Keep thread meaning and reply relationships intact when retention policy removes the content of an '
               'ancestor.',
     'applies_when': ['Threaded conversations can delete, redact, hide, or moderate parent comments while retaining '
                      'descendant replies.'],
     'does_not_apply_when': [],
     'failure_modes': ['Removal of the parent collapses its node completely and descendants render as top-level comments '
                       'or attach to the wrong ancestor.'],
     'user_impacts': ['Readers lose who or what replies were responding to and moderation or discussion chronology '
                      'becomes misleading.'],
     'observables': ['Create nested replies, delete parents at several depths, and inspect parent identifiers, '
                     'indentation, placeholders, permalink behavior, and thread ordering.'],
     'falsifiers': ['Descendants retain their logical ancestry through a tombstone, placeholder, or equivalent '
                    'structural record consistent with product policy.'],
     'repairs': ['Preserve thread nodes separately from retained content so content deletion does not rewrite reply '
                 'topology unless the product explicitly restructures the thread.'],
     'exceptions': [],
     'verification': ['Test user deletion, moderator removal, retention purge, and restored content and verify '
                      'descendant relationships remain logically stable.'],
     'owner_hints': ['designing-threaded-conversations'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.moderation-action-scope-visible',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Moderation actions must expose whether they affect one comment, a thread, an author, or future content',
     'statement': 'Before a moderator commits a consequential action, the surface must make the action scope explicit '
                  'when the same control could hide one item, remove an entire thread, restrict an author, or apply a '
                  'broader policy effect.',
     'intent': 'Prevent moderation language from concealing multiplicative authority behind a generic Remove, Hide, or '
               'Restrict action.',
     'applies_when': ['A moderation tool offers actions whose effects can extend beyond the currently visible comment or '
                      'report.'],
     'does_not_apply_when': [],
     'failure_modes': ['The confirmation describes only the selected comment even though the authoritative operation '
                       'affects descendants, the author account, future posts, or a larger content set.'],
     'user_impacts': ['Moderators can apply significantly broader sanctions than intended and may not be able to '
                      'reconstruct the affected scope afterward.'],
     'observables': ['Inspect each moderation operation with nested threads and repeated-author content, then compare '
                     'confirmation scope with the server mutation and audit record.'],
     'falsifiers': ['The pre-commit UI names the actual target set and authority level, including broader account or '
                    'future-content effects where they exist.'],
     'repairs': ['Derive confirmation copy and target count from the same moderation command object sent to authority '
                 'rather than from the selected row label.'],
     'exceptions': [],
     'verification': ['Test item, thread, author, batch, and policy actions and verify confirmation, result, and audit '
                      'scope remain identical.'],
     'owner_hints': ['designing-moderation-action-surfaces'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.moderation-reversal-restores-prior-state',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Reversing a moderation action must restore the correct prior visibility state',
     'statement': 'When a moderation decision is reversible, undo or appeal acceptance must restore the content and '
                  'related thread state that existed before that specific moderation action rather than applying a '
                  'generic visible state that ignores earlier restrictions.',
     'intent': 'Make moderation reversal a state transition against recorded history instead of an unconditional '
               'show-content toggle.',
     'applies_when': ['The product supports undoing, reversing, or approving an appeal for hidden, limited, or removed '
                      'content.'],
     'does_not_apply_when': [],
     'failure_modes': ['Reversal always marks the item visible even if it was already muted, age-gated, '
                       'thread-collapsed, or restricted by another still-active moderation rule.'],
     'user_impacts': ['Content can become more visible than it was before moderation or remain incorrectly suppressed '
                      'after a successful reversal.'],
     'observables': ['Apply layered moderation states, reverse them in different orders, and compare resulting '
                     'visibility and authority with the pre-action state snapshots.'],
     'falsifiers': ['Each reversal removes only the effect of the targeted moderation decision and preserves independent '
                    'restrictions or prior visibility settings.'],
     'repairs': ['Record moderation effects as separately reversible state transitions and recompute effective '
                 'visibility from the remaining active decisions.'],
     'exceptions': [],
     'verification': ['Test stacked hide, restrict, lock, and appeal outcomes and verify reversal order does not erase '
                      'unrelated moderation state.'],
     'owner_hints': ['designing-moderation-action-surfaces'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.hidden-state-distinct-from-deleted',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Hidden comments must remain distinct from deleted comments in user and moderator state',
     'statement': 'A comment hidden from a viewer, muted by preference, collapsed by moderation, or suppressed by '
                  'ranking must not be represented as deleted when the authoritative record still exists and can '
                  'reappear under another visibility context.',
     'intent': 'Preserve the distinction between record lifecycle and presentation visibility so recovery and moderation '
               'actions remain truthful.',
     'applies_when': ['The product has visibility states that can remove a comment from a particular view without '
                      'deleting the underlying comment record.'],
     'does_not_apply_when': [],
     'failure_modes': ['The UI labels or treats a hidden comment as deleted, removing recovery controls or implying the '
                       'author removed content that still exists.'],
     'user_impacts': ['Users and moderators can misunderstand retention, believe a record is gone, or take redundant '
                      'deletion actions against still-existing content.'],
     'observables': ['Hide comments through viewer preference, moderation, and ranking paths and compare record '
                     'existence, permalink behavior, restore controls, and user-facing labels.'],
     'falsifiers': ["Hidden or suppressed states remain distinguishable from deletion according to the viewer's "
                    'authority and product disclosure policy.'],
     'repairs': ['Model visibility and lifecycle separately and map each state to its permitted disclosure and recovery '
                 'controls instead of collapsing them into one absence state.'],
     'exceptions': [],
     'verification': ['Test hide, mute, collapse, moderation suppress, user delete, hard delete, and restoration and '
                      'verify each transition preserves the correct lifecycle meaning.'],
     'owner_hints': ['designing-comment-systems'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.comments.unread-marker-survives-thread-reorder',
     'domain': 'comments',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Unread thread position must survive comment reordering and late-arriving replies',
     'statement': 'An unread marker should be anchored to message or event identity rather than a fragile visual index '
                  'so sorting, moderation, insertion of late replies, or thread expansion does not move the marker onto '
                  'already-read or unrelated content.',
     'intent': 'Keep read continuity stable when conversation structure changes after the user leaves and returns.',
     'applies_when': ['Threads track unread position while comments can reorder because of chronology correction, '
                      'moderation, threading, late sync, or ranking.'],
     'does_not_apply_when': [],
     'failure_modes': ['The unread divider is stored as a row index or current array position and shifts when comments '
                       'are inserted or reordered.'],
     'user_impacts': ['Users can skip unseen replies or repeatedly revisit already-read content because the read '
                      'boundary no longer maps to the same events.'],
     'observables': ['Mark a thread partially read, inject and reorder replies around the boundary, then reopen and '
                     'compare unread identities with the stored read watermark.'],
     'falsifiers': ['The unread boundary is derived from stable event identity or authoritative read state and remains '
                    'correct after structural changes.'],
     'repairs': ['Persist read watermarks by event or monotonic thread sequence appropriate to the product rather than '
                 'by rendered list offset.'],
     'exceptions': [],
     'verification': ['Test late delivery, moderation removal, restored comments, nested expansion, and sort changes and '
                      'verify unread state tracks the intended events.'],
     'owner_hints': ['designing-threaded-conversations'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-comments-moderation-owners-v13'],
     'status': 'active'},
]

__all__ = ['COMMENTS_MODERATION_RULES_V13']
