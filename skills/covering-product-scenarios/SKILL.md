---
name: covering-product-scenarios
description: Use when individual feature flows are insufficient and the product must prove cross-feature, role, lifecycle, interruption, responsive, permission, recovery, and concurrent scenarios.
---

# Covering Product Scenarios

## Parent Contract
**Required parent:** `designing-task-flows`.

Consume task-flow models, capability/action registries, product states, actor profiles, and reachability evidence. The parent owns local task-flow structure; this faculty owns **coverage across feature boundaries and operating conditions**.

## Decision Boundary
A scenario is an end-to-end product situation with an actor goal, starting state, contextual constraints, a sequence of capabilities/actions, expected observations, and acceptable recovery. It may cross pages, devices, permissions, async boundaries, sessions, or features. This skill does not invent every possible combinatorial path. It selects a risk- and consequence-based set sufficient to expose gaps that single-screen reviews miss.

## Product Truth
AI tends to design features independently: upload works, search works, permissions work, history works. Real users combine them. They upload while storage is near quota, search an archived item, follow a notification after access was revoked, retry a payment after a timeout, resize a dashboard while a drawer is open, edit content that a collaborator moved, or return to a wizard after session expiration. Failures often sit **between** two locally correct features.

Completeness therefore needs scenario coverage. It is not “test everything.” It is a disciplined map of critical journeys, cross-feature handoffs, state transitions, and failure/recovery combinations that must be represented in design and evidence.

## Decision Model
1. **Seed from user outcomes.** For each primary actor outcome, create happy-path scenarios that exercise the canonical capabilities needed to complete it.
2. **Add lifecycle variants.** Empty/first-run, populated, loading, offline/degraded, read-only, archived, expired, conflict, and recovery states materially alter which actions exist. Include applicable variants rather than assuming the populated online state.
3. **Cross feature boundaries.** Select scenarios where one feature hands state to another: search → detail → edit; notification → permission check → object; import → validation → correction → publish; dashboard → filter → export; create → share → revoke.
4. **Exercise authority changes.** Include insufficient permission, permission granted mid-flow, permission revoked mid-session, role switching, tenant/workspace switching, and external/shared access where relevant.
5. **Exercise interruption.** Navigate away, close/reopen, refresh, background/foreground, network loss, duplicated submit, cancel, browser back, native back, or concurrent change. Specify what must persist, roll back, warn, or resume.
6. **Exercise destructive and transactional paths.** Confirmation, optimistic state, failure after apparent success, retry, undo, idempotency, receipt/history, and post-action navigation require explicit scenarios.
7. **Exercise responsive/platform transformations.** A scenario should survive required viewport/platform changes without silently losing an action. Mobile does not need identical layout, but must preserve required capability semantics.
8. **Exercise alternative modalities.** For keyboard-critical, remote, touch, voice, assistive technology, drag/drop, or gesture-heavy work, select scenarios that prove an equivalent operable path.
9. **Prioritize by risk.** Score frequency, consequence, irreversibility, novelty, dependency complexity, authority sensitivity, and history of failure. High-risk scenario gaps block; low-risk exhaustive permutations may remain out of scope with rationale.
10. **Bind to evidence obligations.** Each scenario names expected checkpoints that later runtime verification can observe. “User can complete onboarding” is too vague; identify action and state transitions that prove completion.

## Evidence
Use product requirements, support incidents, analytics funnels, bug history, existing tests, domain hazards, permission matrices, and real workflows. External best practices can suggest scenario classes but cannot substitute product truth. When no implementation exists, a clickable/stateful prototype plus explicit spec can provide design evidence, but runtime status remains unknown.

Coverage quality is measured by meaningful failure classes, not scenario count. One well-designed permission-revocation scenario can reveal more than twenty duplicated happy paths. Keep a reason for each scenario so future agents know what risk it protects.

## Output Contract
Return `scenario-coverage` with:
- `scenarios[] {id, actor, goal, start_state, constraints, capability_ids, action_sequence, expected_states, recovery_expectations, modalities, priority, evidence_obligations}`
- `coverage_matrix {capabilities, roles, lifecycle_states, consequence_classes, platforms, modalities}`
- `cross_feature_handoffs[]`
- `uncovered_risks[] {risk, reason, disposition}`
- `blocked_scenarios[]`
- `status: PASS|FAIL|UNKNOWN`

Every release-critical capability must appear in at least one scenario appropriate to its actor and consequence. Critical cross-feature handoffs need explicit coverage, not implied adjacency.

## Failure Traps
- Duplicating task-flow diagrams and calling them scenarios.
- Generating a Cartesian explosion of every state × role × viewport with no risk model.
- Testing only happy paths because error states are “implementation details.”
- Treating permission denial as a dead end rather than a designed scenario with explanation/recovery.
- Ignoring second-session behavior, refresh, or backgrounding for long-lived tasks.
- Assuming responsive coverage because individual screenshots exist at three widths.
- Testing drag/drop only with pointer while the same product promises keyboard accessibility.
- Letting a successful optimistic update end the scenario before server failure can be observed.
- Omitting cross-feature handoffs because each feature owner has its own flow.

**Hard gate:** a product-wide completion claim cannot pass when a release-critical capability or high-consequence handoff has no scenario that could falsify it.

## V6 Scenario Coverage Protocol
Use **scenario cross-product pruning** to select interaction combinations by causal distinctness and risk rather than brute-force every axis. Maintain a **lifecycle edge inventory** for first use, empty, normal, loading, partial, stale, error, recovery, archived/deleted, permission change, offline/reconnect, and migration states where applicable.

Include every **rare-high-impact scenario** whose consequence warrants evidence despite low frequency. Vary **role-permission variance** across owner/admin/member/guest/operator/approver or domain equivalents. Track a **coverage frontier** of still-uncertain intersections and why they are deferred.

### Falsification
Search for a valid product state/action pair not represented by the scenario set and ask whether it can change implementation or safety. If yes, “covered” is false.

### Recovery
Add the minimal causally distinct scenario, route its owners/verifiers, and update the frontier rather than inflating a huge undifferentiated checklist.
