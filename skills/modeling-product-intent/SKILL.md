---
name: modeling-product-intent
description: Use when a UI decision depends on what the product is for, which outcomes matter, what users must trust, or which product semantics must remain stable.
---

# Modeling Product Intent

## Overview
Interface quality begins with a truthful product model. This skill prevents visual conventions from defining the product by accident.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the `ui-contract`. Do not rewrite the business/product objective to fit a preferred layout.

## Build the product model
Describe the product in operational terms:
- the core object(s) users manipulate or understand
- the primary value exchange: what users give, do, or decide and what they receive
- the highest-value jobs and the moments when the UI materially affects success
- trust-sensitive facts: money, permissions, identity, irreversible actions, private data, generated output, or uncertainty
- lifecycle of important entities: created, drafted, queued, active, paused, failed, archived, deleted, shared, etc.
- real product vocabulary users already know
- product constraints that must remain visible even when aesthetically inconvenient

Avoid generic category descriptions such as “a SaaS platform.” Name the actual mechanism: incident responders triage alerts and coordinate remediation; researchers compare experiment runs; shop owners reconcile orders and refunds.

## Identify the interface thesis
For the current surface, write one sentence:

`This interface exists so [specific user] can [specific decision/action] with [required confidence/speed/control] despite [main complexity/risk].`

If the sentence contains “manage,” “optimize,” or “seamlessly” without a concrete object/action, refine it.

## Product truth vs presentation
Separate facts from presentation choices.

**Product truth:** a deployment can be partially successful; a role grants destructive access; a payment may be pending; a model answer has uncertainty.

**Presentation choice:** card vs row, table vs list, red vs amber, dialog vs inline confirmation.

Presentation may clarify product truth but may not erase it. A clean UI that turns “partial success” into a single green success state is incorrect.

## Decision hierarchy
Rank what the surface must help users do:
1. decisions whose delay/error is costly
2. frequent high-volume actions
3. state comprehension needed to act safely
4. secondary configuration/exploration
5. optional enrichment

This order influences hierarchy but does not mechanically become screen order. Record conflicts, e.g. an infrequent destructive action may deserve stronger safety treatment than a frequent one.

## Trust model
For each trust-sensitive area identify:
- what users need to know before acting
- what the system knows vs infers
- latency/uncertainty that must be exposed
- whether the action can be undone
- what confirmation or auditability users need afterward

Do not hide uncertainty to make the interface feel decisive.

## Output: `product-intent-model`
Return `product_objects`, `value_exchange`, `surface_thesis`, `high_value_jobs`, `decision_hierarchy`, `entity_lifecycles`, `trust_sensitive_facts`, `product_vocabulary`, `invariants`, and `design_consequences`.

## Quality gate
A visual designer should be able to read the model and understand **why this surface deserves its particular hierarchy and interaction behavior** without seeing any colors or component names.

## Common failures
- Treating “dashboard” as the product model.
- Letting fake demo data invent product semantics.
- Hiding partial/error states to preserve visual cleanliness.
- Copying a competitor’s visible structure without checking whether its underlying product objects match.

## V6 Product-Intent Causal Model
Translate the brief into an **outcome-to-capability map**: every desired user or business outcome must point to the product capability, observable user behavior, and system state that could plausibly cause it. This prevents aesthetic wishes, feature names, and implementation ideas from being confused with product intent. Separate each statement through an **invariant-versus-preference** decision: invariants remain true across candidate solutions; preferences may be traded when evidence shows a better route.

Create an **anti-goal register** for outcomes the product must not optimize accidentally—engagement that delays task completion, visual drama that reduces diagnostic accuracy, automation that removes meaningful control, or onboarding completion that does not create value. Pair goals and anti-goals with a **success-observability plan**: define what could be observed in product behavior, usability evidence, telemetry, or task outcomes and what remains a hypothesis. If no observation could distinguish success from a beautiful mockup, the intent is not operational enough.

Run an **intent drift test** at architecture selection, aesthetic selection, and release. Re-express the current solution without feature names and ask whether it still advances the original outcomes. Trace any new capability back to an explicit goal, discovered necessity, or validated constraint; otherwise mark it scope accretion.

### Falsification
Construct a deliberately polished solution that satisfies the requested feature list but fails the primary outcome. If the intent model still labels it successful, outcome and implementation have been conflated. Also remove one supposed invariant; if no user outcome or risk changes, it was probably a preference.

### Recovery
When intent drift is found, do not patch copy around the current design. Reopen the affected capability, flow, and evidence contracts; demote unsupported preferences, restore invariants, and reroute downstream faculties from the first causal divergence.

## V9 Product Envelope Discovery
Before compressing a product into screens, routes, or a familiar app archetype, perform **broad-before-narrow** discovery. The first model of “what exists” is a hypothesis, not a scope boundary. A prompt such as “sales management platform,” “video editor,” “IDE,” or “team workspace” must trigger a search across actors, entity lifecycles, administration, configuration, trust, recovery, import/export, collaboration, history, integrations, help, system state, and domain-specific operational edges that plausibly matter. This discovery step exists even when the final implementation is intentionally small.

Separate **discovery breadth** from **implementation commitment**. Candidate capability families may become `REQUIRED`, `EXPECTED`, `OPTIONAL`, `EXCLUDED`, or `UNKNOWN`; discovering a capability does not force it onto the screen. The purpose is to prevent the model from silently equating “what I thought of first” with “the whole product.” Every exclusion that would materially change a full-product claim needs rationale and authority, while unresolved high-impact unknowns block that claim.

Calibrate the envelope by ambition. A bounded prototype may explicitly exclude billing, team administration, recovery, audit history, integrations or advanced settings. A production/full-platform claim cannot simply omit such families because they are not visually exciting. Conversely, do not inflate a small utility into enterprise software merely to satisfy a generic completeness checklist. Product class, actors, consequence, lifecycle and stated ambition determine which families deserve disposition.

Run a **scope adequacy challenge** independently from the generator before declaring the envelope closed. Construct an artificially tiny but internally coherent product model—such as dashboard + products + orders for a purported full sales platform—and ask whether important actor outcomes, lifecycle transitions, trust obligations or recovery paths disappear. Probe omitted capability families and compare against product-local evidence, domain expectations and representative real workflows. If the tiny model survives the challenge, the challenge is too weak.

### V9 Falsification
Remove a plausible but non-glamorous family such as settings, account lifecycle, import/export, permission administration, history, recovery, notifications or help. If the product can still claim “full platform” without an explicit disposition and without any consequence appearing in the intent model, the product envelope is under-specified.

### V9 Recovery
Reopen discovery before information architecture. Add the missing family as a hypothesis, identify its actor/outcome/lifecycle consequence, route it to capability inventory, and only then decide whether it is required, expected, optional or explicitly excluded. Never repair an under-scoped model merely by adding more dashboard widgets.

## V10 Empirical Scope Hypothesis
`H-SCOPE-BREADTH` is the falsifiable claim owned by this skill: **broad-before-narrow reasoning should increase recall of consequential implied capability families without turning explicitly bounded utilities into accidental enterprise suites.** That is a behavioral hypothesis, not a statement this skill may certify about itself.

For benchmarked work, preserve a provenance-bearing **scope discovery trace** before screen architecture: actor/job probes, object lifecycles, consequence/recovery probes, domain-specific operations, and candidate capability families. The trace must make it possible to distinguish genuinely discovered product structure from features copied out of the evaluator prompt. Hidden evaluator rubric language is never an input to this skill.

The targeted semantic mutation `scope-compress` removes the broad-before-narrow obligation and lets prompt-literal first recall define the boundary. The `product-envelope` ablation removes this plane from the routed condition. On matched scope tasks, full NUI should improve `capability-recall` and `scope-disposition-quality` relative to those controls; on small negative-control utilities, it should **not** create gratuitous administration, billing, role, integration, or governance machinery. A result that merely contains more feature nouns is not a win.

### V10 attribution test
An efficacy claim for this skill requires all of the following:
1. the same task/model/runtime/tool budget under `baseline`, `nui_full`, and the targeted ablation or mutation;
2. judge evidence that omitted families mattered to actors, lifecycles, trust, or recovery rather than checklist breadth alone;
3. measurable degradation when `scope-compress` or `product-envelope` is applied;
4. no comparable capability-recall shift under a non-semantic placebo;
5. holdout evidence before a cross-task or `EMPIRICAL_TRANSFER` claim;
6. no material increase in unjustified product inflation on bounded negative controls.

Until those runs exist, repository presence, passing validators, and good example outputs support only `STRUCTURAL_ONLY` evidence about this mechanism. Never translate a structural release into “NUI has empirically proven better product thinking.”

### V10 failure interpretation
If full NUI and the ablation perform the same, do not automatically add more product-scope prose. Investigate whether this owner is redundant with another routed faculty, whether the benchmark does not expose implied scope, whether the model ignores the instruction, or whether the evaluator rewards raw list length instead of product consequence. If full NUI recalls more capabilities but dispositions become worse, treat that as an over-expansion regression rather than a partial pass.
