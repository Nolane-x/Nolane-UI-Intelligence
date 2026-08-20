---
name: designing-agent-context-editing
description: Let users add, remove, replace, pin, or constrain agent context without losing track of what changed or accidentally broadening scope.
---

# Designing agent context editing

Once users can inspect context, they need safe ways to correct it. Use this skill when tasks depend on selecting files, records, memories, conversation ranges, branches, folders, or other information sources.

## Decision ownership

Own context-edit operations, scope controls, pinning, replacement semantics, change visibility, and interaction with in-flight work. Decide whether context edits affect only future steps or invalidate an existing plan/result.

## Inputs and evidence

Collect context source types, hierarchical scopes, selection sizes, freshness, running-task dependencies, token limits, and user correction patterns. Identify high-risk broadening actions such as replacing one file with an entire repository or one customer record with a full database.

## Procedure

Provide explicit add/remove/replace operations with previews for hierarchical scope. Show the resulting context set after each edit. Allow pinning important context against automatic eviction where supported, but communicate capacity tradeoffs.

If context changes materially during execution, mark dependent plan steps or outputs stale and ask whether to re-evaluate. Preserve prior context history for audit without silently reusing removed items.

Offer narrow selection tools before broad wildcard inclusion.

## Failure topology

Removing a visible attachment while cached summaries remain active violates user expectation. Broad folder selection can accidentally include secrets. Another failure is editing context after a plan preview while the agent proceeds under assumptions formed from the old set.

Automatic context optimization may override user pinning without disclosure.

## Falsification

Add/remove nested scopes, pin items, exceed capacity, and edit context mid-run. Verify actual retrieval reflects the new set. Introduce a plan dependency on a removed file and ensure the system marks it invalid or recomputes. Test secret-containing subfolders and permission boundaries.

## Output contract

Produce an `agent-context-editing-contract` defining supported edits, hierarchy previews, pinning/eviction precedence, in-flight invalidation, history/audit behavior, sensitive-scope safeguards, and end-to-end retrieval tests.

## Handoffs

Use `designing-agent-context-inspection` for visibility, `designing-agent-memory-controls` for persistent information, `designing-agent-plan-previews` when edits change execution, and permission/privacy skills for protected sources.