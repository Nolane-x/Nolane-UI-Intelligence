---
name: designing-mixed-direction-text
description: Use when user names, URLs, code, numbers, identifiers, or embedded foreign-language phrases can mix RTL and LTR runs and punctuation must remain intelligible without corrupting content order.
---

# Designing Mixed-Direction Text

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns presentation and isolation of bidirectional text runs inside a larger directional interface. It does not own overall page mirroring. The failure it prevents is subtle: surrounding punctuation, labels, numbers, or user-generated text can reorder visually even when the underlying string is correct.

## Decision Boundary
Identify content whose direction is known, inferred, or inherently LTR/neutral: email addresses, URLs, file paths, phone numbers, code, timestamps, transaction IDs, and arbitrary user text. Use semantic isolation so embedded runs do not leak directional influence into neighboring labels or punctuation. Prefer content-driven direction for unknown user-generated strings while keeping control chrome anchored to the interface locale.

Editable fields need additional care because caret movement and selection expose logical versus visual order. Prefix/suffix decorations such as currency symbols, units, @mentions, and punctuation should be separate semantic elements when concatenation creates bidi ambiguity. Do not mutate stored content by injecting visible directional characters as a display hack unless the data contract explicitly supports them.

## Failure Topology
- An Arabic sentence containing a URL places closing punctuation on the wrong visual side.
- A transaction ID appears reordered next to an RTL label, causing copy errors.
- Phone or account numbers visually merge with adjacent text.
- User-generated LTR text inherits RTL alignment and becomes hard to edit or select.
- Hidden direction characters are persisted into copied identifiers and break downstream validation.
- A prefix icon/symbol changes apparent ownership when text direction differs from the shell.

## Falsification and Recovery
Test real strings combining Arabic/Hebrew, Latin words, numbers, emoji, punctuation, URLs, code, names, and empty/unknown content. Verify display, caret navigation, selection, copy/paste, truncation, and screen-reader output. The design fails if users can misread or copy a materially different identifier because visual bidi ordering is ambiguous.

Recover by isolating embedded directional runs, applying semantic `dir` behavior at the content unit, separating decorations from raw strings, and avoiding storage-layer direction marks. Maintain a bidi stress corpus because invented reversed-English samples do not expose real Unicode behavior.

## Output Contract
Return `mixed-direction-text-contract` with content classes, known/unknown direction rules, isolation boundaries, editable-field behavior, prefix/suffix handling, copy/storage constraints, truncation rules, and multilingual bidi stress cases.
