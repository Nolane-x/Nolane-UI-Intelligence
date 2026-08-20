---
name: designing-agent-partial-completion
description: Represent agent tasks that complete only part of the requested work without collapsing mixed outcomes into either success or failure.
---

# Designing agent partial completion

Multi-step agent tasks often end with some useful work complete and some blocked, skipped, or failed. Use this skill when binary success/failure would mislead users about what they can safely rely on.

## Decision ownership

Own completion classification, item-level outcome representation, summary language, downstream action availability, and retry/resume boundaries. Decide what minimum evidence allows an item to be marked complete.

## Inputs and evidence

Collect requested scope, execution plan, per-item outcomes, skipped reasons, warnings, verification status, side effects, and remaining dependencies. Distinguish completed-but-unverified from verified completion.

## Procedure

Preserve the original scope and map each unit to completed, incomplete, blocked, skipped, failed, or uncertain. Summarize useful completed results first without implying whole-task success. Make remaining work explicit and actionable.

Allow retry or continuation against only incomplete units when safe. Avoid rerunning completed mutations unnecessarily. For generated artifacts, mark whether each is final, draft, or potentially inconsistent because related steps failed.

## Failure topology

Saying “Done” after 8 of 10 items trains users to miss omissions. Saying “Failed” can hide valuable completed work and provoke redundant retries. Another failure is presenting a partial artifact as final when missing validation steps materially affect trust.

A resume action can duplicate completed work if the partial state is not persisted precisely.

## Falsification

Run batches with combinations of success, skip, block, uncertain outcome, and hard failure. Ask users which items are safe to use and what remains. Resume and verify completed mutations are not repeated. Force a verification step to fail after generation and ensure the artifact is not labelled fully complete.

## Output contract

Produce an `agent-partial-completion-contract` containing scope units, outcome taxonomy, verification status, summary rules, resume/retry semantics, artifact status, and mixed-outcome examples.

## Handoffs

Use `designing-agent-retry-and-recovery` for failed units, `designing-agent-uncertainty-disclosure` for ambiguous outcomes, `designing-agent-action-progress` during execution, and `designing-agent-result-provenance` for completed evidence.