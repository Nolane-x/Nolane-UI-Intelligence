<div align="center">

# Nolane UI Intelligence

### UI/UX design cognition, runtime evidence, rule intelligence and autonomous journey verification for AI agents

**AI can generate an interface in seconds. NUI is built to make it reason about the product, verify what users actually experience, and justify what it claims before shipping.**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.13.0` · `874 canonical skills` · `813 V13 rules` · `87 provenance records` · `9 agent projections` · `MCP + CLI` · `evidence-gated` · `MIT`

</div>

---

## What is Nolane UI Intelligence?

**Nolane UI Intelligence (NUI)** is an open UI/UX cognition and verification system for AI coding agents.

It combines a large routed graph of specialized design faculties with deterministic validators, rule intelligence, real-browser evidence, UX journey verification, temporal regression analysis and bounded release claims.

NUI is designed to help an agent reason across questions such as:

- What product is actually being built?
- Which user goals and tasks matter most?
- Which capabilities are required, expected, optional or intentionally excluded?
- What information architecture and interaction model fit those goals?
- Does the rendered product match the intended behavior?
- Which UX failures are supported by evidence rather than intuition?
- Which important user journeys should be tested next?
- Did a later revision introduce a semantic UX regression?
- Which verified problems deserve attention first?

NUI is **not** a component library, style preset, screenshot copier, universal beauty score or mega-prompt. It is a design-cognition and verification layer that tries to make UI/UX decisions **explicit, routed, falsifiable, evidence-bound and reviewable**.

### Core principle

> **Discovery decides what is worth testing. Evidence decides what happened. Existing rule authority decides what may be called a UX failure.**

An inferred goal, journey, product relationship or discovery score may guide exploration. It does not silently become blocking UX authority.

---

# Current architecture

NUI now spans five complementary planes:

```text
Canonical Design Cognition
        ↓
Product / Goal / UX Intelligence
        ↓
V13 Rule Intelligence
        ↓
V11 Runtime + Browser Evidence
        ↓
Verification / Regression / Release Claims
```

The system deliberately keeps those responsibilities separate.

- **Skills** describe how an agent should reason.
- **Rules** describe operational failure classes and how they can be verified.
- **Runtime evidence** describes what was actually observed.
- **UX discovery** proposes what is worth testing.
- **UX verification** decides whether a supported failure exists.
- **Regression analysis** compares verified semantics across revisions.
- **Impact ranking** prioritizes verified problems without changing their authority.

---

# UX Intelligence

UX Intelligence extends NUI beyond interface composition into explicit user-goal, journey and recovery reasoning.

## UX Intelligence v1 — cognition and failure ontology

V1 introduces first-class UX mechanisms, cognitive skills and operational UX rules across eight domains:

```text
Goal & Task
→ Mental Model
→ Information Architecture
→ Journey & Flow
→ Cognitive / Friction Cost
→ Comprehension
→ Recovery
→ Evaluation
```

It models failures such as context loss, false completion, premature commitment, hidden dependency, navigation disorientation, unrecoverable progress loss and mental-model mismatch.

The system intentionally rejects folklore such as fixed click-count targets, “less friction is always better,” or arbitrary cognitive limits as universal rules.

## UX Intelligence v2 — journey verification

V2 adds an evidence-gated journey contract and verification layer:

```text
UXJourneySpec
→ explicit evidence / V11 bindings
→ rule-specific evaluators
→ verified UX findings
```

Important boundaries:

- V11 remains the browser/runtime collector.
- V2 remains the authority that emits UX findings.
- Missing evidence produces `insufficient-evidence`, not an invented failure.
- Fuzzy or NLP similarity does not automatically create blocking findings.
- Finding severity and enforcement come from the bound UX rule.

## UX Intelligence v3 — Autonomous UX Scientist

V3 adds the missing layer above journey verification: **what should be tested, what changed, and what matters most?**

The merged pipeline is:

```text
product evidence
→ Product Model
→ Goal Graph
→ journey hypotheses
→ candidate ranking
→ observation planning
→ V11 evidence
→ v2 verification
→ temporal evidence snapshot
→ semantic UX regression
→ impact ranking
```

### Product Model

Represents products as meaningful surfaces, objects, actions, states and relationships instead of a flat list of pages.

### Goal Graph

Represents intent as:

```text
goal → task → object/action → state transition → outcome
```

`goal` and `task` nodes remain explicitly `declared` or `inferred`; browser traversal alone cannot turn inferred intent into observed truth.

### Autonomous Journey Discovery

Deterministically explores product/goal graphs to find journey candidates, with:

- cycle bounds;
- semantic fingerprints;
- duplicate semantic-path collapse;
- explicit/versioned scoring;
- evidence lineage;
- no authority escalation from ranking score.

### Fail-closed promotion

A discovered candidate becomes a V2 journey contract only when the required semantics are actually supported.

NUI does **not** silently invent:

- success criteria;
- recovery expectations;
- context-preservation guarantees;
- ambiguous transitions;
- user intent.

Missing support remains a promotion gap.

### Temporal UX evidence and semantic regression

NUI can snapshot verified journey outcomes across revisions and compare semantic UX changes such as:

- new verified failure;
- reintroduced failure;
- lost recovery path;
- lost context preservation;
- pass → insufficient evidence;
- success evidence disappearing;
- verified journey behavior changing even when pixels barely change.

Evidence loss is kept distinct from a proven UX regression.

### Impact ranking

Verified findings and regressions can be ranked by evidence-bounded impact signals. Priority is operational triage metadata only: a `P0` ranking does not upgrade a warning into a blocking rule.

---

# V11 — runtime and real-browser evidence

NUI distinguishes source intent from what users actually receive at runtime.

V11 provides bounded runtime/browser evidence infrastructure for:

- normalized browser observations;
- Playwright-backed real Chromium collection;
- live visual preview and freshness checks;
- evidence bindings;
- runtime finding routing;
- design-memory freshness;
- visual observation capability checks;
- quality-residue closure;
- source attribution and runtime diagnostics.

For UX Intelligence, V11 remains the **single browser/runtime owner**. V3 may plan what evidence is needed, but it does not create a second Playwright layer or claim an observation happened before V11 actually collects it.

---

# V13 — Rule Intelligence

V13 turns large-scale design knowledge into a deterministic operational rule catalog rather than an unbounded pile of advice.

Current verified repository state includes:

- **813 V13 rules**;
- **87 provenance records**;
- explicit capability requirements;
- applicability and non-applicability conditions;
- failure modes and user impacts;
- observables and falsifiers;
- repairs and exceptions;
- verification modes;
- anti-duplication and boilerplate audits.

Canonical rule records carry fields such as:

```text
rule_id
 domain
 class
 severity
 enforcement
 statement
 intent
 applies_when
 does_not_apply_when
 failure_modes
 user_impacts
 observables
 falsifiers
 repairs
 exceptions
 verification
 capabilities
 provenance_ids
 status
```

Contextual, aesthetic and convergence guidance cannot silently become hard blocking authority. Capability requirements also prevent a rule from pretending that static source inspection proves runtime, accessibility-tree or visual-render behavior.

---

# Canonical design cognition graph

NUI currently preserves **874 canonical skills**.

That number is descriptive, not a quota. A new skill is justified only when it owns a distinct decision or failure class. NUI explicitly prefers **semantic novelty over count** and avoids noun-substitution experts or overlapping skill inflation.

The graph spans areas such as:

- product intent, jobs, users and capability modeling;
- information architecture and settings systems;
- interaction states, rich controls and direct manipulation;
- typography, color, spacing, surfaces, icons and visual hierarchy;
- motion semantics and reduced-motion equivalence;
- responsive, mobile, desktop, TV, XR, automotive, wearable and specialist surfaces;
- keyboard, touch, pen, remote, voice, gaze and other modalities;
- accessibility and cognitive accessibility;
- authentication, trust, privacy, financial and medical domains;
- AI/agent uncertainty, provenance, correction and autonomous action;
- professional workspaces, editors, IDEs, media and complex instruments;
- external UI-source research and safe adaptation;
- visual media sourcing and integration;
- product closure and responsive capability preservation;
- rendered criticism and release verification;
- behavioral evaluation, mutation, ablation and empirical claim discipline;
- UX goals, journeys, mental models, recovery and evaluation.

Canonical bootstrap:

```text
skills/using-nolane-ui/SKILL.md
```

Canonical graph:

```text
skills/skill-graph.json
```

---

# Use NUI with your AI agent

NUI is designed to work with **Codex, Claude Code, Google Antigravity, Gemini CLI, OpenCode, Cursor, VS Code/Copilot-compatible agents, any MCP host and generic shell/CLI agents** without maintaining separate copies of the cognition graph.

```text
one canonical NUI cognition graph
            ↓
     thin host projection
            ↓
Codex / Claude / Gemini / OpenCode / Cursor / VS Code / MCP / CLI
```

## Quick start

```bash
git clone https://github.com/Nolane-x/Nolane-UI-Intelligence.git
cd Nolane-UI-Intelligence
python scripts/nui-agent-export --agent openai-codex
```

Supported adapter IDs:

```text
openai-codex
claude-code
google-antigravity
gemini-cli
opencode
cursor-compatible
vscode-agent-compatible
generic-mcp
generic-cli
```

### Agent matrix

| Agent / host | Recommended NUI surface | Command / bridge |
|---|---|---|
| **Codex** | Native Agent Skills bridge + repository policy | `.agents/skills/nolane-ui/SKILL.md` + `python scripts/nui-agent-export --agent openai-codex` |
| **Claude Code** | Native project skill bridge | `.claude/skills/nolane-ui/SKILL.md` + `python scripts/nui-agent-export --agent claude-code` |
| **Google Antigravity** | Agent-Skills-compatible bridge or MCP | `python scripts/nui-agent-export --agent google-antigravity` |
| **Gemini CLI** | CLI/MCP projection | `python scripts/nui-agent-export --agent gemini-cli` |
| **OpenCode** | CLI/MCP projection | `python scripts/nui-agent-export --agent opencode` |
| **Cursor** | Repository guidance + MCP/CLI | `python scripts/nui-agent-export --agent cursor-compatible` |
| **VS Code / Copilot-compatible agent** | Repository guidance + MCP/CLI | `python scripts/nui-agent-export --agent vscode-agent-compatible` |
| **Any MCP host** | Local NUI MCP sidecar | `python scripts/nui-mcp-server` |
| **Any shell-capable agent** | Canonical skill + CLI | `python scripts/nui-agent-export --agent generic-cli` |

## Put NUI inside another project

```bash
git clone --depth 1 https://github.com/Nolane-x/Nolane-UI-Intelligence.git .nui
python .nui/scripts/nui-agent-export --agent claude-code --root .nui
```

Or expose NUI through MCP:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

Use the current MCP/project configuration syntax of your host to register that command.

> **Permission rule:** the host remains authoritative. NUI never expands shell, filesystem, network, browser, image or MCP permissions by itself.

For complete agent-by-agent setup, see **[`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)**.

---

# Python surfaces

The Python package exposes deterministic APIs for the current architecture, including:

```python
from nolane_ui import (
    validate_repository,
    get_rule_v13,
    query_rules_v13,
    rule_catalog_status_v13,
    verify_ux_journey,
    build_ux_product_model,
    build_ux_goal_graph,
    discover_ux_journeys,
    promote_ux_journey_candidate,
    plan_ux_discovery,
    create_ux_evidence_snapshot,
    compare_ux_snapshots,
    rank_ux_impacts,
    ux_v3_status,
)
```

These APIs intentionally separate discovery, evidence, verification and authority.

---

# MCP surfaces

The optional MCP server exposes bounded local read/analysis tools for:

- repository status and validation;
- canonical skills;
- V13 rules, provenance and catalog status;
- UX mechanisms, skills and rules;
- UX v2 journey verification;
- UX v3 Product Model and Goal Graph construction;
- journey discovery and candidate querying;
- fail-closed journey promotion;
- evidence-request planning;
- temporal snapshots;
- semantic regression comparison;
- impact ranking.

The MCP module deliberately contains **no arbitrary shell executor, remote URL fetcher or third-party installer**. Those permissions remain with the host agent.

Install optional MCP support with the project extra defined in `pyproject.toml`.

---

# Product completeness: broad before narrow

A major NUI rule remains:

> **Think broadly before deciding what to omit.**

When a product is underspecified, NUI first discovers a plausible capability envelope and then dispositions capabilities as:

```text
REQUIRED
EXPECTED
OPTIONAL
EXCLUDED
UNKNOWN
```

This prevents the common AI failure where the first few obvious screens become the whole product.

The goal is **intentional scope**, not enterprise bloat.

---

# Professional tools should behave like professional tools

For editor-, IDE-, design-, media- and operations-class products, NUI reasons in terms of instrument architecture rather than “more buttons.”

Depending on the product, that can include:

```text
workspace shell
→ mode/tool system
→ selection model
→ primary work surface
→ context inspector
→ hierarchy/layers
→ asset/resource system
→ command/search surface
→ history / undo / redo
→ import/export
→ collaboration
→ status/progress
→ persistence
```

Completeness does not mean showing everything simultaneously. Progressive disclosure, keyboard power paths, contextual controls and density strategy remain design decisions.

---

# Render first. Critique what users actually see.

NUI distinguishes a design specification from its rendered result.

A high-ambition workflow can require:

```text
render
→ runtime observation
→ visual / hierarchy critique
→ typography / spacing / density critique
→ platform-residue audit
→ responsive critique
→ correction
→ re-render
→ comparison
→ verification
```

This catches failures that source inspection alone misses: wrapping errors, accidental scrollbars, browser defaults, optical misalignment, weak hierarchy, bad crops, cramped responsive states and interaction behavior that diverges from intent.

---

# References without cloning

NUI uses external design systems, products, research and UI libraries as **mechanism sources**, not trade-dress targets.

```text
need
→ inspect current source
→ identify authority role
→ extract mechanism
→ define transfer boundary
→ adapt to local product truth
→ verify local runtime
```

A reference may teach density, command architecture, typography, motion continuity, material layering, data treatment or accessibility semantics. It does not become permission to reproduce a recognizable product aesthetic.

---

# V10 — behavioral evaluation and empirical proof

NUI also asks:

> **Does using NUI actually change agent behavior in the intended direction?**

The V10 evaluation plane includes falsifiable hypotheses, benchmark tasks, mutation and ablation controls, provenance, treatment-blind judging, matched comparison units and bounded statistical claim promotion.

NUI does not collapse all design quality into one “NUI score.” Product completeness, usability, visual craft, accessibility and other dimensions may move differently and should remain visible.

Repository-only CI supports a **structural evidence ceiling**. Synthetic fixtures are not treated as universal proof that NUI outperforms every model on every UI task.

---

# Verification and authority

NUI is evidence-gated by design.

Current authority principles include:

- user/product requirements outrank heuristics;
- direct measured evidence outranks model preference;
- missing required evidence blocks bounded completion claims;
- self-certification is disabled;
- unresolved critical/major findings cannot be silently ignored;
- discovery confidence is not severity;
- impact priority is not enforcement;
- browser behavior does not prove user intent;
- visual appearance does not prove semantic success;
- runtime claims require runtime-capable evidence.

Run the repository checks with:

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

Repository validation proves structural and evidence-contract invariants for the checked revision. It does not, by itself, prove that a future interface is beautiful, usable, accessible, safe, lawful or empirically superior.

---

# Current verified state

As of **2026-09-06**, UX Intelligence v3 is merged into `main` at:

```text
6421da9b6343e24952ccea5d8c177773230c28fd
```

The merge tree is:

```text
2a8320427e2c3d4a23e7bc31dff73730722889a8
```

Post-merge **Verify NUI #1299** completed successfully on that exact `main` revision:

- Core Python 3.10 — success
- Core Python 3.11 — success
- Core Python 3.12 — success
- Real Chromium runtime — success
- Current-head release gate — success

The verified repository metrics for this revision include:

```text
canonical skills:        874
V13 rules:               813
V13 provenance records:   87
V13 duplicate pairs:       0
V13 boilerplate clusters:  0
```

---

# Repository map

```text
skills/                                canonical design faculties
skills/skill-graph.json               routing / ownership graph
knowledge/                            provenance, ontologies and evidence knowledge
schemas/                              typed evidence contracts
src/nolane_ui/                        deterministic kernels and public Python API
src/nolane_ui/rules_v13/              V13 operational rule intelligence
src/nolane_ui/runtime_v11/            runtime/browser evidence plane
src/nolane_ui/ux_intelligence/        UX cognition, journeys, discovery and regression
benchmarks/v10/                       behavioral benchmark corpus
evals/                                adversarial and behavioral fixtures
.agents/skills/nolane-ui/             Codex / Agent Skills bridge
.claude/skills/nolane-ui/             Claude Code bridge
scripts/nui-agent-export              agent projection CLI
scripts/nui-mcp-server                local MCP entry point
docs/AGENT-INTEGRATION.md             complete AI-agent setup guide
docs/superpowers/specs/               architecture/design specifications
docs/superpowers/plans/               implementation plans
docs/research/                        research provenance and bounded synthesis
```

---

# What NUI is not

NUI is not:

- a React component library;
- a Tailwind preset;
- a Figma kit;
- a single system prompt;
- a collection of trendy screenshots;
- an automatic accessibility certification service;
- a universal numerical beauty function;
- a license to clone another product’s visual identity;
- proof that every AI output becomes excellent merely because NUI is installed.

It is an attempt to build a **design and UX cognition layer around AI agents** and make that layer inspectable, routable, testable and evidence-bound.

---

## License

MIT. See [`LICENSE`](LICENSE).

---

<div align="center">

### AI already knows how to generate UI.
### Nolane UI Intelligence is built to make it **understand the product, test the journey, inspect the runtime and justify the result**.

**Start:** [`skills/using-nolane-ui/SKILL.md`](skills/using-nolane-ui/SKILL.md) · **Agent setup:** [`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)

</div>
