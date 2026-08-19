<div align="center">

# Nolane UI Intelligence

### Design cognition, product completeness, visual craft and evidence-gated verification for AI agents

**AI can generate an interface in seconds. NUI is built to make it think like a serious product/design team before it ships one.**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `274 canonical skills` · `9 agent projections` · `MCP + CLI` · `evidence-gated` · `MIT`

</div>

---

## Description

**Nolane UI Intelligence (NUI)** is an open design-cognition and verification system for AI coding agents. It gives an agent a routed graph of specialized UI/UX faculties for product modeling, information architecture, interaction, visual direction, typography, motion, accessibility, platform behavior, professional workspaces, authentication, settings, product completeness, rendered critique, design-to-code fidelity and empirical evaluation.

NUI is **not** a component library, style preset, mega-prompt, screenshot copier or universal beauty score. It is a system that tries to make design decisions explicit, routed, falsifiable and evidence-bound.

### Topics / tags

`ai-agents` · `agent-skills` · `ui-ux` · `design-intelligence` · `design-system` · `frontend` · `codex` · `claude-code` · `gemini-cli` · `opencode` · `cursor` · `vscode` · `mcp` · `accessibility` · `human-computer-interaction` · `ai-coding`

---

# Use NUI with your AI agent

NUI is designed to work with **Codex, Claude Code, Google Antigravity, Gemini CLI, OpenCode, Cursor, VS Code/Copilot-compatible agents, any MCP host, and generic shell/CLI agents** without maintaining nine copies of the skill graph.

The architecture is:

```text
one canonical NUI cognition graph
            ↓
     thin host projection
            ↓
Codex / Claude / Gemini / OpenCode / Cursor / VS Code / MCP / CLI
```

## Quick start

Clone NUI:

```bash
git clone https://github.com/Nolane-x/Nolane-UI-Intelligence.git
cd Nolane-UI-Intelligence
```

Ask NUI for the integration plan for your agent:

```bash
python scripts/nui-agent-export --agent openai-codex
```

Replace `openai-codex` with any supported adapter ID:

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

If NUI is not the repository itself, keep it as a sidecar instead of copying hundreds of skill files into a giant prompt:

```bash
git clone --depth 1 https://github.com/Nolane-x/Nolane-UI-Intelligence.git .nui
```

Then inspect an agent projection:

```bash
python .nui/scripts/nui-agent-export --agent claude-code --root .nui
```

or expose NUI through a local MCP server:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

Use the **current MCP/project configuration syntax of your host** to register that command. NUI intentionally keeps vendor configuration outside the canonical graph because host syntax changes faster than design cognition.

> **Permission rule:** the host remains authoritative. NUI never expands shell, filesystem, network, browser, image or MCP permissions by itself.

For complete agent-by-agent setup, see **[`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)**.

---

## Why NUI exists

The difficult problem is no longer “can AI write JSX or CSS?”

The difficult problem is that an AI can produce something technically valid while still thinking too narrowly:

- a sales platform becomes only Dashboard + Products + Orders;
- a professional editor has a canvas but no command model, inspector, history, asset workflow or workspace persistence;
- authentication exists but recovery, session/device management or account lifecycle is missing;
- settings are a handful of toggles instead of a scoped preference architecture;
- desktop looks attractive while mobile is merely the same layout squeezed smaller;
- every region becomes a rounded card because that is the easiest visual primitive to synthesize;
- native browser chrome suddenly appears inside an otherwise polished interface;
- motion exists because “premium apps animate,” not because it teaches state or causality;
- a screenshot looks good, so the generating agent certifies its own work.

NUI treats those as **reasoning failures**, not just styling mistakes.

---

## The core idea

Instead of telling an agent:

```text
Make a beautiful modern UI.
```

NUI drives a lifecycle closer to:

```text
product truth
→ task / user / risk contract
→ capability discovery
→ specialist routing
→ information & interaction architecture
→ divergent visual directions
→ design-system decisions
→ implementation
→ real render
→ independent critique
→ repair / re-render
→ verification
→ bounded release claim
```

The agent does not preload every rule. It routes to the **smallest sufficient graph of owners** for the product and task.

---

## 274 canonical design faculties

NUI currently preserves **274 canonical skills**. The number is descriptive, not a license to create overlapping experts. The long-term UI-industry roadmap targets broader coverage toward 1,000 canonical faculties while preserving distinct decision ownership and minimal routing.

A skill is allowed to exist only when it owns a distinct decision or failure class. NUI deliberately avoids turning every new idea into another overlapping “expert.” Batch 001 adds 100 independently authored specialists across motion, rich controls, direct manipulation, spreadsheet/data interaction, enterprise workflows, billing, scheduling, geospatial interaction and historical state. See [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) for the exact inventory, provenance and non-generation constraints.

The graph spans areas such as:

- product intent, jobs, users and capability modeling;
- information architecture and settings systems;
- interaction states, rich components and direct manipulation;
- typography, color, spacing, surfaces, icons and visual hierarchy;
- motion semantics and reduced-motion equivalence;
- responsive, mobile, desktop, TV, XR, automotive, wearables and specialist surfaces;
- keyboard, touch, pen, remote, voice, gaze and other modalities;
- accessibility, cognitive accessibility, low vision, screen readers, AAC and accessible media;
- authentication, trust, privacy, financial, medical and other high-impact domains;
- AI/agent uncertainty, streaming, provenance, correction and autonomous action;
- editor/canvas workspaces, professional desktop workspaces and complex instrument architecture;
- external UI-source research, authority selection and safe adaptation;
- visual media opportunity mapping, sourcing, authoring and integration;
- product closure, route/action reachability and responsive capability preservation;
- rendered criticism, adequacy criticism and release verification;
- behavioral evaluation, mutation, ablation and empirical claim discipline.

The canonical bootstrap is:

```text
skills/using-nolane-ui/SKILL.md
```

The canonical graph is:

```text
skills/skill-graph.json
```

---

## Product completeness: broad before narrow

A major NUI rule is simple:

> **Think broadly before deciding what to omit.**

When a product is underspecified, NUI first discovers a plausible capability envelope and then dispositions capabilities as:

```text
REQUIRED
EXPECTED
OPTIONAL
EXCLUDED
UNKNOWN
```

This prevents the common AI failure where the first four obvious screens become the whole product.

A “full sales management platform,” for example, may need the agent to consider—not automatically implement—areas such as account/workspace lifecycle, roles and permissions, catalog/SKU, inventory, orders, fulfillment, returns/refunds, customers, payments, reporting, search, notifications, import/export, integrations, settings, audit/history and recovery.

The goal is **intentional scope**, not enterprise bloat.

---

## Professional tools should behave like professional tools

For editor-, IDE-, design-, media- and operations-class products, NUI reasons in terms of **instrument architecture**, not “more buttons.”

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

## Flagship visual intelligence

For `flagship`, `exceptional` and `experiential` work, NUI does not accept “premium, clean, modern” as proof of art direction.

High-ambition work must establish a visual thesis and explore **materially different candidates** across composition, type system, material system and signature mechanism. It then resolves:

- attention architecture;
- typographic voice and optical hierarchy;
- composition rhythm and density;
- color/material causality;
- motion purpose;
- domain-native signature;
- bounded reference frontier;
- generic-transfer resistance;
- responsive re-authoring;
- closed render/critique/correction cycles.

The point is not to mathematically prove beauty. The point is to make unsupported high-end visual claims **falsifiable**.

---

## Render first. Critique the thing users actually see.

NUI distinguishes a design specification from its rendered result.

A high-ambition workflow can require:

```text
render
→ screenshot / runtime observation
→ focal hierarchy critique
→ typography / spacing / density critique
→ platform-residue audit
→ responsive critique
→ correction
→ re-render
→ A/B comparison
```

This catches failures that source inspection alone misses: wrong wrapping, accidental scrollbars, browser defaults, optical misalignment, weak hierarchy, poor crops, cramped mobile states, inconsistent materials and motion that feels disconnected from the actual interaction.

---

## Modern interface residue audit

A polished product can still feel cheap when one low-level control falls back to accidental platform chrome.

NUI explicitly examines classes such as:

```text
scrollbars
selects
file inputs
date/time controls
number/range controls
focus / selection / caret
resize handles
drag ghosts
native validation UI
context menus
tooltips / popovers
cursors
overscroll behavior
```

The rule is **not** “customize everything.” Native controls can be correct. The failure is accidental residue, inconsistent styling, or customization that destroys usability/accessibility.

---

## References without cloning

NUI uses external design systems, products, research and UI libraries as **mechanism sources**, not trade-dress targets.

A reference may teach:

- density zoning;
- editorial scale contrast;
- command architecture;
- motion continuity;
- material layering;
- data treatment;
- platform behavior;
- accessibility semantics.

It does not become permission to reproduce a recognizable product aesthetic.

The source flow is:

```text
need
→ inspect current source
→ identify authority role
→ extract mechanism
→ define transfer boundary
→ adapt to local product truth
→ verify local runtime
```

---

## V10: Behavioral Design Intelligence & Empirical Proof

NUI v10 adds a second question after “is the repository structurally deep?”

> **Does using NUI actually change agent behavior in the intended direction?**

The V10 evaluation plane includes:

- **13 falsifiable behavioral hypotheses**;
- **48 benchmark tasks across 12 task families**;
- public-generation vs evaluator-hidden boundaries;
- semantic mutations, targeted ablations and placebo controls;
- model/runtime/prompt/tool-budget provenance;
- treatment-blind pairwise judging;
- matched comparison units;
- exact statistical gates;
- bounded promotion from structural evidence to empirical claims.

NUI does not collapse this into one “NUI score.” Product completeness can improve while another dimension does not. Those trade-offs should remain visible.

Repository-only CI currently supports a **structural evidence ceiling**. It does not pretend synthetic fixtures are proof that NUI is universally superior across real models.

---

## What NUI is not

NUI is not:

- a React component library;
- a Tailwind preset;
- a Figma kit;
- a single system prompt;
- a collection of trendy screenshots;
- an automatic accessibility certification service;
- a universal numerical beauty function;
- permission to copy Apple, Linear, Stripe, Canva, CapCut, VS Code or any other product;
- proof that every AI output becomes excellent just because NUI is present.

It is an attempt to build a **design cognition layer around an AI agent** and make that layer inspectable, routable and testable.

---

## Repository map

```text
skills/                         canonical design faculties
skills/skill-graph.json        routing / ownership graph
knowledge/                     authority, ontology, benchmark and evidence knowledge
schemas/                       typed evidence contracts
src/nolane_ui/                 deterministic routing / validation kernels
evals/                         adversarial and behavioral fixtures
benchmarks/v10/                V10 behavioral benchmark corpus
.adapters / bridges            thin agent-specific discovery surfaces
.agents/skills/nolane-ui/      Codex / Agent Skills bridge
.claude/skills/nolane-ui/      Claude Code bridge
scripts/nui-agent-export       agent projection CLI
scripts/nui-mcp-server         local MCP entry point
docs/AGENT-INTEGRATION.md      complete AI-agent setup guide
docs/research/                 research provenance and bounded synthesis
```

---

## Verify NUI

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

Repository validation proves structural and evidence-contract invariants for the checked revision. It does not, by itself, prove that a future interface is beautiful, usable, accessible, safe, lawful or empirically superior.

---

## License

MIT. See [`LICENSE`](LICENSE).

---

<div align="center">

### AI already knows how to generate UI.
### Nolane UI Intelligence is an attempt to make it learn how to **design, inspect and justify** one.

**Start:** [`skills/using-nolane-ui/SKILL.md`](skills/using-nolane-ui/SKILL.md) · **Agent setup:** [`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)

</div>