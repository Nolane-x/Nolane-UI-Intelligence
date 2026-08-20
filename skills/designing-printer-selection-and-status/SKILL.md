---
name: designing-printer-selection-and-status
description: Use when users print through one or more printers and the interface must reconcile system printer discovery, saved choice, readiness, capabilities, queue state, and error recovery without pretending submission equals physical output.
---

# Designing Printer Selection and Status

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns selecting a printer and representing its operational status. It does not own print-preview composition or label layout. Printing crosses app, OS spooler, network, printer, paper/ink, and physical output; the UI must bound what it can observe.

## Decision Boundary
Use system print dialogs when they are the platform authority unless product-specific devices require embedded selection. Persist a printer only when identity is stable and scope makes sense. Display capability constraints such as color, duplex, media size, label stock, or secure print before allowing incompatible settings. Distinguish ready, offline, busy, paused, unknown, and app-inaccessible states.

Submitting a job to the spooler is not proof the paper printed. Phrase confirmation according to available evidence: “Sent to printer” versus “Printed.” Provide a path to system queue/status when deeper recovery is OS-owned. If a saved printer disappears, do not silently send to a different default for sensitive jobs.

## Failure Topology
- “Print complete” appears immediately after creating a spool job.
- Saved printer ID points to a different device after driver reinstall.
- Color/duplex settings remain selectable on a printer that lacks them.
- Offline printer is reported as generic document error.
- Sensitive job silently falls back to another shared default printer.
- App invents a duplicate queue UI that disagrees with OS spooler state.

## Falsification and Recovery
Test no printer, multiple identical names, offline/busy, capability changes, saved device removal, system-dialog cancellation, spooler acceptance/failure, and physical printer errors where observable. The design fails if output success is claimed beyond evidence or if device substitution occurs without user awareness.

Recover by respecting system authority, capability-filtering settings, scoping persisted identity, labeling submission versus physical completion, and linking to OS queue/recovery. Require explicit re-selection for sensitive output when the chosen device disappears.

## Output Contract
Return `printer-selection-status-contract` with selection authority, printer identity/persistence, capability matrix, status taxonomy, submit-versus-print evidence, fallback prohibition/allowance, system-queue handoff, and printer verification cases.
