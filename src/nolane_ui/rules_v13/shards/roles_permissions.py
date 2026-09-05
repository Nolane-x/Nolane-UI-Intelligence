"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

ROLES_PERMISSIONS_RULES_V13 = [{'rule_id': 'ui.roles.assignment-shows-effective-scope',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Role assignment must expose the effective resource scope before confirmation',
  'statement': 'Assigning a role must show which organization, workspace, project, collection, or record scope will '
               'actually receive the authority rather than presenting the role name alone.',
  'intent': 'Prevent operators from granting correct-looking privileges to the wrong resource boundary when role '
            'labels are reused across scopes.',
  'applies_when': ['A role assignment control can target more than one resource boundary or inherit the currently '
                   'selected administrative context.'],
  'does_not_apply_when': [],
  'failure_modes': ['The confirmation shows “Editor” or an equivalent role but omits the resource scope that will '
                    'become authoritative after the assignment.'],
  'user_impacts': ['An administrator can unintentionally grant access to a broader or different workspace than the '
                   'one they meant to modify.'],
  'observables': ['Select two different administrative scopes, open the same role assignment action, and compare the '
                  'confirmation payload and resulting authority.'],
  'falsifiers': ['The confirmation identifies the exact target scope and the committed grant resolves to that same '
                 'scope without hidden expansion.'],
  'repairs': ['Bind the confirmation copy and mutation payload to an explicit resource identifier and display the '
              'human-readable scope alongside the role.'],
  'exceptions': [],
  'verification': ['Assign the same role in multiple nested scopes and verify the shown scope, request payload, and '
                   'effective authorization agree after refresh.'],
  'owner_hints': ['designing-role-management'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.inheritance-source-visible',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inherited permissions must reveal the source relationship that makes them effective',
  'statement': 'When a permission is inherited from a parent group, workspace, organization, policy, or membership, '
               'the UI must distinguish that inherited authority from a direct local grant.',
  'intent': 'Let administrators understand why access exists so they can change the correct policy layer instead of '
            'editing an ineffective local control.',
  'applies_when': ['The authorization model supports inherited, group-based, parent-scope, or policy-derived '
                   'permissions in addition to direct grants.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user appears to have a permission but the interface gives no indication that it comes from a '
                    'parent or group and cannot be removed locally.'],
  'user_impacts': ['Administrators can chase the wrong control, believe a revoke succeeded, or leave unwanted access '
                   'active because the authority source is hidden.'],
  'observables': ['Inspect a user with only inherited authority and compare the permission surface with a user '
                  'holding the same capability through a direct grant.'],
  'falsifiers': ['The interface labels inherited authority and identifies a source relationship or route that '
                 'explains where the effective grant originates.'],
  'repairs': ['Render direct and inherited grants as different states and provide a navigable source reference when '
              'the user has permission to inspect it.'],
  'exceptions': [],
  'verification': ['Create direct and inherited variants of the same capability, attempt local removal, and verify '
                   'the UI explains which source still supplies access.'],
  'owner_hints': ['designing-collaboration-permissions'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.change-preview-shows-capability-delta',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Changing a role must preview the concrete capability delta before it takes effect',
  'statement': 'A role change that adds or removes consequential capabilities must expose the meaningful authority '
               'delta instead of relying on opaque role names such as Basic, Manager, or Custom.',
  'intent': 'Make role transitions reviewable by showing what authority changes, especially when named roles evolve '
            'over time or differ by workspace.',
  'applies_when': ['An administrative flow changes a principal from one predefined or custom role to another with '
                   'materially different capabilities.'],
  'does_not_apply_when': [],
  'failure_modes': ['The operator can confirm a role transition without seeing that it adds export, billing, '
                    'deletion, sharing, approval, or other consequential authority.'],
  'user_impacts': ['A seemingly routine role change can silently broaden or reduce operational access beyond what '
                   'the administrator intended.'],
  'observables': ['Compare the source and destination role capability sets and inspect whether the confirmation '
                  'surface shows the material additions and removals.'],
  'falsifiers': ['The preview presents the relevant capability additions and removals or a precise policy diff '
                 'before the mutation becomes authoritative.'],
  'repairs': ['Compute a capability delta from the effective policies and surface consequential changes rather than '
              'showing only the destination role label.'],
  'exceptions': [],
  'verification': ['Modify role definitions, transition users between roles, and verify the preview reflects the '
                   'current effective capability delta rather than stale documentation.'],
  'owner_hints': ['designing-role-management'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.bulk-update-partial-failure-maps-members',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bulk role updates must map partial failures back to the affected principals',
  'statement': 'When a bulk membership or role operation succeeds for some principals and fails for others, the '
               'result must identify each failed target instead of collapsing the batch into a generic success or '
               'error.',
  'intent': 'Preserve administrative truth after partial authorization or validation failures so operators know '
            'exactly which users still require action.',
  'applies_when': ['A role-management surface can add, remove, or change authority for multiple users, groups, '
                   'service accounts, or teams in one submitted batch.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface reports the batch as completed or failed without identifying the subset whose '
                    'role changes were not committed.'],
  'user_impacts': ['Operators can assume access changed for everyone and leave inconsistent or risky permission '
                   'states unresolved.'],
  'observables': ['Submit a batch containing one valid target and one target engineered to fail authorization or '
                  'validation, then inspect per-principal outcome state.'],
  'falsifiers': ['Every target has a durable success or failure outcome tied to its identity, and retry can be '
                 'scoped to the failed subset.'],
  'repairs': ['Persist per-target mutation results and render a reconciled result table or list instead of reducing '
              'the batch to one boolean status.'],
  'exceptions': [],
  'verification': ['Force mixed outcomes in a multi-member role change and confirm refresh, retry, and audit history '
                   'preserve the same principal-level result mapping.'],
  'owner_hints': ['designing-role-management'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.last-admin-removal-protected',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Removing the last recovery-capable administrator must be prevented or explicitly transferred',
  'statement': 'A role-management flow must not allow the final principal with required administrative or recovery '
               'authority to be removed without a valid replacement or documented break-glass path.',
  'intent': 'Prevent self-inflicted administrative lockout when the authorization model requires at least one '
            'principal capable of restoring access or managing membership.',
  'applies_when': ['The product has an administrative role whose absence would make ordinary account, workspace, or '
                   'organization recovery impossible.'],
  'does_not_apply_when': [],
  'failure_modes': ['The last administrator can demote or remove themselves or another final administrator and leave '
                    'the scope with no standard recovery authority.'],
  'user_impacts': ['The organization can become operationally locked out, requiring support intervention or '
                   'irreversible abandonment of the resource.'],
  'observables': ['Reduce the administrative membership to one eligible principal and attempt to remove or demote '
                  'that final recovery-capable member.'],
  'falsifiers': ['The action is blocked, transferred to a confirmed replacement, or routed through an explicit '
                 'recovery mechanism that preserves administrative continuity.'],
  'repairs': ['Enforce the minimum administrative invariant at the authoritative mutation boundary and explain the '
              'replacement requirement in the UI.'],
  'exceptions': [],
  'verification': ['Exercise demotion, removal, group deletion, and ownership transfer paths when exactly one '
                   'recovery-capable principal remains and confirm none create an unrecoverable scope.'],
  'owner_hints': ['designing-role-management'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.temporary-grant-expiry-visible',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Temporary authority must expose its effective expiry and post-expiry state',
  'statement': 'Time-bounded roles or access grants must display when the authority expires and must reconcile the '
               'interface when that time passes rather than leaving stale privileged controls active.',
  'intent': 'Make temporary access understandable before and after expiry so users do not mistake a time-limited '
            'grant for durable authority.',
  'applies_when': ['A permission, elevation, role, delegation, or sharing grant has an explicit expiry time or lease '
                   'duration.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface shows the principal as privileged without an expiry indication, or continues to '
                    'present privileged actions after the grant is no longer effective.'],
  'user_impacts': ['Users can plan work around authority they no longer possess or assume temporary access will '
                   'persist beyond its intended security window.'],
  'observables': ['Create a short-lived grant, inspect the visible expiry, cross the expiry boundary without '
                  'reloading, and attempt a formerly permitted action.'],
  'falsifiers': ['The expiry is visible in an appropriate time context and the post-expiry UI reconciles to the '
                 'current authority before protected commit.'],
  'repairs': ['Store and render the authoritative grant expiry, subscribe or poll for policy changes where '
              'appropriate, and revalidate action authority at commit.'],
  'exceptions': [],
  'verification': ['Test grants across clock boundaries, reconnects, and long-lived tabs and confirm displayed '
                   'expiry and effective permission remain consistent.'],
  'owner_hints': ['designing-permissions-and-consent'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.revoked-action-stops-before-authoritative-commit',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'A revoked role must stop a stale privileged action before authoritative commit',
  'statement': 'If a principal loses the role required for an in-progress privileged action, the final mutation must '
               'revalidate current authority and must not rely on permission state captured when the flow began.',
  'intent': 'Keep long-running administrative flows bound to current authorization rather than stale UI state or an '
            'earlier page-load decision.',
  'applies_when': ['A privileged workflow can remain open while another administrator or policy system changes the '
                   'acting principal’s role.'],
  'does_not_apply_when': [],
  'failure_modes': ['A stale confirmation or editor can still commit a protected mutation after the acting '
                    'principal’s relevant role has been revoked.'],
  'user_impacts': ['Revocation can appear successful while the revoked user retains a window to execute high-impact '
                   'changes from an already-open flow.'],
  'observables': ['Open a privileged operation, revoke the actor from another session, and then attempt the final '
                  'commit from the stale flow.'],
  'falsifiers': ['The authoritative commit checks current policy and the stale flow transitions to a truthful denied '
                 'or read-only recovery state.'],
  'repairs': ['Move authorization checks to the authoritative mutation boundary and reconcile open privileged flows '
              'when role-change events arrive.'],
  'exceptions': [],
  'verification': ['Repeat the scenario for direct revocation, inherited-role removal, temporary-grant expiry, and '
                   'group-membership loss without reloading the acting client.'],
  'owner_hints': ['designing-collaboration-permissions'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.roles.resource-request-bound-to-target',
  'domain': 'roles',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Permission requests must remain bound to the exact resource and capability requested',
  'statement': 'An access-request flow must identify the target resource and requested capability, and approval must '
               'not silently broaden the request to neighboring resources or a stronger role.',
  'intent': 'Prevent approval ambiguity when request links, notifications, or administrative queues aggregate many '
            'access requests across scopes.',
  'applies_when': ['Users can request access or elevated permissions and another principal can approve or deny the '
                   'request asynchronously.'],
  'does_not_apply_when': [],
  'failure_modes': ['An approver sees a generic “grant access” request whose target resource or requested capability '
                    'is unclear or differs from the resulting grant.'],
  'user_impacts': ['Approvers can grant unintended authority because the approval UI loses the context that made the '
                   'original request acceptable.'],
  'observables': ['Submit requests for two resources or capability levels, open them from notifications and queues, '
                  'and compare displayed context with committed grants.'],
  'falsifiers': ['Each request carries immutable target and capability context through approval, and the resulting '
                 'grant cannot exceed that context without a new explicit decision.'],
  'repairs': ['Persist target resource and requested capability as request identity fields and render them at every '
              'approval boundary.'],
  'exceptions': [],
  'verification': ['Approve, deny, and reopen requests from multiple entry points and verify target, capability, '
                   'requester, and resulting grant remain aligned.'],
  'owner_hints': ['designing-permissions-and-consent'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-role-permission-owners-v13'],
  'status': 'active'}]

__all__ = ["ROLES_PERMISSIONS_RULES_V13"]
