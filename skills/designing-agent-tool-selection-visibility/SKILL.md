---
name: designing-agent-tool-selection-visibility
description: Show tool choice and capability boundaries when they matter to trust, cost, side effects, or result quality without forcing users to manage every low-level invocation.
---

# Designing agent tool selection visibility

Agents may choose among browsers, code runners, databases, email, search, internal APIs, or external services. Use this skill when users need enough visibility to understand how results were produced or which systems are about to be touched.

## Decision ownership

Own which tool selections are surfaced, at what granularity, whether users can override them, and how cost, data exposure, permissions, or quality tradeoffs are communicated. Decide when tool identity is operationally material versus implementation detail.

## Inputs and evidence

Collect available tools, side effects, data destinations, pricing, latency, reliability, provider constraints, permission scopes, and user expectations. Identify tools whose use changes privacy posture or commits external state.

## Procedure

Surface tool intent at meaningful boundaries: “search public web,” “query production database read-only,” or “send through Gmail” is often more useful than internal function names. Explain selection when alternatives have material tradeoffs. Allow users to prohibit tools or select a preferred class when policy permits.

During execution, show tool status for long-running or high-impact calls. After completion, retain a compact provenance trail connecting important outputs to tools used.

Do not expose noisy internal routing that users cannot act on.

## Failure topology

Invisible tool choice can surprise users when private data leaves a local context. Overexposure turns the UI into an execution log. Another failure is presenting tool choice as user-configurable when the agent ignores the preference or silently falls back to a disallowed provider.

Tool names can also imply stronger authority than the actual scope, such as “GitHub” when only public search is available.

## Falsification

Run tasks with equivalent tools that differ in privacy, cost, and side effects. Verify material choices are visible and preference constraints are honored. Block a preferred tool and inspect fallback messaging. Ask users what systems received their data after completion.

## Output contract

Produce an `agent-tool-selection-visibility-contract` defining materiality criteria, user-facing tool labels, pre/during/post visibility, override and prohibition semantics, fallback disclosure, cost/privacy cues, and provenance linkage.

## Handoffs

Use `designing-agent-permission-escalation` for access, `designing-agent-result-provenance` for output lineage, `designing-agent-action-progress` for long-running calls, and privacy specialists for provider/data-boundary communication.