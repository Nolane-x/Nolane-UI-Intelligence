---
name: synthesizing-cross-source-ui-language
description: Use when two or more external UI sources materially influence one product; assigns authority by layer and synthesizes mechanisms into one local semantic, interaction and visual language instead of producing library collage.
---

# Synthesizing Cross-Source UI Language

## Parent Contract
**Required parent:** `selecting-ui-building-blocks`.

Receive two or more selected, researched external mechanisms plus local action/state/accessibility/token/visual contracts. The parent still owns which building blocks are selected; this skill owns coherence and authority across the selected set.

## Decision Boundary
This faculty owns the **coherence problem created by multiple strong sources**. It does not discover repositories and does not replace their task-specific archaeology. It receives researched mechanisms and decides which source, if any, may influence each layer while keeping local product semantics as final authority.

A product assembled from individually excellent libraries can still be poor: one dialog follows Radix focus assumptions, one animated card invents a second state model, a chart uses a third palette, a canvas introduces unrelated gestures, and a notification library brings different spacing/radius/icon conventions. “All components are high quality” does not imply the combined UI has a language.

## Local system first
Before assigning external ownership, identify the local authorities: action registry, state model, information architecture, accessibility contract, token system, visual thesis, typography, icon grammar, motion grammar, content language, responsive policy, performance budget, and provenance/license ledger. Missing local authority is not permission for the first library to become the de facto system. It is a design-system gap that must be resolved.

## Layer ownership model
Partition influence into at least semantics, interaction, visual expression, and—when material—motion, data encoding, content, icons, typography, rendering, or platform behavior. For each layer declare exactly who owns the default and what the local override is.

Semantic ownership includes product action meaning, roles, names, focus purpose, state meaning and accessibility semantics. Interaction ownership includes state transitions, keyboard/pointer/touch/gesture behavior, interruption and recovery. Visual ownership includes tokens, hierarchy, typography, color, surface, density, iconography and media. Motion ownership includes information purpose, timing grammar, interruption and reduced-motion alternative. Data encoding ownership is always subordinate to analytical truth and encoding provenance.

An external source can be the implementation owner of a layer without being its product authority. A headless primitive can supply menu mechanics while local actions/names and accessibility expectations still govern. A motion gallery can supply a continuity mechanism while local motion grammar controls timing and reduced motion.

## Synthesis procedure
1. Build a **source-mechanism matrix**. Rows are researched sources; columns are mechanisms/layers. Record evidence strength, product fit, conflicts, dependency cost, accessibility posture, performance risk, visual specificity and exit cost.
2. Identify overlaps. If two sources solve the same layer, do not blend them by default. Compare mechanism strength and choose one primary route or define a narrow boundary where both are necessary.
3. Identify gaps. If no source owns a required layer, declare it local rather than importing a random source merely for completeness.
4. Resolve semantic conflicts before visual conflicts. A beautiful transition never overrides canonical action meaning, focus ownership, destructive confirmation, provenance, or safety.
5. Normalize state. Map each retained external mechanism onto local component/screen states. Remove source states with no product meaning and add local error/loading/permission/offline/interrupted/recovery states omitted by demos.
6. Normalize content and localization. Replace placeholder/demo language; stress long labels, scripts, dates, numbers and domain terminology. Geometry that only works with demo copy is not synthesized.
7. Normalize visual grammar. Decide which radius, border, elevation, shadow, color, typography, icon and density relationships are product rules. External literal values become mapped tokens or are discarded.
8. Normalize motion and gesture. Retain information purpose, not spectacle. Resolve gesture ownership, interruption, focus continuity, reduced motion and low-performance fallbacks.
9. Normalize responsive/platform behavior. A desktop source and a mobile source may encode different assumptions. Define how the local product translates rather than allowing two unrelated breakpoint philosophies.
10. Remove foreign defaults and hidden coupling. Keep an explicit list so reviewers can see that demo labels, palettes, global CSS, providers, analytics, assets and brand-specific composition did not silently survive.
11. Resolve every known source-to-source conflict. “Both are good” is not a resolution. State the winning authority and why.
12. Produce an integration verification matrix: semantics, keyboard/focus, touch/gesture, accessibility tree, content stress, visual coherence, motion, performance, dependency isolation, and update/provenance checks.

## Coherence tests and falsification
Use **source removal**: temporarily remove one source’s visual defaults while preserving its underlying mechanism. If the product becomes more coherent with no loss of capability, that source had excess visual authority. Use **blind provenance review**: can a critic infer where library boundaries are from radii, spacing, motion, copy or focus behavior? If yes, synthesis is incomplete.

Use **cross-source substitution**: replace one source mechanism with a local equivalent. If the product’s identity disappears, ask whether the source is carrying product-specific value or merely borrowed identity. If the source is the only reason the UI feels distinctive, deepen the local signature before release.

Use **conflict injection**: test long localized content, reduced motion, high contrast, keyboard-only interaction, error states and constrained viewports across component boundaries. Collage often appears first at boundaries rather than in isolated demos.

## Evidence
Require archaeology dossiers for every material source. Bind each ownership decision to mechanism evidence and product constraints. Visual coherence requires rendered cross-surface evidence, not token mappings alone. Interaction coherence requires state/input traces across boundaries. Accessibility coherence requires local verification because upstream claims do not compose automatically.

## Output — `ui-cross-source-synthesis`
Return sources; layer ownership with local override for every layer; source-mechanism matrix; conflict resolutions; local authorities; state/content/token/motion/responsive mappings; foreign defaults removed; dependency boundaries; provenance obligations; unresolved conflicts; and cross-source runtime/render verification obligations.

## Failure topology
- **component archipelago:** each region is polished but follows a different language.
- **semantic split-brain:** duplicate controls perform conceptually similar actions with different states/labels/focus behavior.
- **token laundering:** external literal values are renamed as local tokens without reconciling their relationships.
- **motion dialect collision:** unrelated easings, timing, gesture physics and transition purposes coexist.
- **brand borrowing:** product distinctiveness comes primarily from recognizable upstream trade dress.
- **a11y composition fallacy:** individually accessible primitives become inaccessible when wrapped/animated/composed.
- **dependency sovereignty:** a third-party provider/global CSS forces architecture beyond its intended layer.
- **lowest-common-denominator synthesis:** all sources are stripped until the UI is generic; coherence is achieved by timidity rather than authorship.

## Recovery
When conflicts cannot be resolved locally, reduce the source count, replace one source with a more compatible mechanism, or build the conflicted layer locally. When coherence requires suppressing every distinctive feature, return to visual direction/signature work rather than accepting genericity. When semantic authority is unclear, return to product action/state contracts before continuing visual integration.

## Hard gate
**Multi-source material UI work cannot release until semantics, interaction and visual layers have explicit ownership, every external layer declares a local override, known conflicts are resolved, foreign defaults are enumerated/removed, and rendered/runtime evidence shows one product language rather than visible library boundaries.**

## V6 Cross-Source Synthesis Protocol
Create a **layer-authority matrix** assigning semantics, interaction, visual language, motion, data visualization, icons, content, and accessibility to local ownership and bounded source influence. Record a **cross-source conflict graph** for incompatible state models, tokens, keyboard behavior, animation dialects, or visual signatures.

Perform **local-language normalization** so imported mechanisms use one local vocabulary, tokens, states, focus, error/recovery, density, and responsive rules. Run a **source-removal test**: if one upstream reference/library disappears, the product should retain coherent identity/semantics or have a defined replacement. Issue a **synthesis-coherence verdict** based on whether the result feels/behaves like one product rather than recognizable source fragments.

### Falsification
Blind reviewers to provenance and remove one source's styling. If they can still identify conflicting library dialects or the system loses key semantics, synthesis fails.

### Recovery
Reduce source count, assign one local authority for disputed layers, normalize primitives/tokens, and regenerate affected surfaces.
