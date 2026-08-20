---
name: designing-builder-component-authoring
description: Use when a visual builder lets authors turn local structures into reusable components with explicit properties, variants, slots, defaults, boundaries, naming, and update-safe instance contracts.
---

# Designing Builder Component Authoring

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This skill owns creation and evolution of reusable component definitions inside a visual builder. It is not the general design-system governance layer. The focus is the authoring operation that converts concrete structure into a reusable abstraction without hiding what becomes API versus internal implementation.

## Definition decisions

When extracting a component, identify stable semantic boundary first. Decide what the component promises: visual/interaction role, editable properties, variants, event outputs, content slots, data expectations, responsive behavior and accessibility obligations. Do not automatically expose every current literal as a property; doing so freezes incidental implementation and creates unusable APIs.

Separate **definition editing** from **instance editing** with strong contextual cues. Entering the definition should make scope visible and allow navigation back to the originating instance. If edits occur in context, show which surrounding data/style values are borrowed from the instance versus part of the component default; otherwise authors accidentally bake environment-specific assumptions into the reusable definition.

Properties need types and semantics, not arbitrary text fields. A boolean, enum/variant, number with unit, asset, reference, content slot or event has different validation and runtime behavior. Defaults should be meaningful and accessible. Variant combinations may need constraints to prevent impossible states; do not create a Cartesian variant matrix by default.

Refactoring existing structure into a component must preserve stable child identities where feasible so interactions, data bindings, collaboration comments and history remain attached. Preview the extraction diff: what moves into definition, what becomes an input/slot, what remains at instance scope.

## Evidence

Study the builder's document/component schema, runtime composition model, component libraries, nested/repeated examples, variant/state requirements and exported code. Observe real authors deciding reuse boundaries; mechanical “make component” demos often hide API quality problems.

## Failure topology

Failures include components with dozens of meaningless knobs because every style was exposed; extracted components that capture a page-specific data source; definition edits accidentally applied only to one instance; implicit variant combinations that create inaccessible states; and refactors that break comments/bindings because child IDs are regenerated.

Another failure is opaque components whose internal boundaries cannot be inspected, making the builder feel like a black-box template system rather than an authoring environment.

## Falsification

Extract a repeated structure with content, events, responsive behavior and nested children. Create instances, expose only necessary properties/slots, evolve the definition, move an instance to a different context and export/run it. The contract is falsified if the component cannot state its inputs/outputs, if context-specific dependencies leak into defaults, if instance behavior changes unpredictably after definition edits, or if extraction breaks semantic references without warning.

## Recovery

Reduce the public component surface to task-relevant inputs, convert environment dependencies into explicit parameters/slots, preserve or map stable IDs during refactor, and surface invalid variants as authoring errors. If a component has become a page fragment with hidden coupling, split it or reclassify it instead of adding more knobs.

## Output contract

Return a `builder-component-authoring-contract` containing extraction boundary, definition identity, property/event/slot API, types/defaults, variant constraints, contextual editing rules, identity-preserving refactor behavior, nested composition, export/runtime mapping and component-quality verification cases.

## Handoffs

Use `designing-component-instance-overrides` for local divergence, `designing-builder-slot-insertion` for nested content contracts, design-system/component API owners for organization-wide governance, accessibility semantics owners for reusable interaction guarantees, and design-to-code component mapping when builder definitions correspond to implementation components.