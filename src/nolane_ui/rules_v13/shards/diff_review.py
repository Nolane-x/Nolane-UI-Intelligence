"""V13 seventh-wave independently authored rules for diff review."""
from __future__ import annotations

from ._capabilities import interaction_caps


DIFF_REVIEW_RULES_V13 = [{'rule_id': 'ui.diff.baseline-and-head-identities-visible',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Diff views must expose the exact baseline and head identities being compared',
  'statement': 'A review diff must identify the immutable source and destination revisions, environments, '
               'artifacts, or graph snapshots instead of relying on ambiguous labels such as “current” and '
               '“latest.”',
  'intent': 'Make review conclusions reproducible even when the underlying branch, environment, or document '
            'continues changing.',
  'applies_when': ['The compared resources can receive new revisions while a diff is open or can have '
                   'similarly named versions.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI says “main → current” while new commits arrive and the rendered difference '
                    'silently changes without a stable baseline identity.'],
  'user_impacts': ['Reviewers can approve a change set that is different from the one they originally '
                   'inspected.'],
  'observables': ['Open a diff, mutate the moving reference, refresh and deep-link the view, then compare '
                  'displayed and requested revision identifiers.'],
  'falsifiers': ['Both endpoints resolve to stable immutable identities for the reviewed session or the UI '
                 'explicitly signals that the comparison has advanced.'],
  'repairs': ['Resolve moving refs to immutable revision IDs when the review begins and display those '
              'endpoints in the diff contract.'],
  'exceptions': [],
  'verification': ['Test branch updates, environment redeploys, and document edits while a diff remains '
                   'open, verifying reviewed endpoints never shift silently.'],
  'owner_hints': ['designing-diff-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.moved-content-not-double-counted',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Moved content must not be presented as unrelated deletion and addition when move semantics are '
           'known',
  'statement': 'When the product can establish that content was moved or renamed without substantive change, '
               'the diff should preserve that relationship or clearly state that move detection is '
               'unavailable.',
  'intent': 'Reduce false change volume that hides the material edits reviewers need to inspect.',
  'applies_when': ['The compared model has stable identity or a reliable move/rename relationship for files, '
                   'nodes, sections, or records.'],
  'does_not_apply_when': [],
  'failure_modes': ['A pure move appears as a full deletion plus full addition, inflating change counts and '
                    'obscuring the small actual edits that happened inside the moved content.'],
  'user_impacts': ['Reviewers can miss consequential modifications because a large amount of mechanical '
                   'relocation noise dominates the review.'],
  'observables': ['Move an unchanged item, then move and edit it, and compare change counts and navigation '
                  'with stable resource identity.'],
  'falsifiers': ['Unchanged moves are represented as moves or excluded from material-change counts, while '
                 'real edits inside moved content remain reviewable.'],
  'repairs': ['Use stable identity or explicit rename/move metadata for diff alignment and keep fallback '
              'behavior labeled when identity is unavailable.'],
  'exceptions': [],
  'verification': ['Exercise moves across directories or containers with and without edits, verifying '
                   'material change counts correspond to substantive changes rather than path churn.'],
  'owner_hints': ['designing-diff-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.whitespace-normalization-declared',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Whitespace or formatting normalization in a diff must be explicit and reversible',
  'statement': 'If a diff suppresses whitespace, formatting, case, or generated noise, the active '
               'normalization mode must be visible and users must be able to inspect the raw difference when '
               'that detail could matter.',
  'intent': 'Prevent filters intended to reduce noise from concealing a meaningful formatting or syntax '
            'change.',
  'applies_when': ['The diff viewer offers ignore-whitespace or equivalent normalization modes or applies '
                   'them by default.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI hides whitespace changes without indicating the active mode, causing a '
                    'formatting-sensitive change to disappear from review.'],
  'user_impacts': ['Reviewers may approve code, data, or content whose semantics depend on supposedly '
                   'ignorable formatting differences.'],
  'observables': ['Create changes that are cosmetic in one file type and semantic in another, then toggle or '
                  'reload the diff normalization state.'],
  'falsifiers': ['The active normalization is labeled, persists predictably, and raw differences remain '
                 'accessible without losing review context.'],
  'repairs': ['Treat normalization as explicit diff configuration and preserve a raw comparison path for '
              'formats where whitespace can be meaningful.'],
  'exceptions': [],
  'verification': ['Verify deep links, saved preferences, and review comments maintain the declared '
                   'normalization mode and do not silently reinterpret old comments.'],
  'owner_hints': ['designing-diff-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.collapsed-sections-still-count-changes',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Collapsed diff regions must continue to disclose hidden change counts and unresolved review work',
  'statement': 'Folding unchanged or low-interest regions must not make hidden modifications or unresolved '
               'comments disappear from the review summary.',
  'intent': 'Preserve review completeness while allowing large differences to remain navigable.',
  'applies_when': ['The diff UI collapses files, hunks, nodes, or generated sections while computing totals '
                   'and review status.'],
  'does_not_apply_when': [],
  'failure_modes': ['A collapsed file contains changes or unresolved comments but the visible summary looks '
                    'clean and next-change navigation skips the hidden work.'],
  'user_impacts': ['Reviewers can finish or approve a review without realizing material differences remain '
                   'behind collapsed containers.'],
  'observables': ['Collapse changed regions with comments and search hits, then inspect totals, file status, '
                  'and next/previous navigation.'],
  'falsifiers': ['Collapsed containers retain badges or counts for hidden changes and unresolved work, and '
                 'navigation can still reach them.'],
  'repairs': ['Compute review status independently of visual expansion and surface hidden-work indicators on '
              'collapsed parents.'],
  'exceptions': [],
  'verification': ['Exercise nested collapse and bulk-collapse actions, verifying approval readiness never '
                   'depends on whether a changed region happens to be expanded.'],
  'owner_hints': ['designing-diff-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.binary-unrenderable-change-disclosed',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Unrenderable or binary changes must remain visible as review obligations',
  'statement': 'When a changed artifact cannot be rendered as an inline textual or visual diff, the review '
               'must still disclose that it changed and provide available metadata, preview, or download '
               'paths.',
  'intent': 'Prevent review surfaces from appearing complete when unsupported file types contain uninspected '
            'changes.',
  'applies_when': ['A reviewed change set can include binary, encrypted, oversized, proprietary, or '
                   'otherwise unsupported artifacts.'],
  'does_not_apply_when': [],
  'failure_modes': ['Unsupported files vanish from the diff or are counted only in a total with no path, '
                    'size, hash, or reason they cannot be rendered.'],
  'user_impacts': ['Reviewers may approve altered executables, media, models, or sensitive artifacts without '
                   'noticing they were part of the change set.'],
  'observables': ['Add supported and unsupported artifacts to one review and compare file inventory, totals, '
                  'and navigation.'],
  'falsifiers': ['Every changed artifact remains enumerated with stable identity and an explicit rendering '
                 'limitation plus the strongest safe inspection path available.'],
  'repairs': ['Separate change inventory from renderer capability and surface metadata or artifact access '
              'when inline comparison is unsupported.'],
  'exceptions': [],
  'verification': ['Test several unsupported types and size thresholds, confirming none disappear from '
                   'counts, filters, or review completion logic.'],
  'owner_hints': ['designing-diff-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.hunk-context-stable-across-navigation',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Diff hunk anchors must remain attached to the same change when context expands or collapses',
  'statement': 'Comments, selections, and next-change navigation should resolve to stable change identity '
               'rather than brittle line positions that drift when context or neighboring hunks are '
               'expanded.',
  'intent': 'Keep review discussion anchored to the intended modification as the viewer changes '
            'presentation.',
  'applies_when': ['A diff viewer supports expandable context, folded lines, inline comments, or dynamic '
                   'hunk grouping.'],
  'does_not_apply_when': [],
  'failure_modes': ['Expanding context renumbers positions and a comment or copied link jumps to a nearby '
                    'but different line or change.'],
  'user_impacts': ['Reviewers can discuss or approve the wrong code or content because references silently '
                   'retarget.'],
  'observables': ['Place comments on adjacent hunks, expand context and change folding, then follow comment '
                  'and deep-link anchors.'],
  'falsifiers': ['Anchors continue resolving to the same logical change or explicitly report that the target '
                 'no longer exists after a new revision.'],
  'repairs': ['Use stable diff-side identity plus revision and content anchors rather than presentation-only '
              'line indexes.'],
  'exceptions': [],
  'verification': ['Exercise context expansion, file moves, and refreshed diff revisions, verifying anchors '
                   'either stay correct or become explicitly stale.'],
  'owner_hints': ['designing-diff-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.review-stale-after-base-update',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Review state must become stale when the compared base or head changes materially',
  'statement': 'An approval, viewed marker, or “all changes reviewed” state must not carry forward silently '
               'after the underlying compared revision advances beyond what the reviewer inspected.',
  'intent': 'Bind review completion to actual reviewed content rather than to a mutable branch or artifact '
            'name.',
  'applies_when': ['A review can update because new commits, environment deploys, graph edits, or document '
                   'revisions enter the comparison after review begins.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface keeps prior approval and reviewed-file marks even though new or changed '
                    'differences have appeared since that decision.'],
  'user_impacts': ['Unreviewed changes can inherit a misleading approval state and enter release or '
                   'publication.'],
  'observables': ['Complete a review, then update the base and head with new and modified changes and '
                  'observe review markers and gate status.'],
  'falsifiers': ['The system identifies which review evidence is still applicable and marks newly changed or '
                 'invalidated scope as requiring review again.'],
  'repairs': ['Attach review evidence to immutable comparison revisions and compute invalidation from '
              'content or policy-relevant delta.'],
  'exceptions': [],
  'verification': ['Add commits before and after approval, including edits to previously reviewed files, and '
                   'verify release gates respond to stale evidence.'],
  'owner_hints': ['designing-design-code-drift-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.diff.applied-change-result-reconciled',
  'domain': 'diff',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Applying a selected diff or patch must reconcile the actual committed result back into the '
           'review',
  'statement': 'After users accept, apply, cherry-pick, or promote selected changes, the UI must verify what '
               'became authoritative and must not treat the requested patch as equivalent to the committed '
               'result when conflicts or transformations occur.',
  'intent': 'Close the loop between review intent and the actual artifact produced by an apply operation.',
  'applies_when': ['The product can apply reviewed changes into another document, environment, branch, '
                   'graph, or configuration.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI marks selected differences applied even though some hunks conflicted, were '
                    'transformed, or targeted a newer destination state.'],
  'user_impacts': ['Users can believe reviewed state was promoted while the destination contains only a '
                   'subset or a materially altered merge result.'],
  'observables': ['Apply a patch into matching and divergent destinations, then compare requested hunks, '
                  'operation result, and final destination revision.'],
  'falsifiers': ['The UI distinguishes successful, conflicted, skipped, and transformed changes and links '
                 'the result to the final authoritative revision.'],
  'repairs': ['Capture per-change apply outcomes and re-diff the committed destination when necessary '
              'instead of inferring success from request submission.'],
  'exceptions': [],
  'verification': ['Force conflicts and partial application, then verify review status and downstream '
                   'promotion use the actual resulting revision rather than the intended patch.'],
  'owner_hints': ['designing-patch-exposure-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-diff-review-owners-v13'],
  'status': 'active'}]

__all__ = ["DIFF_REVIEW_RULES_V13"]
