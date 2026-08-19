---
name: designing-policy-inheritance
description: Use when configuration or authorization values flow through organization, workspace, group, resource or user scopes and the interface must expose effective value, origin, override, lock and precedence.
---

# Designing Policy Inheritance

## Parent Contract
**Required parent:** `designing-permissions-and-consent`.

This faculty owns user-facing reasoning about inherited policy and effective values. It does not define the enterprise policy engine or settings persistence architecture in general.

## Decision Boundary
For every inheritable policy, distinguish **effective value** from **local value** and **source/origin**. A local field showing `Enabled` is incomplete if the value is inherited from Organization and locked; similarly, an empty local value may mean “inherit,” not “off.”

Render the precedence path in the language of the product: Organization → Workspace → Project → Resource, or whatever hierarchy actually exists. Do not assume deeper scope always wins; explicit denies, locks, compliance policies or condition-based rules may override differently. The UI must reflect the backend’s authoritative resolution algorithm rather than a generic cascade metaphor.

Allow override only where permitted. Before creating an override, show what changes and what source it will shadow. “Reset” should usually mean remove local override and return to inherited behavior, not set a hard-coded default. If the upstream source changes later, inherited values update while explicit overrides remain stable according to policy.

When multiple sources contribute, expose conflict/resolution rather than displaying one value with no explanation. Audit views should preserve historical policy source/version because current hierarchy may differ from what governed a past action.

## Failure Topology
- Toggle looks editable although organization policy locks it.
- Reset sets `false` instead of removing the override, so future organization changes never flow through.
- UI says “Inherited” but cannot show from where.
- Direct user grant and group deny conflict; interface chooses one based on visual nesting rather than engine precedence.
- Moving a resource to another workspace silently changes effective policy with no preview.
- Audit history resolves old events using today’s policy tree.

## Falsification and Recovery
Falsify with upstream changes, local override/reset, locked policy, resource move, multiple conflicting sources and historical inspection. Compare displayed effective value/origin to authoritative policy resolution.

Recover by modeling local/effective/source separately, exposing exact precedence, making reset remove overrides, previewing scope moves and preserving policy snapshot references for historical events.

## Output Contract
Return `policy-inheritance-contract` with scope hierarchy, local/effective/source state, precedence authority, lock/override/reset semantics, conflict resolution presentation, move/reparent impact, historical provenance and resolution-parity tests.