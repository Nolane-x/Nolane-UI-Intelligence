# Research Synthesis: From UI Skill to UI Cognition System

The strongest UI-agent systems and UI standards solve different failure classes. Treating any one source as a complete answer creates blind spots. NUI therefore decomposes the field into decision owners, evidence contracts, independent critics, deterministic gates, and a research layer that can reopen when authority changes.

The v2 research snapshot expands that synthesis beyond conventional web/app design into human factors, modalities, AI/agents, accessibility specialists, robotics, ambient systems, BCI, control rooms, flight decks, media accessibility, AAC, avatars, affective adaptation, and other domains. The important result is not catalogue size; it is sharper ownership.

## 1. Generation and verification are different jobs

Aesthetic generation benefits from commitment, taste, coherent art direction, and willingness to take a justified risk. Verification benefits from skepticism, evidence, explicit failure criteria, and refusal to be persuaded by the generator's narrative. Combining both in one unconstrained prompt encourages self-certification.

NUI response: generation faculties produce contracts/artifacts; `challenging-ui-designs` routes fresh critic lenses; critics have `may_modify: false`; `gating-ui-completion` owns the release decision.

## 2. “Design first” is necessary but not sufficient

Visual-target-first workflows prevent arbitrary design-by-coding, but a screenshot cannot encode hidden interaction states, permissions, accessibility semantics, error recovery, localization, automation authority, safety constraints, or platform behavior.

NUI response: a visual target freezes only the axes it actually specifies. Product truth, human factors, task flow, state algebra, accessibility, modality, responsive behavior, platform adaptation, AI authority, and risk remain explicit obligations.

## 3. Taste databases are useful but can become presets

A structured database can help an agent retrieve palettes, typography, product patterns, and UX heuristics. The failure mode is category determinism: `fintech → dark navy + cards`, `AI → purple gradient`, `premium → serif + cream`.

NUI response: `exploring-aesthetic-directions` constructs a search space from subject semantics, audience, emotional target, trust posture, density, novelty budget, media character, brand maturity, and platform. Product categories can inform retrieval but never select a style by themselves.

## 4. Anti-slop can become another dogma

Lists that ban gradients, cards, glass, pills, or serif faces often improve generic outputs in the short term, then create a recognizable anti-slop house style.

NUI response: `preventing-generic-ui` evaluates `pattern × context × intent × frequency × user impact × justification`. The verdict depends on function, not fashion allegiance.

## 5. Human factors are upstream of visual polish

Interfaces used repeatedly, under time pressure, with fatigue, in motion, in safety-critical settings, or through constrained input cannot be judged by the same aesthetic heuristics as a marketing page.

NUI response: user/task frequency, attention, memory burden, perception, motor constraints, error cost, environment, fatigue, training, and recovery are modeled before visual optimization when they are material. `engineering-human-factors`, `modeling-cognitive-load-and-attention`, `modeling-perception-and-motor-control`, and `designing-high-stakes-decisions` own these decisions.

## 6. Dense UI requires different taste than marketing UI

Many “beautiful UI” prompts reward whitespace, large type, limited visible controls, and cinematic first viewports. Those choices can be harmful in repeated operational work where experts compare many values and build spatial memory.

NUI response: `designing-data-dense-interfaces` protects comparison alignment, spatial memory, selection, live-update stability, bulk scope, and responsive access to critical data. Density is an optimization variable, not a failure by default.

## 7. State is a first-class design dimension

Static screenshots hide the majority of product behavior. Default/hover/disabled alone is too shallow for real software.

NUI response: component state algebra models interaction, availability, validation, async, content, permission, environment, theme/accessibility, locale, and input-modality dimensions. Only material cross-products are required; the goal is coverage, not combinatorial paperwork.

## 8. Accessibility cannot be a final lint pass

Automated tooling is excellent at machine-detectable violations but cannot prove label meaning, focus quality, task comprehension, communication ownership, cognitive simplicity, sign-language adequacy, or every assistive-technology interaction.

NUI response: accessibility obligations exist at design-time, component-time, and runtime, with specialists for cognitive accessibility, low vision/high contrast, screen readers, motion/photosensitivity, accessibility settings, AAC, accessible media, sign-language presentation, and alternative input. Automated findings are evidence scoped to what the tool actually tests.

## 9. Platform universality requires semantic portability, not pixel parity

A universal skill that says “always use this web pattern” is not universal. Conversely, completely separate platform skills lose product-system coherence.

NUI response: preserve product invariants, canonical operations, semantic tokens, and state intent; adapt navigation, input, viewing distance, safe areas, focus, physical controls, system affordances, accessibility APIs, and presentation where the platform or environment differs.

`designing-cross-device-action-equivalence` makes this explicit: the same operation can map to a desktop shortcut, touch gesture, TV remote action, voice intent, or hardware control without changing its meaning or consequence.

## 10. A surface can change release authority

Some domains are not merely different screen sizes. Automotive driving, medical devices, control rooms, robotics, and flight decks change the acceptable evidence and consequences of interaction.

NUI response: specialist surface skills own the domain-specific decision layer while reusing lower-level faculties. A flight-deck skill does not replace human factors or input-modality reasoning; it adds phase-of-flight, crew-role, automation-mode, alert/control integration, design-related flightcrew error, and certification evidence. NUI organizes the reasoning but does not claim certification.

## 11. AI UX is not one pattern

“AI interface” can mean generated text, an assistant, autonomous action, many agents, generated UI, emotion-sensitive adaptation, an embodied avatar, or an ambient system that acts without a visible app.

NUI response: separate skills own human-AI mental models, autonomy, uncertainty/provenance, streaming, correction/revert, multi-agent attribution, generative UI, affective adaptation, avatar/embodied representation, ambient context, and robotics. A high-confidence model output never automatically gains high action authority.

## 12. Generative UI must separate rendering from privilege

A model that can generate interface structure should not automatically gain the authority to create arbitrary executable behavior or invoke privileged actions.

NUI response: `designing-generative-ui` treats generated UI as schema-constrained presentation bound to approved component vocabulary and typed action identifiers. Authorization, target binding, confirmation policy, idempotency, and recovery remain outside untrusted generated structure.

## 13. Communication UI is more than text input

AAC, captions, subtitles, sign-language presentation, transcripts, voice, and avatars all affect who is understood to be speaking and what information remains available.

NUI response: these channels have separate semantic owners. AAC protects expressive agency, vocabulary and access method. Accessible media protects equivalent information and synchronization. Sign-language presentation protects natural-language visual integrity. Avatar representation protects identity/controller attribution. AI suggestions must not silently become the user's speech.

## 14. Assistance should not become a patch over bad UI

Contextual help, tours, tooltips, AI helpers, and troubleshooting can hide weak primary interaction.

NUI response: `designing-in-product-assistance` first asks whether the underlying interface can be made clearer. It owns residual orientation, explanation, procedure, diagnosis, recovery, and escalation after primary semantics are as strong as practical.

## 15. The router is part of intelligence

A catalogue with many excellent skills still fails if the agent loads everything or picks by keyword. Context dilution weakens compliance; keyword matching confuses surface labels with failure modes.

NUI response: `routing-ui-work` builds a typed profile covering intent, platform surfaces, modalities, AI role, risk, time, social context, specialist domains, human context, information, interaction, visual freedom, authority sensitivity, research freshness, and evidence capability. It then selects the minimum sufficient faculties and verifies deterministic hard routes before the profile is valid.

## 16. Deterministic facts should not depend on persuasion

LLMs can rationalize missing evidence, broken parent relationships, incomplete state lists, stale sources, or a test they expect to pass.

NUI response: the Python kernel validates graph completeness/acyclicity, skill metadata, state accounting, token tiers/alias cycles, atlas ownership, source authority/freshness, mandatory routes, completion packet integrity, unresolved findings, and bounded research saturation. It intentionally does **not** attempt to numerically score beauty.

## 17. Research completeness must itself be falsifiable

A long bibliography does not prove that a UI taxonomy is complete. Research can always stop too early or create a new skill for every noun.

NUI response: `measuring-research-saturation` and `validate_bounded_saturation` require breadth, depth, contradiction, novelty, and freshness evidence. Successive adversarial sweeps must be recorded. The current wave closed only after the final primary-source decomposition sweep produced zero new non-decomposable decision owners. A new standard, platform, modality, AI behavior, empirical contradiction, or unowned atlas cell reopens research.

## 18. Source status is part of the design decision

Published standards, drafts, platform guidelines, regulations, empirical studies, and community heuristics have different authority and drift.

NUI response: source ledgers record publisher, authority, status, domain, drift, review date, licensing posture, and the mechanism absorbed. Draft standards remain drafts. Paywalled standards are not reproduced from public abstracts. Platform guidance is monitored for change rather than frozen as eternal truth.

## 19. A universal UI system should compose specialties instead of duplicating them

The research deliberately rejected many candidate skills because their decisions decomposed cleanly into existing owners. For example, rehabilitation robotics composes medical safety + robotics + accessibility + haptics; immersive scene media composes spatial/XR + accessible media + haptics; multimodal customer service composes voice + direct input + cross-device action + realtime behavior.

This is a strength. A graph that creates a new skill for every vertical becomes harder to route, harder to test, and more contradictory.

## Core synthesis

NUI's central design is a division of responsibility:

- **Kernel:** authority, lifecycle, contracting, routing, obligations, evidence, adversary, recovery, completion.
- **Industry Atlas:** machine-readable map of surfaces, modalities, AI roles, risks, temporal behavior, social contexts, specialist domains, owners, and verifiers.
- **Faculties:** product, architecture, interaction, visual craft, systems, human factors, modalities, platforms, inclusion, AI, trust/safety, resilience, design operations, and specialist environments.
- **Critics:** independent failure discovery with no self-certification authority.
- **Deterministic validator:** machine-checkable invariants, mandatory routes, source freshness, and saturation evidence.
- **Research plane:** frontier search, authority calibration, atlas maintenance, standards-to-obligations translation, saturation and reopen policy.
- **Adapters:** runtime capability mapping without changing core policy.
- **Evals:** pressure scenarios that tempt known agent failure modes.

This is intentionally harder to bypass than a single long instruction file while remaining inspectable, portable, and evolvable.

For the complete research-wave record, see `UI-INDUSTRY-RESEARCH-2026-08-12.md` and the machine-readable files under `knowledge/`.
