---
name: designing-responsive-density-shifts
description: Change interface density under spatial pressure without conflating compactness with reduced accessibility, information removal, or arbitrary scaling.
---

# Designing responsive density shifts

A layout may need comfortable spacing on touch surfaces and denser presentation in constrained desktop regions, but density should not twitch at every resize. Use this skill when responsive state changes include coordinated spacing and control-size shifts.

## Decision ownership

Own when responsive constraints may select a different density level, which metrics change, how input modality influences the choice, and what user-selected density preferences override. Decide whether density changes globally, regionally, or only within specific high-throughput components.

## Inputs and evidence

Collect supported density tokens, pointer/touch modality, user settings, minimum targets, content pressure, viewport/container size, text scaling, and task throughput. Inspect layouts where compact mode merely hides whitespace versus those where it genuinely improves information access.

## Procedure

Bind responsive shifts to named density modes rather than ad hoc pixel overrides. Establish precedence among user preference, modality safety, platform conventions, and spatial pressure. A user-selected comfortable mode should not silently become compact just because a sidebar narrows unless the product explicitly defines that behavior.

Preserve hit targets and focus indicators even when visual density tightens. Coordinate typography and icon alignment with spacing changes so components do not look mechanically shrunk.

Use hysteresis or sufficiently separated thresholds to prevent repeated density toggling around a boundary.

## Failure topology

Automatic compaction can violate touch-target requirements on hybrid devices. Density changes that reflow data heavily may move the user’s point of attention. Another failure is partial density: container padding changes but child control metrics do not, creating uneven rhythm.

Preference conflicts are especially harmful when the interface overrides an explicit user accessibility choice.

## Falsification

Test mouse, touch, stylus, hybrid input, explicit density preferences, zoom, and resize around thresholds. Measure target dimensions and focus visibility in every state. Resize while interacting with dense tables or trees and verify row identity and selection remain stable.

If responsive density requires component-specific numeric patches, the token system or ownership model is incomplete.

## Output contract

Produce a `responsive-density-shifts-contract` defining triggers, precedence, supported density transitions, invariants, user-preference handling, modality safeguards, anti-jitter behavior, and representative component tests across responsive states.

## Handoffs

Use `designing-density-token-systems` for density definitions, `designing-content-driven-breakpoints` for thresholds, `designing-touch-targets` for target constraints, and `verifying-responsive-state-parity` for behavioral checks.