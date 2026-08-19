---
name: designing-structured-import-mapping
description: Use when CSV, spreadsheet, JSON, or structured files must map external columns/fields into product schema and users need preview, type inference, validation, transform rules, and partial-error control before commit.
---

# Designing Structured Import Mapping

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns the mapping stage between an uploaded structured file and application records. It does not own raw file transfer. Its job is to make schema interpretation inspectable and correct before data mutation occurs.

## Decision Boundary
Detect source structure but treat inference as a proposal. Show source fields/columns, sample values, inferred types, and target fields. Require explicit mapping for ambiguous/high-impact fields. Define how dates, locale-formatted numbers, booleans, enums, references, required fields, duplicates, and unknown columns transform. Preview the transformed records using the same parser that will commit them.

Separate file-level fatal errors from row-level validation. Decide whether users can import valid rows while rejecting invalid ones, must fix everything first, or can download an error report. Mapping templates may be saved only when source schema identity is stable enough; applying stale mapping to shifted columns is dangerous.

## Failure Topology
- Header similarity auto-maps “Cost” to “Price” and imports materially wrong data.
- Preview parser differs from backend commit parser.
- Locale decimal commas are interpreted using server locale rather than import context.
- Row 2 failure aborts 100,000 otherwise valid rows with no recovery option.
- Saved mapping uses column position rather than header/schema identity.
- Duplicate records are created because identity/dedup strategy is decided only after import.

## Falsification and Recovery
Test reordered/missing/new columns, ambiguous names, locale dates/numbers, invalid rows, duplicates, references, very large files, preview/commit parity, and saved mapping reuse. The design fails if a previewed value can commit differently or if an inferred mapping can mutate high-impact fields without review.

Recover by making inference reversible, binding mapping to semantic source identifiers, sharing parser/validation logic, exposing row-level errors, and defining duplicate/commit policy before execution. Preserve original source and mapping provenance for audit where needed.

## Output Contract
Return `structured-import-mapping-contract` with source schema detection, mapping/inference rules, type/locale parsing, transform preview, validation granularity, duplicate policy, saved-mapping identity, commit semantics, and import verification fixtures.
