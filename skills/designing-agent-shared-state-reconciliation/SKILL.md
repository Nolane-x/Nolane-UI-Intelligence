---
name: designing-agent-shared-state-reconciliation
description: Use when a human-facing interface and an AI agent can both mutate the same task state and the product must reconcile concurrent edits, stale observations, optimistic UI, and authoritative backend outcomes without lying about what is true.
---

# Designing Agent Shared-State Reconciliation

## Why this problem exists
Agentic interfaces stop being ordinary request-response UIs when the user and the agent can both change the same object. A user may edit a destination while an agent is planning with the previous value; the agent may optimistically mark a task complete while the backend later rejects the tool action; a refreshed tab may hydrate newer server state while a streaming agent message still references an older snapshot. This skill owns the decision model for reconciling those competing versions into one legible, truthful interface state.

## Parent Contract
**Required parent:** `designing-human-ai-interaction`.

The parent defines broad human/AI collaboration, control, correction, trust, and interaction principles. This specialist begins when both sides have mutation authority over shared state and the interface must decide what wins, what is provisional, what conflicts, and what the user is allowed to repair.

## Reconciliation model
Represent shared state with at least `(entity, revision, writer, observation_revision, pending_mutations, authoritative_revision, conflict_status)`. A visible value is not enough; the interface needs lineage. Distinguish locally proposed state, agent-proposed state, server-accepted state, and derived presentation state. The decision owner here is the policy that maps competing revisions to merge, reject, queue, rebase, or request human resolution.

Use field-level reconciliation only when fields are semantically independent. A naive last-write-wins rule is unsafe for coupled values such as dates and time zones, selected account plus available permissions, or a resource identifier plus its version. When a mutation was generated from a stale observation, record that fact before attempting a merge. Optimistic UI may remain fast, but it must not silently upgrade provisional data into authoritative truth.

## Conflict classes and invariants
A benign conflict is one where operations commute and can be merged without changing intent. A semantic conflict is one where both writes are individually valid but jointly ambiguous. An authority conflict is one where a lower-authority writer attempts to overwrite a higher-authority source. A temporal conflict occurs when an action was planned against a revision that is no longer current.

Invariants: accepted server state is never overwritten merely because a stream arrived later; a stale agent observation cannot erase a newer human edit; conflict resolution preserves the losing proposal in evidence until the user can understand what changed; and the interface cannot present two incompatible revisions as simultaneously canonical. If the product permits offline or multi-tab work, revision identity must survive those boundaries.

## Evidence to collect
Evidence should include event traces that interleave human edits, agent proposals, server acknowledgements, retries, reconnects, and stale stream events. Capture the revision graph before and after reconciliation, the reason a contender lost, and the rendered state the user saw. Valuable adversarial cases include same-field simultaneous edits, a server rejection after optimistic success, a stale agent tool result, and a reconnect that replays an already-applied event.

A screenshot can prove presentation but not reconciliation correctness. Strong evidence demonstrates deterministic replay: given the same ordered event log and authority rules, independent clients converge to the same canonical state while exposing any unresolved conflict.

## Characteristic Failure modes
Failure includes last-arrival-wins corruption, hidden overwrites, optimistic state that never rolls back, conflict banners that do not identify the affected data, and agent text that claims an action succeeded while the shared object shows failure. Another characteristic failure is dual truth: the chat transcript references one revision while the editable surface uses another, with no visible reconciliation boundary.

## Falsification protocol
Falsification should deliberately inject stale reads, reorder acknowledgements, duplicate tool events, and mutate the same field from human and agent paths. The contract is disproved if replay produces different final state, if a losing write disappears without evidence, if an agent can overwrite a later human decision merely by finishing later, or if the user cannot tell which value is authoritative.

## Recovery strategy
Recovery freezes new automatic writes for the conflicted entity, reconstructs the revision lineage, identifies the last mutually acknowledged state, and replays only mutations whose preconditions still hold. Present semantic conflicts for explicit human resolution rather than inventing a merge. Once resolved, emit a new authoritative revision and invalidate stale agent context so future actions cannot continue from the old branch.

## Output, Handoff, and Sibling boundary
Output: `agent-shared-state-reconciliation-contract`, containing revision identity, writer authority, conflict classes, merge rules, rollback behavior, stale-observation handling, and evidence requirements. Handoff concurrency implementation details to the persistence/runtime layer and hand off correction copy to the parent when the conflict becomes a conversational repair problem.

Sibling boundary: agent tool-call lifecycle owns execution phases of a tool invocation, not reconciliation of shared domain state. Human correction owns how a user amends agent-understood intent, not which concurrent mutation wins. The delete-the-skill test passes because removing this specialist leaves no owner for deterministic convergence when human and agent mutations overlap.