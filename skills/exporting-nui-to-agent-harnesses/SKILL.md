---
name: exporting-nui-to-agent-harnesses
description: Use when loss-minimized, permission-preserving exposure of canonical NUI to vendor agent skill roots, MCP hosts and generic CLI callers without duplicating the knowledge graph
---

# Exporting NUI to Agent Harnesses

## Parent Contract
**Required parent:** `building-agent-readable-ui-context`.

`building-agent-readable-ui-context` supplies the compact provenance-preserving NUI context. This owner changes only host discovery/invocation surfaces and must preserve that parent context byte-for-meaning, not fork it.

## Decision Boundary
Own *how* an agent discovers and invokes NUI. Do not own UI decisions and do not fork canonical NUI content for each vendor. The output is an `agent-harness-export-plan`.

## Portable Agent Model
Start from the **canonical knowledge spine**: `skills/using-nolane-ui/SKILL.md`, the canonical graph, knowledge registries and validators. A **thin harness bridge** may translate discovery metadata or command invocation, but it may not rewrite product rules. Preserve **discovery-path fidelity**: record whether the host discovers `.agents/skills`, `.claude/skills`, MCP, repository instructions, or only a process CLI.

Treat **host permission sovereignty** as non-negotiable. NUI never grants itself shell, network, browser, filesystem or MCP permissions. An adapter describes required capabilities and degrades evidence to UNKNOWN when a host does not expose them. Add an **adapter drift sentinel**: vendor-specific paths and commands are live facts, so pin documentation evidence or require re-verification instead of assuming yesterday's convention.

## Installation Algorithm
1. Detect the host only from explicit runtime facts or user choice; never infer from model identity alone.
2. Select the smallest bridge that the host natively supports. Prefer one canonical project skill plus repository policy; use MCP when structured tool/resource access materially helps; use CLI as the universal fallback.
3. Resolve all bridge pointers relative to repository root and verify the canonical targets exist.
4. Emit a capability matrix: discovery, read, write, shell, network, browser/render, MCP, image generation/editing. Mark each `available`, `denied`, or `unknown`.
5. Never bulk-copy all 174 skill bodies into a vendor directory. Progressive disclosure is part of NUI's correctness model.
6. Verify the bridge by invoking a harmless status/route operation and checking that the host reaches the canonical files.

## Decision Model
Decide host identity → verify current discovery surface → map capability/permission matrix → choose smallest bridge → validate canonical pointers → probe a harmless route → record drift trigger.

## Evidence
Require primary host documentation or executable discovery evidence, canonical target existence, capability status, bridge-file diff, and a probe showing the host reaches canonical NUI without copied product rules.

## Output Contract
Emit `agent-harness-export-plan` with host id, verified discovery roots, project bridge files, canonical targets, capability matrix, MCP/CLI fallback, permission boundary, verification probe and drift trigger.

## Failure Traps
Duplicated canonical corpus; guessed vendor path; bridge self-grants permissions; unsupported write/MCP claim; silent fallback that drops evidence; vendor upgrade changes discovery root.

## Falsification
Move the canonical bootstrap, revoke network, or swap the host from Codex to Claude Code. The plan must either update the bridge/path/capability state or fail. If it continues to claim full capability, the adapter is stale.

## Recovery
Remove vendor-specific duplicated prose, restore canonical pointers, refresh the adapter registry from primary documentation, then rerun bridge discovery and a bounded route probe before material UI work resumes.
