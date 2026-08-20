---
name: designing-indicator-of-compromise-search
description: Use when analysts search hashes, domains, IPs, URLs, certificates, file names, or other indicators across heterogeneous telemetry and must distinguish exact matches, transformations, scope, and absence-of-evidence.
---
# Designing Indicator of Compromise Search

## Decision ownership

Own the query and result semantics for indicator hunting. Decide how an entered indicator is typed, normalized, transformed, scoped, and matched across sources; how exact, derived, historical, and fuzzy matches differ; and how the interface communicates incomplete telemetry. This faculty does not determine whether an indicator is malicious or author a detection rule. Its job is to prevent search mechanics from fabricating confidence.

## Inputs and evidence

Require supported indicator types, normalization rules, source-specific field mappings, retention periods, index freshness, tenant boundaries, wildcard/fuzzy capabilities, passive-DNS or reputation enrichments, and known transformations such as URL canonicalization, case normalization, defanged forms, punycode, or hash type inference. Gather searches that produce exact matches, no matches, enormous fan-out, ambiguous indicator typing, invalid syntax, stale index results, and results that exist only in one data source.

## Procedure

Classify the query before execution. If a token can represent multiple types, expose the interpretation instead of silently choosing one. Normalize reversible syntax—such as defanged domains—while retaining the original query. Separate exact telemetry matches from enriched associations: a domain resolving to an IP is not the same as the IP appearing in an endpoint event. Show source coverage and retention next to result counts so zero has context. Preserve time range, source filters, entity scope, and query transformations in the shareable search state. For very large result sets, prioritize aggregation that preserves distinct entities, first/last seen, source distribution, and confidence rather than arbitrary top-N truncation.

## Failure topology

- The interface auto-detects the wrong indicator type and silently returns misleading matches.
- A reputation-service association is presented as a local observation.
- “No results” implies the indicator never appeared despite missing or expired data sources.
- URL normalization collapses materially different paths or query values.
- Hash prefixes or fuzzy matches are mixed with exact cryptographic matches.
- Search filters disappear when analysts pivot from results into investigation.
- Massive result sets are truncated without showing what was excluded.

## Falsification

Search a defanged domain, an ambiguous hexadecimal string, a URL with meaningful query parameters, a known indicator outside one source's retention window, and an indicator with both direct observations and enrichment-only associations. Fail the design if users cannot distinguish those result classes or explain why zero results do not prove absence.

## Output contract

Return `indicator-of-compromise-search-contract` containing indicator typing, normalization transformations, match classes, source/retention coverage, query-state persistence, result aggregation, no-result semantics, enrichment boundaries, and adversarial search cases.

## Handoffs

Entity-centric investigation routes to `designing-security-entity-investigation`; relationship inference routes to `designing-security-event-correlation`; repeated hunt logic that should become detection routes to `designing-detection-rule-authoring`. Generic search/facet faculties provide mechanics but may not redefine security match truth.