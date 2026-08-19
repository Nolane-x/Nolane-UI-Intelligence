---
name: designing-formula-authoring
description: Use when users author expressions referencing cells, ranges, fields or functions and the interface must support syntax, reference acquisition, autocomplete, error diagnosis and evaluation state without pretending formula text is plain input.
---

# Designing Formula Authoring

## Parent Contract
**Required parent:** `designing-spreadsheet-interfaces`.

This faculty owns formula authoring UX. The calculation engine, security sandbox and mathematical correctness are external authorities whose results must be surfaced faithfully.

## Decision Boundary
A formula editor is a structured expression environment. Track raw source, tokenization/parse state, referenced entities, evaluation state and committed result separately. The user may be editing syntactically incomplete text that should not be treated as a final error until commit or a stable parse boundary.

Reference acquisition is a key interaction. While editing `=SUM(`, clicking/dragging a range can insert a reference instead of changing active edit target. Use distinct visual outlines for each referenced range, keep source caret visible, and provide a clear way to return from reference-picking to text editing. Cross-sheet references must identify sheet context unambiguously.

Autocomplete should know parser position: function names, field names, named ranges and arguments are different suggestion domains. Show signatures/argument position without covering the cells users are referencing. Keyboard acceptance must not steal operators or delimiters the parser expects.

Errors need diagnosis: syntax, unknown name, invalid type, circular dependency, unavailable external data, permission or evaluation failure. Do not collapse all into `#ERROR` without actionable provenance where the engine can provide it.

## Failure Topology
- Clicking a cell while typing a formula ends editing instead of inserting a reference.
- Autocomplete inserts a function but leaves malformed parentheses/comma syntax.
- Color-coded range references are the only mapping cue and become unreadable with many ranges.
- Circular dependency appears as a generic invalid-value toast detached from the cell graph.
- Slow external formula result shows stale previous value without pending state.
- Parser flags every intermediate keystroke as an error and creates visual noise.

## Falsification and Recovery
Author nested functions, multiple ranges, cross-sheet references, incomplete syntax, circular references, external/async functions, rename referenced fields and use keyboard/screen reader. The contract fails if the source expression and highlighted references can diverge without warning.

Recover by parser-aware editing state, stable reference IDs, structured error classes, explicit pending/evaluation state and source/result separation.

## Output Contract
Return `formula-authoring-contract` with source/parse/evaluation states, reference-picking mode, reference visualization, autocomplete/signature behavior, commit policy, error taxonomy, async evaluation treatment and expression-reference parity tests.