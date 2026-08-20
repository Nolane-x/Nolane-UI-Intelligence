---
name: designing-slot-and-part-contracts
description: Define named slots and component parts as semantic extension points without exposing incidental DOM structure or allowing invalid composition.
---

# Designing slot and part contracts

Slots and parts let consumers customize structure, content, or styling, but every exposed name becomes a compatibility surface. Use this skill when a component needs explicit subregions or stylable parts beyond a flat prop API.

## Decision ownership

Own which regions deserve stable names, what content each accepts, ordering and multiplicity rules, semantic relationships between parts, and whether parts are content slots, behavioral subcomponents, or style targets. Decide what remains private.

## Inputs and evidence

Inventory consumer customization requests, existing DOM structure, compound subcomponents, CSS selectors in downstream code, accessibility relationships, repeated wrapper hacks, and potential future refactors. Distinguish requests for content placement from requests for behavior or state access.

## Procedure

Name slots by semantic role rather than visual position: `leading-action` is more durable than `left`. Specify accepted content, cardinality, default content, and behavior when omitted. For behavioral parts, document parent context dependencies and registration lifecycle.

Expose style parts only when consumers have a legitimate supported customization need. Avoid mirroring every internal element. Ensure slot ordering changes do not break accessible naming, focus order, or reading order.

Define nested and repeated-slot behavior, including keying and state retention where relevant.

## Failure topology

DOM-shaped part APIs freeze implementation. Unconstrained slots let consumers insert interactive content into regions that cannot support correct focus or event behavior. Another failure is semantic ambiguity: two slots overlap in purpose, so consumers choose based on current visuals and later refactors become breaking.

Style parts can bypass token and variant governance if they become an unrestricted theming API.

## Falsification

Rename or restructure internal elements while preserving documented slots; consumers should not notice. Insert edge-case content—long text, interactive descendants, missing slots, repeated slots—and test layout and accessibility. Ask independent users to choose the correct slot from documentation; frequent disagreement reveals weak semantics.

Search downstream code for selectors targeting private structure after the contract is introduced.

## Output contract

Produce a `slot-and-part-contracts-contract` listing public slots/parts, semantic roles, accepted content, multiplicity, defaults, ordering, parent-state dependencies, accessibility relationships, style authority, private boundaries, and compatibility expectations under internal refactor.

## Handoffs

Use `designing-composition-boundaries` to decide whether a slot is appropriate at all, `designing-component-api-governance` for non-structural options, `designing-component-token-scopes` for supported styling decisions, and `designing-variant-prop-taxonomies` when slot presence represents a finite variant.