---
name: designing-responsive-priority-collapse
description: Collapse lower-priority information and actions under space pressure without hiding critical affordances, state, or recoverable context.
---

# Designing responsive priority collapse

When everything cannot remain visible, the interface must express priority intentionally. Use this skill for deciding what stays, wraps, moves into overflow, summarizes, or disappears as available space decreases.

## Decision ownership

Own the priority model, collapse sequence, alternate representations, discoverability obligations, and rules for preserving active or exceptional state. Decide which elements may be removed visually versus deferred behind an explicit control.

## Inputs and evidence

Collect task frequency, action criticality, user roles, active-state indicators, error/warning importance, usage telemetry, support cases, and narrow-layout observations. Identify supposedly “secondary” controls that become essential only in rare but high-impact situations.

## Procedure

Rank elements by task necessity, consequence, and context rather than raw click frequency. Define a deterministic collapse order and alternative home for hidden controls. Preserve currently active filters, selections, or warnings even if their normal priority is low; active state changes relevance.

Use summary indicators when detailed content moves behind disclosure so users know meaningful state exists. Avoid collapsing several unrelated controls into an unlabeled generic menu if their discoverability matters.

Ensure keyboard and assistive technology can reach collapsed content predictably.

## Failure topology

Frequency-only prioritization hides rare safety or recovery actions. Collapsed filters can remain active invisibly, making data appear wrong. Overflow menus can become junk drawers whose organization differs at every width.

Another failure is non-deterministic collapse caused by measurement races, making controls move unexpectedly as fonts or asynchronous data load.

## Falsification

Test narrow states with active errors, filters, permissions, and long labels. Ask users to locate actions that moved into overflow. Resize repeatedly and verify control identity and state remain stable. Introduce late-loading badges or banners and confirm the collapse order remains deterministic.

Audit whether any hidden state continues to affect results without a visible summary.

## Output contract

Produce a `responsive-priority-collapse-contract` with priority rationale, collapse sequence, per-element alternate representation, active/exception state overrides, overflow organization, discoverability evidence, and state-preservation tests.

## Handoffs

Use `designing-responsive-toolbar-overflow` for toolbars, `designing-responsive-navigation-transitions` for nav items, `designing-responsive-table-transformations` for tabular data, and `engineering-responsive-composition` for whole-page hierarchy.