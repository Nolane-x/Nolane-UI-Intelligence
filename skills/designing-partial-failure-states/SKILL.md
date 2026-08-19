---
name: designing-partial-failure-states
description: Use when a composite operation or surface can succeed in some parts and fail in others and the UI must preserve successful work, identify failed scope, and support targeted recovery without collapsing everything into success or error.
---

# Designing Partial Failure States

## Parent Contract
**Required parent:** `designing-empty-loading-error-states`.

This faculty owns mixed outcomes. It applies when the system has enough granularity to know which items, regions, or sub-operations succeeded, failed, remain pending, or were skipped. It does not downgrade atomic transactional failure into “partial success” when consistency requires all-or-nothing behavior.

## Decision Boundary
Start from the operation’s atomicity contract. Bulk imports, batch edits, multi-source dashboards, synchronized resources, and federated requests may legitimately produce mixed results. Define the result unit and preserve successful outcomes visibly; do not roll them back in the interface unless the backend actually rolled them back.

Failure communication needs scope. A top-level summary can state “37 updated, 3 failed,” but users also need item-level reasons and repair paths. Distinguish retryable transport/service failures from deterministic validation or permission failures; retrying everything can duplicate already-completed side effects or waste time.

State reconciliation is critical. If a retry targets only failed items, the UI must merge the new outcomes into the existing result set without erasing prior success evidence. If some failures leave the final object in an uncertain state, label it unknown rather than guessing success or failure.

## Failure Topology
- Batch action reports “Failed” although 97% of items succeeded, prompting unsafe full retry.
- Whole operation reports “Success” while three silently failed items are omitted.
- Retry resubmits successful non-idempotent operations and creates duplicates.
- Error summary lists counts but offers no mapping to failed objects.
- Recovered items remain visually marked failed because state is not reconciled.
- Network interruption produces an assumed failure for items whose server outcome is actually unknown.

## Falsification and Recovery
Falsify with mixed validation errors, permission failures, timeouts after server commit, item-specific retry, full retry on an idempotent operation, result export, keyboard navigation through failed items, and a second recovery pass that succeeds for some failures. The design fails if users cannot distinguish failed, successful, pending, skipped, and unknown units or cannot retry safely at the correct granularity.

Recover by defining atomicity and result units, retaining successful work, classifying retryability, exposing item-level causes, using idempotency/operation IDs where available, representing unknown outcomes honestly, and reconciling recovered units into the existing result model.

## Output Contract
Return `partial-failure-state-contract` with atomicity assumptions, result-unit states, summary/detail representation, failure taxonomy, targeted-retry rules, idempotency dependencies, unknown-outcome handling, reconciliation behavior, accessible navigation, and falsification cases.