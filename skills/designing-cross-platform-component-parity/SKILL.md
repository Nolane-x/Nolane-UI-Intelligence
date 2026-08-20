---
name: designing-cross-platform-component-parity
description: Define parity across web, iOS, Android, desktop, and other platforms by shared user intent and guarantees rather than pixel or API identity.
---

# Designing cross-platform component parity

Parity does not mean forcing every platform to render or expose the same API. Use this skill when a design system spans multiple platforms and teams need a precise contract for what must remain equivalent and what may adapt to native conventions.

## Decision ownership

Own parity dimensions, allowed platform divergence, shared semantic states, accessibility guarantees, naming correspondence, and evidence required before one implementation is considered equivalent to another. Decide whether a divergence is native adaptation, capability gap, or product inconsistency.

## Inputs and evidence

Collect platform component APIs, rendered states, native HIG conventions, input modalities, accessibility trees, keyboard/gesture behavior, typography metrics, tokens, analytics semantics, and product workflows. Map platform limitations such as hover absence, back-navigation conventions, or system picker ownership.

## Procedure

Define a platform-independent semantic contract first: purpose, states, actions, error behavior, selection model, and accessibility outcomes. Then document platform realizations. Preserve intent and user-observable guarantees while allowing native controls, spacing, motion, or navigation behavior where appropriate.

Maintain an explicit divergence ledger with rationale and expiry/review conditions for temporary gaps. Avoid sharing implementation abstractions when they erase platform affordances.

Test equivalent tasks, not screenshots alone. A date picker may be visually unrelated across platforms yet fully parity-compliant if selection, constraints, errors, and accessibility are equivalent.

## Failure topology

Pixel parity can create alien interfaces and accessibility regressions on native platforms. API parity can produce lowest-common-denominator abstractions. The opposite failure is unchecked divergence, where similarly named components behave differently enough to confuse users and product teams.

Temporary platform gaps often become permanent when they are not tracked as explicit debt.

## Falsification

Run the same user goals across platforms and compare state transitions and outcomes. Audit semantics at unsupported or edge states, not only default appearance. Ask platform specialists to identify where the shared contract conflicts with native expectations. If product logic must branch on undocumented platform quirks, parity documentation is incomplete.

Review the divergence ledger against current platform capabilities periodically.

## Output contract

Produce a `cross-platform-component-parity-contract` containing shared semantic guarantees, per-platform realizations, allowed divergences, accessibility and input expectations, naming/API mappings, gap ownership, parity test scenarios, and evidence for each intentional exception.

## Handoffs

Use `designing-component-api-governance` for platform-specific API design, `designing-multi-brand-theming` for identity differences, `designing-design-system-versioning` for coordinated releases, and platform-specific UI skills when native mechanics require deeper treatment.