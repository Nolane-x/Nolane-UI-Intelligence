# Agent Onboarding & Discoverability Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Nolane UI Intelligence immediately understandable, discoverable, and practically usable from major AI-agent harnesses without creating duplicate NUI skill bodies or vendor-specific forks.

**Architecture:** Keep one canonical NUI graph under `skills/`; expose it through thin host bridges and a provider-neutral export plan. README onboarding explains the same canonical path in English, Vietnamese, and Simplified Chinese. GitHub metadata describes NUI as an AI-agent design cognition/evaluation system rather than a component library.

**Tech Stack:** Python 3.12, Markdown, JSON, GitHub Actions, existing NUI interoperability kernel.

## Global Constraints

- Preserve exactly 174 canonical skills; do not duplicate skill bodies for vendors.
- Host permissions remain authoritative; NUI adapters never expand filesystem, shell, network, browser, image, or MCP permissions.
- Agent onboarding must be backed by executable repository paths, not aspirational README-only claims.
- README language versions must preserve the same technical facts while using natural local prose.
- Existing V10 empirical claim ceiling remains evidence-gated; onboarding must not imply empirical superiority that has not been measured.

---

### Task 1: Synchronize the agent interoperability surface

**Files:**
- Modify: `src/nolane_ui/interop.py`
- Modify: `scripts/nui-agent-export`
- Test: `tests/test_v10_agent_onboarding.py`

**Interfaces:**
- Produces: `SUPPORTED_AGENT_IDS`, `build_agent_install_plan(agent_id, root)` for Codex, Claude Code, Google Antigravity, Gemini CLI, OpenCode, Cursor-compatible, VS Code-agent-compatible, generic MCP, and generic CLI.

- [ ] Write a failing test asserting every adapter declared by `knowledge/agent-interop-v8.json` has a valid export plan and that the CLI uses the same supported ID set.
- [ ] Run the focused test and confirm the current registry/CLI mismatch fails.
- [ ] Add one canonical supported-agent tuple and complete host projections without duplicating canonical skill content.
- [ ] Run focused tests until green.

### Task 2: Add executable agent onboarding documentation

**Files:**
- Create: `docs/AGENT-INTEGRATION.md`
- Modify: `README.md`
- Modify: `README-VN.md`
- Modify: `README-CN.md`
- Test: `tests/test_v10_agent_onboarding.py`

**Interfaces:**
- Documents: clone/download path, canonical bootstrap, Codex bridge, Claude Code bridge, generic MCP command, generic CLI export command, and projections for Gemini CLI/OpenCode/Cursor/VS Code agents.

- [ ] Write failing documentation tests requiring `Use with your AI agent`/localized equivalents, Codex, Claude Code, Gemini CLI, OpenCode, Cursor, VS Code, MCP, and `scripts/nui-agent-export` references.
- [ ] Run focused test and confirm failure before prose changes.
- [ ] Write concise top-level onboarding plus a deeper integration guide with copy/paste-safe commands that invoke repository-owned scripts only.
- [ ] Keep vendor-specific instructions bounded to NUI-owned bridge files and state that current host syntax may need live verification where registry marks it high drift.
- [ ] Run focused tests until green.

### Task 3: Improve repository discovery metadata

**Files:**
- No repository source file required unless connector metadata writes are unavailable.

**Metadata:**
- Description: concise positioning around design cognition, UI/UX verification, and AI agents.
- Topics: `ai-agents`, `agent-skills`, `ui-ux`, `design-system`, `design-intelligence`, `codex`, `claude-code`, `mcp`, `frontend`, `accessibility`, `human-computer-interaction`, `ai-coding`.

- [ ] Inspect connector support for repository description/topics mutation.
- [ ] Apply metadata only through an authenticated GitHub repository mutation; do not fake topics inside README as a substitute.
- [ ] Re-fetch repository metadata to verify the resulting description/topics. If mutation is unsupported by the connector, record the limitation and keep the README keyword block.

### Task 4: Full verification and integration

**Files:**
- Validate all changed files.

- [ ] Run `python -m unittest discover -s tests -v` through GitHub CI.
- [ ] Require fresh completion packet, exact-revision repository validation, and V10 package upload to pass.
- [ ] Review branch diff for README claims that are not backed by repository files.
- [ ] Fast-forward `main` only when branch CI is green and branch is ahead with no divergence.
- [ ] Run GitHub Actions again on the final `main` SHA and verify V10 artifacts are generated from that SHA.
