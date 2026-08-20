---
name: designing-design-system-versioning
description: Version design-system contracts according to observable consumer impact across code, visuals, behavior, and assets rather than package API shape alone.
---

# Designing design-system versioning

A design-system release can be breaking even when every function signature still compiles. Use this skill to define version boundaries for components, tokens, assets, behavior, and documentation consumed by many products.

## Decision ownership

Own the release compatibility model and versioning policy. Decide what counts as major, minor, patch, experimental, or separately versioned data; how coordinated packages share versions; and how visual or accessibility behavior is classified when source APIs are unchanged.

## Inputs and evidence

Collect public component APIs, token contracts, CSS/custom-property surfaces, assets, design-library components, generated platform packages, behavioral snapshots, accessibility semantics, and downstream override patterns. Review past releases that caused product regressions despite nominal semantic-version compatibility.

Identify whether consumers can pin components independently or must upgrade a bundle.

## Procedure

Define compatibility dimensions: source/API, rendered structure, visual metrics, interaction behavior, accessibility semantics, token resolution, asset identity, and migration tooling. Specify which changes are guaranteed stable within each release class. Treat default-value changes and renamed semantics as observable contract changes even when types remain identical.

Choose package coupling deliberately. Lockstep versions simplify compatibility reasoning but increase release blast radius; independent versions reduce blast radius but require a compatibility matrix. Document prerelease and experimental guarantees separately from stable surfaces.

Require release notes to state migration obligations and known cross-platform differences.

## Failure topology

Type-centric semver misses visual and behavioral breakage. Excessive major versions make consumers stop trusting upgrade paths, while falsely compatible releases make them fear every patch. Independent package versions can produce unsupported combinations; lockstep monorepo versions can force unnecessary upgrades.

Another failure is versioning runtime packages while leaving design-tool libraries or generated token artifacts unversioned, creating mismatched sources of truth.

## Falsification

Take representative proposed changes and have multiple maintainers classify them using the policy. Material disagreement means rules are underspecified. Install old consumers against candidate releases and run rendered, accessibility, and interaction regression suites. Test package combinations at compatibility boundaries.

Verify that a consumer can determine supported versions without reading internal repository history.

## Output contract

Produce a `design-system-versioning-contract` defining compatibility dimensions, release classes, package coupling, experimental policy, supported combination rules, release-note obligations, migration thresholds, cross-platform treatment, and examples of changes classified with rationale.

## Handoffs

Use `governing-design-system-evolution` to classify change intent, `designing-token-deprecation-migrations` for token retirement, `designing-component-api-governance` for interface changes, and `designing-design-system-adoption-migrations` for downstream rollout.