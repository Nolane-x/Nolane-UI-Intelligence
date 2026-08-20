---
name: designing-graph-search-and-navigation
description: Own finding, revealing, jumping to, and returning from graph entities or paths without losing structural context, especially across collapsed or virtualized regions.
---
# Designing Graph Search and Navigation

## Decision ownership

Own locate-and-move behavior inside a graph. Decide searchable fields, result disambiguation, reveal behavior through collapsed containers, viewport jumps versus animated travel, next/previous match semantics, navigation history, breadcrumbs or focus stacks, and how path results remain understandable. This owner does not decide global product search outside the graph.

## Inputs and evidence

Require node/edge identity fields, labels and aliases, graph size, collapsed-container rules, virtualized rendering, common search queries, duplicate names, path/hierarchy metadata, and whether search results can refer to hidden or permission-restricted content. Determine whether users need fuzzy matching, structured filters, or exact identifiers.

## Procedure

Index semantic identity separately from what is currently rendered so virtualization does not make nodes unsearchable. Results must carry enough context—type, parent/container, path, identifier—to disambiguate duplicate labels. Selecting a hidden result should reveal the minimum ancestor chain and place the target in a stable viewport location with a temporary locator highlight. Preserve the previous viewport/selection in navigation history. Provide next/previous match within the current query without repeatedly zooming to disruptive scales. For edge/path matches, reveal endpoints and enough surrounding structure to interpret the relationship.

## Failure topology

Failures include search only covering visible nodes, duplicate labels with indistinguishable results, jumping to a hidden node without expanding its parent, zooming so far in that users lose all context, search highlights disappearing instantly, and no back navigation to the previous investigation. Permission failures occur when result counts leak inaccessible graph entities.

## Falsification

Reject if a known off-screen virtualized node cannot be found; if two same-named nodes cannot be distinguished before selection; if selecting a result destroys the previous viewport with no back path; if a result inside a collapsed subgraph remains invisible; if search reveals restricted entity names through snippets/counts; or if next/previous matching causes uncontrolled zoom oscillation.

## Output contract

Return a `graph-search-and-navigation-contract` containing: indexed fields; query modes; result context fields; duplicate disambiguation; hidden-result reveal protocol; locator/highlight duration; viewport transition; navigation history; match iteration; edge/path result handling; permission filtering; and large-graph performance expectations. Include one hidden result and one duplicate-name scenario.

## Handoffs

Use subgraph/container owners to reveal ancestry, minimap for overview orientation, large-graph virtualization for render strategy, and dependency/topology specialists for domain-specific result context. Global product search may deep-link into this contract but does not replace it.