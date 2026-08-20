---
name: designing-software-supply-chain-provenance
description: Use when this specialist's decision ownership is materially in scope. Own human-readable provenance and attestation interfaces linking software artifacts to source, builder, dependencies, signatures, policies, and verification state without collapsing trust to one badge.
---
# Designing Software Supply Chain Provenance

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the UI representation of software artifact provenance. Decide how source revision, build identity, builder, dependency/material references, signatures, attestations, SBOM/provenance documents, verification status, policy results, and missing evidence are exposed. This owner does not perform cryptographic verification; it makes verification scope and evidence legible.

## Inputs and evidence

Require artifact digest, source URI/revision, build system identity, attestation types, signature verification, dependency/material references, SBOM, policy evaluations, issuer trust configuration, timestamps, and revocation/expiry. Identify evidence that is optional versus required for a given promotion target.

## Procedure

Center provenance on immutable artifact digest. Present each attestation separately with type, issuer, subject, verification result, policy relevance, timestamp, and evidence link. Avoid a single "trusted" badge unless its exact policy can be expanded. Missing, unverifiable, expired, revoked, and policy-failing evidence need distinct states. Show source/build chain graphically or as structured lineage only when relationships are accurate. Promotion/deployment surfaces should summarize required provenance and deep-link to the full evidence.

## Failure topology

Failures include green shield icons with unknown meaning, signature valid but issuer untrusted presented as verified, missing evidence treated as pass, provenance attached to version label instead of digest, expired attestations hidden, and huge SBOMs dumped without policy relevance. Another failure is conflating provenance with vulnerability-free status.

## Falsification

Reject if a trust badge cannot name the policy/evidence behind it; if artifact digest is absent; if missing and passing evidence look the same; if verification result lacks issuer/subject; if revoked/expired state is hidden; or if the UI implies signed provenance proves software is secure/correct.

## Output contract

Return a `software-supply-chain-provenance-contract` with: artifact subject/digest; source/build lineage; attestation inventory; issuer/verification state; required-versus-optional evidence; missing/expired/revoked/failing states; policy mapping; evidence links; and summary/deep-link behavior. Include one valid-signature/untrusted-issuer case.

## Handoffs

Build/artifact ownership supplies subject identity, release approvals consume required evidence, artifact promotion enforces stage policy, and security operations may investigate provenance anomalies without redefining cryptographic truth.