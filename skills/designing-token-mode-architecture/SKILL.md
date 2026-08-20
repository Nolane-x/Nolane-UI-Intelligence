---
name: designing-token-mode-architecture
description: Model token modes such as light, dark, density, contrast, brand, and platform without exploding combinations or hiding precedence.
---

# Designing token mode architecture

A mode is not simply another theme file. It is a context dimension that changes how a design decision resolves. Use this skill when a token system must support contextual variants while remaining predictable as dimensions combine.

## Decision ownership

Own which contextual differences deserve first-class modes, whether dimensions are independent or mutually exclusive, how combinations resolve, and what precedence applies when several contexts are active. Decide the fallback behavior for unsupported combinations and the boundary between a token mode and a runtime component state.

Do not own individual dark-theme values or responsive component rules. Own the mode model that makes those values addressable without combinatorial chaos.

## Inputs and evidence

Inventory required contexts: color scheme, contrast preference, brand, density, platform, input modality, locale, product tier, or environmental state. For each, collect evidence that the same semantic decision legitimately resolves differently. Measure how many combinations are actually supported and where current overrides conflict.

Inspect build artifacts and runtime switching behavior. A mode architecture that exists only in source naming but cannot be changed safely at runtime may not satisfy product requirements.

## Procedure

Treat modes as dimensions with declared domains. Mark dimensions as orthogonal, dependent, or exclusive. Define a base resolution order and explicit override precedence. Prefer sparse overrides: a mode should declare only decisions that differ from its inherited baseline rather than copy the entire token set.

Separate environment modes from component state. `dark` may change global semantic colors; `pressed` belongs to interaction state unless there is a strong reason to make it a system-wide resolution dimension. Avoid encoding viewport breakpoints as global token modes when layout behavior should be component- or container-owned.

Construct a compatibility matrix for meaningful combinations and a policy for impossible states. Ensure diagnostics can report the active mode tuple and source of each resolved token.

## Failure topology

The common failure is multiplying theme files until every brand × color scheme × density × platform combination has a full copy. Drift becomes inevitable and one fix must be repeated across dozens of files. The opposite failure is forcing unrelated contexts into one monolithic theme selector, making composition impossible.

Silent precedence is especially dangerous: a high-contrast override may be accidentally overwritten by a brand theme because load order rather than declared authority decides the result.

## Falsification

Enumerate supported mode tuples and resolve representative semantic tokens in each. Randomize source-file order; resolution should not change if precedence is explicit. Disable one dimension and verify sensible fallback. Add a hypothetical new brand or density option and estimate how many files or mappings must change; explosive growth falsifies the architecture.

Check that component states do not require globally switching modes and global modes do not leak into component APIs as arbitrary booleans.

## Output contract

Produce a `token-mode-architecture-contract` listing dimensions, allowed values, orthogonality and dependency rules, active-context representation, precedence, fallback behavior, sparse-override rules, unsupported combinations, runtime switching obligations, and inspection diagnostics. Include a resolved combination matrix for representative tokens.

## Handoffs

Pass base category questions to `designing-token-taxonomies`, reference resolution to `designing-semantic-token-aliasing`, cascading theme policy to `designing-theme-inheritance`, brand-specific dimensions to `designing-multi-brand-theming`, and density semantics to `designing-density-token-systems`.