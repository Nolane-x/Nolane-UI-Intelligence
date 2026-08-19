---
name: designing-export-configuration
description: Use when users export product data or documents and must choose scope, format, fields, filters, locale, privacy, fidelity, and delivery without confusing what is visible on screen with what the exported artifact contains.
---

# Designing Export Configuration

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns configuration before generating an export artifact. It is distinct from data portability account exports and from converting one existing file. It decides what dataset/view state becomes an output and makes exclusions or sensitive fields explicit.

## Decision Boundary
Define export scope: selected records, current filtered view, current page, all matching records, full workspace, or document. Do not infer “current view” ambiguously when hidden filters/sorts/grouping affect output. Format choices should explain material differences such as raw data versus presentation fidelity. Field selection needs defaults appropriate to privacy and user task; hidden columns in UI are not automatically excluded from export unless that is the declared rule.

Locale and machine interoperability must be separate options where necessary. Human-facing PDF may use local formatting while CSV/JSON may need stable machine representation. Large exports may become asynchronous jobs with notification/download later. Apply authorization at generation time, not only when configuration UI first opens.

## Failure Topology
- “Export” unexpectedly includes all records when users intended selected rows.
- CSV reuses visual truncated values rather than full underlying data.
- Hidden sensitive columns are exported because they exist in the backend schema.
- Current filters are not recorded and users cannot explain the output scope later.
- A long-running export continues after the user's permission was revoked.
- Locale-formatted numbers make machine import ambiguous.

## Falsification and Recovery
Test selection/filter/page/all scopes, hidden fields, revoked permissions, very large exports, each format, locale differences, null/precision, and asynchronous completion. Compare exported rows/fields against the configuration summary. The design fails if users cannot predict the artifact before generation.

Recover by presenting an explicit scope/field/format summary, applying least-surprise sensitive defaults, separating display from machine representation, reauthorizing generation, and binding async output to its configuration snapshot.

## Output Contract
Return `export-configuration-contract` with scope semantics, field inclusion, format/fidelity differences, locale/machine representation, privacy/authorization checks, async generation behavior, configuration snapshot, and export verification cases.
