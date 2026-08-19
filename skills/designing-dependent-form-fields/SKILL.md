---
name: designing-dependent-form-fields
description: Use when the availability, meaning, requirement, options, or validity of one form field depends on another field and the dependency must remain understandable and stable.
---

# Designing Dependent Form Fields

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns dependency topology inside forms: what upstream state controls a downstream field, how that relationship is communicated, and what happens to downstream values when the controlling state changes. It does not own generic validation styling or the domain policy that creates the dependency.

## Decision Boundary
Represent dependencies as explicit state transitions rather than imperative show/hide snippets. For each dependent field, record the controlling values, whether the child is hidden, disabled, optional, required, re-labeled, or given a different option set, and whether an existing child value remains semantically valid after the transition.

Preservation is a product decision. Hiding a field must not automatically erase its value; keeping a hidden value must not automatically submit it either. Distinguish dormant retained state, excluded state, and invalidated state. If changing country invalidates a previously selected region, explain the reset. If changing an account type merely hides advanced options temporarily, preservation may reduce destructive re-entry.

Avoid dependency chains that become invisible programs. When A changes B, which changes C, users need a comprehensible causal path and predictable focus. Do not move focus merely because content appeared. Announce material dynamic changes accessibly when they alter available choices or requirements.

## Failure Topology
- A child field disappears and silently submits an old value the user can no longer see.
- Changing an upstream answer wipes ten minutes of downstream work without warning.
- Disabled fields look editable or required indicators lag behind the current dependency state.
- Remote option loading races with a second upstream change and installs stale choices.
- A circular dependency leaves the form in an impossible state.
- Screen-reader users are not told that a newly required region has appeared.

## Falsification and Recovery
Falsify with rapid upstream toggling, prefilled edit forms, browser back/forward restoration, server-provided defaults, asynchronous option fetches completing out of order, keyboard-only operation, and a dependency chain three levels deep. The design fails if the submitted payload contains state the visible form cannot explain or if users cannot predict what an upstream change will invalidate.

Recover by making the dependency graph explicit, versioning async requests by controlling state, defining preservation/reset rules per edge, surfacing destructive invalidation before it occurs, and serializing only active semantically permitted values.

## Output Contract
Return `dependent-field-state-contract` with dependency edges, controlling predicates, child-state transitions, retention/reset policy, async option authority, payload inclusion rules, dynamic announcement behavior, focus policy, cycle checks, and falsification scenarios.