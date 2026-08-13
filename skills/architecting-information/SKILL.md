---
name: architecting-information
description: Use when content grouping, hierarchy, labels, relationships, findability, comparison, or the boundary between primary and secondary information materially affects a UI.
---

# Architecting Information

## Overview
Information architecture is the structure users learn. Visual styling may reinforce that structure, but cannot substitute for it.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume product objects, user jobs, task frequency, and known content. Preserve product semantics; do not group solely because elements have similar visual size.

## Inventory by meaning
Create an inventory of information entities, actions, metadata, status, controls, and supporting explanation. For each item identify:
- who needs it
- which task/decision it supports
- urgency and update frequency
- relationship to other items
- whether comparison across items matters
- whether it is actionable, descriptive, or diagnostic

## Build the conceptual model
Define the nouns and relationships users should be able to learn. Prefer user-recognizable concepts over implementation boundaries. “Notifications,” “API access,” and “Billing” are conceptual areas; internal service names are not unless users genuinely operate those services.

## Grouping tests
A group is legitimate when at least one of these is true:
- items share a task or decision
- items describe the same object/state
- users must compare them together
- they share a lifecycle/permission model
- they are sequential parts of one understandable process

Do not group because “four cards fit in a row.”

## Hierarchy design
Rank layers:
- orientation: where am I / what object am I looking at
- decision-critical state
- primary actions
- supporting evidence/context
- secondary settings/history/help

The rendered hierarchy should allow a user to predict these layers before reading every label. Use position, scale, type, spacing, alignment, and disclosure before adding decoration.

## Label discipline
Labels must be mutually distinguishable, user-facing, and stable. Test sibling labels together: if “General,” “Advanced,” and “Other” are the main distinctions, the taxonomy is probably avoiding a real model.

Use one name for one concept across navigation, headings, actions, empty states, and feedback unless context demands an explicit grammatical variation.

## Comparison architecture
When users compare entities, align comparable fields spatially and semantically. Cards with different internal layouts reduce comparison even if each card is individually attractive. Consider tables, aligned rows, matrices, or small multiples when comparison dominates.

## Scalability stress
Project the IA under:
- 3 items vs 300
- one workspace vs many
- shallow vs nested objects
- new feature categories
- long translated labels
- permissions hiding some branches

A structure that only works for the demo dataset is not architecture.

## Output: `information-architecture-map`
Return `entity_inventory`, `conceptual_model`, `groups`, `hierarchy_layers`, `label_taxonomy`, `comparison_requirements`, `disclosure_rules`, `scalability_stress`, and `open_ia_risks`.

## Quality questions
Can a user predict where a new related item belongs? Can two sibling groups be distinguished without reading their contents? Can the hierarchy survive if all color and borders are removed? If not, revisit the structure.

## V6 Information Architecture Stress Protocol
Before drawing navigation, derive an **object-action taxonomy**: canonical user-visible objects, their parent/peer relations, lifecycle, actions, attributes, and views. Distinguish a destination from a filter, a persistent object from a transient result, and a domain concept from an internal service boundary. Use this taxonomy to decide labels and grouping rather than inheriting the backend tree.

When one item legitimately belongs in multiple conceptual neighborhoods, record a **polyhierarchy decision** instead of forcing a single tree. Define the canonical identity, alternate access paths, breadcrumb behavior, URL/deep-link truth, and whether duplicate representations share state. Set a **retrieval-path budget** for critical objects/tasks: how many recognition, navigation, search, or switching steps are acceptable for frequent and infrequent work, including return visits.

Use an **information-scent probe** on every major label or group: show the cue without its destination and ask what a user would expect behind it, then compare that expectation with actual contents. Finally run a **scale-growth simulation** with realistic 10x object counts, longer labels, added roles, archived items, and nested ownership. IA that only works for the seed demo is not architecture.

### Falsification
Swap two labels while retaining the same layout, or remove breadcrumbs/search shortcuts. If test users or an independent critic cannot predict destination or recover orientation, the grouping is too visual or internally named. Introduce a new object type and see whether the taxonomy can place it without a catch-all “Other.”

### Recovery
If scent or scale fails, return to the object-action taxonomy and regroup by user decisions rather than tweaking menu styling. Preserve stable object IDs and deep links while changing presentation; document migrations when canonical paths move.
