---
name: critiquing-design-system
description: Use when an independent reviewer must detect token drift, inconsistent component semantics, variant explosion, one-off overrides, broken state parity, or design-system misuse in a UI.
---

# Critiquing Design System

## Overview
Review whether the interface expresses a coherent system without forcing incorrect reuse.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Use token model, component system, project conventions, and implementation evidence.

## Audit dimensions
### Token integrity
Find repeated raw values bypassing semantic tokens, incorrect alias layers, page-specific values promoted globally, inconsistent theme overrides, and semantic tokens used for unrelated purposes.

### Component semantics
Compare instances with the same concept: anatomy, keyboard/focus, label behavior, spacing, state treatment, iconography. Then check the opposite: visually reused component for semantically different concepts.

### Variants
Flag variants created to patch one screen or props that expose raw styling rather than meaning. Identify when repeated escape hatches indicate a missing system capability.

### State parity
Shared components must treat hover/focus/selected/disabled/loading/error consistently except where explicit variants change behavior. A dark theme or compact density cannot silently drop focus/status cues.

### Composition
A design system should constrain primitives while allowing product composition. Do not flag legitimate layout variation merely because two screens differ.

### Governance debt
Record duplicated components, deprecated patterns, undocumented custom widgets, and overrides likely to create future divergence.

## Output
Return typed findings with affected component/token paths, semantic impact, blast radius, and repair layer (`primitive`, `semantic-token`, `component`, `composition`, or `local-exception`). Prefer the highest correct shared layer; do not recommend a global change for a local anomaly.
