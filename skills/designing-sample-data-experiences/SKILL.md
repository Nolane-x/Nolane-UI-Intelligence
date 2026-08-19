---
name: designing-sample-data-experiences
description: Use when a product can provide synthetic or example content so users learn real workflows before importing their own data and the interface must keep sample state unmistakably separate, removable, resettable, and non-billable where appropriate.
---

# Designing Sample Data Experiences

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns a reversible learning substrate made from non-user data. It is not migration onboarding and must never blur example records with real customer, financial, production, or operational data. The point is to let users exercise authentic product behavior without the risk or effort of bringing real information first.

## Decision Boundary
Decide whether sample data is created automatically, offered explicitly, or loaded inside a dedicated sandbox/demo workspace. Automatic creation is acceptable only when it cannot contaminate reports, quotas, notifications, integrations, or team workflows. Label sample entities persistently enough that users cannot mistake them for real records after leaving the initial onboarding screen.

Samples should demonstrate meaningful relationships and edge states, not merely populate empty tables. A commerce sample might include products, an order lifecycle, a return, and inventory states; an analytics sample needs coherent metrics whose relationships make sense. Keep complexity bounded so users can understand what the example teaches.

Removal and reset are core states. Users need to know whether deleting sample data is irreversible, whether they can restore it, and whether “Start with my data” removes the sample set or creates a separate workspace. Integrations must not accidentally send sample notifications, webhooks, invoices, or external side effects.

## Failure Topology
- Sample customers appear in real revenue reports and distort business metrics.
- Example records are unlabeled after onboarding, so users think the product imported unknown data.
- Sample order triggers a real webhook or email because examples use the production event pipeline.
- Removing sample data leaves dangling dashboards and broken references.
- Examples are too pristine and never teach empty, error, or exception states.
- User begins real setup inside the sample workspace and later cannot separate real from synthetic content.

## Falsification and Recovery
Falsify with reporting, billing/quota calculation, outbound integration enabled, multi-user workspace, sample reset after user edits examples, transition to real data, deletion of sample workspace, and a user returning weeks later. The design fails if synthetic records can materially affect production decisions or if their provenance becomes invisible.

Recover by tagging sample provenance at the data layer, isolating side effects, excluding examples from authoritative metrics unless explicitly requested, providing reset/delete semantics, and creating a clear transition path into real data or a separate production workspace.

## Output Contract
Return `sample-data-experience-contract` with creation trigger, provenance marking, example scenario design, sandbox/production boundary, reporting/quota exclusions, integration suppression, reset/delete behavior, transition-to-real-data rules, accessibility labeling, and falsification cases.