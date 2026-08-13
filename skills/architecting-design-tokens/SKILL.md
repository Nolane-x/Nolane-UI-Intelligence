---
name: architecting-design-tokens
description: Use when a UI needs reusable color, type, spacing, radius, elevation, motion, size, or other design decisions expressed as a portable semantic token system.
---

# Architecting Design Tokens

## Overview
Tokens encode design decisions so repeated semantics stay coherent across components, themes, platforms, and implementations. They are not a dumping ground for every CSS value.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the selected visual direction and craft contracts. Preserve existing project tokens unless the contract authorizes a system change.

## Four-tier model
Use these conceptual layers:
1. **primitive:** raw reusable values (`blue-600`, `space-3`, type metric)
2. **semantic:** intent (`text-primary`, `surface-raised`, `action-danger`)
3. **component:** component-local contract (`button-primary-bg`, `table-row-height`) only when semantics cannot be expressed cleanly by aliases
4. **context/state override:** theme, density, platform, high-contrast, selected/disabled, or other bounded override

Avoid jumping from a raw value directly into dozens of components; that creates invisible coupling.

## Naming
Name semantic tokens by purpose, not current appearance. `text-danger` survives a palette change; `red-text` does not. Avoid semantic names so vague they become universal escape hatches (`surface-2` may be valid for elevation, but `misc-gray` is not).

## Token eligibility
A value deserves a token when it is:
- repeated by meaning
- part of a deliberate scale/relationship
- expected to vary by theme/platform/density
- useful to constrain downstream design

Do not tokenize one-off illustration coordinates, accidental margin fixes, or every numeric value encountered.

## Alias discipline
Prefer semantic aliasing rather than duplicating values. Record why two semantics share a primitive today; they may diverge later. Example: border subtle and disabled text may currently use similar gray but should not necessarily share one semantic token.

## Themes
Themes override semantic/context layers, not component code at random. Verify each theme as a coherent surface/text/border/focus/status system. Dark theme is not primitive inversion.

## Typography tokens
Separate font family, size, line height, weight, tracking, and role combinations. A role token can reference primitives while allowing platform-specific font substitution.

## Motion tokens
Tokenize durations/easing when repeated transition semantics exist (quick feedback, standard transition, emphasized movement). Do not force every animation to one duration if distance/purpose differ.

## Interchange
When serializing across tools, prefer current Design Tokens Community Group-compatible structures when practical, but keep the internal semantic model independent of one file format. Runtime adapters own tool-specific conversion.

## Output: `token-model`
Return `primitives`, `semantics`, `components`, `contexts`, `aliases`, `theme_overrides`, `density_overrides`, `platform_overrides`, `naming_rules`, and `non_tokenized_exceptions`.

## Gates
- No circular aliases.
- Every component token has a clear owner and use.
- Repeated semantic values do not bypass tokens without an explicit exception.
- Global tokens do not contain page-specific coordinates.
- Theme overrides preserve required semantic contrast/state distinctions.

## V6 Token Semantics and Lifecycle
Represent aliases as a **semantic alias graph** from primitive values through semantic roles to component/context tokens. The graph must expose cycles, aliases that skip meaning, and many-to-one mappings that erase state distinctions. For each theme, density, platform, forced-colors, and high-contrast context define a **mode-invariance contract**: which semantics must remain stable even when physical values change.

Perform a **literal-escape audit** on implementation surfaces. Literal values are allowed only for documented local exceptions or values that are not design decisions; repeated literals that bypass semantic tokens are drift. Establish a **token lifecycle policy** for introduction, rename, deprecation, migration, ownership, and compatibility so tokens do not become permanent archaeology.

Run a **theme-drift probe** by rendering representative components across every supported mode and checking semantic relationships—primary text vs muted, action vs danger, selected vs hover, raised vs base—rather than checking raw equality. A dark theme that mechanically inverts primitives but reverses hierarchy has failed.

### Falsification
Change a primitive palette or spacing scale and observe whether unrelated component semantics unexpectedly move together. If one token alteration causes conceptually unrelated regressions, the alias graph encodes visual coincidence instead of meaning.

### Recovery
Introduce or split semantic roles, migrate consumers, and deprecate misleading aliases. Do not add component overrides until the token model explains why the exception exists.
