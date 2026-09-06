"""V13 eighth-wave independently authored rules for securitycase."""
from __future__ import annotations

from ._capabilities import interaction_caps


SECURITY_CASE_RULES_V13 = [{'rule_id': 'ui.securitycase.evidence-provenance-immutable',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Security case evidence must preserve immutable provenance from acquisition through review',
  'statement': 'Once evidence is attached to a case, its origin, acquisition time, collector, and '
               'source identity must remain durable even if labels, notes, or presentation metadata are '
               'edited.',
  'intent': 'Protect investigative traceability without preventing analysts from adding interpretation '
            'or organization metadata.',
  'applies_when': ['A security investigation collects logs, files, indicators, screenshots, or external '
                   'evidence into a case.'],
  'does_not_apply_when': [],
  'failure_modes': ['An analyst edits the evidence title and the original source URI and acquisition '
                    'metadata are overwritten by the new display values.'],
  'user_impacts': ['Investigators cannot prove where evidence came from or distinguish later annotation '
                   'from original acquisition context.'],
  'observables': ['Edit evidence labels and descriptions, then compare immutable acquisition metadata '
                  'before and after those changes and in exports.'],
  'falsifiers': ['Presentation edits leave source identity, acquisition time, collector, and original '
                 'provenance unchanged and separately inspectable.'],
  'repairs': ['Separate immutable acquisition provenance from mutable analyst annotations and prevent '
              'UI edits from rewriting the acquisition record.'],
  'exceptions': [],
  'verification': ['Import, annotate, rename, and export evidence while verifying the original '
                   'provenance tuple remains byte-for-byte or semantically stable.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.evidence-redaction-scope-visible',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Evidence redaction must show whether it affects the view, export, or underlying stored '
           'evidence',
  'statement': 'A redaction control must distinguish temporary display masking, export-time redaction, '
               'and destructive modification of stored evidence before the analyst commits it.',
  'intent': 'Prevent privacy controls from misleading investigators about what evidence still exists '
            'and where it remains accessible.',
  'applies_when': ['Case evidence can contain secrets or personal data that require masking or '
                   'redaction for different audiences.'],
  'does_not_apply_when': [],
  'failure_modes': ['An analyst clicks redact on a screenshot, assuming only the shared export changes, '
                    'but the application irreversibly modifies the stored original.'],
  'user_impacts': ['Critical investigative material can be destroyed or sensitive data can remain '
                   'exposed because redaction authority was ambiguous.'],
  'observables': ['Apply each redaction mode and inspect original evidence, analyst view, shared view, '
                  'generated exports, and recovery behavior.'],
  'falsifiers': ['Each redaction operation states its persistence and audience scope, and observed '
                 'outputs match that declared boundary.'],
  'repairs': ['Offer distinct redaction modes with explicit scope and preserve originals where policy '
              'allows rather than overloading one ambiguous action.'],
  'exceptions': [],
  'verification': ['Test view-only masking, export redaction, and destructive redaction, verifying '
                   'scope and reversibility behave exactly as disclosed.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.case-merge-lineage-preserved',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Merging security cases must preserve the identities and lineage of the source cases',
  'statement': 'A merged investigation may present one current workspace, but prior case identities, '
               'ownership, evidence membership, and timeline lineage must remain traceable.',
  'intent': 'Allow consolidation without rewriting investigative history as though separate cases never '
            'existed.',
  'applies_when': ['Analysts can merge duplicate or related security cases into a consolidated '
                   'investigation.'],
  'does_not_apply_when': [],
  'failure_modes': ['After merge, all events are rewritten under the destination case with no '
                    'indication which source case originally contained each item.'],
  'user_impacts': ['Reviewers lose historical context, prior decisions, and evidence boundaries that '
                   'may explain how the investigation evolved.'],
  'observables': ['Merge cases with overlapping and unique evidence, then inspect timeline, exported '
                  'case history, and source-case navigation.'],
  'falsifiers': ['Every source case remains identifiable and each migrated event or artifact retains '
                 'its original lineage plus the merge relationship.'],
  'repairs': ['Represent merge as a durable relationship and migration event rather than renumbering '
              'historical records into the destination case.'],
  'exceptions': [],
  'verification': ['Merge and later review several cases, verifying source identities, evidence '
                   'origins, prior owners, and merge time remain reconstructable.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.export-chain-of-custody-consistent',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Case exports must carry a consistent chain-of-custody record for included evidence',
  'statement': 'When evidence leaves the investigative workspace, the export should identify what was '
               'included, source hashes or identities where available, export actor, time, and '
               'transformation steps.',
  'intent': 'Keep exported investigative packages auditable without pretending that export itself '
            'proves legal admissibility.',
  'applies_when': ['Security cases can be exported for escalation, external review, archival, or '
                   'downstream analysis.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two exports of the same selected evidence contain different files or omit '
                    'transformation history while both are labeled as the complete case package.'],
  'user_impacts': ['Recipients cannot determine whether evidence changed, was omitted, or was '
                   'transformed between workspace and export.'],
  'observables': ['Export the same bounded selection repeatedly and compare manifest membership, '
                  'identifiers, hashes, redactions, exporter, and time metadata.'],
  'falsifiers': ['Each export contains a self-consistent manifest that matches the selected evidence '
                 'and records transformations performed during export.'],
  'repairs': ['Generate an explicit export manifest from the committed selection and evidence metadata, '
              'and bind transformed artifacts to their source identities.'],
  'exceptions': [],
  'verification': ['Create full and redacted exports, then verify manifests reconcile with case '
                   'membership and every included artifact can be traced to its source.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.relationship-links-not-rewrite-history',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Linking cases, entities, and evidence must add relationships without rewriting prior '
           'history',
  'statement': 'Analysts should be able to relate investigations after new context emerges while '
               'preserving the fact that earlier actions occurred before that relationship was known.',
  'intent': 'Maintain temporal truth when investigations are connected retrospectively.',
  'applies_when': ['Case workspaces support linking evidence, entities, alerts, incidents, or other '
                   'cases after investigation has begun.'],
  'does_not_apply_when': [],
  'failure_modes': ['Adding a relationship causes old timeline entries to display as if the linked '
                    'entity had always been associated with the case.'],
  'user_impacts': ['Reviewers can infer knowledge or investigative scope that responders did not '
                   'actually have at the time of earlier decisions.'],
  'observables': ['Add a relationship after several historical events and inspect old timeline entries, '
                  'current graph views, and exports.'],
  'falsifiers': ['The current relationship is visible with its effective or discovery time while '
                 'historical entries keep their original context.'],
  'repairs': ['Store relationship creation as a timestamped event and avoid retroactively injecting '
              'later knowledge into immutable historical renderings.'],
  'exceptions': [],
  'verification': ['Create, remove, and restore links and verify current relationship views change '
                   'without rewriting the chronology of prior case actions.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.access-revocation-effective-immediately',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Revoking security case access must invalidate current authority rather than only future '
           'navigation',
  'statement': 'When a user loses permission to a sensitive investigation, open tabs, cached routes, '
               'and action endpoints must stop granting effective case access according to the product '
               'policy.',
  'intent': 'Prevent permission revocation from being a cosmetic list change while sensitive case data '
            'remains operationally reachable.',
  'applies_when': ['Case membership or role-based permissions can be revoked while a user already has '
                   'the investigation open.'],
  'does_not_apply_when': [],
  'failure_modes': ['A removed analyst disappears from the member list but can continue reading new '
                    'evidence and adding notes from an existing tab.'],
  'user_impacts': ['Sensitive investigation data and actions remain exposed after administrators '
                   'believe access was revoked.'],
  'observables': ['Revoke access from another session and test existing tabs, refreshes, background '
                  'updates, downloads, and mutation endpoints.'],
  'falsifiers': ['All case capabilities reconcile to the revoked authority boundary and the UI does not '
                 'present stale permissions as still valid.'],
  'repairs': ['Enforce authorization server-side for every sensitive read and write, then make clients '
              'respond immediately to revocation events or failures.'],
  'exceptions': [],
  'verification': ['Revoke and restore several permission levels while verifying live sessions converge '
                   'to the current access decision without silent continued authority.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.status-transition-basis-preserved',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Case status transitions must retain the decision basis, actor, and effective time',
  'statement': 'Moving an investigation between open, monitoring, contained, resolved, or other '
               'workflow states should preserve why the transition occurred instead of leaving only the '
               'latest label.',
  'intent': 'Make case state useful as investigative evidence rather than an opaque mutable workflow '
            'field.',
  'applies_when': ['A security case lifecycle contains meaningful transitions that influence response '
                   'ownership and downstream reporting.'],
  'does_not_apply_when': [],
  'failure_modes': ['A case changes from investigating to resolved with no retained reason or actor, '
                    'and a later reopen makes the earlier resolution impossible to reconstruct.'],
  'user_impacts': ['Reviewers cannot distinguish justified resolution from administrative cleanup or '
                   'understand why the case changed direction.'],
  'observables': ['Perform resolve, reopen, monitor, and containment transitions and inspect timeline, '
                  'status history, audit export, and summary surfaces.'],
  'falsifiers': ['Every meaningful status transition records its prior and new state, actor, time, and '
                 'decision basis without erasing earlier transitions.'],
  'repairs': ['Model case status as an append-only transition history with a current state projection '
              'and require rationale where the workflow needs it.'],
  'exceptions': [],
  'verification': ['Cycle a case through several states and verify the current status is correct while '
                   'every transition remains reconstructable.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.securitycase.external-evidence-load-failure-explicit',
  'domain': 'securitycase',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Failures loading externally referenced evidence must remain explicit and must not look like '
           'absent evidence',
  'statement': 'If a case references evidence stored in another service or archive, a retrieval failure '
               'must be distinguished from a case that never had that evidence.',
  'intent': 'Prevent infrastructure failures from silently shrinking the apparent evidence set of an '
            'investigation.',
  'applies_when': ['A case contains links to external logs, object storage, forensic archives, or '
                   'third-party evidence systems.'],
  'does_not_apply_when': [],
  'failure_modes': ['The external source times out and the evidence panel simply omits the item, making '
                    'the case appear to contain fewer artifacts.'],
  'user_impacts': ['Analysts can reach conclusions from an incomplete record without knowing that '
                   'evidence was unavailable rather than nonexistent.'],
  'observables': ['Induce external source timeout, authorization failure, deletion, and partial '
                  'retrieval while inspecting case counts and evidence placeholders.'],
  'falsifiers': ['The case retains the evidence reference and exposes its current retrieval state, '
                 'source, and retry or escalation path.'],
  'repairs': ['Persist external evidence references independently from retrieval success and render '
              'unavailable states as first-class evidence placeholders.'],
  'exceptions': [],
  'verification': ['Test transient and permanent source failures and verify missing, inaccessible, and '
                   'successfully loaded evidence remain semantically distinct.'],
  'owner_hints': ['designing-security-case-evidence-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-security-case-owners-v13'],
  'status': 'active'}]


__all__ = ["SECURITY_CASE_RULES_V13"]
