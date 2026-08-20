---
name: designing-software-delivery-pipelines
description: Use when this specialist's decision ownership is materially in scope. Own the operator model for software delivery pipelines across source revision, build, test, artifact, approval, deployment, verification, and promotion stages.
---
# Designing Software Delivery Pipelines

## Parent Contract

**Required parent:** `designing-environment-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the end-to-end delivery pipeline as a traceable sequence of software states. Decide how source revision, jobs, artifacts, environments, approvals, deploys, verifications, and promotions are related and navigated. This owner does not implement CI/CD execution; it ensures a user can understand what version is where, why a stage is blocked, and which action changes delivery state.

## Inputs and evidence

Require pipeline graph/stages, source revision identity, job/run model, artifact identity, environment topology, approval rules, rollout strategies, verification gates, retry/rerun semantics, deployment permissions, and retention/history. Inspect multi-branch, concurrent-release, and partially failed runs rather than a single happy path.

## Procedure

Anchor every run to immutable source and artifact identities. Distinguish pipeline definition from a specific run. Present stage state with dependencies and blockers; a downstream stage waiting on approval must not look identical to one waiting on compute. Separate rerun of a job from creation of a new pipeline run, and show when outputs are reused versus rebuilt. Environment/deployment state should connect back to the exact artifact and run that produced it. Long pipelines need focused navigation without hiding skipped/cancelled stages. High-consequence actions such as promote, deploy, or rollback should expose target, artifact, and consequence before commit.

## Failure topology

Failures include users unable to tell which commit produced a deployed artifact, stage colors with no blocker reason, reruns silently replacing history, approvals detached from the artifact they authorize, skipped jobs appearing successful, and parallel runs overwriting each other's perceived environment state. Another failure is a pipeline graph optimized for spectacle rather than diagnosis.

## Falsification

Reject if a deployed version cannot trace to immutable source/artifact; if blocked/waiting/queued states are visually conflated; if rerun loses the original failed attempt; if an approval can accidentally apply to a different artifact; if skipped stages count as success without explanation; or if parallel runs make environment ownership ambiguous.

## Output contract

Return a `software-delivery-pipelines-contract` containing: pipeline/run identity; stage dependency model; source/artifact linkage; state vocabulary; blocker reasons; rerun/retry semantics; approval binding; environment/deployment linkage; high-consequence action preview; and historical traceability. Include one parallel-run and one partial-failure scenario.

## Handoffs

Delegate stage visualization, build/artifacts, job logs, approvals, deployment targets, rollout strategies, rollback, promotion, release notes, environment diff/drift, locks, release trains, freezes, preview environments, provenance, and diagnosis to dedicated owners. Existing environment and log skills remain lower-level authorities.