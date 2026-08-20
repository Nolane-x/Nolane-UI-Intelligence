---
name: designing-component-token-scopes
description: Decide when styling decisions deserve component-scoped tokens and how those tokens relate to shared semantic foundations without duplicating the system.
---

# Designing component token scopes

Component tokens are valuable when a component owns a stable design decision that cannot be expressed safely through global semantics. They are harmful when every declaration receives a token. Use this skill to set that boundary.

## Decision ownership

Own eligibility, namespace, inheritance, and override policy for component-scoped tokens. Decide whether a decision belongs to the component API, a semantic global token, an internal implementation detail, or a consumer override surface. Define what downstream products may customize without forking the component.

## Inputs and evidence

Inventory component styles, repeated overrides, theme requirements, variant/state matrices, downstream customization requests, and tokens whose names mention component parts. Trace each candidate token to real consumers and change history. Distinguish decisions that vary by product from values that only changed during refactoring.

Inspect whether consumers need semantic intent or exact geometry. A button border radius may be globally governed shape language; a disclosure chevron gap may genuinely be component-local.

## Procedure

Classify candidates by ownership. Promote to component scope only if the component is the stable authority and independent variation is plausible. Reference global semantic tokens where possible rather than copying raw primitives. Keep internal tokens private unless external customization is an explicit supported contract.

Define state and part naming consistently. Avoid publishing every subpart as a token merely because the implementation has a DOM node. For exposed tokens, specify fallback and theme behavior plus which combinations are supported.

Review token count against component complexity. A component with dozens of public tokens may be exposing implementation rather than a design contract.

## Failure topology

Over-tokenization creates an unofficial CSS API that cannot evolve. Under-tokenization forces consumers to override selectors or fork components. Another failure is false locality: component tokens duplicate a semantic role used across many components, causing divergence under theme changes. Public tokens that map one-to-one to internal DOM structure also freeze refactoring.

Scoped tokens can conflict with variant props when both control the same decision through different channels.

## Falsification

For each public token, ask what independent consumer decision it enables and what compatibility promise follows. Remove a candidate token and see whether consumers can still express legitimate needs through shared semantics or component props. Change internal markup and test whether the public token contract survives.

Compare analogous decisions across components. If many local tokens encode the same role, elevate the role globally instead.

## Output contract

Produce a `component-token-scopes-contract` containing token eligibility rules, namespace grammar, public/private boundaries, semantic references, state/part naming, override precedence, compatibility obligations, and an audited list of exposed component tokens with rationale and consumers.

## Handoffs

Use `designing-token-taxonomies` for global layer boundaries, `designing-component-api-governance` for prop-level customization, `designing-slot-and-part-contracts` for structural exposure, and `designing-token-deprecation-migrations` when removing public component tokens.