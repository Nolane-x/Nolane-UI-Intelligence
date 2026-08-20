---
name: designing-work-item-status-transitions
description: Use when this specialist's decision ownership is materially in scope. Own project work-item state machines, allowed transitions, transition evidence, automation, blocked states, and history across boards, lists, and detail views.
---
# Designing Work-Item Status Transitions

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the canonical status/state transition model for project work. Decide state meanings, allowed transitions, required evidence or fields, blocked/on-hold semantics, automation versus manual changes, and how state changes propagate across views. Board columns may trigger transitions, but this owner remains authoritative for the state machine.

## Inputs and evidence

Require status taxonomy, lifecycle rules, terminal states, reopen policy, required fields, approvals, automation events, blocked/on-hold semantics, permissions, and audit requirements. Identify products that currently overload priority, progress, and status into one label and separate those concerns before designing controls.

## Procedure

Define states by operational meaning, not color. Prefer a small canonical set with explicit transition rules, then allow views to group/filter without creating new implicit states. Before a transition that requires evidence—review complete, deployment linked, acceptance met—show missing requirements inline. Blocked should carry blocker identity/reason and not simply become another progress column. Automated state changes need visible provenance and a user path to understand/reconcile unexpected changes. Reopen from terminal state should preserve prior completion context. Bulk transitions must validate each item and report partial failures precisely.

## Failure topology

Failures include every team inventing duplicate statuses, boards redefining canonical state by column name, blocked items marked "in progress" with no blocker semantics, automation flipping state without explanation, terminal items silently reopening, and bulk status changes skipping required evidence. Another failure is using percent complete as a status substitute.

## Falsification

Reject if the same canonical state has different operational meaning in two views; if an invalid transition can be committed and only fails later; if a blocked item has no inspectable blocker; if automated changes lack actor/source; if terminal-to-active transitions erase completion history; or if bulk changes report success while some items remained unchanged without an itemized result.

## Output contract

Return a `work-item-status-transitions-contract` containing: state taxonomy; allowed transition graph; required transition evidence; blocked/on-hold model; automation provenance; manual override policy; terminal/reopen semantics; cross-view mapping; bulk transition behavior; and audit fields. Include one invalid evidence-gated transition and one automated-change reconciliation case.

## Handoffs

Kanban boards may invoke transitions, backlog/sprint planning determine planning membership, approvals remain separate authorities, and project health consumes status evidence rather than redefining states.