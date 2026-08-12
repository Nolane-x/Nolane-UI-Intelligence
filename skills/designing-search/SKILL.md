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
