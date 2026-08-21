---
name: designing-hover-to-nonhover-affordance-transitions
description: Use when information, controls, previews, or discoverability currently depend on hover and the interface must preserve their function on touch, pen, keyboard, or devices where hover is unavailable or unreliable.
---

# Designing Hover-to-Nonhover Affordance Transitions

## Hover Is Optional Capability
Hover can cheaply reveal controls and previews, but it is not a universal interaction state. This skill owns the replacement path when hover disappears: what becomes persistent, what moves to focus/press/disclosure, and what should be removed because it was merely decorative.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent provides adaptive context. Tooltip semantics, accessible names, and base input mechanics remain with their specialists; this skill governs cross-capability affordance equivalence.

## Affordance Inventory
Classify every hover-dependent behavior as required information, required action discovery, preview, status, explanation, or decoration. Required information cannot exist only on hover. Required actions need a visible or otherwise discoverable non-hover path. Previews may map to long-press/tap only if that does not conflict with the primary action.

Hybrid devices complicate detection: `hover: hover` support does not guarantee the user currently has a mouse. Design a stable baseline that remains operable without hover and treat hover as enhancement.

## Evidence
Evidence includes operation with touch only, keyboard focus only, hover-disabled emulation, hybrid device transitions, long-press conflict checks, and screen-reader inspection where hover content carries meaning. Verify that replacement affordances do not duplicate or obscure primary actions.

## Failure Modes
Failure includes delete/edit icons visible only on row hover, status detail available only in a tooltip, tap opening the primary action so no gesture remains for a hover preview, persistent fallback controls causing severe clutter, and CSS hover states stuck after touch interaction.

## Falsification
Falsification disables hover and attempts every action/information task previously reachable by hover; then switches input modality without reloading. Missing function, ambiguous tap conflict, or stale hover state falsifies the contract.

## Recovery
Recovery promotes essential information/actions to durable UI, maps optional previews to explicit disclosure, and removes hover decoration that has no non-hover meaning. Do not solve the problem by detecting “mobile” user agents; capability and task are the relevant variables.

## Output
Output: `hover-to-nonhover-affordance-transitions-contract` with affordance classification, non-hover equivalent, hybrid behavior, conflict rules, and evidence.

## Handoff
Handoff target-size/density changes to pointer-to-touch transitions and tooltip content design to tooltip/accessibility owners.

## Sibling Boundary and delete-the-skill
Density adaptation does not decide how hover-exclusive meaning is recovered. Removing this skill leaves a unique capability-loss failure class unowned.