# UI Industry 1000 — Batch 006 Research, Provenance, and Ownership Ledger

## Status and non-generation rule

Batch 006 starts from the 774-node canonical graph and admits exactly 100 independently owned specialists, producing the 874-node graph. The 100 count is a delivery constraint, never a license to create cosmetic siblings.

Canonical `SKILL.md` prose was authored independently. External systems are mechanism/domain evidence only; no third-party skill prose, demo composition, brand trade dress, or library-specific visual language is copied. Deterministic automation in this batch is limited to graph registration, count bookkeeping, validation, and this provenance index; it does not create or rewrite canonical skill bodies.

## Snapshot and source-role matrix

| Court | Primary snapshot / authority | Secondary evidence | Transfer boundary |
|---|---|---|---|
| design-system-governance | `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f` | openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26 | Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. |
| adaptive-composition | `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7` | openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26 | Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. |
| typography-engineering | `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7` | W3C CSS Fonts/Text specifications (normative web standards, live authority) | Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. |
| agentic-execution | `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b` | CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted) | Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. |
| ui-evidence | `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a` | dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence | Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. |
| game-ten-foot | `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce` | Qt/Qt Quick control/focus mechanisms (corroboration) | Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. |
| automotive-hmi | `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)` | godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only | Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. |
| multi-surface-continuity | `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2` | expo/expo@5a97a546476fd0bea35227b60297ad472f065168 | Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. |

## Admission rules

Every owner below survived parent/sibling review and the delete-the-skill test. If removing a candidate leaves no material decision or failure class unowned, that candidate is not canonical. Repository popularity is never authority, and source implementation details are not generalized beyond the mechanism they evidence.

## Exact ownership ledger

### `governing-token-resolution-contexts`
Parent: `architecting-design-tokens`
Trigger: Use when one token graph can resolve to different concrete values across themes, modes, brands, platforms, density regimes, or runtime environments and the precedence must remain deterministic.
Decision owned: This skill owns the decision model that turns those inputs into one deterministic resolved value.
Sibling exclusion: Sibling token-reference integrity owns graph validity, not contextual precedence.
Failure class: Characteristic Failure includes shadowed candidates that can never win, contradictory precedence across platforms, silent fallback to a primitive token, context keys with different normalization rules, and circular environment dependence.
Falsifier: Falsification should vary one context dimension at a time, permute candidate declaration order, remove the expected winner, and replay the same input in independent consumers.
Output: `token-resolution-contexts-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Sibling token-reference integrity owns graph validity, not contextual precedence.

### `governing-token-reference-integrity`
Parent: `architecting-design-tokens`
Trigger: Use when design tokens alias or reference other tokens and the reference graph must remain acyclic where required, resolvable, stable under rename, and diagnosable across packages.
Decision owned: This skill owns the graph-integrity decisions: what constitutes a legal edge, when cycles are invalid, how dangling references are reported, and how identities survive moves or renames.
Sibling exclusion: Sibling resolution-context governance decides among valid contextual candidates; this skill decides whether the reference chain itself is valid.
Failure class: Failure includes dangling aliases that resolve to null, self-reference hidden inside composites, long cycles crossing package boundaries, same-name accidental capture after import, and refactors that preserve final color in one theme while changing semantic ancestry.
Falsifier: Falsification deletes or renames a referenced target, introduces a synthetic cycle, reorders package imports, and resolves every inbound alias.
Output: `token-reference-integrity-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Sibling resolution-context governance decides among valid contextual candidates; this skill decides whether the reference chain itself is valid.

### `governing-token-type-conformance`
Parent: `architecting-design-tokens`
Trigger: Use when token producers and consumers must agree on value types, composite shapes, units, and coercion rules so interchange does not silently change semantics.
Decision owned: This skill owns type conformance across authoring, storage, transformation, and consumption: declared type, inferred type, unit domain, composite field shape, and whether coercion is legal.
Sibling exclusion: Reference integrity proves a target exists; it does not prove the target's type is compatible.
Failure class: Failure includes a duration interpreted as a length, color channels clamped without notice, shadow composites losing spread, dimension aliases crossing incompatible units, font-weight strings coerced differently, or a token whose declared type no longer matches its referenced target after refactoring.
Falsifier: Falsification sends boundary values through every supported transform, changes a referenced token to an incompatible type, removes optional composite fields, and round-trips values through at least two consumers.
Output: `token-type-conformance-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Reference integrity proves a target exists; it does not prove the target's type is compatible.

### `governing-token-extension-boundaries`
Parent: `architecting-design-tokens`
Trigger: Use when a token format permits vendor or tool-specific extensions and portability must be preserved without pretending proprietary metadata is universally understood.
Decision owned: This skill owns which information may live in extensions, how namespaces are versioned, and what happens when an extension is unavailable.
Sibling exclusion: Type conformance validates known value shapes; it cannot govern unknown vendor namespaces.
Failure class: Failure appears as a theme that only works in one design tool, a proprietary gradient/shadow definition with no canonical fallback, an exporter that discards unknown metadata, namespace collisions, or an extension version change that silently alters interpretation.
Falsifier: Falsification removes each extension namespace in isolation, feeds a future/unknown version to current consumers, and round-trips through an extension-unaware tool.
Output: `token-extension-boundaries-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Type conformance validates known value shapes; it cannot govern unknown vendor namespaces.

### `governing-token-mode-inheritance`
Parent: `architecting-design-tokens`
Trigger: Use when token modes or themes inherit from one another and override behavior, missing values, ancestry, and shadowing must remain explicit and deterministic.
Decision owned: This skill owns those semantics.
Sibling exclusion: Resolution-context governance selects among context-qualified candidates, whereas this skill governs a declared inheritance relation between mode sets.
Failure class: Failure includes a dark mode that inherits an obsolete base value after refactor, cyclic mode ancestry, override shadowing that hides parent security/contrast updates, null treated as “inherit” in one tool and “clear” in another, and multiple inheritance whose winner depends on serialization order.
Falsifier: Falsification changes a base token and predicts which descendants should update; removes a child override; inserts an explicit clear; and permutes multiple-parent declaration order.
Output: `token-mode-inheritance-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Resolution-context governance selects among context-qualified candidates, whereas this skill governs a declared inheritance relation between mode sets.

### `governing-semantic-token-layering`
Parent: `architecting-design-tokens`
Trigger: Use when primitive, semantic, component, and product-local tokens form dependency layers and leakage between layers would couple consumers to implementation detail.
Decision owned: This skill owns the dependency boundaries among primitive, semantic, component, and product-local layers.
Sibling exclusion: Type conformance proves values are compatible; reference integrity proves edges are valid.
Failure class: Failure includes components reading raw palette indexes, semantic aliases named after current colors, primitives referencing component state, component tokens reused globally because they are convenient, and migrations that merge distinct meanings because their current values happen to match.
Falsifier: Falsification changes primitive values, separates previously equal values, and searches for consumers whose intended meaning changes unexpectedly.
Output: `semantic-token-layering-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Type conformance proves values are compatible; reference integrity proves edges are valid.

### `auditing-token-migration-impact`
Parent: `architecting-design-tokens`
Trigger: Use when replacing, renaming, splitting, merging, or revaluing tokens and the actual consumer and rendered-state blast radius must be known before migration is accepted.
Decision owned: This skill owns the pre-change and post-change impact audit; it does not own the lifecycle policy that decides when an old token is deprecated.
Sibling exclusion: Handoff lifecycle timing to token deprecation governance and implementation sequencing to design-system adoption migration.
Failure class: Failure includes hidden consumers using generated aliases, unexpected mode inheritance, a renamed token accidentally captured from another namespace, visually silent semantic merges, and broad snapshot churn with no classification.
Falsifier: Falsification selects predicted-unchanged controls and verifies they remain unchanged; samples indirect consumers; and reverses the migration in a test branch to see whether attributed diffs disappear.
Output: `token-migration-impact-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Handoff lifecycle timing to token deprecation governance and implementation sequencing to design-system adoption migration.

### `governing-token-deprecation-lifecycles`
Parent: `architecting-design-tokens`
Trigger: Use when an obsolete design token needs a replacement path, warning interval, consumer migration signal, and defensible removal gate without indefinite compatibility debt.
Decision owned: --- # Governing Token Deprecation Lifecycles ## Lifecycle Purpose Deprecation is a state machine, not a comment that says “old.” This skill owns the transition from supported token to deprecated token to removed token, including replacement mapping, warning behavior, deadlines, exceptions, and proof that removal will not orphan consumers.
Sibling exclusion: Handoff blast-radius discovery to token migration impact auditing and coordinated product rollout to design-system breaking-change rollout.
Failure class: Failure includes permanent deprecation with no removal criteria, removal while generated consumers still reference the token, automatic replacement that changes meaning, warnings that cannot identify call sites, and a token resurrected by an old package after apparent cleanup.
Falsifier: Falsification installs a supported old consumer against the proposed removal, scans generated outputs, exercises non-default modes, and checks that warnings lead to a valid migration path.
Output: `token-deprecation-lifecycles-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Remove this skill and token architecture can still label something obsolete, but no owner remains for the temporal support/removal contract, warning interval, or evidence-bound removal gate.

### `governing-design-system-version-compatibility`
Parent: `architecting-component-systems`
Trigger: Use when design-system producers and consumers evolve independently and support guarantees, compatibility matrices, peer constraints, and mixed-version behavior must be explicit.
Decision owned: This skill owns the decision “which producer versions are supported with which consumer, runtime, framework, token schema, and companion package versions?” It separates support policy from the mechanics of migrating a particular application.
Sibling exclusion: Adoption migration owns movement between versions; breaking rollout owns release sequencing.
Failure class: Failure includes components rendering but losing focus behavior, new tokens consumed by old CSS, peer dependency ranges that install an untested combination, minor versions introducing state semantics old consumers cannot express, or documentation claiming support beyond tested matrix edges.
Falsifier: Falsification chooses boundary combinations—oldest supported consumer/newest producer and inverse where claimed—then exercises behavior, not just compilation.
Output: `design-system-version-compatibility-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Adoption migration owns movement between versions; breaking rollout owns release sequencing.

### `governing-component-anatomy-contracts`
Parent: `architecting-component-systems`
Trigger: Use when component internals expose semantic parts to styling, composition, testing, accessibility, or tooling and those part identities must remain stable enough to be a contract.
Decision owned: This skill owns which semantic parts are public, what each part means, which states they expose, and how anatomy may evolve without accidental breakage.
Sibling exclusion: Slot contracts govern insertion authority and allowed children; anatomy contracts govern stable semantic identity even when no consumer inserts content.
Failure class: Characteristic Failure includes tests reaching private descendants, styling hooks tied to wrapper order, a “label” part that sometimes stops labeling the control, duplicate part names with ambiguous identity, and major internal rewrites shipped as non-breaking despite consumer part contracts.
Falsifier: Falsification wraps/reorders private nodes while holding public anatomy constant, then tests consumer selectors and semantics.
Output: `component-anatomy-contracts-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Slot contracts govern insertion authority and allowed children; anatomy contracts govern stable semantic identity even when no consumer inserts content.

### `governing-component-slot-contracts`
Parent: `architecting-component-systems`
Trigger: Use when a component exposes named insertion points and allowed content, cardinality, ordering, ownership, and invalid compositions need explicit enforcement.
Decision owned: This skill owns the content contract for each exposed insertion point.
Sibling exclusion: Anatomy says what a region is; this skill says what a consumer may put there and under which invariants.
Failure class: Failure includes two primary actions inserted into a single-primary slot, interactive content nested inside an interactive host, a title slot omitted while the host still advertises a labeled-dialog requirement, slot content stealing spacing authority, or reorderable slots producing incorrect reading order.
Falsifier: Falsification deliberately supplies boundary compositions: zero, one, many, wrong semantic type, very long content, conditional removal, and nested focusable content.
Output: `component-slot-contracts-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Anatomy says what a region is; this skill says what a consumer may put there and under which invariants.

### `governing-component-state-contracts`
Parent: `architecting-component-systems`
Trigger: Use when a reusable component has controlled, uncontrolled, transient, async, disabled, error, selection, or open states whose legal combinations and transitions must be part of its API contract.
Decision owned: This skill owns legal states, forbidden combinations, transition authority, controlled/uncontrolled boundaries, and externally observable state semantics for reusable components.
Sibling exclusion: Variant taxonomy decides which variation deserves API surface; it does not define runtime state legality.
Failure class: Failure includes impossible combinations rendered anyway, controlled components mutating internal state ahead of the owner, disabled state that can still commit actions, stale async completion overwriting newer state, and visual variants that imply a state different from the actual machine.
Falsifier: Falsification races state updates, denies a controlled transition, toggles disabled during pending work, resets while an operation is inflight, and replays events out of order.
Output: `component-state-contracts-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Variant taxonomy decides which variation deserves API surface; it does not define runtime state legality.

### `governing-component-variant-taxonomies`
Parent: `architecting-component-systems`
Trigger: Use when a component accumulates size, emphasis, intent, density, layout, platform, or stylistic options and the system must decide which differences deserve first-class variants instead of tokens or composition.
Decision owned: This skill owns the decision about which axes are legitimate component variants, which are semantic state, which belong in tokens, and which should be achieved through composition.
Sibling exclusion: State contracts can be correct while the public variant API is still incoherent.
Failure class: Failure includes `compact` and `small` overlapping, semantic danger encoded only as a color variant, platform names used as style presets, booleans that interact unpredictably, and variant values that exist for one page-specific exception.
Falsifier: Falsification removes a proposed variant and tries tokenization or composition; if no material semantic/behavioral decision is lost, the variant was unnecessary.
Output: `component-variant-taxonomies-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: State contracts can be correct while the public variant API is still incoherent.

### `governing-design-system-exceptions`
Parent: `architecting-component-systems`
Trigger: Use when a product team needs to violate or bypass a design-system rule and the exception requires explicit scope, rationale, risk, owner, expiry, and reintegration path.
Decision owned: This skill owns the governance state of a deliberate deviation: why it exists, which rule it bypasses, who can approve it, where it applies, how long it lives, and how it returns to the system.
Sibling exclusion: Contribution governance owns ordinary upstream change, not bounded deviation debt.
Failure class: Failure includes copy-pasted exceptions, permanent “temporary” overrides, exceptions with no owner, local forks that stop receiving fixes, and approvals that waive obligations the approver does not control.
Falsifier: Falsification searches for the exception's implementation signature outside its scope, removes the exception after an upstream capability lands, and checks whether the original need still exists.
Output: `design-system-exceptions-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Contribution governance owns ordinary upstream change, not bounded deviation debt.

### `governing-design-system-contribution-workflows`
Parent: `architecting-component-systems`
Trigger: Use when product teams propose reusable components, tokens, patterns, fixes, or documentation upstream and acceptance authority, evidence, review stages, and ownership transfer need governance.
Decision owned: This skill owns the path from local need to accepted shared-system capability: intake quality, evidence threshold, semantic review, technical review, accessibility review, decision authority, maintenance assignment, and release eligibility.
Sibling exclusion: Exceptions govern deviations; adoption migrations govern downstream consumption.
Failure class: Failure includes contribution queues with no decision owner, shared components accepted because they look reusable, local abstractions dumped upstream without consumer evidence, accessibility review after API freeze, and contributions merged without long-term maintainer assignment.
Falsifier: Falsification attempts to satisfy the need with existing primitives, tests a second consumer, and removes product-specific assumptions.
Output: `design-system-contribution-workflows-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Exceptions govern deviations; adoption migrations govern downstream consumption.

### `governing-cross-platform-component-parity`
Parent: `architecting-component-systems`
Trigger: Use when a design-system capability exists across web, iOS, Android, desktop, or other platforms and semantic parity must be distinguished from intentional platform-native divergence.
Decision owned: This skill owns which component semantics, states, actions, accessibility outcomes, and product obligations must remain equivalent across platforms, and which presentation or interaction details should intentionally follow platform convention.
Sibling exclusion: Version compatibility concerns producer/consumer revisions; this skill concerns simultaneous platform implementations.
Failure class: Failure includes visually matching components with different disabled semantics, one platform lacking an error state, action labels diverging in meaning, unsupported platform capability hidden behind a dead control, or lowest-common-denominator APIs that erase useful native behavior.
Falsifier: Falsification executes the same user intent on each platform, injects equivalent failure conditions, and compares observable outcome rather than gesture sequence.
Output: `cross-platform-component-parity-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Version compatibility concerns producer/consumer revisions; this skill concerns simultaneous platform implementations.

### `governing-design-system-adoption-migrations`
Parent: `architecting-component-systems`
Trigger: Use when a product or product fleet must move from legacy UI contracts to a newer design-system version and coexistence, sequencing, codemods, manual decisions, and completion evidence need control.
Decision owned: --- # Governing Design-System Adoption Migrations ## Migration Scope This skill owns the consumer-side transition from an old design-system contract to a new one.
Sibling exclusion: Migration impact auditing can predict a token change, but it does not govern fleet-wide component-system coexistence and cutover.
Failure class: Failure includes a codemod that changes syntax but not semantics, partial migration with duplicate global styles, new components wrapped in legacy spacing hacks, “100% migrated” based only on imports while generated CSS remains, and teams recreating removed APIs as local compatibility layers.
Falsifier: Falsification scans for legacy runtime artifacts after source migration, exercises mixed old/new boundaries, and samples conversions marked mechanical for semantic drift.
Output: `design-system-adoption-migrations-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Migration impact auditing can predict a token change, but it does not govern fleet-wide component-system coexistence and cutover.

### `governing-design-system-breaking-change-rollouts`
Parent: `architecting-component-systems`
Trigger: Use when a design-system change intentionally breaks prior consumer assumptions and release waves, opt-in windows, rollback, escape hatches, and cutover authority must be controlled.
Decision owned: This skill owns producer-side release sequencing, wave criteria, opt-in/opt-out rules, rollback windows, and the point at which old behavior stops being available.
Sibling exclusion: Version compatibility defines supported combinations; adoption migration executes consumer change.
Failure class: Failure includes a release train that advances by calendar despite unresolved regressions, rollback that restores package version but not migrated data/tokens, escape hatches with no expiry, consumer groups missed by telemetry, and forced cutover before critical consumers can migrate.
Falsifier: Falsification triggers a representative failure during pilot, rehearses rollback after partial consumer migration, and checks whether the old contract can be restored without hidden mixed state.
Output: `design-system-breaking-change-rollouts-contract`
Evidence role: Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative. Primary pin: `design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Version compatibility defines supported combinations; adoption migration executes consumer change.

### `designing-container-query-composition`
Parent: `adapting-responsive-layouts`
Trigger: Use when a reusable region must adapt to the space allocated by its containing layout rather than to the global viewport and container-local composition rules need explicit task-preserving behavior.
Decision owned: This skill owns the decision of how a region changes composition from measured container conditions while preserving its semantic task and avoiding hidden coupling to page-level breakpoints.
Sibling exclusion: Sibling content-pressure breakpoints determine when content actually fails; this skill determines the local container context that owns the transition.
Failure class: Characteristic Failure includes local widgets staying desktop-shaped inside narrow columns, nested query loops, thresholds chosen from phone/tablet labels, actions disappearing when a container shrinks, and source order that becomes nonsensical after grid rearrangement.
Falsifier: Falsification holds the viewport constant while resizing only the container, moves the component into a differently sized parent, injects long content near thresholds, and nests it under another querying component.
Output: `container-query-composition-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Sibling content-pressure breakpoints determine when content actually fails; this skill determines the local container context that owns the transition.

### `designing-content-pressure-breakpoints`
Parent: `adapting-responsive-layouts`
Trigger: Use when responsive thresholds should be derived from observed content or task failure rather than device categories and each breakpoint needs evidence tied to a real pressure condition.
Decision owned: This skill owns the evidence that locates those boundaries and the policy for selecting stable thresholds around them.
Sibling exclusion: Container queries answer *where* a local threshold is evaluated.
Failure class: A breakpoint is justified when the current composition stops satisfying an invariant: labels collide, comparison becomes impossible, line measure degrades, actions wrap into ambiguity, or critical context leaves the visible task.
Falsifier: Falsification substitutes worst-plausible content, changes font metrics, enables browser zoom/text scaling, and sweeps through threshold neighborhoods.
Output: `content-pressure-breakpoints-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Remove this owner and responsive layouts can still change at widths, but there is no faculty requiring those widths to correspond to actual content/task failure.

### `designing-region-priority-collapse`
Parent: `adapting-responsive-layouts`
Trigger: Use when limited space forces interface regions to compress, summarize, defer, relocate, or disappear and task priority must govern what is sacrificed before mere visual convenience.
Decision owned: This skill owns which information and controls remain primary, which may compress, which can move behind disclosure, and which may disappear because their task value is genuinely lower in the constrained state.
Sibling exclusion: Reordering preserves all regions while changing position; priority collapse decides what can lose fidelity or immediate presence.
Failure class: Failure includes hiding validation context while keeping decorative media, moving primary actions into generic overflow, summaries that omit exception states, layouts that preserve equal visual weight for unequal tasks, and “mobile simplification” that removes necessary decision evidence.
Falsifier: Falsification asks users or task simulations to complete high-priority flows using only the constrained state, injects warnings/errors, and removes each deferred region to determine whether a decision becomes under-informed.
Output: `region-priority-collapse-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Reordering preserves all regions while changing position; priority collapse decides what can lose fidelity or immediate presence.

### `designing-responsive-region-reordering`
Parent: `adapting-responsive-layouts`
Trigger: Use when responsive composition changes the visual order of major regions and reading order, focus order, task sequence, and semantic relationships must remain coherent across layouts.
Decision owned: This skill owns the decision about when region order may change and how visual, reading, focus, and task order stay aligned enough to preserve meaning.
Sibling exclusion: Priority collapse decides presence/fidelity, not sequence.
Failure class: Failure includes a visually first action reached last by keyboard, headings read after their controlled content, filters displayed before a context selector they depend on, and focus jumping to an unrelated region after breakpoint transition.
Falsifier: Falsification navigates each responsive state without a pointer, disables layout CSS to inspect semantic source order, moves across the breakpoint while focus is inside a relocated region, and checks announcement sequence.
Output: `responsive-region-reordering-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Priority collapse decides presence/fidelity, not sequence.

### `designing-adaptive-navigation-mode-transitions`
Parent: `adapting-responsive-layouts`
Trigger: Use when navigation changes between rail, sidebar, tabs, drawer, menu, or compact affordances and current location, hierarchy, reachability, open state, and orientation must survive the transition.
Decision owned: This skill owns the state mapping between navigation modes.
Sibling exclusion: Responsive region reordering governs general regions, not navigation's persistent route/hierarchy state.
Failure class: Failure includes drawer state persisting invisibly after becoming a sidebar, selected destinations hidden in “More” with no current-location cue, focus stranded in an unmounted drawer, hierarchy collapsed without ancestry indication, and route coverage differing by width.
Falsifier: Falsification deep-links to every navigation depth, transitions width while focus is inside navigation, changes modes with a branch expanded, and verifies every destination remains reachable.
Output: `adaptive-navigation-mode-transitions-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Responsive region reordering governs general regions, not navigation's persistent route/hierarchy state.

### `designing-responsive-toolbar-overflow`
Parent: `adapting-responsive-layouts`
Trigger: Use when a command toolbar cannot fit its available width and commands must migrate into overflow without losing priority, current state, discoverability, grouping, or operation context.
Decision owned: This skill owns that migration based on command priority and state, not arbitrary DOM order or icon width.
Sibling exclusion: Region collapse is coarse-grained; toolbar overflow owns individual command migration and state equivalence.
Failure class: Failure includes primary save/apply actions disappearing behind “More,” active formatting modes hidden with no visible cue, command groups split unpredictably, disabled reasons lost in overflow, duplicate commands rendered both inline and in the menu, and focus reset when commands migrate.
Falsifier: Falsification narrows the toolbar while a command is active, while focus is on the next-to-overflow item, and while permissions hide neighboring actions.
Output: `responsive-toolbar-overflow-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Region collapse is coarse-grained; toolbar overflow owns individual command migration and state equivalence.

### `designing-responsive-table-mode-transitions`
Parent: `adapting-responsive-layouts`
Trigger: Use when a table cannot preserve its full row-column geometry at constrained widths and the interface must change mode while retaining comparison, row identity, sorting/filtering context, and action meaning.
Decision owned: This skill owns the mode transition that preserves those tasks when full geometry no longer fits.
Sibling exclusion: Priority collapse can hide regions but does not understand row-column comparison invariants.
Failure class: Failure includes stacked cards that make cross-record comparison impossible, hidden sort keys, row actions detached from the correct identity, selection cleared on transition, horizontal scrolling with no persistent row/column anchor, and different filtering semantics between representations.
Falsifier: Falsification asks for the same comparison and row-action tasks on both sides of the breakpoint, then transitions while sort/filter/selection are active.
Output: `responsive-table-mode-transitions-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Priority collapse can hide regions but does not understand row-column comparison invariants.

### `designing-responsive-form-reflow`
Parent: `adapting-responsive-layouts`
Trigger: Use when form fields, groups, help, errors, and actions reflow across responsive layouts and dependency order, labeling, validation context, and progress must remain semantically coherent.
Decision owned: This skill owns responsive rearrangement of field groups, labels, help, summaries, and actions while preserving dependencies and completion state.
Sibling exclusion: Generic region reordering lacks form-specific dependency and validation relationships.
Failure class: Failure includes dependent fields appearing before their controlling field, two-column source order reading across rows incorrectly, labels detached after layout switches, sticky submit obscuring the last input, help text moved so far that its field relationship is unclear, and input state remounted/lost at the breakpoint.
Falsifier: Falsification fills a partial form, triggers several validation errors, focuses a mid-form control, crosses the responsive threshold, and continues only by keyboard.
Output: `responsive-form-reflow-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Generic region reordering lacks form-specific dependency and validation relationships.

### `designing-pointer-to-touch-density-transitions`
Parent: `adapting-responsive-layouts`
Trigger: Use when the same interface can move between precise pointer input and coarse touch input and control density, target geometry, spacing, and adjacent-action risk must adapt without changing task semantics.
Decision owned: This skill owns the transition in density and target geometry when input capability changes, including hybrid devices that can switch without viewport change.
Sibling exclusion: Viewport layout can be identical while input precision changes.
Failure class: Failure includes hover-sized icon buttons on touch, invisible hit regions overlapping neighbors, layout jumping after a single accidental touch, dense expert mode automatically forced on a large touch display, and increased spacing that destroys critical data comparison without providing an alternative.
Falsifier: Falsification performs repeated adjacent-target tasks with touch, switches from pointer to touch at fixed viewport, rotates or docks a hybrid device, and verifies target geometry and task state.
Output: `pointer-to-touch-density-transitions-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Viewport layout can be identical while input precision changes.

### `designing-hover-to-nonhover-affordance-transitions`
Parent: `adapting-responsive-layouts`
Trigger: Use when information, controls, previews, or discoverability currently depend on hover and the interface must preserve their function on touch, pen, keyboard, or devices where hover is unavailable or unreliable.
Decision owned: This skill owns the replacement path when hover disappears: what becomes persistent, what moves to focus/press/disclosure, and what should be removed because it was merely decorative.
Sibling exclusion: Density adaptation does not decide how hover-exclusive meaning is recovered.
Failure class: Failure includes delete/edit icons visible only on row hover, status detail available only in a tooltip, tap opening the primary action so no gesture remains for a hover preview, persistent fallback controls causing severe clutter, and CSS hover states stuck after touch interaction.
Falsifier: Falsification disables hover and attempts every action/information task previously reachable by hover; then switches input modality without reloading.
Output: `hover-to-nonhover-affordance-transitions-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Density adaptation does not decide how hover-exclusive meaning is recovered.

### `designing-foldable-hinge-aware-layouts`
Parent: `adapting-responsive-layouts`
Trigger: Use when a foldable or dual-screen device can occlude, separate, or reshape usable regions and layout must account for hinge geometry, posture, spanning, continuity, and task placement.
Decision owned: This skill owns how interface regions span, avoid, or exploit that physical discontinuity while preserving interaction and content continuity across device postures.
Sibling exclusion: Container queries model allocated size but not a physical non-content gap inside that allocation.
Failure class: Failure includes dialogs centered under the hinge, text columns split through unreadable gaps, drag targets crossing unreachable space, master and detail swapping unexpectedly on posture change, keyboard focus jumping between panes, and designs that treat two panes as a decorative wide canvas instead of separate physical attention zones.
Falsifier: Falsification changes posture while a modal, selection, or edit is active; varies hinge orientation and bounds; and runs tasks near the discontinuity.
Output: `foldable-hinge-aware-layouts-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Container queries model allocated size but not a physical non-content gap inside that allocation.

### `preserving-responsive-state-continuity`
Parent: `adapting-responsive-layouts`
Trigger: Use when responsive mode changes can remount, relocate, hide, or transform interface regions and selection, input, focus, scroll, disclosure, and transient task state must survive correctly.
Decision owned: This skill owns which UI state is presentation-independent, how it maps between alternate layouts, and what must happen to focus/scroll when a stateful region moves or changes representation.
Sibling exclusion: Responsive reordering governs spatial sequence, not persistence of task state.
Failure class: Failure includes drafts cleared because mobile and desktop forms are separate trees, focus falling to body after a sidebar becomes a drawer, selected items disappearing, duplicated async submissions from remount effects, and scroll restoration to the wrong semantic location after layout reordering.
Falsifier: Falsification establishes each state class, crosses the breakpoint repeatedly, changes orientation, and continues the task without reload.
Output: `responsive-state-continuity-contract`
Evidence role: Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26.
Delete-the-skill: Responsive reordering governs spatial sequence, not persistence of task state.

### `engineering-webfont-loading-transitions`
Parent: `crafting-typography`
Trigger: Use when web typography changes between unavailable, fallback, loading, and final font states and readability, layout stability, timing, and failure behavior need an explicit loading contract.
Decision owned: This skill owns how those states transition without sacrificing readable content or destabilizing the interface.
Sibling exclusion: Fallback-metric engineering can make two faces geometrically compatible but does not decide when either face appears or how load failure behaves.
Failure class: Characteristic Failure includes invisible body text during a long request, a late swap moving a confirmation control under the pointer, fallback glyphs missing symbols, preloads that compete with more critical resources, duplicate font downloads from mismatched descriptors, and cached runs masking a broken cold-start policy.
Falsifier: Falsification blocks the font host, adds high latency, clears cache, starts an interaction before the final face arrives, and compares geometry across states.
Output: `webfont-loading-transitions-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Fallback-metric engineering can make two faces geometrically compatible but does not decide when either face appears or how load failure behaves.

### `engineering-font-fallback-metric-compatibility`
Parent: `crafting-typography`
Trigger: Use when fallback and final fonts need compatible advance widths, x-height, ascent, descent, and line metrics so font substitution does not materially reflow or shift the interface.
Decision owned: This skill owns metric compatibility: how fallback candidates are measured, normalized, and adjusted so substitution preserves line breaks, control size, and vertical rhythm within declared tolerances.
Sibling exclusion: Loading transitions decide *when* substitution happens; this skill decides *how geometrically compatible* the states are.
Failure class: Failure includes fallback text requiring an extra line that pushes actions below the fold, clipped diacritics from aggressive ascent overrides, icons misaligned because baseline metrics changed, numeric columns jittering after swap, and metric tuning based only on Latin samples while supported scripts choose a different fallback chain.
Falsifier: Falsification renders the same content with the final face blocked and enabled, sweeps widths near known wrapping boundaries, and checks height/line-count deltas.
Output: `font-fallback-metric-compatibility-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Without this owner the system can load fonts correctly yet still incur preventable wrapping and layout shifts during fallback.

### `designing-variable-font-axis-behavior`
Parent: `crafting-typography`
Trigger: Use when a variable font exposes weight, width, optical size, slant, grade, or custom axes and axis values must change predictably across roles, states, sizes, and responsive conditions.
Decision owned: This skill owns how supported axes are mapped to semantic roles and runtime conditions so interpolation remains intentional rather than arbitrary.
Sibling exclusion: Readable-line measure and fallback metrics consume the resulting typography but do not decide axis semantics.
Failure class: Failure includes using width axis as an emergency fit mechanism until glyphs become hard to read, mapping emphasis to weight values that move neighboring layout, combining automatic and manual optical size unpredictably, custom-axis values outside the meaningful design space, and browsers falling back to static instances with no visible indication in evidence.
Falsifier: Falsification renders min/default/max and boundary role values, disables variable-font support, changes container size around responsive mappings, and compares task-relevant text.
Output: `variable-font-axis-behavior-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Readable-line measure and fallback metrics consume the resulting typography but do not decide axis semantics.

### `engineering-font-subsetting-and-glyph-coverage`
Parent: `crafting-typography`
Trigger: Use when font files are subset by script, Unicode range, locale, feature, or product surface and loading savings must not create missing glyphs, broken fallback chains, or inconsistent typographic behavior.
Decision owned: This skill owns how subsets are partitioned, declared, requested, and verified against the actual character repertoire a product promises to support.
Sibling exclusion: Fallback metrics assume a fallback is intentionally selected; this skill decides whether and when missing repertoire forces that selection.
Failure class: Failure includes tofu boxes for rare but valid names, punctuation taken from an unintended fallback, a currency symbol missing from a “Latin” subset, shaping tables removed from complex scripts, ranges that trigger both large files, and build pipelines whose subset contents drift without cache/version updates.
Falsifier: Falsification samples the edge of every declared range, introduces rare supported characters, tests mixed-script and combining sequences, and blocks secondary subsets.
Output: `font-subsetting-and-glyph-coverage-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Fallback metrics assume a fallback is intentionally selected; this skill decides whether and when missing repertoire forces that selection.

### `designing-readable-line-measure`
Parent: `crafting-typography`
Trigger: Use when prose, labels, or dense reading text needs an evidence-backed line-length policy across font metrics, viewport/container changes, text scaling, and content types.
Decision owned: This skill owns the line-measure contract for sustained or task-critical text: which content types require bounded measure, how metrics influence that bound, and how the measure adapts without forcing arbitrary viewport constants.
Sibling exclusion: Line breaking determines where a line can break; it does not decide how long the reading line should be.
Failure class: Failure includes full-width desktop paragraphs that require large eye travel, overly narrow columns creating choppy one- or two-word line endings, text reduced in size to fit a fixed card, reading width changing sharply after font swap, and “max-width” applied to containers whose internal text already has a different effective measure.
Falsifier: Falsification swaps to the supported fallback face, increases text size, changes container width, and renders representative long and short content.
Output: `readable-line-measure-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Line breaking determines where a line can break; it does not decide how long the reading line should be.

### `designing-line-breaking-and-hyphenation`
Parent: `crafting-typography`
Trigger: Use when text wrapping, break opportunities, hyphenation, unbreakable sequences, language rules, and narrow-column behavior must preserve readability without silently removing content.
Decision owned: This skill owns break and hyphenation policy for visible text: preserving words and semantics while preventing layout overflow under realistic languages, URLs, identifiers, and narrow measures.
Sibling exclusion: Truncation removes visible content; this skill preserves all content while choosing legal wrapping points.
Failure class: Failure includes horizontal overflow caused by a single long token, aggressive break-all splitting ordinary words at arbitrary characters, hyphenation applied to codes that users must copy exactly, incorrect language tags producing absurd break points, and line-breaking rules that visually separate a sign or unit from its value.
Falsifier: Falsification injects the longest plausible strings for each class, switches document language, disables hyphenation support, and narrows the container below normal breakpoints.
Output: `line-breaking-and-hyphenation-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Truncation removes visible content; this skill preserves all content while choosing legal wrapping points.

### `designing-truncation-and-overflow-truth`
Parent: `crafting-typography`
Trigger: Use when visible text may be clipped, ellipsized, line-clamped, or summarized and the interface must preserve access to the full truth, distinguish omission from absence, and protect decision-critical content.
Decision owned: This skill owns whether shortening is permissible, what information may be hidden, how omission is signaled, and how the complete value remains recoverable for users and assistive technology.
Sibling exclusion: Line-breaking retains all text; readable measure sets preferred width.
Failure class: Failure includes two files both shown as `quarterly-repo…`, hidden negative signs or units, warnings clamped before the consequence, full values available only in hover tooltips, ellipsis used even though text is actually absent, and copy actions copying the truncated visual string instead of the canonical value.
Falsifier: Falsification constructs values that differ only in the truncated region, disables hover, navigates by keyboard/touch, and asks the user to identify/copy the correct full value.
Output: `truncation-and-overflow-truth-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Line-breaking retains all text; readable measure sets preferred width.

### `designing-numeric-tabular-alignment`
Parent: `crafting-typography`
Trigger: Use when changing numeric values must remain visually comparable across rows, columns, counters, timers, or dashboards and digit width, sign, grouping, and update stability need typographic control.
Decision owned: This skill owns typographic treatment that preserves digit rhythm and positional comparability for general numeric data without imposing financial/accounting conventions.
Sibling exclusion: Financial alignment owns accounting semantics; this skill applies to generic dynamic numbers such as metrics and timers.
Failure class: Failure includes timers that visibly wobble each second, right-aligned columns whose internal digit widths impede comparison, fallback fonts lacking the requested feature, units causing changing column width, and numeric styling that accidentally makes text labels monospaced too.
Falsifier: Falsification cycles every digit through the same position, updates magnitude boundaries such as 99→100, switches locale/grouping, and blocks the primary font.
Output: `numeric-tabular-alignment-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Financial alignment owns accounting semantics; this skill applies to generic dynamic numbers such as metrics and timers.

### `designing-decimal-and-financial-type-alignment`
Parent: `crafting-typography`
Trigger: Use when monetary or accounting values require consistent decimal, sign, currency, magnitude, parenthesis, and missing-value alignment so financial comparison remains truthful across locales and states.
Decision owned: This skill owns the visual alignment contract that makes those structures comparable without falsifying locale or accounting meaning.
Sibling exclusion: Generic tabular numerals cannot decide accounting parentheses, currency lanes, missing-value notation, or locale-specific decimal guides.
Failure class: Failure includes negatives whose parentheses shift decimals, currency symbols consuming variable width and hiding comparison, em dashes that look like negative signs for missing values, mixed decimal precision without a declared rounding policy, locale formatting overridden to keep columns visually identical, and accounting alignment achieved with inserted spaces that corrupt copying.
Falsifier: Falsification changes locale, sign, magnitude, precision, and exceptional state while holding the column contract constant.
Output: `decimal-and-financial-type-alignment-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Generic tabular numerals cannot decide accounting parentheses, currency lanes, missing-value notation, or locale-specific decimal guides.

### `designing-code-and-monospace-typography`
Parent: `crafting-typography`
Trigger: Use when code, logs, terminals, diffs, identifiers, or structured technical text needs typography optimized for glyph disambiguation, indentation, line scanning, selection, wrapping, and dense developer workflows.
Decision owned: This skill owns typographic decisions for code-like content: monospacing policy, ambiguous glyphs, line height, ligatures, tab width, wrapping, whitespace visibility, and how dense technical text coexists with UI chrome.
Sibling exclusion: General typography can establish hierarchy but does not own source-code character fidelity and structural scanning.
Failure class: Failure includes ambiguous zero/O causing operator error, ligatures concealing character count in diffs, fallback font breaking alignment, line height clipping underlines/diagnostics, wrapped logs whose continuation cannot be distinguished from new records, and `pre` blocks forcing page-wide horizontal overflow without a containment strategy.
Falsifier: Falsification asks reviewers to distinguish known ambiguous tokens, blocks the primary font, changes zoom, displays deep indentation and long lines, and compares copied source to visible glyphs.
Output: `code-and-monospace-typography-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: General typography can establish hierarchy but does not own source-code character fidelity and structural scanning.

### `designing-mixed-font-baseline-alignment`
Parent: `crafting-typography`
Trigger: Use when text runs combine fonts, scripts, icon glyphs, badges, inline controls, or fallback faces and their baselines, optical centers, line boxes, and vertical rhythm must remain coherent.
Decision owned: This skill owns how those elements align without clipping or optical drift.
Sibling exclusion: Fallback metric compatibility compares alternate faces occupying the same role over time.
Failure class: Failure includes icons appearing to sag below adjacent text, CJK or accented glyphs clipped by a line-height tuned to Latin, badges expanding row height unpredictably, fallback runs jumping vertically, and center-aligned inline controls that visually disconnect from the textual baseline.
Falsifier: Falsification forces fallback faces, inserts tall/deep glyphs, increases text size, and compares multiple inline element types in the same row.
Output: `mixed-font-baseline-alignment-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Fallback metric compatibility compares alternate faces occupying the same role over time.

### `diagnosing-runtime-text-rendering-drift`
Parent: `crafting-typography`
Trigger: Use when implemented text does not match expected wrapping, weight, line boxes, glyph shapes, spacing, or baselines and the cause may be resolved fonts, browser metrics, platform rasterization, fallback, or runtime CSS.
Decision owned: This skill owns the diagnosis that separates those causes before anyone “fixes” the screenshot with arbitrary spacing.
Sibling exclusion: Rendered-UI critique may detect that text differs, but it does not own font-resolution root-cause diagnosis.
Failure class: Characteristic Failure includes fixing line-height when the wrong fallback face loaded, adding letter spacing to compensate for a stale font build, blaming anti-aliasing for actual container-width differences, comparing screenshots at different DPR/zoom, and declaring parity based on CSS declarations even though the browser resolved a different font.
Falsifier: Falsification recreates the render in a controlled environment, swaps only one suspected variable, and predicts the observed change before testing.
Output: `runtime-text-rendering-drift-contract`
Evidence role: Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices. Primary pin: `adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7`. Secondary: W3C CSS Fonts/Text specifications (normative web standards, live authority).
Delete-the-skill: Rendered-UI critique may detect that text differs, but it does not own font-resolution root-cause diagnosis.

### `designing-agent-shared-state-reconciliation`
Parent: `designing-human-ai-interaction`
Trigger: Use when a human-facing interface and an AI agent can both mutate the same task state and the product must reconcile concurrent edits, stale observations, optimistic UI, and authoritative backend outcomes without lying about what is true.
Decision owned: This skill owns the decision model for reconciling those competing versions into one legible, truthful interface state.
Sibling exclusion: Output: `agent-shared-state-reconciliation-contract`, containing revision identity, writer authority, conflict classes, merge rules, rollback behavior, stale-observation handling, and evidence requirements.
Failure class: Failure includes last-arrival-wins corruption, hidden overwrites, optimistic state that never rolls back, conflict banners that do not identify the affected data, and agent text that claims an action succeeded while the shared object shows failure.
Falsifier: Falsification should deliberately inject stale reads, reorder acknowledgements, duplicate tool events, and mutate the same field from human and agent paths.
Output: `agent-shared-state-reconciliation-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling boundary: agent tool-call lifecycle owns execution phases of a tool invocation, not reconciliation of shared domain state.

### `designing-agent-tool-call-lifecycles`
Parent: `designing-human-ai-interaction`
Trigger: Use when an AI agent invokes tools whose requests move through proposed, authorized, dispatched, running, succeeded, failed, cancelled, timed-out, or indeterminate states and the UI must expose those transitions truthfully.
Decision owned: This skill owns the interface contract that maps execution state to what the user can see and do.
Sibling exclusion: Sibling approval-scope design owns what a human authorization covers, not whether an authorized operation is queued or running.
Failure class: Characteristic Failure includes premature success badges, spinners that survive a terminal error, duplicate attempts hidden behind one card, cancellation UI that claims certainty before acknowledgement, and retries that repeat an irreversible action.
Falsifier: Falsification should inject late success after a local timeout, duplicated terminal events, cancellation races, network loss immediately after dispatch, and a retry against a non-idempotent tool.
Output: `agent-tool-call-lifecycles-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling approval-scope design owns what a human authorization covers, not whether an authorized operation is queued or running.

### `designing-tool-result-presentation-lifecycles`
Parent: `designing-generative-ui`
Trigger: Use when tool output arrives incrementally, changes shape over time, can be superseded, or needs to graduate from raw execution evidence into a stable user-facing result without losing provenance.
Decision owned: This skill owns the decisions that transform runtime output into a user-facing result surface: when raw evidence is shown, when it is summarized, when a structured view becomes canonical, how superseded views remain inspectable, and how uncertainty is preserved.
Sibling exclusion: Handoff execution truth to `designing-agent-tool-call-lifecycles`; hand off generated-component trust decisions to `designing-agent-generated-component-authority`; hand off schema degradation to `designing-generative-ui-schema-fallbacks`.
Failure class: Characteristic Failure includes rendering a parser error as tool failure, hiding partial completeness, silently replacing a result after the user acted on it, presenting model-generated summaries as source data, and allowing controls that assume fields the current representation does not possess.
Falsifier: Falsification should force malformed structured output, schema version drift, delayed enrichment, a renderer crash after tool success, and a corrected second result that contradicts the first.
Output: `tool-result-presentation-lifecycles-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Handoff execution truth to `designing-agent-tool-call-lifecycles`; hand off generated-component trust decisions to `designing-agent-generated-component-authority`; hand off schema degradation to `designing-generative-ui-schema-fallbacks`.

### `designing-agent-plan-preview-surfaces`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent can expose a proposed multi-step plan before execution and the interface must communicate intent, dependencies, uncertainty, side effects, and editable scope without implying the plan is guaranteed or already executed.
Decision owned: This skill owns what planning information is safe and useful to expose: user-relevant steps, dependencies, side-effect boundaries, required approvals, estimated uncertainty, and places where the plan may legitimately branch.
Sibling exclusion: Sibling approval-scope design owns the legal/semantic extent of an authorization, while this skill owns how a plan is represented and revised.
Failure class: Characteristic Failure includes exposing verbose pseudo-reasoning instead of actionable commitments, showing a fixed checklist that the runtime does not actually follow, silently inserting side-effecting steps after approval, retaining stale approval after a plan edit, and presenting speculative later steps as guaranteed.
Falsifier: Falsification should edit an early step with downstream dependencies, insert a newly required permission, make a planned tool unavailable, and force the agent to replan after partial execution.
Output: `agent-plan-preview-surfaces-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling approval-scope design owns the legal/semantic extent of an authorization, while this skill owns how a plan is represented and revised.

### `designing-agent-approval-scope-boundaries`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when a human approval must authorize a bounded set of agent actions and the interface must define exactly which operations, resources, parameters, duration, and side effects that approval covers.
Decision owned: This skill owns the decision contract for what one approval covers: operation class, target resources, parameter ranges, time window, quantity or spend limits, data disclosure, downstream delegation, and whether repeated executions remain authorized.
Sibling exclusion: Sibling plan-preview design owns how intended steps are represented.
Failure class: Characteristic Failure includes approvals attached only to chat-message IDs, wildcard resources hidden behind friendly wording, an old approval surviving a material parameter change, session-wide authorization with no revocation path, and a sub-agent treating another agent’s permission as transferable.
Falsifier: Falsification changes one scope dimension after approval, attempts an additional execution, swaps target resource identity while preserving the label, exceeds a numeric bound, waits past expiry, and delegates the action through another actor.
Output: `agent-approval-scope-boundaries-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling plan-preview design owns how intended steps are represented.

### `detecting-agent-approval-scope-drift`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent is executing under a prior approval and later evidence, replanning, parameter substitution, retries, or delegated work may cause the actual operation to exceed the scope the user originally authorized.
Decision owned: This skill owns the continuous comparison between the authorized semantic action and the action about to execute.
Sibling exclusion: Handoff authorization construction to `designing-agent-approval-scope-boundaries`, changed plan semantics to `designing-agent-plan-preview-surfaces`, and runtime permission growth to `designing-agent-tool-permission-escalation`.
Failure class: Characteristic Failure includes checking only tool name while parameters broaden, ignoring expiry, comparing friendly labels instead of stable resource identity, allowing a retry to inherit approval after a material plan change, and detecting drift only after the side effect occurred.
Falsifier: Falsification should mutate one dimension at a time: recipient, amount, environment, resource version, disclosure field, delegation route, and time.
Output: `agent-approval-scope-drift-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: The delete-the-skill test passes because a static approval boundary alone cannot protect against later semantic movement.

### `designing-agent-interruption-and-resume`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when users, system events, policy changes, or external failures can interrupt a running agent and the UI must preserve what is valid, expose what stopped, and resume from a defensible checkpoint instead of restarting blindly.
Decision owned: This skill owns the contract for pausing execution and constructing a resumable checkpoint.
Sibling exclusion: Sibling background-run surfaces own visibility while a run continues away from the foreground; this skill owns a run that actually stops or loses continuity.
Failure class: Characteristic Failure includes restarting from the beginning after a stop, losing artifacts that were already valid, claiming cancellation while external work continues, reusing expired approval, and resuming from stale task state without revalidation.
Falsifier: Interrupt during each important lifecycle phase: before dispatch, after dispatch but before acknowledgement, after partial side effects, during a permission prompt, and after a dependency changes.
Output: `agent-interruption-and-resume-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling background-run surfaces own visibility while a run continues away from the foreground; this skill owns a run that actually stops or loses continuity.

### `designing-agent-partial-completion-recovery`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent finishes some intended work but fails, blocks, or loses authority before the task is complete and the UI must preserve valid outcomes, expose residual obligations, and avoid pretending the whole run either succeeded or failed.
Decision owned: --- # Designing Agent Partial-Completion Recovery ## What this skill owns Agentic work is often non-atomic.
Sibling exclusion: Sibling interruption/resume decides whether a stopped run can continue from a checkpoint.
Failure class: Characteristic Failure includes “run failed” banners that hide completed side effects, restart buttons that duplicate work, declaring success because most steps finished, losing generated artifacts after a late error, and assuming an operation can be rolled back when only compensation exists.
Falsifier: Falsification should fail the run after each materially different obligation, inject a late verification failure after apparent success, make a completed artifact stale before recovery, and test a non-reversible side effect.
Output: `agent-partial-completion-recovery-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling interruption/resume decides whether a stopped run can continue from a checkpoint.

### `designing-agent-retry-and-replay-controls`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when users or agents may repeat a failed, timed-out, or disputed operation and the interface must distinguish safe retry, exact replay, modified rerun, and reconcile-first recovery so repeated side effects do not occur accidentally.
Decision owned: This skill owns which of those controls are available and what semantic guarantee each one makes.
Sibling exclusion: Sibling partial-completion recovery derives what remains to be done at the task level.
Failure class: Characteristic Failure includes a generic Retry button after an outcome-unknown send, silently changing parameters while calling it replay, overwriting failure history with the successful second attempt, reusing approval after the operation’s scope changed, and re-executing already-successful items in a batch.
Falsifier: Force a timeout after dispatch, a duplicated callback, a non-idempotent endpoint, a batch with mixed success, expired approval, and an external record that changes between attempts.
Output: `agent-retry-and-replay-controls-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling partial-completion recovery derives what remains to be done at the task level.

### `designing-agent-run-branching`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when a user or agent can fork an in-progress or completed run into alternate continuations and the UI must preserve shared history, branch-local state, side effects, approvals, and comparison without merging incompatible realities.
Decision owned: This skill owns the branch model: what is inherited, what is copied, what remains globally shared, and what must be revalidated before the new branch can act.
Sibling exclusion: Sibling plan previews own alternative steps before a run is committed; this skill owns actual divergent execution lineages.
Failure class: Characteristic Failure includes forked runs sharing mutable local state accidentally, duplicated external side effects when a branch replays ancestral work, cloned approvals that no longer match, hidden ancestry that makes two branches look independent, and “switch branch” controls that imply external reality changes with the view.
Falsifier: Fork before and after a side effect, fork while an outcome is unknown, edit the same shared resource in both descendants, change approval-sensitive parameters in one branch, and switch repeatedly between branches.
Output: `agent-run-branching-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling plan previews own alternative steps before a run is committed; this skill owns actual divergent execution lineages.

### `designing-agent-side-effect-ledgers`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent performs externally observable actions and the interface needs a durable ledger of intended, attempted, confirmed, disputed, compensated, and irreversible effects so users can audit what actually changed.
Decision owned: This skill owns the interface contract for a durable side-effect ledger: a user-facing and machine-auditable record of actions that changed or may have changed external state.
Sibling exclusion: Sibling approval-scope skills govern authority before action.
Failure class: Characteristic Failure includes transcript-only accountability, overwriting failed attempts after a retry, hiding partial batch outcomes, labeling ambiguous results as failed or successful, failing to connect approvals to effects, and treating compensation as if the original effect never happened.
Falsifier: Inject duplicate callbacks, partial batches, an outcome-unknown network loss, a successful compensation, a changed target label, and a delegated sub-agent action.
Output: `agent-side-effect-ledgers-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling approval-scope skills govern authority before action.

### `designing-agent-reversible-action-surfaces`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent performs actions that can be undone, rolled back, or compensated and the interface must represent what reversal really means, how long it remains available, and which consequences cannot be restored exactly.
Decision owned: This skill owns the decision model that classifies reversal and turns it into truthful controls.
Sibling exclusion: Sibling retry/replay controls repeat attempts toward an intended outcome; this skill changes or compensates an outcome that already occurred.
Failure class: Characteristic Failure includes calling compensation “undo,” restoring visible content but losing permissions or references without disclosure, leaving expired undo controls active, reversing one step while dependent side effects remain, and claiming rollback before the external system confirms it.
Falsifier: Test reversal after the resource changes concurrently, after the advertised time window, after a dependent action occurs, after reconnect, and against a tool that reports success while the external state remains changed.
Output: `agent-reversible-action-surfaces-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling retry/replay controls repeat attempts toward an intended outcome; this skill changes or compensates an outcome that already occurred.

### `designing-agent-background-run-surfaces`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent continues working after the initiating view loses focus, closes, or hands off to another surface and the product must preserve run identity, progress truth, notification boundaries, and re-entry without pretending the work is synchronous.
Decision owned: This skill owns how a background run remains findable, truthful, interruptible where possible, and reconnectable to the context that initiated it.
Sibling exclusion: Sibling interruption/resume owns execution that stops; this skill owns execution that continues while foreground attention stops.
Failure class: Characteristic Failure includes “background” runs that die when the tab closes, duplicated work when a user reopens the task, stale notifications after a run was cancelled elsewhere, progress percentages fabricated from elapsed time, and re-entry that loses prior approvals or side effects.
Falsifier: Close the initiating surface during each lifecycle phase, reconnect from another device, issue cancellation from a secondary surface, expire an approval while backgrounded, and deliver a late completion after the user thought the run had stopped.
Output: `agent-background-run-surfaces-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling interruption/resume owns execution that stops; this skill owns execution that continues while foreground attention stops.

### `designing-agent-tool-permission-escalation`
Parent: `designing-agent-autonomy-and-control`
Trigger: Use when an agent reaches a step that requires broader tool permissions, stronger credentials, additional data access, or a more privileged execution mode and the UI must explain the delta without normalizing blanket escalation.
Decision owned: This skill owns how that delta is represented, justified, constrained, and either granted or denied without losing prior progress.
Sibling exclusion: Sibling approval-scope design defines what an approval authorizes once presented.
Failure class: Characteristic Failure includes “Allow access” prompts that hide read/write differences, broad OAuth grants represented as task-local permission, escalation requested after execution already began, permissions retained beyond the stated duration, and denial that causes the agent to loop the same prompt.
Falsifier: Test a provider that offers only coarse scopes, a request whose affected resource changes before approval, denial followed by a degraded path, expiry mid-run, and a sub-agent that attempts to reuse the grant.
Output: `agent-tool-permission-escalation-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling approval-scope design defines what an approval authorizes once presented.

### `designing-agent-generated-component-authority`
Parent: `designing-generative-ui`
Trigger: Use when an agent can generate interactive UI components and the product must decide which generated controls are allowed to display data, mutate state, request approval, or trigger tools without granting arbitrary generated markup product authority.
Decision owned: This skill owns the authority boundary between generated presentation and product-controlled capability.
Sibling exclusion: Sibling tool-result presentation owns how results evolve from raw to structured views, not what generated controls may do.
Failure class: Characteristic Failure includes generated buttons calling arbitrary tool names, inferred data rendered as server truth, host actions triggered with unvalidated resource IDs, a generated confirmation dialog that omits material side effects, and stale generated controls remaining active after capability revocation.
Falsifier: Feed a generated schema with an unknown action, altered action parameters, forged success status, a stale resource revision, and a request to render privileged data.
Output: `agent-generated-component-authority-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling tool-result presentation owns how results evolve from raw to structured views, not what generated controls may do.

### `designing-generative-ui-schema-fallbacks`
Parent: `designing-generative-ui`
Trigger: Use when generative UI may receive unknown, partial, invalid, newer, or unsupported component schemas and the host must degrade to safe representations without losing tool truth, user control, or provenance.
Decision owned: This skill owns the fallback ladder that keeps the product useful and truthful when structured rendering cannot proceed as intended.
Sibling exclusion: Sibling generated-component authority governs what a valid generated component may do.
Failure class: Generative UI cannot assume every produced schema matches the current renderer.
Falsifier: Falsification should send future-version schemas, remove required fields, corrupt one nested component while leaving siblings valid, disable a platform capability, and trigger a runtime renderer exception after partial display.
Output: `generative-ui-schema-fallbacks-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling generated-component authority governs what a valid generated component may do.

### `designing-human-correction-of-agent-state`
Parent: `designing-human-ai-interaction`
Trigger: Use when a human needs to correct what an agent currently believes about task facts, intent, constraints, entities, or progress and the interface must propagate that correction into execution state without rewriting history or leaving stale assumptions active.
Decision owned: This skill owns the contract for turning a human correction into explicit state mutation with known blast radius.
Sibling exclusion: Sibling shared-state reconciliation handles concurrent versions from multiple writers; this skill handles an explicit human declaration that some agent-held state should change.
Failure class: Characteristic Failure includes acknowledging correction conversationally while runtime state stays unchanged, rewriting history so audit becomes impossible, failing to invalidate approval based on old semantics, over-propagating a small change into unnecessary task reset, and letting a user assertion override authoritative external outcome without distinction.
Falsifier: Correct a value after it appears in a plan, after approval but before dispatch, after a generated component renders, and after one dependent step already completed.
Output: `human-correction-of-agent-state-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling shared-state reconciliation handles concurrent versions from multiple writers; this skill handles an explicit human declaration that some agent-held state should change.

### `designing-multi-agent-handoff-visibility`
Parent: `designing-multi-agent-surfaces`
Trigger: Use when one agent delegates or transfers work to another agent and the interface must show responsibility, context transfer, authority boundaries, pending obligations, and return conditions so users do not lose track of who is acting or why.
Decision owned: This skill owns the visible contract for a handoff—who owns the task now, what context was transferred, what authority the receiving agent has, what remains with the sender, and how results return.
Sibling exclusion: Sibling multi-agent surface design covers overall actor presence and coordination.
Failure class: Characteristic Failure includes invisible delegation, permissions inherited implicitly, duplicate agents working the same side-effecting task, stale sub-agent results merged without warning, and handoffs with no defined return path.
Falsifier: Delegate a task that requires narrower authority, change shared state while the sub-agent works, cancel the parent run, reject the handoff, and create overlapping obligation assignments.
Output: `multi-agent-handoff-visibility-contract`
Evidence role: Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety. Primary pin: `ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b`. Secondary: CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted).
Delete-the-skill: Sibling multi-agent surface design covers overall actor presence and coordination.

### `designing-component-state-evidence-matrices`
Parent: `binding-ui-evidence`
Trigger: Use when a component has many semantic, interaction, validation, permission, async, or accessibility states and verification needs an explicit matrix showing which meaningful states must be rendered and evidenced rather than relying on a happy-path screenshot.
Decision owned: This skill owns the matrix that decides which component states are materially distinct enough to require evidence.
Sibling exclusion: Sibling interaction-regression evidence focuses on behavioral sequences across revisions; this skill defines state-space coverage for one component contract.
Failure class: Characteristic Failure includes a gallery of visually different variants with no semantic coverage model, exhaustive combinatorics that hides important cells in noise, happy-path-only snapshots, unreachable fixture states, and matrices that omit transitions.
Falsifier: Remove one material state, mutate a transition, make a permission state unreachable, and change a component revision without updating fixtures.
Output: `component-state-evidence-matrices-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling interaction-regression evidence focuses on behavioral sequences across revisions; this skill defines state-space coverage for one component contract.

### `designing-interaction-regression-evidence`
Parent: `binding-ui-evidence`
Trigger: Use when a UI change could preserve static appearance while breaking event order, focus movement, async behavior, keyboard paths, cancellation, or multi-step task semantics and verification needs evidence of interaction sequences across revisions.
Decision owned: This skill owns the evidence model for proving behavior across meaningful event sequences, not merely final screenshots.
Sibling exclusion: Handoff visual appearance changes to visual-regression baselines, responsive variants to responsive regression matrices, and per-state coverage to component-state evidence matrices.
Failure class: Failure includes tests that jump directly to target state, event recordings tied to unstable selectors, hidden race conditions masked by generous waits, snapshots after the bug has already self-corrected, and suites that cover mouse but not the keyboard path sharing the same feature.
Falsifier: Deliberately reorder async responses, slow network acknowledgement, inject duplicate input, move focusable elements, cancel at boundary moments, and run the same sequence with keyboard and pointer where both are supported.
Output: `interaction-regression-evidence-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: The delete-the-skill test passes because removing this owner leaves a verification gap where regressions that occur only during interaction can pass every static screenshot and final-state assertion.

### `designing-visual-regression-baselines`
Parent: `binding-ui-evidence`
Trigger: Use when rendered UI must be compared against approved visual references and the team needs a disciplined baseline model that separates intentional design change from rendering defect, environment noise, and stale reference data.
Decision owned: This skill owns how visual baselines are created, scoped, versioned, and linked to design intent so diffs can be interpreted rather than blindly approved.
Sibling exclusion: Sibling responsive regression matrices decide which viewport/layout states need evidence; this skill governs the reference image for an admitted state.
Failure class: Characteristic Failure includes baselines captured from an unpinned environment, approval of huge diff sets without review, stale references after component state changes, masks that hide real content movement, and visual tests that assert one viewport while claiming responsive fidelity.
Falsifier: Change one spacing token, load a fallback font, alter device scale factor, mutate fixture content, and inject a deliberate one-pixel alignment defect.
Output: `visual-regression-baselines-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling responsive regression matrices decide which viewport/layout states need evidence; this skill governs the reference image for an admitted state.

### `designing-responsive-regression-matrices`
Parent: `binding-ui-evidence`
Trigger: Use when a surface changes structure, priority, navigation, density, or interaction across available space and verification needs a bounded matrix of widths, heights, container states, orientations, zoom, and content pressure rather than a few device screenshots.
Decision owned: This skill owns the evidence matrix for those structural boundaries.
Sibling exclusion: Sibling browser/device evidence owns implementation variance across engines and hardware.
Failure class: Characteristic Failure includes testing only canonical phone/tablet/desktop widths, missing height-constrained states, a visual reorder that disagrees with focus order, content overflow appearing only under localization, container components tested only full-page, and state lost when crossing a breakpoint.
Falsifier: Move each structural threshold by a small amount, expand labels, increase zoom, constrain height, place a component inside a narrow container on a wide viewport, and resize during an active interaction.
Output: `responsive-regression-matrices-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling browser/device evidence owns implementation variance across engines and hardware.

### `designing-browser-and-device-evidence-matrices`
Parent: `binding-ui-evidence`
Trigger: Use when UI correctness may vary by browser engine, OS, input hardware, device class, pixel density, installed capabilities, or assistive technology stack and verification needs risk-based environment coverage rather than one canonical machine.
Decision owned: This skill owns which environment combinations are materially different enough to require evidence and how that coverage is justified.
Sibling exclusion: Sibling responsive regression owns layout mode transitions regardless of browser.
Failure class: Characteristic Failure includes calling a desktop responsive emulator “mobile tested,” treating all Chromium hosts as identical despite different embedding policies, ignoring OS-level font or accessibility differences, stale device lab evidence, and claiming broad support from one engine.
Falsifier: Change engine, device pixel ratio, hardware input mix, installed font availability, accessibility stack, and permission behavior while holding the product fixture constant.
Output: `browser-and-device-evidence-matrices-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling responsive regression owns layout mode transitions regardless of browser.

### `designing-accessibility-evidence-packets`
Parent: `binding-ui-evidence`
Trigger: Use when an accessibility claim must be supported by a mixed packet of automated checks, semantic inspection, keyboard interaction, assistive technology testing, visual review, and documented manual judgment rather than a single scanner result.
Decision owned: This skill owns how those evidence types are assembled into one claim-bounded packet.
Sibling exclusion: Sibling component-state matrices decide which states need evidence; this skill decides how accessibility obligations are proven within them.
Failure class: Characteristic Failure includes scanner-only certification, one keyboard smoke test standing in for state coverage, undocumented assistive-technology setup, manual checks with no criterion mapping, suppressed “incomplete” automated results, and evidence copied forward after a semantic rewrite.
Falsifier: Inject a keyboard trap that scanners miss, remove an accessible name, change live-region timing, alter zoom/reflow behavior, and update the component DOM without refreshing the packet.
Output: `accessibility-evidence-packets-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling component-state matrices decide which states need evidence; this skill decides how accessibility obligations are proven within them.

### `designing-manual-review-evidence-contracts`
Parent: `binding-ui-evidence`
Trigger: Use when important UI qualities cannot be fully automated and a human review must produce reproducible, bounded evidence with explicit questions, artifacts, verdicts, uncertainty, reviewer role, and escalation instead of informal approval comments.
Decision owned: This skill owns how those judgments become evidence rather than unstructured opinion.
Sibling exclusion: Sibling visual-diff triage helps reviewers decide whether image differences are noise or material; it does not define a general human-review protocol.
Failure class: Characteristic Failure includes “LGTM” as the only record, review against an unpinned build, reviewers answering different implicit questions, authors self-certifying high-risk work with no independence rule, and blocked checks being omitted from the packet.
Falsifier: Give the same packet to another qualified reviewer, change the build revision while keeping screenshots, remove the review question, or inject an artifact that contradicts the written verdict.
Output: `manual-review-evidence-contracts-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling visual-diff triage helps reviewers decide whether image differences are noise or material; it does not define a general human-review protocol.

### `detecting-rendered-environment-drift`
Parent: `binding-ui-evidence`
Trigger: Use when the same UI revision renders differently across CI, local development, browsers, operating systems, fonts, GPU paths, themes, or runtime configuration and the team must determine whether the difference is environmental drift or a product regression.
Decision owned: This skill owns the diagnosis that separates environment drift from product change.
Sibling exclusion: Sibling browser/device matrices decide which environments deserve testing; this skill explains unexpected divergence between supposedly comparable evidence.
Failure class: Characteristic Failure includes updating baselines to match a drifting CI image, blaming “browser differences” without identifying the changed capability, treating missing fonts as harmless raster noise, and comparing different fixture data as though it were environment variance.
Falsifier: Pin all environment dimensions and reproduce the diff; then vary suspected dimensions one at a time.
Output: `rendered-environment-drift-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling browser/device matrices decide which environments deserve testing; this skill explains unexpected divergence between supposedly comparable evidence.

### `designing-design-system-consumer-regression-tests`
Parent: `binding-ui-evidence`
Trigger: Use when a design-system primitive, token, component, or package change can break downstream applications and verification must prove consumer behavior across representative integration patterns rather than only the design-system repository itself.
Decision owned: This skill owns the evidence strategy for validating changes against representative downstream consumer contexts.
Sibling exclusion: Sibling story-state fixtures validate isolated component states; this skill validates package behavior inside downstream integration environments.
Failure class: Characteristic Failure includes testing only Storybook, one pristine example app, consumers all using identical integration style, skipped upgrade-path testing, and baselines updated in every consumer without identifying a shared breaking cause.
Falsifier: Change a token name, component slot, CSS layer order, package export, hydration behavior, and deprecated prop handling.
Output: `design-system-consumer-regression-tests-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling story-state fixtures validate isolated component states; this skill validates package behavior inside downstream integration environments.

### `designing-story-state-fixture-coverage`
Parent: `binding-ui-evidence`
Trigger: Use when isolated component stories or fixtures are used as verification inputs and the team must ensure they represent reachable semantic states, stable data boundaries, interaction preconditions, and high-risk variants rather than a decorative component gallery.
Decision owned: This skill owns which fixtures exist and whether they faithfully instantiate the component contract.
Sibling exclusion: Sibling component-state matrices define what must be covered; this skill defines the deterministic story/fixture artifacts that instantiate those cells.
Failure class: Characteristic Failure includes happy-path story galleries, dozens of color/size variants with no behavioral states, fixtures that bypass real permission or validation logic, live API dependence that makes baselines flaky, and stale stories that render states the component no longer supports.
Falsifier: Remove a high-risk state, alter fixture data so an overflow boundary disappears, bypass a real transition with an impossible prop combination, or inject nondeterministic time.
Output: `story-state-fixture-coverage-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling component-state matrices define what must be covered; this skill defines the deterministic story/fixture artifacts that instantiate those cells.

### `triaging-visual-diff-noise`
Parent: `binding-ui-evidence`
Trigger: Use when visual regression systems produce image differences and reviewers must distinguish product regressions from anti-aliasing, animation, font rasterization, dynamic content, capture timing, subpixel layout, or other nondeterministic noise without masking real defects.
Decision owned: This skill owns the decision process that classifies a diff and chooses the narrowest mitigation that removes nondeterminism without weakening the visual contract.
Sibling exclusion: Sibling visual-regression baselines define what is expected; this skill decides whether an observed pixel delta is trustworthy evidence of change.
Failure class: Characteristic Failure includes approving all low-percentage diffs, masking dynamic containers whose size can regress, treating fallback fonts as harmless anti-aliasing, increasing global tolerance after one flaky component, and updating baselines before isolating capture timing.
Falsifier: Introduce a deliberate one-pixel alignment error inside a noisy region, shift font load timing, enable animation, randomize fixture text, and capture the same revision repeatedly.
Output: `visual-diff-noise-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling visual-regression baselines define what is expected; this skill decides whether an observed pixel delta is trustworthy evidence of change.

### `governing-regression-baseline-updates`
Parent: `binding-ui-evidence`
Trigger: Use when visual, interaction, snapshot, or other regression references need to change and the team must prove the baseline is obsolete because the product contract intentionally changed rather than accepting new output merely to make verification pass.
Decision owned: This skill owns when a reference may move, what evidence must accompany the move, and how reviewers distinguish intentional product evolution from accidental normalization of a defect.
Sibling exclusion: Sibling visual-regression baselines define reference identity; this skill governs changing that reference.
Failure class: Characteristic Failure includes updating references automatically after tests fail, accepting large baseline sets with no causal grouping, rebaselining from an unpinned environment, letting fixture changes silently redefine expected behavior, and using baseline promotion to hide a real browser-specific defect.
Falsifier: Introduce an unrelated regression alongside a legitimate design change, change a fixture and image in the same patch, and generate baselines from a drifting environment.
Output: `regression-baseline-updates-contract`
Evidence role: Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth. Primary pin: `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a`. Secondary: dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence.
Delete-the-skill: Sibling visual-regression baselines define reference identity; this skill governs changing that reference.

### `designing-directional-focus-graphs`
Parent: `routing-ui-work`
Trigger: Use when users navigate an interface with directional input such as a gamepad, remote, D-pad, or keyboard arrows and the product needs a deterministic focus graph that survives dynamic layout, disabled items, virtualized content, overlays, and spatial ambiguity.
Decision owned: This skill owns the semantic graph that maps directional intent to the next valid focus target.
Sibling exclusion: Sibling remote-control navigation owns remote-specific command mapping and long-range navigation conventions; this skill owns spatial focus adjacency for any directional device.
Failure class: Characteristic Failure includes focus oscillation between two nodes, invisible offscreen destinations, geometry-based jumps across unrelated regions, disabled targets capturing focus, virtualized lists losing identity, and overlays returning focus to an arbitrary default.
Falsifier: Randomly disable nodes, insert content, change aspect ratio, open nested overlays, virtualize a long rail, and traverse every edge from representative nodes.
Output: `directional-focus-graphs-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling remote-control navigation owns remote-specific command mapping and long-range navigation conventions; this skill owns spatial focus adjacency for any directional device.

### `designing-remote-control-navigation`
Parent: `routing-ui-work`
Trigger: Use when a TV, console, set-top box, kiosk, or couch-distance interface is controlled by a limited remote and navigation must map sparse buttons, long-press behavior, back semantics, paging, focus memory, and accessibility expectations into predictable movement.
Decision owned: This skill owns the command semantics that turn that sparse device into a complete navigation model without overloading buttons differently from screen to screen.
Sibling exclusion: Sibling directional focus graphs decide where focus moves spatially; this skill decides what a remote command means and how navigation depth behaves.
Failure class: Characteristic Failure includes Back exiting the app from a modal, Select triggering different semantic actions in visually similar cards, inaccessible actions requiring colored or platform-specific buttons, key-repeat causing focus to skip unpredictably, and button hints that show keyboard keys on a TV.
Falsifier: Remove optional buttons from the simulated remote, hold directional keys, nest overlays, navigate deeply, and attempt every critical task with only the minimal command set.
Output: `remote-control-navigation-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling directional focus graphs decide where focus moves spatially; this skill decides what a remote command means and how navigation depth behaves.

### `designing-controller-disconnect-recovery`
Parent: `routing-ui-work`
Trigger: Use when a gamepad, remote, or other primary controller can disconnect during navigation or gameplay and the UI must preserve focus, pause or protect unsafe actions, identify the missing device, and recover cleanly when control returns.
Decision owned: This skill owns the UI state transition from connected control to degraded/no-control state and back.
Sibling exclusion: Sibling gameplay-to-menu handoff owns intentional mode transitions; this skill owns unplanned loss of the control channel.
Failure class: A controller disappearing mid-action can strand focus, leave a held input logically active, or let gameplay continue while the user has no control.
Falsifier: Disconnect during every high-risk phase, reconnect a different device, reconnect while another player is active, and send noisy duplicate connection events.
Output: `controller-disconnect-recovery-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling gameplay-to-menu handoff owns intentional mode transitions; this skill owns unplanned loss of the control channel.

### `designing-input-device-prompt-switching`
Parent: `routing-ui-work`
Trigger: Use when keyboard, mouse, touch, gamepad, remote, or other input devices can alternate during one session and the interface must switch button glyphs, hints, control legends, and affordances without flicker, stale prompts, or misleading capability assumptions.
Decision owned: This skill owns how the product infers the active prompt family and when visible legends should update.
Sibling exclusion: Sibling controller remapping owns what action a button performs; this skill reflects that mapping in prompts as the active device changes.
Failure class: Characteristic Failure includes glyph flicker between keyboard and gamepad, stale prompts after a device switch, showing Xbox-style labels for an unknown layout, touch users seeing hover-only instructions, remapped controls still displaying defaults, and one player’s input changing another player’s legends.
Falsifier: Inject noisy interleaved events, swap controller type, enable a custom mapping, switch from touch to keyboard without pointer movement, and connect two players.
Output: `input-device-prompt-switching-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling controller remapping owns what action a button performs; this skill reflects that mapping in prompts as the active device changes.

### `designing-controller-remapping-surfaces`
Parent: `routing-ui-work`
Trigger: Use when users can customize controller bindings and the interface must prevent unreachable command sets, expose conflicts and reserved inputs, support multiple devices/layouts, and preserve accessibility and recovery paths after remapping.
Decision owned: This skill owns how remapping is captured, validated, previewed, conflicted, restored, and persisted.
Sibling exclusion: Sibling prompt switching reflects the current mapping but does not validate it.
Failure class: Characteristic Failure includes allowing the user to unbind Back with no reset path, detecting conflicts only by button name, input capture that binds stick drift, prompts that ignore custom bindings, per-player maps leaking across accounts, and settings that persist an invalid partial update after a crash.
Falsifier: Try to remove every essential command, create context-overlapping conflicts, bind reserved controls, disconnect during capture, and reload after a partially written map.
Output: `controller-remapping-surfaces-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling prompt switching reflects the current mapping but does not validate it.

### `designing-multiplayer-ui-focus-ownership`
Parent: `routing-ui-work`
Trigger: Use when multiple local players or controllers can interact with menus, lobbies, inventories, split-screen overlays, or shared dialogs and the UI must decide who owns focus, which surfaces are private or shared, and how simultaneous input is arbitrated.
Decision owned: This skill owns the authority model that assigns focus and command ownership across players and shared UI regions.
Sibling exclusion: Sibling split-screen safe-region design owns geometry, not interaction authority.
Failure class: Characteristic Failure includes controller races deciding shared settings unpredictably, one player stealing another’s private focus, shared confirmation triggered by the wrong player, focus indicators distinguished only by similar colors, and owner disconnect leaving a modal permanently locked.
Falsifier: Generate simultaneous events with reversed ordering, reassign controllers, disconnect the owner, add a new player mid-dialog, and open/close shared overlays repeatedly.
Output: `multiplayer-ui-focus-ownership-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling split-screen safe-region design owns geometry, not interaction authority.

### `designing-ten-foot-readable-density`
Parent: `routing-ui-work`
Trigger: Use when an interface is viewed from couch or room distance and must balance readable type, focus clarity, information density, overscan/safe areas, content hierarchy, and navigation efficiency without simply scaling a desktop layout up.
Decision owned: This skill owns the density decisions that determine what remains visible, what is deferred, and what size/spacing is required for reliable recognition at distance.
Sibling exclusion: Sibling HUD priority owns in-game information under active play pressure; this skill owns room-distance readability across menus and surfaces.
Failure class: Characteristic Failure includes desktop-density menus with tiny metadata, critical status encoded in small badges, giant type causing excessive wrapping and navigation, focus rings too subtle at distance, captions colliding with controls, and content touching unsafe display edges.
Falsifier: Increase viewing distance, reduce display size within support bounds, add long localized labels, activate captions/system overlays, and populate the densest realistic content state.
Output: `ten-foot-readable-density-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling HUD priority owns in-game information under active play pressure; this skill owns room-distance readability across menus and surfaces.

### `designing-game-hud-information-priority`
Parent: `routing-ui-work`
Trigger: Use when an active gameplay HUD must decide which status, threat, objective, resource, party, cooldown, navigation, and system information stays persistently visible versus appearing contextually so the UI supports play without consuming attention needed for the game world.
Decision owned: This skill owns the priority model that decides what information is persistent, contextual, glanceable, alert-driven, or deferred to menus.
Sibling exclusion: Sibling instrument-cluster priority serves automotive driving constraints, not game-world attention.
Failure class: Characteristic Failure includes always-on telemetry with no decision value, critical alerts hidden among routine notifications, HUD panels obscuring enemies or navigation, mode changes moving familiar information constantly, and cooldown/resource indicators too subtle to scan under pressure.
Falsifier: Trigger several alerts simultaneously, enter dense combat, switch modes quickly, reduce health/resources to critical thresholds, and test with color-vision variation plus reduced audio.
Output: `game-hud-information-priority-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling instrument-cluster priority serves automotive driving constraints, not game-world attention.

### `designing-pause-and-game-state-overlays`
Parent: `routing-ui-work`
Trigger: Use when gameplay can be paused, suspended, spectated, failed, disconnected, or interrupted by system/game-state overlays and the UI must preserve input ownership, world-state truth, resume conditions, multiplayer constraints, and safe transitions back to play.
Decision owned: This skill owns the relationship between overlay state and underlying game-state truth.
Sibling exclusion: Sibling game HUD priority governs information during active play; this skill governs temporary/terminal overlays and their relationship to play state.
Failure class: Characteristic Failure includes calling a continuing online match paused, stuck movement after closing a menu, confirm-to-close immediately firing an attack, overlay state that hides critical continuing timers, one player blocking all split-screen users unexpectedly, and resume returning to stale camera or HUD state.
Falsifier: Open and close overlays at high input rate, disconnect/reconnect while paused, switch from pause to terminal state, and test online/nonpausing modes.
Output: `pause-and-game-state-overlays-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling game HUD priority governs information during active play; this skill governs temporary/terminal overlays and their relationship to play state.

### `designing-split-screen-safe-interface-regions`
Parent: `routing-ui-work`
Trigger: Use when multiple local players share one display and each viewport needs safe HUD, menu, notification, subtitle, and focus regions that remain legible across horizontal/vertical splits, aspect changes, shared overlays, and platform safe-area constraints.
Decision owned: This skill owns the geometry contract for player-local and shared interface regions.
Sibling exclusion: Sibling multiplayer focus ownership governs who can act; this skill governs where each player’s UI can safely appear.
Failure class: Characteristic Failure includes full-screen HUD scaled until unreadable, player-one notifications covering player-two world view, subtitles clipped by split boundaries, global dialogs obscuring critical content unnecessarily, safe areas computed from full screen instead of player viewport, and focus indicators appearing in the wrong pane.
Falsifier: Switch between one/two/three/four players, alternate horizontal and vertical split, activate captions and high-notification load, open a shared modal, and resize/aspect-change the display.
Output: `split-screen-safe-interface-regions-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling multiplayer focus ownership governs who can act; this skill governs where each player’s UI can safely appear.

### `designing-game-menu-stack-recovery`
Parent: `routing-ui-work`
Trigger: Use when nested game menus, overlays, settings, inventories, dialogs, or platform interruptions can leave navigation history corrupted and the UI needs a deterministic way to reconstruct a valid stack, restore focus, and preserve unsaved state without trapping the player.
Decision owned: This skill owns recovery of the menu navigation stack when its recorded hierarchy no longer matches valid UI state.
Sibling exclusion: Sibling gameplay-to-menu handoff governs normal transitions between play and menu input.
Failure class: Characteristic Failure includes Back reopening a stale modal, blank screens after a route vanishes, focus returning behind an overlay, unsaved settings silently discarded, duplicate frames after rapid open/close, and a player-private menu recovered under the wrong player.
Falsifier: Invalidate the current frame and its parent, remove the prior focus target, interrupt with a platform overlay, and trigger async route closure while Back is pressed repeatedly.
Output: `game-menu-stack-recovery-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling gameplay-to-menu handoff governs normal transitions between play and menu input.

### `designing-gameplay-to-menu-input-handoffs`
Parent: `routing-ui-work`
Trigger: Use when controls transition between gameplay and menus and the interface must transfer input ownership, clear held commands, establish focus, suppress accidental activation, preserve camera/player state, and return control without leaking one mode's input semantics into the other.
Decision owned: This skill owns that handoff and the conditions under which input from one mode may begin affecting the other.
Sibling exclusion: Sibling pause overlays decide what the game world does while UI is visible; this skill decides what the input device does at the boundary.
Failure class: Characteristic Failure includes opening a menu and instantly selecting an item, closing a menu and firing a weapon, character drift caused by held analog input, gameplay shortcuts activating behind a modal, focus not established before navigation events arrive, and one player’s menu stealing another player’s controls.
Falsifier: Press and hold the transition button, move sticks through the boundary, remap confirm to a gameplay action, spam open/close, and interrupt with another overlay.
Output: `gameplay-to-menu-input-handoffs-contract`
Evidence role: Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent. Primary pin: `godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce`. Secondary: Qt/Qt Quick control/focus mechanisms (corroboration).
Delete-the-skill: Sibling pause overlays decide what the game world does while UI is visible; this skill decides what the input device does at the boundary.

### `designing-driving-state-interaction-lockouts`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an automotive interface must enable, simplify, defer, or block interactions according to driving state, vehicle motion, task demand, legal/platform constraints, or driver role while preserving clear recovery paths and essential controls.
Decision owned: This skill owns the interface contract that decides which actions are available in each authoritative driving state and how unavailable actions are explained.
Sibling exclusion: Sibling vehicle-state-dependent controls governs controls whose semantics/value change with vehicle state; this skill governs whether an interaction may occur at all.
Failure class: Characteristic Failure includes checking driving state only when the screen opens, hiding essential controls with a blanket lockout, using stale speed/gear state, allowing a focused action to execute after motion begins, losing user input when a task becomes blocked, and replacing one high-demand interaction with an equally demanding alternative.
Falsifier: Change driving state at the moment of activation, inject stale/unknown signals, switch driver/passenger role, and resume a partially completed task after returning to a permissive state.
Output: `driving-state-interaction-lockouts-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling vehicle-state-dependent controls governs controls whose semantics/value change with vehicle state; this skill governs whether an interaction may occur at all.

### `designing-vehicle-warning-priority-surfaces`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an automotive interface must present simultaneous warnings, faults, advisories, confirmations, and status changes with different urgency and required driver response without allowing routine notifications to obscure time-critical vehicle information.
Decision owned: This skill owns the priority model that decides what interrupts, what persists, what is queued, and what can be summarized so the driver receives the right information at the right time.
Sibling exclusion: Sibling instrument-cluster priority governs the complete information hierarchy of the cluster; this skill specifically owns competing warning urgency and interruption.
Failure class: Characteristic Failure includes routine notifications covering critical warnings, identical styling for unrelated urgency levels, warnings disappearing on acknowledgement while the condition remains, alert fatigue from repeating unchanged faults, color-only severity, and queued urgent warnings waiting behind older low-priority messages.
Falsifier: Inject several warnings in different orders, escalate one existing condition, fail an audio/haptic channel, acknowledge without clearing the fault, and activate unrelated infotainment notifications.
Output: `vehicle-warning-priority-surfaces-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling instrument-cluster priority governs the complete information hierarchy of the cluster; this skill specifically owns competing warning urgency and interruption.

### `designing-driver-distraction-aware-information-density`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an automotive interface must adapt information volume, glance demand, interaction depth, and visual complexity to driving workload so important content remains comprehensible without treating every screen as a parked-state dashboard.
Decision owned: This skill owns how much information is visible, how deeply it can be interacted with, and what is deferred or summarized according to driver role and driving workload.
Sibling exclusion: Sibling instrument-cluster priority owns the cluster’s safety-critical information hierarchy; this skill owns broader driver-facing density across infotainment and task surfaces.
Failure class: Characteristic Failure includes copying a tablet dashboard into the center stack, shrinking text to retain every field, hiding critical context alongside low-priority detail, several independent notification systems competing simultaneously, and dynamic layout changes that force the driver to relearn where status appears.
Falsifier: Populate the maximum realistic data set, trigger navigation and vehicle notifications together, switch from parked to moving mid-task, and test at representative glance durations.
Output: `driver-distraction-aware-information-density-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling instrument-cluster priority owns the cluster’s safety-critical information hierarchy; this skill owns broader driver-facing density across infotainment and task surfaces.

### `designing-rotary-controller-focus-navigation`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an automotive HMI is navigated with a rotary controller, knob, touchpad-dial hybrid, or detented hardware and focus movement must map rotation, push, tilt, back, acceleration, and region transitions into predictable low-glance interaction.
Decision owned: This skill owns how rotation and associated hardware commands move focus, enter regions, activate controls, and accelerate through long collections.
Sibling exclusion: Sibling directional focus graphs serve general D-pad/remote geometry; rotary navigation owns ordered detent semantics and value-edit mode.
Failure class: Characteristic Failure includes rotation scrolling while focus stays offscreen, accidental value changes during navigation, skipped/duplicated detents, acceleration outrunning visible context, focus trapped in disabled regions, and inconsistent Back/press behavior across similar controls.
Falsifier: Rotate rapidly and slowly, reverse direction, enter/exit value edit repeatedly, disable intermediate controls, change layout mode, and transition driving state while the controller is active.
Output: `rotary-controller-focus-navigation-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling directional focus graphs serve general D-pad/remote geometry; rotary navigation owns ordered detent semantics and value-edit mode.

### `designing-instrument-cluster-information-priority`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an instrument cluster must arbitrate persistent vehicle state, speed, telltales, warnings, driver-assistance status, navigation, energy/fuel, and contextual information so critical state remains stable and legible under competing demands.
Decision owned: This skill owns the priority architecture that decides which information is persistent, which can temporarily expand, and which must never be displaced.
Sibling exclusion: Sibling vehicle-warning priority owns the urgency and lifecycle of warnings; this skill owns the entire cluster hierarchy into which warnings enter.
Failure class: Characteristic Failure includes navigation cards displacing required status, different drive modes moving critical values unpredictably, personalization hiding telltales, several warnings competing without hierarchy, transient media content covering automation-state indicators, and decorative animation drawing attention from operational state.
Falsifier: Activate several optional features, switch modes, trigger urgent warnings, change personalization, and transition assistance/automation state rapidly.
Output: `instrument-cluster-information-priority-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling vehicle-warning priority owns the urgency and lifecycle of warnings; this skill owns the entire cluster hierarchy into which warnings enter.

### `designing-driver-passenger-authority-splits`
Parent: `designing-high-stakes-decisions`
Trigger: Use when the same vehicle system exposes different controls, content, permissions, or interaction depth to driver and passenger surfaces and the UI must preserve role authority as occupants, seats, devices, and driving state change.
Decision owned: This skill owns the authority model that separates driver-facing and passenger-facing interaction without assuming that every screen, touch, or device belongs to the same principal.
Sibling exclusion: Sibling driving-state lockouts decide whether driver actions are available under motion/workload.
Failure class: Characteristic Failure includes passenger presence unlocking a shared driver screen, driver inheriting a passenger’s high-demand task while moving, sensitive passenger data mirrored globally, stale passenger privileges after seat change, and shared settings modified with no visible ownership.
Falsifier: Change occupant role, remove actor identity, transfer an active task between surfaces, switch profiles, and alter driving state during handoff.
Output: `driver-passenger-authority-splits-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling driving-state lockouts decide whether driver actions are available under motion/workload.

### `designing-vehicle-state-dependent-controls`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an automotive control’s meaning, valid range, availability, feedback, or consequence changes with vehicle state and the UI must bind the control to authoritative state so stale or visually similar controls cannot issue the wrong action.
Decision owned: This skill owns the semantic binding between authoritative vehicle state and control behavior.
Sibling exclusion: Sibling driving-state lockouts govern whether a class of interaction is allowed; this skill governs controls that remain visible but whose semantics depend on vehicle state.
Failure class: Characteristic Failure includes showing a toggle as on because a command was sent but the vehicle rejected it, retaining a valid-looking control after its precondition disappeared, reusing the same label for materially different mode semantics, retrying commands after state changed, and stale cached state enabling an unavailable action.
Falsifier: Change vehicle state immediately before activation, reject a command after optimistic feedback, mutate the same setting through a physical control, and enter a subsystem fault.
Output: `vehicle-state-dependent-controls-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling driving-state lockouts govern whether a class of interaction is allowed; this skill governs controls that remain visible but whose semantics depend on vehicle state.

### `designing-automotive-modality-fallbacks`
Parent: `designing-high-stakes-decisions`
Trigger: Use when an automotive task can use touch, rotary, steering-wheel controls, voice, physical switches, audio, haptics, or display channels and the UI must provide safe fallback when one modality is unavailable, unreliable, inappropriate, or restricted by driving state.
Decision owned: This skill owns the fallback hierarchy that preserves essential task capability without pretending one modality can always substitute for another.
Sibling exclusion: Sibling vehicle-state-dependent controls own semantic changes in a control; this skill owns continuity when an entire interaction or feedback channel is unavailable.
Failure class: Characteristic Failure includes treating voice as a universal safe substitute, fallback commands with no feedback channel, essential tasks becoming unreachable after one display fails, touch-only recovery from touch failure, passenger-private content read aloud during voice fallback, and degraded mode continuing a task whose demand is no longer appropriate.
Falsifier: Disable each primary modality in turn, combine two failures, add cabin noise, change driving state mid-task, and test privacy-sensitive content with passengers present.
Output: `automotive-modality-fallbacks-contract`
Evidence role: Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples. Primary pin: `Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)`. Secondary: godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only.
Delete-the-skill: Sibling vehicle-state-dependent controls own semantic changes in a control; this skill owns continuity when an entire interaction or feedback channel is unavailable.

### `designing-cross-device-session-handoffs`
Parent: `routing-ui-work`
Trigger: Use when a user intentionally moves an active task from one device or surface to another and the product must transfer session identity, task position, authority, privacy context, pending operations, and recovery state without duplicating or losing work.
Decision owned: This skill owns the explicit transfer contract that moves an active session from source to destination while preserving one coherent task identity.
Sibling exclusion: Sibling notification-to-app continuation starts from an asynchronous notification rather than an explicit live transfer.
Failure class: Characteristic Failure includes opening a stale snapshot on the new device, duplicate background operations, source and destination both believing they are sole owner, sensitive data appearing on an inappropriate surface, and lost drafts when the source closes too early.
Falsifier: Interrupt transfer at every phase, reject authentication on destination, mutate task state during handoff, and complete a pending operation while ownership changes.
Output: `cross-device-session-handoffs-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Sibling notification-to-app continuation starts from an asynchronous notification rather than an explicit live transfer.

### `designing-companion-surface-authority`
Parent: `routing-ui-work`
Trigger: Use when a secondary device or companion surface can view, propose, or control state belonging to a primary product and the UI must define which surface is authoritative for each action, how conflicts are surfaced, and what happens when the primary is unavailable.
Decision owned: This skill owns the authority partition between primary and companion surfaces rather than assuming one global master device.
Sibling exclusion: Sibling second-screen control continuity owns uninterrupted control as users move between cooperating surfaces; this skill decides which surface is allowed to control each domain action in the first place.
Failure class: Characteristic Failure includes both surfaces believing they are canonical, a companion showing successful state before the primary/backend accepts it, controls remaining active after authority is lost, privacy-sensitive details mirrored solely because control permission exists, and a supposedly subordinate surface silently overriding the primary.
Falsifier: Disconnect the primary, swap principals, send conflicting commands, revoke companion capability, and delay authoritative acknowledgement.
Output: `companion-surface-authority-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Sibling second-screen control continuity owns uninterrupted control as users move between cooperating surfaces; this skill decides which surface is allowed to control each domain action in the first place.

### `designing-second-screen-control-continuity`
Parent: `routing-ui-work`
Trigger: Use when control of a shared experience can move between a primary display and one or more second screens and the interface must preserve command state, selection, queue position, ownership, latency feedback, and current context while users switch where they control it.
Decision owned: Companion authority determines which surface may act; this skill owns continuity once authority exists.
Sibling exclusion: Sibling cross-device session handoff moves an entire active task/session; this skill keeps control of one shared target coherent while presentation may remain distributed.
Failure class: Characteristic Failure includes second screens showing different current selections, commands applied in stale order, a new controller replaying old queued actions, private control context leaking to the shared display, and ownership switching with no indication.
Falsifier: Add network delay and reordering, switch controlling surfaces during a pending action, disconnect/reconnect a second screen, and issue conflicting commands from two authorized surfaces.
Output: `second-screen-control-continuity-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Sibling cross-device session handoff moves an entire active task/session; this skill keeps control of one shared target coherent while presentation may remain distributed.

### `designing-notification-to-app-continuation`
Parent: `routing-ui-work`
Trigger: Use when a notification, wearable alert, email deep link, or operating-system surface must continue into an application without losing task identity, authorization state, or the user's place in the work.
Decision owned: This skill owns the decision about how an external alert becomes a trustworthy in-app continuation rather than merely which route opens.
Sibling exclusion: Cross-device session handoff owns transfer of an active session between peer surfaces.
Failure class: Characteristic Failure includes opening the right object under the wrong identity, acting on stale notification copy, landing on a generic home screen after a failed lookup, dropping an unsent reply that began from an alert, or allowing duplicate execution because the notification remains actionable after the server state changed.
Falsifier: Falsification deliberately changes reality between notification issue and tap.
Output: `notification-to-app-continuation-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Cross-device session handoff owns transfer of an active session between peer surfaces.

### `designing-cross-device-capability-negotiation`
Parent: `routing-ui-work`
Trigger: Use when a task can move among devices or surfaces whose input, output, security, connectivity, sensor, or execution capabilities differ and the UI must negotiate what remains possible without lying about equivalence.
Decision owned: This skill owns the Decision that maps a task requirement set against device capabilities and chooses full transfer, degraded transfer, delegated action, deferred action, or refusal.
Sibling exclusion: Session handoff owns the movement of an active session.
Failure class: Failure appears when a transferred task reaches a dead-end control that the destination can never satisfy, when a weaker device silently skips required verification, when the UI shows an action that depends on an absent sensor, or when a capability is inferred from form factor instead of detected state.
Falsifier: Falsification removes or mutates one capability at a time: disconnect the camera, deny microphone permission, remove the hardware keyboard, disable secure authentication, drop network transport, revoke background execution, or switch to a device with a different controller model.
Output: `cross-device-capability-negotiation-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Delete-the-skill test: without this owner, multi-device flows can still transfer identifiers and UI state, but there is no canonical decision point that compares task requirements against destination capabilities.

### `preserving-task-state-across-device-switches`
Parent: `routing-ui-work`
Trigger: Use when a user moves an in-progress task between devices and the product must preserve meaningful work state, provenance, progress, and recoverability without serializing every transient UI detail.
Decision owned: This skill owns the Decision about which state is semantically necessary for the task to remain continuous and which state must be recomputed, discarded, or explicitly re-confirmed.
Sibling exclusion: This skill does not decide which surface may act, whether the destination has required capabilities, or how simultaneous edits are merged.
Failure class: Characteristic Failure includes copying too little and dropping drafts, copying too much and reviving stale presentation state, replaying a side effect from serialized execution state, restoring a wizard step whose prerequisites are no longer true, or hiding a conflict by overwriting the destination's fresher server read.
Falsifier: Falsification switches devices at adversarial moments: immediately before submit, during upload, after local draft change but before sync, after another actor changes the object, while a step-specific permission is revoked, and after the source device goes offline.
Output: `task-state-across-device-switches-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Delete-the-skill test: if this owner is removed, session transfer can still move credentials or routes, but no one defines the semantic checkpoint that distinguishes durable task meaning from ephemeral UI implementation.

### `resolving-cross-device-state-conflicts`
Parent: `routing-ui-work`
Trigger: Use when the same task, object, or draft can be changed from more than one device and the UI must detect, explain, and resolve divergent state without silent last-write-wins corruption.
Decision owned: This skill owns the Decision that classifies divergence and chooses automatic merge, authoritative refresh, user-assisted reconciliation, operation invalidation, or hard conflict blocking.
Sibling exclusion: Session handoff moves control; companion authority decides who may control; task-state preservation reconstructs a single continuation.
Failure class: Characteristic Failure includes silent overwrite, duplicated side effects, presenting a merged document that never actually existed on the server, letting a stale device submit against an invalid base, losing attachments or annotations during a field-level merge, or offering “keep mine / keep theirs” when a more precise semantic merge exists.
Falsifier: Falsification intentionally creates divergent revisions under clock skew, offline queues, delayed sync, partial network failure, and repeated reconnect.
Output: `cross-device-state-conflicts-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Session handoff moves control; companion authority decides who may control; task-state preservation reconstructs a single continuation.

### `designing-device-proximity-handoff-cues`
Parent: `routing-ui-work`
Trigger: Use when nearby-device discovery, proximity, presence, or physical co-location can trigger or suggest a task handoff and the UI must communicate readiness, destination identity, consent, and transfer state without accidental switching.
Decision owned: This skill owns the Decision about when proximity is strong enough to surface a handoff cue, what that cue must disclose, and when a suggestion may advance to an explicit transfer request.
Sibling exclusion: Notification continuation begins from an asynchronous alert, not physical presence.
Failure class: Characteristic Failure includes transferring to the wrong nearby device, presenting raw hardware identifiers that users cannot distinguish, prompting continuously as signal strength oscillates, treating discovery as consent, exposing task contents before the destination is trusted, or declaring success when only transport initiation occurred.
Falsifier: Falsification moves devices across discovery thresholds, introduces two same-type devices, locks and unlocks the destination, disables its required capability, changes the signed-in user, and breaks proximity immediately after confirmation.
Output: `device-proximity-handoff-cues-contract`
Evidence role: Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification. Primary pin: `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2`. Secondary: expo/expo@5a97a546476fd0bea35227b60297ad472f065168.
Delete-the-skill: Delete-the-skill test: without this owner, transfer protocols can still discover peers and move sessions, but no canonical contract governs when proximity is trustworthy enough to surface, how users identify the destination, or what happens when presence oscillates.
