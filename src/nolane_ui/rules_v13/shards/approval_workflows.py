"""V13 seventh-wave independently authored rules for approval workflows."""
from __future__ import annotations

from ._capabilities import interaction_caps


APPROVAL_WORKFLOW_RULES_V13 = [{'rule_id': 'ui.approval.decision-bound-to-request-version',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Approval decisions must bind to the exact request version that was reviewed',
  'statement': 'An approval must identify the immutable request, document, configuration, or payload version '
               'that the approver saw, and later edits must not inherit that earlier decision silently.',
  'intent': 'Prevent approval authority from being reused after the subject of the decision changes '
            'materially.',
  'applies_when': ['A request can be edited, recalculated, regenerated, or otherwise versioned while an '
                   'approval workflow is active.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reviewer approves version A, the requester changes material fields to version B, and '
                    'the system still treats the old approval as authorizing the new content.'],
  'user_impacts': ['Unreviewed financial, operational, or release changes can become authoritative under a '
                   'decision made about different data.'],
  'observables': ['Open an approval, modify the request from another session before and after decision, then '
                  'inspect the version referenced by the final approved state.'],
  'falsifiers': ['The decision records the reviewed version, and a material update either invalidates the '
                 'decision or requires a policy-defined reaffirmation.'],
  'repairs': ['Attach approval records to immutable request revisions and compute invalidation from explicit '
              'material-change policy rather than current row identity.'],
  'exceptions': [],
  'verification': ['Approve then mutate each consequential field class and verify the final workflow never '
                   'attributes the original approval to an unreviewed revision.'],
  'owner_hints': ['designing-approval-workflows'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.approver-authority-current-at-decision',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Approval commit must verify the approver still holds required authority',
  'statement': 'The system must re-evaluate approval permission at decision time rather than assuming that '
               'an approver who opened the task or was assigned earlier still has current authority.',
  'intent': 'Close the gap between stale workflow assignment and the actual authorization boundary at the '
            'moment a consequential decision is committed.',
  'applies_when': ['Approver roles or delegations can be revoked or expire while approval tasks remain '
                   'open.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user opens an approval while authorized, loses the required role, and can still '
                    'submit an authoritative approval from the stale screen.'],
  'user_impacts': ['Revoked or expired principals can authorize spending, access, release, or policy changes '
                   'after administrators believe that authority ended.'],
  'observables': ['Open a pending approval, remove the approver’s permission elsewhere, then attempt approve '
                  'and reject actions without refreshing the original client.'],
  'falsifiers': ['The server rejects decisions that no longer satisfy the policy and the client reconciles '
                 'the task instead of showing a false successful approval.'],
  'repairs': ['Authorize at commit time against the current principal, target scope, and approval policy, '
              'and invalidate stale action controls on denial.'],
  'exceptions': [],
  'verification': ['Revoke, expire, and change approval roles during open tasks and confirm no stale client '
                   'can commit a decision outside current authority.'],
  'owner_hints': ['designing-approval-workflows'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.delegation-source-visible',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Delegated approval authority must identify who delegated it and its effective limits',
  'statement': 'When an approval is performed under delegated authority, the interface must distinguish the '
               'acting approver from the delegation source and expose meaningful scope or expiry '
               'constraints.',
  'intent': 'Make delegated decisions auditable and prevent users from interpreting borrowed authority as '
            'permanent direct ownership.',
  'applies_when': ['The workflow supports temporary substitutes, delegated approvers, acting roles, or '
                   'manager-on-behalf-of decisions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A delegated approver appears identical to a direct approver, with no indication of the '
                    'delegator, covered request scope, or delegation lifetime.'],
  'user_impacts': ['Reviewers can misread accountability and administrators may not recognize that an '
                   'expired or overbroad delegation enabled a decision.'],
  'observables': ['Create direct and delegated approval paths for the same request and inspect decision '
                  'detail, task assignment, and audit representations.'],
  'falsifiers': ['Delegated decisions identify the acting principal, delegation source, and relevant scope '
                 'or expiry without exposing unauthorized private details.'],
  'repairs': ['Persist delegation context on the decision and render it distinctly from direct role '
              'authority.'],
  'exceptions': [],
  'verification': ['Exercise overlapping and expired delegations, then verify every decision resolves to the '
                   'correct source and effective constraints.'],
  'owner_hints': ['designing-approval-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.rejection-reason-preserved',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Rejection reasons must remain attached to the rejected revision and next action',
  'statement': 'A rejection that requires explanation must preserve the reviewer’s reason with the rejected '
               'request revision and surface it to the person responsible for remediation.',
  'intent': 'Turn rejection into actionable workflow evidence instead of a transient notification that '
            'disappears before correction.',
  'applies_when': ['The product asks approvers for a rejection reason, comment, or requested change and '
                   'supports resubmission.'],
  'does_not_apply_when': [],
  'failure_modes': ['The rejection reason exists only in a toast or activity feed, is detached from the '
                    'rejected revision, or disappears when the request is edited for resubmission.'],
  'user_impacts': ['Requesters can repeat the same problem, and later reviewers cannot determine why a prior '
                   'revision was denied.'],
  'observables': ['Reject a request with a reason, navigate away, edit and resubmit, then inspect history '
                  'and the remediation surface.'],
  'falsifiers': ['The original rejection retains its reason and revision identity, while the active revision '
                 'exposes the relevant unresolved feedback until addressed or superseded.'],
  'repairs': ['Store rejection feedback as workflow state linked to the decision and revision rather than '
              'ephemeral client copy.'],
  'exceptions': [],
  'verification': ['Perform multiple reject-edit-resubmit cycles and confirm each reason stays attributable '
                   'to the correct revision and reviewer.'],
  'owner_hints': ['designing-review-feedback-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.multi-stage-order-and-gate-state-visible',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Multi-stage approvals must expose which gates are complete, active, blocked, or still required',
  'statement': 'A staged approval flow must represent the actual gate sequence and current blocking stage '
               'rather than collapsing all reviewers into a flat list of names or checkmarks.',
  'intent': 'Help participants understand why a request cannot advance and which authority still controls '
            'the next transition.',
  'applies_when': ['A request requires serial, conditional, or role-specific approvals before it can reach '
                   'its final state.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface shows several approvers but does not reveal that finance cannot act until '
                    'security approves, or that one conditional gate became required after data changed.'],
  'user_impacts': ['Users chase the wrong reviewer or believe the workflow is complete while a hidden gate '
                   'still blocks execution.'],
  'observables': ['Create workflows with serial and conditional stages, then inspect task visibility and '
                  'summary state before and after each decision.'],
  'falsifiers': ['The UI distinguishes completed, current, skipped-by-policy, blocked, and pending stages in '
                 'the same order the workflow engine enforces.'],
  'repairs': ['Render stage state from the authoritative workflow graph and include policy-derived skipped '
              'or newly required gates explicitly.'],
  'exceptions': [],
  'verification': ['Exercise conditional branches and role changes, verifying visual stage state always '
                   'matches the engine’s permitted next transition.'],
  'owner_hints': ['designing-multi-stage-approval'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.concurrent-decisions-reconciled',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Concurrent approval decisions must reconcile to one authoritative workflow outcome',
  'statement': 'When multiple approvers act at nearly the same time, each client must reconcile against the '
               'committed decision model instead of retaining contradictory local success states.',
  'intent': 'Prevent split-brain approval history where different reviewers believe mutually exclusive '
            'outcomes became effective.',
  'applies_when': ['A stage allows several authorized reviewers or a request can be approved and withdrawn, '
                   'rejected, or superseded concurrently.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two clients submit conflicting decisions and both continue showing their own action as '
                    'final even though only one transition won or the policy combines them differently.'],
  'user_impacts': ['Teams can execute work based on an approval that was never authoritative or overlook a '
                   'valid rejection.'],
  'observables': ['Open the same request in multiple sessions and submit conflicting decisions within the '
                  'same concurrency window, then refresh all views.'],
  'falsifiers': ['Every client converges on the same decision set and policy outcome, with losing or '
                 'superseded attempts represented accurately rather than as successful final state.'],
  'repairs': ['Use versioned workflow transitions or idempotent decision records and reconcile clients from '
              'authoritative workflow history after conflict.'],
  'exceptions': [],
  'verification': ['Race approve/reject/withdraw actions repeatedly and verify summaries, task queues, audit '
                   'history, and downstream actions converge identically.'],
  'owner_hints': ['designing-approval-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.withdrawal-invalidates-pending-actions',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Withdrawing or superseding a request must invalidate stale approval actions',
  'statement': 'Once a request is withdrawn, cancelled, or replaced, open approval screens must stop '
               'permitting decisions that target the obsolete request instance.',
  'intent': 'Prevent stale reviewer tabs from reviving or authorizing work the requester has explicitly '
            'removed from consideration.',
  'applies_when': ['Approval tasks may remain open in multiple sessions while the requester can withdraw or '
                   'supersede the request.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reviewer can approve an obsolete task after withdrawal because the client action '
                    'still posts successfully against a stale identifier.'],
  'user_impacts': ['Cancelled expenses, access requests, or releases can unexpectedly resume under authority '
                   'applied to a request that should be dead.'],
  'observables': ['Open an approval in one client, withdraw or supersede it elsewhere, then submit from the '
                  'stale reviewer screen.'],
  'falsifiers': ['The stale decision is rejected or clearly recorded as non-authoritative and the reviewer '
                 'is shown the request’s terminal or superseded state.'],
  'repairs': ['Validate request lifecycle and version at decision commit, and push or fetch invalidation '
              'state into open approval clients.'],
  'exceptions': [],
  'verification': ['Test withdrawal before, during, and immediately after review submission to verify '
                   'obsolete tasks never transition back to approved.'],
  'owner_hints': ['designing-approval-workflows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.approval.bulk-mixed-outcomes-map-requests',
  'domain': 'approval',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bulk approval actions must report per-request outcomes when the batch partially succeeds',
  'statement': 'A multi-request approve or reject operation must preserve each request’s result when '
               'eligibility, authority, validation, or concurrency causes mixed outcomes.',
  'intent': 'Keep reviewers from assuming a whole queue moved when only a subset satisfied the approval '
            'policy.',
  'applies_when': ['An approval inbox allows one action to target multiple selected requests.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface reports “8 approved” or a generic error even though some selected '
                    'requests were stale, unauthorized, or rejected by validation.'],
  'user_impacts': ['Users may perform downstream work for requests that remain pending or waste time '
                   'reopening items that did succeed.'],
  'observables': ['Select requests with deliberately mixed eligibility and submit one bulk decision, then '
                  'compare result state by stable request ID.'],
  'falsifiers': ['Each selected request receives a durable outcome and failed items can be retried or '
                 'inspected without replaying successful decisions.'],
  'repairs': ['Execute bulk decisions as per-request transitions with reconciled result mapping rather than '
              'reducing the batch to one boolean.'],
  'exceptions': [],
  'verification': ['Force authorization, stale-version, and validation failures inside one batch and verify '
                   'the final queue and audit records map every outcome correctly.'],
  'owner_hints': ['designing-bulk-administration'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-approval-workflow-owners-v13'],
  'status': 'active'}]

__all__ = ["APPROVAL_WORKFLOW_RULES_V13"]
