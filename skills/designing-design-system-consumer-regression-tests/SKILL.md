---
name: designing-design-system-consumer-regression-tests
description: Use when a design-system primitive, token, component, or package change can break downstream applications and verification must prove consumer behavior across representative integration patterns rather than only the design-system repository itself.
---

# Designing Design-System Consumer Regression Tests

## Consumer reality is part of the contract
A design-system package can pass all of its own tests and still break real products through composition, CSS order, token overrides, wrapper components, bundlers, server rendering, theme layering, or version skew. This skill owns the evidence strategy for validating changes against representative downstream consumer contexts.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent governs evidence lineage. This specialist begins when the verification claim is not “the component works in isolation” but “this system change remains safe for consuming applications.”

## Consumer archetypes
Select archetypes by integration mechanism and risk: direct primitive use, wrapped components, token override/theme extension, CSS-in-JS or static CSS consumption, SSR/hydration, mixed-version microfrontends, framework adapter, embedded WebView, or application-specific composition. The decision owner is the smallest set that captures distinct integration failure classes.

Do not choose consumers merely because they are famous or easy to test. A small internal app may be the strongest canary if it exercises deep overrides or legacy wrappers. Record why each consumer exists in the suite and which contract it represents.

## Regression contract
For each archetype, bind package versions, integration pattern, product fixture, critical flows, expected visual/semantic invariants, and upgrade path. Test both clean install and realistic upgrade where migrations matter. A design-system change that works in a fresh sandbox can still fail when old tokens, deprecated props, or cached CSS coexist during rollout.

Include negative evidence for breaking changes: prove that an intentionally removed API fails in the documented way and that the migration path restores function. This makes deprecation behavior testable instead of purely narrative.

## Evidence
Strong evidence includes consumer lockfiles or version manifests, rendered state fixtures, interaction traces, build/bundle diagnostics, hydration/console output, and before/after upgrade artifacts. When a regression depends on CSS order or bundling, capture those mechanisms rather than only the resulting screenshot.

## Failure modes
Characteristic Failure includes testing only Storybook, one pristine example app, consumers all using identical integration style, skipped upgrade-path testing, and baselines updated in every consumer without identifying a shared breaking cause. Another failure is accidental scope creep: consumer tests become full end-to-end suites unrelated to design-system contracts and are eventually too slow to protect releases.

## Falsification
Change a token name, component slot, CSS layer order, package export, hydration behavior, and deprecated prop handling. Run against wrapped and direct consumers. The contract fails if a materially distinct integration pattern has no representative, if a known breaking change passes unnoticed, or if a consumer failure cannot be traced back to the system contract that changed.

## Recovery
When a consumer breaks, classify whether the design system violated compatibility, the consumer relied on undocumented behavior, or migration evidence is incomplete. Fix the owning contract, add the minimal regression case, and preserve the failure as a named consumer archetype if it reveals a distinct mechanism. Avoid permanently adding whole applications when a smaller fixture captures the same risk.

## Output and Handoff
Output: `design-system-consumer-regression-tests-contract`, containing consumer archetypes, integration mechanisms, version pins, critical contract cases, upgrade tests, and evidence artifacts. Handoff component-state coverage to state evidence matrices and baseline imagery to visual-regression baselines.

## Sibling Boundary and delete-the-skill
Sibling story-state fixtures validate isolated component states; this skill validates package behavior inside downstream integration environments. Cross-platform component parity governs semantic parity across platform implementations, not consumer breakage from package evolution. The delete-the-skill test passes because without consumer evidence, design-system verification stops at the repository boundary and misses integration regressions that users actually encounter.