---
name: designing-agent-retry-and-recovery
description: Design retries around failure cause, idempotency, changed context, and user control so agents recover without duplicating side effects or looping invisibly.
---

# Designing agent retry and recovery

Retries are safe only when the failed operation and surrounding state are understood. Use this skill when tools time out, rate-limit, return transient errors, partially succeed, or require a changed strategy.

## Decision ownership

Own retry eligibility, automatic retry count/backoff, idempotency requirements, strategy changes, user-visible failure state, and escalation to manual recovery. Decide when an operation must be inspected before retrying because success is ambiguous.

## Inputs and evidence

Collect tool error taxonomy, request IDs, idempotency keys, side effects, rate limits, partial-response behavior, external job status, and historical failure traces. Distinguish “request failed” from “response lost after request succeeded.”

## Procedure

Classify errors as transient, permanent, permission-related, invalid-input, ambiguous-outcome, or dependency failure. Retry transient read operations automatically within bounded policy. For mutations, require idempotency or verify external state before repeating.

Expose meaningful retry status and changed strategy when the agent adapts. Preserve prior attempts in the activity record. After bounded retries, stop and present the blocking cause plus recovery options rather than looping indefinitely.

Use backoff and provider guidance for throttling.

## Failure topology

Blind retries can send duplicate emails, create duplicate records, or charge twice. Hidden retries can make latency inexplicable. Another failure is retrying a permanent validation error repeatedly while presenting optimistic progress.

An agent may also change tools during recovery and silently cross a privacy or permission boundary.

## Falsification

Simulate timeouts before and after side-effect commit, rate limits, invalid inputs, permission denial, and flaky reads. Verify duplicate prevention and bounded retry counts. Inspect activity records for each attempt and confirm tool changes respect policy.

## Output contract

Produce an `agent-retry-and-recovery-contract` defining error classes, retry eligibility, limits/backoff, idempotency/verification requirements, adaptation disclosure, terminal failure behavior, and test scenarios for ambiguous outcomes.

## Handoffs

Use `designing-agent-action-progress` for retry visibility, `designing-agent-partial-completion` for mixed outcomes, `designing-agent-permission-escalation` for denied access, and `designing-agent-reversible-actions` if recovery requires compensating actions.