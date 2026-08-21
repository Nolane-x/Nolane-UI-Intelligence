---
name: designing-responsive-form-reflow
description: Use when form fields, groups, help, errors, and actions reflow across responsive layouts and dependency order, labeling, validation context, and progress must remain semantically coherent.
---

# Designing Responsive Form Reflow

## Form Reflow Is Workflow Reflow
A form is an ordered decision sequence, not a bag of inputs. This skill owns responsive rearrangement of field groups, labels, help, summaries, and actions while preserving dependencies and completion state. Validation rules themselves remain with form/validation specialists.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent authorizes layout adaptation. This skill focuses on the semantic integrity of form workflow during that adaptation.

## Dependency Map
Record which fields reveal, constrain, or explain others; which fields form one conceptual group; where error messages attach; and which action commits the current scope. Multi-column desktop forms may collapse to one column, but source order must follow a valid dependency and reading sequence.

Inline labels may move above controls; side help may become disclosure; sticky action bars may become in-flow. Each transition requires a mapping for focus, validation summary links, and user-entered values.

## Evidence
Evidence includes keyboard traversal, screen-reader reading order, conditional fields, error states, long/localized labels, autofill, text scaling, and breakpoint changes with partially completed input. Verify that error-summary links still focus the correct field after reflow.

## Failure Modes
Failure includes dependent fields appearing before their controlling field, two-column source order reading across rows incorrectly, labels detached after layout switches, sticky submit obscuring the last input, help text moved so far that its field relationship is unclear, and input state remounted/lost at the breakpoint.

## Falsification
Falsification fills a partial form, triggers several validation errors, focuses a mid-form control, crosses the responsive threshold, and continues only by keyboard. Lost values, broken error links, incoherent order, or focus displacement to the page root falsifies the contract.

## Recovery
Recovery establishes semantic source order first, uses layout to create columns without changing control ownership, and preserves mounted state across presentation changes. If a narrow form genuinely needs a staged workflow, route to form-flow architecture rather than conditionally hiding arbitrary fields.

## Output
Output: `responsive-form-reflow-contract` with dependency order, group mapping, label/help transformations, focus/state continuity, action placement, and error-state evidence.

## Handoff
Handoff validation semantics to form validation specialists and threshold evidence to content-pressure breakpoint design.

## Sibling Boundary and delete-the-skill
Generic region reordering lacks form-specific dependency and validation relationships. Removing this owner leaves the semantic workflow of responsive form reflow unprotected.