---
name: designing-component-state-evidence-matrices
description: Use when a component has many semantic, interaction, validation, permission, async, or accessibility states and verification needs an explicit matrix showing which meaningful states must be rendered and evidenced rather than relying on a happy-path screenshot.
---

# Designing Component State Evidence Matrices

## Evidence ownership
Components fail in states that design reviews rarely capture: keyboard focus after validation, disabled-but-explained controls, permission-denied variants, partial data, pending destructive actions, selected rows during refresh, or errors inside nested composition. This skill owns the matrix that decides which component states are materially distinct enough to require evidence.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent establishes how claims bind to evidence. This specialist starts when the claim concerns a component whose correctness depends on combinations of state rather than one static render.

## Matrix construction
Begin from semantic state dimensions, not screenshots. Useful dimensions include availability, focus, selection, validation, async status, permission, content shape, input modality, and relationship to surrounding components. The decision owner is the pruning rule: include combinations that create different behavior, meaning, focus path, or failure risk; reject Cartesian combinations whose semantics are equivalent.

Each admitted cell records the state predicate, trigger path, expected invariant, evidence type, and status. Cells may be represented by rendered snapshots, runtime assertions, accessibility tree captures, interaction traces, or combined artifacts. One artifact can satisfy several cells only when it proves the relevant invariant for each.

## Avoiding matrix inflation
A matrix is not a quota. If hover plus a remote permission state cannot co-occur, do not invent the combination. If four data sizes share identical behavior, use a representative plus boundary cases. Conversely, keep rare states when they own a distinct risk—such as error during a destructive confirmation or focus restoration after async completion.

Prioritize transitions as well as resting states. A component can look correct in both before and after screenshots while failing during the transition, for example losing focus when validation appears or permitting a double submit while pending.

## Evidence requirements
Strong evidence names the component revision, fixture or data identity, environment, state predicate, and expected invariant. For interactive states, include the event path that reached the state; a directly forced CSS class may prove styling but not reachability. For accessibility-sensitive states, pair visual evidence with semantic/runtime evidence.

## Failure modes
Characteristic Failure includes a gallery of visually different variants with no semantic coverage model, exhaustive combinatorics that hides important cells in noise, happy-path-only snapshots, unreachable fixture states, and matrices that omit transitions. Another failure is stale evidence: the matrix says a cell is covered but the artifact was captured from an older component contract.

## Falsification
Remove one material state, mutate a transition, make a permission state unreachable, and change a component revision without updating fixtures. The contract is falsified if the matrix still reports complete coverage, if a cell can be marked covered without reaching its predicate, or if semantically distinct failure states collapse into one representative without justification.

## Recovery
Rebuild dimensions from the current state machine, map existing artifacts to cells by revision and predicate, and mark unmatched cells unknown rather than inferring coverage. Prune redundant cells only with an explicit equivalence rationale. Route newly discovered state behavior back to the component owner before generating new evidence.

## Output and Handoff
Output: `component-state-evidence-matrices-contract`, containing dimensions, admitted cells, pruning rationale, state predicates, artifact bindings, transition coverage, and freshness rules. Handoff story construction to story-state fixture coverage and cross-environment expansion to browser/device evidence matrices.

## Sibling Boundary and delete-the-skill
Sibling interaction-regression evidence focuses on behavioral sequences across revisions; this skill defines state-space coverage for one component contract. Visual regression baselines compare pixels but do not decide which semantic states deserve baselines. The delete-the-skill test passes because without a state matrix, evidence quantity can grow while material component states remain completely unverified.