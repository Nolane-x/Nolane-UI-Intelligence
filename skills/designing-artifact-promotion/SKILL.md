---
name: designing-artifact-promotion
description: Own promotion of immutable software artifacts through environments or release channels, preserving provenance, gate evidence, target eligibility, and distinction between promoting bytes and rebuilding them.
---
# Designing Artifact Promotion

## Decision ownership

Own movement of an already-built immutable artifact between lifecycle stages such as dev, staging, approved, production candidate, or distribution channel. Decide source artifact identity, destination stage, evidence gates, revalidation, promotion history, and whether a rebuild would create a new artifact rather than a promotion.

## Inputs and evidence

Require artifact digest/version, current stage/channel, target stages, promotion policy, test/security attestations, approvals, retention, compatibility, and provenance. Determine whether metadata can change during promotion and whether signed attestations are destination-specific.

## Procedure

Show the immutable digest prominently and treat a rebuild—even from identical source—as a different artifact unless reproducibility policy proves equivalence. Promotion should list current and target stage, required checks, approvals, and missing evidence. Do not imply that moving metadata copies bytes if the underlying registry behavior differs; expose actual result. Record every promotion event and prevent cycles/illegal regressions unless policy allows demotion. Re-run destination-specific checks when evidence is not portable.

## Failure topology

Failures include "promote version 1.2" when several digests share that label, silently rebuilding during promotion, carrying stale attestations to a stricter target, losing origin history, and promoting an artifact whose retention is near expiry. Another failure is treating environment deployment and artifact promotion as the same state transition when one changes registry eligibility and the other changes runtime.

## Falsification

Reject if the immutable artifact cannot be identified; if promotion can substitute a rebuild without new identity; if destination-specific required evidence is missing but the action appears allowed; if promotion history cannot trace origin; or if UI language conflates promotion with deployment consequences.

## Output contract

Return an `artifact-promotion-contract` with: artifact digest/version; source/target stage; eligibility checks; approval/evidence portability; rebuild distinction; promotion/demotion rules; provenance history; retention cue; destination-specific revalidation; and deployment separation. Include one same-version/different-digest case.

## Handoffs

Build/artifact ownership defines identity, release approval gates supply decisions, supply-chain provenance supplies attestations, and deployment owners act only after promotion/eligibility is established.