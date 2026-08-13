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

## Output: `finding-set`
Return typed findings with affected component/token paths, semantic impact, blast radius, and repair layer (`primitive`, `semantic-token`, `component`, `composition`, or `local-exception`). Prefer the highest correct shared layer; do not recommend a global change for a local anomaly.

## V6 Design-System Integrity Critique
Audit **token semantic drift**: tokens that started as semantic roles but became containers for arbitrary values, or multiple tokens that mean the same thing because teams avoided migration. Compare token names to actual use across themes/surfaces; a token is not semantic merely because it has a name.

Inspect every **component escape hatch**—raw class/style props, arbitrary slots, boolean piles, untyped overrides, global selectors. Escape hatches are sometimes necessary, but high usage can mean the component boundary is wrong or the product has unmodeled variants.

Detect **variant explosion** by mapping variants to product decisions. If combinations exist only because the API exposes toggles, consolidate. If materially different semantic states are forced through cosmetic variants, split the contract. Complexity belongs where product meaning changes.

Measure **cross-surface consistency** by semantics and interaction before pixels. The same action/state should use compatible language, feedback, focus and accessibility across web/mobile/desktop even when platform composition differs. Visual uniformity that breaks native behavior is not consistency.

Track **governance debt**: undocumented exceptions, duplicated primitives, stale tokens, source-library divergence, missing migrations, unowned accessibility regressions, abandoned experiments and private component forks. Debt becomes release risk when nobody can tell which rule is authoritative.

### Falsification
Sample real product surfaces rather than Storybook only. Try to implement an adversarial but legitimate product scenario with the public system API. If success requires scattered literals and overrides, the system does not cover the product. Conversely, if an allegedly inconsistent component is intentionally platform-specific and preserves semantic equivalence, remove the finding.

### Recovery
Route semantic gaps to component/token architecture, visual inconsistencies to craft/system owners, and source divergence to integration/provenance. Do not respond to variant explosion by adding another variant. Define migration and deprecation paths so correction is operational, not aspirational.
