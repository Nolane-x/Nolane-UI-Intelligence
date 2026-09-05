"""V13 identity and session rules authored as distinct authority and recovery contracts."""
from __future__ import annotations

from ._capabilities import interaction_caps


IDENTITY_SESSION_RULES_V13 = [
    {'rule_id': 'ui.identity.session-revocation-blocks-protected-commit',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Protected commits must revalidate a session after revocation',
     'statement': 'A protected mutation started in an already-open session must be rejected if that session has been '
                  'revoked before the authoritative commit boundary, even when stale controls remain visible.',
     'intent': 'Bind authorization to current session authority rather than to the fact that a screen was rendered while '
               'the session was previously valid.',
     'applies_when': ['Long-lived authenticated screens can initiate protected account, security, billing, or data '
                      'mutations while sessions may be revoked elsewhere.'],
     'does_not_apply_when': [],
     'failure_modes': ['A revoked session can still commit a protected action because the client treats its earlier '
                       'authenticated render as continuing authorization.'],
     'user_impacts': ['An attacker or lost device can retain effective authority after the user believes the session was '
                      'terminated.'],
     'observables': ['Open a protected screen, revoke its session from another client, then attempt the mutation without '
                     'refreshing and compare server authority with the visible result.'],
     'falsifiers': ['The commit is rejected against current session state and the client reconciles to a '
                    'reauthentication or signed-out boundary without representing success.'],
     'repairs': ['Revalidate session authority at protected commit time and reconcile stale authenticated UI when '
                 'revocation is observed or returned by the server.'],
     'exceptions': [],
     'verification': ['Revoke a live session remotely and exercise several protected actions from the stale client, '
                      'verifying that none become authoritative.'],
     'owner_hints': ['designing-device-session-management'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-form-auth-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.reauthentication-returns-to-intended-action',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Reauthentication should resume the user at the intended protected action',
     'statement': 'When a valid protected action requires fresh authentication, successful reauthentication should '
                  'return the user to that same bounded action rather than dropping them into an unrelated home or '
                  'account screen.',
     'intent': 'Keep step-up authentication from turning a deliberate action into navigation loss or accidental '
               'repetition while still requiring current authority.',
     'applies_when': ['A user is interrupted by a reauthentication challenge while attempting a specific action whose '
                      'input and target remain valid.'],
     'does_not_apply_when': [],
     'failure_modes': ['After authenticating, the product forgets the target or draft and forces the user to rediscover '
                       'or reconstruct the action from the beginning.'],
     'user_impacts': ['Users can abandon the task, repeat side effects, or accidentally act on a different record after '
                      'rebuilding context.'],
     'observables': ['Begin a protected action with identifiable target state, trigger reauthentication, complete it, '
                     'and inspect the resumed route, target, draft, and action boundary.'],
     'falsifiers': ['The exact still-valid target and draft are restored, while stale or changed targets are revalidated '
                    'before the action can continue.'],
     'repairs': ['Persist a bounded continuation token for the intended action and restore it only after successful '
                 'authentication and freshness checks.'],
     'exceptions': [],
     'verification': ['Exercise step-up authentication from multiple protected actions and confirm each returns to the '
                      'correct target without auto-committing the action.'],
     'owner_hints': ['designing-authentication-and-passkeys'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-form-auth-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.current-session-distinguished-in-device-list',
     'domain': 'identity',
     'class': 'mechanical',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'The current session must be distinguishable in session-management lists',
     'statement': 'A device or session management surface must clearly identify the session being used to view the list '
                  'so users can revoke other sessions without guessing which entry represents the active client.',
     'intent': 'Prevent session-management controls from creating self-lockout or false confidence through ambiguous '
               'device labels and timestamps.',
     'applies_when': ['The product exposes multiple authenticated sessions or devices that can be individually revoked '
                      'or signed out.'],
     'does_not_apply_when': [],
     'failure_modes': ['The current client is visually indistinguishable from similar sessions, making a user choose '
                       'based only on uncertain device names or approximate times.'],
     'user_impacts': ['Users can terminate the wrong session or leave an unwanted session active because the list does '
                      'not expose the one fact the product knows locally.'],
     'observables': ['Open the session list from two similar devices and compare the entry representing the current '
                     'request context against the authoritative session identifier.'],
     'falsifiers': ['Exactly one entry is marked as the current session when the product can determine it, and uncertain '
                    'device metadata is not presented as stronger identity proof.'],
     'repairs': ['Bind the local session identifier to its list entry and expose a current-session marker separate from '
                 'inferred device name or location.'],
     'exceptions': [],
     'verification': ['Create several similar sessions, open management from each, and verify the current marker follows '
                      'the actual authenticated session rather than list ordering.'],
     'owner_hints': ['designing-device-session-management'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-form-auth-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.recovery-channel-change-requires-fresh-auth',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Recovery-channel changes require current high-confidence authority',
     'statement': 'Changing the email address, phone number, authenticator destination, or other channel used for '
                  'account recovery must not rely solely on an old ambient session when the change would redirect future '
                  'recovery authority.',
     'intent': 'Treat recovery-channel mutation as an authority transfer rather than an ordinary profile edit because it '
               'changes who can regain the account later.',
     'applies_when': ['An authenticated user can replace or add a channel that participates in account recovery or '
                      'authenticator reset.'],
     'does_not_apply_when': [],
     'failure_modes': ['A long-lived or weakly authenticated session can redirect recovery to a new channel without a '
                       'fresh check appropriate to the product risk model.'],
     'user_impacts': ['Compromise of an unattended session can be converted into durable account takeover even after the '
                      'original session is later revoked.'],
     'observables': ['Attempt recovery-channel changes from fresh, aged, and remotely revoked sessions and inspect '
                     'whether the product applies its declared recent-authentication policy.'],
     'falsifiers': ['The change is accepted only after the required current authentication evidence and the new channel '
                    'does not silently become recovery authority before verification.'],
     'repairs': ['Insert an explicit recent-authentication boundary before recovery authority changes and verify the '
                 'destination according to the product recovery model.'],
     'exceptions': [],
     'verification': ['Exercise channel addition, replacement, and removal across session-age states and verify the '
                      'authoritative recovery configuration after each attempt.'],
     'owner_hints': ['designing-account-recovery-flows'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-form-auth-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.passkey-registration-exposes-account-and-device-context',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Passkey registration must expose the account and authenticator context being changed',
     'statement': 'Before committing passkey registration, the UI should make clear which account is receiving the '
                  'credential and enough authenticator or provider context to distinguish the new registration from an '
                  'unexplained generic success.',
     'intent': 'Keep authenticator enrollment legible when users have multiple accounts, synced credential providers, '
               'roaming authenticators, or device-bound credentials.',
     'applies_when': ['The product allows adding a passkey or comparable authenticator while multiple accounts or '
                      'credential storage contexts can be active.'],
     'does_not_apply_when': [],
     'failure_modes': ['Registration reports only that a passkey was added, without confirming the target account or '
                       'giving any useful context for recognizing the new authenticator later.'],
     'user_impacts': ['Users can enroll the wrong account, fail to recognize a credential in management UI, or remove '
                      'the wrong authenticator during later recovery.'],
     'observables': ['Register credentials under multiple signed-in accounts and authenticator contexts, then compare '
                     'the enrollment confirmation with the resulting credential-management record.'],
     'falsifiers': ['The confirmation and management record identify the same account and expose only authenticator '
                    'context the platform can truthfully provide without inventing hardware identity.'],
     'repairs': ['Carry account identity and platform-provided authenticator metadata through the enrollment transaction '
                 'and render them consistently in confirmation and management views.'],
     'exceptions': [],
     'verification': ['Enroll, rename when supported, and remove several passkeys while verifying that each visible '
                      'record maps to the intended account and underlying credential.'],
     'owner_hints': ['designing-authentication-and-passkeys'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-form-auth-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.account-switch-clears-prior-account-authority',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Account switching must clear action authority inherited from the prior account',
     'statement': 'After switching identities inside the same client, pending forms, selections, cached permissions, and '
                  'mutation targets owned by the previous account must not remain actionable under the newly active '
                  'account without explicit revalidation.',
     'intent': 'Prevent a client-level identity switch from carrying record authority or drafts across account '
               'boundaries merely because the view instance stayed mounted.',
     'applies_when': ['The application supports switching between accounts, tenants, profiles, or organizations without '
                      'fully closing the client.'],
     'does_not_apply_when': [],
     'failure_modes': ['A view created under account A remains capable of submitting or mutating account A state after '
                       'account B becomes the active identity, or it silently redirects the action to B.'],
     'user_impacts': ['Users can write to the wrong account, leak cross-tenant context, or misattribute an action '
                      'because visible identity and underlying target authority diverge.'],
     'observables': ['Open mutable state under one account, switch identity without a hard reload, then attempt each '
                     'stale action while observing target account and authorization checks.'],
     'falsifiers': ['Old account actions are invalidated or clearly retained as non-committable drafts, and new actions '
                    'bind to the newly active identity only after target revalidation.'],
     'repairs': ['Invalidate identity-scoped action contexts on switch and require record, tenant, permission, and draft '
                 'ownership to be rebound before commit.'],
     'exceptions': [],
     'verification': ['Test rapid account switching with open drafts, selected rows, uploads, and destructive dialogs '
                      'and verify no stale authority crosses the identity boundary.'],
     'owner_hints': ['designing-cross-device-session-handoffs'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-internal-product-truth-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.shared-device-signout-clears-sensitive-residue',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Sign-out on a shared device must clear sensitive residue owned by the departed identity',
     'statement': 'When a user signs out from a shared-device context, sensitive cached previews, recent records, '
                  'clipboard helpers, drafts, notifications, and identity-scoped suggestions must not remain exposed to '
                  'the next user unless explicitly designed as device-shared data.',
     'intent': 'Make sign-out a real privacy boundary on shared hardware rather than only a token deletion while '
               'sensitive UI state remains locally visible.',
     'applies_when': ['The product can be used by different people on the same device and retains local caches, drafts, '
                      'recents, or notification surfaces across sessions.'],
     'does_not_apply_when': [],
     'failure_modes': ['After sign-out, another person can recover sensitive content from application recents, preserved '
                       'drafts, previews, autocomplete, or locally rendered notification history.'],
     'user_impacts': ['Private information can cross user boundaries even though the departed user completed the '
                      "product's explicit sign-out action."],
     'observables': ['Populate sensitive local state, sign out, enter the application as another user or unauthenticated '
                     'user, and inspect every persisted identity-scoped surface.'],
     'falsifiers': ['Identity-scoped sensitive residue is removed or cryptographically inaccessible, while intentionally '
                    'device-shared data is clearly governed by a separate policy.'],
     'repairs': ['Tag local persistence by identity and sensitivity, then purge or seal identity-scoped data at sign-out '
                 'without deleting intentionally shared device resources.'],
     'exceptions': [],
     'verification': ['Run shared-device sign-out tests covering recents, caches, notifications, drafts, local search, '
                      'previews, and offline storage before and after a different user signs in.'],
     'owner_hints': ['designing-shared-device-session-boundaries'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.identity.auth-step-retry-does-not-reset-valid-progress',
     'domain': 'identity',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Retrying one failed authentication step must not erase still-valid completed factors',
     'statement': 'In a multi-step authentication ceremony, retrying a failed or expired factor should preserve other '
                  'completed evidence when the authentication protocol still considers that evidence valid instead of '
                  'restarting the entire flow by UI convention.',
     'intent': 'Keep retry behavior aligned with actual authentication evidence lifetime while avoiding unnecessary '
               'repetition that can cause abandonment or mistakes.',
     'applies_when': ['The declared authentication flow combines multiple factors, device checks, identity proofing '
                      'steps, or recovery confirmations with independent validity windows.'],
     'does_not_apply_when': [],
     'failure_modes': ['A transient failure in one step resets every prior step even though the server still retains '
                       'valid evidence, or the UI preserves a step after server validity expired.'],
     'user_impacts': ['Users repeat sensitive challenges unnecessarily or believe a factor remains accepted when the '
                      'authority has actually discarded it.'],
     'observables': ['Complete all but one authentication step, induce retriable and expiry failures, then compare the '
                     'resumed UI with server-side factor validity after each retry.'],
     'falsifiers': ['Only evidence the authentication authority still considers valid is preserved; expired or '
                    'invalidated factors are clearly required again.'],
     'repairs': ['Drive the stepper from authoritative ceremony state rather than local step index and retry only the '
                 'factor or branch whose evidence actually failed.'],
     'exceptions': [],
     'verification': ['Test transient failure, timeout, explicit cancel, and server-side evidence expiry at each stage '
                      'and verify the UI resumes from the correct authoritative state.'],
     'owner_hints': ['designing-authentication-and-passkeys'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nist-sp800-63b4-v13', 'nui-form-auth-owners-v13'],
     'status': 'active'},
]

__all__ = ['IDENTITY_SESSION_RULES_V13']
