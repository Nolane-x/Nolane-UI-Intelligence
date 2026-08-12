---
name: maintaining-ui-domain-atlas
description: Use when a UI surface, modality, AI role, risk class, temporal behavior, or social context is absent from coverage, or when new research changes which skills own or verify an industry domain.
---

# Maintaining the UI Domain Atlas

## Overview
The atlas is a coverage model, not a taxonomy for browsing. It prevents false completeness by forcing NUI to represent UI work as orthogonal constraints that can combine in ways no product-category preset anticipates.

## Parent Contract
**Required parent:** `researching-ui-frontiers`.

A proposed atlas change must be supported by a new domain class, mechanism, or ownership gap. Synonyms and marketing categories do not justify new axes.

## Decision Model
Model interfaces across independent axes: surface, input modality, AI role, risk, temporal behavior, and social context. Ask whether the candidate changes design obligations. “Banking app” alone is not a new surface; it is usually mobile/web plus financial risk, authentication, privacy, realtime or offline constraints. “Spatial medical training” combines XR, gaze/hand, possible safety domain, collaborative/supervised context, and accessibility.

A mandatory coverage cell needs an owner that creates the relevant contract and an independent verifier that can challenge it. Reusing an owner is allowed when the mechanism is genuinely shared; inventing a new skill solely to make the atlas symmetrical is forbidden. Conversely, if a cell requires a distinct model — driving glance budget, TV directional focus, wearable glance duration, or agent autonomy — hiding it inside a generic platform skill is under-modeling.

Cross-axis combinations can be stricter than either axis. `automotive + driving + agentic AI`, for example, needs both distraction/safety and autonomy/agency constraints. Record these as mandatory route rules rather than exploding the atlas into every Cartesian combination.

## Evidence
An atlas delta must name the source or observed failure that exposed the gap, affected tasks, owner/verifier mapping, and whether existing evals would have caught it. Coverage is evidence of *responsibility*, not proof of quality.

## Output Contract
Return a `coverage-delta` with `axis_changes[]`, `new_or_changed_cells[]`, `ownership_changes[]`, `mandatory_route_changes[]`, `new_eval_needs[]`, `source_refs[]`, and `coverage_status`. Each cell records `id`, `axis`, `value`, `owner_skills[]`, and `verifier_skills[]`.

## Failure Traps
- Product-category explosion: one skill per industry noun.
- Treating responsive web as equivalent to mobile native, TV, or desktop.
- Counting a cell as covered because a generic skill mentions it once.
- No independent verifier for high-risk domains.
- Creating a new axis that does not change any decision or evidence requirement.
- Ignoring cross-axis risk escalation.
- Declaring atlas completeness while mandatory cells are unowned.

The atlas succeeds when an unfamiliar task can be decomposed into owned constraints without loading the whole skill graph.