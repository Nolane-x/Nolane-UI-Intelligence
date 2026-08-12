---
name: governing-design-systems
description: Use when a design system spans teams or products and needs contribution rules, ownership, adoption, exceptions, quality gates, versioning, deprecation, decision rights, or mechanisms to prevent semantic fragmentation.
---

# Governing Design Systems

## Overview
A design system is a socio-technical product. Governance decides who may change shared semantics, how evidence enters the system, how exceptions work, and how adoption remains faster than local reinvention.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require system scope, teams/products, maintainers, contribution model, release/version process, component/token architecture, accessibility ownership, adoption pain, and current forks/exceptions. This skill governs decisions; it does not replace component design.

## Decision Model
Define decision classes: token/semantic foundation, component API/behavior, visual style, content pattern, accessibility contract, platform adaptation, experimental pattern, and breaking change. Assign decision rights and required review to each. A minor icon tweak should not need the same ceremony as changing focus semantics across products.

Create a contribution funnel: problem evidence → existing solution search → proposal with affected use cases → accessibility/platform review → implementation/evals → release → adoption/migration → post-release evidence. Contributions solve shared problems rather than promote a team’s local aesthetic preference.

Exceptions are explicit, scoped, owned, and time-bounded. A product may need a domain-specific pattern, but copying a component and changing semantics silently creates system debt. Track forks and either upstream the generalized need or preserve the exception with rationale.

Govern adoption as UX. Documentation, examples, design assets, code APIs, migration tools, support, and release notes determine whether teams use the system. Measure duplicate local primitives, accessibility defect rates, upgrade lag, contribution turnaround, and task-fit feedback — not only component count.

## Evidence
Use adoption telemetry, issue/contribution history, product audits, accessibility findings, API breakage, migration effort, user research across teams, and exception inventory. Popularity of a component does not prove correct semantics.

## Output Contract
Return a `design-system-governance` with `scope`, `roles_and_decision_rights`, `change_classes[]`, `contribution_funnel`, `review_requirements`, `exception_registry`, `release_policy`, `adoption_support`, `health_metrics[]`, `debt_signals[]`, and `governance_tests[]`.

## Failure Traps
- Central team approval required for every tiny change.
- Anyone can change semantic tokens/components with no compatibility review.
- “No exceptions” policy driving teams to hidden forks.
- Component count used as system maturity metric.
- Accessibility review only after release.
- Design library and code implementation drifting independently.
- Governance based on taste authority instead of shared evidence.

Strong governance makes the correct shared path easier than the local fork while preserving justified domain differences.