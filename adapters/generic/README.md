# Generic Agent Skills adapter

Use this adapter when the runtime can discover Agent Skills but no runtime-specific binding is available.

## Binding rule
Load `skills/using-nolane-ui/SKILL.md`, then obey `skills/skill-graph.json`. Treat every tool operation as a capability, not a named vendor command. Before routing, inventory which capabilities in `adapters/capabilities.json` are actually available.

## Evidence rule
A capability description is not evidence that the runtime has it. Only bind an obligation to a capability after the current runtime exposes a tool or the user supplies an artifact. If browser/screenshot/semantic-tree execution is absent, narrow the completion claim instead of simulating an observation in prose.

## Critic independence
Prefer a fresh-context worker for critic skills. If unavailable, clear implementation-centric assumptions, re-load only the contract/artifact/critic skill, and mark independence as degraded in evidence.

## Framework neutrality
The generic adapter never chooses React, Tailwind, Figma, shadcn, Storybook, Playwright, or another implementation stack solely because NUI exists. Route based on the project and task; external tools are oracles/adapters, not the UI architecture.
