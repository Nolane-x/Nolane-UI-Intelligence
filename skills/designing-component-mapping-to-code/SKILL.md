---
name: designing-component-mapping-to-code
description: Use when design-tool components or instances must map to production component APIs and the handoff must resolve semantic identity, variants, slots, props, composition, unsupported overrides, and custom cases without cloning the design tree into code.
---

# Designing Component Mapping to Code

Component mapping is semantic resolution between two component systems. Similar names or shapes are weak evidence; the mapping must show that design intent fits the production component's role, states, slots, accessibility, and API constraints.

## Parent Contract
**Required parent:** `designing-design-to-code-handoffs`.

The parent owns the overall translation. This skill owns design-component ↔ production-component identity and prop/slot mapping.

## Mapping Identity
Use stable design component IDs/keys and production component identifiers rather than display names alone. A design “Button/Primary” may map to a production `Button` with intent prop; a visually similar custom rectangle with click interaction may not. Confirm semantics first.

Represent mapping fields: component identity, variant-to-prop mapping, boolean/state props, text/content slots, icon/media slots, child composition, event/action bindings, accessibility contract, and unsupported design overrides. Where one design component maps to a composition of several production components, make the composition explicit rather than forcing one-to-one mapping.

## Variants and Overrides
Design variants often encode presentation choices that production APIs derive from semantics or state. Do not generate new props solely to mirror every design variant. Resolve whether the variant is semantic, visual token, responsive condition, interaction state, or accidental artifact.

Instance overrides may indicate real product content or local misuse. Validate overrides against production API. If the design instance detaches or overrides internal geometry unsupported by the system, mark custom/exception rather than forking the production component silently.

## Mapping Confidence
Use states such as exact, compatible-with-transform, composition, custom-required, deprecated, ambiguous, and unmapped. Confidence should depend on semantic/API evidence, not string similarity. Ambiguous mappings require a human/design-system decision.

## Evidence
Test components with same name but different semantics, variant aliases, deprecated production component, slots, nested composition, detached instance, accessibility prop, and local override. Compile or render mapped examples against the actual production API where possible.

## Failure Modes
- Mapping uses name similarity only.
- Every design variant becomes a production prop.
- Detached design instance causes a duplicated component fork.
- Slot content is flattened into raw HTML strings.
- Accessibility semantics in production are bypassed by lower-level mapping.
- Deprecated component is selected because its shape matches best.

## Falsification
Create two production components with similar visual appearance but different semantics, plus one design component whose name matches the wrong one. Falsify if the mapper chooses by name/shape or cannot explain the semantic/API evidence for the mapping.

## Recovery
Re-evaluate semantics, route through stable IDs, map variants to existing API concepts, mark unsupported overrides, and preserve custom exceptions explicitly. If no production component satisfies the contract, hand off a new-component decision rather than generating a hidden fork.

## Handoff
Token values route to `designing-token-mapping-to-code`; responsive variants to `designing-responsive-intent-handoff`; behavior/actions to `designing-interaction-specification-handoff`; system API evolution remains with `evolving-component-apis`.

## Output Contract
Return a `component-mapping-to-code-contract` with `design_component_id`, `production_component_id`, `mapping_state`, `variant_prop_map`, `slots[]`, `composition_rules`, `unsupported_overrides[]`, `accessibility_binding`, `evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.