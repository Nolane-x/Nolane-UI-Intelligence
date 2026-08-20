---
name: designing-sample-tracking-interfaces
description: Own scientific sample identity, lineage, aliquots, location, status, custody, consumption, and linkage to experiments and measurements without relying on ambiguous human labels.
---
# Designing Sample Tracking Interfaces

## Decision ownership

Own lifecycle representation of physical or logical samples used in experiments. Decide stable identity, parent/child lineage, aliquot/split/merge, storage location, quantity, condition/status, custody, reservation, consumption, disposal, and linkage to runs/results. This owner does not define inventory accounting generally; it preserves scientific chain and identity.

## Inputs and evidence

Require sample identifier scheme, type, parent source, quantity/unit, container, location hierarchy, storage conditions, status, custody requirements, aliquot operations, expiration, permissions, experiment linkage, and barcode/scan support. Identify labels that may be reused by humans and must not serve as primary identity.

## Procedure

Use immutable sample IDs plus readable labels. Make lineage navigable in both directions. Split/aliquot operations should preview child IDs, quantity balance, containers, and inherited metadata; merge/pool operations need explicit provenance of all sources. Location changes require from/to and actor/time; scanning can accelerate but not bypass validation. Reservations and consumption should distinguish planned from actual quantity. Terminal states—consumed, disposed, lost—must retain history and prevent accidental reuse. Experiment selection should show sample condition/availability before commit.

## Failure topology

Failures include two samples with same label confused, quantity going negative after parallel reservations, lineage lost after aliquoting, storage moves overwriting previous location, consumed samples remaining selectable, and barcode scans silently accepting a wrong sample type. Another failure is merge/pooling collapsing multiple sources into one record with no recoverable provenance.

## Falsification

Reject if sample identity depends solely on mutable label; if split/merge cannot conserve and explain source quantities; if current location lacks move history; if terminal samples appear available; if parallel reservations can oversubscribe quantity without conflict; or if experiment data cannot trace back through aliquot lineage to source sample.

## Output contract

Return a `sample-tracking-interfaces-contract` with: immutable identity/label; sample type; parent/child lineage; split/merge semantics; quantity/unit; container/location history; status/condition; custody; reservation/consumption; expiration; scan validation; experiment/result links; and terminal-state rules. Include one concurrent-reservation and one pooled-sample scenario.

## Handoffs

Barcode/QR device skills provide capture mechanics, microplate layouts organize sample placement, batch/lot traceability handles manufacturing/material cohorts, and experiment setup consumes sample eligibility.