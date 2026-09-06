"""V13 eighth-wave independently authored rules for marketplace dispute."""
from __future__ import annotations

from ._capabilities import interaction_caps


MARKETPLACE_DISPUTE_RULES_V13 = [{'rule_id': 'ui.dispute.deadline-authority-visible',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dispute deadlines must expose their authoritative source and effective cutoff',
  'statement': 'Appeal and evidence deadlines can come from providers or policy engines and must '
               'not be inferred from local display time alone.',
  'intent': 'Prevent parties from missing a deadline because the UI hides its authority or '
            'timezone basis.',
  'applies_when': ['A dispute has evidence, response, appeal, or escalation deadlines.'],
  'does_not_apply_when': [],
  'failure_modes': ['The case screen says “2 days left” but omits a provider cutoff already less '
                    'than 36 hours away.'],
  'user_impacts': ['A party can lose review rights despite acting within the apparent window.'],
  'observables': ['Compare provider deadline data, local timezone display, countdowns, '
                  'notifications, and action availability near cutoff.'],
  'falsifiers': ['The exact cutoff, timezone, and owning authority are inspectable and action '
                 'availability follows that same deadline.'],
  'repairs': ['Persist provider/policy deadline identity and compute countdowns from the '
              'authoritative instant.'],
  'exceptions': [],
  'verification': ['Test before, at, and after cutoff from multiple zones and verify the same '
                   'authority governs UI and backend acceptance.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.evidence-submission-receipt-preserved',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Submitted dispute evidence must receive a durable receipt tied to the exact payload',
  'statement': 'Upload progress is not proof that evidence became part of the dispute record; '
               'successful submission needs immutable acknowledgment.',
  'intent': 'Give users proof of what evidence the dispute system actually accepted.',
  'applies_when': ['Parties submit documents, images, or statements to a dispute case.'],
  'does_not_apply_when': [],
  'failure_modes': ['Files show 100% uploaded, the page closes, and later the provider reports no '
                    'evidence because the final submit failed.'],
  'user_impacts': ['A party can lose a case without knowing evidence was never accepted.'],
  'observables': ['Submit multiple evidence items under retries and network interruptions, then '
                  'inspect case history and provider receipt.'],
  'falsifiers': ['Accepted evidence has a stable receipt or event linking exact items and '
                 'submission time; failed items remain visibly unsubmitted.'],
  'repairs': ['Separate file transfer from case submission and store the authoritative receipt '
              'with item identifiers.'],
  'exceptions': [],
  'verification': ['Interrupt after upload but before submit, retry, and verify receipts map '
                   'exactly to accepted evidence once.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.partial-refund-distinct-from-dispute-resolution',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Partial refunds must not be presented as final dispute resolution',
  'statement': 'A refund can reduce exposure without resolving responsibility, remaining amount, '
               'appeal rights, or provider case status.',
  'intent': 'Prevent operators and parties from mistaking money movement for case closure.',
  'applies_when': ['A dispute can coexist with partial or provisional refunds.'],
  'does_not_apply_when': [],
  'failure_modes': ['A 30% refund causes the case badge to switch to “resolved” although the '
                    'provider dispute remains open for the remaining amount.'],
  'user_impacts': ['Users may stop responding or miss deadlines while the case is still active.'],
  'observables': ['Create partial/full refunds across open, won, lost, and appealed disputes and '
                  'inspect both financial and case state.'],
  'falsifiers': ['Refund amount/state and dispute lifecycle remain separate and can represent all '
                 'valid combinations.'],
  'repairs': ['Model refund transactions independently from dispute resolution and display '
              'remaining disputed exposure.'],
  'exceptions': [],
  'verification': ['Exercise partial refunds before and after case decisions and verify neither '
                   'lifecycle overwrites the other.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.party-identity-stable',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dispute party identity must remain stable across account profile changes',
  'statement': 'Case evidence and decisions must stay bound to the party identity at issue even if '
               'display names, emails, or account metadata change later.',
  'intent': 'Preserve who participated in the dispute without relying on mutable profile labels.',
  'applies_when': ['Buyer, seller, or external-party account attributes can change during a '
                   'dispute.'],
  'does_not_apply_when': [],
  'failure_modes': ['A seller renames its store and historical evidence now appears to have been '
                    'submitted by a different-looking party with no immutable identifier.'],
  'user_impacts': ['Reviewers can misattribute statements or decisions.'],
  'observables': ['Change party profile metadata during an open case and inspect historical '
                  'events, exports, and provider mappings.'],
  'falsifiers': ['Historical events retain stable party identifiers while current labels may '
                 'update with clear identity continuity.'],
  'repairs': ['Store immutable party references on dispute events and render current labels as '
              'presentation metadata, not identity keys.'],
  'exceptions': [],
  'verification': ['Rename and merge profile metadata and verify event authorship and provider '
                   'party mapping remain unchanged.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.evidence-access-scope-visible',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dispute evidence access must show which parties and reviewers can view each item',
  'statement': 'Evidence can contain sensitive material and may have party-specific or '
               'internal-only visibility; access scope must not be implicit.',
  'intent': 'Prevent accidental disclosure and false assumptions about what the other party can '
            'see.',
  'applies_when': ['A dispute system supports evidence with different visibility scopes.'],
  'does_not_apply_when': [],
  'failure_modes': ['An operator uploads an internal fraud note into the same evidence list as '
                    'buyer-visible documents without a scope label.'],
  'user_impacts': ['Sensitive analysis can be disclosed or parties may rely on evidence they '
                   'cannot actually access.'],
  'observables': ['Create public, counterparty-visible, provider-only, and internal evidence and '
                  'inspect every role and export.'],
  'falsifiers': ['Each item exposes its effective access class and unauthorized roles cannot '
                 'retrieve or infer hidden content.'],
  'repairs': ['Model evidence visibility explicitly and enforce it at retrieval as well as '
              'presentation.'],
  'exceptions': [],
  'verification': ['Switch roles and export paths, verifying each item is visible only to the '
                   'disclosed audience.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.status-and-appeal-path-visible',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dispute status must expose whether an appeal or next review path remains available',
  'statement': 'A closed-looking status can still permit appeal, escalation, or reconsideration; '
               'the next allowable path and deadline should be explicit.',
  'intent': 'Keep users from treating a reviewable decision as final or attempting impossible '
            'actions.',
  'applies_when': ['Dispute workflows have decisions that may be appealed or escalated.'],
  'does_not_apply_when': [],
  'failure_modes': ['A case says “lost” with no indication that an appeal is available for three '
                    'more days.'],
  'user_impacts': ['The party may miss a valid escalation path or open duplicate support cases.'],
  'observables': ['Move cases through initial decision, appeal eligibility, appealed, final '
                  'decision, and expired appeal states.'],
  'falsifiers': ['Status, available next action, and deadline remain mutually consistent at every '
                 'stage.'],
  'repairs': ['Represent appeal eligibility as an explicit state derived from decision authority '
              'and deadline.'],
  'exceptions': [],
  'verification': ['Test all decision outcomes and deadline boundaries, verifying only valid next '
                   'paths are offered and disclosed.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.provider-decision-import-reconciled',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Imported provider decisions must reconcile with local case state before actions '
           'continue',
  'statement': 'External dispute providers can update asynchronously; local state must not '
               'continue offering actions based on an older decision.',
  'intent': 'Prevent local workflow from contradicting the authoritative provider outcome.',
  'applies_when': ['Case status is synchronized from an external dispute or payment provider.'],
  'does_not_apply_when': [],
  'failure_modes': ['The provider marks a dispute won, but the local UI still permits evidence '
                    'submission because its last sync said “under review.”'],
  'user_impacts': ['Users can perform invalid or confusing actions after the authority already '
                   'changed state.'],
  'observables': ['Delay provider webhooks, import out-of-order decisions, and inspect action '
                  'availability before and after reconciliation.'],
  'falsifiers': ['Local state converges to the provider decision monotonically or flags a '
                 'reconciliation conflict instead of silently regressing.'],
  'repairs': ['Store provider event/version identity and reconcile imported decisions against '
              'local transitions before enabling actions.'],
  'exceptions': [],
  'verification': ['Replay delayed and duplicate provider events and verify final local state and '
                   'available actions match authoritative ordering.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.dispute.merge-lineage-preserved',
  'domain': 'dispute',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Merged dispute cases must preserve lineage to every original case and evidence record',
  'statement': 'Merging related disputes for review must not erase original identifiers, '
               'deadlines, or evidence provenance.',
  'intent': 'Keep consolidated investigation from destroying reconstructable case history.',
  'applies_when': ['Operations allow duplicate or related dispute cases to be merged.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two disputes are merged and the surviving case silently adopts one deadline '
                    'while evidence from the other loses its source case.'],
  'user_impacts': ['Reviewers cannot reconstruct which provider case or deadline governed each '
                   'event.'],
  'observables': ['Merge cases with different events and deadlines, then inspect history, exports, '
                  'and direct links to original identifiers.'],
  'falsifiers': ['The merged view retains immutable source-case lineage and never rewrites '
                 'original event identity.'],
  'repairs': ['Represent merge as a relationship over preserved cases rather than destructive '
              'record replacement.'],
  'exceptions': [],
  'verification': ['Merge and later unmerge or audit cases, verifying every original identifier, '
                   'event, and evidence source remains traceable.'],
  'owner_hints': ['designing-marketplace-dispute-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-dispute-owners-v13'],
  'status': 'active'}]

__all__ = ["MARKETPLACE_DISPUTE_RULES_V13"]
