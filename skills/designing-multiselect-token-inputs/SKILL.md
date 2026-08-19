---
name: designing-multiselect-token-inputs
description: Use when users select many values into a compact field and the interface must coordinate token identity, text search, keyboard deletion/reordering, overflow and accessible selection state.
---

# Designing Multiselect Token Inputs

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns controls that combine a multi-value collection with search/entry, often rendered as chips/tokens inside or near an input. It does not decide tag taxonomy, permission to create new values, or domain-specific duplicate rules.

## Decision Boundary
Model the selected collection separately from the text query. Tokens are committed values with stable IDs; the text caret edits the query or, when explicitly supported, edits a selected token. Backspace on an empty query can move focus to the previous token before deletion rather than instantly destroying it, especially when deletion has consequences.

Decide whether order matters. Recipient order, workflow stages and priority labels may be ordered; ordinary tags may be sets. Do not add drag/reorder mechanics when the domain is unordered. If order matters, keyboard-accessible reordering and clear position feedback are required.

Overflow deserves its own design. Hundreds of tokens cannot expand a form indefinitely. Possible strategies include wrapping to a bounded area, summary count, collapsed tokens, or dedicated management surface. Any compression must preserve a route to inspect and remove individual selections.

Search suggestions should exclude, mark or allow already-selected items according to domain rules. Free-created tokens need parsing, normalization, duplicate detection and validation before commitment.

## Failure Topology
- Backspace deletes the last token while the user intended to edit text.
- Visual chip order implies priority although the data is an unordered set.
- Collapsed `+12` summary has no accessible route to inspect those twelve values.
- Duplicate labels with different IDs become indistinguishable.
- Screen reader focus jumps between input and chips unpredictably.
- Pasting a comma-separated list creates partially invalid tokens with no recovery.

## Falsification and Recovery
Test empty query + Backspace, arrow movement among tokens, 1/20/200 selections, duplicate labels, paste, IME, invalid new values, reordering, screen reader and narrow viewport. The skill fails if users cannot tell query focus from token focus or cannot recover individual values after overflow compression.

Recover by separating collection/query state, making deletion two-step where needed, exposing stable labels/metadata for ambiguous tokens and moving very large collections to a dedicated manager.

## Output Contract
Return `multiselect-token-input-contract` with collection semantics, order policy, token focus/deletion model, query/suggestion behavior, creation/validation rules, overflow strategy, reordering alternative, accessibility announcements and stress tests.