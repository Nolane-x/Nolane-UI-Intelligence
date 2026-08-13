---
name: performing-ui-repository-archaeology
description: Use whenever an external repository may materially influence UI behavior, implementation, motion, visual language, data representation, accessibility, or interaction; converts a repository link into an artifact-level, snapshot-bound research dossier before the source is allowed to influence the product.
---

# Performing UI Repository Archaeology

## Parent Contract
**Required parent:** `researching-ui-implementation-ecosystems`.

Receive canonical source candidate, task profile, source role, intended usage, local product obligations and the upstream ecosystem research decision. The parent still owns discovery and candidate identification; this skill owns artifact-level depth for a chosen candidate.

## Decision Boundary
This faculty owns **how deeply a concrete external UI source must be inspected before it may influence a product decision**. It begins after a source has been discovered and role-classified by `researching-ui-implementation-ecosystems`; it ends before final adoption/adaptation or cross-source synthesis. It does not choose the product aesthetic, does not certify a license, and does not assume that upstream quality survives local integration.

Its central distinction is: **repository existence is not repository understanding**. A README, landing page, screenshot, package description, star count, or generated summary can establish that a source is worth investigating. None can establish the semantics of a component, the interruption behavior of an animation, the accessibility contract of a primitive, the scaling limits of a renderer, the script coverage of a font, or the update risk of a token pipeline.

## Inherited obligations
Receive the task profile, source role, intended use (`adopt | adapt | inspire | build | reject`), visual ambition, risk class, local stack, accessibility contract, product action/state registry, performance budget, licensing constraints, and current registry entry. Parent obligations survive this skill. If the product forbids a dependency, no amount of source quality can waive that constraint. If the product requires keyboard equivalence, an upstream pointer-only demo cannot redefine the requirement.

## Archaeology depth is role-specific
Do not run one generic checklist over every repository. Ask which artifacts can **falsify the reason this source is attractive**.

For an animated component gallery, inspect representative component source, live/demo context, dependency configuration, animation timing/interruption, reduced-motion handling, and performance/accessibility fallbacks. For a headless primitive, inspect implementation plus interaction tests, keyboard/focus ownership, accessibility guidance, and edge-state demos. For a design system, inspect design guidance, component source, tests, token/theme model, accessibility posture, and migration/versioning signals. For iconography, inspect the actual catalog, construction grid/stroke/weight conventions, semantic naming/tags, framework delivery, and license. For typography, inspect script/language coverage, variable axes, weights/styles, font metrics, delivery/subsetting, fallback behavior, and license. For graph editors, maps, code editors, canvas/3D engines, terminal UI, AI-native UI, animation runtimes, data visualization, rich text, data grids, and form engines, use the role-specific artifact classes emitted by `plan_source_research`.

The question is not “did I open enough files?” It is “have I inspected the files that carry the mechanism, assumptions, failure modes and legal/runtime boundaries relevant to this task?”

## Observation protocol
1. Resolve the **canonical source identity**. Confirm repository ownership, current default branch/release posture, archive/deprecation state, and whether documentation refers to the same project/version.
2. Pin a **research snapshot**. For material or high-drift use, record canonical URL, ref/tag, exact commit SHA where available, and retrieval time. Never silently treat `main` as universal; default branches and active development lines differ across projects.
3. Write the **decision question before reading deeply**. Examples: “Can this primitive carry menu semantics while preserving our focus restoration contract?” or “Can this motion mechanism communicate object continuity without requiring a pointer or violating reduced motion?” This prevents aimless repository tourism.
4. Generate the role-specific artifact plan. Every required artifact class gets a reason: what uncertainty can this class reduce, and what decision could it reverse?
5. Inspect **mechanism-bearing artifacts**, not just descriptive prose. Record exact path/URL, what was observed, and an evidence reference. If source and demo disagree, record the contradiction rather than selecting the convenient version.
6. Trace dependencies and hidden coupling. Look for providers, global CSS, implicit DOM structure, browser assumptions, asset pipelines, peer dependencies, runtime services, framework-specific state, environment requirements, and build-time transforms.
7. Inspect failure behavior. Search tests/issues/docs/source for disabled/loading/error states, interruption, keyboard/focus, long content, localization, reduced motion, high contrast, touch/coarse pointer, offline/latency, hydration, concurrency, data volume, and device constraints as applicable.
8. Extract **mechanisms**, not vibes. A mechanism names a causal relationship such as shared-layout continuity, collision-aware placement, virtualized rendering, token transform precedence, semantic icon construction, or state-machine-driven animation. Bind each mechanism to inspected artifact paths.
9. Define the transfer boundary. State what may transfer, what is only inspiration, what must be rebuilt locally, and what must not transfer: demo copy, brand trade dress, source-specific state semantics, global token vocabulary, hidden analytics, or inaccessible interaction assumptions.
10. Record contradictions, hazards, and unread material. “Unread” is not embarrassment; it is uncertainty accounting. Name what remains and why it is unlikely—or likely—to overturn the current decision.
11. Stop only when the stopping reason is causal. “I read enough” is invalid. A valid stop says why the mechanism, dependency surface, critical failure classes, legal posture, and unresolved uncertainty are characterized enough for the next decision.

## Falsification discipline
Repository research must be capable of proving the source **wrong for the task**. Before authorizing influence, name at least one disconfirming observation that would change the decision. Examples: focus is manually trapped in a way incompatible with the local dialog primitive; a visual effect requires a WebGL budget unavailable on target devices; an icon family lacks the domain concepts needed and would force mixed families; variable font axes render poorly in the target script; an animation becomes the sole carrier of state and has no reduced-motion equivalent.

Use counterfactual inspection: if the attractive demo styling were removed, is there still a useful mechanism? If the dependency were replaced with a local primitive, what information or behavior would be lost? If the source name/brand were hidden, would the evidence still justify selection? A source that survives only through aesthetic halo has not passed archaeology.

## Evidence quality ladder
Prefer, in order where applicable: exact source/tests at a pinned snapshot; official docs tied to that implementation; reproducible demo/runtime observation; maintainer migration/accessibility/performance guidance; issue history that reveals known failure modes; secondary explanation only as a lead. Search snippets and AI summaries are discovery evidence, not material authorization.

A repository can be an excellent visual reference and a poor semantic dependency. It can be a strong implementation primitive and a poor visual authority. The dossier must preserve these distinctions.

## Output — `ui-source-research-dossier`
Return a typed dossier containing source identity/role/usage; snapshot; task-fit decision; role-specific required artifact classes; inspected artifacts with path, finding and evidence reference; extracted mechanisms with product-fit and transfer boundaries; contradictions; dependency and integration hazards; license/accessibility/performance evidence or explicit unknowns; unread material; stop reason; and decisions that remain blocked.

No downstream agent may convert an UNKNOWN into a PASS merely because the repository is popular or visually impressive.

## Failure topology
- **README authority inversion:** descriptive claims replace source/test inspection.
- **demo-source mismatch:** agent copies demo behavior that is not the actual reusable contract.
- **version smear:** evidence from different branches/releases is mixed into one imaginary version.
- **aesthetic halo:** visual appeal suppresses accessibility, semantic, licensing or performance objections.
- **role mismatch:** a gallery is treated as semantic authority; a headless primitive as art direction; a chart library as analytical truth.
- **happy-path tunneling:** only default mouse/desktop/English/ideal-data behavior is inspected.
- **dependency blindness:** copied component imports a second design system or runtime architecture.
- **provenance evaporation:** after copying, nobody can identify why the mechanism exists or where it came from.
- **false completeness:** unread critical artifacts are omitted from the dossier rather than represented as uncertainty.

## Recovery
If a required artifact cannot be inspected, downgrade the source to discovery/inspiration, choose a better-evidenced alternative, or mark the decision BLOCKED. If contradictory artifacts materially change the assumed mechanism, re-plan the research rather than averaging the contradiction away. If the repository is archived, renamed, relicensed, or rapidly drifting, reopen source identity/currentness before continuing. If archaeology reveals that the source solves a different problem, return to ecosystem research instead of forcing adaptation.

## Hard gate
**A material external source may not influence implementation or visual direction until role-specific mechanism-bearing artifacts—not README alone—have been inspected at an identifiable snapshot, mechanisms are bound to evidence paths, critical contradictions/hazards are recorded, and a falsifiable stop reason exists.**

## V6 Repository Archaeology Depth Lock
Use an **artifact-depth ladder** from identity/README → docs/API → representative implementation → examples/demo wiring → tests → theme/styles/tokens → accessibility/performance evidence → issues/release/commit context as required by source role. Record **source-tree path proof** for every extracted mechanism so another agent can open the exact artifact.

Pin **commit-snapshot identity** before material extraction. Maintain **implementation-claim trace** from mechanism claim to relevant code/test/demo paths and distinguish observed behavior from inferred behavior. Keep an **unread-material ledger** for plausible but uninspected files/issues and explain why they cannot overturn the current bounded decision.

### Falsification
Ask whether README-only evidence or a changed default branch/commit would still authorize the mechanism. If yes, archaeology is shallow.

### Recovery
Inspect the missing artifact class at a pinned snapshot, revise the mechanism/risks, or downgrade the source to discovery/inspiration only.
