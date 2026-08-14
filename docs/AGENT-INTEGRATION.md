# Use Nolane UI Intelligence with AI agents

Nolane UI Intelligence is designed to travel **with the repository that an agent is working on**. It does not require a vendor-specific fork of the 174-skill graph. The canonical entry point always remains:

```text
skills/using-nolane-ui/SKILL.md
```

From there NUI routes through `skills/nolane-ui/SKILL.md` and loads only the owners required by the task. Native bridges, MCP and CLI are discovery/invocation surfaces; they do not become design authority.

## Choose an integration mode

There are three useful modes. Pick the smallest one your host supports.

| Mode | Best for | What the agent receives |
|---|---|---|
| Native project-skill bridge | Codex, Claude Code, Agent-Skills-compatible hosts | A tiny host-visible bridge that points to the canonical NUI bootstrap |
| MCP sidecar | Any host with local MCP support | A bounded local NUI server over stdio/host configuration |
| CLI/repository mode | Shell-capable agents, CI, editors without native skill discovery | An explicit agent plan plus repository validation commands |

**Security boundary:** host permissions remain authoritative. NUI never grants itself broader shell, network, filesystem, browser, image or MCP access than the host already allows.

---

## 1. Get NUI

### Option A — clone NUI as the repository you are working in

```bash
git clone https://github.com/Nolane-x/Nolane-UI-Intelligence.git
cd Nolane-UI-Intelligence
```

This is the easiest mode for evaluating or developing NUI itself. Codex and Claude Code can discover the native bridges already present in the repository.

### Option B — keep NUI as a sidecar inside another project

From your product repository:

```bash
git clone --depth 1 https://github.com/Nolane-x/Nolane-UI-Intelligence.git .nui
```

Then query the adapter plan you want:

```bash
python .nui/scripts/nui-agent-export --agent openai-codex --root .nui
```

or run NUI as a local MCP sidecar:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

Sidecar mode avoids copying 174 skill bodies into your product repository. Configure the MCP command in the **current syntax of your host**. Host configuration formats change faster than the NUI cognition graph, so NUI intentionally does not freeze vendor configuration JSON into its canonical contract.

---

## 2. Codex

NUI ships a thin Codex/Open-Agent-Skills-compatible bridge at:

```text
.agents/skills/nolane-ui/SKILL.md
```

and repository policy at:

```text
AGENTS.md
```

When NUI is present at repository root, the bridge tells Codex to read the canonical bootstrap instead of duplicating it. Inspect the generated integration plan with:

```bash
python scripts/nui-agent-export --agent openai-codex
```

For a product repository using `.nui` sidecar mode, MCP is the cleanest portable boundary:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

The important invariant is not the host syntax. It is that Codex reaches the **same canonical NUI graph** and that host sandbox/approval policy remains in control.

---

## 3. Claude Code

Claude Code has a dedicated thin project bridge:

```text
.claude/skills/nolane-ui/SKILL.md
```

Inspect the plan:

```bash
python scripts/nui-agent-export --agent claude-code
```

The bridge points to `skills/using-nolane-ui/SKILL.md`; it does not contain a second copy of the design system. If Claude Code is operating on a separate product repository, use NUI as a `.nui` sidecar and expose the local MCP server through the current Claude Code MCP configuration.

---

## 4. Google Antigravity

NUI exposes the Open Agent Skills bridge:

```text
.agents/skills/nolane-ui/SKILL.md
```

Generate the plan:

```bash
python scripts/nui-agent-export --agent google-antigravity
```

Antigravity integration is intentionally treated as a high-drift host surface. Use the bridge when the current workspace supports Agent Skills; otherwise use the local MCP/CLI projection.

---

## 5. Gemini CLI

Gemini CLI uses the provider-neutral path in NUI rather than a duplicated Gemini-specific skill graph:

```bash
python scripts/nui-agent-export --agent gemini-cli
```

For a product-sidecar install:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

Wire that stdio command through Gemini CLI's **current** MCP/project-context mechanism. NUI keeps the command stable and leaves vendor configuration syntax to the host.

---

## 6. OpenCode

Generate the OpenCode projection:

```bash
python scripts/nui-agent-export --agent opencode
```

NUI deliberately uses repository context + CLI/MCP instead of maintaining an OpenCode copy of every skill. In sidecar mode:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

Verify the current OpenCode host configuration before wiring the command because integration syntax can drift independently of NUI.

---

## 7. Cursor

For Cursor-compatible agent workflows:

```bash
python scripts/nui-agent-export --agent cursor-compatible
```

Use repository instructions plus the current MCP/agent integration surface. NUI remains inside the repository or `.nui` sidecar; Cursor receives the relevant routed knowledge rather than a huge static prompt.

---

## 8. VS Code / Copilot-compatible agent hosts

For VS Code-agent-compatible workflows:

```bash
python scripts/nui-agent-export --agent vscode-agent-compatible
```

Connect repository guidance and, where supported, the NUI MCP sidecar. Workspace trust, extension permissions and tool approval remain owned by VS Code/the installed agent host.

---

## 9. Any MCP-compatible AI agent

This is the most portable route when a host is not explicitly named above.

Start NUI:

```bash
python scripts/nui-mcp-server
```

or from sidecar mode:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

The server is local and bounded. The MCP host decides whether to connect, which tools/resources are exposed, and what the model may invoke.

Inspect the generic projection:

```bash
python scripts/nui-agent-export --agent generic-mcp
```

---

## 10. Any shell/CLI-capable AI agent

If an agent can read files and execute local commands, it can use NUI without native skill or MCP support.

```bash
python scripts/nui-agent-export --agent generic-cli
python scripts/nui-validate .
```

Then instruct the agent to start at:

```text
skills/using-nolane-ui/SKILL.md
```

and route through:

```text
skills/nolane-ui/SKILL.md
```

Do **not** preload all 174 skills. NUI's router is designed to activate the smallest sufficient ownership graph for the task.

---

## Supported adapter IDs

The CLI and the interoperability registry share one executable supported set:

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

You can inspect any projection as JSON:

```bash
python scripts/nui-agent-export --agent <adapter-id>
```

That JSON describes the canonical bootstrap, project files, recommended mode, MCP command, CLI command, validation command, permission boundary and copy policy.

---

## What should be copied — and what should not

**Copy or expose:**

- the thin host bridge, when your host has a native skill surface;
- the canonical NUI repository or `.nui` sidecar;
- the MCP/CLI invocation required by the host;
- your product-specific design evidence and task profile.

**Do not copy:**

- all 174 skill bodies into one giant system prompt;
- a vendor-specific fork of NUI unless you are intentionally maintaining a fork;
- external design prompts or skill packs as trusted authority without NUI's provenance/review boundary;
- host permissions into NUI. Permission remains a host concern.

The architecture is intentionally **one cognition system, many thin projections**.

---

## A good first prompt

Once NUI is reachable by your agent, you do not need a long magic incantation. A useful request is simply specific about product intent and ambition:

```text
Use Nolane UI Intelligence for this task. Design and implement the product as a real production interface, not a demo. Preserve product completeness, route the necessary specialist skills, explore materially different visual directions where ambition requires it, inspect the rendered result, critique it, and do not claim completion without the evidence required by NUI.
```

NUI should then decide which owners are relevant. The user should not have to manually enumerate typography, settings, responsive behavior, accessibility, motion, authentication, product scope, media, or every other possible concern.

---

## Verify the NUI checkout

Before blaming the agent integration, verify the NUI repository itself:

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

A passing repository validator proves NUI's structural/evidence contracts for that revision. It does **not** prove that a future generated interface is automatically beautiful, accessible, usable, lawful, or empirically superior. Those claims remain task- and evidence-specific.
