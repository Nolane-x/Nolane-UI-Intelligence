"""V13 seventh-wave independently authored rules for sharing access."""
from __future__ import annotations

from ._capabilities import interaction_caps


SHARING_ACCESS_RULES_V13 = [{'rule_id': 'ui.sharing.link-scope-visible-before-copy',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Share-link scope must be visible before the link is copied or sent',
  'statement': 'A share-link control must expose the effective audience, resource, and permission scope '
               'before producing a link that the user can distribute.',
  'intent': 'Prevent users from treating a convenient copy action as harmless when the generated link may '
            'grant broader access than the current screen implies.',
  'applies_when': ['The product can create links with different audience or permission scopes for the same '
                   'resource.'],
  'does_not_apply_when': [],
  'failure_modes': ['The primary copy action generates a link using remembered or default scope while the '
                    'actual audience and capabilities are hidden behind a secondary settings surface.'],
  'user_impacts': ['Sensitive material can be exposed to the wrong group before the sender notices that the '
                   'link was public, organization-wide, or editable.'],
  'observables': ['Switch among sharing presets, reopen the dialog, and inspect the state immediately before '
                  'invoking copy or send.'],
  'falsifiers': ['The effective audience and permission are visible at the action boundary and the generated '
                 'token encodes the same scope.'],
  'repairs': ['Move effective share scope into the primary confirmation state and bind token generation to '
              'the displayed canonical sharing model.'],
  'exceptions': [],
  'verification': ['Generate links under every audience/permission combination and verify recipient access '
                   'exactly matches what the sender saw before copy.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.expiration-effective-state-visible',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Expiring shares must show the effective expiration time and time-zone basis',
  'statement': 'A time-limited share must expose when access will stop in an unambiguous time basis and must '
               'distinguish configured expiry from server-effective expiry.',
  'intent': 'Let senders and recipients reason about access windows without relying on ambiguous local dates '
            'or stale client countdowns.',
  'applies_when': ['Share links, invitations, or file grants can expire at a configured time.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI says “expires tomorrow” or shows a local clock time that maps differently for '
                    'sender and recipient, while the server enforces another instant.'],
  'user_impacts': ['Recipients can lose access earlier than expected or sensitive access can persist longer '
                   'than the sender intended.'],
  'observables': ['Configure expiry near a time-zone or daylight-saving boundary and inspect the sender, '
                  'recipient, and post-refresh representations.'],
  'falsifiers': ['All surfaces resolve to the same authoritative expiry instant and disclose enough zone or '
                 'relative context to avoid ambiguity.'],
  'repairs': ['Store expiry as an authoritative instant or explicitly zone-bound local time and derive all '
              'countdowns and labels from that value.'],
  'exceptions': [],
  'verification': ['Test sender and recipient in different zones plus expired/reopened states, verifying '
                   'enforcement and displayed expiry remain aligned.'],
  'owner_hints': ['designing-file-sharing-expiration'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.revoked-link-not-presented-active',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Revoked share links must stop appearing active after authority is removed',
  'statement': 'A link that has been revoked or whose grant was removed must reconcile to a revoked state '
               'across management, copy, recipient, and activity surfaces instead of remaining visually '
               'reusable.',
  'intent': 'Prevent stale management UI from encouraging redistribution of an access token that no longer '
            'carries authority.',
  'applies_when': ['Users can revoke a share link while it may still be open in other tabs, devices, or '
                   'recipient sessions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A stale share dialog still labels the old link active and offers copy even though '
                    'recipients now receive denial, or the reverse after delayed revocation.'],
  'user_impacts': ['Senders cannot tell whether access is actually disabled and may communicate unusable or '
                   'unexpectedly still-active links.'],
  'observables': ['Open the same share on multiple clients, revoke from one, then copy, open, and inspect '
                  'the link from the others.'],
  'falsifiers': ['All clients reconcile to the authoritative revocation state and no stale surface '
                 'represents a revoked token as currently granting access.'],
  'repairs': ['Invalidate share grants server-side and refresh or push their status to management and '
              'recipient clients; keep historical metadata separate from active capability.'],
  'exceptions': [],
  'verification': ['Revoke links under network delay and cross-device use, verifying management state and '
                   'recipient authorization converge without false active labels.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.audience-preview-resolves-groups',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Share audience previews must resolve group membership enough to expose effective reach',
  'statement': 'When a share targets teams, groups, domains, or organization-wide audiences, the preview '
               'must communicate the effective reach rather than displaying only an opaque group label.',
  'intent': 'Help users catch unexpectedly large or nested audiences before creating consequential access '
            'grants.',
  'applies_when': ['Sharing can target dynamic groups, nested teams, domains, or organization-level '
                   'principals.'],
  'does_not_apply_when': [],
  'failure_modes': ['The dialog says “Design Team” but gives no indication that the group includes external '
                    'members, nested teams, or hundreds of users under current membership.'],
  'user_impacts': ['A sender can grant access far beyond the people they intended because the audience label '
                   'hides meaningful expansion.'],
  'observables': ['Create groups with nested and external membership, select them as share audiences, and '
                  'inspect the pre-commit audience representation.'],
  'falsifiers': ['The preview communicates meaningful membership scale and exceptional reach such as '
                 'external or nested audiences without requiring exposure of unauthorized member details.'],
  'repairs': ['Resolve effective audience characteristics from the current directory and surface '
              'risk-relevant expansion before grant creation.'],
  'exceptions': [],
  'verification': ['Vary group membership after opening the dialog and verify commit-time preview or '
                   'revalidation reflects the current effective audience.'],
  'owner_hints': ['designing-sharing-dialogs'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.public-vs-organization-boundary-explicit',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Public and organization-restricted sharing must be visually and semantically distinct',
  'statement': 'A share surface must not present “anyone in the organization” and “anyone with the link” as '
               'minor variants when they cross materially different trust boundaries.',
  'intent': 'Reduce accidental public exposure by making the audience boundary understandable before users '
            'act.',
  'applies_when': ['The product supports both organization-restricted and internet-accessible link sharing.'],
  'does_not_apply_when': [],
  'failure_modes': ['Public and organization-only options use ambiguous labels, identical summaries, or '
                    'remembered defaults that obscure which boundary is currently effective.'],
  'user_impacts': ['Users can publish confidential material outside their organization while believing the '
                   'link still requires membership.'],
  'observables': ['Toggle between restricted and public modes, close and reopen the dialog, and inspect '
                  'summary, confirmation, and recipient behavior.'],
  'falsifiers': ['The current boundary is explicit in label and consequence, and recipient tests from '
                 'outside the organization match that state exactly.'],
  'repairs': ['Use distinct audience terminology and confirmation language for cross-trust-boundary changes, '
              'backed by commit-time scope validation.'],
  'exceptions': [],
  'verification': ['Exercise default changes and cross-organization recipients to verify no surface '
                   'collapses public and organization-only authority into the same appearance.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.download-permission-distinct-from-view',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'View access and download permission must remain distinct when the product enforces both',
  'statement': 'If a sharing model can allow viewing while restricting download or export, the interface '
               'must represent those as separate capabilities and recipient behavior must honor the '
               'distinction.',
  'intent': 'Avoid implying that “viewer” necessarily grants or denies every form of file extraction when '
            'the product has finer authority.',
  'applies_when': ['Shared content exposes a policy that differentiates viewing from downloading, exporting, '
                   'or saving originals.'],
  'does_not_apply_when': [],
  'failure_modes': ['The sender sees only a generic Viewer role while a hidden toggle changes download '
                    'capability, or recipient controls disagree with the configured policy.'],
  'user_impacts': ['Sensitive originals may be copied despite a sender’s restriction, or legitimate '
                   'recipients may be blocked without an understandable reason.'],
  'observables': ['Create shares with all supported view/download combinations and inspect sender summary '
                  'plus recipient controls and network-authoritative outcomes.'],
  'falsifiers': ['The sharing summary states the effective download capability and recipient surfaces '
                 'enforce and explain the same policy.'],
  'repairs': ['Model view and download as explicit capabilities, bind them to the grant, and surface the '
              'effective combination before sharing.'],
  'exceptions': [],
  'verification': ['Test recipient attempts through direct buttons, keyboard commands, deep links, and '
                   'refresh to verify no UI path contradicts the configured grant.'],
  'owner_hints': ['designing-sharing-dialogs'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.reshare-inheritance-visible',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Reshare capability must reveal whether recipients can extend access and under what boundary',
  'statement': 'When recipients can invite others, create derivative links, or otherwise extend access, the '
               'original sharing surface must expose that capability and its scope.',
  'intent': 'Make second-order access expansion visible to the sender rather than treating it as an '
            'unrelated recipient action.',
  'applies_when': ['The sharing policy allows some recipients to reshare, invite, or create links derived '
                   'from the original grant.'],
  'does_not_apply_when': [],
  'failure_modes': ['A sender grants access without seeing that the recipient role can further distribute '
                    'it, or later management cannot distinguish direct from reshared access.'],
  'user_impacts': ['Access can spread beyond the sender’s intended audience with no clear explanation of how '
                   'the new principals obtained authority.'],
  'observables': ['Grant a reshare-capable role, have the recipient extend access, and inspect original '
                  'share summary, recipient controls, and access history.'],
  'falsifiers': ['The sender can see whether resharing is allowed and later access records identify '
                 'reshare-derived authority distinctly from direct grants.'],
  'repairs': ['Represent reshare as an explicit capability on the grant and preserve provenance when '
              'downstream grants are created.'],
  'exceptions': [],
  'verification': ['Exercise nested reshares and revocation of the source grant, verifying effective access '
                   'and provenance are explained consistently.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.sharing.native-handoff-result-reconciled',
  'domain': 'sharing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Native share handoff must not be represented as delivered before the operating system result is '
           'known',
  'statement': 'When content is passed to a native share sheet or external target, the product must '
               'distinguish initiating the handoff from successful delivery or publication by the chosen '
               'destination.',
  'intent': 'Prevent false success when the app can only know that the operating-system share flow was '
            'invoked, cancelled, or returned a limited result.',
  'applies_when': ['A web or native product invokes an operating-system share sheet, intent, or external '
                   'application it does not fully control.'],
  'does_not_apply_when': [],
  'failure_modes': ['The source app shows “Shared successfully” immediately on opening the share sheet even '
                    'if the user cancels or the destination fails later.'],
  'user_impacts': ['Users can believe sensitive or important information reached a recipient when the source '
                   'product has no evidence that it did.'],
  'observables': ['Open the share sheet, cancel, choose multiple target apps, and observe what result '
                  'signals the platform actually returns to the source.'],
  'falsifiers': ['The product labels only the state it can observe, such as “share sheet opened” or “handoff '
                 'completed,” and does not claim recipient delivery without evidence.'],
  'repairs': ['Map platform callback states to bounded source-app language and keep downstream delivery '
              'claims within the external target’s observable contract.'],
  'exceptions': [],
  'verification': ['Test cancellation and destinations with different callback capabilities, confirming the '
                   'source never upgrades initiation into unsupported delivery success.'],
  'owner_hints': ['designing-native-share-sheet-intents'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-sharing-owners-v13'],
  'status': 'active'}]

__all__ = ["SHARING_ACCESS_RULES_V13"]
