# UI Industry 1000 — Batch 005 Design

Date: 2026-08-20
Target: expand the canonical skill graph from 674 to exactly 774 nodes.

## Objective

Batch 005 adds 100 independently owned UI specialists across five under-covered courts: design-system governance, responsive composition, typography, AI/agent interaction, and research/verification. The batch is an expansion of decision ownership, not a vocabulary expansion. A node is canonical only when it owns a failure class that cannot be adequately discharged by an existing parent or sibling.

## Non-negotiable authoring rule

Canonical `SKILL.md` prose is written individually. No loop, template, cartesian product, suffix inflation, keyword substitution, or script may create or transform specialist prose. Automation is permitted only for deterministic bookkeeping such as graph insertion, count checks, provenance tables, routing tests, and duplicate detection.

Each skill must be independently falsifiable and must expose an actionable output contract. Shared section names are repository protocol; shared intellectual content is not.

## Court A — Design-system governance

Owns decisions that make a component/token system evolvable across products, brands, platforms, versions, and contributors. The court is rooted under `governing-design-systems`. It deliberately separates token ontology, aliasing, modes, inheritance, component API policy, migration, contribution, documentation, adoption, and parity because each fails through a different organizational or runtime mechanism.

## Court B — Responsive composition

Owns behavior when available space, content pressure, modality, and viewport constraints change. The court is rooted under `adapting-responsive-layouts`. It treats responsive behavior as stateful composition rather than a list of breakpoint widths: priority collapse, region reordering, overflow, docking, media crops, loading/error states, and parity each have separate failure topology.

## Court C — Typography

Owns reading, hierarchy, rhythm, numerical scanning, truncation, code, variable-font behavior, fallback, legal text, and zoom resilience. The court is rooted under `crafting-typography`. The specialists are intentionally mechanic-specific so typographic quality can be tested instead of reduced to subjective taste.

## Court D — AI / agent interaction

Owns user control and comprehension when software can plan, call tools, mutate external state, preserve context, delegate, continue in the background, and return uncertain or partially complete results. The court is rooted under `designing-agent-autonomy-and-control`. It does not duplicate generic chat UX or generic confirmation UI; every node is bound to an agentic state transition or side-effect boundary.

## Court E — Research / critique / verification

Owns the evidence pipeline used to decide whether UI hypotheses survive contact with users and rendered product behavior. The court is rooted under `challenging-ui-designs`. It separates protocol design, observation, synthesis, triangulation, experiment interpretation, regression evidence, fidelity auditing, accessibility evidence, and durable decision records.

## Acceptance invariants

- exactly 100 Batch 005 slugs, 20 per court;
- final canonical graph count exactly 774;
- every skill has matching frontmatter name and repository-standard behavioral sections;
- every specialist has at least 2,200 characters of substantive individually authored guidance;
- graph metadata is locked by the acceptance test;
- every parent chain reaches `using-nolane-ui` without cycles;
- all Batch 005 outputs are unique and do not collide with the prior graph;
- no exact normalized body duplicates and no trivial rename pair;
- full repository tests and `scripts/nui-validate` remain green.

## Routing shape

The batch preserves hierarchical routing. A task should first land on an established owner (`governing-design-systems`, `adapting-responsive-layouts`, `crafting-typography`, `designing-agent-autonomy-and-control`, or `challenging-ui-designs`), then load only the specialist needed for the material decision. The 100 nodes are not a preload bundle.

## Provenance posture

External standards and mature systems may be used as evidence for mechanisms, but no source is copied as a house style. Specialist guidance must distinguish normative requirements from heuristics and product-specific evidence. The final provenance ledger records ownership, parent, output, court, and the failure boundary that justifies canonization.