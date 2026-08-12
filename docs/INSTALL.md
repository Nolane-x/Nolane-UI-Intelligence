# Installation

Nolane UI Intelligence is a repository-level Agent Skill system. The universal core does not require a particular JavaScript framework, design tool, or model vendor.

## Recommended: project-scoped installation

Clone or vendor this repository into a stable project location, then make the runtime's project instructions point to:

`skills/using-nolane-ui/SKILL.md`

For UI work, the bootstrap routes into `skills/skill-graph.json`. Keep skill directories separate; do not concatenate all `SKILL.md` files into one prompt.

## Cross-runtime Agent Skills installation

For runtimes that support the common Agent Skills directory convention, expose individual `skills/<name>/` directories under the runtime's scanned skills root (commonly a project or user `.agents/skills/` location). Keep the NUI repository available so shared graph/config/schemas remain inspectable.

A symlink-based installation is preferable during development because updating the repository updates every skill without duplicating content.

## Runtime adapters

Read the matching adapter after the bootstrap:

- `adapters/generic/README.md`
- `adapters/codex/README.md`
- `adapters/claude-code/README.md`
- `adapters/gemini-cli/README.md`
- `adapters/cursor/README.md`
- `adapters/opencode/README.md`

Adapters translate capabilities. They do not weaken NUI policy. If an adapter says browser inspection is unavailable, the correct result is a narrower/blocked verification claim—not an imagined browser result.

## Validate the installation

From the repository root:

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

The validator uses Python's standard library only. Python 3.10+ is the project floor.

## Optional project tools

NUI can use, but does not require, browser automation, Storybook, Playwright, accessibility tooling, Figma/design sources, component registries/MCPs, screenshot tools, or independent workers. Bind only capabilities that really exist in the current runtime/project.

## Updating

Treat NUI like code: update on a branch, run the test suite and validator, review changed skill contracts/evals, then merge. A skill wording change can alter agent behavior even when no Python code changes.
