---
name: designing-patch-exposure-review
description: Use when teams must understand which systems remain exposed to a remediable vulnerability, why patch state differs across assets, and what deployment or exception evidence justifies remaining exposure.
---
# Designing Patch Exposure Review

## Decision ownership

Own the review surface that connects vulnerability risk to actual patch/configuration state across assets. Decide how applicable, installed, pending, failed, deferred, superseded, not-applicable, and unknown remediation states are represented; how maintenance windows and reboot requirements affect exposure; and how analysts distinguish a patch being available from a control actually being effective. This faculty does not schedule deployments or rank all vulnerabilities globally.

## Inputs and evidence

Require asset identity and lifecycle, vulnerability applicability, current software/package version, available remediation versions, patch management source, install attempt history, reboot or service-restart state, maintenance window, deployment ring, exception owner, compensating controls, last-seen timestamp, and scanner revalidation. Include machines that are offline, ephemeral, replaced, partially patched, pending reboot, manually remediated, or intentionally deferred. Track source freshness separately for inventory, patch manager, and vulnerability scanner.

## Procedure

Build exposure state from evidence, not one boolean “patched” field. Show applicability, intended remediation, deployment status, verification status, and current residual exposure as separate stages. Make “installed but not active until reboot” distinct from completed remediation. Group assets by actionable reason—deployment failed, ring not reached, maintenance window future, unsupported version, exception active, unknown status—rather than only by operating system. Let users compare expected fleet policy to actual state and inspect the evidence timestamps behind discrepancies. For large estates, highlight concentration of exposure by internet reachability, business service, privilege, or patch wave without hiding individual exceptions.

## Failure topology

- Patch manager says installed and the UI marks risk closed before scanner or runtime verification.
- Pending reboot is indistinguishable from fully remediated.
- Offline assets vanish from counts even though they will reconnect vulnerable.
- A broad exception hides which specific machines or versions are covered.
- Asset identity drift attributes a patch result to a replacement machine with the same name.
- “Not applicable” comes from stale inventory and is treated as permanent truth.
- Deployment failure reasons are hidden behind one red status, preventing operational action.

## Falsification

Use assets in states installed-awaiting-reboot, deployment-failed, offline, stale-inventory, manual-fix, active exception, and verified remediated. Include one renamed/rebuilt host. The design fails if a reviewer cannot tell what evidence establishes current exposure, if unknown becomes safe, or if exception scope cannot be reconstructed.

## Output contract

Return `patch-exposure-review-contract` containing remediation-state machine, applicability model, evidence freshness, verification rules, reboot/restart semantics, grouping by actionable cause, exception visibility, fleet-to-asset drilldown, and exposure validation scenarios.

## Handoffs

Global remediation ranking belongs to `designing-vulnerability-prioritization`; deployment mechanics belong to software-delivery and endpoint-management owners; asset truth routes to `designing-security-entity-investigation`. This skill owns the state between “a fix exists” and “this asset is actually no longer exposed.”