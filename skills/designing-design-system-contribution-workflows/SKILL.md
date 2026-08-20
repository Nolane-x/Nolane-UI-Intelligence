---
name: designing-design-system-contribution-workflows
description: Design contribution workflows that let distributed teams improve a shared system while preserving ownership, evidence quality, compatibility, and maintenance responsibility.
---

# Designing design-system contribution workflows

A contribution model is the operational API of a design system. Use this skill when product teams can propose tokens, components, patterns, docs, fixes, or behavioral changes and the system needs to accept useful work without becoming a dumping ground.

## Decision ownership

Own intake classes, required evidence, reviewers, decision rights, lifecycle states, contribution ownership, and rejection/exception paths. Decide what contributors may change directly versus what requires system-team stewardship.

## Inputs and evidence

Collect issue and PR history, rejected proposals, review latency, repeated product forks, contributor expertise, test requirements, design assets, maintenance capacity, and release cadence. Identify where proposals stall because ownership is unclear versus where quality is genuinely insufficient.

## Procedure

Create contribution lanes by risk: documentation fixes, compatible bug fixes, additive capabilities, semantic changes, and breaking changes should not carry identical process. Define required artifacts for each lane, including consumer evidence, accessibility behavior, API rationale, migration impact, and verification.

Assign a durable maintainer before accepting new surface area. Separate proposal approval from implementation approval so a strong need does not justify weak code. Publish review SLAs or status expectations and provide a path for time-sensitive product exceptions without silently forking canon.

Capture decisions and rejected alternatives so repeated proposals start from accumulated knowledge.

## Failure topology

A gate-heavy process drives teams to fork instead of contribute. A permissive process accepts one-off product needs and transfers maintenance burden to the central team. Another failure is “drive-by contribution”: a feature merges without an owner for future bugs or platform parity.

Opaque rejection creates political rather than technical routing and reduces future contribution quality.

## Falsification

Walk representative proposals through the workflow and identify ambiguous owners or artifacts. Measure time from intake to decision, not just merge. Sample accepted contributions six months later for maintenance ownership and adoption. Track forks created while contributions are pending; rising fork rate can indicate process failure.

Verify that the workflow can explicitly say no without forcing contributors into endless revision loops.

## Output contract

Produce a `design-system-contribution-workflows-contract` with contribution classes, entry criteria, required evidence, reviewer/decision roles, lifecycle states, service expectations, exception path, maintenance ownership, decision-record requirements, and measurable health indicators.

## Handoffs

Use `governing-design-system-evolution` for semantic change classification, `designing-component-api-governance` for component proposals, `designing-design-system-versioning` for release impact, and `designing-design-decision-records` for durable rationale.