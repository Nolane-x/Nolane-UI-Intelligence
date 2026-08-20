---
name: designing-locale-aware-search
description: Use when search matching must respect language-specific case folding, accents, segmentation, morphology, scripts, transliteration, and user expectations instead of applying one English tokenization strategy globally.
---

# Designing Locale Aware Search

## Parent Contract
**Required parent:** `designing-search`.

This faculty owns linguistic matching behavior, not the visual search-results layout. It defines how query text is normalized, segmented, expanded, transliterated, and ranked across supported languages while protecting exact identifiers from destructive normalization.

## Decision Boundary
Classify searchable fields: natural language, person names, exact IDs, codes, filenames, or mixed content. Natural language may benefit from locale-aware case folding, diacritic tolerance, stemming, segmentation, and synonym resources. Exact identifiers often must remain exact or offer a separate normalized mode. Languages without whitespace word boundaries require real segmentation rather than splitting on spaces.

Transliteration can increase recall across scripts but may introduce collisions; rank original-script exact matches above loose transliterations and show why a result matched when ambiguity is high. Search locale can follow content language, query detection, explicit scope, or viewer setting depending on corpus. Do not assume shell language equals document language.

## Failure Topology
- Turkish dotted/dotless I handling follows English lowercasing and misses valid matches.
- CJK queries are tokenized only on spaces and return poor results.
- Accent removal improves names but corrupts exact product codes that distinguish characters.
- Transliteration causes unrelated names to rank above exact same-script matches.
- Server and local cached search use different normalization.
- Search switches analyzers when UI locale changes even though the corpus language stays constant.

## Falsification and Recovery
Create language-specific query/corpus fixtures covering case, accents, inflection, compounds, no-space scripts, transliteration, mixed scripts, typos, and exact identifiers. Evaluate recall and false-positive behavior, not just whether some result appears. The design fails if normalization that helps one field silently damages another semantic class.

Recover by assigning analyzers per field/content language, separating exact and linguistic matching, ranking stronger evidence above transliterated/expanded matches, and making analyzer selection explicit. Preserve raw query for display and audit while normalized forms remain internal.

## Output Contract
Return `locale-search-contract` with searchable field classes, analyzer/locale selection, case/diacritic/segmentation rules, transliteration policy, exact-ID protections, ranking precedence, and multilingual relevance fixtures.
