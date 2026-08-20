---
name: designing-token-mapping-to-code
description: Use when design values or design-tool variables must map to production design tokens and code references while preserving semantic intent, aliases, modes, themes, fallback behavior, and exceptions instead of copying resolved values.
---

# Designing Token Mapping to Code

A resolved value is the end of a token chain, not the token's meaning. Design-to-code mapping should preserve semantic references so production can change themes, modes, density, and system values without freezing a snapshot into literal code.

## Parent Contract
**Required parent:** `designing-design-to-code-handoffs`.

The parent owns the translation. This skill owns binding design variables/styles/resolved values to existing production token identities. Token architecture itself remains with `architecting-design-tokens`.

## Mapping Layers
Distinguish design variable ID, collection/mode, semantic role, alias chain, resolved value, production token ID/name, target platform representation, and fallback. Prefer semantic mapping (`surface-danger`, `text-secondary`, spacing scale role) over matching equal hex/pixel values.

Two tokens can resolve to the same value today and have different semantics. Conversely, design and production tokens can have different current values because one artifact is stale. Value equality is corroborating evidence only.

## Modes and Themes
Map light/dark/high-contrast/brand/density modes intentionally. A design variable defined only in light mode should not generate a hardcoded value for dark production. Mark missing mode coverage and route it for design-system resolution.

Alias structure can differ across systems. Preserve the nearest semantic authority rather than recreating the exact design-tool alias graph in code. If production has an established alias hierarchy, map the design concept into it.

## Exceptions
Some values are genuinely local—illustration dimensions, one-off data-viz color, optical correction. Require an exception rationale and decide whether it belongs as a component local value, new token proposal, or intentionally literal constant. Do not inflate the global token system for every isolated measurement.

## Evidence
Map a set including equal-value/different-semantic tokens, aliases, missing dark-mode variable, deprecated token, responsive token, and legitimate local exception. Render across modes and inspect emitted code references rather than only visual equality.

## Failure Modes
- Mapping chooses token by hex/value equality.
- Resolved values are emitted instead of semantic references.
- Dark mode silently reuses light value.
- Design alias graph overwrites production token architecture.
- Every one-off value generates a new global token.
- Deprecated token remains mapped because the design file is stale.

## Falsification
Set two production tokens to the same current value, then change one theme mode. Falsify if the mapping cannot distinguish their semantic roles or if generated code fails after the mode change despite matching the original screenshot.

## Recovery
Map through semantic identity, preserve production aliases, mark missing modes, remove deprecated references, and document local exceptions. If semantic role cannot be established, leave the value unmapped rather than selecting the closest numeric token.

## Handoff
Token creation/governance remains with `architecting-design-tokens`; component prop mapping uses `designing-component-mapping-to-code`; rendered divergence appears in `designing-design-code-drift-review`.

## Output Contract
Return a `token-mapping-to-code-contract` with `design_variable_id`, `semantic_role`, `alias_evidence`, `production_token_id`, `mode_map`, `fallback_rules`, `mapping_state`, `local_exceptions[]`, `render_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.