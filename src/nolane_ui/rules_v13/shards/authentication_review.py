"""V13 eighth-wave independently authored rules for authreview."""
from __future__ import annotations

from ._capabilities import interaction_caps


AUTH_REVIEW_RULES_V13 = [{'rule_id': 'ui.authreview.risk-signal-freshness-visible',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Authentication risk signals must disclose the observation time used in the current review',
  'statement': 'Device reputation, impossible-travel, IP risk, behavior scores, and similar signals '
               'should expose freshness so reviewers can distinguish current evidence from stale '
               'enrichment.',
  'intent': 'Prevent security decisions from treating old risk context as though it were observed at '
            'the moment of review.',
  'applies_when': ['Authentication anomaly review combines signals that arrive or refresh on different '
                   'schedules.'],
  'does_not_apply_when': [],
  'failure_modes': ['A device reputation badge remains high risk for days after the source changed, '
                    'with no timestamp or stale indicator in the review workspace.'],
  'user_impacts': ['Reviewers can block or allow access based on evidence whose temporal relevance they '
                   'cannot assess.'],
  'observables': ['Freeze and refresh individual risk feeds while inspecting timestamps, stale '
                  'indicators, and the decision summary.'],
  'falsifiers': ['Each signal exposes an observation or effective time and stale data remains visibly '
                 'distinct from freshly evaluated evidence.'],
  'repairs': ['Carry source freshness metadata into the review model and render stale state instead of '
              'caching only the latest label.'],
  'exceptions': [],
  'verification': ['Vary source update cadence and verify the reviewer can identify which risk signals '
                   'were current at the decision boundary.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.session-target-identity-stable',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Authentication review actions must remain bound to the exact session or attempt under '
           'investigation',
  'statement': 'When several login attempts or active sessions belong to the same account, revoke, '
               'challenge, or allow actions must target the stable reviewed session identity rather '
               'than whichever attempt is newest.',
  'intent': 'Prevent security actions from drifting to a different authentication event during live '
            'account activity.',
  'applies_when': ['One identity can have multiple concurrent or rapidly repeated authentication '
                   'attempts and sessions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reviewer opens attempt A, a new login B arrives, and the “revoke session” '
                    'control silently targets B because the UI tracks only the account’s current '
                    'session.'],
  'user_impacts': ['Legitimate sessions can be disrupted while the anomalous session remains active.'],
  'observables': ['Generate multiple attempts for one user, keep an older review open, and inspect '
                  'action payloads and resulting session state.'],
  'falsifiers': ['Every decision and action names the stable session or attempt identity reviewed and '
                 'cannot retarget due to later account activity.'],
  'repairs': ['Bind review context and commands to immutable attempt or session IDs and require '
              'explicit selection when acting on account-wide scope.'],
  'exceptions': [],
  'verification': ['Race new sign-ins with revoke, challenge, and allow actions, verifying each '
                   'operation affects only the disclosed target scope.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.reauthentication-not-dismiss-investigation',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Successful reauthentication must not automatically erase the anomaly investigation that '
           'prompted it',
  'statement': 'A user completing an authentication challenge can satisfy one control while the '
               'underlying suspicious event, device, or session may still require analyst disposition.',
  'intent': 'Keep challenge success from being mistaken for proof that every risk signal was false.',
  'applies_when': ['An anomaly workflow can request reauthentication while analysts separately review '
                   'the triggering evidence.'],
  'does_not_apply_when': [],
  'failure_modes': ['The challenged user succeeds with MFA and the case disappears from the analyst '
                    'queue even though the anomalous device or impossible-travel evidence was never '
                    'reviewed.'],
  'user_impacts': ['Important account-compromise evidence can be lost because one authentication factor '
                   'was treated as full investigative resolution.'],
  'observables': ['Complete and fail reauthentication under several anomaly types and observe queue '
                  'state, evidence retention, and analyst disposition controls.'],
  'falsifiers': ['Challenge outcome is recorded as evidence but investigation closure remains an '
                 'explicit, separately justified transition.'],
  'repairs': ['Model authentication challenge and investigation lifecycle independently, linking the '
              'outcome without allowing it to auto-delete review authority.'],
  'exceptions': [],
  'verification': ['Exercise successful challenges with both benign and malicious fixtures and verify '
                   'investigators still control final anomaly disposition.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.challenge-outcome-distinguished',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Authentication challenge outcomes must distinguish success, failure, timeout, cancel, and '
           'unavailable paths',
  'statement': 'The review surface should not collapse all non-successful challenges into “failed” '
               'because different outcomes imply different confidence about user intent and system '
               'availability.',
  'intent': 'Preserve the evidentiary meaning of authentication challenge results.',
  'applies_when': ['An anomaly response can send or require MFA, passkey, recovery, or other '
                   'authentication challenges.'],
  'does_not_apply_when': [],
  'failure_modes': ['A push challenge expires because the user is offline and the UI records “user '
                    'failed MFA,” making timeout look like an explicit failed response.'],
  'user_impacts': ['Reviewers can infer malicious or negligent behavior from an outcome that actually '
                   'reflects delivery or availability failure.'],
  'observables': ['Force success, explicit denial, wrong response, timeout, cancellation, and provider '
                  'outage while inspecting the stored challenge event.'],
  'falsifiers': ['Each outcome retains its distinct state, actor or system cause, and timing rather '
                 'than being normalized into one failure label.'],
  'repairs': ['Use a typed challenge outcome model and preserve transport or availability failures '
              'separately from user responses.'],
  'exceptions': [],
  'verification': ['Run controlled challenge outcomes and verify analyst summaries, audit history, and '
                   'automation consume the same distinct semantics.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.device-trust-state-visible',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Device trust state must show its source and effective scope during authentication review',
  'statement': 'A trusted or untrusted badge should identify whether it comes from enrollment, policy, '
               'prior verification, administrative override, or another source and where that trust '
               'applies.',
  'intent': 'Prevent reviewers from treating a vague trust label as stronger or broader evidence than '
            'the underlying authority grants.',
  'applies_when': ['Authentication risk decisions incorporate device enrollment, trust, management, or '
                   'remembered-device state.'],
  'does_not_apply_when': [],
  'failure_modes': ['A device appears “trusted” because it passed an old remember-device flow, but the '
                    'reviewer assumes it is currently managed and organization-approved.'],
  'user_impacts': ['Access decisions can be relaxed on a misleading trust signal whose origin and scope '
                   'are unclear.'],
  'observables': ['Create devices with different trust sources and inspect review badges, details, and '
                  'policy decisions across tenants or applications.'],
  'falsifiers': ['Trust state exposes its source, age or effective period, and applicable scope without '
                 'conflating remembered, managed, and verified meanings.'],
  'repairs': ['Model device trust as typed evidence with provenance and scope rather than a single '
              'boolean reused across authentication contexts.'],
  'exceptions': [],
  'verification': ['Review remembered, managed, newly enrolled, and revoked devices and verify each '
                   'trust representation matches its real authority.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.false-positive-dismissal-scope-visible',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dismissing an authentication anomaly as false positive must disclose what future detections '
           'the dismissal affects',
  'statement': 'A reviewer decision can close one event, tune a detector, trust an entity, or suppress '
               'a pattern; the UI must make that downstream scope explicit before commitment.',
  'intent': 'Prevent a benign decision on one login from silently weakening future anomaly detection.',
  'applies_when': ['Anomaly review offers false-positive, allow, trust, suppress, or similar '
                   'disposition actions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reviewer marks one travel anomaly false positive and unknowingly creates a broad '
                    'allowlist for the source IP across all users.'],
  'user_impacts': ['Future malicious sign-ins can bypass review because the disposition had broader '
                   'authority than the analyst intended.'],
  'observables': ['Apply each dismissal variant and inspect generated rules, entity trust, future '
                  'detections, and expiration behavior.'],
  'falsifiers': ['The disposition preview states whether it affects only the reviewed event or creates '
                 'persistent scope, and subsequent detections follow that scope exactly.'],
  'repairs': ['Separate event disposition from future suppression or trust creation and require '
              'explicit confirmation for persistent policy effects.'],
  'exceptions': [],
  'verification': ['Dismiss identical-looking anomalies with event-only and persistent choices, then '
                   'verify future alerts differ only according to the disclosed scope.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.lockout-bypass-authority-explicit',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Lockout bypass and emergency access actions must make their authority and expiration '
           'explicit',
  'statement': 'When a reviewer can bypass authentication controls for recovery or emergency '
               'operations, the interface must show who is authorized, what control is bypassed, for '
               'whom, and until when.',
  'intent': 'Keep exceptional access from becoming an ambiguous permanent weakening of authentication '
            'policy.',
  'applies_when': ['Administrators can override lockouts, risk blocks, MFA requirements, or other '
                   'authentication controls.'],
  'does_not_apply_when': [],
  'failure_modes': ['An operator clicks “allow login” with no visible duration and the account remains '
                    'exempt from risk enforcement indefinitely.'],
  'user_impacts': ['Exceptional recovery access can outlive its intended purpose and expose the account '
                   'to ongoing compromise.'],
  'observables': ['Create time-bounded and one-time overrides, inspect active policy state, and attempt '
                  'access before, during, and after expiration.'],
  'falsifiers': ['Every bypass exposes actor, target, bypassed control, effective scope, and expiry or '
                 'one-time consumption state.'],
  'repairs': ['Represent bypasses as explicit, auditable grants with bounded scope and automatic expiry '
              'instead of hidden flags on the account.'],
  'exceptions': [],
  'verification': ['Exercise override creation, revocation, expiration, and concurrent login attempts, '
                   'verifying policy resumes exactly when the grant ends.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.authreview.investigation-action-linked-to-audit-event',
  'domain': 'authreview',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Authentication review actions must create traceable audit events linked to the investigated '
           'attempt',
  'statement': 'Revocation, unlock, challenge, allow, block, trust, and suppression actions should '
               'preserve who acted, on which attempt or session, and from which review context.',
  'intent': 'Enable later reconstruction of security decisions without relying on mutable screen state '
            'or analyst memory.',
  'applies_when': ['An anomaly workspace allows analysts to take actions that change account, session, '
                   'or detection policy state.'],
  'does_not_apply_when': [],
  'failure_modes': ['A session is revoked from the review screen but the audit trail records only a '
                    'generic account update with no link to the suspicious attempt that motivated it.'],
  'user_impacts': ['Incident review cannot connect a security action to the evidence and decision '
                   'context that caused it.'],
  'observables': ['Perform each review action and inspect the authentication event timeline, '
                  'centralized audit log, and case linkage.'],
  'falsifiers': ['Every material action emits an immutable audit record naming actor, target, action '
                 'result, and the reviewed authentication context.'],
  'repairs': ['Pass investigation identifiers through command execution and write audit events from '
              'committed outcomes rather than from button clicks alone.'],
  'exceptions': [],
  'verification': ['Run successful and failed review actions and verify their audit records remain '
                   'linked to the exact attempt, session, and decision outcome.'],
  'owner_hints': ['designing-authentication-anomaly-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-auth-review-owners-v13'],
  'status': 'active'}]


__all__ = ["AUTH_REVIEW_RULES_V13"]
