---
name: designing-agent-interruption-and-cancel
description: Let users interrupt or cancel agent work with clear boundaries for in-flight side effects, partial artifacts, cleanup, and safe continuation.
---

# Designing agent interruption and cancel

Cancel is not equivalent to stopping text generation when the agent may already have started uploads, writes, external jobs, or transactions. Use this skill to define interruption semantics throughout agent execution.

## Decision ownership

Own interruptibility by action phase, cancel request behavior, in-flight operation handling, cleanup, partial-result preservation, and restart/continue semantics. Decide when the UI should offer pause, stop-after-current-step, immediate cancel, or only abort of future work.

## Inputs and evidence

Collect tool cancellation capabilities, transaction boundaries, irreversible operations, queued work, background jobs, temporary resources, partial files, and side-effect logs. Identify operations that cannot be interrupted once committed.

## Procedure

Define cancellation points explicitly. When immediate abort is possible, stop pending work and reconcile partial state. When an external action cannot be cancelled, communicate that the current operation may finish while subsequent work is stopped. Preserve useful partial artifacts unless they are unsafe or misleading.

After interruption, summarize what completed, what was not attempted, what may still be running externally, and available next actions. Keep undo/reversal separate from cancel; stopping future work does not reverse past effects.

## Failure topology

A cancel button that merely hides the UI while jobs continue is deceptive. Force-stopping processes can corrupt files or leave locks. Another failure is discarding all partial output, forcing users to repeat expensive completed work.

Cancel may also race with completion, producing duplicate actions if the user retries before the previous operation actually stops.

## Falsification

Cancel during reads, writes, external sends, queued batches, retries, and background operations. Inspect external systems afterward. Verify the summary matches actual side effects. Rapidly cancel and restart to test duplicate-prevention and stale status.

## Output contract

Produce an `agent-interruption-and-cancel-contract` containing interruption points, per-tool cancellation behavior, in-flight semantics, cleanup/preservation rules, post-cancel summary, external-job treatment, restart guards, and tested race scenarios.

## Handoffs

Use `designing-agent-reversible-actions` to undo completed effects, `designing-agent-action-progress` to expose in-flight state, `designing-agent-background-task-surfaces` for detached jobs, and `designing-agent-retry-and-recovery` after interruption-related failures.