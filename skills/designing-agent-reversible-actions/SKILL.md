---
name: designing-agent-reversible-actions
description: Design undo and compensating-action systems for agent side effects with explicit reversibility limits, snapshots, dependencies, and verification.
---

# Designing agent reversible actions

Undo can safely reduce confirmation burden only when the product knows what can actually be reversed. Use this skill when agents edit files, records, settings, messages, or other state and users need a reliable way back.

## Decision ownership

Own reversibility classification, snapshot requirements, undo window, dependency handling, compensating actions, conflict detection, and verification after reversal. Decide whether an action is exactly reversible, approximately compensable, or irreversible.

## Inputs and evidence

Collect mutation types, before-state snapshots, version IDs, external APIs, cascading effects, concurrent edits, retention limits, and legal/business constraints. Identify actions like email send or external notification that cannot truly be unsent even if a local record can be deleted.

## Procedure

Classify each side effect before promising undo. For exactly reversible changes, preserve sufficient prior state and version identity. For compensating actions, label them honestly: refund is not “undo purchase” in every domain, and deleting a sent message does not erase delivery.

Before reversal, detect intervening changes to avoid overwriting newer work. After reversal, verify destination state and report any residual effects. Group multi-step undo only when dependency order is understood.

## Failure topology

A global “Undo” label can imply stronger reversibility than reality. Restoring stale snapshots may erase concurrent user edits. Another failure is reversing primary state while leaving notifications, caches, webhooks, or downstream copies untouched.

Undo windows may expire without users knowing until they need them.

## Falsification

Undo immediately, after concurrent modification, after dependency changes, and after expiry. Inspect downstream systems for residual effects. Test partial reversal where one compensating action fails. Ensure the UI distinguishes exact reversal from mitigation.

## Output contract

Produce an `agent-reversible-actions-contract` defining reversibility classes, snapshot/version needs, undo windows, conflict handling, dependency order, compensating semantics, residual-effect disclosure, and verification scenarios.

## Handoffs

Use `designing-agent-side-effect-review` to expose changes, `designing-agent-action-confirmations` when reversibility is insufficient, `designing-agent-interruption-and-cancel` for stopping future work, and domain transaction skills for specialized compensation.