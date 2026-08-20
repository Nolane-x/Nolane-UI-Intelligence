---
name: designing-label-printing
description: Use when printing to fixed label stock or thermal devices requires exact template, dimensions, orientation, calibration, copies, barcode/text fit, and device media compatibility.
---

# Designing Label Printing

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns print interaction where millimeters, stock geometry, and printer calibration are part of task correctness. It is not ordinary page printing. A shipping, inventory, specimen, or shelf label can fail operationally if content shifts a few millimeters or targets the wrong stock.

## Decision Boundary
Bind label template to physical dimensions, orientation, margins/gaps, DPI, and supported printer/stock capabilities. Preview at logical scale but make real dimensions explicit; screen pixels are not evidence of physical fit. Validate barcode quiet zones, text size, line wrap, and required fields before printing. Support copies/batches without turning one logical label identity into duplicate records unless domain workflow says each copy is unique.

Calibration/test print should be separate from production commit and clearly marked to avoid accidental use. Thermal printer darkness/speed may be device settings owned by driver; expose only when app has authoritative control. Reprints can have audit or duplicate-label consequences in logistics/medical domains and need domain handoff.

## Failure Topology
- Template is designed in CSS pixels and prints at wrong physical size.
- A long address wraps into barcode quiet zone.
- App allows label stock incompatible with selected printer width.
- Test/calibration print looks identical to production label and is accidentally used.
- Reprint creates a new tracking identifier instead of reproducing the original label.
- Batch copies are sent before the printer's media size is confirmed.

## Falsification and Recovery
Test supported stock sizes, DPI, long text, barcode scanning after print, orientation, calibration offset, multiple copies, reprint, printer mismatch, and physical measurement. The design fails if screen preview cannot predict required physical dimensions or machine-readable elements become invalid after printing.

Recover by using physical-unit templates, capability checks, barcode/layout validation, explicit calibration mode, and domain-aware reprint semantics. Verify actual printed labels with ruler/scanner where correctness depends on physical output.

## Output Contract
Return `label-printing-contract` with template physical geometry, printer/stock capability, DPI/orientation, content/barcode fit validation, calibration mode, copies/reprint semantics, and physical-output verification cases.
