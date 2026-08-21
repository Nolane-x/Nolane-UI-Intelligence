---
name: designing-agent-tool-permission-escalation
description: Use when an agent reaches a step that requires broader tool permissions, stronger credentials, additional data access, or a more privileged execution mode and the UI must explain the delta without normalizing blanket escalation.
---

# Designing Agent Tool Permission Escalation

## Escalation boundary
Permission escalation is not an error state and not a generic approval prompt. It is a request to widen the authority available to an agent or tool beyond the current envelope. This skill owns how that delta is represented, justified, constrained, and either granted or denied without losing prior progress.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent establishes the initial autonomy and permission envelope. This specialist activates when current execution cannot continue without additional authority.

## Describe the delta, not the whole universe
An escalation request should identify the exact capability missing: write instead of read, production instead of staging, one repository instead of all repositories, one contact instead of the full address book, temporary secret access instead of persistent credentials. The decision owner is the least-privilege expansion that can satisfy the blocked obligation.

Represent `(current_capabilities, requested_delta, reason, affected_step, resources, duration, reuse, revocation, alternative_path)`. Do not replace the current scope with an opaque larger role. If the system’s underlying provider exposes coarse permissions, say so and show the practical blast radius rather than presenting them as narrower than they are.

## Timing and context
Ask at the moment the permission is needed, but before dispatch. Bind the request to the plan or action that triggered it. A permission prompt detached from context encourages automatic consent. If a task can continue with a safer degraded path, show that alternative and its consequence.

Persistent escalation deserves a stronger treatment than one-time capability. Make duration and future reuse visible. Credential installation, organization-wide grants, or permission changes affecting other agents should not be smuggled through the same lightweight UI as a single action approval.

## Evidence
Evidence includes the prior capability set, requested delta, provider-native permission names, user-facing explanation, approving principal, expiry, revocation path, and the executions that consume the new grant. When a provider returns broader capability than requested, record the mismatch and either reject or explicitly surface it.

## Failure modes
Characteristic Failure includes “Allow access” prompts that hide read/write differences, broad OAuth grants represented as task-local permission, escalation requested after execution already began, permissions retained beyond the stated duration, and denial that causes the agent to loop the same prompt. Another failure is privilege laundering: one tool delegates to another privileged service without a new visible boundary.

## Falsification
Test a provider that offers only coarse scopes, a request whose affected resource changes before approval, denial followed by a degraded path, expiry mid-run, and a sub-agent that attempts to reuse the grant. The contract fails if broader-than-requested authority is silently accepted, if approval attaches to changed semantics, if privilege survives its promised lifetime, or if the UI cannot show what new capability became available.

## Recovery
On denial, preserve completed work and either re-plan around the missing capability or mark the affected obligation blocked. On over-broad provider grants, avoid proceeding until the user understands the actual scope. On accidental persistent escalation, revoke where possible, record actions performed under it, and refresh agent context so cached authority does not linger.

## Output and Handoff
Output: `agent-tool-permission-escalation-contract`, containing permission delta, provider mapping, least-privilege policy, context binding, duration, alternatives, revocation, and evidence. Handoff exact authorization semantics to approval-scope boundaries and later scope checks to approval-scope drift.

## Sibling Boundary and delete-the-skill
Sibling approval-scope design defines what an approval authorizes once presented. This skill decides how a new permission requirement is derived and surfaced from a blocked tool step. The delete-the-skill test passes because without a dedicated escalation owner, agent products tend to convert capability gaps into vague blanket permission prompts.