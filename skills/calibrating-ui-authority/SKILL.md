---
name: calibrating-ui-authority
description: Use when UI sources disagree, a community heuristic conflicts with a standard or platform rule, guidance has draft or regulatory status, or a decision needs an explicit source-of-truth hierarchy.
---

# Calibrating UI Authority

## Overview
Resolve evidence conflicts without flattening unlike sources into “best practices.” Authority is scoped: a regulator can dominate a medical safety question while platform guidance can dominate a native interaction convention, and neither automatically owns brand aesthetics.

## Parent Contract
**Required parent:** `researching-ui-frontiers`.

Consume source records with explicit status and scope. If provenance is missing, return an authority gap instead of ranking from reputation alone.

## Decision Model
For every disputed decision, define four things before ranking sources: jurisdiction/surface, affected user outcome, failure consequence, and whether the issue is conformance, safety, platform convention, empirical usability, or taste. Apply the NUI authority ladder: explicit product safety constraints; applicable law/regulation and normative standards; regulator/safety authority guidance; platform authority; validated product evidence; empirical human-factors evidence; mature design-system guidance; community heuristics; model preference.

The ladder is not blind precedence. A higher source must actually govern the question. WCAG cannot choose a brand typeface; a platform HIG cannot waive an applicable accessibility requirement; a community anti-slop rule cannot override an accepted design target. Drafts remain informative unless another contract explicitly adopts them. Regulatory guidance receives domain scope, not universal scope.

When two same-level authorities differ, inspect assumptions: input modality, device, driving/parked state, user expertise, locale, safety class, version, or implementation technology. Often the right resolution is conditional rather than a winner. Preserve unresolved conflict as an obligation requiring human/domain review when consequences are material.

## Evidence
Cite the exact source records, status, reviewed date, and scope relation used in the resolution. Record why rejected evidence was inapplicable rather than simply “lower quality.” For empirical evidence, note sample/task fit and whether the result is observational, experimental, expert guidance, or product telemetry.

## Output Contract
Return an `authority-resolution` with `decision_question`, `applicable_sources[]`, `excluded_sources[] {id, reason}`, `precedence_chain[]`, `scope_conditions[]`, `resolved_rule`, `confidence`, `unresolved_conflicts[]`, and `human_review_required`.

## Failure Traps
- “Official” as a substitute for checking scope.
- Newer automatically outranks normative status.
- Treating a Working Draft as a released requirement.
- Letting a design system override law, safety, or accessibility.
- Treating user preference as irrelevant when it is compatible with higher constraints.
- Averaging contradictory requirements into a vague compromise.
- Hiding uncertainty to make the router appear decisive.

The result must tell later skills *why* a rule is binding and where it stops binding.