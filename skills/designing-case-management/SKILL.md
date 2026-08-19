---
name: designing-case-management
description: Use when work centers on a durable case that accumulates evidence, participants, tasks, decisions and history over time and the interface must preserve case identity, lifecycle and context across many interactions.
---

# Designing Case Management

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns the product-level interaction model for durable cases: support cases, investigations, claims, applications, incidents, reviews or similar dossiers. It does not define triage intake, individual approval policy or the domain decision itself.

## Decision Boundary
A case is more than a row in a queue. Give it a stable identity and lifecycle, such as opened, awaiting information, in progress, blocked, escalated, resolved, reopened and closed, with domain-specific additions only when justified. Distinguish lifecycle state from priority, owner, SLA and attention state; all may change independently.

The case workspace should organize evidence around the user’s reasoning task. Typical surfaces include summary/status, participants, chronology, structured fields, documents/evidence, communications, tasks, decisions and audit history. Do not duplicate the same truth in independent panels that can drift. Identify the authoritative edit location for each field.

Chronology is critical when events arrive asynchronously. Show event time, recording time and actor/source where those differ materially. Attachments and comments need provenance and version identity. If the case includes sensitive information, visibility may vary by field/document; do not imply every collaborator sees the same dossier.

Closing/resolving a case should require the minimum evidence the domain policy needs and communicate what remains editable afterward. Reopen must not erase the original resolution or make historical timelines look continuous with no boundary.

Case navigation should preserve work context when moving through a queue: current tab/section, expanded evidence and safe draft state where appropriate. However, drafts must remain bound to the correct case ID.

## Failure Topology
- Priority and lifecycle share one “status” field, so lowering priority appears to close the case.
- Timeline sorts by ingestion time while labels imply occurrence time.
- The same customer/contact field is editable in three panels and values diverge.
- Closing hides unresolved tasks with no warning or disposition.
- Reopening overwrites the original resolution reason.
- Moving to the next case leaves an unsaved draft attached to the new case.

## Falsification and Recovery
Falsify with long-running cases, reopen, concurrent edits, restricted evidence, delayed events, reassignment, unresolved tasks, queue next/previous and stale tabs. Reconstruct the case lifecycle and decisive evidence solely from authoritative records and rendered history. If case identity or chronology can be confused across transitions, the design fails.

Recover by separating lifecycle/priority/ownership, centralizing authoritative fields, preserving immutable historical events and binding drafts/navigation state to stable case IDs.

## Output Contract
Return `case-management-contract` with case identity, lifecycle state machine, workspace information model, chronology/provenance, evidence and participant boundaries, resolution/reopen rules, draft/navigation persistence, permission handoffs and longitudinal tests.