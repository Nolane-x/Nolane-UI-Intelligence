---
name: designing-agent-side-effect-review
description: Let users inspect actual external changes made by an agent, including scope, unexpected differences, irreversible effects, and verification status.
---

# Designing agent side-effect review

After an agent acts, users need evidence of what changed—not merely a confident summary. Use this skill for file edits, messages, deployments, database mutations, calendar changes, purchases, permissions, or any external side effect.

## Decision ownership

Own post-action change representation, grouping, before/after evidence, verification, unexpected-effect disclosure, and follow-up controls. Decide which side effects require mandatory review before the task can be called complete.

## Inputs and evidence

Collect executed tool calls, target identifiers, before/after state, diffs, external acknowledgments, failures, irreversible operations, timestamps, and validation results. Distinguish requested changes from incidental side effects.

## Procedure

Show actual effects grouped by user goal or external system. Prefer concrete diffs, sent-message previews, changed-event details, or deployment versions over natural-language summaries alone. Mark whether each effect was verified from the destination system.

Highlight deviations from the approved plan: extra files touched, recipients changed, fallback provider used, or partial rollback. Provide direct follow-up actions such as undo, open destination, retry verification, or fix only the failed subset.

## Failure topology

Agent summaries can omit accidental changes. A successful API response may not mean the destination reached desired state. Another failure is hiding dozens of small mutations under “updated project,” making review impossible.

Review can also overwhelm users if every harmless internal file is listed with equal prominence.

## Falsification

Inject an unintended extra mutation and verify it appears. Simulate success responses with failed downstream state. Compare review surface against destination truth. Ask users to identify irreversible changes and whether all approved scope was satisfied.

## Output contract

Produce an `agent-side-effect-review-contract` defining effect grouping, before/after evidence, verification states, deviation highlighting, irreversible markers, follow-up controls, and reconciliation tests against external systems.

## Handoffs

Use `designing-agent-action-confirmations` before execution, `designing-agent-reversible-actions` for undo, `designing-agent-result-provenance` for evidence lineage, and `designing-agent-partial-completion` for mixed side-effect outcomes.