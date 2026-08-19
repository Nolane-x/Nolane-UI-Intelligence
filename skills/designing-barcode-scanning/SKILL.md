---
name: designing-barcode-scanning
description: Use when linear or stacked barcodes are scanned for inventory, tickets, products, logistics, or records and the interface must control continuous detection, confirmation, duplicates, unsupported symbologies, and manual fallback.
---

# Designing Barcode Scanning

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns scanning machine-readable barcode identifiers from camera or scanner input. It does not own QR-specific deep-link/security behavior. It decides how detection becomes a product action rather than treating every decoder result as trusted immediate input.

## Decision Boundary
Declare supported symbologies and expected data domains. Continuous scanning for warehouse workflows differs from one-shot lookup; define whether a valid decode auto-commits, stages a row, or requires confirmation. Debounce repeated frames so one physical code does not create ten records. If checksum or domain validation fails, explain whether the code was unreadable versus valid barcode containing unknown data.

Provide aiming/alignment guidance that does not rely solely on color and a manual-entry/search fallback when camera/scanner use fails. Hardware scanner keyboards may inject characters rapidly; distinguish scan terminators from human typing without breaking accessibility. High-impact actions such as redeeming a ticket should verify current backend state before confirmation.

## Failure Topology
- Continuous camera frames add the same inventory item repeatedly.
- Any syntactically valid barcode immediately triggers a destructive/redeem action.
- Unsupported symbology is reported as “camera error.”
- Manual fallback is hidden behind permission denial and users cannot continue.
- Scanner wedge input focuses the wrong field and corrupts another form value.
- Duplicate codes in a batch cannot be distinguished from accidental repeated detection.

## Falsification and Recovery
Test supported/unsupported formats, damaged/partial codes, repeated frames, continuous batch, scanner wedge, manual fallback, duplicate legitimate items, network validation, and permission loss. The design fails if decoder success is treated as domain authorization or if repeated visual detection produces uncontrolled duplicate actions.

Recover by separating decode/validate/commit stages, debouncing by code/time/context, validating domain state, scoping scanner focus, and offering manual entry. Make continuous versus one-shot mode explicit.

## Output Contract
Return `barcode-scanning-contract` with supported symbologies, scan modes, decode/validate/commit stages, duplicate/debounce policy, hardware-scanner handling, manual fallback, domain validation, and barcode verification cases.
