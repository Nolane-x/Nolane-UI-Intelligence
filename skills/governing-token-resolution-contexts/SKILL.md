---
name: governing-token-resolution-contexts
description: Use when one token graph can resolve to different concrete values across themes, modes, brands, platforms, density regimes, or runtime environments and the precedence must remain deterministic.
---

# Governing Token Resolution Contexts

## Overview
A token reference is not fully specified by its key when the resolver can see theme, mode, platform, component scope, user preference, or environment. This skill owns the decision model that turns those inputs into one deterministic resolved value. It prevents a design-token graph from becoming an implicit cascade whose result depends on load order or implementation accident.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent defines token architecture, naming, semantic layers, and broad system intent. This specialist begins only when the same token identity has context-sensitive candidates and a resolver must choose among them.

## Resolution State Model
Represent resolution as `(token, context, candidate-set, precedence, result, trace)`. Context dimensions must be declared and ordered; absence is a first-class state, not silently treated as a default. A resolver trace records which condition matched, which candidate lost, and why. Context values that are unknown at authoring time require an explicit fallback branch.

The core decision is whether two context dimensions compose, override, or conflict. Theme plus platform may legitimately compose; brand plus emergency-contrast may require one dimension to dominate. Never let object insertion order decide authority.

## Invariants
- identical token + identical normalized context resolves identically;
- precedence is explicit and inspectable;
- unresolved required dimensions produce an observable blocked/fallback state;
- fallback cannot jump across semantic layers and change meaning;
- context narrowing cannot accidentally broaden to a less-specific rule without a recorded reason.

## Evidence
Evidence includes resolver traces for representative contexts, precedence tables, theme/mode snapshots, negative cases where no candidate applies, and consumer renders showing that semantic meaning survives context changes. A screenshot alone is weak evidence because it hides the path used to obtain the value.

## Failure Modes
Characteristic Failure includes shadowed candidates that can never win, contradictory precedence across platforms, silent fallback to a primitive token, context keys with different normalization rules, and circular environment dependence. Another failure is visually plausible output produced by an unstable resolver: a later package load changes which value wins without changing token data.

## Falsification
Falsification should vary one context dimension at a time, permute candidate declaration order, remove the expected winner, and replay the same input in independent consumers. The contract is disproved if equivalent contexts yield different values, if declaration order changes authority, or if the trace cannot explain a fallback.

## Recovery
Recovery first freezes the observed context and trace, then reduces the candidate set to the smallest conflicting rules. Repair precedence or normalization rather than adding a higher-specificity patch. If no valid candidate exists, surface that fact and route to token architecture instead of fabricating a value.

## Output and Handoff
Output: `token-resolution-contexts-contract`, containing context dimensions, normalization, precedence, fallback rules, conflict policy, and trace requirements. Handoff resolved values to implementation adapters; hand off semantic-layer changes to the parent.

## Sibling Boundary and delete-the-skill
Sibling token-reference integrity owns graph validity, not contextual precedence. Mode inheritance owns parent/child mode relations, not arbitrary resolver dimensions. The delete-the-skill test passes because removing this owner leaves no contract for deterministic precedence when several context-qualified values are simultaneously valid.