"""V13 seventh-wave independently authored rules for incident response."""
from __future__ import annotations

from ._capabilities import interaction_caps


INCIDENT_RESPONSE_RULES_V13 = [{'rule_id': 'ui.incident.severity-current-state-visible',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Incident severity must show current authoritative level separately from historical changes',
  'statement': 'An incident interface should distinguish the currently effective severity from prior '
               'declared levels and preserve who changed it and when.',
  'intent': 'Keep response urgency aligned with current command state without erasing escalation history.',
  'applies_when': ['Incidents can be promoted or downgraded during response.'],
  'does_not_apply_when': [],
  'failure_modes': ['A timeline shows several severity badges but the header remains stale or a downgrade '
                    'rewrites history as though the incident was always lower severity.'],
  'user_impacts': ['Responders can allocate the wrong urgency or lose evidence of escalation decisions.'],
  'observables': ['Change severity from multiple sessions and compare header, timeline, notifications, and '
                  'exported incident history.'],
  'falsifiers': ['One current severity is authoritative and every transition remains visible as historical '
                 'evidence with actor and time.'],
  'repairs': ['Model severity transitions as durable events plus a current state pointer, and reconcile all '
              'response surfaces from that authority.'],
  'exceptions': [],
  'verification': ['Race escalation and downgrade, verifying current severity converges while transition '
                   'history remains append-only.'],
  'owner_hints': ['designing-incident-severity-declaration'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.responder-role-handoff-visible',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Incident role handoffs must identify the new accountable responder and handoff time',
  'statement': 'When incident commander, communications lead, investigator, or other response roles '
               'transfer, the interface must make the effective owner transition explicit.',
  'intent': 'Prevent duplicate command or unattended responsibilities during shift and escalation changes.',
  'applies_when': ['Incident response assigns named operational roles that can be transferred during an '
                   'active event.'],
  'does_not_apply_when': [],
  'failure_modes': ['A new commander begins acting but the incident header still shows the old person or '
                    'both clients believe they own the role.'],
  'user_impacts': ['Responders can issue conflicting decisions or critical tasks can fall between owners.'],
  'observables': ['Transfer roles under concurrent sessions and inspect role roster, timeline, permissions, '
                  'and notification targets.'],
  'falsifiers': ['Exactly one authoritative holder is shown for exclusive roles, with handoff history and '
                 'effective time preserved.'],
  'repairs': ['Commit role transfer atomically and update current roster plus incident timeline from the '
              'same event.'],
  'exceptions': [],
  'verification': ['Exercise shift changes and failed transfer attempts, verifying accountability never '
                   'becomes ambiguous.'],
  'owner_hints': ['designing-responder-role-assignment'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.timeline-event-source-and-time-visible',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Incident timeline entries must distinguish event occurrence time from record-entry time and '
           'source',
  'statement': 'A response timeline should preserve when an event actually occurred, when it was recorded, '
               'and whether the source is human observation, monitoring, automation, or imported evidence '
               'when those differ.',
  'intent': 'Support accurate reconstruction without treating late-entered notes as events that happened at '
            'entry time.',
  'applies_when': ['Incident timelines combine automatic signals and manually backfilled observations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A responder adds “database failed at 10:02” at 10:30 and the timeline orders it only by '
                    'entry time with no source distinction.'],
  'user_impacts': ['Post-incident analysis can reconstruct the wrong causal sequence and response latency.'],
  'observables': ['Add backdated manual evidence and live automated events, then inspect ordering, labels, '
                  'and export.'],
  'falsifiers': ['Occurrence time and record time are independently available where needed, and source '
                 'attribution survives editing.'],
  'repairs': ['Store event-time, recorded-time, and source metadata explicitly and define the timeline '
              'sort/visualization contract.'],
  'exceptions': [],
  'verification': ['Test clock-skewed sources and backfill, verifying the interface never implies more '
                   'temporal certainty than the evidence provides.'],
  'owner_hints': ['designing-incident-timeline-capture'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.hypothesis-distinct-from-confirmed-finding',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Incident hypotheses must remain visually and semantically distinct from confirmed findings',
  'statement': 'Suspected causes and investigative ideas should not be promoted into confirmed root cause '
               'merely because they are repeated, assigned, or added to the main incident view.',
  'intent': 'Preserve epistemic status during fast-moving investigations.',
  'applies_when': ['Responders record hypotheses, observations, evidence, and confirmed findings during '
                   'incident analysis.'],
  'does_not_apply_when': [],
  'failure_modes': ['A note labelled “possible database saturation” appears in the summary as the root cause '
                    'before supporting evidence establishes it.'],
  'user_impacts': ['Teams may take harmful remediation or communicate unsupported claims to stakeholders.'],
  'observables': ['Create competing hypotheses with mixed evidence and inspect summary, timeline, handoff, '
                  'and postmortem promotion behavior.'],
  'falsifiers': ['Hypotheses retain their provisional state until an explicit evidence-backed transition '
                 'marks a finding confirmed or rejected.'],
  'repairs': ['Model investigation claims with explicit status and evidence links rather than inferring '
              'truth from placement or popularity.'],
  'exceptions': [],
  'verification': ['Exercise promotion, rejection, and reopened hypotheses, verifying every surface '
                   'preserves current epistemic status and history.'],
  'owner_hints': ['designing-incident-hypothesis-evidence-logs'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.acknowledged-alert-owner-visible',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Acknowledged alerts must show who owns follow-up rather than using acknowledgement as a generic '
           'resolved state',
  'statement': 'Acknowledging an incident-related alert should indicate the accountable responder or queue '
               'and remain distinct from mitigation or resolution.',
  'intent': 'Prevent acknowledgement from being mistaken for completed response work.',
  'applies_when': ['Alerts can be acknowledged, assigned, investigated, and later resolved as part of '
                   'incident operations.'],
  'does_not_apply_when': [],
  'failure_modes': ['One click changes an alert from New to green Acknowledged with no owner, causing other '
                    'responders to assume someone else is handling it.'],
  'user_impacts': ['Critical investigation can stall because acknowledgement removed attention without '
                   'establishing accountability.'],
  'observables': ['Acknowledge alerts with and without assignment, then inspect alert queue, incident view, '
                  'and responder roster.'],
  'falsifiers': ['Acknowledgement retains a distinct lifecycle state and exposes follow-up ownership or '
                 'explicitly unowned status.'],
  'repairs': ['Separate acknowledgement timestamp from assignment and resolution fields, and show all three '
              'according to workflow.'],
  'exceptions': [],
  'verification': ['Test reassignment and unacknowledge/reopen paths, verifying owner and lifecycle state '
                   'remain independently truthful.'],
  'owner_hints': ['designing-alert-triage-workspaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.runbook-step-execution-state-visible',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Runbook steps must distinguish planned, started, succeeded, failed, skipped, and rolled-back '
           'execution states',
  'statement': 'Incident runbook UIs should reflect actual step execution rather than marking a checklist '
               'complete merely because a responder opened or checked an instruction.',
  'intent': 'Keep operational procedure evidence aligned with what systems and responders actually did.',
  'applies_when': ['Incident response uses runbooks with manual or automated steps and tracks progress.'],
  'does_not_apply_when': [],
  'failure_modes': ['A responder checks a step before an automation fails, yet the runbook shows it '
                    'completed with no failed execution evidence.'],
  'user_impacts': ['Later responders can assume mitigation occurred and skip a required corrective action.'],
  'observables': ['Execute runbook steps with success, failure, cancellation, manual skip, and rollback '
                  'while comparing checklist and execution logs.'],
  'falsifiers': ['Each step state corresponds to its actual execution lifecycle and manual attestations are '
                 'distinguished from automated outcomes.'],
  'repairs': ['Model runbook step intent and execution attempts separately, attaching outputs and failure '
              'state to each attempt.'],
  'exceptions': [],
  'verification': ['Repeat failed and retried steps, verifying current status plus attempt history remain '
                   'understandable during handoff.'],
  'owner_hints': ['designing-runbook-execution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.merged-incident-identity-preserved',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Merging duplicate incidents must preserve source identities and redirect participants to one '
           'authoritative parent',
  'statement': 'When two incident records are merged, links, timelines, and responders must reconcile to a '
               'canonical incident while retaining the fact that separate records once existed.',
  'intent': 'Avoid split response after deduplication and preserve historical evidence provenance.',
  'applies_when': ['Incident operations can identify duplicate or related incident records and merge them.'],
  'does_not_apply_when': [],
  'failure_modes': ['One record disappears while old links still open an active-looking duplicate or its '
                    'timeline events lose their source identity in the merged incident.'],
  'user_impacts': ['Responders can continue coordinating in two places or misattribute evidence after the '
                   'merge.'],
  'observables': ['Merge active incidents with separate responders and events, then open old links and '
                  'inspect canonical timeline and role ownership.'],
  'falsifiers': ['Old identifiers resolve to the canonical incident or an explicit merged state, and '
                 'imported events retain source provenance.'],
  'repairs': ['Persist alias/merge relationships and migrate active workflow references transactionally '
              'rather than copying content and deleting the source.'],
  'exceptions': [],
  'verification': ['Test notifications, bookmarks, and API-linked views after merge, verifying no obsolete '
                   'incident remains independently actionable.'],
  'owner_hints': ['designing-incident-response-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.incident.postmortem-linked-to-closed-incident',
  'domain': 'incident',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Postmortems must remain linked to the exact incident state they analyze',
  'statement': 'A postmortem should identify the incident and relevant closure revision or timeline scope so '
               'later incident edits do not make the analysis appear to cover evidence added afterward.',
  'intent': 'Preserve the relationship between retrospective conclusions and the evidence set available when '
            'they were written.',
  'applies_when': ['Closed incidents can receive late notes, severity corrections, or merged evidence after '
                   'a postmortem begins.'],
  'does_not_apply_when': [],
  'failure_modes': ['The postmortem references only a mutable incident URL and silently appears to include '
                    'timeline data that was added after review.'],
  'user_impacts': ['Readers may attribute later evidence or changed severity to the original analysis '
                   'incorrectly.'],
  'observables': ['Create a postmortem, add late incident evidence, and compare linked scope, timeline '
                  'references, and later postmortem revision.'],
  'falsifiers': ['The postmortem identifies its incident and can distinguish evidence known at authoring '
                 'from later additions or explicit updates.'],
  'repairs': ['Link postmortem revisions to stable incident identity plus evidence/timeline revision '
              'metadata where the product supports retrospective traceability.'],
  'exceptions': [],
  'verification': ['Add late events and reopen/close the incident, verifying postmortem provenance remains '
                   'interpretable rather than silently rewriting history.'],
  'owner_hints': ['designing-postmortem-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-incident-response-owners-v13'],
  'status': 'active'}]

__all__ = ["INCIDENT_RESPONSE_RULES_V13"]
