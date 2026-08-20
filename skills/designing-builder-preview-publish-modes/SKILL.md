---
name: designing-builder-preview-publish-modes
description: Use when a visual builder separates edit, preview, staged/test, and published runtime states and authors must know which revision, data/environment, permissions, and generated artifacts each mode represents.
---

# Designing Builder Preview and Publish Modes

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This owner establishes evidence boundaries between authoring and executable delivery. Preview is for observing behavior without editor interference; publish is a release operation that binds a concrete revision and environment. Neither may be treated as a cosmetic toolbar toggle.

## Decision ownership

This skill owns the decision boundary between editable authoring state, executable preview, staged/test delivery, and published runtime truth. For each mode it must resolve which revision is included, which data/auth/environment is active, whether side effects are real or isolated, and whether generated artifacts are ephemeral or release-bound. Deployment mechanics remain with delivery owners; this skill prevents the builder from presenting materially different execution authorities as interchangeable “modes.”

## Mode contract

Define named modes with exact capabilities: edit, interactive preview, device/responsive preview, test/stage environment, published production, and optionally historical published revision. For each, state whether editor overlays exist, whether side effects are mocked/real, which data and auth identity are used, what asset/code generation has run, and whether unsaved editor changes are included.

Bind every preview/publish result to a revision. A preview of working tree changes can be labeled ephemeral; a staged build needs a stable build/revision identifier; production needs a deployment record. If publishing involves asynchronous compilation, asset upload or server configuration, distinguish `requested`, `building`, `validated`, `released`, `partially released`, `failed`, and `rolled back` rather than showing a single spinner.

Preview isolation is an interaction requirement. Canvas selection handles, drag gestures, keyboard shortcuts and editor focus management must not change the behavior being tested. However, preview tooling may provide diagnostics through a separate non-interfering channel. Make it obvious when test data or sandbox APIs differ from production.

Publication should surface validation relevant to the artifact: broken bindings, inaccessible routes, unresolved component references, unsupported code, environment secrets, permission issues, missing assets and responsive/runtime errors. A successful build is not proof of usable UI, but known blockers should not be hidden behind a green publish button.

## Evidence

Inspect build/deploy pipeline, editor revision model, environment/data configuration, generated artifacts, runtime URLs, rollback support and analytics/logging. Test publication with concurrent edits, failing assets, stale preview, sandbox vs production data and rollback to earlier revision.

## Failure topology

Failures include preview accidentally sending real emails; production excluding unsaved changes the author thought were included; another collaborator publishing a different revision while the UI still says “your changes are live”; a failed partial deployment leaving assets/code mismatched; and preview passing because it uses fixtures that conceal missing production permissions.

## Falsification

Modify content while preview is open, publish during concurrent collaboration, intentionally break a binding/asset, switch environments, run a consequential interaction and rollback. The contract fails if the user cannot identify the exact revision/environment observed, if editor mechanics contaminate runtime behavior, if production side effects occur in ordinary preview without explicit authority, or if partial/failure states are collapsed into success.

## Recovery

Bind surfaces to immutable revision/build IDs, invalidate stale previews after material changes, separate sandbox credentials/data, and reconcile partial releases before allowing another publish. Provide one-click navigation from deployment diagnostics back to the responsible authored object where identity is known.

## Output contract

Return a `builder-preview-publish-modes-contract` containing mode capability matrix, revision binding, editor-isolation rules, environment/data identity, side-effect policy, validation gates, publish state machine, concurrent-edit behavior, rollback semantics, diagnostics linking and exact-revision evidence requirements.

## Handoffs

Use software delivery owners for deployment mechanics, runtime verification for behavioral proof, data-binding/interaction owners for preview fidelity, design-code drift review for generated artifacts and completion gates for claims beyond successful publication.