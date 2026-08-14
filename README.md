<div align="center">

# Nolane UI Intelligence

### A design cognition and verification system for AI agents

**AI can generate an interface in seconds. NUI is built to make it understand why that interface should exist, what it must preserve, how it should feel, and what evidence is required before calling it good.**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `174 canonical skills` · `evidence-gated` · `platform-agnostic` · `MIT`

</div>

---

## The problem is not generating UI anymore

Modern AI can produce pages, dashboards, apps, components, animations and entire front ends astonishingly fast.

The harder problem is everything that happens **before and after the code appears**:

- Did the model understand the actual product, or did it reduce the brief to a familiar template?
- Did important capabilities disappear because they were not visually exciting?
- Did a professional tool become a collection of oversized cards?
- Did “premium” collapse into dark backgrounds, blur and gradients?
- Did mobile become a squeezed desktop layout?
- Did motion explain state, or merely decorate it?
- Did the implementation preserve accessibility, platform behavior, permissions, recovery and trust?
- Did the critic actually inspect the rendered result, or simply agree with the design rationale?
- And when the system says a skill “improves UI quality”, **what evidence makes that claim true?**

**Nolane UI Intelligence (NUI)** is an attempt to solve that layer.

It is not another component library, not a style preset, and not a giant “make this beautiful” prompt. NUI is a **structured design-intelligence system for agents**: a graph of specialized decision owners, routing rules, evidence contracts, independent critics, research provenance, deterministic validators and empirical-evaluation machinery.

The goal is simple to state and difficult to achieve:

> **Turn UI generation from a one-shot act of imitation into a disciplined process of product reasoning, design divergence, implementation, rendered critique, recovery and evidence-bound release.**

---

## What NUI changes in an AI design workflow

Without a design cognition layer, an agent often follows a short loop:

`prompt → familiar pattern → code → “looks good” → done`

NUI replaces that with a lifecycle:

```text
INTAKE
  ↓
CONTRACTED
  ↓
ROUTED
  ↓
DISCOVERED
  ↓
ARCHITECTED
  ↓
DIVERGED
  ↓
DESIGN_SELECTED
  ↓
SYSTEMIZED
  ↓
SPECIFIED
  ↓
IMPLEMENTABLE
  ↓
RENDERED
  ↓
CRITIQUED
  ↓
VERIFIED
  ↓
RELEASED
```

A failed obligation, stale source, missing capability, weak visual basin, runtime defect or unsupported claim can send the system to `RECOVERY` or `BLOCKED` instead of letting confidence substitute for evidence.

The agent is therefore encouraged to ask different questions at different moments. Product intent is not allowed to become layout prematurely. Visual direction is not allowed to collapse into the first fashionable answer. Implementation success is not allowed to certify visual quality. A generator is not allowed to silently certify its own material work.

---

## 174 skills — one graph, not 174 prompts

NUI currently contains **174 canonical skills**.

That number is descriptive, not a target and not a reason to load everything. The system uses `routing-ui-work` to activate the **smallest sufficient graph** for the actual task.

A marketing site, a video editor, a fintech console, a medical workflow, a TV interface, an AAC communication surface, an AI agent workspace and a flight deck should not receive the same reasoning context.

The skill graph spans, among other areas:

- product intent, capability modeling and product completeness;
- users, tasks, expertise, error cost and human factors;
- information architecture, navigation and settings architecture;
- interaction, state, forms, search, tables and data-dense workflows;
- desktop, mobile, large-screen, TV, wearable, automotive, XR, terminal, kiosk and specialist surfaces;
- keyboard, pointer, touch, pen, remote, voice, gaze, haptics and alternative input;
- accessibility, cognitive access, low vision, screen readers, reduced motion, AAC and accessible media;
- AI uncertainty, human-AI interaction, agent autonomy, generative UI and multi-agent surfaces;
- authentication, permissions, privacy, finance, medical and other high-consequence interfaces;
- typography, color, spacing, material, composition, imagery, motion and visual hierarchy;
- editors, canvases, professional workspaces, command systems and rich interaction;
- design systems, tokens, component architecture and implementation fidelity;
- research authority, external libraries, source archaeology and integration audits;
- independent visual, UX, accessibility, safety, platform, resilience and fidelity critics.

A new skill is justified only when it owns a genuinely distinct decision or failure class. Later NUI versions deliberately deepen existing owners rather than inflating the graph with near-duplicates.

---

## Flagship visual intelligence: beautiful is not a checkbox

NUI treats visual ambition as a real contract.

For `flagship`, `exceptional` or `experiential` work, one polished screenshot is not enough. The system expects evidence that the visual direction was actually discovered and stress-tested.

High-ambition work includes mechanisms such as:

**Material divergence.** At least three candidates must differ meaningfully in composition, typography, material language and signature mechanism. A palette swap is not a new direction.

**Generic-transfer resistance.** Blind the logo and product name. If the same authored shell could host an unrelated SaaS product without losing important meaning, the identity layer is not finished.

**Attention architecture.** The design must establish what the eye should understand first, second and third — not simply make every region equally polished.

**Domain-native signature.** Memorability should come from the subject, workflow, information or interaction itself rather than decorative geometry pasted on top.

**Responsive art direction.** Smaller screens must structurally recompose the experience when needed, not merely stack desktop rectangles vertically.

**Closed critique loops.** A material visual finding must be corrected and re-observed in a named render. NUI requires critique to change evidence, not just produce commentary.

This is why NUI does not expose a universal “beauty score.” Taste is comparative, contextual and evidence-bearing. Product truth, accessibility and interaction correctness remain hard boundaries even when a visually louder answer would score better in a superficial preference test.

---

## Product completeness before screen completeness

A UI can be internally coherent and still represent an incomplete product.

NUI therefore separates **discovery breadth** from **implementation commitment**. Before an ambitious product is compressed into routes and screens, plausible capability families are discovered and explicitly dispositioned as:

`REQUIRED · EXPECTED · OPTIONAL · EXCLUDED · UNKNOWN`

This prevents a “full platform” from quietly becoming Dashboard + Items + Settings simply because those were the first screens the model imagined.

At the same time, broad discovery is not permission to turn every utility into enterprise software. Scope must remain tied to actors, outcomes, lifecycle, consequence and declared product ambition.

Professional tools receive additional scrutiny around workspace regions, selection, inspectors, commands, history, assets, status, import/export, collaboration and persistence. Completeness is measured by meaningful capability and reachability — not by showing every control simultaneously.

---

## Authority without imitation

NUI can learn from external design systems, platforms, component libraries, research and production products, but it separates **access** from **authority**.

A source being famous, beautiful, easy to query through MCP, or available as agent-readable documentation does not make it authoritative for every decision.

NUI resolves authority by dimension. A platform guide may own platform convention. A headless primitive may contribute semantic interaction mechanics. A motion engine may contribute interpolation mechanics. A visual reference may raise the bar for composition. None of those sources silently inherits product strategy, accessibility proof or visual ownership outside its scope.

The transfer rule is:

> **Transfer mechanism, not trade dress.**

Material external influence is expected to carry provenance, role classification, licensing posture, transfer boundaries, contraindications and local runtime verification. README-only research does not authorize production influence when deeper evidence is required.

---

## V10: from design rules to falsifiable design intelligence

V10 introduces one of the most important changes in the project: **NUI is no longer satisfied with a skill merely sounding intelligent.**

A behavioral rule should be capable of failing.

The V10 evaluation layer currently contains:

- **13 falsifiable behavioral hypotheses**;
- **48 original benchmark tasks** across **12 task families**;
- a public-generation / hidden-evaluator boundary;
- holdout tasks for transfer-sensitive evaluation;
- targeted semantic mutations, ablations and placebo controls;
- blinded pairwise judging support;
- run records with provider, model, snapshot, runtime and artifact provenance;
- canonical SHA-256 hashing for experimental identity;
- matched-pair aggregation and uncertainty-aware statistics;
- hard-blocker regression checks;
- bounded claim promotion: `STRUCTURAL_ONLY`, `EMPIRICAL_LOCAL`, `EMPIRICAL_TRANSFER`, or `REJECTED`.

The crucial distinction is this:

```text
artifact quality ≠ evidence that NUI caused the improvement
```

A beautiful result can demonstrate artifact quality. It does not, by itself, prove that a particular NUI skill made a model better.

For an empirical claim, NUI requires stronger lineage: real validated runs, matched treatment pairs, blinded evaluation, bundle digests, targeted ablation evidence and bounded statistics. A boolean such as `real_model_runs: true` cannot promote a claim by itself.

### Current claim ceiling

The repository's ordinary CI and bundled structural fixtures currently certify the **evaluation framework**, not universal model-quality improvement. Therefore the default repository claim ceiling remains:

**`STRUCTURAL_ONLY`**

That is intentional. `EMPIRICAL_LOCAL` or `EMPIRICAL_TRANSFER` must be earned from real provider/model run bundles that satisfy the V10 gates. NUI would rather say “not yet proven” than turn synthetic fixtures into marketing evidence.

---

## What NUI is not

NUI is **not**:

- a component kit;
- a Figma replacement;
- a collection of fashionable palettes;
- a mega-prompt that should be pasted into every conversation;
- an objective oracle of beauty;
- a certificate that every generated UI is accessible, safe or production-ready;
- a license to copy Apple, Linear, Stripe, Notion, Canva, VS Code or any other product;
- a benchmark score pretending to be design intelligence.

It is infrastructure for **reasoning, routing, design decisions, criticism, evidence and recovery**.

---

## Architecture at a glance

```text
Nolane-UI-Intelligence/
├── skills/                 # canonical design cognition graph
│   └── skill-graph.json    # ownership, parents and outputs
├── knowledge/              # authority, research, design and V10 evidence memory
├── benchmarks/v10/         # public tasks, hidden evaluator data, mutations
├── evals/                  # adversarial and behavioral pressure tests
├── schemas/                # typed evidence contracts
├── src/nolane_ui/          # deterministic validators and reasoning kernels
├── scripts/                # validation, release and V10 empirical tooling
├── adapters/               # agent/runtime capability mappings
├── docs/                   # architecture, research and run protocols
└── tests/                  # repository, behavior, mutation and claim gates
```

The canonical entry point for material UI work is:

`skills/using-nolane-ui/SKILL.md`

That bootstrap hands the task to `nolane-ui`, which contracts the work and invokes `routing-ui-work`. **Do not preload all 174 skills.** Progressive disclosure is part of the architecture.

---

## Quick start

Validate the repository:

```bash
PYTHONPATH=src python scripts/nui-validate .
```

Run the complete test suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

For V10 controlled evaluation, start with:

```bash
python scripts/nui-v10-build-run-matrix examples/v10/experiment.example.json
python scripts/nui-v10-validate-run-bundle <manifest.json> <runs.jsonl>
python scripts/nui-v10-aggregate <runs.jsonl>
```

Read `docs/V10-EMPIRICAL-RUN-PROTOCOL.md` before interpreting any efficacy result.

---

## Design principles encoded into the project

A few rules summarize the spirit of NUI:

1. **Product truth precedes visual polish.**
2. **The first plausible UI is a hypothesis, not an answer.**
3. **High ambition requires divergence before refinement.**
4. **Familiar interaction can coexist with distinctive visual identity.**
5. **Missing evidence is `UNKNOWN` or `BLOCKED`, never `PASS`.**
6. **A generator cannot silently certify its own material completion.**
7. **Rendered perception matters; source code is not the final interface.**
8. **External authority is decision-dimensional, never global by prestige.**
9. **A skill is deep because it changes decisions and catches failures — not because it is long.**
10. **Claims about improvement require controlled evidence, not confidence.**

---

## Research and provenance

NUI synthesizes mechanisms from platform guidance, accessibility standards, human-factors material, production design systems, implementation ecosystems and agent-design research while preserving source role and reuse boundaries.

Detailed provenance lives in `docs/research/SOURCES.md` and the machine-readable ledgers under `knowledge/`.

The project intentionally does not bulk-copy third-party skill prose, proprietary design databases or recognizable product trade dress. High-drift sources can reopen research when their guidance changes.

---

## Why this project exists

The future of AI-generated software will not be won only by the model that can emit the most JSX.

It will also depend on the systems surrounding the model: systems that preserve product truth, expose missing assumptions, retrieve the right expertise, resist generic attractors, understand risk, compare alternatives, observe actual rendered behavior, criticize independently, recover from failure and know when a claim has not yet been proven.

**Nolane UI Intelligence is an attempt to build that design layer.**

Not a prettier prompt.

A more rigorous way for an AI to design.

---

## License

MIT. See `LICENSE` for details.
