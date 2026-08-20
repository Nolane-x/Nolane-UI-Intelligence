---
name: designing-parametric-constraint-editing
description: Own driving and geometric constraint editing, including dependencies, degrees of freedom, conflicts, over/under-constrained state, expression links, solve feedback, and safe rollback.
---
# Designing Parametric Constraint Editing

## Decision ownership

Own the UI for constraints that drive geometry. Decide dimensional/geometric constraint creation, driving versus reference values, degrees of freedom, variable/expression linkage, solver state, conflicting/redundant constraints, edit propagation, and recovery from failed solve. Measurements alone do not alter geometry; this owner governs model intent.

## Inputs and evidence

Require constraint types, solver capabilities, parameter/variable system, units, dependency graph, degrees-of-freedom data, allowed expressions, history, and failure diagnostics. Identify assemblies/sketches where constraint scope differs.

## Procedure

Show whether a dimension is driving, driven/reference, or linked to an expression. When adding constraints, highlight affected geometry and predicted remaining degrees of freedom. Solver response must distinguish solved, under-constrained, over-constrained, inconsistent, redundant, and failed. Editing a driving value should preview propagation where feasible and preserve the old model until a valid solve commits. Conflict diagnosis should identify the minimal or likely constraint set rather than only "solve failed". Variable expressions need dependency/cycle validation and unit compatibility.

## Failure topology

Failures include a reference dimension mistaken for editable driver, geometry jumping after value entry with no preview, over-constraint error that identifies no conflicting constraints, solver failure corrupting the previous valid model, expression cycles, and unit-incompatible formulas accepted. Another failure is green "fully constrained" status while hidden components remain free due scope mismatch.

## Falsification

Reject if driving/reference state is ambiguous; if failed solve can replace the last valid geometry; if conflict diagnostics cannot localize relevant constraints; if expression cycles or unit mismatch can commit; if degrees-of-freedom scope is unclear; or if changing one parameter propagates to unexpected distant geometry with no dependency trace.

## Output contract

Return a `parametric-constraint-editing-contract` with: constraint taxonomy; driving/reference state; variable/expression model; unit validation; degrees of freedom; solver states; preview/commit; conflict diagnosis; dependency trace; cycle handling; rollback; and history. Include one over-constrained and one expression-cycle scenario.

## Handoffs

Measurements supply references, snapping supplies geometry targets, assembly constraints may extend this model, and history/modeling operations consume solved geometry.