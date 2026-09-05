"""V13 seventh-wave independently authored rules for audit log."""
from __future__ import annotations

from ._capabilities import interaction_caps


AUDIT_LOG_RULES_V13 = [{'rule_id': 'ui.audit.event-actor-identity-preserved',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Audit events must preserve the authoritative actor identity after account changes',
  'statement': 'An audit event must retain the actor identity that was authoritative when the event occurred '
               'rather than silently relabeling historical actions after a user is renamed, removed, merged, '
               'or deactivated.',
  'intent': 'Keep historical accountability stable even when the current directory representation of the '
            'actor changes later.',
  'applies_when': ['The product records user, service-account, automation, or administrator actions in a '
                   'durable audit history.'],
  'does_not_apply_when': [],
  'failure_modes': ['An old event is rendered using only the actor’s current mutable display record, so a '
                    'rename or account merge changes who the historical action appears to belong to.'],
  'user_impacts': ['Investigators can attribute an action to the wrong principal or lose the ability to '
                   'distinguish identities that were separate at event time.'],
  'observables': ['Record an event, rename or deactivate the actor, then reopen the historical event and '
                  'compare stable actor identifiers with displayed attribution.'],
  'falsifiers': ['The historical entry retains an immutable actor identifier and can show current display '
                 'metadata without rewriting the event-time identity.'],
  'repairs': ['Persist actor identity fields with the event and render current directory data as '
              'supplemental metadata rather than replacing event-time attribution.'],
  'exceptions': [],
  'verification': ['Create events before and after actor rename, deactivation, and identity merge, then '
                   'verify historical attribution remains distinguishable and stable.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.event-target-scope-visible',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Audit records must identify the exact resource scope affected by each action',
  'statement': 'A consequential audit entry must expose the organization, workspace, project, object, or '
               'policy scope that was actually mutated instead of presenting an action label without its '
               'authoritative target boundary.',
  'intent': 'Make audit review useful when the same action and object names can exist in multiple '
            'administrative scopes.',
  'applies_when': ['The same action type can be performed against similarly named resources in more than one '
                   'scope or tenant.'],
  'does_not_apply_when': [],
  'failure_modes': ['An event says that a record was changed or deleted but omits the parent scope needed to '
                    'distinguish which similarly named resource was affected.'],
  'user_impacts': ['Operators can investigate the wrong workspace or conclude that an action touched a '
                   'broader or narrower boundary than it actually did.'],
  'observables': ['Perform the same mutation against identically named resources in two scopes and compare '
                  'the resulting audit entries.'],
  'falsifiers': ['Each event identifies a stable target and sufficient parent scope to distinguish the '
                 'affected resource from same-named alternatives.'],
  'repairs': ['Persist target identifiers and scope lineage with the event, and expose that context in the '
              'event detail or navigable target reference.'],
  'exceptions': [],
  'verification': ['Generate same-named targets across scopes, mutate each, and verify audit navigation '
                   'lands on the correct resource or explains that it no longer exists.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.timestamp-timezone-and-ordering-visible',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Audit timelines must expose timestamp basis when ordering can cross time zones or clocks',
  'statement': 'Audit history must distinguish the authoritative event timestamp from localized presentation '
               'and must not imply a total order from ambiguous local times or untrusted client clocks.',
  'intent': 'Prevent investigators from reconstructing an incorrect sequence when events originate across '
            'regions, clients, or daylight-saving transitions.',
  'applies_when': ['Audit events may originate on multiple clients or services and are displayed to users in '
                   'a locale or time zone.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI sorts events by a localized or client-supplied time that can repeat, jump, or '
                    'disagree with authoritative server ordering without disclosing that basis.'],
  'user_impacts': ['An investigator can infer that one security or administrative action preceded another '
                   'when the evidence does not support that conclusion.'],
  'observables': ['Generate events around a time-zone or DST boundary and from a client with a skewed clock, '
                  'then inspect sort order and timestamp labels.'],
  'falsifiers': ['The UI uses an authoritative ordering key, shows a disambiguated time basis, and treats '
                 'client-originated time as metadata rather than ordering authority.'],
  'repairs': ['Store server or ledger ordering information separately from reported client time and localize '
              'presentation without discarding the underlying time-zone or offset context.'],
  'exceptions': [],
  'verification': ['Exercise cross-zone and clock-skew cases, then verify exported and on-screen order agree '
                   'on the same authoritative sequence.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.before-after-value-diff-preserved',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Audit changes must preserve enough before-and-after state to explain the material mutation',
  'statement': 'When an audit event represents a configuration or policy change, its detail must expose the '
               'material fields that changed rather than reducing the event to a generic “updated” label.',
  'intent': 'Allow reviewers to determine what actually changed without relying on current state, which may '
            'have been edited again later.',
  'applies_when': ['A mutable configuration, permission, policy, or record can be changed repeatedly and the '
                   'audit system claims to record those updates.'],
  'does_not_apply_when': [],
  'failure_modes': ['The event records only that an update occurred, while the changed values are '
                    'unavailable or reconstructed from the resource’s later current state.'],
  'user_impacts': ['Reviewers cannot establish which setting caused an incident or distinguish a benign '
                   'update from a consequential one.'],
  'observables': ['Change one field, then several fields, then change them again; inspect whether each '
                  'historical event retains its own field-level transition.'],
  'falsifiers': ['The event retains the relevant old and new values or an equivalent immutable patch whose '
                 'meaning survives subsequent edits.'],
  'repairs': ['Capture material change payloads at commit time, redact only where required, and render a '
              'field-aware difference instead of consulting present-day state.'],
  'exceptions': [],
  'verification': ['Replay a sequence of conflicting edits and verify every audit entry still explains its '
                   'own mutation after the resource has changed again.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.filter-export-scope-consistent',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Exported audit data must preserve the effective filter scope shown before export',
  'statement': 'When users export a filtered audit view, the generated artifact must reflect the effective '
               'time range, actors, event types, and resource filters or clearly declare a different export '
               'scope before generation.',
  'intent': 'Prevent compliance or incident evidence packages from silently containing a broader or narrower '
            'population than the reviewed screen.',
  'applies_when': ['An audit viewer supports filters and an export or download action from the filtered '
                   'result set.'],
  'does_not_apply_when': [],
  'failure_modes': ['The screen shows a narrowed result set but the exported file defaults to all events, a '
                    'different date range, or stale filters without warning.'],
  'user_impacts': ['A reviewer can submit an incomplete or overbroad evidence set while believing it matches '
                   'the view they inspected.'],
  'observables': ['Apply several filters, export, and compare the artifact population and metadata with the '
                  'exact effective filter model on screen.'],
  'falsifiers': ['The export either matches the effective filtered population or explicitly previews the '
                 'alternate scope and records it in artifact metadata.'],
  'repairs': ['Bind export job parameters to the same canonical filter object used by the viewer and include '
              'that scope in export metadata.'],
  'exceptions': [],
  'verification': ['Test combinations of filters, saved views, and reset actions, then verify artifact rows '
                   'and declared scope remain consistent with the final effective query.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.pagination-does-not-drop-events',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Audit pagination must not lose or duplicate events when new records arrive concurrently',
  'statement': 'Navigating a growing audit log must use stable event identity and cursor semantics so '
               'inserts that occur between page requests do not cause older events to disappear or reappear '
               'across pages.',
  'intent': 'Preserve evidentiary completeness in long histories that continue receiving events while an '
            'investigator browses them.',
  'applies_when': ['The audit history is paginated or incrementally loaded while new events can be appended '
                   'during the browsing session.'],
  'does_not_apply_when': [],
  'failure_modes': ['Offset-based paging over a changing result set causes an event to shift across page '
                    'boundaries and be skipped or returned twice.'],
  'user_impacts': ['An investigator may miss a consequential action or waste time reconciling duplicate '
                   'entries that are artifacts of pagination.'],
  'observables': ['Load one page, create new events before requesting the next page, then enumerate stable '
                  'event IDs across the combined browsing session.'],
  'falsifiers': ['Every event in the requested historical window appears at most once and no event is '
                 'skipped because of concurrent inserts ahead of the cursor.'],
  'repairs': ['Use a stable cursor based on authoritative event ordering and identity, and define whether '
              'the browsing snapshot is fixed or live.'],
  'exceptions': [],
  'verification': ['Inject events between successive page loads at several boundaries and compare the '
                   'collected IDs with an authoritative query over the same scope.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.redaction-preserves-event-meaning',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Audit redaction must hide sensitive values without erasing the meaning of the recorded action',
  'statement': 'When an audit field must be masked for privacy or secret handling, the event should still '
               'communicate which field or class of value changed and why details are unavailable.',
  'intent': 'Balance least disclosure with the need to understand that a consequential action occurred and '
            'what category of state it affected.',
  'applies_when': ['Audit payloads can contain secrets, personal data, tokens, message content, or other '
                   'values that some viewers are not authorized to inspect.'],
  'does_not_apply_when': [],
  'failure_modes': ['Redaction replaces an entire event with an opaque placeholder, making a password '
                    'rotation, key change, recipient update, and unrelated edit indistinguishable.'],
  'user_impacts': ['Authorized reviewers with limited data access cannot reconstruct event meaning and may '
                   'overlook a security-relevant transition.'],
  'observables': ['View the same event with full and restricted audit permissions and compare whether the '
                  'restricted representation retains action type and field identity.'],
  'falsifiers': ['Restricted viewers cannot recover protected values but can still distinguish the '
                 'operation, target field category, actor, time, and outcome where policy permits.'],
  'repairs': ['Apply field-level masking and explanatory redaction labels rather than discarding the '
              'surrounding event structure.'],
  'exceptions': [],
  'verification': ['Exercise events containing secrets and personal fields under multiple audit roles, '
                   'verifying disclosure decreases without collapsing distinct actions into identical '
                   'records.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.audit.correlation-identity-stable-across-views',
  'domain': 'audit',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Correlated audit events must keep a stable operation identity across summary and detail views',
  'statement': 'Events that belong to one transaction, request, job, or administrative operation must expose '
               'a stable correlation identity so grouping, drill-down, and export do not create '
               'contradictory event membership.',
  'intent': 'Let investigators follow multi-event operations without guessing which records belong to the '
            'same causal action.',
  'applies_when': ['One user action or backend operation emits multiple audit events across services, '
                   'resources, or lifecycle stages.'],
  'does_not_apply_when': [],
  'failure_modes': ['The summary groups events by a transient label or timestamp proximity, while detail and '
                    'export use different membership and no stable correlation key is exposed.'],
  'user_impacts': ['Reviewers can incorrectly combine unrelated actions or split one operation into separate '
                   'incidents.'],
  'observables': ['Trigger a multi-stage operation with concurrent unrelated events, then compare group '
                  'membership in timeline, detail, search, and export surfaces.'],
  'falsifiers': ['All surfaces resolve the same stable correlation identifier or explicitly state that '
                 'causal grouping is unavailable rather than inferring it heuristically.'],
  'repairs': ['Persist and expose operation or trace correlation identifiers at event creation, with '
              'fallback to independent events when no authoritative relationship exists.'],
  'exceptions': [],
  'verification': ['Create interleaved multi-service operations and confirm correlation membership stays '
                   'identical through filters, refresh, drill-down, and export.'],
  'owner_hints': ['designing-audit-log-interfaces'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-audit-log-owners-v13'],
  'status': 'active'}]

__all__ = ["AUDIT_LOG_RULES_V13"]
