---
name: compiling-ui-implementation-specifications
description: Use when a material UI design is about to be implemented and the specification must be detailed enough that engineering does not invent missing product or interaction decisions.
---

# Compiling UI Implementation Specifications

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the selected architecture, interaction, navigation, visual, component-system, accessibility, content, responsive, motion, capability, action, scenario, and platform artifacts that apply. This faculty synthesizes existing decisions; it does not silently resolve unresolved product authority.

## Decision Boundary
This skill owns the **implementation boundary** between design intent and code. It asks whether every material surface can be built without a developer or coding agent guessing what a control does, what text appears, which state follows, how focus moves, what happens at narrow width, how errors recover, or which token/component variant applies.

A polished screenshot is not a specification. A component list is not a specification. Source code written from an underspecified mockup is not proof the missing decisions were correct. The output must be precise enough that two competent implementers converge on materially equivalent behavior while still allowing harmless engineering choices.

## Product Truth
Generated UI frequently fails in the “last 10%”: the main button exists, but loading disables the wrong controls; a kebab menu omits an action; keyboard focus disappears after a dialog closes; empty-state copy differs from the product vocabulary; a table collapses on mobile by dropping a critical field; a destructive flow has a confirmation screenshot but no failed-submit state; icons are invented inconsistently; async status uses indefinite animation with no completion semantics.

These are not cosmetic implementation details. They are interface decisions. The specification must carry them explicitly.

## Decision Model
1. **Enumerate surfaces and regions.** Every required surface receives stable IDs, purpose, actor/state availability, layout regions, and relationship to the navigation/reachability graph.
2. **Inventory visible and interactive elements.** Record exact copy or content source, semantic role, canonical action/destination, component/variant, state, icon/media reference, and visibility rule. Do not use “etc.” where a missing item could change functionality.
3. **Bind controls to actions.** Every required action has at least one control/binding specification. The spec names label, accessible name when different, control type, enabled/disabled conditions, confirmation, loading/pressed/selected state, shortcut/gesture alternatives, and success/failure feedback.
4. **Specify state matrices.** Include empty, loading, skeleton/progressive, partial, success, validation, permission denied, offline/degraded, conflict, stale data, destructive pending, and retry states when applicable. State transitions reference canonical actions.
5. **Specify navigation and focus.** Define destination, replace/push/modal semantics when material, back/cancel behavior, deep-link handling, initial focus, focus return, focus order exceptions, and announcement/live-region behavior.
6. **Specify responsive transformation.** State what reflows, wraps, collapses, scrolls, becomes overflow, changes navigation pattern, or changes interaction modality. Explicitly prove that required capabilities survive each required breakpoint/profile.
7. **Specify visual system choices.** Bind typography roles, spacing, color semantics, radius/elevation/surface, icon family, image treatment, density, and motion tokens to system definitions. One-off exceptions need rationale.
8. **Specify rich interaction mechanics.** For animation, drag, resize, canvas, carousel, command palette, editor, or 3D behavior, reference the interaction/motion contracts and any selected external building blocks; include reduced-motion, interruption, input alternatives, and performance constraints.
9. **Separate fixed decisions from engineering latitude.** Mark details that engineering may choose without altering product intent, such as internal file structure, while keeping user-observable behavior fixed.
10. **Expose unresolved decisions.** Unknown copy, authority, data shape, accessibility behavior, or platform behavior remains in `unresolved[]` and blocks `IMPLEMENTABLE` when material.

## Evidence
The specification cites source artifacts rather than restating them from memory. A control binding references action ID; a page references reachability surface ID; visual rules reference token/visual contracts; animation references motion/rich-interaction evidence; accessibility obligations reference their source. For reproduction work, exact target evidence can freeze visual dimensions, but unspecified behavior still requires product reasoning.

Validate the spec structurally before implementation and compare it against the rendered application afterward. Any material behavior invented during coding becomes a spec delta and requires re-review.

## Output Contract
Return `ui-specification` with:
- `surfaces[] {id, purpose, actors, states, regions, responsive_rules, navigation}`
- `controls[] {id, surface_id, exact_copy, semantic_role, action_id, destination_id, component_variant, states, enabled_conditions, feedback, focus_behavior, accessibility, modalities, responsive_behavior}`
- `content_inventory[]`
- `icon_media_inventory[]`
- `state_transitions[] {from, action_id, to, async, failure, recovery}`
- `system_bindings {tokens, components, motion, platform}`
- `external_building_block_refs[]`
- `engineering_latitude[]`
- `unresolved[] {decision, materiality, owner}`
- `status: IMPLEMENTABLE|BLOCKED`

`IMPLEMENTABLE` requires complete control coverage for required actions and no unresolved material user-observable decision.

## Failure Traps
- Calling Figma/screenshots the implementation spec without enumerating behavior.
- Using placeholders such as “other menu items,” “standard loading,” or “responsive as needed.”
- Specifying a button visually but not binding its canonical action.
- Omitting focus return, keyboard shortcut conflicts, touch target behavior, or screen-reader naming because a component library “probably handles it.”
- Letting external component defaults become product decisions without review.
- Describing only desktop and asking engineering to “make it responsive.”
- Treating error/retry/permission states as backend concerns.
- Freezing exact pixels while leaving destructive consequences ambiguous.
- Hiding unresolved authority in engineering notes instead of blocking implementation.

**Hard gate:** if an implementer must invent a material product, interaction, accessibility, responsive, or visual-system decision to finish the UI, the specification is not `IMPLEMENTABLE`.

## V6 Implementation Specification Protocol
Compile a **component-behavior matrix** covering anatomy, semantic role, state, input modalities, events, focus, async behavior, accessibility, content extremes, and ownership. Add a **token-resolution table** from semantic design decisions to actual token/variable values and allowed component-level exceptions.

Create a **breakpoint-state matrix** showing how the same product state transforms across containers/viewports without losing selection, focus, actions, or content relationships. Set an **implementation ambiguity budget**: every unresolved material choice must be explicitly labeled and assigned to an owner; the spec cannot hide uncertainty in adjectives. Attach an **executable acceptance hook** to each critical behavior—test name, browser check, visual artifact, schema validation, or runtime assertion.

### Falsification
Give the spec to an independent implementer and identify places where two incompatible implementations both satisfy the prose. Material ambiguity falsifies readiness.

### Recovery
Return to the owning design contract, resolve or type the ambiguity, add acceptance evidence, and regenerate affected implementation artifacts.
