---
name: designing-agent-run-branching
description: Use when a user or agent can fork an in-progress or completed run into alternate continuations and the UI must preserve shared history, branch-local state, side effects, approvals, and comparison without merging incompatible realities.
---

# Designing Agent Run Branching

## Branching semantics
Branching creates more than another chat thread. It creates a new execution lineage whose future assumptions, tool calls, artifacts, and permissions may diverge while still sharing an ancestral state. This skill owns the branch model: what is inherited, what is copied, what remains globally shared, and what must be revalidated before the new branch can act.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent defines how much action authority an agent may exercise. This specialist activates when the product supports alternate execution paths derived from a common run history.

## Ancestry and branch-local truth
Represent a branch with `(branch_id, ancestor_checkpoint, inherited_artifacts, local_mutations, external_side_effects, approval_lineage, status)`. Conversation history may be inherited as context, but external side effects already performed before the fork remain facts shared by all descendants. A branch cannot pretend those actions did not happen merely because its local narrative diverges.

Distinguish copy-on-write artifacts from shared resources. Editing a branch-local draft may safely diverge; editing a live external document may affect sibling branches. The interface must show when an operation targets shared reality rather than branch-local state.

## Fork rules
A fork point should be a stable checkpoint, not an arbitrary partial event unless the runtime can reconstruct exact state there. Pending or outcome-unknown operations complicate branching: either reconcile them before forking or mark them as shared unresolved ancestors that every branch must account for.

Approvals do not automatically clone. If approval was bound to an intent or plan revision, a branch that changes that intent needs a new authorization. Cached tool results may be inherited only when their validity conditions still hold.

## Comparing and selecting branches
Users need to compare branch outcomes without conflating them. Surface branch ancestry, unique actions, changed assumptions, costs or side effects, and current validity. “Choose this branch” should define what happens to siblings: archive, keep for reference, or explicitly merge selected artifacts. Selecting a conversational branch cannot roll back side effects from another branch.

## Evidence
Evidence includes fork checkpoint identity, inherited state hash, branch-local mutations, consumed approvals, tool attempts, external effects, and any artifact copied or shared across branches. A branch comparison should be reconstructible from this ledger rather than generated summaries alone.

## Failure modes
Characteristic Failure includes forked runs sharing mutable local state accidentally, duplicated external side effects when a branch replays ancestral work, cloned approvals that no longer match, hidden ancestry that makes two branches look independent, and “switch branch” controls that imply external reality changes with the view. Another failure is unsafe merge: conflicting branch artifacts are combined without a decision owner.

## Falsification
Fork before and after a side effect, fork while an outcome is unknown, edit the same shared resource in both descendants, change approval-sensitive parameters in one branch, and switch repeatedly between branches. The contract fails if branch-local changes leak, if ancestral side effects repeat, if authority is inherited after semantic divergence, or if the user cannot tell which external effects are shared facts.

## Recovery
If branches accidentally share mutable state, freeze both, reconstruct ancestry, identify the first leaked mutation, and classify affected artifacts as local or global. Preserve external side-effect truth, even when inconvenient. If two branches need to converge, create an explicit merge/reconciliation action with conflict evidence rather than silently picking the last writer.

## Output and Handoff
Output: `agent-run-branching-contract`, containing fork eligibility, ancestry, inheritance classes, shared-side-effect rules, approval lineage, branch comparison, selection, and reconciliation hooks. Handoff shared-state conflicts to shared-state reconciliation and repeated actions to retry/replay controls.

## Sibling Boundary and delete-the-skill
Sibling plan previews own alternative steps before a run is committed; this skill owns actual divergent execution lineages. Multi-agent handoff visibility tracks ownership between actors, not branch ancestry. The delete-the-skill test passes because without a branch contract, alternate runs become ordinary duplicated chats that cannot account for shared side effects, inherited authority, or branch-local truth.