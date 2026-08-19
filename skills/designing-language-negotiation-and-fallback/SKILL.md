---
name: designing-language-negotiation-and-fallback
description: Use when the product must choose an initial language or resolve missing translations from browser, account, content, workspace, or regional signals without surprising explicit user choice.
---

# Designing Language Negotiation and Fallback

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns automatic language resolution before or beneath explicit locale selection. It defines signal precedence, language-tag matching, fallback chains, and how partial translation gaps are surfaced. It does not decide the wording of translated strings.

## Decision Boundary
List available language resources using precise language tags rather than informal names. Define how exact tags, script variants, and broader parent languages resolve. A request for `pt-BR` may fall back differently from `pt-PT`; Chinese script variants must not be collapsed merely because they share a language family. Explicit user choice outranks inference unless an authoritative product scope says otherwise.

Fallback can occur at product, route, resource, or content level. Avoid mixing languages string-by-string when a more coherent page-level fallback is possible, but do not hide critical actions because one translation key is missing. Make fallback observable in diagnostics and quality review without exposing internal keys to end users. User-generated or authored content language is separate from shell language and may require its own labeling.

## Failure Topology
- Browser negotiation overrides a previously saved explicit language on every visit.
- A missing regional resource falls back to a linguistically inappropriate variant.
- Some buttons expose untranslated localization keys while neighboring copy falls back correctly.
- Language tags are compared as raw strings and ignore script or region subtags.
- A partial translation silently mixes three languages on one critical transaction screen.
- Search/index language follows shell language even when the underlying content is in another language.

## Falsification and Recovery
Exercise a matrix of browser preferences, account choices, supported/unsupported region variants, missing bundles, signed-out/signed-in transitions, and partially translated routes. Inspect the resolved language tag for every stage. The design fails if the same inputs resolve nondeterministically or if a lower-authority inference replaces an explicit user choice.

Recover by publishing a deterministic precedence and fallback chain, normalizing language tags, distinguishing shell and content languages, and defining bounded fallback granularity. Instrument missing-resource fallbacks so quality teams can eliminate accidental mixed-language experiences instead of treating them as harmless runtime behavior.

## Output Contract
Return `language-negotiation-fallback-contract` with input signals, precedence, tag matching, script/region fallback graph, resource granularity, explicit-choice protection, missing-resource behavior, observability, and negotiation test matrix.
