---
name: designing-bulk-work-item-editing
description: Use when this specialist's decision ownership is materially in scope. Own safe multi-item project edits with heterogeneous current values, eligibility checks, partial failure reporting, preview, and recoverability.
---
# Designing Bulk Work-Item Editing

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own editing many project work items at once. Decide selection scope, mixed-value representation, eligible/ineligible items, field operations such as set/clear/add/remove, validation, preview, transaction boundaries, partial failures, and undo. Generic bulk toolbars provide controls; this skill owns project-specific multi-item consequences.

## Inputs and evidence

Require editable fields, per-item permissions, transition rules, hierarchy implications, dependency constraints, project boundaries, maximum selection size, async processing behavior, and audit/undo capabilities. Identify fields where "set value" differs materially from "add member/tag" or "shift dates".

## Procedure

Show exact selection count and whether hidden/filter-selected items are included. For fields with mixed current values, present "mixed" rather than guessing a default. Use operation semantics appropriate to the field: replace status, add tag, remove assignee, shift due dates, move project. Before commit, compute eligibility and preview counts for changed, unchanged, skipped, and blocked items. Large async operations need progress and resumable results. Partial success must return itemized failures and leave a retry path. Undo should match the operation boundary and warn when subsequent edits make exact reversal unsafe.

## Failure topology

Failures include hidden selected items being changed unexpectedly, mixed values overwritten by an apparent blank field, one invalid item causing an opaque total failure, partial success reported as complete, shifting dates without preserving relative spacing, moving children while leaving parents behind unintentionally, and undo reverting unrelated later changes.

## Falsification

Reject if the user cannot know the exact selection scope; if a mixed field appears empty; if ineligible items are only discovered after a long operation with no itemized reason; if the success summary does not reconcile to the selection count; if hierarchy/dependency consequences are omitted from preview; or if retry re-applies changes to already-successful items without idempotence.

## Output contract

Return a `bulk-work-item-editing-contract` containing: selection semantics; hidden-selection disclosure; mixed-value UI; supported field operations; eligibility calculation; preview summary; async progress; transaction/partial-success policy; itemized failure result; retry/idempotence; audit trail; and undo boundary. Include one mixed-permission selection scenario.

## Handoffs

Use canonical status transitions, assignment, hierarchy, dependencies, and scheduling owners to validate each specific field operation. Generic bulk-action toolbar design supplies placement and selection affordances, not mutation semantics.