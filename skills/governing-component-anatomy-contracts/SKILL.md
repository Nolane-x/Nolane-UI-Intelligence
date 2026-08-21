---
name: governing-component-anatomy-contracts
description: Use when component internals expose semantic parts to styling, composition, testing, accessibility, or tooling and those part identities must remain stable enough to be a contract.
---

# Governing Component Anatomy Contracts

## Anatomy as API
When consumers can target `root`, `label`, `trigger`, `viewport`, `thumb`, or similar parts, internal structure is no longer purely private. This skill owns which semantic parts are public, what each part means, which states they expose, and how anatomy may evolve without accidental breakage.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent chooses component boundaries and overall API philosophy. This specialist governs named internal parts once they are intentionally consumable.

## Part Identity
Define anatomy by semantic role, not current DOM depth. A `trigger` stays the trigger if wrappers change. Each part declares cardinality, ownership, accessibility relationship, state exposure, and whether consumers may style, query, or compose it. Avoid publishing decorative implementation nodes as stable parts.

## Change Classification
An internal refactor is compatible when public part identity and obligations remain. Renaming/removing a part, changing one-to-many cardinality, moving state attributes to a different part, or changing its semantic role is contract-affecting even if screenshots look identical.

## Evidence Protocol
Evidence includes part inventories, rendered tree snapshots at structural—not pixel—level, selector/test probes for each public part, and compatibility fixtures for consumer customizations. Test multiple states because anatomy may materialize differently when open, disabled, loading, virtualized, or portal-mounted.

## Failure Modes
Characteristic Failure includes tests reaching private descendants, styling hooks tied to wrapper order, a “label” part that sometimes stops labeling the control, duplicate part names with ambiguous identity, and major internal rewrites shipped as non-breaking despite consumer part contracts.

## Falsification
Falsification wraps/reorders private nodes while holding public anatomy constant, then tests consumer selectors and semantics. Also force conditional states that add/remove internals. If a documented part disappears, changes role, or requires undocumented DOM assumptions, the anatomy contract fails.

## Recovery
Recovery restores semantic part identity or versions the anatomy change. Move consumer hooks from structural selectors to named parts. If a published part was accidental, deprecate it with migration evidence rather than declaring it private retroactively.

## Output
Output: `component-anatomy-contracts-contract`, listing public parts, meanings, cardinality, state exposure, compatibility rules, and evidence probes.

## Handoff
Handoff what content may be inserted into named regions to slot-contract governance; handoff component boundary redesign to the parent.

## Sibling Boundary and delete-the-skill
Slot contracts govern insertion authority and allowed children; anatomy contracts govern stable semantic identity even when no consumer inserts content. The delete-the-skill test leaves public part evolution and structural compatibility unowned.