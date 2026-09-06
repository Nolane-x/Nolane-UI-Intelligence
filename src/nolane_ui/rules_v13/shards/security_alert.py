"""V13 eighth-wave independently authored rules for securityalert."""
from __future__ import annotations

from ._capabilities import interaction_caps


SECURITY_ALERT_RULES_V13 = [{'rule_id': 'ui.securityalert.source-event-identity-preserved',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Security alerts must preserve the identity of every contributing source event',
  'statement': 'An alert may aggregate detections, but the interface must retain stable source-event '
               'identities so an analyst can inspect exactly which observations created the alert.',
  'intent': 'Keep triage evidence traceable even when alerts are deduplicated, regrouped, enriched, or '
            'reassigned.',
  'applies_when': ['An alert is derived from one or more detector, log, sensor, or correlation events.'],
  'does_not_apply_when': [],
  'failure_modes': ['Alert enrichment replaces event references with a summary count, so later review '
                    'cannot determine which exact events originally contributed.'],
  'user_impacts': ['Analysts can close or escalate a case on evidence that cannot be reconstructed or '
                   'independently checked.'],
  'observables': ['Open an alert before and after regrouping and compare the source-event identifiers, '
                  'timestamps, and links exposed to the analyst.'],
  'falsifiers': ['Every contributing event remains addressable by a stable identity and its '
                 'relationship to the alert survives regrouping.'],
  'repairs': ['Store alert membership as durable event references and render summaries as views over '
              'that membership rather than replacements for it.'],
  'exceptions': [],
  'verification': ['Force deduplication and enrichment updates, then verify the same contributing event '
                   'set can still be enumerated and opened.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.status-distinct-from-resolution',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Alert workflow status must remain distinct from incident resolution or evidence disposition',
  'statement': 'Triage labels such as new, acknowledged, investigating, or closed must not silently '
               'imply that the underlying security condition has been remediated.',
  'intent': 'Prevent queue-management actions from overstating the operational outcome of a security '
            'investigation.',
  'applies_when': ['Security alerts have workflow states that can change independently from remediation '
                   'of the detected condition.'],
  'does_not_apply_when': [],
  'failure_modes': ['An analyst closes an alert as duplicate and the UI presents the protected asset as '
                    'remediated even though no remediation action occurred.'],
  'user_impacts': ['Responders can believe risk has been removed when only the alert queue was '
                   'administratively cleared.'],
  'observables': ['Change alert workflow state without changing remediation records and compare queue '
                  'badges, case summaries, and asset posture surfaces.'],
  'falsifiers': ['Queue status and remediation or disposition state are separately named and can '
                 'diverge without one overwriting the other.'],
  'repairs': ['Model triage state, evidence disposition, and remediation state as separate authorities '
              'and label them explicitly wherever surfaced.'],
  'exceptions': [],
  'verification': ['Exercise duplicate, benign-positive, remediated, and unresolved closures and verify '
                   'each state retains its independent meaning.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.suppression-scope-visible',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Alert suppression must expose the exact matcher, scope, and expiration that will be applied',
  'statement': 'Before an analyst suppresses recurring alerts, the UI must reveal which rule, entities, '
               'tenants, time window, and conditions the suppression will affect.',
  'intent': 'Keep noise-reduction controls from hiding security signals outside the analyst’s intended '
            'boundary.',
  'applies_when': ['A triage workflow can create suppressions, exclusions, mutes, or temporary '
                   'exceptions from an alert.'],
  'does_not_apply_when': [],
  'failure_modes': ['A mute action is labeled only “suppress similar alerts” and later hides detections '
                    'from unrelated hosts because its effective scope was broader than the preview.'],
  'user_impacts': ['Legitimate attacks can become invisible because an analyst could not see the '
                   'authority of the suppression being created.'],
  'observables': ['Preview a suppression, then inspect the generated matcher and test alerts just '
                  'inside and outside each declared boundary.'],
  'falsifiers': ['The preview and persisted suppression agree on matcher, entities, time bounds, '
                 'ownership scope, and expiry behavior.'],
  'repairs': ['Compile suppression intent into an inspectable condition set and require confirmation '
              'against the effective scope before activation.'],
  'exceptions': [],
  'verification': ['Create narrow and broad suppressions, generate boundary-case alerts, and verify '
                   'only events matching the confirmed scope are muted.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.severity-recalculation-history-visible',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Severity recalculation must preserve prior values and the evidence that caused each change',
  'statement': 'When enrichment or analyst review changes alert severity, the interface should show the '
               'current authoritative value without erasing the previous level and its basis.',
  'intent': 'Let responders understand why urgency changed instead of treating severity as an '
            'unexplained mutable badge.',
  'applies_when': ['Alert severity can be recalculated by policy, new telemetry, correlation, or '
                   'analyst action.'],
  'does_not_apply_when': [],
  'failure_modes': ['An alert silently moves from medium to critical after correlation, but the analyst '
                    'cannot see when the change occurred or which evidence justified it.'],
  'user_impacts': ['Response prioritization can be distrusted or reconstructed incorrectly during '
                   'incident review.'],
  'observables': ['Add and remove evidence that affects severity and inspect the alert timeline, '
                  'current badge, and exported history.'],
  'falsifiers': ['The current severity converges correctly while each prior severity and change basis '
                 'remains visible as history.'],
  'repairs': ['Represent severity changes as attributed transitions and derive the current value from '
              'the latest effective transition.'],
  'exceptions': [],
  'verification': ['Trigger automated and manual severity changes, then verify current priority and '
                   'historical rationale remain consistent across surfaces.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.dedup-preserves-contributing-evidence',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Deduplicating alerts must not discard evidence that differs between the merged detections',
  'statement': 'Collapsing repeated detections into one alert is acceptable only if unique indicators, '
               'entities, timestamps, and detector evidence from every member remain inspectable.',
  'intent': 'Reduce queue noise without converting evidence diversity into a misleading single '
            'exemplar.',
  'applies_when': ['The alerting system groups repeated or correlated detections into a consolidated '
                   'triage object.'],
  'does_not_apply_when': [],
  'failure_modes': ['Deduplication keeps only the first detection payload, so a later member containing '
                    'a different host or indicator disappears from analyst view.'],
  'user_impacts': ['Analysts can miss lateral spread or scope changes because the merged alert hides '
                   'evidence that was not identical.'],
  'observables': ['Generate several deduplicated members with intentionally different entities and '
                  'indicators, then inspect the consolidated evidence list.'],
  'falsifiers': ['Every unique contributing fact remains discoverable and the summary never claims '
                 'members are identical when they are not.'],
  'repairs': ['Merge presentation around a durable member collection and summarize common fields while '
              'retaining non-common evidence per member.'],
  'exceptions': [],
  'verification': ['Deduplicate heterogeneous members and verify the analyst can reconstruct each '
                   'contribution and its unique fields.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.assignment-handoff-atomic',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Alert assignment handoff must move accountability atomically between analysts or queues',
  'statement': 'When triage ownership is transferred, the interface must converge on one effective '
               'owner and record the handoff instead of briefly or permanently showing competing '
               'authorities.',
  'intent': 'Avoid abandoned or doubly-owned security work during reassignment and shift changes.',
  'applies_when': ['Alerts can be assigned, reassigned, or moved between analysts, teams, and '
                   'operational queues.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two analysts reassign the same alert concurrently and each client shows a '
                    'different owner, while notifications continue routing to both.'],
  'user_impacts': ['Critical alerts can be neglected or duplicated because accountability is no longer '
                   'trustworthy.'],
  'observables': ['Race reassignment from multiple sessions and compare owner badges, queue membership, '
                  'notifications, and audit history.'],
  'falsifiers': ['Exactly one current assignment is authoritative after reconciliation and every '
                 'attempted handoff has a clear outcome.'],
  'repairs': ['Use a versioned or transactional assignment transition and derive all '
              'ownership-dependent surfaces from that committed state.'],
  'exceptions': [],
  'verification': ['Run concurrent reassignments and failed transfers, verifying ownership converges '
                   'without losing the prior or new accountable party.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.bulk-close-scope-confirmed',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bulk alert closure must confirm the evaluated selection scope rather than only the visible '
           'rows',
  'statement': 'Closing many alerts at once must state whether the action targets selected IDs, the '
               'current filtered result set, or an all-results scope, including items outside the '
               'viewport.',
  'intent': 'Prevent destructive triage actions from affecting more alerts than the analyst reviewed.',
  'applies_when': ['The alert queue supports multi-select or bulk close across pagination, '
                   'virtualization, or active filters.'],
  'does_not_apply_when': [],
  'failure_modes': ['An analyst selects all visible high-confidence benign alerts and the action closes '
                    'every alert matching a broader saved filter, including unseen items.'],
  'user_impacts': ['Unreviewed security signals can be removed from operational attention without '
                   'informed confirmation.'],
  'observables': ['Change filters and pagination after selection, then inspect the close confirmation '
                  'and the exact IDs affected.'],
  'falsifiers': ['The confirmation names the effective selection semantics and the committed closure '
                 'set matches that disclosed scope exactly.'],
  'repairs': ['Bind bulk actions to an immutable evaluated target set or require an explicit '
              'all-filtered-results choice with count and filter summary.'],
  'exceptions': [],
  'verification': ['Test page-only, cross-page, and filtered-all selection modes and compare previewed '
                   'counts to the final closed alert identities.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securityalert.stale-alert-state-reconciled',
  'domain': 'securityalert',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Stale alert views must reconcile before committing actions that depend on current triage '
           'state',
  'statement': 'If an alert changes elsewhere, actions such as assign, close, suppress, or escalate '
               'must not execute against an obsolete state without surfacing the conflict.',
  'intent': 'Keep analyst decisions attached to the alert state they actually reviewed.',
  'applies_when': ['Multiple analysts or automations can mutate an alert while another analyst keeps an '
                   'older view open.'],
  'does_not_apply_when': [],
  'failure_modes': ['An analyst closes an old copy of an alert after another responder escalated it, '
                    'and the stale closure silently overwrites the newer investigation state.'],
  'user_impacts': ['Fresh investigative work or ownership can be lost because a stale client was '
                   'treated as authoritative.'],
  'observables': ['Open the same alert in two sessions, mutate it in one, then attempt state-dependent '
                  'actions from the stale session.'],
  'falsifiers': ['The stale session refreshes, rejects, or explicitly reconciles the conflict before '
                 'any destructive state transition is committed.'],
  'repairs': ['Attach versions to state-dependent commands and surface a conflict path that preserves '
              'the newer authoritative alert state.'],
  'exceptions': [],
  'verification': ['Race close, assign, suppress, and escalate operations across sessions and verify '
                   'stale commands cannot silently overwrite newer state.'],
  'owner_hints': ['designing-security-alert-triage'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-alert-owners-v13'],
  'status': 'active'}]


__all__ = ["SECURITY_ALERT_RULES_V13"]
