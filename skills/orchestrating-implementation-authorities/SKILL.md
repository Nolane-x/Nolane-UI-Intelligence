---
name: orchestrating-implementation-authorities
description: Use when one product should combine tested semantic primitives, visual mechanisms, platform-native components, motion engines, specialist SDKs, or open-code building blocks without letting one library own layers it cannot prove.
---

# Orchestrating Implementation Authorities

## Parent Contract
**Required parent:** `selecting-ui-building-blocks`.

Receive selected source candidates, authority route, local component/state contracts, visual direction, stack/runtime constraints, licensing, accessibility and performance requirements. The parent chooses building blocks; this skill decides how their responsibilities compose in code.

## Layer Ownership
Separate at least: semantic interaction, platform-native behavior, visual rendering, motion, data/specialist mechanics, styling/tokens, and product state. Assign a **semantic implementation authority** only where code/tests support semantics. Assign a **visual implementation authority** only where the visual mechanism is actually desired. Neither inherits the other's role.

Examples of healthy composition: a headless primitive owns dialog semantics while local CSS owns appearance; a motion engine owns temporal interpolation while product state owns truth; a canvas engine renders a domain visualization while accessible DOM equivalents carry task-critical meaning.

## Authority Interface Contract
For every dependency boundary state:
- input/state it is allowed to own;
- output/events it emits;
- focus/keyboard/pointer responsibilities;
- styles/tokens it may inject;
- lifecycle/cleanup and SSR/hydration assumptions;
- failure/degraded behavior;
- local wrapper responsibilities;
- replacement path.

Record **implementation lineage** from a product decision to wrapper/component to upstream source/version so future maintainers can distinguish intentional mechanisms from accidental dependency behavior.

## Open Code and Copying
Open-code distribution lowers integration friction but does not waive review. Once code is copied, the local project owns its semantics, accessibility, tests, maintenance and drift. Remove upstream defaults that conflict with the local design language; do not preserve them merely because they shipped in the example.

## Multi-Authority Collision
Reject hidden nested design systems, competing focus managers, duplicate gesture ownership, contradictory token resets, multiple animation clocks for the same transition, or two libraries claiming the same selection state. If two authorities must meet, define one explicit adapter edge rather than interleaving responsibilities throughout the tree.

## Output — `implementation-authority-plan`
Return `layers[] {layer, source_id, authority_role, owned_responsibilities, forbidden_responsibilities, local_adapter, version_snapshot}`, `interfaces[]`, `implementation_lineage[]`, `collision_findings[]`, `replacement_boundaries[]`, and `decision`.

## Falsification
Temporarily remove each external library from the architecture diagram. Can you state exactly what behavior or mechanism disappears? If not, the dependency has no justified authority. Replace the visual source while retaining semantic primitives; semantics should survive. Replace the semantic source while retaining the visual layer; appearance may survive but behavior must be reverified.

## Recovery
Split overloaded wrappers, move product truth out of animation/render libraries, reassign one owner per layer, and add adapter-level tests. Where upstream coupling prevents clean boundaries, build locally or select a different source.

## Hard gate
**No implementation plan may ship with overlapping authority over the same semantic state, implicit cross-library ownership, or missing implementation lineage for a material external mechanism.**
