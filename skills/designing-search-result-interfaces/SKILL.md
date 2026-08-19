---
name: designing-search-result-interfaces
description: Use when search results must communicate match quality, ranking, provenance, snippets, result types, actions, and no-result recovery without pretending ranking is objective truth.
---

# Designing Search Result Interfaces

## Parent Contract
**Required parent:** `designing-search`.

This faculty owns how returned matches are interpreted and acted on after a query is executed. It does not own query parsing or filter construction. Its job is to make result identity, relevance cues, type, context, and next action legible while respecting uncertainty in ranking.

## Decision Boundary
Define the result unit by the search domain: document, person, product, command, message, setting, event, or mixed entity. Mixed search requires type differentiation and grouping/ranking policy; a universal undifferentiated list makes similarly named objects dangerous. Titles, metadata, path/context, and snippets should answer why a result is relevant without forcing users to open each item.

Highlighting must reflect actual matched terms or semantic evidence and remain readable. Do not highlight substrings that distort words or imply an exact lexical match when retrieval was semantic. Ranking explanations can be lightweight—recency, exact title match, in current workspace—but should never reveal sensitive scoring data or claim certainty the system does not have.

No-results is a query-repair state, not an empty-state illustration. Preserve the query, expose active filters, identify whether scope or spelling may be constraining results, and offer bounded alternatives. If partial indexes or permissions exclude data, disclose the search scope without leaking inaccessible object existence.

## Failure Topology
- Mixed results omit type/context, causing users to open the wrong same-named object.
- Semantic results highlight unrelated lexical fragments and imply false evidence.
- Sponsored or promoted results are visually indistinguishable from relevance-ranked results.
- No-results clears the query and removes the evidence needed to repair it.
- Restricted results leak object titles through snippets despite permission boundaries.
- Result actions differ from the canonical object actions elsewhere in the product.

## Falsification and Recovery
Falsify with duplicate names across types, typo queries, semantic matches without exact terms, active filters producing zero results, permission-restricted content, very long snippets, keyboard navigation, screen-reader result counts, and result updates while the query remains focused. The design fails if users cannot identify what a result is and why opening it is plausible before activation.

Recover by defining result schemas per type, showing contextual metadata, binding actions to canonical object operations, making ranking/promotions legible, preserving repairable query state, and constraining snippets to authorized content.

## Output Contract
Return `search-result-interface-contract` with result schemas, mixed-type policy, ranking cues, match highlighting semantics, metadata/snippet rules, action bindings, count/update announcements, no-result repair behavior, permission boundaries, and falsification cases.