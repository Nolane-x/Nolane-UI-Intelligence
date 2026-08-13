---
name: designing-search
description: Use when users need to find, filter, rank, refine, recover, or navigate large or uncertain information spaces through query-driven interaction.
---

# Designing Search

## Overview
Search is a query lifecycle, not a text box. Design query formulation, system interpretation, result scanning, refinement, and recovery as one interaction.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require enough IA to know what can be searched and how result types relate.

## Query model
Define:
- searchable entities/fields
- exact vs fuzzy matching expectations
- synonyms/aliases/domain vocabulary
- prefix/autocomplete behavior
- scope: current context vs global
- permission filtering
- version/time/environment context
- whether queries are transient, shareable, or saved

Never display results a user lacks permission to open just because the index can retrieve them.

## Input behavior
Clarify when search executes: submit, debounce, instant local filtering, or hybrid. Preserve the user’s query during loading/error/refinement. Keyboard behavior must distinguish suggestion navigation from normal cursor editing.

Autocomplete suggestions should have a reason: recent queries, entities, commands, categories, or completions. Do not mix types without visible differentiation.

## Result architecture
Optimize for the dominant decision:
- navigation result → strong title/context/path
- comparison result → aligned metadata
- knowledge result → useful snippet/highlight
- action result → explicit action semantics

Make ranking cues understandable when order has meaningful logic. Do not imply precision the search system does not have.

## Filters and facets
Filters narrow the current query; sorting changes order. Keep these semantics distinct. Show active filters, result impact, and a reversible clear path. Preserve query unless changing scope logically invalidates it.

For many facets, prioritize high-discrimination/high-frequency dimensions rather than exposing the whole database schema.

## States
Design: initial/empty, suggestions, loading, partial/streaming if relevant, results, zero results, corrected query, unavailable/error, permission-limited, and stale-index states when the product exposes them.

Zero results should preserve the query and offer relevant recovery: broaden scope, remove filters, fix syntax, or navigate to a known destination. Do not replace it with generic encouragement.

## Search vs navigation
If users repeatedly search for the same top-level destinations, the IA may be failing. Search can complement navigation but should not conceal an incoherent taxonomy.

## Output: `search-contract`
Return `corpus`, `scope_model`, `query_lifecycle`, `suggestion_types`, `result_schema`, `ranking_cues`, `filter_facets`, `sorting`, `keyboard_model`, `state_model`, `permission_behavior`, `shareability`, and `recovery_paths`.

## Common failures
- Query cleared after a recoverable error.
- Loading state replaces the whole page and destroys context.
- Filter chips with ambiguous removal/AND/OR semantics.
- “No results” without showing which scope/filters produced it.

## V6 Search Relevance and Recovery Model
Start with a **query-intent model**: exact lookup, navigational search, exploratory discovery, troubleshooting, command invocation, fuzzy recall, or domain-specific syntax. The intent determines indexing, ranking, filters, snippets, keyboard behavior, and whether instant results are appropriate.

Define a **result-confidence contract**: when the system can claim an exact match, when it should expose uncertainty, how spelling/fuzzy expansion is communicated, and when no result is safer than a weak result. Preserve user control with **facet-state persistence** across pagination, back navigation, shareable URLs, saved views, and object opening/return.

Design a **zero-result recovery strategy** based on why zero happened: restrictive filters, typo, stale index, permissions, unsupported syntax, or genuinely absent data. Offer the smallest truthful relaxation rather than generic “try again.” For adaptive/ranked systems, define a **ranking-feedback loop**: what behavioral signals may influence ranking, how bias/feedback loops are bounded, and how users can understand or override surprising ordering.

### Falsification
Test misspellings, ambiguous names, exact identifiers, no permission, stale indexed objects, all filters active, long multilingual queries, and keyboard-only result traversal. A plausible-looking but wrong top result is a relevance failure, not UI polish.

### Recovery
Expose scope and filter state, repair indexing/ranking assumptions, or fall back to deterministic ordering where confidence is insufficient. Never manufacture results to avoid an empty state.
