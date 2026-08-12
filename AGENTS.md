# Agent instructions

When this repository is used as an Agent Skill pack:

1. For material UI/UX work, read `skills/using-nolane-ui/SKILL.md` before designing or implementing.
2. Follow the parent-child graph in `skills/skill-graph.json`; a child may strengthen but may not waive a parent obligation.
3. Use `routing-ui-work` to select task-relevant faculties. Do not load every skill by default.
4. Preserve the authority hierarchy in `nui.config.json` when guidance conflicts.
5. Treat absent evidence as UNKNOWN/BLOCKED, never PASS.
6. Do not claim material UI completion from compile/lint/render success alone.
7. Keep generative and critic roles logically separate. A critic records findings; it does not silently rewrite the artifact it is judging.
8. Use deterministic validators for deterministic facts. Do not substitute model confidence for a validator result.
9. Do not bulk-copy third-party skill text into this repository. Synthesize mechanisms and record sources in `docs/research/SOURCES.md`.
10. Completion claims must name their bounds and unverified areas.

These rules are repository policy. Runtime adapters may change tool syntax, not these semantics.
