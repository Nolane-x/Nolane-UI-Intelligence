---
name: designing-multi-stage-approval
description: Use when approval requires sequential, parallel, conditional or quorum-based stages and the interface must expose progress, blockers, dependencies, skipped stages, delegation and policy changes without flattening everything into one pending status.
---

# Designing Multi-Stage Approval

## Parent Contract
**Required parent:** `designing-approval-workflows`.

This specialist owns orchestration and visualization of multiple approval stages. The semantics of each individual approval decision remain inherited from the parent.

## Decision Model
Represent the workflow as a graph of stages, not a decorative progress stepper. A stage may be sequential, parallel, any-of, all-of, quorum, conditional or automatically satisfied by policy. Define activation conditions, eligible approvers, completion rule, failure/rejection rule and what downstream stages depend on it.

The UI must distinguish **not started**, **blocked**, **active**, **partially approved**, **completed**, **skipped/not applicable**, **rejected**, **expired** and **superseded**. Greyed-out future steps are not enough when users need to know whether a stage is waiting on evidence, waiting on another stage or excluded by a branch condition.

Parallel approvals need aggregate truth. “2 of 3 approved” differs from a quorum where only two are required. A rejection may block immediately or coexist with a majority rule; expose the actual rule rather than inferring from counts.

Policy changes mid-flight need versioning. Adding a new approval stage to the organization policy should not silently rewrite the historical meaning of already approved requests. Define whether in-flight requests migrate, grandfather or restart and show the applicable policy version/rationale.

Delegation/escalation should retain original responsibility and decision provenance. A delegated approval is not the same as changing the workflow owner retroactively.

## Failure Topology
- Stepper marks a conditional stage “complete” when it was actually skipped.
- “2/3” appears green although policy requires all three approvals.
- Parallel rejection does not visibly block downstream work, so users wait on impossible stages.
- Policy update inserts a new approver into historical requests and makes old approvals look incomplete.
- Delegation replaces the original approver name and loses the audit trail.
- Request revision invalidates one stage but UI leaves downstream stages green.

## Falsification and Recovery
Falsify with sequential + parallel branches, quorum, conditional skips, rejection, delegation, policy version changes, subject revision changes and expired stages. Derive rendered progress from the workflow graph and event history. If the visual step state cannot be reproduced from those facts, it fails.

Recover by explicitly modeling stage rules/status, versioning policy, distinguishing skipped from approved and recalculating downstream validity when upstream evidence or subject revision changes.

## Output Contract
Return `multi-stage-approval-contract` with stage graph, activation/dependency rules, quorum/parallel semantics, status vocabulary, policy version, revision invalidation, delegation/escalation provenance, progress visualization and graph-state tests.