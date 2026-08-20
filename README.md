<div align="center">

# Nolane UI Intelligence

### Design cognition, product completeness, visual craft and evidence-gated verification for AI agents

**AI can generate an interface in seconds. NUI is built to make it think like a serious product/design team before it ships one.**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `374 canonical skills` · `9 agent projections` · `MCP + CLI` · `evidence-gated` · `MIT`

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

## 374 canonical design faculties

NUI currently preserves **374 canonical skills**. The number is descriptive, not a license to create overlapping experts. The long-term UI-industry roadmap targets broader coverage toward 1,000 canonical faculties while preserving distinct decision ownership and minimal routing.

A skill is allowed to exist only when it owns a distinct decision or failure class. NUI deliberately avoids turning every new idea into another overlapping “expert.” Batch 001 added 100 independently authored specialists across motion, rich controls, direct manipulation, spreadsheet/data interaction, enterprise workflows, billing, scheduling, geospatial interaction and historical state. Batch 002 adds 100 more independently authored specialists across high-friction input, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations, and trust/account lifecycle. See [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) and [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) for exact inventories, ownership, provenance and non-generation constraints.
