---
name: designing-agent-memory-controls
description: Give users understandable control over what agent memory stores, reuses, edits, forgets, and scopes across conversations, projects, and accounts.
---

# Designing agent memory controls

Memory changes future behavior, so it is a persistent product state rather than an invisible convenience. Use this skill when an agent can retain preferences, facts, project context, or interaction history beyond the immediate session.

## Decision ownership

Own memory visibility, scope, save triggers, user consent, editing/deletion, retention, conflict handling, and distinction between ephemeral context and persistent memory. Decide what categories should never be stored automatically.

## Inputs and evidence

Collect memory types, storage duration, data sensitivity, project/account boundaries, retrieval triggers, privacy policy, user corrections, and cases where stale memory caused wrong behavior. Inspect actual stored representations and not only friendly summaries.

## Procedure

Make persistence legible at the moment it matters. Allow users to inspect remembered items, their scope, and why they were saved. Provide edit and forget controls with predictable effect. Distinguish “use in this conversation,” “remember for this project,” and “remember across account” where those scopes exist.

When new information conflicts with stored memory, avoid silently accumulating contradictory facts. Ask or apply documented precedence based on recency/source authority. Sensitive data should require stronger justification and retention controls.

## Failure topology

Invisible memory makes surprising personalization feel creepy or incorrect. A single global memory pool leaks context across projects. Another failure is deleting a visible summary while hidden embeddings or derived records continue to influence retrieval.

Users may also be unable to tell whether a bad answer came from stale memory or current context.

## Falsification

Save, edit, scope, and delete representative memories, then run future tasks that would retrieve them. Cross project/account boundaries and verify isolation. Introduce conflicting updates and inspect resolution. After deletion, verify downstream retrieval and derived indexes no longer influence behavior according to policy.

## Output contract

Produce an `agent-memory-controls-contract` defining memory classes, scopes, save/consent rules, inspection/edit/delete behavior, conflict resolution, retention, sensitive-data policy, and end-to-end retrieval/deletion tests.

## Handoffs

Use `designing-agent-context-inspection` for current-session context, `designing-agent-context-editing` for active context changes, privacy-control skills for data rights, and `designing-agent-result-provenance` when outputs rely on remembered facts.