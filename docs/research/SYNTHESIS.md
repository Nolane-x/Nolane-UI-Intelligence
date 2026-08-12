# Research Synthesis: Why NUI Is Not a Mega-Prompt

The strongest UI-agent systems we studied each solve a different failure class. Treating any one of them as a complete answer produces blind spots. NUI therefore separates mechanisms and assigns each to the layer where it can be enforced.

## 1. Generation and verification are different jobs

Aesthetic generation benefits from commitment, taste, coherent art direction, and willingness to take a justified risk. Verification benefits from skepticism, evidence, explicit failure criteria, and refusal to be persuaded by the generator's narrative. Combining both in one unconstrained prompt encourages self-certification.

NUI response: generation faculties produce contracts/artifacts; `challenging-ui-designs` routes fresh critic lenses; critics have `may_modify: false`; `gating-ui-completion` owns the release decision.

## 2. “Design first” is necessary but not sufficient

Visual-target-first workflows prevent arbitrary design-by-coding, but a screenshot cannot encode hidden interaction states, permissions, accessibility semantics, error recovery, localization, or platform behavior.

NUI response: a visual target freezes only the axes it actually specifies. Product truth, task flow, state algebra, accessibility, responsive behavior, and platform adaptation remain explicit obligations.

## 3. Taste databases are useful but can become presets

A structured database can help an agent retrieve palettes, typography, product patterns, and UX heuristics. The failure mode is category determinism: `fintech → dark navy + cards`, `AI → purple gradient`, `premium → serif + cream`.

NUI response: `exploring-aesthetic-directions` constructs a search space from subject semantics, audience, emotional target, trust posture, density, novelty budget, media character, and platform. Product categories can inform retrieval but never select a style by themselves.

## 4. Anti-slop can become another dogma

Lists that ban gradients, cards, glass, pills, or serif faces often improve generic outputs in the short term, then create a recognizable anti-slop house style.

NUI response: `preventing-generic-ui` evaluates `pattern × context × intent × frequency × user impact × justification`. A card that represents a bounded selectable object can be correct; a card around every paragraph can be a hierarchy tax. The verdict depends on function.

## 5. Dense UI requires different taste than marketing UI

Many “beautiful UI” prompts reward whitespace, large type, limited visible controls, and cinematic first viewports. Those choices can be actively harmful in repeated operational work where experts compare many values and build spatial memory.

NUI response: user/task frequency and information throughput are upstream of visual styling. `designing-data-dense-interfaces` protects comparison alignment, spatial memory, selection, live-update stability, bulk scope, and responsive access to critical data.

## 6. State is a first-class design dimension

Static screenshots hide the majority of product behavior. Default/hover/disabled alone is too shallow for real software.

NUI response: component state algebra models interaction, availability, validation, async, content, environment, theme/accessibility, and locale dimensions. Only material cross-products are required; the goal is coverage, not combinatorial paperwork.

## 7. Accessibility cannot be a final lint pass

Automated tooling is excellent at machine-detectable violations but cannot prove label meaning, focus quality, task comprehension, every screen-reader interaction, or the full normative standard.

NUI response: accessibility obligations exist at design-time, component-time, and runtime. Automated findings are evidence scoped to what the tool tests. Exact conformance claims require exact normative source and adequate runtime/manual evidence.

## 8. Platform universality requires semantic portability, not pixel parity

A universal skill that says “always use this web pattern” is not universal. Conversely, completely separate platform skills lose product-system coherence.

NUI response: preserve product invariants and semantic token/component intent; adapt navigation, input, safe areas, system controls, typography, focus, accessibility APIs, and presentation where authoritative platform behavior differs.

## 9. The router is part of intelligence

A catalogue with many excellent skills still fails if the agent loads everything or picks by keyword. Context dilution weakens compliance; keyword matching confuses surface labels with failure modes.

NUI response: `routing-ui-work` first builds a typed task profile covering intent, product surface, users/task pressure, information, interaction, visual freedom, constraints, and available evidence capabilities. It then selects the minimum sufficient faculties and records why plausible faculties are inactive.

## 10. Deterministic facts should not depend on persuasion

LLMs can rationalize missing evidence, broken parent relationships, incomplete state lists, or a test they expect to pass.

NUI response: the Python kernel validates graph completeness/acyclicity, skill metadata, required state accounting, token tiers/alias cycles, completion packet status, unresolved findings, evidence results, and bounded claims. It intentionally does **not** attempt to numerically score beauty.

## Core synthesis

NUI's central design is a division of responsibility:

- **Kernel:** authority, lifecycle, routing, obligations, evidence, adversary, recovery, completion.
- **Faculties:** product, architecture, interaction, visual craft, systems, platform, inclusion, specialist surfaces.
- **Critics:** independent failure discovery.
- **Deterministic validator:** machine-checkable invariants.
- **Adapters:** capability mapping without changing core policy.
- **Evals:** pressure scenarios that tempt known agent failure modes.

This is intentionally harder to bypass than a single long instruction file while remaining inspectable and portable.
