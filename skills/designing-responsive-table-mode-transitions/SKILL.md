---
name: designing-responsive-table-mode-transitions
description: Use when a table cannot preserve its full row-column geometry at constrained widths and the interface must change mode while retaining comparison, row identity, sorting/filtering context, and action meaning.
---

# Designing Responsive Table Mode Transitions

## Task Before Geometry
A narrow viewport does not justify converting every table to cards. The key question is what users do with the table: compare columns, scan trends, select rows, inspect one record, or act on multiple records. This skill owns the mode transition that preserves those tasks when full geometry no longer fits.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent governs adaptation. Data-grid behavior such as sorting and selection remains with existing data interaction owners; this specialist preserves those semantics while representation changes.

## Mode Decision
Classify columns by comparison criticality, identity role, action role, and optional detail. Candidate modes include horizontal preservation with intentional scrolling, pinned identity columns, selective column disclosure, row-detail expansion, stacked record summaries, or a dedicated record view. Choose based on task, not fashion.

Any transformed mode must keep row identity and the meaning of active sort/filter/selection. If a card representation hides the column that defines the current sort, expose that ordering context elsewhere.

## Evidence
Evidence includes realistic wide data, long headers/values, multi-select, sorted/filtered states, row actions, keyboard traversal, and transitions while a row is selected or expanded. Compare task completion between wide and constrained modes, not only screenshot neatness.

## Failure Modes
Failure includes stacked cards that make cross-record comparison impossible, hidden sort keys, row actions detached from the correct identity, selection cleared on transition, horizontal scrolling with no persistent row/column anchor, and different filtering semantics between representations.

## Falsification
Falsification asks for the same comparison and row-action tasks on both sides of the breakpoint, then transitions while sort/filter/selection are active. If the user must infer missing context or loses state solely because representation changes, the contract fails.

## Recovery
Recovery restores the task-critical dimension, keeps a stable row identity model, and chooses a less destructive mode such as controlled horizontal scrolling when comparison is fundamental. If constrained use requires a different workflow, declare that product decision explicitly rather than pretending it is the same table.

## Output
Output: `responsive-table-mode-transitions-contract` with preserved tasks, column priority, state mapping, transition rules, and comparative evidence.

## Handoff
Handoff base table semantics and virtualization to data-grid specialists; handoff generic threshold selection to content-pressure breakpoint design.

## Sibling Boundary and delete-the-skill
Priority collapse can hide regions but does not understand row-column comparison invariants. Removing this skill leaves responsive representation change for tabular tasks without a material owner.