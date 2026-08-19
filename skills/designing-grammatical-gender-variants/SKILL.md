---
name: designing-grammatical-gender-variants
description: Use when localized messages change grammar based on the grammatical gender of people, objects, roles, or referenced entities and the product must avoid unsafe inference or fragment assembly.
---

# Designing Grammatical Gender Variants

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns message-selection semantics where grammar requires gendered variants. It is not a policy for assigning human identity categories. It distinguishes grammatical metadata needed by a language from personal gender information and avoids inferring sensitive identity merely to satisfy a translation template.

## Decision Boundary
Identify which messages genuinely require gender agreement and what authoritative metadata is available. Product nouns may have known grammatical gender per locale; user-referenced people may not. Prefer neutral or rephrased messages when the necessary personal information is unavailable or inappropriate to collect. When variants are required, treat the whole sentence as a selectable translation unit so articles, adjectives, verbs, and word order can change together.

Do not derive gender from first names, avatars, honorific guesses, or account type. Some languages require agreement for objects but not people; others offer neutral strategies that differ by context. Translator tooling needs enough semantic context to know what the selector represents without exposing private user data.

## Failure Topology
- The UI guesses a person's gender from their name to choose a localized verb form.
- Code concatenates a gendered adjective with a separately translated noun and produces invalid agreement.
- “Other” becomes a catch-all grammatical variant that still assumes a binary human identity.
- Product-object grammatical gender is reused across languages where the noun changes gender.
- A translator sees opaque values like `m/f` without knowing whether they refer to actor, recipient, or object.
- Gender metadata leaks into analytics or UI where it is not otherwise needed.

## Falsification and Recovery
Review all gender-select messages with native-language experts and test missing/unknown metadata, product nouns, user references, plural combinations, and privacy-restricted contexts. The design fails if a message cannot render without inferring sensitive identity or if variants are fragments that prevent natural grammar.

Recover by rephrasing neutrally, separating grammatical object metadata from personal identity, using full-message select variants, and documenting selector semantics. Collect personal data only when independently justified by product requirements, never because the localization implementation is convenient.

## Output Contract
Return `grammatical-gender-contract` with gender-sensitive message inventory, metadata source/authority, neutral fallback strategy, full-message variant rules, privacy boundaries, translator context, and native-language verification cases.
