---
name: designing-material-assignment-workflows
description: Own assignment and inspection of visual or engineering materials across objects, faces, instances, variants, libraries, overrides, and physical-property consequences.
---
# Designing Material Assignment Workflows

## Decision ownership

Own how materials are selected, assigned, inherited, overridden, and inspected in a 3D/CAD model. Decide visual versus physical material identity, assignment scope, face/object/component inheritance, library provenance, instance overrides, variants, missing assets, and consequences for rendering or mass properties. This owner does not author shader internals.

## Inputs and evidence

Require material library, visual/physical properties, object/face assignment support, inheritance rules, assembly instance behavior, texture dependencies, density/engineering properties, variants, licensing/provenance, and render/export targets. Identify where appearance and engineering material are intentionally separate.

## Procedure

Show current effective material and its source: direct assignment, parent/default, instance override, or variant. Assignment must preview affected geometry count/scope. Keep engineering material properties such as density/grade distinct from a purely visual shader when the product supports both, and warn when one is missing for downstream calculations. Multi-material face assignments need an inspectable mapping. Library updates should not silently mutate released models; bind or version according to product policy. Missing textures/material references need graceful fallback and resolution links.

## Failure topology

Failures include assigning a visual material and unintentionally changing mass properties, instance override propagating to all occurrences, library updates changing appearance without version control, missing textures rendering silently black, and face-level assignments impossible to audit. Another failure is one material name representing different property definitions across libraries.

## Falsification

Reject if assignment scope is ambiguous; if visual/physical material consequences are conflated; if effective material source cannot be inspected; if library identity/version is absent where reproducibility matters; if missing dependencies look valid; or if engineering calculations use a material density that the UI does not disclose.

## Output contract

Return a `material-assignment-workflows-contract` with: material identities/types; library/version; assignment scope; inheritance/override; face/object/instance behavior; visual-versus-physical properties; missing dependency state; downstream property consequences; variant behavior; and provenance. Include one instance override and one visual-only material case.

## Handoffs

UV/texture mapping handles coordinate assignment, render preview consumes visual material, assembly/mass measurement consumes physical material, and external asset provenance governs library reuse.