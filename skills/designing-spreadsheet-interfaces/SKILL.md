---
name: designing-spreadsheet-interfaces
description: Use when a product exposes spreadsheet-like work with cells, ranges, formulas, multiple sheets, fill operations and dense keyboard navigation rather than a conventional editable table.
---

# Designing Spreadsheet Interfaces

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns the spreadsheet workspace as a coherent interaction system. Cell editing, formulas, frozen panes, sorting/filtering and virtualization route to specialist children. It does not define calculation semantics or file-format compatibility.

## Decision Boundary
A spreadsheet is not “a data grid with more columns.” It combines a two-dimensional addressable cell space, active cell, one or more selected ranges, formula/value duality, row/column operations, often multiple sheets and a command model optimized for keyboard repetition. Preserve those invariants before adding visual polish.

Model the workbook hierarchy: workbook → sheet → row/column coordinates → cell identity/value/formula/format. Decide what survives structural changes. Inserting a row may shift address-based references while object/table references can remain semantic; the UI must reflect the engine’s actual reference model rather than pretending all coordinates are stable IDs.

Navigation is a power path. Arrow keys move active cell, modifiers extend ranges, Enter/Tab can commit and move according to conventions, Home/End/Page keys navigate extents, and name box/go-to/search can reach distant cells. Keep only a small number of elements in the page Tab sequence if the grid uses managed focus; thousands of tabbable cells are not usable.

Differentiate active cell, selected range, copied range, formula-reference range, error cell, protected cell and collaborator presence. Color alone is insufficient when multiple outlines overlap.

Workspace chrome—formula bar, row/column headers, sheet tabs, status/aggregate summary, name box—must be task-justified and synchronized with the active cell/range. Mobile may require a radically different editing shell rather than shrinking desktop chrome.

## Failure Topology
- Every cell is a Tab stop and keyboard navigation becomes impossible.
- Active cell and selected range share one border, so copy/edit scope is ambiguous.
- Sorting a region breaks formulas because UI did not communicate reference semantics.
- Sheet tabs become tiny overflow chips with no searchable sheet navigation.
- Mobile exposes desktop ribbon density but no room to see data.
- Protected/read-only cells look disabled without explaining protection scope.

## Falsification and Recovery
Navigate 100k×100 cells, multi-range select, insert/delete rows, switch sheets, copy/paste, edit formulas, protect ranges, zoom, use screen reader and narrow viewport. The design fails if the active semantic coordinate or operation scope cannot be identified after a structural change.

Recover by restoring explicit workbook/cell/range state, managed focus, dedicated navigation commands and responsive re-authoring of editing chrome.

## Output Contract
Return `spreadsheet-interface-contract` with workbook/sheet/cell state model, active/selection layers, navigation grammar, workspace surfaces, structural-operation handoffs, protected/collaborative states, mobile transformation and large-sheet tests.