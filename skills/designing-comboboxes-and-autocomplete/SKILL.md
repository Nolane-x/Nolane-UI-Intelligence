---
name: designing-comboboxes-and-autocomplete
description: Use when an input combines text entry with suggested or allowed values and the design must reconcile freeform editing, popup selection, async suggestions, keyboard focus and accessible combobox semantics.
---

# Designing Comboboxes and Autocomplete

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns editable/select-only combobox interaction and autocomplete behavior. It does not decide the underlying data vocabulary, search engine quality or form-level validation policy.

## Decision Model
Choose the value contract first. Is the final value restricted to a known option, or may arbitrary text be submitted? That single decision changes blur behavior, validation, selection commitment and how typed text relates to the highlighted suggestion.

Separate three things that are often conflated: **input text**, **active suggestion**, and **committed value**. Arrow movement may change active suggestion without changing the text; Enter or another commit action may accept it. In inline-completion variants, the proposed completion must remain visually/semantically distinct from characters actually typed.

Choose popup content appropriate to the task: listbox for simple options, grid for options with multiple descriptive fields, tree for hierarchical values, dialog for complex date/location selectors. Preserve the focus model of the chosen pattern; in common list/grid/tree combobox patterns, DOM focus can remain in the input while assistive focus is conveyed through the active descendant.

Async suggestions require request identity, loading, stale-response rejection and empty/error treatment. Avoid clearing useful prior suggestions on every keystroke if it causes flicker, but never let an old response overwrite a newer query. Debounce for backend cost without making typing feel unresponsive.

## Failure Topology
- Typed text looks committed even though only predefined options are legal.
- Arrow navigation changes the input value irreversibly before selection.
- A slow earlier network response replaces results for the latest query.
- Escape closes the popup but also erases user text unexpectedly.
- The control has combobox visuals but behaves like a menu, breaking text editing keys.
- Highlight and actual selected value are indistinguishable to screen reader users.

## Falsification and Recovery
Test freeform vs restricted mode, partial queries, no result, async races, IME composition, paste, Home/End, Escape, Tab, pointer selection, screen reader and zoom. The contract fails if focus/selection/value states cannot be named independently at every step.

Recover by making the value contract explicit, separating typed/highlighted/committed state, canceling stale requests and aligning roles/keyboard behavior with the popup primitive.

## Output Contract
Return `combobox-autocomplete-contract` with value policy, text/highlight/value state model, popup role, filtering/autocomplete behavior, keyboard/focus rules, async lifecycle, commit/cancel behavior, validation handoff and accessibility tests.