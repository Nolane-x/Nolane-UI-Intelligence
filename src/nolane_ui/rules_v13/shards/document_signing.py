"""V13 seventh-wave independently authored rules for document signing."""
from __future__ import annotations

from ._capabilities import interaction_caps


DOCUMENT_SIGNING_RULES_V13 = [{'rule_id': 'ui.signing.signer-identity-and-document-version-visible',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Signing surfaces must bind signer identity to the exact document version being signed',
  'statement': 'Before signature commit, the interface must identify both the acting signer and immutable '
               'document revision so a stale tab cannot sign a replaced document under an old preview.',
  'intent': 'Make the legal or operational act traceable to the content actually reviewed.',
  'applies_when': ['A document can be revised or regenerated while a signing invitation or session remains '
                   'open.'],
  'does_not_apply_when': [],
  'failure_modes': ['The signer reviews version A, the sender replaces content with version B, and the '
                    'existing Sign button authorizes the newer document without an updated review.'],
  'user_impacts': ['A signature can be attached to terms the signer never saw.'],
  'observables': ['Open a signing session, replace or revise the document elsewhere, then attempt to sign '
                  'without refreshing.'],
  'falsifiers': ['Signature commit is bound to the reviewed immutable revision and stale sessions require '
                 'explicit review of any replacement.'],
  'repairs': ['Include document revision identity in signing challenges and reject commits against '
              'superseded content.'],
  'exceptions': [],
  'verification': ['Modify the document at several points in the signing flow and verify no signature can '
                   'transfer silently to a different revision.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.required-signature-fields-complete-before-submit',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Signing submission must verify every required signature and acknowledgement field in scope',
  'statement': 'The final signing action should be blocked until all required fields for the current signer '
               'are complete, with unresolved fields discoverable without hunting through pages.',
  'intent': 'Prevent apparently completed signatures that are rejected later because hidden mandatory fields '
            'were missed.',
  'applies_when': ['A document contains multiple signer-specific required signatures, initials, '
                   'acknowledgements, or data fields.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user can submit with an off-screen required field missing, receiving a generic '
                    'error or incomplete document later.'],
  'user_impacts': ['Signers may believe the process finished while the document remains invalid or pending.'],
  'observables': ['Create required fields across distant pages and conditional sections, then attempt submit '
                  'with different omissions.'],
  'falsifiers': ['Submission readiness reflects the authoritative required-field set and navigation '
                 'identifies every unresolved field.'],
  'repairs': ['Compute completeness from field schema and signer role, surfacing a summary and direct '
              'navigation before commit.'],
  'exceptions': [],
  'verification': ['Test conditional required fields and page reordering, confirming the final gate never '
                   'ignores or invents signer obligations.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.signing-order-and-next-signer-visible',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Sequential signing workflows must expose current signer order and who is waiting next',
  'statement': 'When signatures are required in sequence, participants should be able to distinguish '
               'completed, active, and not-yet-eligible signers without implying that invitations are '
               'simultaneously actionable.',
  'intent': 'Clarify workflow progress and prevent premature or duplicate outreach.',
  'applies_when': ['A document requires signers in a defined sequential or conditional order.'],
  'does_not_apply_when': [],
  'failure_modes': ['All signers appear simply “pending,” so the sender cannot tell whether the next person '
                    'is blocked by an earlier signature or never received an invitation.'],
  'user_impacts': ['Teams may resend, escalate, or troubleshoot the wrong participant and misinterpret '
                   'document status.'],
  'observables': ['Create a three-stage signing order and inspect sender plus signer views before and after '
                  'each completion.'],
  'falsifiers': ['The current eligible signer and future blocked stages are distinguishable and follow the '
                 'authoritative workflow order.'],
  'repairs': ['Render signing stages from the signing engine state and label invitations according to '
              'eligibility rather than generic pending status.'],
  'exceptions': [],
  'verification': ['Complete and decline stages in different sequences, verifying next-signer state changes '
                   'exactly with policy.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.decline-state-finality-visible',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Declining to sign must expose whether the workflow ends, returns for revision, or continues for '
           'others',
  'statement': 'A decline action should explain its effective consequence before commit and the resulting '
               'document state must remain visible to all participants.',
  'intent': 'Prevent a signer from assuming decline is a private note when it terminates or alters the '
            'entire workflow.',
  'applies_when': ['The signing system supports signer decline or refusal and has a policy for downstream '
                   'signers.'],
  'does_not_apply_when': [],
  'failure_modes': ['The button says Decline without indicating that it voids all remaining invitations, or '
                    'the sender sees only “not signed” afterward.'],
  'user_impacts': ['A document process can stop unexpectedly or continue when participants believe it '
                   'ended.'],
  'observables': ['Decline at different stages and inspect sender, declined signer, and later signer states '
                  'plus audit history.'],
  'falsifiers': ['The pre-action consequence matches the authoritative post-decline workflow and the '
                 'reason/state remains attributable.'],
  'repairs': ['Model decline as an explicit workflow transition with policy-dependent consequences and '
              'surface those consequences before confirmation.'],
  'exceptions': [],
  'verification': ['Test first, middle, and final signer decline plus revision-and-resend paths, verifying '
                   'state never collapses to generic pending.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.expired-signing-link-recovery',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Expired signing links must route to a safe recovery path without reviving obsolete authority',
  'statement': 'When a signing invitation expires, opening it should identify the document or request '
               'context safely and provide an authorized route to request a new invitation rather than '
               'reactivating the old token.',
  'intent': 'Help legitimate signers recover without weakening expiry semantics.',
  'applies_when': ['Signing invitations use expiring links or tokens.'],
  'does_not_apply_when': [],
  'failure_modes': ['An expired URL opens a generic error with no context, or clicking Retry silently '
                    'creates a new valid session from the expired token alone.'],
  'user_impacts': ['Users abandon valid workflows or expired credentials regain authority beyond their '
                   'intended lifetime.'],
  'observables': ['Open expired invitations before and after document revision and test '
                  'resend/request-new-link behavior.'],
  'falsifiers': ['Expired tokens cannot sign, while recovery creates a fresh policy-authorized invitation '
                 'tied to the current document state.'],
  'repairs': ['Separate contextual identification from authentication authority and require a new issuance '
              'path for expired invitations.'],
  'exceptions': [],
  'verification': ['Test copied old links after resend and document replacement, confirming only current '
                   'authorized invitations can reach signing commit.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.document-change-invalidates-prior-signatures',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Material document changes must invalidate or explicitly preserve prior signatures according to '
           'policy',
  'statement': 'If signed content changes after a signature, the system must not continue displaying that '
               'signature as covering modified terms unless the signing model explicitly supports and '
               'evidences that relationship.',
  'intent': 'Prevent signatures from appearing to authorize content that was added or altered later.',
  'applies_when': ['A document may be edited, regenerated, or have fields changed after one or more '
                   'signatures exist.'],
  'does_not_apply_when': [],
  'failure_modes': ['The sender changes a material clause and prior signatures remain shown as valid with no '
                    'indication that they refer to an earlier revision.'],
  'user_impacts': ['Recipients can rely on a document whose visible signatures do not actually cover its '
                   'current content.'],
  'observables': ['Sign a document, alter material and nonmaterial fields under the product policy, then '
                  'inspect signature validity and revision history.'],
  'falsifiers': ['Signature status remains bound to the signed revision and any policy-defined carry-forward '
                 'is explicit and auditable.'],
  'repairs': ['Hash or version-bind signatures to content and recompute workflow validity when the document '
              'changes.'],
  'exceptions': [],
  'verification': ['Test edits before, between, and after signers, verifying signature representation always '
                   'matches the exact covered revision.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.signed-artifact-download-integrity-visible',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Downloaded signed artifacts must expose enough identity to distinguish final signed content from '
           'drafts',
  'statement': 'After completion, download surfaces should identify the final signed revision and not offer '
               'an ambiguous file that can be confused with an unsigned preview or superseded draft.',
  'intent': 'Preserve confidence that the artifact users store is the same one the signing workflow '
            'finalized.',
  'applies_when': ['The product offers multiple document downloads during draft, signing, and completed '
                   'states.'],
  'does_not_apply_when': [],
  'failure_modes': ['All files share the same filename and summary while one is a pre-sign preview and '
                    'another is the executed artifact.'],
  'user_impacts': ['Users can archive, forward, or rely on the wrong document despite the signing flow '
                   'succeeding.'],
  'observables': ['Download at draft, partially signed, and completed stages and compare file identity, '
                  'revision metadata, signatures, and labels.'],
  'falsifiers': ['The final artifact is clearly identified and corresponds to the completed signed revision; '
                 'intermediate files are labelled as such.'],
  'repairs': ['Bind downloads to immutable artifact revisions and include status/revision metadata in the UI '
              'and, where appropriate, the file itself.'],
  'exceptions': [],
  'verification': ['Test completion, later correction, and replacement workflows, verifying downloaded '
                   'artifact identity remains unambiguous.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.signing.witness-and-counterparty-roles-distinct',
  'domain': 'signing',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Witness, counterparty, approver, and signer roles must remain distinct in signing workflows',
  'statement': 'A signing interface must not collapse participants with different legal or workflow '
               'responsibilities into a single generic signer role when their required actions and authority '
               'differ.',
  'intent': 'Keep participant obligations and completion status interpretable in multi-role documents.',
  'applies_when': ['The document workflow includes witnesses, counterparties, approvers, preparers, or other '
                   'participant roles alongside signers.'],
  'does_not_apply_when': [],
  'failure_modes': ['A witness is shown as just another signer and receives signature fields or completion '
                    'logic intended for a contracting party.'],
  'user_impacts': ['Participants may perform the wrong action or the sender may believe the document '
                   'satisfies a role requirement that was never met.'],
  'observables': ['Configure documents with several participant roles and inspect invitation, field '
                  'assignment, progress, and completion summaries.'],
  'falsifiers': ['Each participant sees role-appropriate actions and the workflow engine evaluates '
                 'completion against distinct role requirements.'],
  'repairs': ['Model participant role explicitly and bind fields, permissions, messaging, and completion '
              'logic to that role.'],
  'exceptions': [],
  'verification': ['Test role reassignment and substitute participants, verifying no generic signer state '
                   'erases the intended responsibility boundary.'],
  'owner_hints': ['designing-document-signing-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-signing-owners-v13'],
  'status': 'active'}]

__all__ = ["DOCUMENT_SIGNING_RULES_V13"]
