"""V13 seventh-wave independently authored rules for preview publish."""
from __future__ import annotations

from ._capabilities import interaction_caps


PREVIEW_PUBLISH_RULES_V13 = [{'rule_id': 'ui.preview.preview-bound-to-source-revision',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Preview surfaces must identify the exact source revision they render',
  'statement': 'A preview should be tied to an immutable draft, commit, build, or content revision so users '
               'can tell whether it reflects the edits they intend to review.',
  'intent': 'Prevent stale preview content from being mistaken for the latest source.',
  'applies_when': ['Source content can change while rendering or preview generation happens asynchronously.'],
  'does_not_apply_when': [],
  'failure_modes': ['The preview header says Latest while it actually shows an earlier build and gives no '
                    'revision or stale indicator.'],
  'user_impacts': ['Users can approve, publish, or report visual issues against the wrong source version.'],
  'observables': ['Edit source during preview generation and compare source revision, preview artifact '
                  'metadata, and displayed status.'],
  'falsifiers': ['The preview identifies its rendered source revision and becomes stale or regenerates when '
                 'current source advances.'],
  'repairs': ['Propagate source revision identity through the render job and expose it in preview state '
              'rather than inferring freshness from completion time.'],
  'exceptions': [],
  'verification': ['Race source edits and preview builds, verifying every artifact remains attributable to '
                   'one immutable input revision.'],
  'owner_hints': ['designing-render-preview-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.draft-distinct-from-published-state',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Preview and editor surfaces must keep draft state distinct from the currently published release',
  'statement': 'A rendered draft may look production-like, but the interface must state whether users are '
               'viewing unpublished work or the live published version.',
  'intent': 'Prevent preview realism from erasing the publication boundary.',
  'applies_when': ['The product supports drafts, previews, and a separate publish or deploy action.'],
  'does_not_apply_when': [],
  'failure_modes': ['A draft preview uses the production URL chrome and success styling with no indication '
                    'that public users still see an older release.'],
  'user_impacts': ['Authors can tell stakeholders that changes are live or edit the wrong version because '
                   'preview and publication appear identical.'],
  'observables': ['Create unpublished changes, open preview and public routes side by side, and inspect '
                  'status labels plus source revisions.'],
  'falsifiers': ['Draft and published views identify their lifecycle state and current revision '
                 'independently even when visual content is similar.'],
  'repairs': ['Expose environment/release state persistently in preview chrome and bind public status to '
              'deployment authority, not render success.'],
  'exceptions': [],
  'verification': ['Test multiple drafts and environments, verifying no preview can be confused with the '
                   'authoritative published release.'],
  'owner_hints': ['designing-builder-preview-publish-modes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.environment-expiry-visible',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Temporary preview environments must expose expiry and terminal state before links become '
           'unusable',
  'statement': 'When a preview environment is scheduled to expire or can be automatically destroyed, users '
               'should see that lifecycle and know whether a shared link is durable.',
  'intent': 'Avoid sharing ephemeral review links as though they were permanent references.',
  'applies_when': ['Preview deployments have TTLs, branch-lifecycle cleanup, or automatic teardown.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reviewer receives a link that later returns a generic error because the environment '
                    'expired with no prior indication.'],
  'user_impacts': ['Review work and stakeholder communication can be lost or delayed because the preview’s '
                   'lifetime was hidden.'],
  'observables': ['Create previews with short expiry, share them, and inspect lifecycle before, during, and '
                  'after teardown.'],
  'falsifiers': ['The environment exposes authoritative expiry or policy, and an expired link resolves to a '
                 'clear terminal state with an appropriate regeneration path.'],
  'repairs': ['Attach lifecycle metadata to preview artifacts and surface it in both management and review '
              'views.'],
  'exceptions': [],
  'verification': ['Test auto-expiry, manual deletion, and regeneration, verifying old URLs never appear '
                   'indefinitely valid.'],
  'owner_hints': ['designing-preview-environment-lifecycle'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.preview-data-isolation-visible',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Preview environments must disclose when data is synthetic, copied, redacted, or connected to '
           'production',
  'statement': 'A preview’s data source should be understandable where it affects what reviewers can safely '
               'do or how representative the rendered experience is.',
  'intent': 'Prevent destructive testing against production and prevent fake-data previews from being '
            'mistaken for production validation.',
  'applies_when': ['Preview environments may use fixtures, snapshots, anonymized datasets, staging services, '
                   'or production-connected data.'],
  'does_not_apply_when': [],
  'failure_modes': ['The preview looks realistic but gives no indication that actions affect live production '
                    'records, or conversely uses sample data while reviewers believe it proves live '
                    'behavior.'],
  'user_impacts': ['Reviewers can modify real data unexpectedly or overclaim the fidelity of a synthetic '
                   'test.'],
  'observables': ['Open previews under each supported data mode and inspect environment chrome, action '
                  'consequences, and network/backend targets.'],
  'falsifiers': ['The data authority boundary is visible enough for reviewers to understand whether state is '
                 'synthetic, isolated, or production-connected.'],
  'repairs': ['Carry environment data-mode metadata into preview chrome and gate consequential actions '
              'according to the declared isolation policy.'],
  'exceptions': [],
  'verification': ['Test copied snapshots and production-linked services, confirming preview labels and '
                   'action safety match actual backend connections.'],
  'owner_hints': ['designing-preview-environment-lifecycle'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.publish-diff-visible-before-commit',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Publishing must preview the material delta from the currently live release before commit',
  'statement': 'A publish action should show which revision and consequential changes will replace the live '
               'version rather than offering a generic Publish button from an arbitrarily stale editor '
               'state.',
  'intent': 'Give authors a final release-specific review boundary distinct from ordinary draft editing.',
  'applies_when': ['Multiple draft revisions can exist and publication changes what other users see or '
                   'execute.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user publishes from a stale tab without seeing that other draft changes were '
                    'included or that the live release advanced since preview.'],
  'user_impacts': ['Unexpected content or configuration can become public under a confirmation that did not '
                   'describe the actual delta.'],
  'observables': ['Open multiple draft sessions, change live state, then inspect the publish confirmation '
                  'and resulting release revision.'],
  'falsifiers': ['The confirmation binds to the exact candidate and live baseline and exposes material '
                 'difference or a clear route to review it.'],
  'repairs': ['Resolve immutable candidate and baseline revisions at publish time and block or refresh stale '
              'confirmations when either changes.'],
  'exceptions': [],
  'verification': ['Race draft edits and publishing from separate sessions, verifying the committed release '
                   'always matches the reviewed candidate diff.'],
  'owner_hints': ['designing-publishing-controls'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.stale-after-source-change-visible',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Open previews must become visibly stale when their source changes after render',
  'statement': 'A preview that no longer corresponds to the current draft should indicate that gap instead '
               'of remaining indistinguishable from a freshly rendered preview.',
  'intent': 'Prevent reviewers from continuing feedback against obsolete content after authors edit the '
            'source.',
  'applies_when': ['Preview rendering is asynchronous or cached and source edits can happen while a preview '
                   'remains open.'],
  'does_not_apply_when': [],
  'failure_modes': ['The author changes source after rendering, but the preview still says Ready with no '
                    'revision mismatch or refresh prompt.'],
  'user_impacts': ['Feedback and approval can target a version that will never be published.'],
  'observables': ['Open a preview, modify source from another session, and inspect preview state before any '
                  'manual refresh.'],
  'falsifiers': ['The preview either regenerates automatically or indicates that its rendered revision is '
                 'behind current source.'],
  'repairs': ['Track current source revision separately from rendered artifact revision and derive stale '
              'state from their mismatch.'],
  'exceptions': [],
  'verification': ['Exercise rapid source edits and multiple preview tabs, verifying stale state is '
                   'deterministic and clears only after a matching render.'],
  'owner_hints': ['designing-render-preview-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.failed-publish-retains-draft',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Failed publish attempts must retain the candidate draft and explain what became authoritative',
  'statement': 'When publication fails after validation, upload, deployment, or activation begins, the '
               'product must preserve the draft and distinguish partial backend work from the unchanged live '
               'release.',
  'intent': 'Make publication recovery safe without forcing authors to reconstruct work or guessing whether '
            'some users saw it.',
  'applies_when': ['Publishing involves multiple stages that can fail before the new release becomes '
                   'authoritative.'],
  'does_not_apply_when': [],
  'failure_modes': ['A failed publish clears the draft or says Failed without stating whether the live '
                    'release changed, leaving the author unsure what to retry.'],
  'user_impacts': ['Authors can lose work or repeat deployment actions against an uncertain release state.'],
  'observables': ['Fail publish at validation, build, upload, and activation stages, then inspect draft '
                  'availability and public revision.'],
  'falsifiers': ['The draft remains recoverable and the UI identifies whether the authoritative published '
                 'revision changed at all.'],
  'repairs': ['Separate candidate persistence from deployment lifecycle and reconcile final live authority '
              'before presenting outcome.'],
  'exceptions': [],
  'verification': ['Inject failures across stages, verifying retry always begins from a known preserved '
                   'candidate and never assumes activation from partial work.'],
  'owner_hints': ['designing-publishing-controls'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.preview.rollback-target-release-visible',
  'domain': 'preview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Rollback controls must identify the exact release that will become live and the release being '
           'replaced',
  'statement': 'A rollback action should bind to an immutable target release and show enough identity to '
               'distinguish it from neighboring builds or similarly named deployments.',
  'intent': 'Prevent emergency recovery from activating the wrong historical release under pressure.',
  'applies_when': ['The product retains multiple published releases and supports rollback or promotion of an '
                   'older one.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface offers “Rollback to previous” after several rapid deploys without '
                    'identifying which revision previous currently means.'],
  'user_impacts': ['Operators can restore an unintended version and extend an incident.'],
  'observables': ['Create multiple releases, change deployment ordering, then open and execute rollback from '
                  'different clients.'],
  'falsifiers': ['The rollback confirmation names immutable target and current release identities and the '
                 'resulting live state matches that target.'],
  'repairs': ['Resolve rollback target explicitly at action time and reject stale confirmations if current '
              'release changed before commit.'],
  'exceptions': [],
  'verification': ['Race a new deploy with an open rollback dialog, verifying the action cannot silently '
                   'reinterpret “previous” to a different release.'],
  'owner_hints': ['designing-deployment-rollback'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-preview-publish-owners-v13'],
  'status': 'active'}]

__all__ = ["PREVIEW_PUBLISH_RULES_V13"]
