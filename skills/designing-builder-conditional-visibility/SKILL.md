---
name: designing-builder-conditional-visibility
description: Use when builder-authored elements or branches appear based on data, permissions, feature state, viewport, experiment, or runtime conditions and authors must reason about absence, layout, accessibility, and mutually exclusive branches.
---

# Designing Builder Conditional Visibility

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This owner governs runtime presence rules inside a visual authoring system. It is not merely toggling `display:none`; a condition can alter whether an object exists, occupies layout, participates in focus/reading order, loads data, executes interactions, or has an alternate branch.

## Conditional model

Classify conditions by authority: user/permission, data value, feature/config flag, experiment assignment, local interaction state, environment, responsive range or product lifecycle. Do not mix materially different authorities into one opaque expression without showing provenance. A permission condition must not be presented as a cosmetic visibility preference if backend authorization still matters.

Define condition outcomes precisely: hidden but mounted, removed from render/accessibility tree, collapsed from layout, replaced by fallback/else branch, disabled/read-only, or deferred until data is known. Each has different interaction and performance semantics. Builders should make the chosen behavior inspectable rather than assuming all “visibility” rules are equivalent.

Authoring absent objects requires a deliberate editor representation. An element false under current preview data still needs discoverable hierarchy presence, condition badge and a way to switch/test the branch. Prevent edits to a ghost representation from accidentally changing the condition itself. Show mutually exclusive branches together in structural context even if runtime renders only one.

Unknown/loading states need first-class logic. A condition based on asynchronous data is often tri-state, not boolean. Rendering privileged content briefly before data resolves is a privacy defect; rendering nothing forever on error is an observability defect.

## Evidence

Use runtime condition engine, permission/feature models, data-binding states, accessibility tree behavior, SSR/hydration if applicable and exported code. Test branch editing under several preview personas/data fixtures, including unknown and error states.

## Failure topology

Failures include hiding an action visually while it remains keyboard/screen-reader reachable; permission-sensitive content flashing before condition resolution; authors unable to select a false branch; an else branch drifting because it is never previewed; conditions duplicated across many children rather than owned by a semantic group; and runtime/export treating “hidden” differently from the builder preview.

## Falsification

Toggle every material authority source, force unknown/loading/error, inspect layout/focus/accessibility tree, preview alternate personas and compare exported runtime behavior. The contract fails if hidden semantics differ from the label, if users can interact with absent/protected content, if authors cannot discover/edit false branches, or if condition evaluation order changes between editor and runtime.

## Recovery

Promote condition authority and outcome type into explicit metadata, introduce tri-state/fallback behavior, group repeated conditions where semantics permit, and provide branch preview controls. Remove security claims from client-only visibility and route authorization to the proper backend/permission owner.

## Output contract

Return a `builder-conditional-visibility-contract` with condition authorities, expression model, outcome semantics, unknown/error behavior, editor ghost/branch representation, accessibility/layout effects, preview fixtures, export/runtime mapping and falsification cases.

## Handoffs

Use data binding for values, permissions/consent for authorization, feature-flag owners for rollout semantics, responsive authoring for range-based transformations, interaction wiring for local state transitions and accessibility owners for presence/focus behavior.