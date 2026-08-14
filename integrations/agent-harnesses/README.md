# NUI agent harness integrations

NUI keeps one canonical skill graph. Use the smallest native bridge:

- **Codex:** `.agents/skills/nolane-ui/SKILL.md` + root `AGENTS.md`; use `scripts/nui-agent-export --agent openai-codex` to inspect the bounded plan.
- **Claude Code:** `.claude/skills/nolane-ui/SKILL.md` + root `AGENTS.md`; use `--agent claude-code`.
- **Google Antigravity:** `.agents/skills/nolane-ui/SKILL.md` + repository context; use `--agent google-antigravity`.
- **MCP hosts:** install optional dependency `pip install -e '.[mcp]'`, then run `python scripts/nui-mcp-server`. The server only exposes bounded local NUI read/analysis tools.
- **Any shell/CI agent:** use `scripts/nui-agent-export`, `scripts/nui-validate`, source plans/audits and the canonical skill files directly.

Do not paste all NUI skills into vendor config. Do not grant network/shell/browser permissions merely because an adapter can describe them.
