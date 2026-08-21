---
name: designing-agent-partial-completion-recovery
description: Use when an agent finishes some intended work but fails, blocks, or loses authority before the task is complete and the UI must preserve valid outcomes, expose residual obligations, and avoid pretending the whole run either succeeded or failed.
---

# Designing Agent Partial-Completion Recovery

## What this skill owns
Agentic work is often non-atomic. A run may create three files and fail on the fourth, send one approved message while another is blocked, finish analysis but fail to publish, or update one service while a dependent service is unavailable. This skill owns the decision model for classifying partial completion and presenting a recoverable remainder. It prevents binary run status from erasing useful work or concealing unfinished obligations.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent governs permissible autonomous behavior. This specialist activates when execution has already produced material outcomes yet the overall task cannot reach its intended completion state.

## Completion decomposition
Decompose the task into outcome obligations rather than merely tool calls. For each obligation record: intended result, dependencies, side-effect class, current evidence, validity horizon, and disposition such as `satisfied`, `satisfied_but_unverified`, `blocked`, `failed`, `not_attempted`, `superseded`, or `requires_compensation`. A tool call can succeed while the obligation remains unsatisfied, and several tool calls can jointly satisfy one obligation.

The decision owner is whether completed artifacts remain valid independent of the failed remainder. Preserve them when their preconditions still hold. Do not roll back useful work simply to regain a clean all-or-nothing story unless domain semantics require atomicity.

## Residual work contract
The recovery surface should answer four questions: what definitely succeeded, what definitely did not, what is uncertain, and what can be done next. Residual steps need their original prerequisites rechecked; failure may have changed the world. If a later step depended on an earlier one that only partially completed, mark the dependency explicitly rather than blindly resuming.

Where compensation is available, distinguish compensating action from rollback. A sent message cannot be unsent in the same sense that a draft edit can be reverted. The interface should describe the actual remediation semantics.

## Evidence model
Evidence includes obligation-to-artifact links, terminal tool results, authoritative checks, failure causes, preserved outputs, and any compensation performed. Capture the exact completion frontier so a new run can consume it without repeating already satisfied work. Evidence must also show why a seemingly successful operation did not satisfy its higher-level obligation when that occurs.

## Failure topology
Characteristic Failure includes “run failed” banners that hide completed side effects, restart buttons that duplicate work, declaring success because most steps finished, losing generated artifacts after a late error, and assuming an operation can be rolled back when only compensation exists. Another failure is residual ambiguity: the user sees which step failed but cannot tell whether the intended task outcome is still usable.

## Falsification
Falsification should fail the run after each materially different obligation, inject a late verification failure after apparent success, make a completed artifact stale before recovery, and test a non-reversible side effect. The contract is false if a completed obligation is unnecessarily repeated, if an unsatisfied obligation is reported complete, if uncertain state is flattened into failure, or if recovery cannot construct a minimal remaining-work set.

## Recovery algorithm
Freeze the completion frontier, verify durable outcomes against authoritative sources, invalidate any artifacts whose preconditions no longer hold, and derive the smallest residual obligation set. Re-plan only that remainder. Preserve provenance linking the recovered run to the original run, and request fresh approval for any residual action whose prior authorization no longer applies.

## Output and Handoff
Output: `agent-partial-completion-recovery-contract`, containing obligation decomposition, completion frontier, preserved artifacts, residual obligations, compensation semantics, revalidation, and evidence lineage. Handoff interruption mechanics to `designing-agent-interruption-and-resume`, per-attempt repetition to retry/replay controls, and side-effect accounting to the side-effect ledger.

## Sibling Boundary and delete-the-skill
Sibling interruption/resume decides whether a stopped run can continue from a checkpoint. This skill decides how to salvage a run whose intended outcome is already partially realized. The delete-the-skill test passes because without this owner, partial outcomes are forced into binary run statuses that either discard valid work or hide missing obligations.