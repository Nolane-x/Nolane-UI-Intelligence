# Gemini CLI adapter

NUI uses Gemini CLI as an execution runtime, not as a different design policy.

## Discovery
Install the skill graph in a Gemini/Agent-Skills-compatible path used by the current runtime, or reference the repository bootstrap from project instructions. Keep `skills/skill-graph.json` intact so routing remains portable.

## Capability mapping
Use native workspace and shell actions for file/test obligations. Bind browser/Chrome, screenshot, semantic-tree, component-registry, and worker capabilities only when configured and visible to the current session.

## Review separation
If worker/subagent execution is available, run critic skills in fresh contexts. Otherwise perform a logically separated review and mark the reduced independence in evidence.

## Completion
Gemini output that predicts a test/browser result is not evidence. Only executed commands/captures close deterministic/runtime obligations.
