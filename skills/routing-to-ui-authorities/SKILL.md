---
name: routing-to-ui-authorities
description: Use when a UI decision materially depends on platform guidance, institutional practice, component semantics, accessibility evidence, a specialist implementation ecosystem, or a visual frontier whose authority must be scoped before it influences design.
---

# Routing to UI Authorities

## Parent Contract
**Required parent:** `routing-ui-work`.

Receive the `UI_TASK_PROFILE`, hard product/safety/legal obligations, external-source candidates, platform/domain identity, stack, visual ambition, research freshness, and known design-system constraints. The parent decides that external authority is material; this skill decides **which source may speak for which decision**.

## Decision Boundary
Own **decision-dimensional authority**. Never ask “which design system is best?” as one global ranking. Partition the work into questions such as platform convention, service journey, accessibility testing, component semantics, enterprise workflow, commerce workflow, motion mechanics, visual possibility, content guidance, or agent-readable access. A source may be primary on one dimension and irrelevant on another.

This boundary prevents **authority smear**: the accidental promotion of a beautiful gallery into a keyboard-semantics authority, an MCP endpoint into a normative authority, a platform design system into universal web guidance, or a popular component library into product strategy.

## Resolution Model
1. Preserve explicit product, safety, law, regulation, and user-research constraints above all external sources.
2. Split the task into decision dimensions that can independently fail.
3. For each dimension, identify candidates whose stated scope and evidence actually cover the question.
4. Apply context specificity: platform-native guidance gains weight only on its platform; vertical systems gain weight only inside the relevant business/service domain.
5. Use a **primary/corroborating split**. One source owns the decision where a clear authority exists; other sources challenge or enrich it without creating an averaged pseudo-standard.
6. Record why each candidate lost. A rejected source may remain useful for another layer.
7. Escalate currentness when the chosen source is versioned, rapidly changing, policy-bound, or agent-accessed live.

## Authority Interfaces
Treat these as separate channels:
- **normative/platform:** what the target environment expects or requires;
- **semantic/behavioral:** focus, keyboard, screen reader, selection, state, validation, localization;
- **institutional workflow:** accumulated service, enterprise, commerce, or professional practice;
- **implementation:** tested primitives, components, engines, APIs and code;
- **visual frontier:** examples of possible composition, motion, material, 3D, canvas or expressive mechanisms;
- **retrieval adapter:** MCP, llms.txt, skills, structured docs, open code. This changes access cost, not truth status.

## Conflict Protocol
When authorities disagree, do not blend them. Identify the contested dimension, target context, evidence class, and reversal condition. Prefer the source closer to the actual target platform/domain for that dimension unless a higher-level obligation blocks it. Where no authority can be justified, return `UNRESOLVED` and route research rather than choosing the most familiar source.

A React project can use React Aria for semantics, Motion for temporal mechanics, a visual gallery for inspiration, and a local design language for art direction. That is not inconsistency; it is layered authority with explicit interfaces.

## Output — `ui-authority-route-plan`
Return `decisions[] {dimension, source_id, role, reason, applicability, primary_or_corroborating, currentness, evidence_basis, transfer_boundary, reversal_trigger}`, `unresolved_dimensions[]`, `authority_conflicts[]`, and `live_verification_requests[]`.

Every primary decision must explain both why the source applies and what it **does not** authorize.

## Failure Topology
- prestige ranking instead of dimensional authority;
- visual library promoted to semantics because its demo looked polished;
- “official” treated as universal outside its platform/domain;
- access protocol treated as stronger evidence;
- cross-source compromise that satisfies no real system;
- stale authority retained because the local registry still has a URL;
- local research erased by institutional precedent.

## Falsification
Hide every source name and inspect only scope, evidence, target context, and failure coverage. If the route changes because a famous brand name disappeared, the authority decision is contaminated. Swap the target from iOS to generic web or Shopify to generic commerce; platform-specific primaries must lose authority when their applicability disappears.

## Recovery
Repartition the disputed decision, inspect primary artifacts at a current snapshot, downgrade over-broad sources, and preserve unaffected dimensions. If ambiguity remains material, keep the dimension blocked and let `performing-ui-repository-archaeology` or live research resolve it.

## Hard gate
**No external source may materially control a UI decision until its authority is declared for that exact decision dimension, its applicability and transfer boundary are recorded, and access convenience or visual appeal has been prevented from inflating its authority.**
