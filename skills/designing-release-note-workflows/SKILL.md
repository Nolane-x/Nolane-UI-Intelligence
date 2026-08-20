---
name: designing-release-note-workflows
description: Use when this specialist's decision ownership is materially in scope. Own release-note assembly, change attribution, audience filtering, breaking-change prominence, draft/review/publish state, and traceability to shipped artifacts.
---
# Designing Release Note Workflows

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the workflow that turns shipped changes into trustworthy release communication. Decide change sources, grouping, audience variants, breaking/security change treatment, draft/review/publish states, artifact/release binding, and correction history. Generic content publishing handles mechanics; this owner ensures notes correspond to what actually shipped.

## Inputs and evidence

Require release artifact/version, commits/PRs/issues, feature flags if they affect exposure, migration/breaking-change metadata, security disclosure policy, audience, localization, reviewers, and publish channels. Identify changes merged but not included in the artifact and features shipped dark but not user-visible.

## Procedure

Seed candidate changes from artifact provenance rather than branch history alone. Require classification: user-visible feature, fix, breaking change, deprecation, operational change, security note, or internal/no-note. Group by audience impact. Breaking changes and required migration steps must remain prominent and cannot be buried by auto-generated prose. Drafts need reviewers and explicit binding to release digest/version. Publishing should preserve history; corrections append or version notes. If rollout/flags mean availability differs, state exposure conditions.

## Failure topology

Failures include notes listing merged-but-not-shipped work, missing breaking changes, auto-generated summaries inventing impact, release notes detached from artifact identity, dark features announced prematurely, and corrections rewriting the original publication with no trace. Another failure is overwhelming users with internal implementation details.

## Falsification

Reject if a note cannot trace to shipped artifact evidence; if a known breaking change can be omitted without review; if feature availability conditions are hidden; if publication can bind to mutable "latest" rather than a release identity; if corrections erase history; or if generated summary claims user impact unsupported by source evidence.

## Output contract

Return a `release-note-workflows-contract` with: release/artifact binding; change-source rules; classification; audience grouping; breaking/deprecation prominence; rollout/flag disclosure; draft/review/publish states; localization handoff; correction/versioning; and source traceability. Include one merged-not-shipped change case.

## Handoffs

Supply-chain/artifact provenance provides shipped scope, feature-flag management provides exposure state, content localization/publishing provide language/channel mechanics, and release trains provide timing.