---
name: designing-migration-onboarding
description: Use when users bring existing real work from another product, file, account, or legacy version and the onboarding experience must establish source mapping, preview, validation, progress, exception handling, rollback, and trust.
---

# Designing Migration Onboarding

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns the transition of real user data and workflows into the product. It is deliberately distinct from sample data: migration can alter durable production state and therefore needs preview, mapping, exception, provenance, and recovery semantics. It does not own the low-level importer implementation or generic background-job UI.

## Decision Architecture
Start with source authority and migration scope. Users must know what will be imported, copied, transformed, skipped, or linked rather than moved. Detect source versions and schema variants before presenting a confident “Import” action. When mapping is required—columns, fields, users, categories, statuses, units—show the destination model and preserve reusable mappings only when their scope is safe and explicit.

Provide a preflight summary before durable mutation: object counts where known, unresolved mappings, unsupported features, duplicates, permission gaps, expected side effects, and whether existing destination data can be merged or overwritten. Do not bury lossy transformations in post-import warnings. For large migrations, background progress should expose phases and exceptions while allowing users to continue normal work if consistency permits.

Define reversibility. Some migrations can be deleted as one batch, some can roll back only before users edit imported records, and others are irreversible after external side effects. State that boundary before commit. Keep source-to-destination provenance long enough to diagnose duplicate imports, retries, and user questions.

## Failure Topology
- Import starts immediately after file selection with no preview of destructive field mapping.
- Unsupported source states are silently mapped to a generic destination status and meaning is lost.
- Retrying after timeout duplicates half the records because batch identity is absent.
- Users are told migration is “complete” although 400 records are quarantined with errors.
- Rollback button remains visible after downstream edits make rollback unsafe.
- Imported users receive notifications before the administrator reviews membership mapping.

## Falsification and Recovery
Falsify with duplicate destination records, unsupported source fields, partial failure, large background import, retry after unknown outcome, session interruption, changed mapping between retries, permission-restricted records, rollback after destination edits, and a second migration from the same source. The design fails if users cannot explain what changed from source to destination or safely distinguish completed, skipped, transformed, failed, and unknown records.

Recover by assigning migration/batch identity, performing schema-aware preflight, requiring explicit lossy mappings, preserving item provenance, separating completion from exception closure, making rollback eligibility authoritative, and suppressing external side effects until their migration phase is intentionally committed.

## Output Contract
Return `migration-onboarding-contract` with source/scope, schema detection, mapping model, preflight summary, duplicate policy, side-effect gates, background phases, exception handling, provenance, retry/idempotency rules, rollback boundary, and falsification cases.