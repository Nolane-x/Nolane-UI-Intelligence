# Nolane UI Intelligence

**Universal Design Cognition, Industry Routing & Verification System for AI agents.**

Nolane UI Intelligence (NUI) is a platform-agnostic Agent Skill graph for serious UI/UX work. It treats interface design as a system of independent decisions — product semantics, human factors, interaction, visual craft, platform behavior, input modalities, accessibility, AI agency, safety, resilience, design systems, and verification — rather than one vague instruction to “make it beautiful.”

The current v5 graph declares **154 skills**: the v2 industry-wide cognition system, v3 Product UI Closure + Visual Learning plane, v4 UI Ecosystem Intelligence plane, and the v5 Affective & Aesthetic Enforcement Spine. That number is descriptive, not a target. The router normally loads the **smallest sufficient graph** for the current task; high visual ambition is an explicit exception where required visual faculties become a hard route rather than optional context.

NUI does not promise objective beauty, automatic compliance, or permanent completeness. It constrains observable agent behavior so material assumptions become explicit, high-impact domains cannot be silently omitted, independent critics can falsify the design, machine-checkable invariants are enforced by code, and release claims remain bounded by actual evidence.

## What makes NUI different

- **Industry Atlas instead of an app-template catalogue.** Tasks are profiled across surface, modality, AI role, risk, time, social context, specialist domains, authority sensitivity, and evidence capability.
- **Depth-locked ownership.** A skill exists only when it owns a distinct decision or failure class. Child skills cannot waive parent obligations.
- **Progressive disclosure.** `routing-ui-work` selects the minimum sufficient faculties and records why nearby faculties are inactive.
- **Human factors before decoration.** Error cost, cognitive load, perception, motor control, attention, fatigue, task frequency, and operating environment can change the design before visual styling begins.
- **Aesthetic intelligence without preset determinism.** Product category informs search but never dictates `fintech = dark navy` or `AI = purple gradient`.
- **Contextual anti-slop.** Cards, gradients, glass, serif faces, motion, minimalism, and maximalism are judged by function and context rather than blanket bans.
- **Multi-platform and multi-modality reasoning.** Web, mobile, desktop, foldables, TV, wearables, automotive, flight deck, XR, games, terminal UI, kiosks, robotics, ambient systems, control rooms, keyboard, touch, pen, remote, voice, gaze, haptics, alternative input, and BCI can receive specialized ownership.
- **AI/agent-specific authority.** Human-AI interaction, uncertainty/provenance, streaming, correction, autonomous action, multi-agent attribution, generative UI, affective adaptation, and embodied/avatar representation are separate contracts.
- **Deep inclusive design.** Root accessibility is augmented by cognitive, low-vision/high-contrast, screen-reader, motion/photosensitivity, accessibility-settings, AAC, accessible-media, and sign-language faculties.
- **Independent criticism.** The generator may not certify material UI completion by itself.
- **Evidence-gated release.** Missing verification remains UNKNOWN/BLOCKED rather than being converted into confidence.
- **Deterministic invariants.** Graphs, ownership, routes, source freshness, state/token contracts, completion packets, and bounded research saturation are checked by Python rather than trusted to model self-report.
- **Research that can reopen.** High-drift standards/platforms live in `knowledge/research-radar.json`; a changed authority can reopen a domain and force a new research wave.

## Affective & Aesthetic Enforcement (v5)

NUI v5 closes a failure exposed by the ATLAS regression: a UI can pass code, viewport, overflow and browser-error checks while still failing the original request for exceptional beauty, awe, magnitude, memorability or aspirational identity. v5 treats those experiential goals as product requirements rather than decoration.

The v5 control path is:

`raw intent → experiential intent → visual ambition → hard routes → divergent candidates + reference frontier → craft → global perceptual/semantic evidence → execution critic → adequacy critic → refine/re-diverge → release gate`

Flagship/exceptional/experiential work cannot silently drop reference research, aesthetic divergence, typography/color/spacing/surface/media/motion craft, anti-generic analysis, computed legibility, visual-energy evidence, signature-depth analysis, adequacy criticism, rendered iteration or basin escape merely to save context. Material visualization adds channel provenance; role fantasy adds aspirational-identity modeling; magnitude adds spatial dramaturgy; multi-screen products add perceptual-diversity evidence.

The system deliberately does **not** compute a universal beauty score. It separates aesthetic specificity from aesthetic excellence and requires evidence against the preserved intent. A coherent implementation of a weak thesis can be marked `INADEQUATE`; repeated failure can emit `RE_DIVERGE` instead of polishing the wrong aesthetic basin.

NUI v5 also adds semantic-mutation and factorial skill-interaction eval specifications so “well-written skill prose” is not treated as proof of behavioral effect. Historical token-length depth proxies have been removed from the v2-v4 depth tests; v5 tests focus on contracts, decisions, failure detection, routing, mutation sensitivity and interaction regressions.

## Product closure and ecosystem intelligence

NUI v3/v4 adds two system-wide planes that address common agent failures which screen-level design advice does not catch.

**Product UI Closure** treats the product as a connected capability/action/state graph. A screen that exists but has no discoverable path, an action with no binding, a hidden route that only works by typing a URL, a duplicated command with conflicting semantics, or a responsive layout that drops a material capability is a release blocker rather than a small polish issue.

**UI Ecosystem Intelligence** gives the agent a typed, evidence-bound way to use the external UI ecosystem. `knowledge/ui-ecosystem-registry.json` contains curated implementation sources across animated components, motion engines, headless accessibility primitives, design systems, data visualization, editors, tables/forms, drag-and-drop, canvas/whiteboard, 3D/spatial, mobile and agent-skill catalogues. It is not a popularity leaderboard and it does not authorize copying.

For any material external source, the agent follows:

`need → research → inspect primary source → cite → classify source role → select adopt/adapt/inspire/build/reject → reconcile with local semantics/tokens/content → audit integration → verify local runtime`

High-drift or legally ambiguous sources require live re-verification before use. A repository's upstream accessibility demo is not evidence that the local wrapper remains accessible. A visually strong component gallery is not the semantic authority for focus, keyboard behavior or product actions.

The registry is intentionally incomplete by design: when no current source fits, or registered candidates are stale/high-drift, `query_ui_ecosystem` reports `live_search_required` and the research faculty must extend the reference ledger instead of hallucinating a library from model memory.

## Canonical lifecycle

`INTAKE → CONTRACTED → ROUTED → DISCOVERED → ARCHITECTED → DIVERGED → DESIGN_SELECTED → SYSTEMIZED → SPECIFIED → IMPLEMENTABLE → RENDERED → CRITIQUED → VERIFIED → RELEASED`

Any failed obligation, stale evidence, contradiction, missing mandatory route, or material regression routes to `RECOVERY` or `BLOCKED`.

## v5 domain families

NUI currently separates responsibilities across:

- kernel / contract / routing / evidence / release;
- product and information architecture;
- interaction and component state semantics;
- visual art direction and craft;
- design tokens and component systems;
- human factors and usability research;
- input modalities;
- platform/surface specialists;
- AI, agents, generative UI, affective and embodied systems;
- trust, privacy, authentication, financial, medical, aviation and other high-risk domains;
- temporal/resilience behavior;
- accessibility and communication specialists;
- design-system governance;
- independent critic courts;
- research authority, atlas maintenance, and saturation measurement.

See `docs/research/UI-INDUSTRY-RESEARCH-2026-08-12.md` for the full research rationale and the four adversarial expansion waves.

## Repository map

- `skills/` — universal and specialist cognitive/design skills
- `skills/skill-graph.json` — parent/owner/output graph
- `knowledge/` — UI Industry Atlas, source ledgers, research radar, manifests, saturation evidence
- `schemas/` — typed record contracts
- `src/nolane_ui/` — deterministic validators and modular routing predicates
- `evals/` — routing, pressure, craft, accessibility, safety, emerging-domain and adversarial fixtures
- `adapters/` — runtime capability mappings for supported agents
- `docs/research/` — provenance, research synthesis, and bounded saturation report
- `artifacts/` — bounded completion packets and verification outputs

## Authority order

Explicit product/safety constraints > applicable law/regulation/normative standards > safety/regulatory guidance > authoritative platform guidance > project design system and validated product evidence > empirical human-factors/usability evidence > mature design-system guidance > high-quality agent/community heuristics > model aesthetic preference.

Source status matters. A draft standard remains a draft. Current platform guidance can override an older heuristic. A community UI rule never becomes normative because it is popular.

## Start here

For any material UI/UX task, load:

`skills/using-nolane-ui/SKILL.md`

The bootstrap hands control to `nolane-ui`, which contracts the task and invokes `routing-ui-work`. Do **not** preload all skills. A web marketing surface, an AAC communication app, a flight deck, a generative-UI agent, and a TV interface must not receive the same context.

See `docs/USAGE.md` for route examples and task-profile guidance.

## Research saturation

The 2026-08-12 research wave is marked **bounded SATURATED**, not permanently complete. Earlier adversarial sweeps continued to reveal new owners; the final primary-source decomposition sweep added zero new non-decomposable decision classes. `validate_bounded_saturation` requires PASS evidence for breadth/depth/contradictions/novelty/freshness, a zero-novelty final sweep, explicit bounds, and reopen conditions.

A new standard, platform, modality, AI behavior, empirical result, or unowned atlas cell reopens research.

## Verification

Run:

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

Repository validation proves structural and evidence-contract invariants only. It does not prove that a future interface is beautiful, usable, accessible, safe, certified, or faithful without task-specific evidence.
