---
name: measuring-design-system-adoption
description: Measure design-system adoption as verified use and conformance rather than package installation, page counts, or self-reported compliance.
---

# Measuring design-system adoption

Adoption metrics should reveal where the shared system actually governs product UI and where forks, wrappers, overrides, or stale versions undermine it. Use this skill to design measurement that supports migration and investment decisions.

## Decision ownership

Own adoption definitions, telemetry units, conformance dimensions, confidence levels, exception treatment, and reporting semantics. Decide what counts as direct use, wrapped use, copied implementation, deprecated use, override-heavy use, or deliberate exception.

## Inputs and evidence

Collect dependency graphs, source imports, component runtime telemetry where permitted, design-library instances, token usage, package versions, CSS overrides, lint results, migration records, and product inventories. Understand privacy and performance limits before adding runtime instrumentation.

## Procedure

Define several measures rather than one vanity percentage: coverage of eligible UI, current-version adoption, deprecated-surface usage, override/fork incidence, and conformance to behavioral/accessibility contracts. Weight by product criticality or user exposure when raw component counts would mislead.

Combine static and runtime evidence when possible. Static imports show potential use; runtime observations show exposure; visual or contract audits show conformance. Label confidence for inferred metrics.

Segment results by product, platform, team, and release cohort so action owners are visible.

## Failure topology

Package-installed metrics can report 100% adoption while products render mostly bespoke components. Counting design-file instances may diverge from shipped code. Another failure is punishing legitimate exceptions, which incentivizes teams to hide divergence instead of documenting it.

A single global score can improve while critical workflows remain on legacy infrastructure.

## Falsification

Sample products manually and compare observed UI to reported adoption. Seed known exceptions, wrappers, and copied components to test classification. Remove an unused dependency and confirm adoption does not change. Compare static and runtime estimates and investigate large gaps.

Ask whether the metric can distinguish “uses system” from “conforms to system”; if not, it is insufficient for quality decisions.

## Output contract

Produce a `design-system-adoption-contract` defining eligibility, adoption classes, data sources, confidence model, weighting, exception handling, segmentation, dashboards, sampling/audit method, and thresholds tied to concrete migration or governance actions.

## Handoffs

Use `designing-design-system-adoption-migrations` for remediation plans, `designing-design-system-versioning` for current-version definitions, `designing-design-system-contribution-workflows` where forks reveal missing capabilities, and `engineering-ui-evidence-workflows` for broader evidence governance.