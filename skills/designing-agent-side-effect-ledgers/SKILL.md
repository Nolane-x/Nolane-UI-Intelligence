---
name: designing-agent-side-effect-ledgers
description: Use when an agent performs externally observable actions and the interface needs a durable ledger of intended, attempted, confirmed, disputed, compensated, and irreversible effects so users can audit what actually changed.
---

# Designing Agent Side-Effect Ledgers

## Ledger purpose
Agent transcripts are poor audit logs. They mix intention, narration, speculation, and runtime events, and they can be summarized or regenerated. This skill owns the interface contract for a durable side-effect ledger: a user-facing and machine-auditable record of actions that changed or may have changed external state.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent defines when side-effecting actions are allowed. This specialist begins once such actions are proposed or performed and the product needs authoritative accountability beyond conversational text.

## Entry model
Each ledger entry should identify logical action, execution attempt, target identity, side-effect class, precondition, authority evidence, dispatch evidence, outcome evidence, external confirmation, reversibility, compensation options, and current status. Distinguish `planned`, `attempted`, `confirmed`, `failed_before_effect`, `outcome_unknown`, `partially_effective`, `compensated`, and `irreversible` where relevant.

The decision owner is what qualifies as a side effect worthy of ledgering. Persist actions that alter external resources, permissions, money, communications, publication state, physical devices, or durable project state. Pure reads may still require ledger entries when they expose sensitive data or have compliance significance, but routine ephemeral UI reads need not flood the user.

## Identity and grouping
Group repeated attempts under one logical action while preserving each attempt. Batch operations should support expansion from aggregate intent to item-level effects. A single “updated 200 records” line is insufficient when some items failed or were retried. Stable target identifiers matter more than friendly labels, which may change later.

## User-facing semantics
The ledger should support both at-a-glance confidence and forensic inspection. Users need to distinguish what definitely changed from what may have changed. Do not use green success styling for an operation whose only evidence is dispatch. Expose who or what initiated the action, whether it consumed approval, and whether a compensating action exists.

## Evidence
Evidence is the ledger’s raw material: tool request identity, runtime acknowledgement, domain confirmation, revision IDs, receipts, transaction IDs, timestamps or sequence tokens, and compensation results. Keep generated summaries linked to those artifacts rather than replacing them. Evidence retention policy may vary by product, but the existence and state of a side effect must not depend on the model remembering it.

## Failure modes
Characteristic Failure includes transcript-only accountability, overwriting failed attempts after a retry, hiding partial batch outcomes, labeling ambiguous results as failed or successful, failing to connect approvals to effects, and treating compensation as if the original effect never happened. Another failure is ledger incompleteness caused by recording only tool calls while omitting side effects produced indirectly by delegated tools.

## Falsification
Inject duplicate callbacks, partial batches, an outcome-unknown network loss, a successful compensation, a changed target label, and a delegated sub-agent action. The contract fails if the ledger loses attempt identity, cannot reconstruct the effect’s target, collapses ambiguity, or omits a material external change.

## Recovery
When evidence conflicts, keep the entry disputed and query the authoritative external system. If an unledgered side effect is discovered, append a corrective entry with provenance rather than rewriting history. For duplicate actions, relate the entries and route remediation to reversible-action or compensation controls.

## Output and Handoff
Output: `agent-side-effect-ledgers-contract`, defining material effect classes, entry schema, attempt grouping, evidence authority, ambiguity states, user inspection, retention, and corrective updates. Handoff reversible controls to `designing-agent-reversible-action-surfaces`; hand off operation lifecycle truth to tool-call lifecycles.

## Sibling Boundary and delete-the-skill
Sibling approval-scope skills govern authority before action. This skill records what was actually attempted and changed afterward. Partial-completion recovery uses ledger evidence but does not own the durable effect record. The delete-the-skill test passes because without a side-effect ledger, users cannot audit an agent’s durable impact independently of mutable conversational narration.