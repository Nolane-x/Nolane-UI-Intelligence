---
name: auditing-ui-library-integration
description: Use when external UI code, a component library, motion engine, editor, canvas SDK, charting system, primitive or copied implementation is about to ship and an independent critic must test legal, semantic, accessibility, rendering, performance, lifecycle and local-behavior risks.
---

# Auditing UI Library Integration

## Parent Contract
**Required parent:** `selecting-ui-building-blocks`.

Receive the approved source selection, reference ledger, adaptation contract where applicable, exact package/source version or copied revision, local wrapper/component implementation, dependency graph, product obligations and runtime claims. The selection itself is not evidence that integration succeeded.

## Decision Boundary
This is an **independent integration critic**. It can block an otherwise attractive component. It owns the question: *did external leverage survive contact with this product without violating rights, semantics, accessibility, rendering integrity, performance, maintainability or exit assumptions?* It does not redesign the component while auditing and it cannot waive a failure because the upstream source is reputable.

The audit is source-specific and local. “Radix handles accessibility” is not an audit result. “Local `ProjectDeleteDialog` composed Radix Dialog, preserved labelled title/description, trapped and returned focus in keyboard and screen-reader probes, and passed the project's destructive confirmation flow” is evidence.

## Product Truth
Integration defects live between systems. Upstream and local code can each be correct alone while their composition fails. A wrapper removes an ARIA label. A CSS reset hides focus. A portal crosses a shadow root. A motion presence wrapper unmounts a dialog before focus return. A Next.js boundary causes hydration mismatch. A second copy of a package creates context identity problems. A library update changes markup and invalidates selectors. A license permits application use but not redistribution in a component kit. A large editor becomes impossible to replace because product data shape leaks its schema everywhere.

AI-generated code is especially vulnerable because agents see the happy-path example and omit lifecycle boundaries. The audit exists to make those hidden costs visible before release.

## Decision Model
1. **Pin what was integrated.** Record source, version/commit where available, installation/copy mode, local wrapper path and material modifications. A moving `latest` URL is not enough for reproducibility.
2. **Audit license and distribution context.** Re-read current primary terms when material. Verify intended deployment, redistribution, attribution, trademarks/assets, hosted-service terms and production keys where relevant. A prior registry classification cannot substitute for this release check on high-drift or restricted sources.
3. **Audit dependency shape.** Identify new direct/transitive dependencies, duplicate engines, peer requirements, providers, CSS/global side effects, native modules, server/client boundaries and package update policy. Check whether the source pulled more architecture than the selected capability justified.
4. **Audit semantic ownership.** Confirm canonical actions, labels, roles, state and consequences remain local-product truth. Remove demo actions and undocumented shortcuts. Verify external state does not diverge from product state.
5. **Audit accessibility locally.** Test keyboard, focus order, focus containment/return, accessible names, screen-reader relationships, pointer alternatives, high contrast, zoom/text scaling and reduced motion as required. Upstream claims are background evidence only.
6. **Audit motion safety.** Verify reduced-motion behavior, looping/auto-play policy, photosensitivity risk where relevant, interruption and information equivalence. External effects cannot override the project's motion-safety contract.
7. **Audit SSR/hydration/rendering lifecycle.** Test server markup stability, browser-only APIs, layout measurement timing, portals, Suspense/transitions, resize and cleanup. For canvas/WebGL/editor SDKs, include resource disposal and initialization failure.
8. **Audit performance.** Measure the real composition: initial and route-level load, runtime frames, main-thread work, memory, network/assets, large-data behavior and low-end fallback. Do not use upstream bundle claims for a local tree containing different plugins.
9. **Audit API drift and maintenance.** Record source freshness, upgrade surface, deprecated APIs, pinned/semver strategy and tests likely to catch upstream breakage. High-drift sources require a revalidation trigger.
10. **Audit security and trust boundary.** Inspect HTML rendering, plugin execution, remote assets, user content, editor extensions, canvas import/export, unsafe evaluation and external network calls appropriate to the source role.
11. **Audit exit strategy.** Confirm adapter/component boundaries match dependency depth. Name what must change to replace the source and where upstream-specific types leak into the application. If deliberate lock-in is accepted, record the authorized reason.
12. **Demand local runtime proof.** Material behavioral claims go to `verifying-runtime-ui-behavior`. Passing upstream examples or unit tests does not close this item.

## Evidence
Evidence includes primary license/terms, package lock or exact copied revision, dependency diff, local source paths, accessibility-tree and keyboard traces, reduced-motion screenshots/video, server/client console traces, performance profiles, runtime probes, build output and upgrade tests. Each PASS needs an evidence reference. `N/A` is allowed only with a reason proving the dimension is genuinely inapplicable.

Audit findings should state consequence and remediation boundary. “Hydration risk” is weak; “MorphingDialog reads layout before client hydration, producing different initial DOM; move measurement behind client effect or render a stable non-morphing server state” is actionable.

## Output Contract
Return `ui-integration-audit` with:
- `source_revision`
- `local_integration_paths[]`
- `checks {license, dependency, accessibility, reduced_motion, ssr_hydration, performance, api_drift, security, exit_strategy, local_runtime}` where each is `{status: PASS|FAIL|UNKNOWN|N/A, evidence[], findings[]}`
- `dependency_delta`
- `upstream_specific_leaks[]`
- `runtime_probe_refs[]`
- `blocking_findings[]`
- `accepted_residual_risks[]`
- `revalidation_triggers[]`
- `decision: PASS|BLOCKED|UNKNOWN`

A release PASS requires every applicable check to be evidence-backed PASS and no blocking finding.

## Failure Traps
- Copying the license name from registry memory without checking current terms for a material release.
- Treating upstream accessibility tests as local proof.
- Auditing source code but not the wrapper/composition that actually ships.
- Ignoring hydration because the client eventually “looks correct.”
- Ignoring dependency duplication because tree shaking might remove it.
- Measuring a component alone instead of inside realistic screen density/data volume.
- Forgetting cleanup of observers, event listeners, timelines, editor instances or WebGL resources.
- Passing reduced motion because animations are merely shorter.
- Accepting a core SDK with no replacement boundary because migration is “unlikely.”
- Allowing a visual effect to introduce unsafe HTML or remote asset behavior without review.
- Using `N/A` to avoid producing evidence.
- Fixing findings while auditing and then marking the same evidence PASS without a new revision/probe.

**Hard gate:** external UI integration has no release authority until license, dependency, accessibility, reduced motion, rendering lifecycle, performance, API drift, security, exit strategy and local runtime obligations are explicitly resolved or legitimately N/A with evidence.

## V6 Library Integration Audit
Inventory the full **dependency-surface inventory**: direct/transitive packages, CSS/global reset, fonts/assets, portals, event listeners, context/providers, SSR/hydration assumptions, workers/WASM, network calls, and runtime polyfills. Perform a **bundled-global-style audit** for selectors, variables, resets, stacking contexts, animation defaults, and theming hooks that can contaminate unrelated surfaces.

Search for **runtime-semantic regression** after composition: focus order, accessible names, disabled semantics, form submission, history, keyboard behavior, reduced motion, and responsive state can differ from the upstream demo. Conduct an **upstream-update rehearsal** using a representative version bump/changed API and inspect whether the local boundary contains breakage. Evaluate **removal feasibility**: what data/API/DOM assumptions must change if the library is removed or replaced?

### Falsification
Temporarily remove provider/global CSS, change version, and execute the critical states. Hidden coupling or semantic drift falsifies “clean integration.”

### Recovery
Wrap/normalize the library, move globals behind scope, pin version, add migration tests, or reject the integration when replacement cost or semantic leakage is too high.
