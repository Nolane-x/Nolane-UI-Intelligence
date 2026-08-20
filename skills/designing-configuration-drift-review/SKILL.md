---
name: designing-configuration-drift-review
description: Own review of unexpected divergence from desired or peer configuration, including baseline authority, detection freshness, intentional exceptions, remediation, and reappearance.
---
# Designing Configuration Drift Review

## Decision ownership

Own the lifecycle of a configuration drift finding. Decide desired/baseline source, comparison scope, severity, intentional exception, owner, remediation path, verification, and recurrence. Environment diff is a one-time comparison; this skill governs ongoing unexpected divergence.

## Inputs and evidence

Require desired-state source, observed configuration snapshots, detection cadence, environment scope, severity rules, change history, exception policy, remediation capabilities, and ownership. Identify drift that is auto-corrected versus informational.

## Procedure

State the baseline authority explicitly: desired config repository, policy, golden environment, or approved snapshot. Each finding should show desired versus observed, first/last seen, affected target, source freshness, and recent related changes. Allow "expected exception" only with owner, reason, scope, and expiry/review date. Remediation should preview whether it changes live systems and provide verification after apply. Reappearing drift should link to prior incidents/findings rather than create unrelated duplicates.

## Failure topology

Failures include unknown baseline, drift noise from nondeterministic values, permanent exception suppressions, remediation buttons with hidden production effects, stale observations shown as current, and repeated drift treated as new every scan. Another failure is declaring environment compliant because the detector cannot read a field.

## Falsification

Reject if baseline authority cannot be named; if unreadable fields count as compliant; if exceptions can be indefinite without review; if remediation consequence/target is ambiguous; if post-remediation verification is absent; or if recurring identical drift cannot be correlated to history.

## Output contract

Return a `configuration-drift-review-contract` with: baseline authority; observation freshness; drift identity; desired/observed values; severity; recent-change context; exception scope/owner/expiry; remediation preview; verification; recurrence linking; and unknown/unreadable state. Include one recurring drift and one expiring exception case.

## Handoffs

Environment diff provides comparison mechanics, deployment locks/freezes may constrain remediation, software supply-chain provenance can identify config source, and incident operations take over if drift contributes to active impact.