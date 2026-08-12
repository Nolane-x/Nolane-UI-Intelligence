# Nolane UI Intelligence

**Universal Design Cognition, Industry Routing & Verification System for AI agents.**

Nolane UI Intelligence (NUI) is a platform-agnostic Agent Skill graph for serious UI/UX work. It treats interface design as a system of independent decisions — product semantics, human factors, interaction, visual craft, platform behavior, input modalities, accessibility, AI agency, safety, resilience, design systems, and verification — rather than one vague instruction to “make it beautiful.”

The current v2 research snapshot declares **125 skills** across a universal core and specialist faculties. That number is descriptive, not a target. The router loads the **smallest sufficient graph** for the current task; preloading every skill is a defect.

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

## Canonical lifecycle

`INTAKE → CONTRACTED → ROUTED → DISCOVERED → ARCHITECTED → DIVERGED → DESIGN_SELECTED → SYSTEMIZED → SPECIFIED → IMPLEMENTABLE → RENDERED → CRITIQUED → VERIFIED → RELEASED`

Any failed obligation, stale evidence, contradiction, missing mandatory route, or material regression routes to `RECOVERY` or `BLOCKED`.

## v2 domain families

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
