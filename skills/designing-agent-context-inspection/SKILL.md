---
name: designing-agent-context-inspection
description: Let users inspect the active context an agent can draw from so hidden files, messages, memories, and selections do not silently steer results.
---

# Designing agent context inspection

Agents may operate over files, conversation history, selected records, web pages, memories, or project state. Use this skill when users need a trustworthy picture of what information is currently in scope.

## Decision ownership

Own context inventory, grouping, provenance, inclusion/exclusion visibility, freshness indicators, and the level of detail users can inspect. Decide how to represent implicit context such as workspace defaults or retrieved memory.

## Inputs and evidence

Collect all context sources, retrieval layers, attachment semantics, current selection, token/window limits, summarization, stale-cache behavior, and permission boundaries. Identify context that is included automatically without an obvious UI representation.

## Procedure

Expose context as an inspectable set of sources with meaningful labels, scope, and status. Distinguish explicitly attached items from automatically retrieved or inherited context. Indicate when only a summary or excerpt is available rather than the full source.

Show freshness and version where relevant, especially for mutable files or records. Allow users to trace outputs back to source context through provenance rather than dumping raw prompt internals.

Keep sensitive context visibility appropriate to access rights.

## Failure topology

A simple “3 files attached” label hides which versions or sections were used. Showing raw tokenized prompt content overwhelms users and may expose internal implementation. Another failure is silently dropping earlier context due to limits while the UI still implies it is active.

Stale context can produce confident answers about files that have since changed.

## Falsification

Change a source after it is added and verify freshness indicators. Exceed context limits and observe how evicted or summarized material is represented. Compare user-visible inventory against actual retrieval traces. Remove a context item and confirm subsequent execution no longer uses it.

## Output contract

Produce an `agent-context-inspection-contract` defining source categories, inclusion status, provenance, freshness/version representation, summarized/partial states, eviction visibility, and tests matching visible context to actual agent inputs.

## Handoffs

Use `designing-agent-context-editing` for changing active context, `designing-agent-memory-controls` for persistence, `designing-agent-result-provenance` for output linkage, and file/data privacy skills for sensitive sources.