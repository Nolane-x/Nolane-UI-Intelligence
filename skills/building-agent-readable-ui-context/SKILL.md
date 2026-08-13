---
name: building-agent-readable-ui-context
description: Use when current UI knowledge is exposed through MCP, llms.txt, agent skills, structured documentation, code registries, or other machine-readable adapters and an agent needs compact trustworthy context for implementation.
---

# Building Agent-Readable UI Context

## Parent Contract
**Required parent:** `performing-ui-repository-archaeology`.

Receive resolved source identity, role, intended usage, pinned/currentness requirements, inspected artifacts, authority route and task-specific decision questions. Archaeology establishes what the source is; this skill creates a live retrieval interface for the next agent.

## Access-Mode Neutrality
Enforce **access-mode neutrality**: MCP, llms.txt, an official skill, open code, or a structured API makes a source easier to query, not more authoritative. Store `authority_escalation: false` in every adapter. Resolve authority through `routing-to-ui-authorities` separately.

## Live-Source Hydration
Prefer **live-source hydration**: retrieve only the docs/API/example slices needed for the current decision from the current upstream. Pin version/ref where the source drifts or where generated docs correspond to releases. Cache identity and provenance, not a giant copied corpus that becomes stale and legally ambiguous.

## Agent Context Budget
Allocate an **agent context budget**. Include: decision question, target version/platform, authoritative snippet/path handles, exact API/behavior facts needed, constraints/contraindications, and a verification command or retrieval handle. Exclude marketing prose, unrelated component catalogs, screenshots with no mechanism, and redundant examples.

A good adapter can answer “what does the current Primer dialog guidance require?” or “what props does this Mantine component expose?” without loading the entire design system. It cannot answer “what should our product be?” unless that is within the underlying source's authority.

## Provenance and Drift
Every hydrated item keeps source ID, canonical URL, retrieval time, version/ref if available, access mode and underlying authority. Generated LLM docs that update every release are still currentness-sensitive. A tool response without version identity can be useful but must not silently overwrite pinned project reality.

## Output — `agent-readable-ui-context`
Return `source`, `underlying_authority`, `access_mode`, `decision_question`, `hydrated_items[] {claim, source_handle, version, retrieved_at}`, `context_budget`, `excluded_noise[]`, `verification_next_step`, `staleness_trigger`, and `authority_escalation:false`.

## Falsification
Disable the MCP/skill adapter and inspect the underlying documentation/source. If the substantive authority claim disappears, the system confused protocol with evidence. Replay the cached context against a newer release; material API mismatch proves stale-context risk.

## Recovery
Refresh from canonical upstream, reduce context to the unresolved decision, preserve pinned project versions, and demote unavailable adapters to manual retrieval. If license/access boundaries prevent durable caching, store only pointers and local derived decisions.

## Hard gate
**Machine-readable context may accelerate execution only when the underlying authority, live/pinned source identity, context budget, provenance and staleness trigger are explicit; no adapter protocol grants authority by itself.**
