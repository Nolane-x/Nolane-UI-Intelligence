---
name: designing-token-taxonomies
description: Design token vocabularies whose categories encode stable design decisions instead of implementation accidents.
---

# Designing token taxonomies

Token systems fail long before a color value is wrong. They fail when names mix primitives, semantics, components, states, and platforms so thoroughly that consumers cannot infer what is safe to reuse. Use this skill to define the classification system that determines where a token belongs and what kind of meaning its name is allowed to carry.

## Decision ownership

Own the token layers, category boundaries, naming grammar, and admissibility rules for new token concepts. Decide how primitives, semantic roles, component-scoped decisions, interaction states, and platform aliases relate. The taxonomy must answer whether two equal values represent one decision or two independent decisions that merely happen to coincide today.

Do not choose the final brand palette or implement token transforms. This skill owns the information architecture of design decisions.

## Inputs and evidence

Inventory real component styling decisions, existing token names, raw literals, theme variations, accessibility states, responsive modes, and cross-platform mappings. Sample call sites rather than trusting token documentation alone. Record ambiguous names such as `gray500`, `primary`, `surfaceAlt`, or `buttonBlue` and identify what a consumer must know to use each safely.

Gather change history: frequently co-changing values often reveal a shared semantic decision; values that diverge under dark mode, high contrast, density, or brand switching should not be collapsed merely because the default theme matches.

## Procedure

Start from consumer intent. Define a small set of layers with one responsibility each, then write positive and negative examples for every layer. Separate value description from usage purpose: a primitive may describe a color coordinate, while a semantic token expresses a role such as critical text on an interactive surface. Reserve component scope for decisions that genuinely belong to that component and cannot be stated at a reusable semantic level.

Define state composition explicitly. Decide whether hover, disabled, selected, emphasis, density, and platform are dimensions, aliases, or separate namespaces. Establish naming order so token names remain parseable and do not accumulate arbitrary adjectives.

Test the taxonomy by classifying new examples without adding exceptions. If every novel case forces a new category, the model is not stable.

## Failure topology

A primitive-only system leaks implementation values into products and makes themes expensive. A semantic-only system can become a flat pile of vague roles. Component tokens copied for every component create duplication without ownership. Names that encode current values in semantic layers make future changes linguistically false. Names that encode every possible dimension create combinatorial namespaces.

The dangerous failure is false reuse: two contexts share a token because they look equal today, then one cannot evolve without changing the other.

## Falsification

Take twenty styling decisions from unrelated components and classify them independently. Ask a second maintainer to do the same without verbal coaching. Material disagreement indicates unclear boundaries. Switch theme, contrast mode, density, and platform assumptions; if supposedly identical decisions diverge, split their ownership. Search for tokens whose names require knowledge of a particular component implementation to understand.

Reject a taxonomy that can only be applied by its original author.

## Output contract

Produce a `token-taxonomies-contract` defining layers, namespaces, naming grammar, dimension order, examples and counterexamples, rules for promoting or splitting tokens, collision policy, and review questions for new additions. Include a mapping of representative existing tokens into the proposed taxonomy and mark unresolved ambiguity rather than hiding it.

## Handoffs

Pass meaning-preserving reference chains to `designing-semantic-token-aliasing`, theme dimensions to `designing-token-mode-architecture`, component-local decisions to `designing-component-token-scopes`, and removal or renaming of legacy categories to `designing-token-deprecation-migrations`.