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
