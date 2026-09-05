"""V13 seventh-wave independently authored rules for verification codes."""
from __future__ import annotations

from ._capabilities import interaction_caps


VERIFICATION_CODE_RULES_V13 = [{'rule_id': 'ui.verification.code-expiry-state-visible',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'One-time verification codes must expose expiry or expired state without pretending stale codes '
           'remain usable',
  'statement': 'When a challenge code has an expiry, the UI should communicate whether the current code is '
               'still valid or has expired and provide the appropriate next step.',
  'intent': 'Prevent users from repeatedly entering a code the server can no longer accept.',
  'applies_when': ['An authentication or verification challenge issues time-limited codes.'],
  'does_not_apply_when': [],
  'failure_modes': ['The entry screen continues accepting an expired code with no state change or shows an '
                    'inaccurate client-only countdown after the server invalidated it.'],
  'user_impacts': ['Users can waste attempts, trigger lockouts, or believe delivery is broken when the '
                   'challenge itself is obsolete.'],
  'observables': ['Issue a short-lived code, skew or pause the client clock, let server expiry occur, then '
                  'submit and inspect the recovery state.'],
  'falsifiers': ['The UI reconciles authoritative expiry and routes users toward resend or a fresh challenge '
                 'without claiming validity from an untrusted timer alone.'],
  'repairs': ['Model challenge expiry server-side and use client timing only as presentation that can be '
              'corrected by authoritative responses.'],
  'exceptions': [],
  'verification': ['Test background suspension, device clock changes, and delayed messages, verifying stale '
                   'codes consistently resolve to an expired challenge state.'],
  'owner_hints': ['designing-one-time-code-entry'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.resend-challenge-replacement-semantics-visible',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resending a verification code must make clear whether earlier codes remain valid or are replaced',
  'statement': 'A resend action should not leave users guessing which of several messages contains the '
               'currently acceptable code when the challenge system invalidates or preserves prior codes.',
  'intent': 'Reduce repeated failures caused by ambiguous multiple-code lifecycles.',
  'applies_when': ['The product can issue more than one code for the same verification purpose.'],
  'does_not_apply_when': [],
  'failure_modes': ['Each resend generates a new code but the UI gives no indication that older codes are '
                    'invalidated, or claims replacement while the server accepts both.'],
  'user_impacts': ['Users may enter an older delivered message and consume attempts even though they '
                   'followed the product’s recovery action.'],
  'observables': ['Request multiple resends, enter codes in different order, and compare server acceptance '
                  'with the UI’s stated lifecycle.'],
  'falsifiers': ['User-facing resend language matches actual challenge semantics, and the current challenge '
                 'identity is unambiguous.'],
  'repairs': ['Bind resends to an explicit challenge policy and present whether a new message replaces or '
              'supplements earlier codes.'],
  'exceptions': [],
  'verification': ['Test rapid resends and delayed delivery, verifying acceptance behavior and guidance '
                   'remain consistent across all issued codes.'],
  'owner_hints': ['designing-one-time-code-entry'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.code-entry-supports-paste-and-autofill',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Verification code inputs should support safe paste and platform autofill without forcing '
           'digit-by-digit entry',
  'statement': 'A multi-cell code UI must accept a complete valid code from paste or supported one-time-code '
               'autofill and distribute it correctly without trapping focus or dropping characters.',
  'intent': 'Make common secure delivery workflows efficient and accessible without weakening challenge '
            'validation.',
  'applies_when': ['Users receive codes through SMS, email, password managers, or device autofill and the '
                   'product uses segmented visual inputs.'],
  'does_not_apply_when': [],
  'failure_modes': ['Pasting six digits enters only the first cell, reverses digits, or causes focus jumps '
                    'that overwrite characters.'],
  'user_impacts': ['Users make unnecessary entry errors and assistive technology has difficulty interacting '
                   'with a purely visual segmented control.'],
  'observables': ['Paste and autofill complete codes using keyboard, mobile OTP suggestions, and assistive '
                  'technology while inspecting the logical input value.'],
  'falsifiers': ['The full code is accepted as one logical value, validation remains server-authoritative, '
                 'and segmented presentation does not block standard input mechanisms.'],
  'repairs': ['Implement a coherent logical input model that can render segmentation without splitting basic '
              'paste/autofill semantics.'],
  'exceptions': [],
  'verification': ['Test paste with separators, mobile autofill, deletion, and screen readers, verifying the '
                   'submitted code exactly matches user input.'],
  'owner_hints': ['designing-one-time-code-entry'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.attempt-lock-state-visible-without-false-countdown',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Verification lock or cooldown state must be visible without inventing a precise countdown the '
           'server does not guarantee',
  'statement': 'If repeated attempts trigger throttling or temporary lock, the UI should explain that state '
               'and only show remaining time when the authority actually provides a reliable expiry.',
  'intent': 'Help users recover without revealing or fabricating security-state precision.',
  'applies_when': ['The verification service can throttle attempts or temporarily block further '
                   'submissions.'],
  'does_not_apply_when': [],
  'failure_modes': ['The client starts its own fixed 60-second countdown after an error even though the '
                    'server uses a different or adaptive cooldown.'],
  'user_impacts': ['Users retry too early, see contradictory timers across devices, or infer security policy '
                   'that is not actually true.'],
  'observables': ['Trigger rate limiting from multiple clients and compare displayed lock state with '
                  'authoritative retry responses and timestamps.'],
  'falsifiers': ['The UI communicates the blocked state and any retry time within the precision supported by '
                 'the service, reconciling when policy changes.'],
  'repairs': ['Drive cooldown feedback from server-provided retry semantics and fall back to nonprecise '
              'guidance when no stable duration exists.'],
  'exceptions': [],
  'verification': ['Test adaptive limits, device clock changes, and cross-client attempts, verifying no '
                   'fabricated countdown survives authoritative disagreement.'],
  'owner_hints': ['designing-one-time-code-entry'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.recovery-code-consumption-one-time-visible',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Recovery code use must reconcile visibly to its one-time consumption state',
  'statement': 'When recovery codes are single-use, a successful use should mark that code consumed in '
               'management surfaces without exposing the secret value again or leaving it apparently '
               'reusable.',
  'intent': 'Help account owners understand remaining recovery capacity after emergency access.',
  'applies_when': ['The account provides a finite set of one-time recovery codes and users can inspect their '
                   'status later.'],
  'does_not_apply_when': [],
  'failure_modes': ['A used code remains listed as available or the UI regenerates a display of the consumed '
                    'secret as though it can be reused.'],
  'user_impacts': ['Users may store an invalid code for future emergencies or misunderstand whether '
                   'unauthorized use occurred.'],
  'observables': ['Consume a code from one client, then open recovery-code management elsewhere and inspect '
                  'remaining count and code status.'],
  'falsifiers': ['The used code becomes nonreusable authoritatively and management reflects consumption '
                 'without re-exposing the secret.'],
  'repairs': ['Persist one-way recovery-code status and reconcile management views after successful use or '
              'revocation.'],
  'exceptions': [],
  'verification': ['Use codes in different order and across devices, verifying each can succeed at most once '
                   'and remaining capacity stays accurate.'],
  'owner_hints': ['designing-recovery-code-management'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.recovery-code-export-confirmation',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Recovery code copy or download must confirm the scope and storage consequence before secrets '
           'leave the protected view',
  'statement': 'Exporting recovery codes should make clear that the artifact contains reusable '
               'authentication secrets and should not be treated like an ordinary harmless download.',
  'intent': 'Reduce accidental leakage of break-glass credentials while still allowing users to store them '
            'safely.',
  'applies_when': ['The product lets users copy, print, or download recovery codes after generation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A generic Download button writes plaintext codes with no warning, scope confirmation, '
                    'or indication that later viewers of the file can authenticate.'],
  'user_impacts': ['Users can leave long-lived authentication secrets in shared downloads, printers, or '
                   'clipboard history unintentionally.'],
  'observables': ['Generate recovery codes and exercise each export path, inspecting pre-action warning, '
                  'resulting file/clipboard content, and post-action state.'],
  'falsifiers': ['The action explicitly identifies that recovery credentials are being exported and does not '
                 'imply the destination is secure.'],
  'repairs': ['Add a consequence boundary around externalizing secrets and use platform-appropriate secure '
              'handling where available.'],
  'exceptions': [],
  'verification': ['Test copy, file download, print, and shared-device scenarios, verifying secret export '
                   'never looks equivalent to downloading ordinary account data.'],
  'owner_hints': ['designing-recovery-code-management'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.device-switch-preserves-challenge-context',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Switching devices during verification must preserve the challenge purpose or start a clearly new '
           'challenge',
  'statement': 'A user moving from one device to another should never land on an input that accepts a code '
               'for a different action, account, or verification purpose because context was reconstructed '
               'incompletely.',
  'intent': 'Prevent challenge tokens from becoming detached from the operation they are meant to authorize.',
  'applies_when': ['Verification can be initiated on one device and completed through a link, code, or '
                   'continuation on another.'],
  'does_not_apply_when': [],
  'failure_modes': ['The second device opens a generic code form with no bound account or action context and '
                    'accepts a code issued for another pending challenge.'],
  'user_impacts': ['Users can authorize the wrong operation or become vulnerable to cross-purpose challenge '
                   'confusion.'],
  'observables': ['Create multiple simultaneous challenges, move one continuation to another device, and '
                  'submit codes across purposes.'],
  'falsifiers': ['Each continuation resolves to one explicit challenge identity and purpose, with mismatched '
                 'codes rejected without silently switching context.'],
  'repairs': ['Carry signed challenge identity and purpose through handoff rather than rebuilding context '
              'from session defaults.'],
  'exceptions': [],
  'verification': ['Test concurrent login, email-change, and recovery challenges across devices, verifying '
                   'no code can cross purpose boundaries.'],
  'owner_hints': ['designing-one-time-code-entry'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.verification.multiple-active-challenges-bound-to-purpose',
  'domain': 'verification',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Multiple active verification challenges must remain distinguishable by account, purpose, and '
           'destination',
  'statement': 'When several challenges are active, messages and entry surfaces must identify enough context '
               'that a code for one operation is not mistaken for another.',
  'intent': 'Reduce ambiguity without exposing unnecessary sensitive information in verification messages.',
  'applies_when': ['A user can request codes for multiple accounts, destinations, or actions within '
                   'overlapping validity windows.'],
  'does_not_apply_when': [],
  'failure_modes': ['Every message says only “Your code is 123456,” and generic entry screens accept input '
                    'without showing which action is being verified.'],
  'user_impacts': ['Users can submit the wrong code repeatedly or authorize a different pending operation '
                   'than intended.'],
  'observables': ['Start simultaneous challenges for distinct purposes and destinations, then inspect '
                  'message context and each input surface.'],
  'falsifiers': ['Challenges remain purpose-bound in server validation and present enough safe context to '
                 'distinguish the intended operation.'],
  'repairs': ['Attach challenge metadata to both delivery and entry flows and avoid relying solely on code '
              'value uniqueness.'],
  'exceptions': [],
  'verification': ['Exercise overlapping challenge creation and delayed delivery, verifying context remains '
                   'distinguishable until each challenge ends.'],
  'owner_hints': ['designing-one-time-code-entry'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-verification-code-owners-v13'],
  'status': 'active'}]

__all__ = ["VERIFICATION_CODE_RULES_V13"]
