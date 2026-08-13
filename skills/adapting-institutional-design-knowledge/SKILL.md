---
name: adapting-institutional-design-knowledge
description: Use when mature design systems, public-service guidance, enterprise systems, accessibility programs, or vertical platforms contain accumulated practice that should inform a local product without being copied as universal truth.
---

# Adapting Institutional Design Knowledge

## Parent Contract
**Required parent:** `synthesizing-cross-source-ui-language`.

Receive source dossiers, authority assignments, local users/tasks, jurisdiction/platform/domain, research evidence, and the exact pattern or workflow being considered. This skill handles the gap between a mature institution having years of practice and NUI merely knowing that a domain exists.

## Decision Boundary
Own transfer of **accumulated concrete practice**. Institutional evidence can be more valuable than abstract principles because it often encodes repeated production failures, service research, accessibility testing, workflow conventions, migration history, and operational constraints. But institutional maturity does not make a rule universal.

## Adaptation Protocol
1. Identify the institution's original context: users, service/business goal, platform, organization, risk, scale, and evidence history.
2. Extract the mechanism, not the branded layout. “Eligibility before application” is transferable logic; a ministry's exact page hierarchy is not automatically transferable.
3. Record the evidence class behind the mechanism: tested component behavior, field research, production pattern, accessibility test, platform convention, or conceptual guidance.
4. Build a **transfer-boundary ledger** with `transfer`, `adapt`, `revalidate`, and `do-not-transfer` entries.
5. Calculate **institutional evidence debt**: what the upstream institution has validated that the local product has not. Debt is not solved by citing the source; it identifies local validation still required.
6. Require **local-context revalidation** whenever population, jurisdiction, workflow, device/input, language, risk, or business incentives differ materially.
7. Preserve disagreements between institutions when they expose context dependence instead of averaging them into generic advice.

## Vertical Depth Rule
When a vertical source “lives” in the problem—government service, enterprise ERP, commerce platform, creative professional workflow—prefer its concrete workflow semantics over NUI's generic ontology for that exact scope. NUI still owns cross-domain routing, conflicts, hard obligations and local synthesis.

## Output — `institutional-knowledge-synthesis`
Return `borrowed_mechanisms[]`, `upstream_context`, `evidence_basis[]`, `transfer_boundary_ledger[]`, `institutional_evidence_debt[]`, `local_revalidation[]`, `contradictions[]`, `rejected_trade_dress[]`, and `decision`.

## Failure Topology
- cargo-culting institutional UI because it is “best practice”;
- copying workflow order without matching user need;
- assuming decades of usage equals evidence for a different population;
- extracting only surface style from a system whose value is operational semantics;
- treating accessibility guidance as proof of the local implementation;
- losing local user research beneath source authority.

## Falsification
Change one defining upstream condition—jurisdiction, expert role, platform, or transaction model. Ask which transferred mechanisms still have causal support. If everything survives unchanged, adaptation is too generic. Ask what local evidence would overturn the borrowed pattern; if no answer exists, the mechanism has become dogma.

## Recovery
Narrow scope, restore upstream context, convert unsupported transfers into hypotheses, and schedule local validation. When evidence debt is too large for a consequential decision, block adoption and route research or a better-matched authority.

## Hard gate
**Institutional practice may influence local design only when its original context, evidence basis, transfer boundary, institutional evidence debt, and required local revalidation are explicit; upstream maturity cannot waive local mismatch.**
