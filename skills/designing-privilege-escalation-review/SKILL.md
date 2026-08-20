---
name: designing-privilege-escalation-review
description: Use when analysts must review changes or uses of privilege across accounts, roles, groups, tokens, processes, and cloud entitlements and distinguish legitimate administration from suspicious escalation.
---
# Designing Privilege Escalation Review

## Parent Contract

**Required parent:** `designing-security-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the review surface for privilege changes and privilege use. Decide how before/after authority, actor, target, grant mechanism, duration, approval, session context, inherited permissions, and resulting capabilities are made inspectable. This faculty distinguishes “permission changed,” “privilege exercised,” and “effective privilege increased” as different events. It does not design RBAC administration generally and does not decide whether an attack path is exploitable end to end.

## Inputs and evidence

Require identity and resource identifiers, role/group memberships, entitlement inheritance, policy evaluations, sudo/elevation events, token scopes, process integrity/elevation, cloud role assumptions, privilege start/end time, actor and approver, ticket/change references, session/device context, administrative tooling source, baseline privilege, and audit-log provenance. Include temporary elevation, nested group membership, service principals, break-glass accounts, just-in-time roles, privilege inherited through ownership, and permissions that remain after an intended expiry.

## Procedure

Begin with effective authority, not only the named role. Show what the subject could do before, what changed, and what new capabilities became possible. Represent direct grants separately from inherited or transitive access. For temporary elevation, expose requested duration, actual activation, expiry, and any lingering tokens or sessions. Link a privilege change to the session or process that requested and used it when possible; a legitimate admin grant followed by anomalous use may still be security-relevant. Make approval provenance explicit without equating approval with safety. Provide comparison against normal peer or account behavior only when the baseline has enough evidence. For suspicious events, let analysts pivot to affected resources and downstream actions without losing the original grant context.

## Failure topology

- The UI shows a role name but not the capabilities that role actually grants.
- Nested groups hide a transitive privilege increase.
- Temporary access appears expired while cached tokens remain valid.
- An approved change is automatically classified benign.
- Privilege use and privilege assignment are merged, obscuring whether the new authority was exercised.
- Service principals are judged with human-user baseline assumptions.
- The interface shows current permissions while investigating a historical event and rewrites the past.

## Falsification

Test a nested-group escalation, just-in-time admin role, break-glass account, cloud role assumption, local process elevation, a permission that expires but leaves an active session, and an approved grant followed by unusual resource access. The design fails if analysts cannot reconstruct effective before/after authority, inheritance, temporal validity, and evidence of actual privilege use.

## Output contract

Return `privilege-escalation-review-contract` containing effective-authority model, direct/inherited grant distinction, temporal privilege lifecycle, session/token continuation, approval provenance, privilege-use linkage, historical-state rules, baseline caveats, and investigation scenarios.

## Handoffs

Role administration itself routes to `designing-role-management` and `designing-rbac-matrices`; attack reachability routes to `designing-attack-path-visualization`; authentication context routes to `designing-authentication-anomaly-review`; entity pivots route to `designing-security-entity-investigation`. This skill owns security review of changing or exercised authority, not generic permission editing.