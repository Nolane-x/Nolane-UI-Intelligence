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

## V9 Settings Architecture
Treat a material settings system as an information architecture in its own right, not as a final page named “Settings” containing unrelated toggles. Start from the capability ledger and separate preference, policy, account/security, workspace administration, billing, notifications, integrations, data/export/retention, accessibility, appearance, developer/advanced and product-specific configuration only where those concepts truly exist.

Model **scope precedence** explicitly. A setting may belong to device, session, user, workspace, organization, project/document, role/policy or another product-local scope. State inheritance and override semantics, including locked organization policy and what a user sees when a lower scope cannot override a higher one. Do not display an editable-looking control whose effective value is actually owned elsewhere.

Design **settings search** as semantic retrieval when the inventory becomes large: synonyms, old names, task language and destination context may be needed. Search results must land at the owning setting with enough surrounding context to understand scope and consequence. Deep links, command palette entries or contextual “configure…” actions may accelerate access but do not create duplicate setting ownership.

For every configurable value define default/source, current effective value, persistence/sync behavior, dependency on other settings, validation, preview where meaningful, and **recovery/reset**. Reset may target one setting, one group, one scope or all user customizations; destructive/security/policy configuration needs consequences and appropriate confirmation. Settings that can make the product difficult to operate—density, motion, shortcuts, accessibility, language, high-contrast or custom themes—must retain a safe rollback path.

Scale-test the taxonomy with novice and expert users. Novices should not need to understand backend ownership; experts should not be forced through a wizard for repeated configuration. “General / Advanced / Other” is not acceptable as the main architecture when task- or domain-based distinctions can be named.

### V9 Falsification
Take twenty unrelated settings and place them in one beautiful searchable page. If users can find controls but cannot predict scope, inheritance, effective value, dependency or reset behavior, the settings surface is reachable yet architecturally incomplete.

### V9 Recovery
Return to capability ownership and scope, split configuration by conceptual responsibility, define precedence/persistence/recovery, then redesign navigation and search. Do not repair a broken settings model by adding more cards or a stronger visual hierarchy alone.

## V10 Settings-Architecture Identification
`H-SETTINGS-ARCH` claims something more specific than “settings should be organized”: when configuration has multiple owners/scopes, this faculty should reduce **effective-value ambiguity, configuration dead ends, and flat miscellaneous grouping** while avoiding needless machinery in small preference sets.

The empirical evidence object for this owner is a **configuration semantics map**, not a screenshot of a clean settings page. For each material configuration class it should identify the conceptual owner, scope, default/source, current effective value, override/lock relationship, persistence/sync, dependencies, consequence, and useful recovery/reset boundary. Search and taxonomy are evaluated as retrieval mechanisms only when scale justifies them; their presence is not scored as quality by itself.

`settings-flat-misc` intentionally removes scope precedence, effective-value origin and recovery architecture. The `settings-architecture` ablation removes this V9/V10 extension. On multi-scope tasks, those treatments should increase conflicting or unexplained configuration behavior; on `settings-01`, full NUI must resist the opposite failure of creating enterprise hierarchy for six preferences.

### V10 causal probes
Use paired counterfactuals rather than menu aesthetics:
- switch user, workspace, project or device and ask which value is effective;
- introduce a policy lock and test whether the UI can explain both stored and effective state;
- reset one scope and verify unrelated scopes are preserved;
- deep-link from contextual “configure…” access and verify one canonical setting identity;
- remove search on a large inventory and measure findability, then remove search on a tiny inventory and verify no material harm.

If the full condition merely adds categories/search while precedence remains unclear, the hypothesis fails. If the ablation performs equivalently because every benchmark setting is single-scope, the task corpus is insensitive rather than the skill automatically useless. `STRUCTURAL_ONLY` remains the claim ceiling until matched real-run evidence shows targeted degradation and no over-architecture regression.
