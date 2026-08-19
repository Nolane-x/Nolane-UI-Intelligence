---
name: designing-phone-number-entry
description: Use when a product collects telephone numbers and must preserve international dialing meaning, country context, editable formatting, and verification without assuming a domestic mask.
---

# Designing Phone Number Entry

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns human entry and interpretation of telephone identifiers. It does not decide whether a phone number is required as an identity factor; authentication policy belongs to the trust owners. Its job is to prevent formatting convenience from corrupting international meaning.

## Decision Boundary
Separate the user-visible national form from the canonical dialing representation. Country context may come from an explicit selector, an already-known account locale, or a leading international prefix, but inferred geography must remain correctable. Do not silently convert a number using IP country or device locale when the person is entering a number from elsewhere.

Formatting should be reversible. Spaces and punctuation can aid readability, but cursor behavior must not fight editing and paste must accept common human formats. Avoid rigid masks that reject legitimate length variation or extensions. If extensions are supported, model them separately from the primary number unless the downstream system explicitly accepts combined notation.

Verification is a separate state from syntactic plausibility. A number can parse correctly but fail SMS delivery, be unreachable, be a landline, or belong to another person. The interface must not label a parsed number “verified.” When sending a code, show a safely masked destination and provide a path to correct it without forcing the entire flow to restart.

## Failure Topology
- Domestic mask rejects valid international lengths.
- Country code is auto-selected from IP and cannot be corrected before normalization.
- Pasting `+` notation duplicates the selected country prefix.
- Formatting logic jumps the caret and makes mid-string edits nearly impossible.
- A successful parse is presented as proof of ownership.
- Resend controls enable abuse or hide which destination receives the code.

## Falsification and Recovery
Falsify with international prefixes, leading national zeros, variable-length numbers, extensions, copied numbers containing punctuation, RTL locale presentation, keyboard-only country selection, rapid country changes, and a verification attempt after editing the number. The design fails if canonical output differs from the number the user intended or if verification state survives a material number change.

Recover by using explicit country context, parse/format libraries as bounded mechanisms rather than policy authorities, stable editable formatting, separate verification state, and invalidating ownership evidence whenever the canonical number changes.

## Output Contract
Return `phone-entry-contract` containing country-context rules, accepted input forms, canonical representation, display formatting, paste/caret behavior, extension policy, parse-vs-verification states, correction/resend behavior, privacy masking, and international falsification cases.