---
name: designing-microplate-layout-interfaces
description: Own well-plate scientific layouts, sample assignment, controls, replicates, volumes, gradients, orientation, bulk fill, validation, and instrument-ready mapping.
---
# Designing Microplate Layout Interfaces

## Decision ownership

Own interaction with standardized or custom arrays of wells used for experiments. Decide plate format/orientation, well identity, sample/control assignment, replicate grouping, volume/concentration fields, bulk pattern operations, gradients, validation, legends, and instrument export. Generic spreadsheets do not own the physical well semantics.

## Inputs and evidence

Require plate format (e.g. dimensions), well naming convention, orientation, instrument expectations, sample IDs, control types, replicate rules, volume/concentration units, allowed empty wells, edge effects if relevant, and export mapping. Identify multi-plate experiments and plate barcode identity.

## Procedure

Fix orientation with unmistakable row/column labels and plate identity. Selection supports individual, range, row, column, and pattern operations while previewing affected wells. Assign samples through stable IDs and show controls/replicates as semantic categories, not color alone. Bulk dilution/gradient operations should preview calculated values and units before commit. Validate duplicate/conflicting assignments, insufficient sample quantity, invalid volumes, and required controls. Keep a table/list equivalent for accessibility and precise inspection. Export must match the target instrument's well mapping and plate identity.

## Failure topology

Failures include mirrored orientation, well labels hidden during scroll/zoom, color-only control identity, bulk fill overwriting occupied wells, dilution calculations with mixed units, sample quantity insufficiency discovered only at run time, and exported plate maps offset by one row/column. Another failure is selection gestures so spreadsheet-like that users forget actions correspond to physical wells/material.

## Falsification

Reject if orientation cannot be confirmed at any zoom; if a bulk operation lacks affected-well preview; if controls/replicates lose textual identity; if unit mismatch can silently enter calculated gradients; if required controls are missing with no finding; if sample quantities are oversubscribed; or if exported mapping cannot be cross-checked against visible well IDs.

## Output contract

Return a `microplate-layout-interfaces-contract` with: plate identity/format/orientation; well naming; selection modes; sample/control/replicate assignment; volume/concentration units; bulk pattern/gradient preview; validation; quantity checks; accessibility table equivalent; multi-plate behavior; and instrument export mapping. Include one mirrored-orientation safeguard example.

## Handoffs

Sample tracking supplies sample identity/quantity, experiment setup consumes the plate manifest, instrument run control executes against it, and spreadsheet mechanics may support selection but not well semantics.