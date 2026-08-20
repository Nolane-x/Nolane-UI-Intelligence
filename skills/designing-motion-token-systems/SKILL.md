---
name: designing-motion-token-systems
description: Define motion tokens that encode temporal intent and transition roles instead of reducing animation to reusable duration numbers.
---

# Designing motion token systems

Motion tokens should make temporal decisions legible and consistent without flattening every interaction into the same easing and duration. Use this skill when a design system needs shared motion primitives across components, platforms, and reduced-motion variants.

## Decision ownership

Own the taxonomy for durations, easing curves, springs, delays, choreography offsets, and semantic transition roles. Decide which motion properties are primitives and which are semantic aliases, how reduced-motion alternatives map, and when a component may diverge from a shared token.

This skill does not design the complete animation behavior of a particular component; it provides the temporal vocabulary that behavior consumes.

## Inputs and evidence

Collect existing animations, measured durations, easing definitions, platform-native motion conventions, interruption behavior, reduced-motion states, performance traces, and qualitative intent such as enter, exit, confirm, relocate, or reveal. Identify repeated numeric values that represent different meanings and different values that actually serve one temporal role.

Record whether transitions are interruptible and whether duration scales with travel distance or content complexity.

## Procedure

Separate low-level primitives from semantic roles. A cubic curve or spring can be primitive; `motion.enter.emphasized` should communicate why it exists. Avoid a single global “fast/medium/slow” scale when spatial movement, opacity feedback, and system transitions have different perceptual requirements.

Define relationships between enter and exit, local feedback and navigational change, and continuous gesture motion versus discrete animation. Include reduced-motion mapping at the semantic level so components do not invent their own fallback. Specify platform substitutions where the same intent uses native motion APIs differently.

Validate tokens in real compositions, not isolated demos. Choreography can make individually correct durations feel sluggish when stacked.

## Failure topology

A numeric-only token set encourages cargo-cult reuse: everything becomes `duration-200`. Overly semantic sets can explode into component-specific names and stop being reusable. Another failure is tokenizing animation while ignoring interruption, velocity continuity, and reduced-motion equivalence, leaving the most important behavioral properties outside the system.

Motion tokens can also encode brand flourish that harms task speed when applied to high-frequency controls.

## Falsification

Replace a token in several consumers and verify they still share intent, not merely a value. Test enter/exit pairs under rapid interruption and inspect whether temporal relationships hold. Enable reduced motion and ensure semantic outcomes remain legible without relying on suppressed transforms.

Add a new interaction category and see whether existing roles describe it cleanly. Repeated component-specific exceptions indicate the taxonomy is too coarse or too prescriptive.

## Output contract

Produce a `motion-token-systems-contract` defining primitive and semantic layers, temporal roles, easing/spring policy, distance or velocity scaling, interruption assumptions, reduced-motion mappings, platform substitutions, exception criteria, and representative component evidence.

## Handoffs

Use `designing-motion-timing-and-easing` for detailed temporal curves, `designing-interruptible-motion` for interruption mechanics, `designing-reduced-motion` for accessibility behavior, and `designing-component-token-scopes` for component-local temporal decisions.