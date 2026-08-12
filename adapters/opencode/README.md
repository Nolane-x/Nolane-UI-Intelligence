# OpenCode adapter

Use this adapter to bind NUI's universal skill graph to OpenCode workspace, terminal, worker, and MCP capabilities available in the current environment.

## Skill discovery
Use the runtime's Agent Skills-compatible discovery mechanism and keep NUI skills as separate directories. Do not combine them into one prompt: the router must be able to load only selected faculties.

## Capabilities
Bind file/test/browser/screenshot/semantic-tree/subagent/component-registry capabilities only after they are actually available. Use `adapters/capabilities.json` fallbacks when a capability is missing.

## Critic isolation
Prefer an independent worker for each release-critical critic family. Supply the contract and evidence, not a persuasive summary from the generator.

## Completion
OpenCode's successful edit or command execution proves only that operation. NUI's completion gate still requires domain obligations, critics, evidence, and explicit bounds.
