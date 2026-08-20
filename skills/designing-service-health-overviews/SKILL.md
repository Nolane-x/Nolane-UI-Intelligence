---
name: designing-service-health-overviews
description: Own operational service-health summaries that distinguish impact, telemetry confidence, dependency state, partial degradation, recovery, and unknown observation rather than collapsing everything into red/green.
---
# Designing Service Health Overviews

## Decision ownership

Own the incident-facing view of current service health. Decide health dimensions, affected scope, partial degradation, telemetry freshness/confidence, dependency contribution, recovery trend, and unknown state. It does not define SLOs or monitoring detectors; it determines how evidence is synthesized without hiding uncertainty.

## Inputs and evidence

Require service catalog, key user journeys, SLO/SLI or health metrics, telemetry freshness, region/tenant segmentation, dependency topology, known maintenance, baseline/seasonality, and incident impact signals. Identify metrics that can remain green while customers are failing.

## Procedure

Organize health around service capabilities or user journeys, then support infrastructure drill-down. Separate availability, latency, correctness, capacity, and dependency state when they can fail independently. Display freshness and missing telemetry. Partial degradation should show affected segment and denominator; avoid global red when 1% is affected unless policy justifies it. Recovery views should show duration/stability, not only the latest sample. Dependency health may inform but should not automatically determine parent service status without evidence of impact.

## Failure topology

Failures include red/green summary with no evidence, missing telemetry shown as healthy, regional outage hidden by global average, one recovered sample triggering green, dependency failure assumed to imply user impact, and dashboard panels using inconsistent time windows. Another failure is too many low-level metrics for commanders to determine customer effect.

## Falsification

Reject if unknown telemetry can render green; if the health summary cannot identify affected segment; if panels compare incompatible windows without disclosure; if a dependency issue changes service health absent impact evidence; if recovery status ignores recent instability; or if a user-impact metric cannot be traced to source/freshness.

## Output contract

Return a `service-health-overviews-contract` with: service/journey hierarchy; health dimensions; segment scope; unknown/freshness states; dependency treatment; partial-degradation representation; recovery stability window; source drill-down; and commander summary. Include one regional partial outage and one telemetry-gap case.

## Handoffs

Dependency impact analysis evaluates likely propagation, severity declaration consumes confirmed impact, status-page authoring chooses public wording, and topology maps provide structural context.