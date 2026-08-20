---
name: designing-build-status-and-artifacts
description: Own build-result interpretation and artifact lineage, including reproducibility, checksums, variants, retention, provenance, and distinction between build success and deployability.
---
# Designing Build Status and Artifacts

## Decision ownership

Own the UI relationship between a build attempt and the artifacts it produced. Decide build status, outputs, variants, checksums/digests, retention, provenance, reproducibility cues, and whether an artifact is eligible for promotion/deployment. A green build does not automatically mean an artifact passed every policy gate.

## Inputs and evidence

Require build system result schema, artifact names/types, immutable digests, platform/architecture variants, test/security attestations, retention rules, provenance, reproducibility metadata, and promotion criteria. Identify artifacts produced partially when a build fails.

## Procedure

Anchor artifact identity to immutable digest plus human-readable name/version. Separate build attempt status from each artifact's eligibility. Show variant dimensions—OS, architecture, configuration—without burying users in file lists. Partial builds must identify which artifacts are valid and which are missing/untrusted. Provide lineage back to source revision and forward to promotions/deployments. Retention/expiry should be visible before artifacts disappear. If reproducible-build evidence exists, show verification without implying it proves functional correctness.

## Failure topology

Failures include ambiguous artifact names, a failed build leaving downloadable files that appear production-ready, checksums hidden, platform variants confused, retention deleting the only deployable artifact unexpectedly, and re-built same-version artifacts sharing a mutable identity. Another failure is labeling an artifact "verified" without explaining which attestation verified what.

## Falsification

Reject if two different bytes can appear under one immutable artifact identity; if a failed/partial build artifact looks equally deployable as a fully gated one; if platform variant is unclear; if source revision cannot be traced; if expiry is invisible until download fails; or if verification badges cannot expose their underlying evidence type.

## Output contract

Return a `build-status-and-artifacts-contract` containing: build-attempt state; artifact identity/digest; variant dimensions; partial-output semantics; eligibility/gates; source lineage; promotion/deployment backlinks; retention/expiry; attestation display; and reproducibility evidence. Include one partial-build scenario.

## Handoffs

Artifact promotion controls environment movement, supply-chain provenance supplies attestations, deployment target selection consumes eligible artifacts, and generic file download handles transfer mechanics.