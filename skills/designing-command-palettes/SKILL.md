---
name: designing-command-palettes
description: Use when a product needs a fast searchable command surface that unifies actions, navigation or object operations without becoming a second inconsistent information architecture.
---

# Designing Command Palettes

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

A command palette is not merely a modal search box. This faculty owns the model that turns a large command/action vocabulary into a searchable, keyboard-first execution surface. It does not invent commands, replace primary navigation, or waive confirmation/permission rules attached to actions.

## Decision Boundary
Start from the canonical action registry. Every palette result must map to a real action, destination or object operation with stable identity. Do not create palette-only verbs whose labels or consequences diverge from menus, buttons or shortcuts. The palette may offer aliases and synonyms for discovery, but the selected command still resolves to canonical semantics.

Decide search domains explicitly: global commands, current-context commands, navigation targets, recent objects, settings, or multi-step command arguments. Mixing all domains without grouping can make ranking opaque. Context-sensitive commands should explain scope (“Archive selected 3 messages”) rather than presenting the same generic label everywhere.

Keyboard flow is central. Opening focus should land in the query field; arrow navigation explores results; Enter executes or advances into argument mode; Escape backs out of nested command states before dismissing the palette. Focus returns to a sensible origin after dismissal. Pointer operation remains possible, but keyboard speed should not be degraded by hover-only affordances.

Ranking must be understandable enough not to surprise. Exact/prefix matches, aliases, recency, frequency and context can contribute, but dangerous commands should not climb solely because they are frequently used. Destructive or high-impact actions keep their downstream confirmation gates.

## Failure Topology
- Palette invents alternative action names and users cannot map results to visible UI.
- Search ranking changes unpredictably as telemetry learns, harming muscle memory.
- A destructive command executes immediately because “command palettes are for experts.”
- Nested argument mode has no clear way back.
- Results include disabled/inapplicable commands with no explanation.
- Opening the palette destroys the user’s current selection/context, so contextual commands act on the wrong object.

## Falsification and Recovery
Test zero query, ambiguous synonyms, disabled permissions, no results, nested commands, rapid typing, IME input, screen reader, keyboard-only, destructive actions and context changes while open. The design fails if the same command has materially different semantics outside the palette or if a user cannot predict what Enter will do.

Recover by binding results to canonical action IDs, making search domains explicit, stabilizing ranking, adding argument breadcrumbs and delegating consequences to existing confirmation/permission owners.

## Output Contract
Return `command-palette-contract` with invocation paths, searchable domains, canonical action bindings, query/ranking policy, result grouping, keyboard/focus model, nested argument states, dangerous-action handoff, empty/error states and verification cases.