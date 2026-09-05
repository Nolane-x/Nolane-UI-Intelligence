"""V13 onboarding and permission rules for deferral, progress truth, prompt state, and scope expansion."""
from __future__ import annotations

from ._capabilities import interaction_caps


ONBOARDING_PERMISSIONS_RULES_V13 = [
    {'rule_id': 'ui.onboarding.skip-keeps-settings-reentry-path',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Skipping onboarding must leave a discoverable path to the skipped configuration',
     'statement': 'When onboarding lets users skip a setup choice that can be completed later, the normal product must '
                  'provide a discoverable place to return to that choice instead of making skip effectively permanent.',
     'intent': 'Keep skip as deferral rather than accidental loss of access to configuration the product itself '
               'considers optional at first run.',
     'applies_when': ['An onboarding step can be skipped and the underlying configuration remains valid to perform later '
                      'from the product.'],
     'does_not_apply_when': [],
     'failure_modes': ['After skip, the same setting or setup action has no discoverable destination except resetting '
                       'onboarding or finding an undocumented deep link.'],
     'user_impacts': ['Users can become stuck with defaults they intentionally deferred and may conclude the product '
                      'does not support changing them.'],
     'observables': ['Skip each deferrable step, enter the normal product, and locate the corresponding setting or '
                     'workflow without using test-only routes.'],
     'falsifiers': ['Every deferrable skipped choice has a documented normal-product reentry path, while truly one-time '
                    'setup is not falsely labeled skippable.'],
     'repairs': ['Pair skip-enabled onboarding steps with stable settings or workflow destinations and link to them from '
                 'relevant product surfaces.'],
     'exceptions': [],
     'verification': ['Test skip, later completion, completion from another device, and onboarding reset and verify the '
                      'deferred configuration remains reachable.'],
     'owner_hints': ['designing-onboarding'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-onboarding-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.checklist-completion-derived-from-real-state',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Onboarding checklist completion must reflect actual product state rather than click history',
     'statement': 'A checklist item representing setup completion must derive from the authoritative configuration or '
                  'successful outcome it names, not merely from the user opening the step or pressing a local continue '
                  'button.',
     'intent': 'Prevent progress UI from claiming readiness when the underlying integration, profile, permission, or '
               'setup task never actually completed.',
     'applies_when': ['Onboarding uses a checklist to represent externally verifiable setup tasks or product '
                      'configuration state.'],
     'does_not_apply_when': [],
     'failure_modes': ['An item becomes complete after visiting its screen even though the integration failed, '
                       'permission was denied, or required configuration remains missing.'],
     'user_impacts': ['Users can finish onboarding with a false sense that the product is ready and discover missing '
                      'setup only during later work.'],
     'observables': ['Open checklist steps while forcing their underlying setup to fail or be revoked, then compare '
                     'checklist state with authoritative product configuration.'],
     'falsifiers': ['Completion tracks the real state and can revert when the relevant setup is later removed or no '
                    'longer valid if the product semantics require that.'],
     'repairs': ['Derive checklist status from the same source of truth used by the feature itself and treat navigation '
                 'history only as tutorial progress, not setup authority.'],
     'exceptions': [],
     'verification': ['Test successful, failed, skipped, revoked, and cross-device setup outcomes and verify checklist '
                      'completion matches effective configuration.'],
     'owner_hints': ['designing-onboarding-checklists'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-onboarding-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.permission-primer-matches-requested-capability',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Permission primers must describe the capability the next system prompt will actually request',
     'statement': 'If a product shows explanatory UI before a platform permission prompt, the primer must match the '
                  'exact powerful feature and purpose about to be requested rather than bundling unrelated capabilities '
                  'or promising narrower access than the system request.',
     'intent': 'Keep pre-permission explanation aligned with the real platform capability boundary so informed choice is '
               'possible.',
     'applies_when': ['Onboarding or first-run flows show custom education immediately before invoking camera, '
                      'microphone, location, notification, sensor, or similar platform permission.'],
     'does_not_apply_when': [],
     'failure_modes': ['The primer describes one purpose or narrower scope while the following system prompt requests a '
                       'different or broader capability.'],
     'user_impacts': ['Users can grant access under a misleading expectation and may not understand why the platform '
                      'prompt differs from the product explanation.'],
     'observables': ['Instrument each primer-to-system-prompt transition and compare visible capability/purpose with the '
                     'permission descriptor actually requested.'],
     'falsifiers': ['The primer accurately names the requested capability and product purpose without claiming platform '
                    'scope or persistence the application cannot control.'],
     'repairs': ['Generate the primer from the same permission request definition and split unrelated capabilities into '
                 'separate user decisions where platform APIs permit.'],
     'exceptions': [],
     'verification': ['Test every permission path including optional features, retries, upgrades, and platform variants '
                      'and verify primer and actual request remain aligned.'],
     'owner_hints': ['designing-permission-onboarding'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-permissions-2025-v13', 'nui-internal-product-truth-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.denied-permission-does-not-loop-prompt',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'A denied permission must not trap onboarding in a repeated prompt loop',
     'statement': 'After a user denies or dismisses a platform permission, onboarding must transition to a truthful '
                  'denied, deferred, or alternative state rather than immediately invoking the same prompt again with no '
                  'new user intent.',
     'intent': 'Respect a permission decision as product state and preserve forward progress where the feature is '
               'optional or recoverable.',
     'applies_when': ['An onboarding step requests a platform permission that users may deny, dismiss, or configure as '
                      'ask-later.'],
     'does_not_apply_when': [],
     'failure_modes': ['Denial returns to the same screen whose automatic entry immediately triggers another prompt, '
                       'making escape difficult or impossible.'],
     'user_impacts': ['Users can be coerced into granting a permission or forced to abandon the application because the '
                      'UI ignores the denial state.'],
     'observables': ['Deny, dismiss, and permanently block the permission across supported platforms and observe whether '
                     'onboarding can proceed or reach a stable recovery state without prompt recursion.'],
     'falsifiers': ['The product records the denied or unavailable state and only requests again after explicit user '
                    'action or a documented platform-appropriate retry boundary.'],
     'repairs': ['Gate permission invocation behind explicit intent after denial and provide skip, settings, manual '
                 'alternative, or feature-disabled paths as appropriate.'],
     'exceptions': [],
     'verification': ['Test repeated denials, app restart, settings changes, and one-time grants and verify prompt count '
                      'and onboarding state follow user intent.'],
     'owner_hints': ['designing-permission-onboarding'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-permissions-2025-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.one-time-permission-expiry-reconciles-ui',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'One-time permission expiry must reconcile setup UI back to a truthful capability state',
     'statement': 'If a platform grant is temporary or one-time, onboarding and later settings must not keep showing the '
                  'feature as permanently configured after the permission expires or the session loses that grant.',
     'intent': 'Distinguish completed education from current platform authorization so permission lifetime does not '
               'become invisible stale state.',
     'applies_when': ['The platform can grant a powerful feature temporarily, for one session, one use, foreground-only '
                      'access, or another bounded lifetime.'],
     'does_not_apply_when': [],
     'failure_modes': ['The onboarding checklist and feature settings remain checked or complete indefinitely after the '
                       'temporary permission has expired.'],
     'user_impacts': ['Users can believe a feature will work automatically and encounter unexplained failure only when '
                      'they later need it.'],
     'observables': ['Grant the shortest supported lifetime, allow it to expire, then inspect onboarding completion, '
                     'settings, feature entry, and the next permission request behavior.'],
     'falsifiers': ['UI reflects that onboarding education may be complete while current authorization is no longer '
                    'granted, and the next action follows platform state.'],
     'repairs': ['Store education progress separately from live permission status and refresh effective capability state '
                 'when the application resumes or permission changes.'],
     'exceptions': [],
     'verification': ['Test one-time, session, persistent, revoked, and restricted permission lifetimes and verify setup '
                      'state never conflates them.'],
     'owner_hints': ['designing-permissions-and-consent'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-permissions-2025-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.resume-returns-to-unresolved-step',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Resuming interrupted onboarding should return to the first still-unresolved requirement',
     'statement': 'When onboarding is interrupted by app termination, authentication, external setup, or device handoff, '
                  'resume should derive the next step from authoritative completion state instead of restarting from '
                  'step one or trusting a stale local index.',
     'intent': 'Preserve progress without skipping work that never completed or forcing users to repeat configuration '
               'already authoritative.',
     'applies_when': ['Onboarding spans multiple steps and can be interrupted or completed partially through external or '
                      'cross-device actions.'],
     'does_not_apply_when': [],
     'failure_modes': ['Resume uses only the last viewed step number, causing already-completed tasks to repeat or '
                       'failed tasks to be skipped after state changes.'],
     'user_impacts': ['Users waste time, miss required setup, or see contradictory progress after returning to the '
                      'product.'],
     'observables': ['Interrupt onboarding at each step, mutate completion externally where possible, then relaunch and '
                     'compare resumed step with current authoritative checklist state.'],
     'falsifiers': ['Resume lands on the earliest unresolved requirement or the completed product when all requirements '
                    'are satisfied, regardless of stale local navigation position.'],
     'repairs': ['Compute resume position from durable per-step completion predicates and use local navigation history '
                 'only as a secondary presentation hint.'],
     'exceptions': [],
     'verification': ['Test app kill, sign-in redirect, device switch, external verification, and step failure and '
                      'verify resume selects the correct unresolved work.'],
     'owner_hints': ['designing-onboarding'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-onboarding-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.optional-personalization-does-not-block-core',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Optional personalization must not become a disguised gate to core product access',
     'statement': 'If personalization questions, preference setup, profile enrichment, or recommendation tuning are '
                  'described as optional, declining them must still reach the core product without substituting an '
                  'endless skip sequence or degraded lockout.',
     'intent': 'Make optionality operational rather than rhetorical so users can begin the product without donating '
               'preferences the core task does not require.',
     'applies_when': ['First-run onboarding asks for optional interests, personalization signals, profile details, or '
                      'recommendation preferences before entering the product.'],
     'does_not_apply_when': [],
     'failure_modes': ['Skip or not-now controls route to equivalent optional questions repeatedly, disable core '
                       'navigation, or produce a screen that cannot proceed without at least one answer.'],
     'user_impacts': ['Users are coerced into providing optional data and cannot distinguish required setup from '
                      'preference collection.'],
     'observables': ['Decline every optional personalization step using supported paths and verify the product reaches '
                     'its normal core entry state with no hidden required answer.'],
     'falsifiers': ['Core access remains available and omitted preferences retain a truthful unset/default state rather '
                    'than being fabricated from forced choices.'],
     'repairs': ['Separate required readiness predicates from optional preference collection and make the skip path '
                 'terminate directly into the product.'],
     'exceptions': [],
     'verification': ['Test all-skip, partial answers, later settings edits, and account restore and verify optional '
                      'personalization never becomes a hidden core-access prerequisite.'],
     'owner_hints': ['designing-first-run-onboarding'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-onboarding-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.onboarding.permission-scope-expansion-explains-delta',
     'domain': 'onboarding',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Permission scope expansion must explain what changed from the previously granted capability',
     'statement': 'When a product asks for broader permission after an earlier narrower grant, the explanatory UI must '
                  'identify the additional capability or persistence being requested rather than presenting the new '
                  'prompt as routine setup repetition.',
     'intent': 'Give users a meaningful new decision when product functionality expands beyond the authority they '
               'already granted.',
     'applies_when': ['A feature can operate under a narrower permission first and later requests additional device, '
                      'background, persistent, or data-access scope.'],
     'does_not_apply_when': [],
     'failure_modes': ['The second request reuses generic onboarding copy and does not distinguish the new authority '
                       'from the capability the user already approved.'],
     'user_impacts': ['Users may consent without realizing the product is asking for broader or longer-lived access than '
                      'before.'],
     'observables': ['Exercise each upgrade path from narrower to broader permission and compare existing grant, primer '
                     'copy, actual descriptor, and resulting capability.'],
     'falsifiers': ['The delta is explicit and the broader request occurs only from a feature path that genuinely '
                    'requires the additional authority.'],
     'repairs': ['Model permission upgrades as transitions between named capability states and render the new authority '
                 'relative to the currently effective grant.'],
     'exceptions': [],
     'verification': ['Test foreground-to-background, single-device-to-broader-device, one-time-to-persistent where '
                      'applicable, and denied upgrades and verify the scope delta stays visible.'],
     'owner_hints': ['designing-permissions-and-consent'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-permissions-2025-v13'],
     'status': 'active'},
]

__all__ = ['ONBOARDING_PERMISSIONS_RULES_V13']
