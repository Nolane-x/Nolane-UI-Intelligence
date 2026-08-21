---
name: governing-token-mode-inheritance
description: Use when token modes or themes inherit from one another and override behavior, missing values, ancestry, and shadowing must remain explicit and deterministic.
---

# Governing Token Mode Inheritance

## Overview
Modes are frequently modeled as sparse overrides: dark inherits most values from base, high-contrast inherits from a theme, compact density overrides spacing. Once modes can inherit, the system needs semantics for ancestry, precedence, missing values, and override intent. This skill owns those semantics.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent decides that modes exist and what semantic tokens represent. This specialist governs inheritance between mode value sets rather than arbitrary resolver dimensions.

## Ancestry Model
Represent a mode as a node with declared parent(s), override set, and resolution scope. Prefer a tree or otherwise prove deterministic linearization when multiple inheritance is allowed. Distinguish “unset so inherit” from “intentionally cleared” and from “unsupported in this mode.” Those states must not collapse into null.

Decision ownership includes whether a child may override only primitives or also semantics, how base changes propagate, and whether an override remains valid when its parent token changes type or layer.

## Mode Invariants
Ancestry is acyclic. Every inherited value has a trace to its defining mode. Intentional clear/disable states survive serialization. Child overrides do not silently detach from parent semantic meaning. Multiple-parent precedence, if supported, is stable and documented.

## Evidence
Evidence includes ancestry diagrams, resolved snapshots per mode, override-diff reports, parent mutation tests, missing/clear fixtures, and traces for values inherited across more than one level. Render evidence should target states where inherited and overridden values meet, such as disabled controls under high contrast.

## Failure Modes
Failure includes a dark mode that inherits an obsolete base value after refactor, cyclic mode ancestry, override shadowing that hides parent security/contrast updates, null treated as “inherit” in one tool and “clear” in another, and multiple inheritance whose winner depends on serialization order.

## Falsification
Falsification changes a base token and predicts which descendants should update; removes a child override; inserts an explicit clear; and permutes multiple-parent declaration order. If observed descendants differ from the predicted inheritance graph, or a trace cannot identify the defining mode, the model fails.

## Recovery
Recovery reconstructs ancestry from authoritative mode definitions, separates absent from explicit-clear states, and removes shadowing overrides that no longer serve a deliberate purpose. Where multiple inheritance cannot be made deterministic, flatten to a supported hierarchy rather than preserve ambiguity.

## Output and Handoff
Output: `token-mode-inheritance-contract` with ancestry, override semantics, clear/unset states, linearization policy, trace requirements, and propagation tests. Handoff general context precedence to resolution-context governance; handoff semantic token redesign to the parent.

## Sibling Boundary and delete-the-skill
Resolution-context governance selects among context-qualified candidates, whereas this skill governs a declared inheritance relation between mode sets. The delete-the-skill test passes because mode ancestry creates propagation and shadowing failures that a generic context resolver does not own.